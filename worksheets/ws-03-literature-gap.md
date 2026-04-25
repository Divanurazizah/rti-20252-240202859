# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Analisis Kepuasan Pelanggan E-Commerce
Database   : Google Scholar
Query      : e-commerce customer satisfaction decision tree classification
Tahun      : 2020-2024
Hasil awal : 45 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study         | Tahun | Method        | Data             | Result  | Limitation                    |
| ------------- | ----- | ------------- | ---------------- | ------- | ----------------------------- |
| Rahman et al. | 2023  | Decision Tree | Review produk    | Acc 86% | Overfitting                   |
| Lee et al.    | 2022  | Decision Tree | Data pelanggan   | Acc 87% | Data terbatas                 |
| Sari et al.   | 2023  | Decision Tree | Tokopedia review | Acc 84% | Kurang akurat di teks panjang |
| Chen et al.   | 2024  | Decision Tree | E-commerce       | Acc 88% | Kurang stabil                 |
| Ahmad et al.  | 2021  | Decision Tree | Review           | Acc 85% | Data tidak bersih             |


Pola yang ditemukan:
  Metode dominan     : Decision Tree
  Dataset umum       : Review produk pelanggan
  Limitasi berulang  : Data masih sedikit, overfitting (model terlalu "menghafal"), akurasi belum stabil, data teks tidak rapi

GAP IDENTIFICATION

Gap 1: [Jenis: Data Gap + Context Gap]
  Deskripsi    : Dataset yang digunakan masih terbatas dan belum fokus ke e-commerce Indonesia secara spesifik
  Bukti        : Banyak penelitian menggunakan data umum atau dataset luar
  Signifikansi : Model bisa tidak optimal saat diterapkan pada kondisi nyata di Indonesia

Gap 2: [Jenis: Performance Gap]
  Deskripsi    : Akurasi Decision Tree belum stabil
  Bukti        : Akurasi berkisar 83%–88%
  Signifikansi : Hasil klasifikasi belum cukup kuat untuk keputusan bisnis

Baseline Selection:
| Baseline      | Relevansi | Representatif | Source      |
|---------------|-----------|---------------|-------------|
| Decision Tree | Klasifikasi kepuasan | Metode umum | Rahman 2023 |
| Naive Bayes   | Sama-sama klasifikasi teks | Banyak digunakan | Sari 2023 |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Klasifikasi kepuasan pelanggan e-commerce
**Query pencarian:** klasifikasi kepuasan pelanggan e-commerce decision tree
**Database:** Google Scholar

| # | Study         | Tahun | Method | Dataset    | Result  | Limitasi     |
| - | ------------- | ----- | ------ | ---------- | ------- | ------------ |
| 1 | Rahman et al. | 2023  | DT     | Review     | Acc 86% | Overfitting  |
| 2 | Lee et al.    | 2022  | DT     | Pelanggan  | Acc 87% | Data kecil   |
| 3 | Sari et al.   | 2023  | DT     | Tokopedia  | Acc 84% | Teks panjang |
| 4 | Chen et al.   | 2024  | DT     | E-commerce | Acc 88% | Tidak stabil |
| 5 | Ahmad et al.  | 2021  | DT     | Review     | Acc 85% | Data noise   |


**Pola yang terlihat — Metode dominan:** Decision Tree
**Limitasi yang berulang:** Overfitting & data terbatas
---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [✔] Ya / [ ] Tidak | Akurasi belm stabil|
| Method Gap | [] Ya / [✔] Tidak | Metode sudah umum |
| Data Gap | [✔] Ya / [ ] Tidak | Dataset terbatas |
| Context Gap | [✔] Ya / [ ] Tidak | Kurang fokus di indonesia |

**Gap utama yang dipilih:** Data + Context Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Dataset yang tidak representatif menyebabkan model kurang optimal saat digunakan di e-commerce Indonesia.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline      | Mengapa Relevan                      | Mengapa Representatif | Apakah SOTA? | Sumber      |
| - | ------------- | ------------------------------------ | --------------------- | ------------ | ----------- |
| 1 | Decision Tree | Digunakan untuk klasifikasi kepuasan | Metode umum           | Tidak        | Rahman 2023 |
| 2 | Naive Bayes   | Sama-sama klasifikasi teks           | Banyak digunakan      | Tidak        | Sari 2023   |


**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [✔ ] Tidak
> Justifikasi: Karena kedua metode merupakan metode umum yang sering digunakan dalam penelitian, sehingga perbandingan tetap adil dan tidak termasuk straw man.
---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Pernyataan “belum ada yang meneliti” tidak cukup tanpa bukti. Research gap yang benar harus didasarkan pada beberapa penelitian yang menunjukkan kekurangan yang sama. Cara membuktikannya adalah dengan mencari dan membandingkan beberapa paper, lalu melihat pola kelemahan yang sering muncul.