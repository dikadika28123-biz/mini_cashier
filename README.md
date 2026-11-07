Mini Cashier — Python Project

Mini Cashier adalah proyek latihan Python yang dikembangkan secara bertahap untuk menerapkan konsep dasar pemrograman ke dalam program kasir sederhana.

Proyek ini dibuat sebagai bagian dari perjalanan belajar Python, dengan pendekatan belajar → memahami → mengimplementasikan → menguji.

---

Project Overview

Mini Cashier merupakan program kasir sederhana berbasis terminal (CLI) yang menerima input barang, harga, dan jumlah pembelian, kemudian menghitung total belanja serta menentukan diskon berdasarkan status member.

Proyek ini dikembangkan secara bertahap mengikuti materi pembelajaran Python.

Version History

Mini Cashier V1.1 — Basic Cashier

Versi awal berfokus pada proses transaksi sederhana.

Fitur:

- Input nama barang.
- Input harga barang.
- Input jumlah barang.
- Menghitung total belanja.
- Menampilkan struk sederhana.

Konsep Python yang diterapkan:

- Variables
- Data Types
- Input & Output
- Type Conversion
- Arithmetic Operators
- F-Strings

Mini Cashier V2 — Member Discount System

Versi kedua menambahkan sistem diskon berdasarkan status member dan total belanja.

Fitur tambahan:

- Input status member.
- Menentukan diskon berdasarkan kondisi pembelian.
- Menghitung nominal potongan.
- Menghitung pembayaran akhir.
- Menampilkan persentase diskon pada struk.

Aturan diskon:

Status Member| Total Belanja| Diskon
Tidak| Berapa pun| 0%
Iya| Di bawah Rp25.000| 5%
Iya| Rp25.000 atau lebih| 10%

---

Python Concepts Applied

Module 01 — Variables & Data Types

Digunakan untuk menyimpan informasi transaksi, seperti:

- "barang1"
- "harga1"
- "jumlah1"
- "member"
- "total"
- "diskon"
- "potongan"
- "bayar"

Program menggunakan tipe data "str", "int", dan "float" sesuai kebutuhan.

Module 02 — Operators & Expressions

Operator matematika digunakan untuk menghitung transaksi:

- "*" untuk menghitung total harga barang.
- "*" untuk menghitung nominal diskon.
- "-" untuk menghitung pembayaran akhir.

Module 03 — Input & Output

Program menerima data menggunakan "input()" dan menampilkan hasil menggunakan "print()".

Konversi tipe data digunakan agar harga dan jumlah dapat dihitung secara matematis.

F-Strings digunakan untuk menampilkan informasi transaksi dengan format yang lebih terstruktur.

Module 04 — Conditional Statements

Mini Cashier V2 menerapkan konsep percabangan untuk menentukan kelayakan diskon.

Nested If

Program menggunakan nested "if" untuk memeriksa status member terlebih dahulu, kemudian memeriksa total belanja.

if member == "Iya":
    if total >= 25000:
        diskon = 0.10
    else:
        diskon = 0.05

Logika tersebut menghasilkan:

- Member dengan belanja minimal Rp25.000 mendapatkan diskon 10%.
- Member dengan belanja di bawah Rp25.000 mendapatkan diskon 5%.

Else

Jika pembeli bukan member, diskon tetap 0% karena nilai awal variabel "diskon" sudah ditetapkan menjadi 0.

Perhitungan setelah percabangan

Setelah persentase diskon ditentukan, program menghitung nominal potongan dan pembayaran akhir.

potongan = total * diskon
bayar = total - potongan

Hal ini menunjukkan penerapan conditional statements dalam menentukan nilai variabel yang kemudian digunakan pada proses perhitungan berikutnya.

---

How It Works

1. Program menampilkan header Mini Cashier.
2. Pengguna memasukkan nama barang.
3. Pengguna memasukkan harga dan jumlah barang.
4. Pengguna menentukan status member.
5. Program menghitung total belanja.
6. Program memeriksa status member dan menentukan persentase diskon.
7. Program menghitung nominal potongan.
8. Program menghitung pembayaran akhir.
9. Program menampilkan struk transaksi.

---

How to Run

Pastikan Python telah terinstal di perangkat.

Jalankan file program melalui terminal:

python mini_cashier.py

Program akan meminta input transaksi dan menampilkan hasilnya secara langsung.

---

📄 Example Output

================================
        MINI CASHIER
================================

Masukkan nama barang pertama : Buku
Masukkan harga barang pertama : 30000
Masukkan jumlah barang pertama : 2
Apakah anda member ? Iya / Tidak : Iya

========== STRUK BELANJA ==========
Nama barang   : Buku
Harga barang  : Rp30000
Jumlah        : 2
Total belanja : Rp60000
Diskon        : 10%
Bayar         : 54000
=================================
Terima kasih telah berbelanja!

---

Project Objectives

Mini Cashier dikembangkan untuk:

- Mempraktikkan materi Python secara bertahap.
- Memahami hubungan antara input, proses, dan output.
- Mengimplementasikan logika percabangan dalam program nyata.
- Melatih kemampuan menyusun program secara mandiri.
- Menjadi fondasi untuk pengembangan sistem kasir yang lebih kompleks.

---

Future Development

Rencana pengembangan berikutnya:

- Multiple item / banyak barang.
- Input validation.
- Exception handling.
- Perulangan transaksi.
- Penggunaan functions.
- Penyimpanan data transaksi.
- Integrasi database.

---

Developer

Andhika Syahputra

Python Learner · Aspiring Developer

Proyek ini merupakan bagian dari perjalanan belajar Python melalui praktik dan pengembangan proyek nyata.

---

Learn → Build → Test → Improve.

GitHub: "dikadika28123-biz" (https://github.com/dikadika28123-biz)
