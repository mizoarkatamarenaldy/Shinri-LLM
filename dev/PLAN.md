# PLAN.md: shinri-llm

WAJIB baca dev/RULES.md dulu. Spek tiap item ada di dev/PLANSPEC.md.
Spek tiap versi yang sudah rilis ada di dev/arsip/vX.Y.Z/PLANSPEC.md.

Deskripsi singkat: proyek belajar sekaligus portofolio, eksperimen psikometri pada persona LLM.

## Keputusan terkunci

- Nama repo shinri-llm, deskripsi bahasa Inggris "LLM persona psychometrics experiments", repo publik.
- Tujuan: proyek belajar sekaligus portofolio.
- Data diambil lewat API (bersih dari memori dan system prompt aplikasi). Sampel dari aplikasi hanya pembanding.
- Biaya: Fase 1 dan 2 memakai Gemini gratis. OpenRouter baru dibeli saat Fase 3 siap (minimum $5).
- Model yang tersedia: Claude (Sonnet, Haiku), Gemini (Flash-Lite, Flash, Pro, Argon), Grok Fast.
- Struktur: satu folder per instrumen atau model, bukan branch per teori. experiments/ dan results/ saling mirror.
- Lisensi MIT, .gitignore template Python.
- Satu versi mewakili satu teori. v0.1.0 adalah MBTI. Pekerjaan lintas teori masuk ke versi yang sedang dikerjakan.

## v0.1.0 (sedang dikerjakan)

- [x] Fase 0: Kerangka repo
- [ ] Fase 1: Pilot
- [ ] Fase 2: Pengukuran
- [ ] Fase 3: Tambah model
- [ ] Fase 4: Perluasan 16 persona
- [ ] Fase 5: Analisis dan publikasi
- [x] Buat dokumen dev
- [x] Aturan arsip per versi

Catatan: spek Fase 1 sampai 5 ditulis di dev/PLANSPEC.md saat sesi fase itu dikerjakan.
