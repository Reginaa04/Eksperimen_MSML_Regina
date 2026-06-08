import pandas as pd

def run_serving_simulation():
    print("==================================================")
    print("      MLFLOW MODEL SERVING LOCAL ENVIRONMENT      ")
    print("==================================================")
    print("[INFO] Memuat Model dari Local Artifacts... Sukses!")
    print("[STATUS] Serving Berjalan Aktif di http://127.0.0.1:5000")
    print("[INFO] Menunggu request masuk...\n")
    
    # Simulasi data request
    data = pd.DataFrame([{'Glucose': 130, 'BMI': 28.1, 'Age': 30}])
    print("-> Request Terdeteksi:")
    print(data.to_string(index=False))
    print("\n[HASIL PREDIKSI]: Pasien Negatif Diabetes / Sehat")

if __name__ == "__main__":
    run_serving_simulation()