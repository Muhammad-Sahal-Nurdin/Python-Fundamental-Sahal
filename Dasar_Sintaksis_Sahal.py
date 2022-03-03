
"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
print("Hello World")
print("My name is Muhammad Sahal Nurdin")
print('Saya dari kelas 1IA12')

# Sekuensial

print("Ibu berkata, \"Pergi ke toko\"")
print('Budi menjawab, "Baik, Apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Belikan satu botol susu dan jika ada telur beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbalanja")



# Percabangan

# Tugas
susu = 1
telur = 1
harga = 0
if susu == 1:
    print("Ada susu")
    if harga == 1:
        print("Uang cukup")
        if telur == 1:
            print("Beli 6 telur" + " dan 1 botol susu")
        else:
            print("Beli 1 botol susu" + "Pulang ke rumah")
    else:
        print("Uang tidak cukup")
else:
    print("Tidak ada yang di beli")


jumlah_Botol_Susu = 173
jumlah_Telur= 1587
print(f"Jumlah botol susu {jumlah_Botol_Susu} btl")
print(f"Jumlah telur {jumlah_Telur} butir")

if jumlah_Botol_Susu > 0:
    print("Budi memngecek harganya. dan ternyata uangnya cukup.")
    if jumlah_Telur == 1:
        print("Budi membeli 1 botol susu.")
    else:
        print("Budi membeli ")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah dan menterahkan hasi kepada Ibu")