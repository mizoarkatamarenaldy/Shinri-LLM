# PLANSPEC v0.1.0 (sedang dikerjakan)

## Buat dokumen dev

Tujuan: Menyiapkan dokumen kerja agent untuk repo shinri-llm (LLM persona psychometrics experiments), supaya sesi berikutnya konsisten dan satu sesi hanya mengerjakan satu item.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru.

dev/RULES.md (judul "Aturan untuk agent (baca ini dulu)"), isinya:
- Di awal sesi, baca dev/RULES.md dan dev/PLAN.md. Baca dev/PLANSPEC.md hanya di bagian item yang dikerjakan. Baca hanya 5 entri teratas dev/CHANGELOG.md.
- Spek item baru wajib ditulis di dev/PLANSPEC.md dengan judul sama seperti item di dev/PLAN.md. Di dev/PLAN.md hanya satu baris checkbox plus judul singkat, tanpa penjelasan dan tanpa sub-poin. Kalau spek dan PLAN.md berbeda, spek yang berlaku.
- Kerjakan satu item per sesi. Jangan lompat ke item lain. Jangan ubah file di luar item yang dikerjakan.
- Bagian "Keputusan terkunci" di dev/PLAN.md tidak boleh diubah tanpa izin pemilik.
- Repo ini publik. Dilarang menaruh API key, token, atau file .env di repo. Dilarang `git add` pada file .env. Kalau .env muncul di `git status --short`, berhenti dan laporkan.
- Dilarang memanggil API model berbayar atau berkuota (Gemini, OpenRouter, Anthropic, xAI) kecuali spek item secara eksplisit menyuruh, dan hanya dengan key yang sudah ada di .env pemilik.
- Folder experiments/ dan results/ saling mirror: satu subfolder per instrumen atau model, nama sama di keduanya. Hasil di results/ dihasilkan oleh skrip di experiments/ dan src/, tidak ditulis atau diedit tangan.
- LICENSE dan .gitignore tidak diubah tanpa izin pemilik.
- Setiap folder kerja disebut di prompt. Tulis semua path dari root repo.
- Di akhir item: centang item di dev/PLAN.md, tambah satu entri di paling atas dev/CHANGELOG.md sesuai formatnya. Item induk baru dicentang setelah semua sub-itemnya tercentang. Jangan ubah entri lama. Kalau tidak yakin tanggalnya, tulis "tidak tercatat".
- Alur commit dan push: (1) jalankan `git status --short`, kalau ada file di luar item ini (selain dev/PLAN.md, dev/CHANGELOG.md, dev/PLANSPEC.md, dev/RULES.md), berhenti dan laporkan; (2) tambah entri CHANGELOG berdasarkan hasil git status; (3) stage file satu per satu, dilarang `git add -A` dan `git add .`; (4) commit dengan judul format "fase N: nama singkat" (untuk item dokumen dev pakai "dev: nama singkat"), isi penjelasan, lalu dua trailer di bawah, dipisah satu baris kosong:
  Co-authored-by: Claude <noreply@anthropic.com>
  Co-authored-by: Gemini (Antigravity) <200291788+gemini-code-assist@users.noreply.github.com>
  (5) `git push` ke branch aktif, dilarang force push, dilarang membuat atau menghapus branch, dilarang mengubah git config; (6) kalau commit atau push gagal, berhenti dan laporkan errornya; (7) kabari file yang diubah dan hash commit.

dev/PLAN.md (judul "PLAN.md: shinri-llm"), isinya:
- Satu baris: WAJIB baca dev/RULES.md dulu. Spek tiap item ada di dev/PLANSPEC.md.
- Deskripsi singkat: proyek belajar sekaligus portofolio, eksperimen psikometri pada persona LLM.
- Bagian "Keputusan terkunci" berisi:
  - Nama repo shinri-llm, deskripsi bahasa Inggris "LLM persona psychometrics experiments", repo publik.
  - Tujuan: proyek belajar sekaligus portofolio.
  - Data diambil lewat API (bersih dari memori dan system prompt aplikasi). Sampel dari aplikasi hanya pembanding.
  - Biaya: Fase 1 dan 2 memakai Gemini gratis. OpenRouter baru dibeli saat Fase 3 siap (minimum $5).
  - Model yang tersedia: Claude (Sonnet, Haiku), Gemini (Flash-Lite, Flash, Pro, Argon), Grok Fast.
  - Struktur: satu folder per instrumen atau model, bukan branch per teori. experiments/ dan results/ saling mirror.
  - Lisensi MIT, .gitignore template Python.
- Bagian "## v0.1.0 (sedang dikerjakan)" berisi checkbox:
  - [x] Fase 0: Kerangka repo
  - [ ] Fase 1: Pilot
  - [ ] Fase 2: Pengukuran
  - [ ] Fase 3: Tambah model
  - [ ] Fase 4: Perluasan 16 persona
  - [ ] Fase 5: Analisis dan publikasi
  - [x] Buat dokumen dev
  Catatan satu baris di bawahnya: spek Fase 1 sampai 5 ditulis di dev/PLANSPEC.md saat sesi fase itu dikerjakan.

dev/PLANSPEC.md: baris pertama "PLANSPEC v0.1.0 (sedang dikerjakan)", lalu bagian "## Buat dokumen dev" berisi spek item ini (Tujuan, Tempat dan tampilan, Aturan, Data, Cek manual) dengan teks yang sama seperti yang kamu baca di sini.

dev/CHANGELOG.md: baris pertama "CHANGELOG v0.1.0 (sedang dikerjakan)", penjelasan "Catat setiap fitur atau perbaikan yang selesai. Entri terbaru di atas.", blok format entri (## YYYY-MM-DD: nama singkat, lalu baris Ditambah, Diperbaiki, Diubah), lalu dua entri:
- ## 2026-11-08: Buat dokumen dev, dengan baris "Ditambah: dev/RULES.md, dev/PLAN.md, dev/PLANSPEC.md, dev/CHANGELOG.md".
- ## tidak tercatat: Fase 0 kerangka repo, dengan baris "Ditambah: src/, experiments/mbti/, results/mbti/, .env.example, README kerangka, LICENSE, .gitignore".

Aturan:
- Hanya buat empat file di dev/. Tidak ada file lain.
- Jangan menambah bagian, aturan, atau fase di luar yang tertulis di spek ini.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- `git ls-files dev/` menampilkan tepat empat file: dev/RULES.md, dev/PLAN.md, dev/PLANSPEC.md, dev/CHANGELOG.md.
- `git status --short` bersih dan tidak ada perubahan di luar dev/.
- Judul item "Buat dokumen dev" di dev/PLAN.md sama persis dengan judul bagian di dev/PLANSPEC.md.

## Aturan arsip per versi

Tujuan: Menetapkan bahwa satu versi mewakili satu teori, dan menyiapkan aturan mengarsipkan CHANGELOG dan PLANSPEC per versi supaya file aktif tetap kecil saat repo membesar. Item ini hanya mengubah dokumen di dev/.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru.

Izin dari pemilik:
- Item ini boleh menambah satu baris ke bagian "Keputusan terkunci" di dev/PLAN.md, persis seperti teks di bawah. Tidak boleh mengubah baris lain di bagian itu.
- Item ini boleh mengubah dev/RULES.md hanya pada dua hal yang disebut di bawah.

Aturan:
- Tambahkan di akhir bagian "Keputusan terkunci" di dev/PLAN.md satu baris: "Satu versi mewakili satu teori. v0.1.0 adalah MBTI. Pekerjaan lintas teori masuk ke versi yang sedang dikerjakan."
- Tambahkan di bawah baris "WAJIB baca dev/RULES.md dulu..." di dev/PLAN.md satu baris: "Spek tiap versi yang sudah rilis ada di dev/arsip/vX.Y.Z/PLANSPEC.md."
- Tambahkan di akhir dev/RULES.md dua aturan ini:
  - "Baca hanya dev/CHANGELOG.md dan dev/PLANSPEC.md yang aktif. Arsip ada di dev/arsip/vX.Y.Z/, tidak dibaca kecuali pemilik memintanya atau item yang dikerjakan menyentuh pekerjaan versi lama. Dalam kasus itu buka hanya bagian yang terkait."
  - "Aturan rilis, berlaku hanya kalau pemilik memintanya lewat prompt: pindahkan dev/CHANGELOG.md lalu dev/PLANSPEC.md ke dev/arsip/vX.Y.Z/ dengan `git mv`, satu pemindahan per commit. Lalu buat file aktif baru berjudul versi berikutnya, berisi hanya entri dan spek setelah rilis itu. Agent tidak boleh memutuskan sendiri kapan rilis, dan dilarang membuat, mengubah, atau menghapus tag git."
- Item ini sengaja TIDAK membuat folder dev/arsip/ dan tidak memindahkan file apa pun. Folder itu baru dibuat saat rilis pertama.
- Jangan mengubah judul versi di dev/PLAN.md, dev/PLANSPEC.md, atau dev/CHANGELOG.md.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- dev/PLAN.md punya satu baris baru di Keputusan terkunci, satu baris baru di bawah baris WAJIB baca, dan satu checkbox baru "Aturan arsip per versi".
- dev/RULES.md bertambah tepat dua aturan baru dan aturan lama tidak berubah.
- Judul item "Aturan arsip per versi" di dev/PLAN.md sama persis dengan judul bagian di dev/PLANSPEC.md.
- `git ls-files dev/` tetap tepat empat file dan tidak ada folder dev/arsip/.
- `git status --short` bersih dan tidak ada perubahan di luar dev/.
