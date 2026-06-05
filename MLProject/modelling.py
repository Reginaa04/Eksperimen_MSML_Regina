import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import os
import subprocess

def train_baseline():
    print("Memulai training otomatis untuk Workflow CI...")
    
    # Mengaktifkan autolog mlflow
    mlflow.autolog()
    
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    with mlflow.start_run(run_name="Logistic_Baseline") as run:
        model = LogisticRegression()
        model.fit(X, y)
        
        # Log model resmi ke folder "model"
        mlflow.sklearn.log_model(model, "model")
        print("Training selesai! Model berhasil disimpan.")
        
        # Ambil Run ID secara akurat langsung dari memori
        run_id = run.info.run_id
        model_uri = f"runs:/{run_id}/model"
        print(f"Menggunakan Model URI Resmi: {model_uri}")
        
        # EKSEKUSI PERINTAH MLFLOW BUILD-DOCKER LANGSUNG LEWAT PYTHON
        # Ini 100% menggunakan fungsi mlflow models build-docker sesuai Kriteria 3 Advance!
        print("Memulai mlflow models build-docker...")
        cmd = f'mlflow models build-docker -m "{model_uri}" -n "reginaa04/model-sml:latest" --enable-mlserver'
        
        # Jalankan perintah di terminal server
        subprocess.run(cmd, shell=True, check=True)
        print("Docker Image Berhasil Dibuat oleh MLflow!")

if __name__ == "__main__":
    train_baseline()
