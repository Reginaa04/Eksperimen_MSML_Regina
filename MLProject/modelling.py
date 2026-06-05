import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import os

def train_baseline():
    print("Memulai training otomatis untuk Workflow CI...")
    
    # 1. PENTING: Aktifkan autolog agar MLflow otomatis membuat folder 'artifacts/model'
    mlflow.autolog()
    
    # Membuat dataset dummy langsung dari memori
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    # 2. Buka MLflow tracking dengan nama run yang jelas
    with mlflow.start_run(run_name="Logistic_Baseline"):
        model = LogisticRegression()
        model.fit(X, y)
        
        # Log model secara eksplisit ke folder bernama "model"
        mlflow.sklearn.log_model(model, "model")
        print("Training selesai! Model dan artefak resmi berhasil disimpan ke MLflow.")

if __name__ == "__main__":
    train_baseline()
