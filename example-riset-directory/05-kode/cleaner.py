import re

class TextCleaner:
    def __init__(self):
        pass

    def case_folding(self, text):
        """Mengubah teks menjadi huruf kecil semua."""
        return text.lower()

    def remove_symbols(self, text):
        """Menghapus angka, tanda baca, dan karakter spesial."""
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Menghapus spasi berlebih
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def clean_pipeline(self, text):
        """Menjalankan seluruh fungsi pembersihan secara berurutan."""
        text = self.case_folding(text)
        text = self.remove_symbols(text)
        return text