from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'database.json'

# Fungsi untuk memvalidasi dan membaca data
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        return []
    
    try:
        with open(DATA_FILE, 'r') as f:
            content = f.read().strip()
            if not content:  # Jika file benar-benar kosong
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # Jika file berisi karakter yang bukan format JSON, reset jadi list kosong
        return []

# Fungsi untuk menyimpan data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    expenses = load_data()
    # Hitung total pengeluaran untuk ditampilkan di Dashboard
    total = sum(item.get('amount', 0) for item in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add_expense():
    try:
        new_entry = request.json
        # Pastikan amount adalah angka
        new_entry['amount'] = int(new_entry['amount'])
        
        all_data = load_data()
        all_data.append(new_entry)
        save_data(all_data)
        
        return jsonify({"status": "success", "message": "Data berhasil disimpan!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    # Flask akan berjalan di http://127.0.0.1:5000
    app.run(debug=True)