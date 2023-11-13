# Deklarasi Identitas
print("\n========================== Selamat Datang Di Program Ganjil Genap     ========================\n")
print('Nama : Ainu Putri Rahmawati')
print('NIM : 22030174109\n')


print('Masukkan nilai awal dan nilai akhir\n')

# Deklarasikan Variabel
nilaiAwal = int(input('Nilai awal : '))
nilaiAkhir = int(input('Nilai akhir : '))

#Membuat Menu Program
print("\nMenu Program : \n")
print("1. Ganjil")
print("2. Genap")

# Membuat Program inputan user 
pilihanMenu = int(input("\nPilih menu 1/2 : "))

# Membuat fungsi 
if pilihanMenu == 1: #Jika menu yang dipilih adalah 1 
    for bilangan in range (nilaiAwal, nilaiAkhir + 1): #maka ulangi dari nilai awal sampai akhir dengan iterasi +1
        if bilangan % 2 != 0: #Jika bilangan dimodulus 2 hasilnya adalah bukan 0
            print(bilangan , end =" ") #Maka tampilkan fungsi bilangan

elif pilihanMenu == 2: #Jika menu yang dipilih adalah 2
    for bilangan in range(nilaiAwal,nilaiAkhir + 1): #maka ulangi dari nilai awal sampai akhir dengan iterasi +1
        if bilangan % 2 == 0: #Jika bilangan dimodulus 2 hasilnya adalah 0
            print(bilangan, end=" ") #Maka tampilkan fungsi bilangan
else:
    print("Harap masukan nomor 1 atau 2 ya, Terimakasih ! ") #Jika user nyeleneh memberikan inputan maka keluarkan pemberitahuan ini