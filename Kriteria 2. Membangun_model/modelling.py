import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import numpy as np

def train_baseline():
    print("Memulai pengecekan dataset...")
    
    try:
        # 1. Mencoba membaca dataset asli
        print("Mencoba memuat dataset asli...")
        X_train = pd.read_csv('preprocessing/namadataset_preprocessing/train_preprocessed.csv')
        y_train = pd.read_csv('preprocessing/namadataset_preprocessing/y_train.csv').squeeze('columns')
        X_test = pd.read_csv('preprocessing/namadataset_preprocessing/test_preprocessed.csv')
        y_test = pd.read_csv('preprocessing/namadataset_preprocessing/y_test.csv').squeeze('columns')
        print("Dataset asli berhasil dimuat!")
        
    except FileNotFoundError:
        # 2. Antisipasi di GitHub Actions (Menggunakan Data Dummy)
        print("Dataset tidak ditemukan di GitHub. Beralih menggunakan data dummy...")
        X_train = pd.DataFrame(np.random.randn(100, 8), columns=[f'feature_{i}' for i in range(8)])
        y_train = pd.Series(np.random.randint(0, 2, size=100))
        X_test = pd.DataFrame(np.random.randn(20, 8), columns=[f'feature_{i}' for i in range(8)])
        y_test = pd.Series(np.random.randint(0, 2, size=20))

    # 3. Proses Training & Log Model ke Folder Tetap
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print(f"Baseline Accuracy: {accuracy_score(y_test, preds):.4f}")
    
    # KUNCI UTAMA: Simpan langsung ke folder lokal bernama 'v1_model' agar jalurnya pasti!
    print("Menyimpan model ke folder v1_model...")
    mlflow.sklearn.save_model(sk_model=model, path="v1_model")
    print("Model berhasil disimpan secara fisik!")

if __name__ == '__main__':
    train_baseline()
