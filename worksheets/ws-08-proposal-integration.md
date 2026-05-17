# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment)
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [ ] Problem → Gap: masalah terdokumentasi di literatur
  [ ] Gap → RQ: pertanyaan menjawab gap spesifik
  [ ] RQ → Hypothesis: hipotesis memprediksi jawaban
  [ ] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [ ] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [ ] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [ ] Istilah sama di semua bagian
  [ ] Variabel di RQ = variabel di hipotesis = metrik di desain
  [ ] Scope tidak berubah dari masalah ke eksperimen

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi |          |           |          |      |
| Specificity |        |           |          |      |
| Feasibility |        |           |          |      |
| Rigor     |          |           |          |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Klaim performa akurasi antar algoritma klasifikasi sentimen e-commerce di Indonesia sangat bervariasi dan tidak konsisten antar penelitian. Hal ini menyulitkan para praktisi TI untuk memilih algoritma yang paling optimal karena adanya perbedaan karakteristik data dasar yang digunakan oleh tiap peneliti. |
| Gap | WS-03 | Terdapat Methodological Gap di mana belum ada studi komparatif sistematis yang mengevaluasi secara menyeluruh bagaimana faktor eksternal (gaya bahasa ulasan dan ukuran dataset) mendistorsi validitas klaim keunggulan algoritma pada literatur terbuka. |
| RQ | WS-04 | Bagaimana dampak karakteristik dataset (ukuran sampel ulasan dan tingkat formalitas gaya bahasa) terhadap variasi tingkat akurasi algoritma klasifikasi sentimen yang dilaporkan dalam literatur ilmiah? |
| Hipotesis | WS-04 | H₁: Variasi akurasi algoritma yang dilaporkan dalam literatur dipengaruhi secara signifikan oleh tingkat formalitas bahasa pada dataset yang diuji (bahasa baku vs bahasa slang/lokal), bukan hanya disebabkan oleh keunggulan internal struktur algoritmanya. |
| Variabel & Metrik | WS-05 | Independent Variable (IV) = Karakteristik dataset pada paper (Ukuran sampel & Kategori bahasa); Dependent Variable (DV) = Nilai performa yang dilaporkan di dalam paper (Metrik nilai $F_1\text{-Score}$ atau Accuracy). |
| Sistem | WS-06 | "Sistem" atau artefak dalam riset ini berupa Protokol Ekstraksi Data berbasis kriteria inklusi-eksklusi standar (PRISMA framework) untuk mengumpulkan, menyaring, dan mengekstraksi parameter paper secara objektif dari database Google Scholar. |
| Desain Eksperimen | WS-07 | Eksperimen dilakukan dalam bentuk studi meta-analisis terhadap 10-15 paper eksperimen sentimen e-commerce di Indonesia, mengelompokkan data performanya berdasarkan karakteristik teks, lalu diuji distribusinya menggunakan analisis statistik deskriptif. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Masalah variasi klaim akurasi di literatur melahirkan gap berupa kebutuhan akan studi komparatif sistematis untuk menguji faktor penyebab distorsi tersebut. |
| Gap → RQ | ✅ | RQ secara langsung menanyakan dampak karakteristik dataset untuk menjawab gap metodologis yang belum diteliti oleh peneliti terdahulu. |
| RQ → Hypothesis |✅ | Hipotesis memberikan dugaan ilmiah yang searah dengan RQ, yaitu variasi akurasi dipengaruhi oleh faktor formalitas bahasa pada dataset. |
| Hypothesis → Metric | ✅ | Variabel karakteristik bahasa dan performa model diturutkan menjadi metrik pengelompokan teks (formal vs slang) dan metrik rasio ($F_1\text{-Score}$ / Accuracy). |
| Metric → System | ✅ | Protokol ekstraksi data (Sistem) dirancang khusus untuk mencatat metrik bahasa dan nilai akurasi dari setiap paper ke dalam tabel spreadsheet |
| System → Experiment | ✅ | Protokol penyaringan tersebut dijalankan sebagai instrumen utama untuk mengumpulkan dan membedah data dari 10-15 paper secara objektif. |

**Koneksi mana yang paling lemah?** Hypothesis → Metric
**Bagaimana cara memperkuatnya?**
> Membuat batasan operasional yang jelas di Bab 5 mengenai apa yang dikategorikan sebagai dataset "Bahasa Formal" dan "Bahasa Slang/Lokal" (misalnya berdasarkan persentase kemunculan kata tidak baku/singkatan yang disebutkan di dalam paper yang di-review).

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [ X ] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Seluruh 6 koneksi vertikal terhubung erat dari atas ke bawah tanpa ada lompatan logika. Benang merah (red thread) sangat jelas. |
| Specificity | 3 | Metrik performa ($F_1\text{-Score}$) dan jumlah batasan sampel data yang akan dianalisis sudah ditentukan angkanya secara pasti, yaitu minimal  |
| Feasibility | 3 | Timeline sangat realistis (1-2 bulan) karena tidak ada risiko gagal koding atau error program. Fokus sepenuhnya pada membaca, merekap, dan menganalisis data di Excel. |
| Rigor | 2 | Menggunakan metode penyaringan literatur formal yang terstruktur sehingga terhindar dari bias pemilihan paper (bukan asal pilih paper yang disukai). |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** WS-01 dan WS-02 karena sejak awal materi tersebut melatih cara berpikir kritis, membaca, dan mengevaluasi argumen dari paper ilmiah tanpa dibebani keharusan membuat kode program.
**Bagian tersulit:** Mengubah pola pikir (mindset) bahwa riset Teknologi Informasi tidak selalu harus menghasilkan produk berupa aplikasi atau baris kode baru, melainkan bisa berbentuk evaluasi kritis terhadap pengetahuan komputasi yang sudah ada.
**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, saya akan konsisten memilih jalur analisis literatur (Meta-Analysis) ini sejak minggu pertama. Dengan begitu, saya bisa mengumpulkan paper berkualitas lebih banyak dan mempermatang kriteria penyaringannya sejak dini tanpa membuang waktu kebingungan di antara urusan koding.
> ___________________________________________________
