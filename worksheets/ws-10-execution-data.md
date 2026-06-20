# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| *1* | Skenario A: Koleksi Data Formal | sentimen AND e-commerce AND baku | Range tahun: 2020–2026 | Planned |
| *2* | Skenario A: Koleksi Data Formal | sentimen AND e-commerce AND kuesioner | Range tahun: 2020–2026 | Planned |
| 3 | Skenario B: Koleksi Data Slang | sentimen AND e-commerce AND slang | Range tahun: 2020–2026 | Planned |
| 4 | Skenario B: Koleksi Data Slang | sentimen AND e-commerce AND media sosial | Range tahun: 2020–2026 | Planned |
| 5 | Skenario B: Koleksi Data Slang | sentimen AND e-commerce AND ulasan casual | Range tahun: 2020–2026 | Planned |

**Total skenario:** 2 Skenario Utama (Kondisi Kontrol Data Formal vs Kondisi Intervensi Data Slang)
**Run per skenario:** Skenario A (2 Sesi Run), Skenario B (3 Sesi Run)
**Total run keseluruhan:** 5 Sesi Eksekusi Penelusuran

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-search-001 |
| Timestamp | 2026-06-20T10:30:00 |
| Paper ID | Sari_et_al_2020 (Format sitasi utama) |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | *sentimen AND e-commerce AND slang |
| Database Source | Google Scholar indexed via Publish or Perish v8.8 |
| Algorithm Checked | Naïve Bayes / C4.5 Decision Tree |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Accuracy | float | 0.0 – 1.0 (atau 0% – 100%) |
| F1-Score | float | 0.0 – 1.0 |
| Dataset Size | integer |  lebih besar sama dengan 1 (Jumlah total baris data ulasan) |

**Format output:** [ ✓ ] CSV / [ ✓ ] JSON / [ ] Database / [ ] Lainnya: File Spreadsheet .xlsx (WPS Office)
---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | IP laptop terblokir sementara oleh Google Scholar (CAPTCHA loop) | Dokumentasikan waktu kejadian, lakukan pembersihan cache browser, istirahatkan penelusuran selama 30 menit, lalu gunakan koneksi alternatif. |
| Hasil ekstrem | Sebuah paper mengklaim akurasi Naïve Bayes mencapai 100% pada data slang. | Lakukan investigasi manual terhadap Bab Pembahasan paper tersebut; periksa apakah terjadi kebocoran data (data leakage) atau overfitting. Jika tidak valid, masukkan ke kategori eksklusi. |
| Waktu eksekusi anomali | Publish or Perish tidak merespons (freeze) saat menarik data. | Hentikan paksa aplikasi, perkecil batasan jumlah maksimal pencarian dari maksimal 1000 menjadi maksimal 200 per run. |
| Inkonsistensi dengan run lain | Metrik evaluasi yang ditulis di abstrak berbeda dengan tabel confusion matrix di dalam isi paper. | Prioritaskan data mentah dari tabel confusion matrix, hitung ulang F1-Score secara mandiri menggunakan rumus teoretis baku, lalu catat revisi tersebut pada log. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Iya, pada tugas-tugas makalah perkuliahan semester sebelumnya, saya seringkali hanya mengambil kesimpulan dari satu paper utama saja tanpa membandingkannya dengan paper lain (single run perspective). Risikonya adalah kesimpulan menjadi sangat subjektif, bias, dan rawan salah apabila paper acuan utama tersebut ternyata memiliki kekeliruan metodologi.
**Yang akan dilakukan berbeda:**
> Melalui metode meta-analisis dengan multiple run penelusuran ini, saya mengumpulkan variabilitas data dari belasan paper (rentang tahun 2020-2026). Dengan begitu, saya bisa menghitung nilai rata-rata (mean) serta melihat sebaran penurunan performa algoritma secara objektif. Hal ini membuat kesimpulan penelitian saya menjadi jauh lebih valid, akurat, dan dapat dipercaya secara ilmiah.