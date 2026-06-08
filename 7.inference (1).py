from flask import Flask, jsonify, request
from prometheus_client import generate_latest, Counter, Gauge
import time

app = Flask(__name__)

# 1. MEMBUAT METRIK PROMETHEUS SIMPEL
REQUEST_COUNT = Counter('api_requests_total', 'Total jumlah request ke API Inference')
MODEL_ACCURACY = Gauge('ml_model_accuracy_reginaa04', 'Nilai akurasi model ML Regina')

# Set nilai akurasi awal agar masuk ke dalam metrik
MODEL_ACCURACY.set(0.95)

# 2. ENDPOINT UTAMA (HOME)
@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return jsonify({"message": "API Inference Flask Reginaa04 Berhasil Jalan!"})

# 3. ENDPOINT HEALTH CHECK
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# 4. ENDPOINT PREDIKSI DUMMY
@app.route('/predict', methods=['POST'])
def predict():
    REQUEST_COUNT.inc()
    # Meniru balasan prediksi sukses
    return jsonify({"prediction": 1, "status": "success_reginaa04"})

# 5. ENDPOINT METRIKS UNTUK PROMETHEUS (Sangat Penting!)
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("Server jalan di http://localhost:5001")
    print("Metrics di http://localhost:5001/metrics")
    # Dijalankan di port 5001 agar sama dengan contoh target kamu
    app.run(host='0.0.0.0', port=5001, debug=False)
