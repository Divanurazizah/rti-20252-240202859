# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Analisis Sentimen Ulasan E-Commerce Menggunakan Algoritma Naïve Bayes dan C4.5: Studi Komparatif Karakteristik Teks Formal dan Bahasa Slang
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan

```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Tingginya penggunaan bahasa slang pada ulasan e-commerce sering kali menurunkan akurasi algoritma klasifikasi sentimen. Penelitian ini membandingkan kinerja Naïve Bayes dan C4.5 pada dataset formal vs slang menggunakan 40 run eksperimen. Hasil menunjukkan C4.5 lebih stabil pada data slang dengan rata-rata akurasi 79.50%, sementara Naïve Bayes mengalami penurunan performa drastis akibat variabilitas kata non-baku. | 200-250 |
| Introduction | Konteks: Pertumbuhan e-commerce memicu lonjakan data ulasan konsumen yang penting bagi analisis bisnis. Gap: Sebagian besar penelitian menguji algoritma pada data bersih, namun mengabaikan drop performa ketika berhadapan langsung dengan teks slang di lapangan. RQ: Bagaimana dampak variasi bahasa slang terhadap stabilitas akurasi Naïve Bayes dan C4.5? | 500-700 |
| Related Work | Tinjauan pustaka berfokus pada penelitian analisis sentimen berbasis Naïve Bayes dan C4.5 terdahulu. Memetakan posisi penelitian ini yang mengisi celah (gap) spesifik pada komparasi ketahanan model tanpa/dengan tahapan text normalization pada korpus bahasa Indonesia. | 700-1000 |
| Method | Desain eksperimen menggunakan pendekatan kuantitatif berbasis data sekunder ulasan e-commerce (n=1.000 data awal). Menjelaskan secara rinci pipeline text preprocessing (case folding, filtering, tokenization, lexicon mapping kata slang). Variabel independen adalah karakteristik teks (formal vs slang) dan variabel dependen adalah nilai Accuracy serta F1-Score. | 800-1200 |
| Results | Menyajikan data pengujian dalam bentuk tabel performa hasil 10-fold cross-validation. Menampilkan diagram batang (bar chart) perbandingan akurasi beserta error bar-nya, serta visualisasi box plot untuk menunjukkan sebaran stabilitas nilai run dari kedua algoritma secara objektif tanpa interpretasi subjektif. | 500-800 |
| Discussion | Menginterpretasikan mengapa C4.5 (85.20% formal / 79.50% slang) lebih tangguh menahan noise teks dibanding Naïve Bayes (82.10% formal / 75.20% slang). Membahas fenomena bias probabilitas pada Naïve Bayes ketika menemui variasi kata non-baku baru, serta mendiskusikan batasan internal validity terkait keterbatasan kamus slang yang digunakan. | 600-900 |
| Conclusion | Menjawab pertanyaan penelitian bahwa karakteristik dataset berupa bahasa slang terbukti menurunkan performa model, namun algoritma berbasis pohon keputusan (C4.5) memiliki stabilitas yang jauh lebih baik. Menyarankan pengembangan masa depan (future work) berupa integrasi modul normalisasi berbasis deep learning. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| *Contoh: RQ1* | *✓* | *✓* | *✓* | *✓* | *✓* |
| *Contoh: Metrik-X* | *✓* | *✓* | *✓* | *✓* | *✓* |
| RQ1 | *✓* | *✓* | *✓* | *✓* | *✓* |
| RQ2 | | *✓* | *✓* | *✓* | *✓* |
| Metrik utama | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel IV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel DV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Klaim/kontribusi | *✓* | *✓* | *✓* | *✓* | *✓* |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Tidak ditemukan inkonsistensi. Seluruh parameter pengujian (variabel, metrik evaluasi, dan rumusan masalah) yang diperkenalkan sejak bab pendahuluan telah diuji pada metodologi, disajikan di bab hasil, dan dijawab tuntas pada bab kesimpulan.

**Tindakan perbaikan:**
> Mempertahankan struktur matriks konsistensi yang sudah linear ini selama proses penulisan draf laporan akhir.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Algoritma Naïve Bayes performanya sangat turun sekali dan tidak bagus waktu dipakai untuk menebak sentimen yang ada bahasa gaulnya di Shopee karena rumusnya bingung membaca kata-kata yang aneh dan tidak beraturan yang diketik oleh para pembeli barang di aplikasi tersebut.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Penggunaan kata "sangat turun sekali", "tidak bagus", dan "menebak" terlalu ambigu dan tidak mencerminkan bahasa ilmiah. | Mengubahnya menjadi istilah teknis operasional klasifikasi teks: "Akurasi model mengalami penurunan signifikan". |
| Precision | Kalimat "rumusnya bingung membaca kata-kata yang aneh" tidak presisi secara keilmuan komputer. | Menggantinya dengan penjelasan matematis algoritma: "mengalami distorsi nilai probabilitas akibat variabilitas kosakata". |
| Conciseness | Kalimat terlalu bertele-tele dan menggunakan banyak kata pengisi informal (filler words). | Memangkas subjek yang redundan agar langsung menuju ke argumen inti hubungan variabel. |

**Paragraf setelah perbaikan:**
> Akurasi algoritma Naïve Bayes mengalami penurunan signifikan saat mengklasifikasikan ulasan berbasis bahasa slang. Hal ini disebabkan oleh distorsi kalkulasi probabilitas kondisional ketika model menghadapi variabilitas kosakata non-baku yang tinggi, sehingga merusak kestabilan matriks klasifikasi jika dibandingkan dengan pengujian pada dataset formal.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset cenderung hanya menceritakan urutan aktivitas kronologis (seperti catatan harian eksperimen), tanpa ada pembuktian posisi ilmiah. Sebaliknya, menulis sebagai "argumen" riset adalah menyusun rantai logika ilmiah yang kuat untuk meyakinkan pembaca bahwa ada masalah nyata (gap), metode yang dipilih adalah solusi paling valid, dan hasil temuan terbukti memberikan kontribusi baru bagi keilmuan.
> Efek urutan penulisan: Menulis dengan urutan Method → Results → Discussion → Introduction meningkatkan kualitas tulisan secara drastis karena menjauhkan peneliti dari bias asumsi. Dengan menulis metodologi dan hasil terlebih dahulu, kita memijakkan draf paper pada fakta angka yang sudah pasti dan objektif. Ketika data sudah matang, menulis pendahuluan (Introduction) menjadi jauh lebih tajam dan terbingkai (framed) dengan pas karena kita sudah tahu persis kontribusi nyata apa yang berhasil diraih di akhir eksperimen.