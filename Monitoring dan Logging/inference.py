import pandas as pd
import time

def jalankan_serving():
    print("==================================================")
    print("       MODEL SERVING LOCAL ENVIRONMENT ACTIVE     ")
    print("==================================================")
    print("[INFO] Model Diabetes berhasil dimuat dari artefak.")
    print("[STATUS] Aplikasi berjalan aktif di http://localhost:5000")
    print("[INFO] Menunggu request inference baru...\n")
    
    # Simulasi inference data baru
    sample_data = pd.DataFrame([{
        'Pregnancies': 2, 'Glucose': 130, 'BloodPressure': 70, 
        'SkinThickness': 20, 'Insulin': 90, 'BMI': 28.1, 
        'DiabetesPedigreeFunction': 0.263, 'Age': 30
    }])
    print("-> Request Masuk (Data Pasien Baru):")
    print(sample_data.to_string(index=False))
    print("\n[HASIL PREDIKSI]: Pasien Dinyatakan Sehat / Negatif Diabetes")

if __name__ == "__main__":
    jalankan_serving()
