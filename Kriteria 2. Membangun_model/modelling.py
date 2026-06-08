import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import subprocess

def train_baseline():
    print("Memulai training otomatis untuk Workflow CI...")
    
    # Aktifkan autolog agar semua tercatat resmi
    mlflow.autolog()
    
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    with mlflow.start_run(run_name="Logistic_Baseline") as run:
        model = LogisticRegression()
        model.fit(X, y)
        
        # Log model secara eksplisit ke folder "model"
        mlflow.sklearn.log_model(model, "model")
        print("Training selesai! Model berhasil disimpan ke MLflow.")
        
        # AMBIL RUN ID YANG SEDANG BERJALAN SAAT INI SECARA AKURAT
        run_id = run.info.run_id
        print(f"Menggunakan Run ID resmi: {run_id}")
        
        # BUAT FILE REQUIREMENTS.TXT LANGSUNG DI TEMPATNYA AGAR DOCKER TIDAK EROR
        with open(f"mlruns/0/{run_id}/artifacts/model/requirements.txt", "w") as f:
            f.write("mlflow\nscikit-learn\npandas\nnumpy\n")

if __name__ == "__main__":
    train_baseline()
