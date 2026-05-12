# 💸 HematMahasiswa
**Solusi Pencatatan Keuangan Cepat & Cerdas untuk Mahasiswa**

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


```yaml
PROYEK_IMK_HEMATMAHASISWA/
├── .venv/                  # Lingkungan virtual Python (Library Flask, dll)
├── static/                 # Aset Frontend statis
│   ├── css/                # Styling tambahan (jika ada)
│   └── js/                 # Logika JavaScript untuk Modal & Fetch API
├── templates/              # File HTML (Jinja2 Templates)
│   ├── index.html          # Halaman Dashboard & Input Utama
│   └── map.html            # Halaman Peta Rekomendasi
├── app.py                  # Server Backend Utama (Python Flask)
├── database.json           # Database lokal (Format JSON)
├── requirements.txt        # Daftar dependensi library
├── .gitignore              # Mengatur file yang tidak di-upload ke GitHub
└── README.md               # Dokumentasi Proyek

🚀 Cara Menjalankan Secara Lokal
1. Persiapan
Pastikan Python sudah terinstal di komputer Anda. Clone repository ini:

