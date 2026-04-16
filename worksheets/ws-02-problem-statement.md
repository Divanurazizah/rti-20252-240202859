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
  Domain   : Teknologi Informasi(e-learning)
  Konteks  : Penggunaan aplikasi pembelajaran online mahasiswa diperguruan tinggi

System Context
  Input       : Materi pembelajaran (file materi, link file, vidio, quiz) dan interaksi pengguna 
  Process     : Penyajian materi dan interaksi pengguna dalam aplikasi (pengerjaan quiz, klik)
  Output      : Tampilan materi dan hasil interaksi (nilai quiz, progres belajar)
  Outcome     : Tingkat penyelesaian materi (completion rate ) dan pemahaman mahasiswa
  Constraints : Koneksi internet, desain antarmuka aplikasi, keterbatasan waktu belajar mahasiswa
  Stakeholders: Mahasiswa, dosen, dan pengembang aplikasi e-learning

Fenomena → Problem
  Fenomena yang diamati             : Pengguna e-learning meningkat namun mahasiswa tidak menyelesaikan materi
  Gejala (symptom) yang terukur     : Completion rate rendah (kurang dari 50%)
  Masalah yang didiagnosis          : Kurangnya fitur interaktif dalam aplikasi (hanya teks dan video tanpa interaksi)
  Masalah riset (researchable)      : Belum ada analisis pengaruh fitur interaktif (quiz real-time) terhadap completion rate mahasiswa 
  Variabel yang terukur             : Completion rate (%), waktu belajar (menit), jumlah interaksi (klik/quiz)


Problem Quality Check
  [ ] Clarity — Apakah satu orang membaca akan paham?
  [ ] Measurability — Apakah ada metrik kuantitatif?
  [ ] Relevance — Apakah penting untuk domain?
  [ ] Testability — Apakah bisa gagal?
  [ ] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Penggunaan aplikasi e-learning dalam proses pembelajaran semakin meningkat, namun tingkat penyelesaian materi oleh mahasiswa masih rendah. Hal ini ditunjukkan dengan completion rate yang berada di bawah 50%. Permasalahan ini diduga disebabkan oleh kurangnya fitur interaktif dalam aplikasi, di mana sebagian besar hanya menyediakan materi berupa teks dan video tanpa adanya interaksi langsung. Hingga saat ini, belum terdapat analisis yang secara spesifik mengkaji pengaruh fitur interaktif seperti quiz real-time terhadap tingkat penyelesaian materi. Oleh karena itu, penelitian ini bertujuan untuk menganalisis pengaruh fitur interaktif terhadap completion rate mahasiswa dengan menggunakan metrik seperti tingkat penyelesaian, waktu belajar, dan jumlah interaksi pengguna.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Penggunaan Aplikasi E-Learning pada Mahasiswa

| Tahap | Hasil |
|-------|-------|
| Reality | Mahasiswa sering menggunakan aplikasi e-learning untuk belajar  |
| Observed Issue (Symptom) | Banyak mahasiswa tidak menyelesaikan materi(completion rate rendah, <50%) |
| Diagnosed Problem (Root Cause) | Kurangnya interaktivitas pada aplikasi (hanya berupa teks atau video tanpa feedback langsung) |
| Researchable Problem | Belum ada studi yang mengukur pengaruh fitur interaktif (quiz real-time) terhadap tingkat penyelesaian materi pada e-learning |
| Measurable Variable | Completion rate (%), waktu belajar (menit), dan jumlah interaksi (klik/quiz) |

**Apakah terjebak solution-first thinking?** [ ] Ya / [ ] Tidak
Tidak


---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Materi pembelajaran + input dari mahasiswa (mengirimkan jawaban jika ada tugas, melakukan presensi) |
| Process | Penyajian materi dan interaksi (quiz, klik) |
| Output | Tampilan materi + hasil quiz |
| Outcome | Mahasiswa memahami materi atau berhenti belajar |
| Constraints | koneksi internet, desain aplikasi, dan waktu belajar mahasiswa |
| Stakeholders | Mahasiswa, dosen, dan pengembang aplikasi |

**Komponen mana yang paling relevan dengan masalah riset?** Process (fitur interaktif dalam aplikasi)

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity |  4  | Sudah jelas, tapi bisa ditambah jenis platform |
| Measurability | 5 | da metrik (%, menit, jumlah interaksi) |
| Relevance | 5 | Sangat relevan di dunia pendidikan |
| Testability | 5 | Bisa diuji dengan eksperimen |
| Impact | 4 | Berdampak pada kualitas pembelajaran |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
Penggunaan aplikasi e-learning dalam proses pembelajaran semakin meningkat, namun tingkat penyelesaian materi oleh mahasiswa masih tergolong rendah. Data menunjukkan bahwa banyak mahasiswa tidak menyelesaikan materi yang diberikan, yang diduga disebabkan oleh kurangnya fitur interaktif dalam aplikasi pembelajaran. Sebagian besar aplikasi hanya menyediakan konten berupa teks dan video tanpa adanya interaksi langsung yang dapat meningkatkan keterlibatan pengguna. Namun, belum terdapat penelitian yang secara spesifik mengukur pengaruh fitur interaktif seperti quiz real-time terhadap tingkat penyelesaian materi. Oleh karena itu, penelitian ini bertujuan untuk menganalisis pengaruh fitur interaktif terhadap completion rate mahasiswa dengan menggunakan metrik seperti tingkat penyelesaian, waktu belajar, dan jumlah interaksi pengguna.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
Masalah pada coding seperti bug atau error berfokus pada perbaikan sistem agar dapat berjalan dengan benar, sedangkan masalah riset lebih menekankan pada pemahaman fenomena dan pencarian bukti ilmiah. Dalam riset, masalah harus dirumuskan secara jelas, terukur, dan dapat diuji, serta tidak langsung berfokus pada solusi, melainkan pada analisis dan pembuktian terhadap suatu masalah.