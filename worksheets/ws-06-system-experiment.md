# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah modifikasi algoritma Decision Tree menggunakan C4.5 dengan Pruning dan SMOTE dapat menghasilkan performa (F1-Score) yang lebih stabil pada dataset fashion e-commerce Indonesia dibandingkan model standar?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Teknik Optimasi (SMOTE & Pruning) | IV | Preprocessing Module & Model Trainer | Toggle (On/Off) pada fungsi SMOTE dan parameter Pruning di kode program. |
| Performa Model (F1-Score) | DV | Evaluation Engine / Logger | Menghasilkan file CSV berisi hasil Confusion Matrix (Accuracy, Precision, Recall, F1) setelah testing. |
| Jenis Algoritma & Dataset | CV | Config Loader / Constants | Mengunci jenis algoritma (C4.5) dan dataset (Fashion lokal) di file konfigurasi/header agar tidak berubah. |

4 Prinsip Desain:
  [✓] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [✓] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [✓] Measurement Integration — Pengukuran DV built-in
  [✓] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Dataset Ulasan Fashion E-Commerce Indonesia (CSV).
  Parameter      : SMOTE (k-neighbors=5), Pruning (Confidence Factor=0.25).
  Output format  : Confusion Matrix Report & Decision Tree Visualization (Graphviz).

```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah penerapan SMOTE dan Pruning meningkatkan F1-Score pada klasifikasi ulasan fashion dibandingkan C4.5 standar?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Penyeimbangan Data | *IV* | SMOTE_Module | Switch Boolean `use_smote = True/False` |
| Stabilitas Prediksi| DV | Metrics_Calculator | Print hasil Accuracy & F1-Score ke konsol/log. |
| Prosedur Cleaning | CV | Preprocessing_Module | Fungsi clean_text() dibuat statis (tidak berubah). |


**Apakah semua variabel bisa di-map?** [ ✓ ] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? Semua variabel sudah terwakili dalam modul utama.

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Setiap modul (SMOTE, Pruning, C4.5) jelas tugasnya melayani variabel penelitian. |
| Modularity | ✅ | Modul SMOTE dipisahkan dari Classifier, sehingga bisa dicopot-pasang tanpa merusak alur klasifikasi. |
| Controllability | ✅ | Parameter seperti `min_samples_leaf` atau `sampling_strategy` diletakkan di variabel konfigurasi di awal kode. |
| Measurability | ✅ | Sistem otomatis menghitung metrics setiap kali selesai melakukan `model.fit().` |

**Prinsip mana yang paling sulit dipenuhi?** Variable Isolation
**Strategi untuk mengatasinya:**
> Memastikan bahwa saat SMOTE dimatikan, dataset yang masuk ke Classifier adalah dataset asli yang belum dimanipulasi, namun tetap melewati tahap preprocessing yang sama (CV).

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ | ✅ | ✅ | Performa optimal dengan pohon keputusan yang ringkas dan seimbang. |
| – A | ❌ | ✅ | ✅ | F1-Score turun drastis karena model bias ke kelas mayoritas (ulasan positif). |
| – B | ✅ | ❌| ✅ | Akurasi tinggi di data latih, tapi rendah di data uji (terjadi overfitting). |
| – C | ✅ | ✅ | ❌ (tanpa normalisasi) | Banyak noise (simbol/angka) masuk ke model, membuat pohon menjadi sangat kompleks. |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (SMOTE)
**Mengapa?**
> Karena dalam data ulasan fashion di e-commerce, jumlah sentimen positif (puas) biasanya jauh lebih banyak daripada sentimen negatif (tidak puas). Ketidakseimbangan data (class imbalance) yang ekstrim ini akan membuat model cenderung mengabaikan ulasan negatif jika tidak ditangani dengan SMOTE, sehingga nilai F1-Score (yang memperhatikan keseimbangan) akan rendah.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko Sistem Monolitik:
Jika sistem dibangun seperti produk (fitur langsung lengkap/monolitik), kita akan mengalami kesulitan saat hasil eksperimen tidak sesuai harapan. Kita tidak akan tahu fitur mana yang sebenarnya membantu meningkatkan akurasi dan fitur mana yang justru menjadi penghambat (noise). Hasil riset menjadi tidak valid secara ilmiah karena tidak ada isolasi variabel; kita hanya bisa mengklaim "sistemnya jalan," tapi tidak bisa menjelaskan "mengapa sistemnya jalan."
> Pentingnya Arsitektur Modular:
Arsitektur modular sangat penting untuk riset karena memungkinkan peneliti melakukan Variable Isolation. Dengan memisahkan modul (SMOTE, Preprocessing, Classifier), kita bisa mengganti atau mematikan satu modul tanpa mengganggu fungsi modul lainnya. Hal ini mempermudah proses evaluasi tiap komponen secara adil, memastikan reprodusibilitas (orang lain bisa mengulang eksperimen dengan mudah), dan membuat penjelasan saat sidang skripsi menjadi jauh lebih logis dan sistematis.
