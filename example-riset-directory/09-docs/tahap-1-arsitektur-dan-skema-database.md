# Tahap 1 — Perancangan Arsitektur & Skema Database

**Status:** Selesai

---

# Tahap 1 — Perancangan Dataset & Skema Data

**Status:** Selesai

## 1. Struktur Dataset
Dataset utama terdiri dari 920 ulasan produk e-commerce yang telah diberi label (Positif/Negatif). Data disimpan dalam format CSV dengan kolom:
- `review_text`: Teks ulasan mentah.
- `cleaned_text`: Teks setelah melalui normalisasi slang.
- `sentiment_label`: Label sentimen (1 untuk Positif, 0 untuk Negatif).

## 2. Alur Pemrosesan Data
`Raw Data` → `Cleaning (Case folding, Stopword removal)` → `Normalisasi Slang` → `TF-IDF Vectorization` → `Model Klasifikasi`.