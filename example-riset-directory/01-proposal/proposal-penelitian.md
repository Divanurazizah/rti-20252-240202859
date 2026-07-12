# Analisis Sentimen Ulasan E-Commerce Menggunakan Algoritma Naïve Bayes dan C4.5: Studi Komparatif Karakteristik Teks Formal dan Bahasa Slang #

## 1. Latar Belakang

Pesatnya perkembangan industri e-commerce di Indonesia menghasilkan volume data ulasan konsumen yang sangat besar setiap harinya. Analisis sentimen terhadap ulasan ini menjadi instrumen krusial bagi pemilik bisnis untuk mengevaluasi kepuasan pelanggan dan kualitas produk. Namun, tantangan terbesar dalam pemrosesan teks ulasan berbahasa Indonesia di media sosial atau platform belanja seperti Shopee adalah tingginya penggunaan bahasa informal, singkatan, dan bahasa gaul (slang).

Sebagian besar model klasifikasi sentimen dikembangkan dan diuji menggunakan dataset teks yang bersih atau formal. Ketika model tersebut dihadapkan pada data lapangan yang dipenuhi teks slang, performa akurasinya cenderung mengalami penurunan drastis karena distorsi distribusi kata. Dua algoritma klasik yang sering digunakan dalam klasifikasi teks adalah Naïve Bayes (berbasis probabilitas murni) dan C4.5 (berbasis pohon keputusan). Kedua algoritma ini memiliki karakteristik arsitektur matematika yang berbeda dalam menangani variabilitas data teks.

Penelitian ini secara khusus melakukan studi komparatif untuk mengukur sejauh mana pengaruh karakteristik teks (formal vs slang) memengaruhi stabilitas performa, serta mencari batasan operasional (boundary condition) dari algoritma Naïve Bayes dan C4.5 saat diuji pada lingkungan data teks informal.

## 2. Rumusan Masalah

RQ1: Bagaimana pengaruh karakteristik dataset ulasan (Formal vs Slang) terhadap stabilitas nilai akurasi klasifikasi algoritma Naïve Bayes dan C4.5?

Metrik Utama: Accuracy (%) dan F1-Score (%).

## 3. Tujuan Penelitian
- Mengukur penurunan performa (drop rate) akurasi dari algoritma Naïve Bayes dan C4.5 ketika ditransisikan dari lingkungan teks formal ke teks slang.
- Memetakan variabilitas data klasifikasi ulasan melalui pengujian berulang (multiple run via 10-Fold Cross-Validation) untuk melihat model mana yang paling konsisten menahan noise tulisan informal.
- Menemukan alasan logis komputasional di balik kegagalan atau keruntuhan performa model (failure analysis) guna memberikan rekomendasi strategi text preprocessing yang lebih adaptif.

## 4. Urgensi Penelitian

Penelitian ini penting untuk memastikan bahwa sistem penilai sentimen otomatis yang dipasang pada platform e-commerce tidak memberikan kesimpulan yang bias atau salah akibat gagal membaca ulasan konsumen yang menggunakan bahasa sehari-hari. Output dari riset komparatif ini ditargetkan mampu memberikan kontribusi ilmiah yang orisinal.

## 5. Metodologi Penelitian
Penelitian ini dijalankan melalui alur pemrosesan data (Data Refinement Pipeline) sebagai berikut:

- Data Selection: Menggunakan basis data ulasan produk e-commerce berbahasa Indonesia dengan ukuran sampel representatif untuk analisis komparatif tekstual.
- Text Preprocessing (WS-13): Tahapan meliputi case folding, filtering (penghapusan angka/tanda baca), tokenization, stopword removal, dan Lexicon Mapping (normalisasi kamus bahasa slang ke bentuk baku).
- Eksperimen Klasifikasi: Data diuji secara berulang menggunakan metode 10-Fold Cross-Validation (total menghasilkan 40 run eksperimen untuk menguji stabilitas nilai statistik).

## 6. Rencana Penyajian Hasil & Visualisasi
Data hasil pengujian disajikan menggunakan kombinasi dua instrumen berikut:Tabel Hasil Berseri (Presisi):
- Menampilkan nilai desimal eksak Mean kurang lebih Standard Deviation (std) dari masing-masing skenario algoritma.
- Grafik Visual (Pola): Menggunakan Bar Chart + Error Bar untuk melihat kontras penurunan akurasi, serta Box Plot untuk mendeteksi sebaran rentang kestabilan model di setiap run.

