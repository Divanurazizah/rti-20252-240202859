# Hasil Penelitian: Klasifikasi Sentimen (Naïve Bayes vs C4.5)

Dokumen ini merangkum hasil eksperimen dari 400 *run* pengujian (4 Run x 10 Fold) pada dataset ulasan e-commerce.

## 1. Tabel Ringkasan Performa
Tabel di bawah menunjukkan rata-rata akurasi dan F1-Score dari kedua algoritma pada skenario teks Formal dan Slang.

| Algoritma | Skenario | Mean Accuracy | Mean F1-Score | Analisis Singkat |
|---|---|---|---|---|
| Naïve Bayes | Formal | 0.856 | 0.852 | Baseline performa tinggi pada data baku. |
| Naïve Bayes | Slang | 0.775 | 0.766 | Performa turun drastis karena sensitif terhadap noise. |
| C4.5 | Formal | 0.876 | 0.873 | Model paling optimal untuk teks standar. |
| C4.5 | Slang | 0.818 | 0.812 | Stabil meskipun teks mengandung banyak slang. |

## 2. Analisis Penurunan Performa (Drop Rate)
Penurunan performa saat berpindah dari teks Formal ke Slang memberikan gambaran seberapa tangguh algoritma tersebut.

| Algoritma | Drop Rate Akurasi (%) | Analisis Dampak |
|---|---|---|
| Naïve Bayes | 9.46% | Sangat sensitif terhadap variasi kata slang. |
| C4.5 | 6.62% | Lebih tahan banting (robust) terhadap noise. |

## 3. Kesimpulan Ilmiah
1. **Superioritas C4.5:** Algoritma C4.5 terbukti lebih unggul dalam menangani dataset ulasan yang tidak terstruktur dibandingkan Naïve Bayes.
2. **Faktor Noise:** Karakteristik bahasa slang (singkatan, penghilangan vokal) secara konsisten menurunkan performa model. Namun, struktur pohon keputusan pada C4.5 mampu memilah fitur (kata) yang relevan lebih baik daripada probabilitas statistik pada Naïve Bayes.
3. **Validitas:** Hasil ini merupakan rata-rata dari 40 iterasi pengujian, sehingga angka yang disajikan memiliki tingkat reliabilitas yang tinggi.

---