FROM python:3.9-slim

WORKDIR /app

# Install library yang dibutuhkan
RUN pip install mlflow scikit-learn pandas numpy

# Salin semua kode proyek ke dalam container
COPY . /app

# Perintah default saat container dijalankan (opsional tapi bagus untuk formalitas)
CMD ["python", "MLProject/modelling.py"]
