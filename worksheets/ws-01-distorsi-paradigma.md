# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Diva Nur Azizah
Tanggal          : 5 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: akurat di data yang mana? Apakah data tersebut seimbang?
   - Data yang dibutuhkan untuk verifikasi: Dataset yang digunakan, metode evaluasi, dan perbandingan dengan metode lain.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Saya memilih positivis karena penelitian di bidang TI dapat diuji secara objektif menggunakan data dan eksperimen serta dapat membuat sistem sebagai alat pengujian.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Menganggap bahwa performa sistem di lingkungan laboratorium yang terkontrol akan selalu sama dengan performa di kondisi nyata.
   - Sumber bias potensial: Dataset tidak seimbang atau hanya diambil dari kondisi tertentu.
   - Langkah mitigasi: Menggunakan dataset beragam dan melakukan validasi silang (cross-validation) untuk memastikan konsistensi hasil.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Data hasil eksperimen asli tanpa penghapusan sembarangan.
   - Batasan yang diakui sejak awal: Keterbatasan dataset dan lingkungan pengujian.

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Perbandingan Metode Klasifikasi C4.5 dan Naïve Bayes untuk Mengukur Kepuasan Pelanggan
> Penulis (Tahun): Devi Yunita dan Ines Heidiani Ikasari (2021)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data primer melalui kuesioner dari pelanggan PT. Solusi Media Semesta sebanyak 1000 responden. | Jika kuesioner hanya disebarkan secara digital, pelanggan yang tidak terlalu paham teknologi mungkin tidak terwakili. |
| Data → Processing | Melakukan coding data (0-3,5 Rendah; 3,6-5 Tinggi) dan mengurangi 1000 record menjadi 120 record data latih untuk menghapus duplikasi. | Pengurangan data dari 1000 menjadi 120 record yang sangat drastis berisiko menghilangkan variasi data yang penting.
| Processing → Analysis | Menguji akurasi menggunakan aplikasi RapidMiner dengan metode C4.5 dan Naïve Bayes. | Hasil sangat bergantung pada konfigurasi parameter di RapidMiner; pengaturan yang berbeda bisa menghasilkan angka yang berbeda. |
| Analysis → Inference | Membandingkan akurasi C4.5 (94,17%) dan Naïve Bayes (85,83%). | Peneliti menyimpulkan C4.5 lebih baik hanya dari akurasi, padahal nilai AUC C4.5 termasuk kategori "buruk" (0.686) dibanding Naïve Bayes (0.918). |
| Inference → Knowledge | Knowledge	
Menyimpulkan bahwa C4.5 lebih akurat untuk mengukur kepuasan pelanggan. | Kesimpulan ini mungkin hanya berlaku untuk kasus PT. Solusi Media Semesta dan tidak bisa langsung dianggap hukum umum untuk semua e-commerce. |

**Distorsi paling besar di tahap:** Data → Processing

**Dua distorsi spesifik yang teridentifikasi:**
1. Peneliti memangkas data dari 1000 record menjadi hanya 120 record data latih, yang berisiko menghilangkan variasi informasi dari 880 responden lainnya.
2. Peneliti mengklaim metode C4.5 lebih akurat (94,17%), namun mengabaikan nilai AUC-nya yang masuk kategori "Buruk" (0.686) jika dibandingkan dengan Naïve Bayes yang memiliki AUC "Sangat Baik" (0.918).
---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti melaporkan bahwa mereka menghapus data outlier, noise, dan missing value untuk menjaga kualitas data. |
| Transparansi | Peneliti secara terbuka menyebutkan adanya pengurangan jumlah data dari 1000 menjadi 120 record demi efisiensi. |
| Peer review | Dengan melampirkan Confusion Matrix, peneliti memudahkan orang lain untuk memverifikasi ulang klaim akurasi tersebut. |

**Keputusan akhir dan justifikasi:**
>Keputusan peneliti untuk melakukan data validation (menghapus outlier) sudah tepat secara etika riset selama kriteria penghapusannya dijelaskan secara objektif, bukan semata-mata untuk menaikkan angka akurasi secara artifisial.
---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Klasifikasi Kepuasan Pelanggan PT. Solusi Media Semesta

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 2 | 4 |
| Jenis data yang dikumpulkan | Data kuantitatif dari kuesioner dan nilai akurasi. | Hasil implementasi sistem |
| Limitasi paradigma | Persepsi mendalam pelanggan (tidak digali mendalam di sini). | Pengembangan model klasifikasi sebagai instrumen ukur. |

**Paradigma yang dipilih:** Positivis
**Alasan:** Karena penelitian ini sangat bergantung pada pengukuran objektif (akurasi, precision, recall) dan penggunaan algoritma matematis untuk membuktikan hipotesis tentang metode mana yang paling akurat.
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya cenderung menerima klaim "95% akurat" sebagai bukti mutlak kesuksesan sebuah metode tanpa mempertanyakan proses di baliknya. Namun, setelah memahami rantai distorsi dan membedah jurnal penelitian kepuasan pelanggan PT. Solusi Media Semesta, saya kini menyadari bahwa akurasi tinggi tidak menjamin validitas pengetahuan jika terjadi reduksi data yang ekstrem dari 1000 menjadi 120 record atau jika nilai AUC-nya ternyata masuk kategori buruk meskipun akurasinya tinggi. Kini, pertanyaan utama yang akan saya ajukan saat membaca paper adalah bagaimana proses pra-pengolahan data dilakukan dan apakah metrik pendukung lainnya seperti AUC dan Confusion Matrix konsisten mendukung klaim akurasi tersebut
