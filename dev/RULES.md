# Aturan untuk agent (baca ini dulu)

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
- Baca hanya dev/CHANGELOG.md dan dev/PLANSPEC.md yang aktif. Arsip ada di dev/arsip/vX.Y.Z/, tidak dibaca kecuali pemilik memintanya atau item yang dikerjakan menyentuh pekerjaan versi lama. Dalam kasus itu buka hanya bagian yang terkait.
- Aturan rilis, berlaku hanya kalau pemilik memintanya lewat prompt: pindahkan dev/CHANGELOG.md lalu dev/PLANSPEC.md ke dev/arsip/vX.Y.Z/ dengan `git mv`, satu pemindahan per commit. Lalu buat file aktif baru berjudul versi berikutnya, berisi hanya entri dan spek setelah rilis itu. Agent tidak boleh memutuskan sendiri kapan rilis, dan dilarang membuat, mengubah, atau menghapus tag git.
