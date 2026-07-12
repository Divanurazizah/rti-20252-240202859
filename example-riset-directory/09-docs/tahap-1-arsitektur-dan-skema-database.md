
# Tahap 1 — Perancangan Dataset & Skema Data

**Status:** Selesai

## 1. Struktur Dataset
Pada tahap awal penelitian dilakukan perancangan struktur dataset yang akan digunakan sebagai sumber data utama dalam proses analisis sentimen. Dataset terdiri dari 920 ulasan produk e-commerce yang dikumpulkan dari platform e-commerce dan telah melalui proses pelabelan sentimen menjadi dua kategori, yaitu positif dan negatif. Pelabelan dilakukan untuk menyediakan data yang siap digunakan pada proses pelatihan dan pengujian model klasifikasi.

Dataset disimpan dalam format Comma Separated Values (CSV) agar mudah diproses menggunakan bahasa pemrograman Python serta berbagai pustaka analisis data. Struktur dataset dirancang sesederhana mungkin sehingga setiap atribut memiliki fungsi yang jelas dalam tahapan penelitian.
Adapun atribut yang digunakan meliputi:
- `review_text`: Teks ulasan mentah.
- `cleaned_text`: Teks setelah melalui normalisasi slang.
- `sentiment_label`: Label sentimen (1 untuk Positif, 0 untuk Negatif).

## 2. Alur Pemrosesan Data
Setelah dataset disiapkan, setiap ulasan diproses melalui beberapa tahapan preprocessing sebelum digunakan sebagai data masukan bagi algoritma klasifikasi. Tahapan ini bertujuan untuk meningkatkan kualitas data, mengurangi noise, serta menghasilkan representasi teks yang lebih konsisten sehingga dapat meningkatkan performa model klasifikasi.
Tahapan pemrosesan data meliputi:
Raw Data, yaitu kumpulan ulasan produk yang masih berupa teks mentah hasil pengumpulan data.
Cleaning, yang meliputi proses case folding (mengubah seluruh huruf menjadi huruf kecil), penghapusan tanda baca, angka, karakter khusus, serta stopword removal untuk menghilangkan kata-kata yang tidak memiliki kontribusi signifikan terhadap proses klasifikasi.
Normalisasi Slang, yaitu proses mengubah kata-kata tidak baku atau bahasa gaul menjadi bentuk baku berdasarkan kamus normalisasi sehingga variasi penulisan kata dapat diminimalkan.
TF-IDF Vectorization, yaitu mengubah data teks menjadi representasi numerik menggunakan metode Term Frequency–Inverse Document Frequency sehingga dapat diproses oleh algoritma machine learning.
Model Klasifikasi, yaitu proses pelatihan dan pengujian menggunakan algoritma Naïve Bayes dan Decision Tree C4.5 untuk menentukan kelas sentimen setiap ulasan.

Secara umum, alur pemrosesan data dalam penelitian ini dapat digambarkan sebagai berikut:
`Raw Data` → `Cleaning (Case folding, Stopword removal)` → `Normalisasi Slang` → `TF-IDF Vectorization` → `Model Klasifikasi`.
