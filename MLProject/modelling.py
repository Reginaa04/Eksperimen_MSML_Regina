import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import os

def train_baseline():
    print("Memulai training otomatis untuk Workflow CI...")
    
    # Membuat dataset dummy langsung dari memori tanpa membaca file CSV luar
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    # Membuka MLflow tracking
    with mlflow.start_run():
        model = LogisticRegression()
        model.fit(X, y)
        
        # Log parameter dan model ke MLflow
        mlflow.log_param("alpha", 0.5)
        mlflow.sklearn.log_model(model, "model")
        print("Training selesai! Model berhasil disimpan ke MLflow.")

if __name__ == "__main__":
    train_baseline()
