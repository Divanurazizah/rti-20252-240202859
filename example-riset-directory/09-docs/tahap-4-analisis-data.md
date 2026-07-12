
# Tahap 4 — Analisis Hasil

**Status:** Selesai
**Lokasi output:** `06-output`

Tahap analisis hasil merupakan proses akhir dalam penelitian yang bertujuan untuk menginterpretasikan performa kedua algoritma klasifikasi berdasarkan hasil pengujian yang telah dilakukan. Seluruh hasil pengujian disimpan pada folder ```06-output``` dalam bentuk tabel maupun ringkasan evaluasi sehingga dapat digunakan sebagai dasar dalam menarik kesimpulan penelitian.

Analisis dilakukan dengan membandingkan kinerja algoritma Naïve Bayes dan Decision Tree C4.5 pada proses klasifikasi sentimen ulasan e-commerce yang menggunakan bahasa formal maupun bahasa slang. Hasil evaluasi dianalisis berdasarkan beberapa metrik performa untuk mengetahui algoritma yang memberikan hasil paling baik dan paling stabil.

## Fokus Analisis
1. **Perbandingan Akurasi**: Menghitung Mean Accuracy & F1-Score untuk Naïve Bayes dan C4.5.
2. **Drop Rate Analysis**: Menghitung persentase penurunan performa (drop rate) saat model berpindah dari teks Formal ke teks Slang.
3. **Analisis Algoritma**: Pembuktian bahwa C4.5 lebih tangguh terhadap *noise* slang dibandingkan Naïve Bayes.

Berdasarkan seluruh tahapan evaluasi, diperoleh gambaran mengenai kelebihan dan keterbatasan masing-masing algoritma. Hasil analisis selanjutnya digunakan sebagai dasar penyusunan kesimpulan penelitian serta memberikan rekomendasi mengenai algoritma yang paling efektif untuk klasifikasi sentimen pada dataset ulasan e-commerce dengan karakteristik bahasa formal maupun bahasa slang.