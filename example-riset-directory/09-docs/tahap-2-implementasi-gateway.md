# Tahap 2 — Implementasi Model Klasifikasi

**Status:** Selesai
**Lokasi kode:** `05-kode

Tahap ini merupakan proses implementasi algoritma klasifikasi yang digunakan dalam penelitian untuk membandingkan performa Naïve Bayes dan Decision Tree C4.5 dalam mengklasifikasikan sentimen ulasan e-commerce yang mengandung bahasa slang. Implementasi dilakukan menggunakan bahasa pemrograman Python dengan memanfaatkan beberapa pustaka pendukung, seperti scikit-learn, pandas, dan NumPy. Sebelum dilakukan proses klasifikasi, data terlebih dahulu melalui tahapan preprocessing dan ekstraksi fitur menggunakan metode TF-IDF (Term Frequency–Inverse Document Frequency) sehingga data teks dapat direpresentasikan dalam bentuk numerik dan diproses oleh algoritma machine learning.

## Komponen
1. **Model Naïve Bayes**: Menggunakan asumsi independensi fitur untuk probabilitas sentimen.
2. **Model C4.5**: Membangun pohon keputusan berdasarkan kriteria *entropy* dan *gain ratio*.
3. **Pipeline**: Skrip Python untuk menjalankan kedua model secara komparatif.
