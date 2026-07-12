import os
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Memanggil modul cleaner yang sekarang letaknya SEJAJAR dengan main.py
from cleaner import TextCleaner

def run_pipeline():
    print("=== Memulai Pipeline Analisis Sentimen (Diva Nur Azizah) ===")
    
    # Inisialisasi alat pembersih teks
    cleaner = TextCleaner()
    
    # 1. Simulasi Load Data (Menggantikan proses load file CSV nyata)
    print("\n[1] Memuat dataset ulasan...")
    X_dummy_kotor = [
        "Kualitas produk SANGAT baik!! :)", 
        "Barang RUSAK, kecewa bgt...", 
        "Pengiriman cepat, mantap123", 
        "Jelek banget, ga sesuai ekspektasi?!"
    ]
    y_dummy = ["Positif", "Negatif", "Positif", "Negatif"]
    
    # Membersihkan data menggunakan cleaner.py sebelum diproses
    X_dummy_bersih = [cleaner.clean_pipeline(text) for text in X_dummy_kotor]
    print(f"    -> Contoh teks kotor  : '{X_dummy_kotor[0]}'")
    print(f"    -> Hasil teks bersih  : '{X_dummy_bersih[0]}'")
    
    # 2. Ekstraksi Fitur (TF-IDF)
    print("\n[2] Melakukan ekstraksi fitur TF-IDF...")
    vectorizer = TfidfVectorizer()
    X_tfidf = vectorizer.fit_transform(X_dummy_bersih)
    
    # 3. Inisialisasi Model
    nb_model = MultinomialNB(alpha=1.0) # Laplace Smoothing aktif
    c45_model = DecisionTreeClassifier(criterion='entropy', min_samples_split=2) # C4.5 menggunakan Entropy
    
    # 4. Simulasi Cross Validation
    print("\n[3] Menjalankan Cross-Validation Engine...")
    kf = KFold(n_splits=2, shuffle=True, random_state=42)
    
    fold = 1
    for train_index, test_index in kf.split(X_tfidf):
        X_train, X_test = X_tfidf[train_index], X_tfidf[test_index]
        # Label handling (Simulasi array slicing manual)
        y_train = [y_dummy[i] for i in train_index]
        y_test = [y_dummy[i] for i in test_index]
        
        # Training (Melatih model)
        nb_model.fit(X_train, y_train)
        c45_model.fit(X_train, y_train)
        
        # Testing (Menguji tebakan model)
        nb_pred = nb_model.predict(X_test)
        c45_pred = c45_model.predict(X_test)
        
        print(f"\n--- Hasil Fold {fold} ---")
        print(f"Akurasi Naïve Bayes : {accuracy_score(y_test, nb_pred):.3f}")
        print(f"Akurasi C4.5        : {accuracy_score(y_test, c45_pred):.3f}")
        fold += 1

if __name__ == "__main__":
    run_pipeline()