# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean (%) | Std (%) | Median (%) | Min (%) | Max (%) | n |
   |----------|----------|---------|------------|---------|---------|---|
   | C4.5 (Dataset Formal)      | 85.20    | 1.15    | 85.30      | 83.10   | 86.90   | 10|
   | Naïve Bayes (Dataset Formal)| 82.10    | 1.85    | 82.00      | 79.20   | 84.50   | 10|
   | C4.5 (Dataset Slang)       | 79.50    | 2.45    | 79.40      | 75.80   | 82.30   | 10|
   | Naïve Bayes (Dataset Slang)| 75.20    | 3.10    | 75.50      | 70.10   | 78.90   | 10|

2. Uji Hipotesis:
   Uji yang digunakan  : Paired t-test (Skenario Formal vs Slang untuk masing-masing model)
   Justifikasi         : Membandingkan rata-rata nilai akurasi dari 2 kelompok algoritma yang sama yang diuji pada sepasang kondisi data berbeda (Normalitas terpenuhi).
   Hasil: p = 0.012, effect size (Cohen's d) = 1.82
   CI 95%              : [1.25, 4.35]

3. Keputusan:
   [x] H₀ ditolak → H₁ diterima (Terdapat perbedaan performa akurasi yang signifikan antara penggunaan teks formal dan slang)
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ        : Penggunaan bahasa slang secara signifikan menurunkan tingkat akurasi dan stabilitas model. C4.5 terbukti lebih tangguh dibanding Naïve Bayes dalam menangani variabilitas kata non-baku.
   Practical significance: Penurunan akurasi hingga ~7% pada teks slang menunjukkan bahwa pembersihan bahasa gaul di aplikasi e-commerce krusial dilakukan sebelum klasifikasi sentimen berjalan.
   Perbandingan literatur: Sejalan dengan temuan riset linguistik komputasional bahwa tingginya variasi sinonim tidak terstruktur pada ulasan informal merusak nilai probabilitas kondisional dari ekstraksi fitur.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Construct validity | Kamus slang buatan manual belum mencakup istilah tren bahasa gaul terbaru 2026. | Penurunan akurasi saat mendeteksi istilah slang yang benar-benar baru. | Melakukan pembaruan korpus kata slang secara berkala menggunakan library eksternal. |

6. Failure Analysis (Kasus Penurunan Performa Naïve Bayes pada Teks Slang):
   Penyebab potensial  : Adanya pelanggaran asumsi "fitur saling bebas" (conditional independence) karena kata-kata slang sering muncul berpasangan atau berulang secara tak teratur (contoh: "yg bgtu", "bgt bgt").
   Boundary condition   : Naïve Bayes hanya bekerja optimal pada data teks bersih/formal dengan sebaran kosakata yang terukur secara teori peluang stokastik.
   Insight              : Algoritma berbasis probabilitas murni sangat sensitif terhadap lonjakan noise tulisan informal, sehingga memerlukan dukungan tahap normalisasi teks yang ekstra ketat.

```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa algortima yang dibandingkan?| 2 algortima Utama (Algoritma C4.5 vs Naïve Bayes) |
| Apakah data berpasangan (paired)? | Ya, karena kedua algoritma diuji menggunakan basis subset data run eksperimen yang sama (Formal vs Slang). |
| Apakah distribusi normal? (uji normalitas) | Ya, hasil uji Shapiro-Wilk menunjukkan nilai p > 0.05 (data akurasi berdistribusi normal). |
| **Uji yang dipilih:** | Paired t-test |
| **Justifikasi:** | Digunakan untuk menguji signifikansi perbedaan nilai rata-rata dari dua algoritma klasifikasi yang dievaluasi berulang kali (n=10) pada parameter lingkungan yang terkontrol. |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 89.2 ± 1.5 | 10 |
| B | 87.8 ± 2.1 | 10 |

p = 0.045, Cohen's d = 0.74, CI 95% = [0.03, 2.77]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | Nilai p = 0.012 < 0.05 menunjukkan bahwa keunggulan nilai akurasi C4.5 atas Naïve Bayes pada data ulasan e-commerce bukanlah faktor kebetulan, melainkan signifikan secara statistik. |
| Effect size | Nilai d = 1.82 masuk dalam kategori Large Effect (> 0.8). Artinya, perbedaan struktur pengkondisian pohon keputusan (C4.5) memberikan pengaruh yang sangat besar terhadap hasil akurasi dibanding kalkulasi probabilitas kata (Naïve Bayes). |
| Practical significance | Secara praktis di industri, selisih akurasi sebesar ~3-5% sudah cukup berharga bagi pemilik e-commerce untuk memilih C4.5 sebagai basis mesin analisis sentimen otomatis pada menu ulasan produknya. |
| Hubungan ke RQ | Menjawab pertanyaan penelitian bahwa karakteristik dataset (adanya teks slang) terbukti menurunkan akurasi, namun model berbasis pohon keputusan jauh lebih kokoh bertahan dibanding model probabilitas. |
| Perbandingan literatur | Hasil ini memperkuat teori klasifikasi teks yang menyatakan bahwa algoritma Decision Tree (C4.5) mampu menangani fitur-fitur non-linear yang tidak relevan lebih baik melalui seleksi Gain Ratio, sementara Naïve Bayes terbebani oleh bias kemunculan kata slang. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan gagal total. Penurunan nilai metrik pada skenario ulasan teks slang merupakan hasil temuan ilmiah yang valid yang menunjukkan batasan operasional (boundary condition) dari masing-masing algoritma. |
| Kemungkinan penyebab? | Model Naïve Bayes mengalami fenomena Zero-Probability atau pembagian bobot yang pincang ketika mendeteksi susunan kata slang baru yang tidak ada atau jarang muncul di data training (misal penulisan "bgt", "bangettt", "bgtt"). |
| Boundary condition? | Algoritma klasifikasi Naïve Bayes terbukti efektif hanya ketika dihadapkan pada data kalimat yang formal, terstruktur, serta memiliki variasi sinonim kata yang rendah. |
| Insight yang bisa diambil? | Ada kebergantungan erat antara kualitas algoritma dengan keseragaman data input. Peneliti selanjutnya disarankan membuat modul dictionary-mapping bahasa daerah/slang sebelum data masuk ke tahap ekstraksi TF-IDF. |
| Apakah layak dilaporkan? Mengapa? | Layak. Melaporkan penurunan performa akibat jenis teks tertentu akan memberi kontribusi informasi penting bagi peneliti lain agar tidak mengulangi kesalahan arsitektur data yang sama. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical limitation | Jumlah iterasi K-Fold Cross Validation terbatas pada angka 10-Fold. | Rentang nilai kepastian (Confidence Interval) akurasi menjadi sedikit lebih lebar pada data teks slang. |
| External validity | Dataset ulasan hanya diambil dari satu kategori produk fashion e-commerce saja. | Hasil interpretasi kesimpulan ini belum tentu sama persis jika diterapkan pada ulasan teks produk gadget atau kuliner. |


---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Failure atau penurunan performa dalam eksperimen ilmiah sama sekali bukan sebuah kegagalan riset yang memalukan. Justru, menganalisis letak kelemahan suatu model adalah salah satu bentuk kontribusi ilmiah yang orisinal. Lewat failure analysis, cara pandang saya terhadap hasil negatif menjadi berubah total: saya tidak lagi sekadar berfokus mencari angka akurasi yang tinggi (p-hacking), melainkan terdorong untuk mengeksplorasi alasan logis di balik sistem komputasi tersebut. Mengetahui di mana dan kapan algoritma C4.5 atau Naïve Bayes runtuh saat memproses kata slang memberikan panduan konkret bagi perbaikan sistem AI di masa depan, agar proses normalisasi bahasa informal bisa dirancang lebih adaptif.
