# PLANSPEC v0.1.0 (sedang dikerjakan)

## Buat dokumen dev

Tujuan: Menyiapkan dokumen kerja agent untuk repo Shinri-LLM (LLM persona psychometrics experiments), supaya sesi berikutnya konsisten dan satu sesi hanya mengerjakan satu item.

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

## Koreksi nama Shinri-LLM

Tujuan: Menyeragamkan penulisan nama proyek menjadi "Shinri-LLM" (huruf S, L, L besar) di dokumen dev, karena sebelumnya tertulis "shinri-llm". Item ini hanya mengubah teks di dev/.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru.

Izin dari pemilik:
- Item ini boleh mengubah satu baris di bagian "Keputusan terkunci" di dev/PLAN.md, yaitu baris yang diawali "Nama repo shinri-llm", hanya pada penulisan nama. Tidak boleh mengubah baris lain di bagian itu.
- Item ini boleh mengubah teks bagian "## Buat dokumen dev" di dev/PLANSPEC.md, hanya pada penulisan nama. Aturan "Jangan ubah entri lama" dilonggarkan hanya untuk ini.

Aturan:
- Ganti penulisan "shinri-llm" menjadi "Shinri-LLM" hanya pada teks nama proyek di tiga tempat: judul dev/PLAN.md ("# PLAN.md: Shinri-LLM"), baris "Nama repo" di Keputusan terkunci (jadi "Nama repo Shinri-LLM, ..."), dan kalimat Tujuan di bagian "## Buat dokumen dev" di dev/PLANSPEC.md (jadi "untuk repo Shinri-LLM").
- Jangan mengubah teks lain di baris-baris itu, termasuk deskripsi bahasa Inggris "LLM persona psychometrics experiments".
- Jangan mengubah dev/RULES.md dan entri lama di dev/CHANGELOG.md.
- Jangan menambah bagian, aturan, atau fase baru.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Mencari "shinri-llm" (huruf kecil semua) di dev/ tidak menemukan hasil.
- Mencari "Shinri-LLM" di dev/ menemukan tepat tiga baris pada dev/PLAN.md dan dev/PLANSPEC.md, ditambah baris item ini sendiri.
- Judul item "Koreksi nama Shinri-LLM" di dev/PLAN.md sama persis dengan judul bagian di dev/PLANSPEC.md.
- `git ls-files dev/` tidak menambah file baru.
- `git status --short` bersih dan tidak ada perubahan di luar dev/.

## Fase 1: Pilot

Tujuan: Menguji apakah satu model murah memberi jawaban MBTI yang berbeda dan konsisten saat diberi dua persona berlawanan. Hasilnya menentukan apakah Fase 2 layak dilanjutkan.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru.

Folder kerja:
- src/
- experiments/mbti/gemini-flash-lite/
- results/mbti/gemini-flash-lite/

Aturan:
- Persona ada dua: INTJ dan ESFP. Keduanya diberikan lewat system instruction dengan kalimat yang sama, hanya kode tipenya yang berbeda: "Kamu adalah seseorang dengan tipe kepribadian [TIPE]. Jawab semua pertanyaan sebagai orang itu."
- Model: satu model Gemini Flash-Lite yang tersedia di free tier. Pengaturan generasi memakai nilai bawaan API.
- Pertanyaan uji ada 10, ditulis sebagai skenario singkat dengan dua pilihan jawaban A atau B, dibagi rata ke empat dimensi (E/I, S/N, T/F, J/P, masing-masing 2 sampai 3 pertanyaan). Simpan di experiments/mbti/gemini-flash-lite/questions.json.
- Tiap persona menjawab tiap pertanyaan 3 kali, satu panggilan API per jawaban. Total 60 panggilan.
- Model diminta menjawab hanya dengan huruf A atau B. Jawaban yang bukan A atau B dicatat apa adanya sebagai tidak valid dan tidak diulang otomatis.
- Beri jeda antar panggilan. Kalau API mengembalikan error kuota atau error otentikasi, berhenti dan laporkan. Jangan coba model atau provider lain.
- Skrip membaca API key dari .env sesuai nama variabel di .env.example. Kalau key tidak ada, berhenti dan laporkan. Key tidak boleh ditulis ke file mana pun di repo.
- Setiap baris hasil mencatat: persona, nomor pertanyaan, ulangan ke berapa, jawaban, ID model persis, provider, dan pengaturan yang dipakai.
- Skrip juga membuat ringkasan: jumlah jawaban A dan B per persona per dimensi, dan konsistensi 3 ulangan per pertanyaan. Ringkasan hanya berisi angka, tanpa interpretasi.
- Semua file di results/mbti/gemini-flash-lite/ dihasilkan oleh skrip di src/ dan experiments/mbti/gemini-flash-lite/, tidak ditulis tangan. Skrip ada di src/ kecuali berkas pertanyaan.
- Kalau butuh dependensi Python, catat di requirements.txt.
- Sengaja tidak dilakukan: OEJTS, model lain, persona selain dua itu, grafik, dan analisis.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Jalankan skrip dengan key valid di .env. Hasil: file jawaban berisi 60 baris dan file ringkasan terbentuk di results/mbti/gemini-flash-lite/.
- Jalankan skrip tanpa key di .env. Hasil: skrip berhenti dengan pesan jelas dan tidak membuat file hasil.
- Jalankan git status --short. Hasil: .env tidak muncul, dan tidak ada file di luar item ini selain file dev yang diizinkan.

## Arsip temuan

Tujuan: Membuat tempat di dev/ untuk mengarsipkan temuan sampingan dari eksperimen, satu file per temuan, dikelompokkan per teori. Dimulai dari temuan jawaban ESFP yang tidak patuh format di Fase 1, supaya temuan bisa dibandingkan satu sama lain di fase berikutnya.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru.

Folder kerja:
- dev/temuan/mbti/
- results/mbti/gemini-flash-lite/ (dibaca saja, tidak diubah)

Aturan:
- Satu temuan satu file Markdown, ditaruh di folder teori yang sesuai. Temuan MBTI ada di dev/temuan/mbti/.
- Nama file: nomor temuan, tanda hubung, judul singkat huruf kecil dengan tanda hubung. Nomor berurutan lintas semua teori (T-001, T-002, dan seterusnya), tidak mulai ulang di tiap folder teori.
- Semua temuan ditulis dalam bahasa Indonesia dengan format yang sama: judul "# T-001: [judul singkat]", lalu baris berlabel Teori, Fase, Model (ID persis dari kolom model_id), Persona, Jenis, Ringkasan (maksimal tiga kalimat), Bukti (path file dan nomor baris), Angka, dan Batasan.
- Label Jenis diisi salah satu dari: perilaku model, kualitas instrumen, atau pola jawaban.
- Entri pertama adalah dev/temuan/mbti/T-001-esfp-tidak-patuh-format.md. Isinya: dua jawaban ESFP tidak berformat A atau B murni. Jawaban A atau B memang diberikan di awal teks, tetapi model lanjut menulis kalimat bergaya persona dengan emoji. Label Persona diisi ESFP, dengan INTJ sebagai pembanding.
- Isi T-001 diambil dari results/mbti/gemini-flash-lite/answers.csv dan summary.json. Baca hanya baris ESFP pertanyaan 2 dan 10, serta baris yang jawabannya bukan A atau B. Bukti menyebut kedua baris itu (ESFP pertanyaan 2 ulangan 3, dan ESFP pertanyaan 10 ulangan 2), dengan nomor baris di berkas CSV.
- Teks mentah kedua jawaban itu disalin persis dari answers.csv sebagai kutipan blok, tidak diketik ulang dan tidak diubah.
- Angka T-001: ESFP 2 dari 30 jawaban tidak berformat A atau B murni, INTJ 0 dari 30. Kalau dihitung dari huruf awal, kedua jawaban itu tetap bermakna A dan B.
- Batasan T-001 wajib menyebut: satu model, satu kali jalan, 30 panggilan per persona, jadi ini temuan sampingan dan bukan bukti bahwa tipe kepribadian tertentu lebih sulit patuh format.
- results/ tidak diubah sama sekali, termasuk answers.csv dan summary.json. Hitungan "invalid" di summary.json dibiarkan apa adanya.
- Sengaja tidak dilakukan: temuan lain (misalnya soal pertanyaan S/N), indeks atau tabel perbandingan, perbaikan parser, perubahan skrip di src/, perubahan README, dan perubahan dev/RULES.md.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka dev/temuan/mbti/T-001-esfp-tidak-patuh-format.md. Hasil: semua label format terisi dan isinya bahasa Indonesia.
- Bandingkan dua kutipan di T-001 dengan baris yang sama di answers.csv. Hasil: teksnya identik.
- Jalankan git status --short sebelum commit. Hasil: hanya file di dev/ yang berubah, results/ dan src/ tidak ada.

## Temuan T-002

Tujuan: Mencatat temuan bahwa pertanyaan 5 di pilot MBTI kemungkinan kurang bersih mengukur dimensi S/N, sebagai temuan jenis kualitas instrumen.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru.

Folder kerja:
- dev/temuan/mbti/
- experiments/mbti/gemini-flash-lite/ (dibaca saja, tidak diubah)
- results/mbti/gemini-flash-lite/ (dibaca saja, tidak diubah)

Aturan:
- Buat satu file: dev/temuan/mbti/T-002-q5-kurang-bersih-sn.md. Format sama persis dengan T-001 di folder yang sama (judul "# T-002: ...", lalu label Teori, Fase, Model, Persona, Jenis, Ringkasan, Bukti, Angka, Batasan, bahasa Indonesia).
- Label Jenis diisi: kualitas instrumen. Label Persona diisi ESFP, dengan INTJ sebagai pembanding.
- Ringkasan (maksimal tiga kalimat): persona ESFP menjawab A di pertanyaan 4 dan B di pertanyaan 5, padahal keduanya memiliki arah kunci yang sama (A = S, B = N). Pertanyaan 5 mencampur preferensi S/N dengan ciri spontan atau suka hal baru, dan hal itu diduga membuat ESFP condong ke opsi B.
- Bukti: kutip teks pertanyaan 4 dan 5 persis dari experiments/mbti/gemini-flash-lite/questions.json (skenario, option_a, option_b, pole_a, pole_b), serta baris ESFP dan INTJ untuk pertanyaan 4 dan 5 dari results/mbti/gemini-flash-lite/answers.csv, dengan nomor baris CSV. Hitungan S/N diambil dari summary.json.
- Angka: ESFP pertanyaan 4 = A tiga dari tiga ulangan, pertanyaan 5 = B tiga dari tiga ulangan. INTJ = B enam dari enam di kedua pertanyaan. Angka ini harus dicocokkan dengan file sumber sebelum ditulis.
- Batasan wajib menyebut: penyebab di Ringkasan adalah dugaan dan belum terbukti. Hanya ada dua pertanyaan S/N, satu model, satu kali jalan, dan tiga ulangan hampir identik sehingga datanya setara dua butir unik per persona. Temuan ini tidak memengaruhi Fase 2 karena Fase 2 memakai OEJTS, bukan 10 pertanyaan pilot.
- experiments/ dan results/ tidak diubah sama sekali, termasuk questions.json, answers.csv, dan summary.json.
- Sengaja tidak dilakukan: revisi pertanyaan 5, perubahan skrip di src/, temuan lain, indeks atau tabel perbandingan, dan perubahan README.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka dev/temuan/mbti/T-002-q5-kurang-bersih-sn.md. Hasil: semua label terisi, format sama dengan T-001.
- Bandingkan kutipan pertanyaan dan baris jawaban di T-002 dengan sumbernya. Hasil: teksnya identik dan angkanya cocok.
- Jalankan git status --short sebelum commit. Hasil: hanya file di dev/ yang berubah, experiments/, results/, dan src/ tidak ada.
