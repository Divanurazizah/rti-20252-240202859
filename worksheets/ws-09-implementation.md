# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : intel core i5-8250U
  RAM     : 8 GB
  GPU     : N/A (CPU-only komputasi statistik deskriptif)
  Storage : SSD 256 GB / 512 GB

Software:
  OS        : ____________________
  Runtime   : ____________________
  Framework : ____________________

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
|         |         |        |               |
|         |         |        |               |

Konfigurasi:
  Config file     : ____________________
  Random seed     : ____________________
  Hyperparameters : ____________________

Reproducibility Check:
  [ ] Dependency terdokumentasi (requirements.txt / lock file)
  [ ] Seed ditetapkan di semua level (Python, NumPy, framework)
  [ ] Config di version control
  [ ] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i5-8250U |
| RAM | 8 GB  |
| GPU | N/A (Studi Literatur Kuantitatif) |
| OS | Windows 11 |
| Runtime | Google Chrome  |
| Framework | PRISMA Statement Framework (Protokol Penyaringan Literatur) |
| Random Seed | non random |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| Google Scholar | engine akses 2026 | Database utama untuk mencari dan mengunduh paper klasifikasi sentimen e-commerce Indonesia. |
| wps office/excel | v12.1.0 | Media pengolahan data instrumen riset untuk mencatat nilai akurasi, F1-Score, dan ukuran dataset.  |
| zotero | v6.0 | Manajemen referensi, menyimpan metadata paper, dan melakukan deteksi otomatis terhadap paper yang duplikat. |
| Publish | v8.8 | Tool otomatisasi untuk menarik metadata ratusan paper sekaligus dari Google Scholar berdasarkan kata kunci riset. |
| harzing's pop loader | default | Membantu mengeksport metadata pencarian ke format .RIS atau .CSV untuk dianalisis di Excel. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | Deterministic Query | Jumlah paper lolos screening & Nilai rata-rata F1-Score | — |
| 2 | Deterministic Query | Jumlah paper lolos screening & Nilai rata-rata F1-Score | [ x ] Ya / [ ] Tidak |
| 3 | Deterministic Query | Jumlah paper lolos screening & Nilai rata-rata F1-Score | [ x ] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> ___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [ x ] Random seed di-set di semua level
- [ x ] Tidak ada background process yang mengganggu
- [ x ] Cache dibersihkan antar-run
- [ x ] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Meta-Analisis Dampak Karakteristik Dataset Terhadap Stabilitas Performa Algoritma Sentimen E-Commerce di Indonesia

## 1. Environment
> Aplikasi Utama: Publish or Perish v8.8 & Mendeley Desktop
> Spreadsheet: WPS Office Excel / Microsoft Excel (.xlsx)
> Mesin Pencari: Google Scholar Indexed
> Protokol: PRISMA Framework 2020

## 2. Installation
> Install software Harzing's Publish or Perish versi terbaru.
> Install Mendeley Desktop atau Zotero untuk manajemen sitasi.
> Siapkan template file pengolah angka (Excel) yang sudah dikonfigurasi rumus rata-rata statistik deskriptifnya.

## 3. Data
>vSumber Data: 10-15 Paper Ilmiah mengenai klasifikasi sentimen e-commerce lokal.
> Format: Dokumen PDF (untuk dibaca) dan file metadata `.RIS` / `.CSV`.
> Batasan Data: Publikasi dalam rentang waktu tahun 2020 - 2026.

## 4. Execution
> Buka Publish or Perish, pilih Google Scholar.
> Masukkan kata kunci pencarian pada kolom title: 
   "sentimen" AND "e-commerce" AND "C4.5" OR "Naïve Bayes"
> Batasi tahun: 2020-2026, lalu klik 'Search'.
> Ekspor hasil pencarian ke format Excel (.csv) untuk disaring manual berdasarkan kriteria PRISMA.

## 5. Configuration
> Inklusi 1: Paper wajib menampilkan metrik evaluasi F1-Score atau Accuracy secara jelas.
> Inklusi 2: Objek riset wajib berupa ulasan e-commerce berbahasa Indonesia.
> Eksklusi 3: Paper review, bab utuh tanpa ringkasan jurnal, dan paper duplikat langsung dieliminasi.

## 6. Expected Output
> File `matriks_ekstraksi.xlsx` berisi data rekapitulasi: Nama Penulis, Tahun, Algoritma, Ukuran Dataset, Karakteristik Bahasa (Formal/Slang), dan Skor F1-Score.
> Diagram Alir PRISMA (format .png) yang menunjukkan proses penyaringan jumlah paper dari awal hingga akhir.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [ x ] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Rumus atau formula spesifik mengenai cara saya mengelompokkan secara objektif mana dataset paper yang masuk kategori "Bahasa Formal" dan mana yang "Bahasa Slang/Lokal" belum tertulis secara matematis di file Excel. 