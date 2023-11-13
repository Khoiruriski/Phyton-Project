from abc import ABC, abstractmethod

print("\n============================ Selamat datang di program kalkulator sederhana saya! ============================\n")

# Membuat interface
class Operasi(ABC): #Ide 1 sek abstrak

    @abstractmethod
    def hitung(self, angka1, angka2):
        pass#pass

class Kalkulator(Operasi): # ide 2 abstrak
    def __init__(self, nama):
        self.nama = nama

    def hitung(self, angka1, angka2):
        pass

class Pertambahan(Kalkulator):
    def hitung(self, angka1, angka2):
        hasil = angka1 + angka2
        return f"{self.nama} sedang menghitung.. hasil pertambahan = {hasil}"

class Pengurangan(Kalkulator):
    def hitung(self, angka1, angka2):
        hasil = angka1 - angka2
        return f"{self.nama} sedang menghitung.. hasil pengurangan = {hasil}"

class Perkalian(Kalkulator):
    def hitung(self, angka1, angka2):
        hasil = angka1 * angka2
        return f"{self.nama} sedang menghitung.. hasil perkalian = {hasil}"

class Pembagian(Kalkulator):
    def hitung(self, angka1, angka2):
        if angka2 == 0:
            return f"pembagian di {self.nama} tidak bisa membagi 0"
        hasil = angka1 / angka2
        return f"{self.nama} sedang menghitung.. hasil pembagian = {hasil}"

class Pangkat(Kalkulator):
    def hitung(self, angka1, angka2):
        hasil = angka1 ** angka2
        return f"{self.nama} sedang menghitung.. hasil perpangkatan = {hasil}"

class PersegiPanjang(Operasi):
    def hitung(self, panjang, lebar):
        luas = panjang * lebar
        return f"Luas Persegi Panjang adalah {luas} satuan persegi"

def input_ya_tidak():
    while True:
        pilihan = input("\nApakah Anda ingin menghitung lagi, Tuan? (ya/tidak): ").lower()
        if pilihan == "ya":
            return True
        elif pilihan == "tidak":
            return False
        else:
            print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

while True:
    print("\nPilih Operasi yang anda butuhkan, Tuan :")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    print("6. Luas Persegi Panjang")

    pilihan = input("\nMasukkan nomor operasi (1-6): ")

    if pilihan not in ['1', '2', '3', '4', '5', '6']:
        print("\nHarap pilih nomor 1-6 ya Tuanku, Terima kasih.")
        continue

    if pilihan in ['1', '2', '3', '4', '5']:
        angkaPertama = float(input("\nMasukkan Angka Pertama yang ingin dihitung: "))
        angkaKedua = float(input("Masukkan Angka Kedua yang ingin dihitung: "))
    elif pilihan == '6':
        panjang = float(input("\nMasukkan panjang dari persegi panjang: "))
        lebar = float(input("Masukkan lebar dari persegi panjang: "))

    if pilihan == '1':
        operasi = Pertambahan("Kalkulator Pertambahan")
    elif pilihan == '2':
        operasi = Pengurangan("Kalkulator Pengurangan")
    elif pilihan == '3':
        operasi = Perkalian("Kalkulator Perkalian")
    elif pilihan == '4':
        operasi = Pembagian("Kalkulator Pembagian")
    elif pilihan == '5':
        operasi = Pangkat("Kalkulator Pangkat")
    elif pilihan == '6':
        operasi = PersegiPanjang()

    print(operasi.hitung(angkaPertama, angkaKedua) if pilihan in ['1', '2', '3', '4', '5'] else operasi.hitung(panjang, lebar))

    ulangi = input_ya_tidak()
    if not ulangi:
        print("\nTerima kasih telah menggunakan program ini, Tuan. Semoga Harimu Menyenangkan :)")
        break
