"""
Program Perulangan "Membaca Buku" dengan for
"""

jumlahBuku = 10
print('Ibu berkata, "Baca semua bukumu!"')

jumlahBukuDibaca = 0
print(f"Jumlah buku yang dibaca {jumlahBukuDibaca}")
for jumlahBukuDibaca in range (1,jumlahBuku+1):
    print(f"jumlah buku ke-{jumlahBukuDibaca} sudah dibaca")
print(f"Jumlah buku yang sudah dibaca {jumlahBukuDibaca}")