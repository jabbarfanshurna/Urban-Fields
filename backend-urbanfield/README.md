# Urban Field (Server-Side)

Website sewa lapangan (Tugas Web Lanjutan B)

## Nama Anggota Kelompok

- Chandra Andaya (H071241044)
- Ryan Firmansyah (H071241082)
- Abd Jabbar Fanshurna Musra (H071241088)

# Panduan Menjalankan Proyek Urban-Fields di Laptop Tim

Panduan ini disusun untuk membantu anggota tim Anda menjalankan proyek **Urban Fields** (Frontend & Backend) dari awal di laptop masing-masing.

---

## 📋 Prasyarat Sistem

Sebelum mulai, pastikan laptop setiap anggota tim sudah menginstal:

1. **Python** (Versi 3.8 s.d 3.13) -> [Download Python](https://www.python.org/downloads/)
2. **Node.js** (Versi LTS) -> [Download Node.js](https://nodejs.org/)
3. **MySQL Server** (Bisa menggunakan **XAMPP**, **Laragon**, atau MySQL Standalone)

---

## 🛠️ Langkah 1: Setup Database MySQL

Proyek ini membutuhkan database MySQL bernama `urban_fields` yang telah diisi data awal.

1. Nyalakan layanan **MySQL** di XAMPP / Laragon Anda.
2. Secara default, koneksi backend diatur ke:
    - **Host:** `localhost:3306`
    - **Username:** `root`
    - **Password:** _(kosong)_
    - **Nama Database:** `urban_fields`
      _(Jika kredensial MySQL rekan tim berbeda, mereka harus menyesuaikannya di file `backend-urbanfield/app/__init__.py` pada baris ke-14)._
3. Untuk membuat tabel dan memasukkan data dummy secara otomatis, buka terminal/command prompt, masuk ke folder **`backend-urbanfield`**, lalu jalankan perintah:
    ```bash
    python sql/init_db.py
    ```
    _Skrip ini akan otomatis membuat database `urban_fields`, membuat semua tabel, dan memasukkan data dummy._

---

## 🐍 Langkah 2: Setup & Menjalankan Backend (Flask)

1. Buka terminal baru dan masuk ke direktori backend:
    ```bash
    cd "backend-urbanfield"
    ```
2. Instal semua pustaka Python yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
3. Jalankan server Flask:
    ```bash
    python main.py
    ```
4. Jika berhasil, server akan berjalan di:
    - API Server: **`http://127.0.0.1:5000`**
    - Dokumentasi Swagger: **`http://127.0.0.1:5000/apidocs/`**

> [!WARNING]
> **Khusus Pengguna macOS:** macOS secara default menggunakan port `5000` untuk fitur AirPlay Receiver. Rekan tim yang menggunakan Mac harus mematikan AirPlay Receiver terlebih dahulu via _System Settings > General > AirPlay & Handoff_, atau mengubah port Flask di `main.py` ke port lain (misal 5001).

---

## ⚛️ Langkah 3: Setup & Menjalankan Frontend (React + Vite)

1. Buka terminal baru (biarkan server backend tetap berjalan) dan masuk ke direktori frontend:
    ```bash
    cd "frontend-urbanfield"
    ```
2. Instal semua modul Node.js (Vite, React, Tailwind, dll):
    ```bash
    npm install
    ```
3. Jalankan server development Vite:
    ```bash
    npm run dev
    ```
4. Buka browser Anda dan akses tautan berikut:
   👉 **`http://localhost:5173/`**

---

## 🔍 Mengatasi Masalah Umum (Troubleshooting)

### 1. Error: `ModuleNotFoundError: No module named '...'`

- **Penyebab:** Ada library python yang belum terinstal.
- **Solusi:** Pastikan sudah menjalankan `pip install -r requirements.txt`. Jika masih error, instal modul yang kurang secara manual, contoh: `pip install pymysql flask-jwt-extended cryptography`.

### 2. Error: `Subject must be a string` (Error 422 saat Login/Aksi)

- **Penyebab:** Ini terjadi karena update library `PyJWT` terbaru.
- **Solusi:** Kami sudah memperbaiki konfigurasi ini di repo utama dengan menambahkan `app.config['JWT_VERIFY_SUB'] = False` di `app/__init__.py`. Pastikan rekan tim melakukan `git pull` untuk mendapatkan kode terbaru.

### 3. Error saat checkout/pencarian data kosong

- **Penyebab:** Kredensial MySQL salah atau database belum diinisialisasi.
- **Solusi:** Pastikan MySQL XAMPP/Laragon menyala, dan skrip `python sql/init_db.py` sudah berhasil dijalankan tanpa error.
