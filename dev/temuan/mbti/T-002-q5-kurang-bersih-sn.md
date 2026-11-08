# T-002: Pertanyaan 5 kurang bersih mengukur S/N

Teori: MBTI  
Fase: Fase 1  
Model: gemini-3.5-flash-lite  
Persona: ESFP, dengan INTJ sebagai pembanding  
Jenis: kualitas instrumen  

Ringkasan: Persona ESFP menjawab A di pertanyaan 4 dan B di pertanyaan 5, padahal keduanya memiliki arah kunci yang sama (A = S, B = N). Pertanyaan 5 mencampur preferensi S/N dengan ciri spontan atau suka hal baru, dan hal itu diduga membuat ESFP condong ke opsi B.

Bukti:
- Teks pertanyaan 4 dan 5 dari experiments/mbti/gemini-flash-lite/questions.json:
  - Pertanyaan 4:
    - scenario: "Dalam menerima dan memproses informasi baru, kamu lebih tertarik pada:"
    - option_a: "Fakta konkret, rincian realistis, dan hal-hal praktis yang dapat langsung diterapkan."
    - option_b: "Konsep abstrak, pola tersembunyi, dan berbagai kemungkinan di masa depan."
    - pole_a: "S"
    - pole_b: "N"
  - Pertanyaan 5:
    - scenario: "Saat mulai mengerjakan suatu proyek baru:"
    - option_a: "Lebih menyukai metode teruji yang langkah-langkahnya jelas dan sudah terbukti berhasil."
    - option_b: "Lebih menyukai merancang pendekatan orisinal dan inovatif meski metodenya belum pernah dicoba."
    - pole_a: "S"
    - pole_b: "N"
- Baris jawaban di results/mbti/gemini-flash-lite/answers.csv:
  - INTJ pertanyaan 4:
    - baris 11: `INTJ,4,1,B,gemini-3.5-flash-lite,google,default`
    - baris 12: `INTJ,4,2,B,gemini-3.5-flash-lite,google,default`
    - baris 13: `INTJ,4,3,B,gemini-3.5-flash-lite,google,default`
  - INTJ pertanyaan 5:
    - baris 14: `INTJ,5,1,B,gemini-3.5-flash-lite,google,default`
    - baris 15: `INTJ,5,2,B,gemini-3.5-flash-lite,google,default`
    - baris 16: `INTJ,5,3,B,gemini-3.5-flash-lite,google,default`
  - ESFP pertanyaan 4:
    - baris 41: `ESFP,4,1,A,gemini-3.5-flash-lite,google,default`
    - baris 42: `ESFP,4,2,A,gemini-3.5-flash-lite,google,default`
    - baris 43: `ESFP,4,3,A,gemini-3.5-flash-lite,google,default`
  - ESFP pertanyaan 5:
    - baris 44: `ESFP,5,1,B,gemini-3.5-flash-lite,google,default`
    - baris 45: `ESFP,5,2,B,gemini-3.5-flash-lite,google,default`
    - baris 46: `ESFP,5,3,B,gemini-3.5-flash-lite,google,default`
- Hitungan dimensi S/N dari results/mbti/gemini-flash-lite/summary.json:
  - INTJ S/N: A = 0, B = 6, invalid = 0
  - ESFP S/N: A = 3, B = 3, invalid = 0

Angka: ESFP pertanyaan 4 = A tiga dari tiga ulangan, pertanyaan 5 = B tiga dari tiga ulangan. INTJ = B enam dari enam di kedua pertanyaan.

Batasan: Penyebab di Ringkasan adalah dugaan dan belum terbukti. Hanya ada dua pertanyaan S/N, satu model, satu kali jalan, dan tiga ulangan hampir identik sehingga datanya setara dua butir unik per persona. Temuan ini tidak memengaruhi Fase 2 karena Fase 2 memakai OEJTS, bukan 10 pertanyaan pilot.
