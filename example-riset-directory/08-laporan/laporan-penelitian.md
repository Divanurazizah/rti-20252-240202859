# LAPORAN AKHIR PENELITIAN
**Judul:** Analisis Komparatif Algoritma Naïve Bayes dan C4.5 pada Klasifikasi Sentimen Ulasan E-Commerce dengan Bahasa Slang
**Peneliti:** Diva Nur Azizah (NIM: 240202859)
**Institusi:** Universitas Putra Bangsa

---

## 1. Ringkasan Eksekutif
Penelitian ini dilaksanakan untuk menjawab tantangan klasifikasi teks pada platform e-commerce yang didominasi oleh bahasa tidak baku (slang). Melalui eksperimen sistematis pada 920 sampel data, penelitian ini berhasil mengidentifikasi bahwa algoritma C4.5 memberikan performa yang lebih stabil dibandingkan Naïve Bayes dalam menghadapi *noise* linguistik. Hasil ini memberikan landasan bagi pengembangan sistem analisis sentimen yang lebih akurat untuk mendukung pengambilan keputusan berbasis data bagi UMKM.

## 2. Pendahuluan
### 2.1 Latar Belakang
Pesatnya pertumbuhan e-commerce menghasilkan data ulasan produk dalam jumlah besar. Namun, karakteristik ulasan yang cenderung subjektif dan tidak terstruktur (banyak mengandung *typo* dan bahasa gaul) menjadi kendala utama dalam analisis sentimen otomatis.

### 2.2 Rumusan Masalah
1. Seberapa besar perbedaan performa antara Naïve Bayes dan C4.5 dalam mengklasifikasikan sentimen formal dan slang?
2. Algoritma manakah yang lebih tahan (*robust*) terhadap variasi bahasa informal?

## 3. Metodologi Penelitian
Penelitian menggunakan metode penelitian eksperimental dengan tahapan sebagai berikut:
1. **Pengumpulan Data:** Data diambil dari platform e-commerce dan dilakukan *labeling* sentimen (Positif/Negatif).
2. **Tahapan Preprocessing:** Meliputi *case folding*, tokenisasi, *stopword removal*, serta normalisasi slang menggunakan kamus leksikon yang dikembangkan khusus untuk ulasan e-commerce.
3. **Ekstraksi Fitur:** Menggunakan metode TF-IDF untuk mengubah data tekstual menjadi matriks numerik agar dapat diproses oleh model.
4. **Tahapan Eksperimen:** Menggunakan metode *10-Fold Cross-Validation*. Eksperimen dijalankan sebanyak 40 replikasi untuk memastikan validitas statistik dan meminimalisir bias dari pemilihan data latih/uji.

## 4. Hasil dan Pembahasan
### 4.1 Statistik Kinerja Model
Pengujian menunjukkan bahwa C4.5 unggul dengan akurasi 81.8% pada skenario slang, sementara Naïve Bayes mencapai 77.5%. 

### 4.2 Analisis Kritis
Analisis *drop rate* menunjukkan penurunan performa Naïve Bayes sebesar 9.46% saat menghadapi teks slang, dibandingkan C4.5 yang hanya 6.62%. Hal ini menegaskan bahwa metode berbasis pohon keputusan (C4.5) lebih efektif dalam memisahkan fitur yang relevan dari *noise*. Ketidakmampuan Naïve Bayes dalam menangani ketergantungan antar-kata menjadi penyebab utama ketidakstabilannya pada data yang tidak terstruktur.

## 5. Kendala dan Catatan Lapangan
Selama penelitian, kendala utama yang dihadapi adalah keterbatasan kamus leksikon slang yang mencakup seluruh variasi kata gaul terbaru. Peneliti melakukan penambahan entri kamus secara manual melalui observasi ulasan untuk meminimalisir data yang tidak terdeteksi. Selain itu, proses *cross-validation* yang berulang memerlukan komputasi intensif yang diselesaikan dengan optimasi kode skrip `run_all.py`.

## 6. Kesimpulan dan Rekomendasi
### 6.1 Kesimpulan
Penelitian menyimpulkan bahwa algoritma C4.5 secara signifikan lebih stabil dan unggul daripada Naïve Bayes dalam menangani teks ulasan e-commerce yang banyak mengandung bahasa slang.

### 6.2 Rekomendasi
1. Untuk penelitian lanjutan, disarankan menggunakan *Deep Learning* (seperti BERT atau LSTM) yang mampu mengenali konteks kata secara lebih baik tanpa bergantung penuh pada kamus.
2. Perlu pengembangan *real-time dictionary updater* untuk menangani istilah slang yang terus berkembang setiap waktu.

---
## 7. Lampiran
*   **Dataset:** Disimpan pada repositori `04-data/`.
*   **Source Code:** Seluruh skrip pengembangan terdapat pada `05-kode/`.
*   **Output Statistik:** Hasil komparasi lengkap tersedia pada `06-output/`.
*   **Referensi:** Total 8 referensi utama yang digunakan untuk memperkuat argumen penelitian.

---