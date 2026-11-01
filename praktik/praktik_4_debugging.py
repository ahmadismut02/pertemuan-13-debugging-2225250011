def hitung_rata_rata(nilai):
    return sum(nilai) / len (nilai)

def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    tertinggi = max (nilai)
    return tertinggi

nilai = [100, 80]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(59))
print("Tertinggi:", nilai_tertinggi(nilai))