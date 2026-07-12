
# Tahap 3 — Validasi Model (10-Fold Cross-Validation)

**Status:** Selesai
**Metode:** *10-Fold Cross-Validation* diulang sebanyak 40 kali untuk menjamin reliabilitas statistik.

Tahap validasi model dilakukan setelah proses implementasi algoritma selesai. Tujuan utama dari tahap ini adalah mengevaluasi kemampuan generalisasi model dalam mengklasifikasikan data yang belum pernah digunakan pada proses pelatihan. Validasi dilakukan menggunakan metode 10-Fold Cross-Validation, yaitu teknik evaluasi yang membagi dataset menjadi sepuluh bagian (fold), kemudian setiap bagian secara bergantian digunakan sebagai data uji sementara sembilan bagian lainnya digunakan sebagai data latih.

Untuk meningkatkan reliabilitas hasil penelitian, proses 10-Fold Cross-Validation diulang sebanyak 40 kali dengan pembagian data yang berbeda pada setiap pengujian. Pengulangan ini bertujuan untuk mengurangi pengaruh pembagian data secara acak (random sampling) sehingga nilai evaluasi yang diperoleh menjadi lebih stabil dan representatif.

## Tujuan
Memastikan model tidak *overfitting* dan mendapatkan rata-rata akurasi serta F1-Score yang stabil pada skenario Formal vs Slang.
