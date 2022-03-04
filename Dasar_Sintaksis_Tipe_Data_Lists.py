daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
print("\nTamipilkan variabel daftar buku")
print(daftar_buku)

print("\nProses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print("\nTampilkan dengan for in range ")
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nTampilkan dalam for in range, di mana tipe data setiap elemen berbeda-beda")
daftar_buku = [1, 'The book of ikigai', 3.14, -313]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nKembalikan nilai daftar_buku")
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
print("Tambahkan 1 buku baru")
daftar_buku.append("Kalkulus jilid 1")
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


