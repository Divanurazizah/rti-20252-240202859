# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Akurasi klasifikasi kepuasan pelanggan menggunakan Decision Tree belum stabil dan dataset yang digunakan masih terbatas.

Research Question:
  Tipe         : [ ] Comparison  [x] Improvement  [ ] Exploratory
  Formulasi    : Apakah penerapan teknik Pruning dan SMOTE pada algoritma Decision Tree dapat meningkatkan Accuracy dan F1-Score secara signifikan pada dataset kepuasan pelanggan e-commerce dibandingkan dengan Decision Tree standar?
  Variabel IV  : Teknik optimasi model (Pruning dan SMOTE).
  Variabel DV  : Performa model (Accuracy dan F1-Score).
  Metrik       : Accuracy, F1-Score, dan Precision.
  Dataset      : Dataset Review E-Commerce Indonesia (contoh: Tokopedia/Shopee).
  Baseline     : Decision Tree Standar (Tanpa optimasi).

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Efektivitas kombinasi penyeimbangan data (SMOTE) dan penyederhanaan pohon (Pruning) dalam menangani ketidakseimbangan data review pelanggan di Indonesia.
  Jenis kontribusi        : [x] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Mengatasi masalah Performance Gap (akurasi tidak stabil) dan Context Gap.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan pada nilai F1-Score antara Decision Tree yang dioptimasi dengan Decision Tree standar.
  H₁ : Penerapan Pruning dan SMOTE menghasilkan F1-Score yang lebih tinggi secara signifikan dibandingkan model standar.
  Threshold              : p < 0,05
  Justifikasi threshold  : Standar umum dalam pengujian statistik untuk menolak hipotesis nol dalam riset IT.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** 
Akurasi Decision Tree belum stabil (83%-88%) dan dataset masih terbatas serta kurang fokus pada konteks lokal.

**RQ versi pertama (tulis bebas):**
> Bagaimana meningkatkan akurasi klasifikasi kepuasan pelanggan e-commerce di Indonesia agar lebih stabil hasilnya?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | Decision Tree + SMOTE/Pruning |
| Metrik terukur | Ya | Accuracy & F1-Score |
| Baseline | Ya | Decision Tree Standar |
| Dataset/konteks | Ya | E-commerce Indonesia |

**Tipe RQ:** [ ] Comparison / [x] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah modifikasi algoritma Decision Tree menggunakan C4.5 dengan Pruning dapat menghasilkan Accuracy yang lebih tinggi dibandingkan algoritma ID3 pada dataset kepuasan pelanggan e-commerce Indonesia?
---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak terdapat peningkatan akurasi yang signifikan pada penggunaan algoritma C4.5 dibanding ID3 pada dataset yang digunakan. |
| H₁ | Algoritma C4.5 memberikan hasil akurasi yang lebih stabil dan tinggi secara signifikan dibandingkan ID3. |
| Metrik | Accuracy (%) |
| Threshold | Kenaikan minimal 3% dari baseline. |
| Justifikasi threshold | Batas minimal untuk dianggap memiliki dampak praktis pada pengambilan keputusan bisnis. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika setelah diuji, hasil akurasi C4.5 ternyata sama dengan atau bahkan lebih rendah dari ID3.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Perbandingan performa C4.5 vs ID3 pada klasifikasi review pelanggan |
| Variable (IV) | Jenis Algoritma (C4.5 vs ID3) |
| Variable (DV) | Akurasi Klasifikasi |
| Metric | Confusion Matrix (Accuracy, Precision, Recall) |
| Data source | Crawling data review dari Google Play Store (App Tokopedia/Shopee) |
| Analysis method | Komparasi hasil matriks evaluasi dan T-Test |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Sentiment Analysis of Indonesian E-Commerce Service Quality using Random Forest
**RQ yang diekstrak:** Sejauh mana efektivitas Random Forest dalam mengklasifikasikan sentimen pelanggan?
**Komponen yang hilang:** RQ tersebut tidak menyebutkan Baseline (dibandingkan dengan apa?) dan Metrik yang spesifik (apakah fokus ke akurasi atau kecepatan proses?).