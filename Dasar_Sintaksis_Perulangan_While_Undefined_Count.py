"""
Program Perulangan "Membaca Buku" Dengan While Sampai Paham
"""
jumlahBuku = 10
print('Ibu berkata, "Baca semua bukumu!"')
totalJumlahBaca = 0

jumlahBukuDibacaDipahami = 0
print(f"Jumlah buku yang dibaca dan dipahami{jumlahBukuDibacaDipahami}")

print("Dengan While")
while totalJumlahBaca < jumlahBuku * 2:
    totalJumlahBaca = totalJumlahBaca + 1
    if jumlahBukuDibacaDipahami == 9:
        print(f"Buku ke-{jumlahBukuDibacaDipahami + 1} belum paham")
    else:
        jumlahBukuDibacaDipahami = jumlahBukuDibacaDipahami + 1
        print(f"Buku ke-{jumlahBukuDibacaDipahami} sudah dibaca dan dipahami")


print(f"Jumlah buku yang dibaca dan dipahami {jumlahBukuDibacaDipahami}")
if jumlahBukuDibacaDipahami == jumlahBuku:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku dipahami. '
          f'Budi hanya bisa memahami {jumlahBukuDibacaDipahami}"')
