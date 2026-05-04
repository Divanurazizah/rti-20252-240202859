# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Teknologi Informasi(Data Mining/Machine Learning)
  Konteks  : Analisis kepuasan pelanggan pada platform e-commerce

System Context
  Input       : Data review pelanggan (teks ulasan, rating)
  Process     : Preprocessing data teks (cleaning, tokenizing) dan proses klasifikasi menggunakan algoritma (Decision Tree / Naive Bayes)
  Output      : Label klasifikasi kepuasan pelanggan (puas / tidak puas)
  Outcome     : Informasi tingkat kepuasan pelanggan untuk mendukung pengambilan keputusan bisnis
  Constraints : Dataset terbatas, data tidak seimbang, adanya noise pada data teks
  Stakeholders: Penjual, platform e-commerce, dan pelanggan

Fenomena → Problem
  Fenomena yang diamati             : Banyak pelanggan memberikan review pada platform e-commerce
  Gejala (symptom) yang terukur     : Hasil klasifikasi kepuasan pelanggan belum stabil (akurasi berkisar 83%–88%)
  Masalah yang didiagnosis          : Dataset yang digunakan terbatas, tidak representatif, dan mengandung noise
  Masalah riset (researchable)      : Belum ada analisis penggunaan dataset yang lebih representatif untuk meningkatkan performa klasifikasi kepuasan pelanggan pada e-commerce Indonesia
  Variabel yang terukur             : Accuracy (%), Precision, Recall, F1-score


Problem Quality Check
  [✔] Clarity — Apakah satu orang membaca akan paham?
  [✔] Measurability — Apakah ada metrik kuantitatif?
  [✔] Relevance — Apakah penting untuk domain?
  [✔] Relevance — Apakah penting untuk domain?
  [✔] Testability — Apakah bisa gagal?
  [✔] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Penggunaan metode klasifikasi untuk menganalisis kepuasan pelanggan pada platform e-commerce semakin meningkat, namun performa model yang dihasilkan masih belum stabil dengan akurasi yang berkisar antara 83% hingga 88%. Permasalahan ini diduga disebabkan oleh keterbatasan dataset yang digunakan, seperti jumlah data yang sedikit, tidak representatif, serta adanya noise pada data review pelanggan. Selain itu, sebagian besar penelitian masih menggunakan dataset umum yang belum tentu sesuai dengan konteks e-commerce di Indonesia. Hingga saat ini, belum terdapat penelitian yang secara khusus menganalisis pengaruh penggunaan dataset yang lebih representatif terhadap peningkatan performa klasifikasi kepuasan pelanggan. Oleh karena itu, penelitian ini bertujuan untuk menganalisis performa metode klasifikasi dengan menggunakan dataset yang lebih representatif, dengan metrik evaluasi berupa accuracy, precision, recall, dan F1-score.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Klasifikasi kepuasan pelanggan e-commerce

| Tahap                          | Hasil                                                                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Reality                        | Banyak pelanggan memberikan review pada platform e-commerce                                                                         |
| Observed Issue (Symptom)       | Akurasi klasifikasi kepuasan pelanggan belum stabil (83%–88%)                                                                       |
| Diagnosed Problem (Root Cause) | Dataset terbatas, tidak representatif, dan mengandung noise                                                                         |
| Researchable Problem           | Belum ada studi yang mengkaji pengaruh penggunaan dataset yang lebih representatif terhadap performa klasifikasi kepuasan pelanggan |
| Measurable Variable            | Accuracy, Precision, Recall, F1-score                                                                                               |

**Apakah terjebak solution-first thinking?** [ ] Ya / [ ] Tidak
Tidak


---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen     | Deskripsi                                                        |
| ------------ | ---------------------------------------------------------------- |
| Input        | Data review pelanggan (teks dan rating)                          |
| Process      | Preprocessing teks dan klasifikasi (Decision Tree / Naive Bayes) |
| Output       | Hasil klasifikasi (puas / tidak puas)                            |
| Outcome      | Insight kepuasan pelanggan                                       |
| Constraints  | Dataset terbatas, data tidak bersih, bahasa tidak baku           |
| Stakeholders | Penjual, platform e-commerce, pelanggan                          |


**Komponen mana yang paling relevan dengan masalah riset?** Input (dataset) dan Process (klasifikasi)

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria      | Skor(1-5) | Justifikasi              |
| ------------- | ---- | ------------------------ |
| Clarity       | 5    | Sudah jelas dan spesifik |
| Measurability | 5    | Metrik lengkap           |
| Relevance     | 5    | Sangat relevan           |
| Testability   | 5    | Bisa diuji eksperimen    |
| Impact        | 5    | Berdampak pada bisnis    |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
Penggunaan metode klasifikasi untuk menganalisis kepuasan pelanggan pada platform e-commerce semakin berkembang, namun performa model yang dihasilkan masih belum stabil dengan akurasi yang berkisar antara 83% hingga 88%. Permasalahan ini diduga disebabkan oleh keterbatasan dataset yang digunakan, seperti jumlah data yang sedikit, tidak representatif, serta adanya noise pada data review pelanggan. Selain itu, sebagian besar penelitian masih menggunakan dataset umum yang belum tentu sesuai dengan konteks e-commerce di Indonesia. Hingga saat ini, belum terdapat penelitian yang secara khusus menganalisis pengaruh penggunaan dataset yang lebih representatif terhadap peningkatan performa klasifikasi kepuasan pelanggan. Oleh karena itu, penelitian ini bertujuan untuk menganalisis performa metode klasifikasi dengan menggunakan dataset yang lebih representatif, dengan metrik evaluasi berupa accuracy, precision, recall, dan F1-score.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
Masalah dalam coding seperti bug atau error berfokus pada memperbaiki sistem agar dapat berjalan dengan benar. Sementara itu, masalah dalam riset tidak hanya berfokus pada penyelesaian, tetapi pada pemahaman dan pembuktian suatu fenomena secara ilmiah. Dalam riset, masalah harus dirumuskan secara sistematis, memiliki variabel yang terukur, serta dapat diuji kebenarannya. Selain itu, riset tidak selalu mencari solusi langsung, melainkan berusaha mengidentifikasi gap dalam pengetahuan dan membuktikannya melalui eksperimen yang valid.
