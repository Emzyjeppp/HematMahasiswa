# 💸 HematMahasiswa
**Solusi Pencatatan Keuangan Cepat & Cerdas untuk Mahasiswa**
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-green?style=flat&logo=flask)
![Redis](https://img.shields.io/badge/Redis-Message_Broker-red?style=flat&logo=redis)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

HematMahasiswa adalah aplikasi web berbasis **Flask** yang dirancang khusus untuk mahasiswa yang ingin mengelola keuangan harian dengan efisien. Fokus utama aplikasi ini adalah **kecepatan input** (Target < 3 detik) dan penyediaan **solusi belanja hemat** melalui integrasi peta warung makan murah.

---

## ✨ Fitur Utama
- **⚡ Quick Logging:** Catat pengeluaran melalui modal pop-up tanpa harus pindah halaman atau menunggu loading lama.
- **💰 Smart Budgeting:** Pantau sisa budget harian secara real-time yang langsung terpotong saat transaksi dicatat.
- **⚠️ Limit Alert:** Peringatan visual saat pengeluaran mulai mendekati batas budget harian.

http://googleusercontent.com/map_location_reference/1
- **📍 Map Warung Murah:** Temukan lokasi makan ramah kantong seperti [Lesehan Pring Ori Sorowajan](http://googleusercontent.com/map_location_reference/0) dan [Warung Makan Sadia](http://googleusercontent.com/map_location_reference/2) langsung di dalam aplikasi.
- **📱 Mobile-First Design:** Antarmuka yang responsif dan nyaman digunakan langsung dari smartphone.

---

## 📂 Struktur Folder Proyek
Struktur ini mengikuti standar pengembangan web Flask untuk menjaga keteraturan aset dan logika:

```text
PROYEK_IMK_HEMATMAHASISWA/
├── .venv/                  # Lingkungan virtual Python (Library Flask, dll)
├── static/                 # Aset frontend statis
│   ├── css/                # Styling tambahan (jika ada)
│   └── js/                 # Logika JavaScript untuk modal & Fetch API
├── templates/              # File HTML (Jinja2 Templates)
│   ├── index.html          # Halaman dashboard & input utama
│   └── map.html            # Halaman peta rekomendasi
├── app.py                  # Server backend utama (Python Flask)
├── database.json           # Database lokal (format JSON)
├── requirements.txt        # Daftar dependensi library
├── .gitignore              # Mengatur file yang tidak di-upload ke GitHub
└── README.md               # Dokumentasi proyek
```

## 🚀 Cara Menjalankan Secara Lokal

### 1. Persiapan
Pastikan Python sudah terinstal di komputer Anda, lalu clone repository berikut:

```bash
git clone https://github.com/Emzyjeppp/HematMahasiswa.git
cd HematMahasiswa
```

### 2. Instalasi
Install seluruh dependency yang dibutuhkan:

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi
Jalankan server Flask menggunakan perintah:

```bash
python app.py
```

Buka browser dan akses:

```text
http://127.0.0.1:5000
```

---

## 🛠️ Metodologi Pengembangan

Aplikasi ini dikembangkan menggunakan pendekatan **User-Centered Design (UCD)**:

- **Plan**  
  Mengidentifikasi masalah mahasiswa yang malas mencatat pengeluaran karena aplikasi keuangan dianggap terlalu rumit.

- **Analysis**  
  Melakukan riset terhadap 30 responden mengenai kebiasaan pengeluaran dan kebutuhan aplikasi keuangan sederhana.

- **Design**  
  Mendesain antarmuka minimalis dengan fokus pada kemudahan penggunaan dan tombol aksi utama.

- **Implementation**  
  Pengembangan aplikasi menggunakan Flask dan Tailwind CSS untuk performa yang ringan dan responsif.

---

## 👨‍💻 Kontributor

- GitHub: @Emzyjeppp

---

## 📌 Langkah Terakhir Push ke GitHub

Setelah menyimpan perubahan pada `README.md`, jalankan perintah berikut di terminal:

```powershell
git add README.md
git commit -m "Add final professional README"
git push origin main
```



