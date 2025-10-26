# File: backend-api/app.py

from flask import Flask, jsonify
from flask_cors import CORS # Pastikan Anda menginstal flask-cors

app = Flask(__name__)
# Mengizinkan akses dari aplikasi mobile (Expo/React Native)
CORS(app) 

@app.route('/')
def home():
    return "API Backend Berjalan!"

@app.route('/data-mahasiswa', methods=['GET'])
def get_data():
    """Endpoint yang akan diakses oleh aplikasi mobile."""
    data = {
        "status": "sukses",
        "nama_proyek": "Virtualisasi Mobile App",
        "data": [
            {"id": 1, "nama": "Budi Santoso", "nim": "2104001"},
            {"id": 2, "nama": "Siti Amelia", "nim": "2104002"},
            {"id": 3, "nama": "Rifki Laroyba", "nim": "1204230026"}
        ],
        "message": "Data diambil dari container Docker!"
    }
    return jsonify(data)

if __name__ == '__main__':
    # Penting: Host '0.0.0.0' agar bisa diakses dari luar container (termasuk dari HP/emulator)
    app.run(debug=True, host='0.0.0.0', port=5000)