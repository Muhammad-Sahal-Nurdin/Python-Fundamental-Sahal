"""
Program Perulangan "Membaca Buku" Dengan While
"""
jumlahBuku = 10
print('Ibu berkata, "Baca semua bukumu!"')

jumlahBukuDibaca = 0
print(f"Jumlah buku yang dibaca {jumlahBukuDibaca}")

print("Dengan While")
while jumlahBukuDibaca < jumlahBuku:
    jumlahBukuDibaca = jumlahBukuDibaca + 1
    print(f"Buku ke-{jumlahBukuDibaca} sudah dibaca")


print(f"Jumlah buku yang dibaca {jumlahBukuDibaca}")
