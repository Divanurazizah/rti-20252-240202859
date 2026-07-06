# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Bagaimana pengaruh karakteristik dataset ulasan (Formal vs Slang) terhadap stabilitas nilai akurasi klasifikasi algoritma Naïve Bayes, C4.5
Metrik Utama      : Akurasi (%) dan F1-Score (%)
Tabel Hasil:
| Skenario | Akurasi (mean ± std) | F1-Score (mean ± std) | n |
|----------|----------------------|-----------------------|---|
| C4.5     | 85.20 ± 1.15%        | 84.10 ± 1.30%         | 10|
| Naïve Bayes| 82.10 ± 1.85%      | 80.40 ± 2.10%         | 10|

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar Chart + Error Bar | Perbandingan rata-rata akurasi sekaligus melihat variabilitas tingkat kestabilan antara C4.5 dan Naïve Bayes. | Mean Accuracy ± Std |
| 2 | Box Plot | Menampilkan sebaran distribusi data akurasi untuk melihat konsistensi performa kedua model di setiap run. | Nilai Akurasi Seluruh Run |

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| C4.5(Data Formal) | 85.20 ± 1.15% | 84.10 ± 1.30% | 10 |
| Naïve Bayes (Dataset Formal) | 82.10 ± 1.85% | 80.40 ± 2.10% | 10 |
| C4.5 (Dataset Slang) | 79.50 ± 2.45% | 77.30 ± 2.80% | 10 |
| Naïve Bayes (Dataset Slang) | 75.20 ± 3.10% | 72.80 ± 3.40% | 10 |
 

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | *Contoh: Bar chart + error bar* | Menunjukkan bahwa model C4.5 mengalami penurunan akurasi yang lebih rendah daripada Naïve Bayes saat menangani ulasan teks slang. | Mean Akurasi ± std dari kedua model di kedua tipe dataset. |
| 2 | *Box plot* | Melihat rentang sebaran variabilitas; model Naïve Bayes memiliki boks sebaran yang lebih lebar (kurang stabil) pada teks slang dibanding C4.5. | Seluruh nilai akurasi dari total 40 run eksperimen. |
---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya — Pemotongan sumbu Y (truncated axis) membuat Metode A terlihat memiliki performa dua kali lipat lebih tinggi, padahal perbedaan aslinya sangat tipis (hanya 0.4%) |
| Apakah error bar ditampilkan? | Tidak ditampilkan, sehingga menyembunyikan ketidakpastian sebaran data antar run. |
| Apakah semua kondisi ditampilkan? | Tidak, visualisasi seperti ini rawan terjadi manipulasi data (cherry-picked) demi memenangkan satu metode secara visual. |
| Apa solusinya? | Sumbu Y (Y-axis) wajib diset dan dimulai dari angka 0% agar proporsi visualnya jujur, serta wajib menambahkan garis error bar. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: Tidak ada, visualisasi dirancang mulai dari angka nol dan menyertakan indikator variabilitas resmi.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel dan grafik saling melengkapi karena membawa fungsi penyajian yang berbeda. Tabel menyediakan aspek presisi, di mana pembaca riset bisa melihat nilai desimal eksak hingga angka standar deviasi untuk keperluan perhitungan statistik lanjut. Sebaliknya, Grafik menyediakan aspek pola, membantu mata manusia mengenali tren kenaikan, penurunan, atau perbandingan antar variabel secara kilat tanpa harus membaca baris angka satu per satu.
> Pengalaman grafik menyesatkan: Pernah, secara tidak sengaja sewaktu membuat grafik otomatis menggunakan aplikasi spreadsheet (seperti Excel atau WPS Office). Ketika rentang data yang dimasukkan berada di angka tinggi (~80-90%), sistem bawaan aplikasi sering kali memotong sumbu Y (truncated axis) secara otomatis agar grafik terlihat kontras. Tanpa disadari, hal tersebut memicu bias visual yang membuat perbedaan kecil nampak sangat ekstrem. Validasi visual manual dengan mengembalikan sumbu ke angka 0 mutlak diperlukan.