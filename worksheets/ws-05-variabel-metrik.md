# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Bagaimana pengaruh tingkat representativitas dataset (lokal vs umum) terhadap performa model klasifikasi sentimen ulasan E-Commerce?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|    Representativitas Dataset      | IV   |    Sumber data ulasan    |   Dataset Lokal vs Umum     |  Nominal  |   -     |         Mengelompokkan data menjadi dua kelompok uji: dataset ulasan lokal Indonesia dan dataset ulasan umum.      | Untuk melihat apakah konteks bahasa lokal berpengaruh pada pemahaman model. |
|      Performa Klasifikasi    | DV   |  Ketepatan prediksi sentimen      |  Accuracy, Precision, Recall, F1-Score  | Ratio | Desimal (0-1) | Menghitung hasil perbandingan antara label prediksi model dengan label asli pada data testing menggunakan confusion matrix. | Metrik ini memberikan gambaran objektif mengenai seberapa cerdas model mengenali ulasan. |
|       Algoritma & Preprocessing   | CV   |    Standarisasi proses    | Decision Tree  | Nominal | - |  Mengunci jenis algoritma dan langkah pembersihan teks (seperti case folding dan filtering) agar tetap sama di semua uji coba.  |   Menjamin bahwa perbedaan hasil murni karena dataset, bukan karena perubahan algoritma.  |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [✓ ] Setiap langkah terdokumentasi
  [✓ ] Tidak ada "lompatan logis"
  [✓ ] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah penggunaan dataset ulasan lokal memberikan performa klasifikasi yang lebih baik dibandingkan dataset umum pada E-commerce?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Sumber Data | IV | Representativitas | Dataset Lokal vs Umum | Nominal | — |
| Efektivitas Prediksi | DV | Performa Model | Skor F1-Score | Ratio | Desimal |
| Algoritma | CV | Konsistensi Metode | Naïve Bayes | Nominal | — |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [ ✓ ] Tidak
> Jika ya, di mana? Pengukuran ini konsisten karena penggunaan metrik statistik seperti F1-Score secara langsung mampu menguantifikasi kemampuan model dalam mengenali pola sentimen pada teks ulasan.

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | F1-Score sangat mewakili kualitas model karena menyeimbangkan kesalahan prediksi positif maupun negatif. |
| Sensitive | 4 | Metrik ini cukup peka untuk menangkap perbedaan kecil saat model memproses kosakata lokal yang unik. |
| Feasible | 5 | Data performa sangat mudah didapatkan secara otomatis melalui proses pengujian program (coding). |

**Apakah perlu secondary metric?** [✓ ] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Perlu menyertakan Accuracy sebagai metrik pendukung untuk melihat performa prediksi secara keseluruhan di samping keseimbangan precision-recall.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika ulasan yang diuji sangat pendek dan hanya berisi kata kunci sederhana (seperti "oke" atau "jelek"), model akan dengan sangat mudah mencapai skor 1.0, sehingga pengaruh dataset lokal tidak lagi terlihat perbedaannya.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ya, setiap ulasan harus memiliki teks dan label sentimen. | Menghapus baris ulasan yang memiliki nilai kosong atau rusak. |
| Consistency | *Apakah ada kontradiksi internal?* | Ada risiko ketidakcocokan antara teks ulasan dan label rating. | Melakukan seleksi data (data cleaning) untuk membuang ulasan yang isinya tidak nyambung dengan labelnya. |
| V alidity | *Apakah benar-benar mengukur yang dimaksud?* | Ya, teks ulasan adalah sumber asli opini pengguna. | Menggunakan tahap preprocessing untuk menghilangkan karakter non-teks yang tidak berguna. |
| Representativeness | *Apakah sampel mewakili populasi target?* | Ya, jika ulasan mencakup berbagai jenis produk. | Mengambil data ulasan dari berbagai kategori barang agar hasil penelitian tidak bias pada satu jenis produk saja. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap sebagai p-hacking karena peneliti bisa sengaja memilih metrik yang hanya menguntungkan hasil penelitian mereka agar terlihat sukses. Hal ini merusak kejujuran ilmiah. Perbedaannya dengan eksplorasi data yang sah adalah eksplorasi bertujuan untuk mempelajari pola baru secara transparan tanpa mengubah parameter keberhasilan utama yang sudah ditentukan di awal penelitian.
