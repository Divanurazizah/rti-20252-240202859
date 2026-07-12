## Arsitektur Pemrosesan Data dan Landasan Teori Sistem

Mendokumentasikan spesifikasi arsitektur sistem, diagram alur pemrosesan teks (Text Preprocessing Pipeline), serta skema representasi data yang dirancang pada Tahap 1 untuk komparasi algoritma Naïve Bayes dan C4.5.

## 1. Diagram Arsitektur Pipeline Pemrosesan Teks
Sistem ini menggunakan arsitektur linear untuk memurnikan ulasan e-commerce mentah (raw reviews) sebelum diekstraksi menjadi fitur numerik. Alur pemrosesan digambarkan melalui diagram Mermaid berikut:

Ulasan Mentah Shopee
          │
          ▼
    Case Folding
          │
          ▼
 Filtering & Cleaning
          │
          ▼
     Tokenization
          │
          ▼
 Skenario Karakteristik Dataset
      ├───────────────┐
      │               │
      ▼               ▼
Dataset Slang    Dataset Formal
      │               │
      │        Lexicon Mapping
      │               │
      │        Stopword Removal
      └───────┬───────┘
              ▼
 Ekstraksi Fitur TF-IDF
              │
              ▼
 10-Fold Cross Validation
              │
              ▼
 Naïve Bayes vs C4.5
              │
              ▼
 Evaluasi Performa


## 2. Landasan Pemetaan Fitur (Vektor TF-IDF)


Representasi data teks ke dalam bentuk matriks numerik menggunakan metode Term Frequency - Inverse Document Frequency (TF-IDF). Setiap dokumen ulasan $d$ diwakili oleh vektor bobot W:
- Term Frequency (TF): Menghitung frekuensi kemunculan kata dalam satu ulasan.
- Inverse Document Frequency (IDF): Mengukur seberapa langka atau pentingnya kata tersebut di seluruh korpus ulasan.

Pada tahap perancangan ini, rentang nilai bobot fitur dipastikan berada pada skala [0, 1] sehingga tidak memerlukan normalisasi numerik tambahan (seperti Min-Max Scaling) untuk menjaga validitas data asli.


## 3. Skema Logis Pemrosesan Algoritma


A. Alur Matematika Naïve Bayes (Probabilitas Bersyarat)
Algoritma Naïve Bayes mengklasifikasikan kelas sentimen (Positif/Negatif) berdasarkan perhitungan peluang tertinggi menggunakan rumus.
Laplace Smoothing: Guna mengantisipasi variabilitas kata slang baru yang memiliki frekuensi nol ($0$) pada data training yang dapat memicu kegagalan total kalkulasi probabilitas (P = 0), sistem menyuntikkan nilai smoothing secara konstan pada setiap bobot kata.

B. Struktur Aturan Keputusan C4.5 (Decision Tree)
Algoritma C4.5 membangun pohon keputusan non-linear dengan menghitung nilai Entropy dan Gain Ratio untuk menentukan kata (term) mana yang paling berpengaruh sebagai akar pemisah (root node), pohon keputusan yang dihasilkan dari skenario teks formal cenderung lebih ringkas, sedangkan skenario teks slang menghasilkan cabang pohon yang jauh lebih dalam (over-branching) akibat tingginya variasi kata non-baku.


## 4. Matriks Pemetaan ke Implementasi Kode
Komponen teori dan arsitektur di atas diimplementasikan secara modular ke dalam kode program sebagai berikut:

| **Komponen Arsitektur**   | **Modul Penulisan Kode**             | **Fungsi Utama**                                                                                          |
| ------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Text Preprocessor**     | `preprocessing.py` / `cleaner.class` | Melakukan *case folding*, tokenisasi, dan pembersihan simbol-simbol non-alfabet.                          |
| **Lexicon Mapper**        | `slang_dictionary.json`              | Kamus pasangan kata slang ke kata formal (misalnya `"jg"` → `"juga"`) untuk normalisasi bahasa.           |
| **Feature Extractor**     | `vectorizer.py` / `tfidf_module`     | Mengubah token kata menjadi representasi matriks bobot numerik menggunakan metode TF-IDF.                 |
| **Classification Engine** | `classifier_models.py`               | Berisi logika eksekusi algoritma Naïve Bayes dan C4.5 secara paralel untuk 40 kali pengujian (*40 runs*). |
