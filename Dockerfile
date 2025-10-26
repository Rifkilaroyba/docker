# File: backend-api/Dockerfile

# 1. Gunakan Python versi tertentu sebagai base image
FROM python:3.9-slim

# 2. Set direktori kerja di dalam container
WORKDIR /app

# 3. Salin requirements.txt dan instal dependensi
# (Ini menghemat waktu build karena jika requirements tidak berubah, Docker bisa pakai cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Salin semua file proyek (app.py, dll.) ke direktori kerja
COPY . .

# 5. Ekspos port 5000, port tempat Flask berjalan
EXPOSE 5000

# 6. Perintah untuk menjalankan aplikasi saat container dimulai
# Kita gunakan gunicorn untuk menjalankan aplikasi secara production-ready
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 
# Jika tidak mau pakai gunicorn, cukup:
# CMD ["python", "app.py"]