## 4. Metodologi

Penelitian ini menggunakan dataset sebanyak **920 ulasan**. Tahapan penelitian meliputi:

1.  **Preprocessing:** *Case folding*, penghapusan simbol, dan normalisasi slang menggunakan kamus leksikon.
2.  **Ekstraksi Fitur:** Menggunakan *Term Frequency-Inverse Document Frequency* (TF-IDF).
3.  **Klasifikasi:** Penerapan Naïve Bayes dan C4.5 
4.  **Validasi:** Dilakukan *10-Fold Cross-Validation* sebanyak 40 replikasi untuk menjamin reliabilitas.