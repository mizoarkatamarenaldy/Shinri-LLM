#!/usr/bin/env python3
"""
Shinri-LLM - MBTI Pilot Experiment (Fase 1)
Menguji apakah model Gemini Flash-Lite memberikan jawaban MBTI
yang berbeda dan konsisten saat diberi persona INTJ dan ESFP.
"""

import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

# Memastikan output konsol tidak error pada encoding non-UTF-8 (seperti cp932 di Windows)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Path konfigurasi
REPO_ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_PATH = REPO_ROOT / "experiments" / "mbti" / "gemini-flash-lite" / "questions.json"
RESULTS_DIR = REPO_ROOT / "results" / "mbti" / "gemini-flash-lite"
ANSWERS_PATH = RESULTS_DIR / "answers.csv"
SUMMARY_PATH = RESULTS_DIR / "summary.json"
ENV_PATH = REPO_ROOT / ".env"

# Parameter eksperimen
DEFAULT_MODEL_ID = "gemini-3.5-flash-lite"
PROVIDER = "google"
SETTINGS = "default"
PERSONAS = ["INTJ", "ESFP"]
REPEATS_PER_QUESTION = 3
DELAY_SECONDS = float(os.environ.get("API_DELAY_SECONDS", "4.0"))


def load_api_key(env_path: Path) -> str:
    """
    Membaca GEMINI_API_KEY dari .env.
    Berhenti dan laporkan jika file atau key tidak ditemukan.
    """
    if not env_path.exists():
        print(f"Error: File .env tidak ditemukan di {env_path}.", file=sys.stderr)
        print("Silakan buat file .env dan isi GEMINI_API_KEY=<key>.", file=sys.stderr)
        sys.exit(1)

    api_key = None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if "=" in stripped:
                k, v = stripped.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                if k == "GEMINI_API_KEY":
                    api_key = v
                    break

    if not api_key:
        print("Error: Variabel GEMINI_API_KEY tidak ditemukan atau kosong di file .env.", file=sys.stderr)
        sys.exit(1)

    return api_key


def load_questions(questions_path: Path) -> list:
    """Membaca berkas daftar pertanyaan pengujian."""
    if not questions_path.exists():
        print(f"Error: Berkas pertanyaan tidak ditemukan di {questions_path}.", file=sys.stderr)
        sys.exit(1)

    with open(questions_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    if len(questions) != 10:
        print(f"Peringatan: Jumlah pertanyaan adalah {len(questions)}, diharapkan 10.", file=sys.stderr)

    return questions


def call_gemini_api(api_key: str, model_id: str, persona: str, question: dict) -> str:
    """
    Memanggil Gemini API via REST generateContent.
    System instruction mengatur persona. Pengaturan generasi default.
    """
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }

    system_text = f"Kamu adalah seseorang dengan tipe kepribadian {persona}. Jawab semua pertanyaan sebagai orang itu."

    user_prompt = (
        f"Pertanyaan: {question['scenario']}\n\n"
        f"A. {question['option_a']}\n"
        f"B. {question['option_b']}\n\n"
        f"Jawab hanya dengan huruf A atau B."
    )

    payload = {
        "system_instruction": {
            "parts": [{"text": system_text}]
        },
        "contents": [
            {
                "parts": [{"text": user_prompt}]
            }
        ]
    }

    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=req_data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read().decode("utf-8")
            data = json.loads(resp_body)
    except urllib.error.HTTPError as e:
        err_msg = ""
        try:
            err_json = json.loads(e.read().decode("utf-8"))
            err_msg = err_json.get("error", {}).get("message", str(e))
        except Exception:
            err_msg = str(e)

        if e.code in (401, 403):
            print(f"Error Otentikasi (HTTP {e.code}): {err_msg}", file=sys.stderr)
            print("Eksperimen dihentikan. Periksa validitas GEMINI_API_KEY di .env.", file=sys.stderr)
            sys.exit(1)
        elif e.code == 429:
            print(f"Error Kuota / Rate Limit (HTTP 429): {err_msg}", file=sys.stderr)
            print("Eksperimen dihentikan. Jangan coba model atau provider lain.", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"Error API (HTTP {e.code}): {err_msg}", file=sys.stderr)
            sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error Jaringan: {e.reason}", file=sys.stderr)
        sys.exit(1)

    # Parsing teks jawaban dari response
    candidates = data.get("candidates", [])
    if not candidates:
        print("Error: Tidak ada candidates dalam respon API.", file=sys.stderr)
        return ""

    candidate = candidates[0]
    parts = candidate.get("content", {}).get("parts", [])
    raw_text = ""
    for part in parts:
        if not part.get("thought", False) and "text" in part:
            raw_text = part["text"]
            break
    if not raw_text and parts:
        for part in reversed(parts):
            if "text" in part:
                raw_text = part["text"]
                break

    cleaned = raw_text.strip()
    if cleaned.upper() in ("A", "B"):
        return cleaned.upper()
    else:
        # Dicatat apa adanya sebagai tidak valid
        return cleaned


def compute_summary(records: list, questions: dict) -> dict:
    """
    Membuat ringkasan:
    - Jumlah jawaban A dan B per persona per dimensi
    - Konsistensi 3 ulangan per pertanyaan
    Ringkasan hanya berisi angka, tanpa interpretasi.
    """
    # 1. Hitung jumlah jawaban per persona per dimensi
    # Dimensi MBTI: E/I, S/N, T/F, J/P
    counts = {
        persona: {
            "E/I": {"A": 0, "B": 0, "invalid": 0},
            "S/N": {"A": 0, "B": 0, "invalid": 0},
            "T/F": {"A": 0, "B": 0, "invalid": 0},
            "J/P": {"A": 0, "B": 0, "invalid": 0},
        }
        for persona in PERSONAS
    }

    # 2. Tampung jawaban per persona per nomor pertanyaan untuk menghitung konsistensi
    responses_by_q = {
        persona: {q_id: [] for q_id in questions.keys()}
        for persona in PERSONAS
    }

    for r in records:
        p = r["persona"]
        q_id = r["nomor_pertanyaan"]
        ans = r["jawaban"]
        dim = questions[q_id]["dimension"]

        if ans in ("A", "B"):
            counts[p][dim][ans] += 1
        else:
            counts[p][dim]["invalid"] += 1

        responses_by_q[p][q_id].append(ans)

    # Konsistensi: jumlah ulangan terbanyak yang sama dari 3 ulangan
    consistency = {
        persona: {}
        for persona in PERSONAS
    }

    for persona in PERSONAS:
        for q_id, ans_list in responses_by_q[persona].items():
            if ans_list:
                c = Counter(ans_list)
                max_agreement = c.most_common(1)[0][1]
            else:
                max_agreement = 0
            consistency[persona][str(q_id)] = max_agreement

    return {
        "counts_per_persona_per_dimension": counts,
        "consistency_per_question": consistency,
    }


def main():
    model_id = os.environ.get("GEMINI_MODEL", DEFAULT_MODEL_ID)
    api_key = load_api_key(ENV_PATH)
    questions_list = load_questions(QUESTIONS_PATH)
    questions_map = {q["id"]: q for q in questions_list}

    print(f"Memulai eksperimen pilot Shinri-LLM...")
    print(f"Model ID: {model_id} | Provider: {PROVIDER} | Settings: {SETTINGS}")
    print(f"Personas: {PERSONAS} | Pertanyaan: {len(questions_list)} | Ulangan: {REPEATS_PER_QUESTION}")
    print(f"Total panggilan direncanakan: {len(PERSONAS) * len(questions_list) * REPEATS_PER_QUESTION}")
    print("-" * 60)

    records = []
    call_count = 0
    total_calls = len(PERSONAS) * len(questions_list) * REPEATS_PER_QUESTION

    for persona in PERSONAS:
        for q in questions_list:
            for rep in range(1, REPEATS_PER_QUESTION + 1):
                call_count += 1
                print(f"[{call_count}/{total_calls}] Persona: {persona} | Q: {q['id']} ({q['dimension']}) | Rep: {rep} ... ", end="", flush=True)

                jawaban = call_gemini_api(api_key, model_id, persona, q)
                display_jawaban = jawaban.replace("\n", " ") if len(jawaban) <= 100 else jawaban[:97].replace("\n", " ") + "..."
                try:
                    print(f"Jawaban: {display_jawaban}")
                except Exception:
                    print(f"Jawaban: [berisi karakter khusus]")

                records.append({
                    "persona": persona,
                    "nomor_pertanyaan": q["id"],
                    "ulangan_ke": rep,
                    "jawaban": jawaban,
                    "model_id": model_id,
                    "provider": PROVIDER,
                    "pengaturan": SETTINGS,
                })

                if call_count < total_calls:
                    time.sleep(DELAY_SECONDS)

    # Simpan hasil jawaban (60 baris)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(ANSWERS_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["persona", "nomor_pertanyaan", "ulangan_ke", "jawaban", "model_id", "provider", "pengaturan"]
        )
        writer.writeheader()
        writer.writerows(records)

    # Buat dan simpan ringkasan angka
    summary_data = compute_summary(records, questions_map)
    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)

    print("-" * 60)
    print(f"Eksperimen selesai.")
    print(f"File jawaban tersimpan di: {ANSWERS_PATH} ({len(records)} baris data)")
    print(f"File ringkasan tersimpan di: {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
