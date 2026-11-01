# Pertemuan 13 - Debugging dan Testing

Nama: [Nama Lengkap Anda]
NIM: [NIM Anda]
Kelas: [Kelas Anda]

## Kasus
Program yang diuji adalah script Python untuk memproses data nilai mahasiswa (`praktik/praktik_4_debugging.py`). Program ini mencakup fungsi untuk menghitung rata-rata nilai, menentukan status kelulusan (lulus/tidak lulus), dan mencari nilai tertinggi dari sebuah list nilai, namun sengaja dirancang memiliki beberapa bug tersembunyi[cite: 9].

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | rata-rata | `[80, 60, 90, 70]` | `75.0` | [Isi hasil aktual] | [FAIL/PASS] |
| T2 | rata-rata | `[100, 80]` | `90.0` | [Isi hasil aktual] | [FAIL/PASS] |
| T3 | status | `60` | `Lulus` | [Isi hasil aktual] | [FAIL/PASS] |
| T4 | status | `59` | `Tidak lulus` | [Isi hasil aktual] | [FAIL/PASS] |
| T5 | tertinggi | `[80, 60, 90, 70]` | `90` | [Isi hasil aktual] | [FAIL/PASS] |

## Bug Report
1. **Bug ID: B01 (Fungsi Rata-rata)**
   * **Gejala:** Hasil perhitungan rata-rata salah jika panjang list data tidak sama dengan 5.
   * **Lokasi:** Fungsi `hitung_rata_rata()` pada baris awal script.
   * **Akar Penyebab:** Program membagi total nilai dengan angka statis `5` (`sum(nilai) / 5`) alih-alih membaginya dengan jumlah elemen aktual menggunakan fungsi `len(nilai)`.
   * **Perbaikan:** Mengubah pembagi statis menjadi `len(nilai)` serta menambahkan validasi jika list kosong agar tidak terjadi `ZeroDivisionError`.

2. **Bug ID: B02 (Fungsi Status Kelulusan)**
   * **Gejala:** Nilai `60` dianggap "Tidak lulus" padahal batas kelulusan yang diharapkan adalah $\ge 60$.
   * **Lokasi:** Fungsi `status()` pada pengkondisian nilai.
   * **Akar Penyebab:** Operator perbandingan menggunakan tanda lebih besar (`> 60`) sehingga angka tepat di batas (`60`) ikut tidak lulus.
   * **Perbaikan:** Mengubah operator perbandingan menjadi lebih besar atau sama dengan (`>= 60`).

3. **Bug ID: B03 (Fungsi Nilai Tertinggi)**
   * **Gejala:** Program mengembalikan nilai `0` meskipun seluruh nilai mahasiswa di atas nol (atau salah dalam mencari nilai maksimum).
   * **Lokasi:** Fungsi `nilai_tertinggi()` pada inisialisasi variabel dan logika iterasi.
   * **Akar Penyebab:** Variabel `tertinggi` diinisialisasi dengan angka `0` dan kondisi perbandingan menggunakan tanda `<` yang salah arah untuk mencari nilai maksimal.
   * **Perbaikan:** Menginisialisasi nilai awal dengan elemen pertama dari list atau `None` untuk list kosong, serta memperbaiki logika pembanding menjadi pencarian nilai maksimum (`>`).

## Retest
Catat hasil pengujian setelah perbaikan kode dilakukan (pastikan seluruh test case dari T1 sampai T5 berstatus **PASS** tanpa ada regresi)[cite: 10].

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi
**Teknik debugging yang paling membantu:** Menggunakan *breakpoint* dan panel *Variables* di VS Code karena memungkinkan saya melihat perubahan nilai variabel secara langsung langkah demi langkah tanpa harus menebak-nebak.
