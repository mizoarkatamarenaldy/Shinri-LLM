# T-001: ESFP tidak patuh format

Teori: MBTI  
Fase: Fase 1  
Model: gemini-3.5-flash-lite  
Persona: ESFP, dengan INTJ sebagai pembanding  
Jenis: perilaku model  

Ringkasan: Dua jawaban ESFP tidak berformat A atau B murni. Jawaban A atau B memang diberikan di awal teks, tetapi model lanjut menulis kalimat bergaya persona dengan emoji.

Bukti:
- results/mbti/gemini-flash-lite/answers.csv baris 37 (ESFP pertanyaan 2 ulangan 3):
  > A! Aduh, mana tahan kalau cuma diam aja, seru banget kan ketemu banyak orang baru di tempat rame! 🥳✨
- results/mbti/gemini-flash-lite/answers.csv baris 60 (ESFP pertanyaan 10 ulangan 2):
  > B! Aduh, kalau disuruh nyicil dari jauh-jauh hari rasanya kurang greget dan bikin bosan! Mendingan nunggu ""the power of *deadline*"" datang, adrenalin langsung ngebut, dan hasilnya justru paling mantap pas detik-detik terakhir! ✨🚀

Angka: ESFP 2 dari 30 jawaban tidak berformat A atau B murni, INTJ 0 dari 30. Kalau dihitung dari huruf awal, kedua jawaban itu tetap bermakna A dan B.

Batasan: Satu model, satu kali jalan, 30 panggilan per persona, jadi ini temuan sampingan dan bukan bukti bahwa tipe kepribadian tertentu lebih sulit patuh format.
