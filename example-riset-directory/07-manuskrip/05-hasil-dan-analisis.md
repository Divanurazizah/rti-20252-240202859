## 5. Hasil dan Analisis

| Algoritma | Skenario | Mean Accuracy | Mean F1-Score |
| :--- | :--- | :--- | :--- |
| Naïve Bayes | Formal | 0.856 | 0.852 |
| Naïve Bayes | Slang | 0.775 | 0.766 |
| C4.5 | Formal | 0.876 | 0.873 |
| C4.5 | Slang | 0.818 | 0.812 |

Berdasarkan tabel di atas, Naïve Bayes mengalami penurunan performa sebesar 9.46% saat menghadapi teks slang. Hal ini terjadi karena asumsi independensi fitur pada Naïve Bayes menjadi rentan ketika frekuensi kata tidak baku meningkat. Sebaliknya, C4.5 hanya mengalami penurunan 6.62%. Keunggulan C4.5 terletak pada kemampuannya membangun hierarki aturan (pohon keputusan) yang secara efektif memfilter fitur yang informatif dan mengabaikan *noise* linguistik, sehingga klasifikasi tetap stabil.