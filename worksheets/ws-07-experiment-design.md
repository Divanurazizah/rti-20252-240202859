# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Bagaimana pengaruh tingkat representativitas dataset (lokal vs umum) terhadap performa model klasifikasi sentimen ulasan E-Commerce?
Hypothesis        : Dataset ulasan lokal menghasilkan performa klasifikasi sentimen (F1-Score) yang lebih tinggi dibandingkan dataset umum karena memiliki representasi bahasa dan konteks lokal yang lebih akurat.
Tipe Eksperimen   : [✓] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control |  Pengujian model menggunakan dataset ulasan e-commerce yang bersifat umum/publik dari literatur global.         |    Dataset Umum (Global/Publik)      |  Algoritma Naïve Bayes, porsi split data 80:20, pipeline preprocessing standar.      |
| Treatment |  Pengujian model menggunakan dataset ulasan e-commerce lokal yang spesifik menggunakan bahasa Indonesia sehari-hari.       |    Dataset Lokal      |      Algoritma Naïve Bayes, porsi split data 80:20, pipeline preprocessing standar.       |

Fairness Checklist:
[ ✓ ] Dataset identik untuk semua kondisi
[ ✓ ] Preprocessing setara
[ ✓ ] Tuning effort setara
[ ✓ ] Environment identik
[ ✓ ] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Terjadinya ketidakseimbangan kelas (imbalance data) antara jumlah ulasan positif dan negatif yang berbeda antar dataset.          |   Menerapkan teknik penyeimbangan data seperti stratified sampling saat melakukan split data training dan testing       |
| External    | Karakteristik ulasan lokal pada satu platform e-commerce belum tentu mewakili platform e-commerce lainnya.                | Mengambil data ulasan dari beberapa kategori produk dan merchant yang bervariasi agar lebih umum.         |
| Construct   | Metrik akurasi murni bisa menipu jika sebaran data ulasan condong ke salah satu sentimen saja.                |   Menggunakan F1-Score sebagai metrik primer karena mengukur keseimbangan antara precision dan recall.       |
| Conclusion  |  umlah sampel ulasan terlalu sedikit sehingga perbedaan performa terjadi karena faktor kebetulan.               |   Memastikan ukuran sampel (sample size) cukup besar (misal, minimal 1000 ulasan per dataset).       |

Statistical Plan:
  Uji statistik   : Paired t-test (jika data berdistribusi normal) atau Wilcoxon Signed-Rank Test (jika data tidak normal).
  Justifikasi      : Digunakan untuk membandingkan dua rata-rata skor performa (F1-Score) dari model klasifikasi yang sama namun diuji pada dua kondisi dataset yang berbeda (berpasangan), yaitu dataset lokal dan dataset umum.
  Alpha            : 0.05
  Effect size min  : Cohen's d > 0.5

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah penggunaan dataset ulasan lokal memberikan performa klasifikasi yang lebih baik dibandingkan dataset umum pada sentimen E-Commerce?
**Tipe eksperimen:** [ ] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Model dilatih dan diuji menggunakan dataset ulasan e-commerce bersifat umum yang biasa digunakan di riset publik. | Dataset Umum | Algoritma Naïve Bayes, pembagian data 80:20, tokenisasi standar, random state seed 42. |
| Treatment | Model dilatih dan diuji menggunakan dataset ulasan lokal hasil penambangan opini pengguna e-commerce Indonesia. | Dataset Lokal | Algoritma Naïve Bayes, pembagian data 80:20, tokenisasi standar, random state seed 42. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Meskipun sumber teks berbeda, jumlah total baris ulasan dan proporsi label kelas disamakan secara ketat antara kedua kelompok data. |
| Preprocessing setara | ✅ | Kedua kelompok data melewati jalur pembersihan teks (case folding, filtering, dan tokenizing) yang menggunakan fungsi kode yang sama. |
| Tuning effort setara | ✅ | Algoritma Naïve Bayes pada kedua kondisi menggunakan parameter bawaan (default) yang sama tanpa ada optimasi sepihak. |
| Environment identik | ✅ | Seluruh eksperimen dijalankan pada perangkat keras, sistem operasi, dan versi library Python (Scikit-Learn) yang sama. |
| Metrik evaluasi sama | ✅ | Evaluasi performa akhir untuk kedua kondisi sama-sama diukur menggunakan F1-Score, Precision, dan Recall. |

**Ada yang tidak fair?** [ ] Ya / [✅] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Adanya bias saat pelabelan sentimen ulasan secara manual | Menggunakan pedoman anotasi (annotation guidelines) yang jelas atau memvalidasi label menggunakan cross-check antar-anator. |
| External | Bahasa ulasan lokal cepat berubah seiring tren slang/bahasa gaul baru di internet. | Menggunakan dataset ulasan yang diambil dalam rentang waktu yang relatif baru dan mencakup variasi kata gaul |
| Construct | Tahap preprocessing yang terlalu ketat justru bisa menghapus kata-kata kunci lokal yang krusial untuk sentimen. | Menghindari penggunaan stopword removal bawaan bahasa asing yang tidak relevan dengan struktur teks lokal. |
| Conclusion | Kesimpulan diambil hanya dari satu kali run eksperimen sehingga rawan bias variasi acak | Melakukan pengujian ulang menggunakan metode K-Fold Cross Validation (misal K=5 atau K=10) untuk mendapatkan rata-rata statistik yang stabil. |

**Ancaman mana yang paling sulit dimitigasi?** External Validity
**Mengapa?**
> Gaya bahasa, singkatan, dan cara konsumen Indonesia menulis ulasan di e-commerce sangat dinamis dan beragam di setiap daerah. Membuat satu dataset lokal yang benar-benar bisa mewakili seluruh populasi pengguna internet di Indonesia secara mutlak adalah hal yang sangat menantang.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah perbandingannya dilakukan secara adil (fair comparison)? (Yaitu apakah baseline juga dioptimalkan dengan tuning effort, struktur data, dan lingkungan komputasi yang setara, ataukah sengaja dibiarkan menggunakan parameter standar agar metode usulan terlihat lebih unggul?)
2. pakah dataset yang digunakan untuk pengujian sama persis? (Seringkali sebuah metode terlihat sangat unggul karena diuji pada dataset yang berbeda atau dataset yang sudah dimodifikasi secara sepihak sehingga menguntungkan algoritma tertentu.)
3. Bagaimana signifikansi statistiknya? (Apakah klaim keunggulan tersebut didukung oleh uji validitas statistik yang kuat seperti p-value, atau sebenarnya selisih keunggulannya sangat tipis dan bisa terjadi hanya karena faktor kebetulan/acak?)
