# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 10 Konten Utama (termasuk Title & Closing)
  Time per slide : ~1.5 - 2 menit
  Total time     : 15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Judul & Latar Belakang Komparasi | Slide Judul, Logo Universitas Putra Bangsa | 1.0 min |
| 2 | Masalah Inti: Noise Bahasa Slang | Tangkapan layar ulasan kotor Shopee (Slang)  | 2.0 min |
| 3 | Celah Riset (Gap) & Pertanyaan (RQ) | Tabel Perbandingan Penelitian Terdahulu     | 1.5 min |
| 4 | Alur Metodologi & Preprocessing  | Diagram Alir (Pipeline) Sistem Komputasi    | 2.0 min |
| 5 | Temuan Utama (Tabel Kinerja)     | Tabel Akurasi & F1-Score (Mean ± Std)       | 2.0 min |
| 6 | Tren Visual Penurunan Performa   | Bar Chart + Error Bar (Formal vs Slang)     | 2.0 min |
| 7 | Analisis Kegagalan Model (Failure) | Box Plot Sebaran Distribusi Run Eksperimen  | 1.5 min |
| 8 | Batasan Penelitian & Kesimpulan  | Bullet points ringkas & Rencana Future Work  | 2.0 min |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa membandingkan teks formal dan slang, bukan fokus menaikkan akurasi saja? | [C] Karena ketahanan model terhadap noise tulisan jauh lebih penting untuk implementasi nyata. [E] Data ulasan e-commerce di lapangan didominasi teks slang yang menurunkan akurasi hingga 7%. [R] Menemukan batasan toleransi model terhadap ragam bahasa lebih mendesak bagi efisiensi sistem industri. |
| Method   | Mengapa memilih C4.5 dan Naïve Bayes sebagai objek perbandingan? | [C] Keduanya mewakili dua pendekatan fundamental yang berbeda. [E] Naïve Bayes berbasis probabilitas murni, sementara C4.5 berbasis pohon keputusan non-linear. [R] Perbedaan arsitektur ini krusial untuk dipetakan guna melihat model mana yang paling rentan terhadap distorsi data. |

Latihan:
  Latihan 1: [11 Juli 2026] — Masalah pada manajemen waktu (slide hasil terlalu lama diulas), feedback: percepat transisi antar slide.
  Latihan 2: [12 Juli 2026] — Penyampaian argumen CER sudah mulai tegas, waktu total pas 14.5 menit.

```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Analisis Sentimen Ulasan E-Commerce Menggunakan Naïve Bayes dan C4.5: Studi Komparatif Teks Formal dan Slang. | Title slide dengan identitas mahasiswa (NIM 240202859, UPB). | 1.0 min |
| 2 | Bahasa slang yang tidak terstruktur menurunkan kinerja algoritma secara drastis di lingkungan e-commerce nyata.| Foto komparasi ulasan produk yang rapi vs ulasan penuh singkatan gaul. | 2.0 min |
| 3 | Belum ada studi komparatif mendalam yang memetakan batasan runtuhnya (boundary condition) Naïve Bayes vs C4.5 pada bahasa non-baku Indonesia. | Tabel pemetaan gap penelitian dari 10 jurnal referensi utama. | *1.5 min* |
| 4 | Data melalui pembersihan (cleaning) dan transformasi pemetaan kamus slang (lexicon mapping). | Diagram alir Data Preprocessing Pipeline (WS-13). | 2.0 min |
| 5 | C4.5 secara konsisten mengungguli Naïve Bayes di semua skenario pengujian. | Tabel hasil metrik Mean Accuracy ± Std (WS-12). | 2.0 min |
| 6 | Terjadi penurunan performa yang signifikan pada kedua model saat berpindah dari teks formal ke teks slang. | Diagram batang (Bar Chart) dilengkapi garis Error Bar. | 2.0 min|
| 7 | Naïve Bayes mengalami kegagalan kalkulasi akibat pelanggaran asumsi independensi fitur oleh frasa slang berulang. | Diagram kotak (Box Plot) sebaran nilai 40 run eksperimen. | 1.5min |
| 8 | Kamus pemetaan slang buatan manual menjadi limitasi utama riset ini. | Teks matriks limitasi internal dan eksternal. | 1.5min |
| 9 | Algoritma C4.5 terbukti lebih tangguh dan stabil dibanding Naïve Bayes dalam menangani noise karakteristik teks slang. | Slide ringkasan kontribusi ilmiah & penutup. | 1.0 min|

**Total waktu estimasi:** 15.0 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | *Problem* | Mengapa masalah bahasa slang ini penting diteliti? | Bahasa slang adalah kendala utama klasifikasi teks ulasan di Indonesia. | Jurnal acuan mencatat ulasan Shopee mengandung >40% kata non-baku. | Jika algoritma tidak diuji ketahanan slangnya, model akan gagal total saat dideploy di aplikasi e-commerce riil. |
| 2 | *Method* | Mengapa parameter normalisasi hanya dihitung dari training set? | Untuk menghindari fenomena kebocoran data (data leakage). | Aturan baku data preprocessing (WS-13) melarang pencampuran informasi test set. | Jika parameter TF-IDF dihitung dari seluruh data, hasil akurasi akan tinggi secara semu (bias) dan tidak valid. |
| 3 | Results | Mengapa nilai standar deviasi ($\pm \text{std}$) Naïve Bayes lebih besar pada data slang? | Karena Naïve Bayes tidak stabil menghadapi variasi kata yang tinggi. | Nilai std Naïve Bayes naik dari 1.85% (formal) menjadi 3.10% (slang). | Kosakata slang yang acak mengacaukan pembagian probabilitas kata, membuat performanya fluktuatif di tiap run. |
| 4 | Failure Analysis | Mengapa Anda menyebut penurunan performa ini bukan kegagalan riset? | Karena penemuan batasan model adalah bentuk kontribusi ilmiah. | Hasil uji statistik p-value = 0.012 dan d = 1.82 membuktikan efek penurunan ini nyata. | Mengetahui kapan model itu "runtuh" memberi petunjuk bagi peneliti lain untuk memperbaiki modul penanganan teks di masa depan. |
| 5 | Generalization | Apakah hasil pengujian ini bisa langsung dipakai di domain teks selain e-commerce? | Tidak bisa langsung, harus ada penyesuaian korpus kata. | Karakteristik kata slang produk fashion berbeda dengan slang ulasan politik atau otomotif. | Perbedaan domain akan mengubah distribusi kata, yang tercatat sebagai batasan eksternal (external validity). |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | "Mengapa tidak menggunakan algoritma Deep Learning seperti BERT yang lebih modern?" | "Fokus riset saya adalah mengukur efisiensi algoritma komputasi ringan (C4.5 & Naïve Bayes) pada perangkat dengan spesifikasi terbatas. Hal ini sudah ditegaskan pada batasan masalah di Bab 1." | *[✓] Direct [✓] Data-based [✓] Honest* |
| 2 | "Bagaimana jika data ulasan yang masuk tidak memiliki label sentimen sama sekali?" | "Model yang dilatih menggunakan basis data berlabel dari data training ($n=920$ records hasil cleaning). Data baru tanpa label akan diprediksi kelasnya berdasarkan aturan pohon keputusan C4.5 yang terbentuk." | [✓] Direct [✓] Data-based [✓] Honest |
| 3 | "Apakah kamus bahasa slang yang digunakan sudah divalidasi oleh ahli bahasa?" | "Belum, kamus slang dikompilasi secara mandiri dari riset-riset terdahulu di Google Scholar. Ini adalah keterbatasan construct validity yang dicantumkan dalam draf laporan." | [✓] Direct [✓] Data-based [✓] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Mempertahankan alasan ilmiah mengapa nilai standar deviasi Naïve Bayes melonjak tinggi ketika membaca dataset ulasan teks slang.

**Apa yang perlu disiapkan lebih baik:**
> Memperdalam pemahaman matematika dasar probabilitas bersyarat Naïve Bayes terhadap penanganan frekuensi kata bernilai nol (Laplace Smoothing).

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Kegagalan atau penurunan performa suatu algoritma (failure analysis) dalam eksperimen ternyata bukanlah aib riset yang harus disembunyikan atau dimanipulasi angkanya. Mengetahui batasan operasional (boundary condition) suatu metode justru merupakan temuan ilmiah yang sangat mahal dan berharga bagi perkembangan ilmu pengetahuan.
**Yang akan selalu diterapkan:**
> Menjaga konsistensi internal (Red Thread) sejak awal menentukan pertanyaan penelitian (RQ), desain variabel (IV & DV), hingga penyajian hasil. Saya tidak akan lagi melakukan over-preprocessing data atau visualisasi yang bias (seperti memotong sumbu Y grafik) demi sekadar membuat hasil penelitian terlihat "sempurna" di mata penguji.
