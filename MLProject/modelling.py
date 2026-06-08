import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

def train_baseline():
    print("Memulai training otomatis untuk Workflow CI...")
    
    # Mengaktifkan pelacakan metrik otomatis MLflow
    mlflow.autolog()
    
    # Generasi data dummy langsung di memori agar bebas eror data hilang
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    
    with mlflow.start_run(run_name="Logistic_Baseline"):
        model = LogisticRegression()
        model.fit(X, y)
        
        # Menyimpan model ke dalam sistem artefak local
        mlflow.sklearn.log_model(model, "model")
        print("Training selesai! Artefak model berhasil didaftarkan ke sistem MLflow.")

if __name__ == "__main__":
    train_baseline()
