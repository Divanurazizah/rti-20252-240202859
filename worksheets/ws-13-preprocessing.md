# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

PREPROCESSING LOG

Dataset           : Dataset Ulasan Produk E-Commerce (Shopee/Casual & Formal)
Jumlah data awal  : 1.000 records ulasan teks

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 15 ulasan   | Listwise deletion | Data kosong < 5% dan bersifat acak, aman untuk dihapus. |
| Duplikat| 45 ulasan   | Identifikasi & hapus | Ulasan duplikat akibat spam/bot dibersihkan agar tidak bias. |
| Error   | 20 ulasan   | Encoding conversion | Memperbaiki karakter abstrak/emoji rusak menjadi format UTF-8 baku. |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Case Folding & Filtering | Teks Ulasan | Mengubah huruf kecil semua dan menghapus angka/tanda baca. | Menyederhanakan struktur teks sebelum ekstraksi fitur. |
| Normalisasi Slang | Teks Ulasan | Mengubah kata informal (misal: "yg", "bgt") menjadi baku ("yang", "banget"). | Mengurangi variabilitas karakteristik teks slang agar performa model stabil. |

Normalization:
  Metode    : Tidak melakukan normalisasi numerik (seperti Min-Max/Z-Score)
  Alasan    : Data berupa representasi teks hasil TF-IDF / Bag of Words, bukan data numerik kontinu berskala besar.
  Parameter : (dihitung dari: tidak menerapkan)

Leakage Check:
  [x] Parameter normalisasi dari training set saja (untuk pembobotan TF-IDF)
  [x] Tidak ada informasi test set dalam preprocessing
  [x] Cross-validation dilakukan setelah split

Jumlah data akhir : 920 records ulasan teks
Script tersedia   : [x] Ya → path: src/preprocessing_text.py | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing value pada kolom ulasan| 15 dari 1.000 (1.5%) | Listwise deletion | < 5%, distribusi data hilang secara acak (MCAR). |
| Duplikasi data teks (Spam ulasan) | 45 dari 1.000 (4.5%) | Verifikasi & hapus data duplikat | Mencegah overfitting pada model C4.5 dan Naïve Bayes. |
| Karakter encoding rusak (Emoji/Simbol) | 20 dari 1.000 (2.0%) | Standardisasi format ke UTF-8 | Memastikan tokenisasi teks berjalan lancar tanpa error pembacaan kata. |

**Jumlah data sebelum cleaning:** 1.000 records
**Jumlah data setelah cleaning:** 920 records
**Persentase data yang hilang/berubah:** 8.0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Teks Ulasan (Bahasa Slang) | Variatif (Kata non-baku) | Long-tailed (Banyak variasi kata) | Ya | Text Normalization (Lexicon Mapping) | Menyamakan kata slang ke bentuk baku berdasarkan kamus formal. |
| Bobot Fitur TF-IDF | 0.0-1.0 | Right-skewed | Tidak | Tidak perlu normalisasi numerik | Nilai pembobotan kata sudah otomatis berada dalam rentang baku [0, 1]. |


**Apakah normalisasi diperlukan?** [x] Ya / [ ] Tidak
**Justifikasi:**
> Normalisasi berbasis rumus matematika (seperti Min-max atau Z-score) tidak diperlukan karena fitur pembobotan TF-IDF sudah berada pada rentang yang aman. Namun, normalisasi linguistik (bahasa slang) mutlak diperlukan untuk mengubah kosakata informal menjadi baku agar algoritma Naïve Bayes dan C4.5 tidak salah mengelompokkan makna sentimen.

**Leakage check:**
- [x] Parameter dihitung dari training set saja
- [x] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

PREPROCESSING SUMMARY

1. Dataset: Dataset Ulasan Produk E-Commerce Indonesia
2. Data awal: 1.000 records, 2 features (Teks Ulasan & Label Sentimen)
3. Cleaning:
   - Missing values: 15 kasus, metode: Listwise deletion
   - Duplikat: 45 kasus, tindakan: Verifikasi dan hapus
   - Error: 20 kasus, tindakan: Konversi encoding ke UTF-8 baku
4. Transformation: Case Folding, Filtering (Stopword Removal), Tokenization, dan Stemming.
5. Normalisasi: Text Normalization (Kamus Bahasa Slang), parameter dari Training Set (Kamus TF-IDF).
6. Data akhir: 920 records, 2 features
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, dulu saya sering berpikir bahwa semua data hasil eksperimen wajib melewati normalisasi matematika seperti Min-Max atau Z-Score hanya karena sering melihatnya di tutorial atau draf penelitian lain. Padahal untuk kasus Analisis Sentimen berbasi teks, data fitur seperti TF-IDF sudah otomatis berada di rentang [0,1], sehingga normalisasi numerik justru tidak dibutuhkan.

Risiko dari over-preprocessing adalah distorsi informasi asli. Jika kita terlalu berlebihan membersihkan data—misalnya menghapus terlalu banyak kata unik (lewat stopword removal yang terlalu ketat) atau memaksakan normalisasi skala pada data yang sudah konsisten—kita bisa kehilangan karakteristik unik dari teks ulasan informal itu sendiri. Akibatnya, model Naïve Bayes atau C4.5 akan kehilangan konteks penting, yang berujung pada penurunan akurasi klasifikasi secara drastis saat mendeteksi sentimen riil di lapangan.
