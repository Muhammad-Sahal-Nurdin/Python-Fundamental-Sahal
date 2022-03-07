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

print('\nMembuat list baru')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru')
daftar_buku = ['Neural Networks', 'Difficult Riddles', 'Atomic Habits', 'Filosofi Teras']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Neural Networks', '2 Difficult Riddles', '3 Atomic Habits', '4 Filosofi Teras']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1 Neural Networks', '2 Difficult Riddles', '3 Atomic Habits', '4 Filosofi Teras']
daftar_buku_baru = daftar_buku[1::2] # START STOP END
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: BUANG DIUJUNG')
daftar_buku = ['1 Neural Networks', '2 Difficult Riddles', '3 Atomic Habits', '4 Filosofi Teras']
daftar_buku_baru = daftar_buku[0:-1:2] # START STOP END
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Neural Networks', '2 Difficult Riddles', '3 Atomic Habits', '4 Filosofi Teras']
print(daftar_buku[0::2])
