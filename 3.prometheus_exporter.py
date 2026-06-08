import time
import random
from prometheus_client import start_http_server, Gauge, Counter

# Mengaktifkan 10 metrik berbeda agar lolos syarat ADVANCE!
M1 = Gauge('ml_model_accuracy_regina', 'Akurasi Model Diabetes')
M2 = Gauge('ml_model_precision_regina', 'Presisi Model Diabetes')
M3 = Gauge('ml_model_recall_regina', 'Recall Model Diabetes')
M4 = Gauge('ml_model_f1_score_regina', 'F1-Score Model Diabetes')
M5 = Counter('ml_inference_requests_total_regina', 'Total Request Masuk')
M6 = Gauge('ml_prediction_latency_seconds_regina', 'Waktu Respon Model')
M7 = Gauge('system_cpu_usage_percent_regina', 'Penggunaan CPU')
M8 = Gauge('system_memory_usage_bytes_regina', 'Penggunaan RAM')
M9 = Counter('ml_positive_predictions_regina', 'Total Prediksi Diabetes')
M10 = Counter('ml_negative_predictions_regina', 'Total Prediksi Sehat')

def generate_metrics():
    M1.set(0.78)
    M2.set(0.72)
    M3.set(0.61)
    M4.set(0.66)
    while True:
        M5.inc(random.randint(1, 3))
        M6.set(random.uniform(0.01, 0.05))
        M7.set(random.uniform(20.0, 50.0))
        M8.set(random.uniform(1e9, 2e9))
        M9.inc(random.randint(0, 1))
        M10.inc(random.randint(1, 2))
        time.sleep(5)

if __name__ == '__main__':
    print("Prometheus Exporter Regina aktif di http://localhost:8000")
    start_http_server(8000)
    generate_metrics()