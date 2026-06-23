# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua skenario tercakup
  [x] Jumlah run sesuai rencana
  [x] Tidak ada file output hilang
  Missing: 0 dari 60 data points

Format Consistency:
  [x] Semua file format sama (CSV/JSON/...)
  [x] Header konsisten
  [x] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [x] Nilai dalam range masuk akal
  [x] Tidak ada waktu negatif
  [x] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: Terdeteksi 1 nilai penurunan akurasi drastis (outlier statistik) pada skenario ulasan non-baku.

Cross-Validation:
  [x] Run identik → hasil mendekati
  [x] Trend konsisten dengan ekspektasi teori

Keputusan:
  [ ] Data siap analisis
  [x] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Naïve Bayes, Dataset Formal (Kuesioner/Baku) | 10 | 10 | 0 | Semua ekstraksi parameter dari paper berjalan lancar. |
| C4.5, Dataset Formal (Kuesioner/Baku) | 10 | 10 | 0 | Struktur data stabil dan konsisten. |
| BERT, Dataset Campuran/Formal | 10 | 10 | 0 | Berhasil memproses tokenisasi teks terstruktur. |
| Naïve Bayes, Dataset Slang (E-Commerce/Casual) | 10 | 10 | 0 | Karakteristik teks non-baku terekstrak sepenuhnya. |
| C4.5, Dataset Slang (E-Commerce/Casual) | 10 | 10 | 0 | Ekstraksi performa ulasan e-commerce lengkap. |
| SVM + SMOTE, Dataset Slang (Fashion Shopee) | 10 | 10 | 0 | Seluruh metrik evaluasi tercatat seimbang. |


**Total expected:** 60 | **Total actual:** 60 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ditemukan data hilang (zero missing data). Seluruh parameter akurasi dari 60 sampel uji meta-analisis terkumpul secara lengkap dan siap masuk ke tahap pemeriksaan distribusi statistik.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | *91.2* |
| 2 | *90.8* |
| 3 | *91.5* |
| 4 | *78.3* |
| 5 | *91.0* |

**Deteksi outlier:**
Urutkan data lebih dulu: 78.3, 90.8, 91.0, 91.2, 91.5
Median (Q2): 91.0
- Q1 = 84.55 | Q3 = 91.35 | IQR = Q3 - Q1 = 91.35 - 84.55 = 6.8
- Batas bawah (Q1 - 1.5×IQR) = 84.55 - (1.5 × 6.8) = 84.55 - 10.2 = 74.35
- Batas atas (Q3 + 1.5×IQR) = 91.35 + (1.5 × 6.8) = 91.35 + 10.2 = 101.55
- Outlier terdeteksi: Tidak ada data di bawah 74.35 atau di atas 101.55 secara rumus IQR kaku 5 data baku. Namun, jika memakai data Run 4 (78.3%) pada konteks variasi riil, nilai ini drop terlalu jauh dari kluster ~91% (Contextual Anomaly).

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *Run 4* | *78.3* | Ketiadaan tahap text normalization (bahasa slang tidak diringkas ke bentuk baku) sehingga menurunkan performa model Naïve Bayes secara drastis. | Tetap pertahankan data tersebut di dalam analisis, karena merupakan bukti ilmiah penting bahwa karakteristik teks non-baku memicu penurunan stabilitas performa algoritma jika tanpa normalisasi. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul
**2. Format:** [ x ] Konsisten / [ x ] Ada inkonsistensi: format penulisan desimal seragam menggunakan titik baku.
**3. Range check (anomali):** Seluruh nilai akurasi berada dalam range logis [0 - 100%], ditemukan 1 data drop deviasi (78.3%) akibat efek variasi teks ulasan informal.
**4. Logic check:** [ x ] Parameter sesuai plan / [ ] Ada ketidaksesuaian: pengelompokan jenis dataset formal vs casual sesuai dengan rancangan awal proposal RTI.

**Kesimpulan:** [ ] Data siap analisis / [ x ] Perlu tindakan: Lakukan proses data normalisasi/cleaning pada pelabelan teks sebelum lanjut ke analisis korelasi atau uji ANOVA agar anomali konteks tidak merusak rata-rata distribusi data.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> "Data yang benar" adalah data yang merekam apa adanya suatu nilai dari lapangan atau log sistem tanpa melihat apakah nilai tersebut masuk akal atau bebas dari gangguan luar (misal: mesin otomatis mencatat akurasi 150% atau waktu minus, secara mekanis itu "benar" terekam). Sementara "data yang dipercaya" adalah data yang telah melalui pengujian kelayakan ilmiah, konsisten, lengkap, dan terbukti valid sesuai batasan logika eksperimen (misal: rentang nilai akurasi wajib di antara 0-100%).
> Validasi formal tetap diperlukan meskipun pengumpulan data dilakukan secara otomatis karena otomatisasi tidak menjamin kebenaran logika riset. Alat scraper otomatis atau fungsi kalkulasi program bisa saja mengalami bug, kegagalan pembacaan encoding teks slang, maupun ketidakseimbangan kelas (data imbalance) yang luput dari pengawasan jika tidak divalidasi lewat pipeline formal (seperti pengecekan empat pilar kualitas data).