from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'database.json'
PROFILE_FILE = 'profile.json'
DAILY_BUDGET = 100000

# --- FUNGSI DATABASE PENGELUARAN ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- FUNGSI DATABASE PROFIL ---
def load_profile():
    if not os.path.exists(PROFILE_FILE):
        return {"name": "Odilia", "photo": ""}
    with open(PROFILE_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"name": "Odilia", "photo": ""}

def save_profile(data):
    with open(PROFILE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- ROUTES ---

@app.route('/')
def index():
    all_expenses = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Filter data hanya untuk hari ini (Reset Harian)
    today_expenses = [e for e in all_expenses if e.get('date') == today]
    
    total_today = sum(item.get('amount', 0) for item in today_expenses)
    remaining = DAILY_BUDGET - total_today
    
    return render_template('index.html', 
                           expenses=today_expenses[::-1], 
                           total=total_today, 
                           remaining=remaining)

@app.route('/add', methods=['POST'])
def add_expense():
    desc = request.form.get('desc')
    amount = request.form.get('amount')
    category = request.form.get('category')
    
    if desc and amount:
        all_expenses = load_data()
        new_entry = {
            "id": int(datetime.now().timestamp() * 1000),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "desc": desc,
            "amount": int(amount),
            "category": category
        }
        all_expenses.append(new_entry)
        save_data(all_expenses)
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_expense(item_id):
    all_expenses = load_data()
    all_expenses = [item for item in all_expenses if item.get('id') != item_id]
    save_data(all_expenses)
    return redirect(url_for('index'))

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/stats')
def stats():
    all_expenses = load_data()
    cat_data = {"Makan & Minum": 0, "Transportasi": 0, "Tidak Terduga": 0}
    
    for item in all_expenses:
        cat = item.get('category', 'Tidak Terduga')
        if cat in cat_data:
            cat_data[cat] += item.get('amount', 0)
            
    total_all = sum(cat_data.values())
    return render_template('stats.html', 
                           makan=cat_data["Makan & Minum"], 
                           transp=cat_data["Transportasi"], 
                           duga=cat_data["Tidak Terduga"],
                           total=total_all)

@app.route('/profil')
def profil():
    profile = load_profile()
    return render_template('profil.html', profile=profile)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    data = request.json
    save_profile(data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)