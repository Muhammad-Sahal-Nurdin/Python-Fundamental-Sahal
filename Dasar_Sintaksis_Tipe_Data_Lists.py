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

print('\nClear List')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
daftar_buku[0]= 'Clean Code'
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop= Mengambil elemen yang paling ujung')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Digunakan pada saat tipe atau struktur data stack untuk optimasi data dan kecepatan program
# Push = append pada struktur data stack
print('\nPop Pop-1')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop Pop-2')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop Pop-3')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
daftar_buku.pop(3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# List Comprehension seperti di PHP
print('\nPerintah del dengan list comprehension')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
del daftar_buku[:]      # START : END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
del daftar_buku[0:3]    # Indeks mulai dari 0 namun jumlah dari 1
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
del daftar_buku[0:0:2]    # start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])





