import time
import random
from prometheus_client import start_http_server, Gauge, Counter

# Mendaftarkan 10 metriks berbeda demi syarat ADVANCE (ML & System Metrics)
METRIC_1 = Gauge('ml_model_accuracy_reginaa04', 'Akurasi Model')
METRIC_2 = Gauge('ml_model_precision_reginaa04', 'Presisi Model')
METRIC_3 = Gauge('ml_model_recall_reginaa04', 'Recall Model')
METRIC_4 = Gauge('ml_model_f1_score_reginaa04', 'F1-Score Model')
METRIC_5 = Counter('ml_inference_requests_total_reginaa04', 'Total Permintaan Prediksi')
METRIC_6 = Gauge('ml_prediction_latency_seconds_reginaa04', 'Waktu Respon Prediksi')
METRIC_7 = Gauge('system_cpu_usage_percent_reginaa04', 'Penggunaan CPU')
METRIC_8 = Gauge('system_memory_usage_bytes_reginaa04', 'Penggunaan Memori')
METRIC_9 = Counter('ml_positive_predictions_total_reginaa04', 'Total Pasien Diabetes')
METRIC_10 = Counter('ml_negative_predictions_total_reginaa04', 'Total Pasien Sehat')

def jalankan_metrics():
    # Set nilai metrik evaluasi model
    METRIC_1.set(0.78)
    METRIC_2.set(0.72)
    METRIC_3.set(0.61)
    METRIC_4.set(0.66)
    
    while True:
        # Simulasi fluktuasi grafik monitoring
        METRIC_5.inc(random.randint(1, 5))
        METRIC_6.set(random.uniform(0.01, 0.04))
        METRIC_7.set(random.uniform(15.0, 55.0))
        METRIC_8.set(random.uniform(1e9, 3e9))
        METRIC_9.inc(random.randint(0, 1))
        METRIC_10.inc(random.randint(1, 2))
        time.sleep(5)

if __name__ == '__main__':
    print("Prometheus Exporter Reginaa04 aktif di port 8000...")
    start_http_server(8000)
    jalankan_metrics()
