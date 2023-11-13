print("\n ============================ Selamat datang di program kalkulator sederhana saya! ==================================\n")
class Kalkulator:
    def __init__(self,nama):
        self.nama = nama

    def pertambahan(self, angkaPertama, angkaKedua):
        hasil = angkaPertama + angkaKedua
        return f"\n{self.nama} sedang menghitung.. hasil pertambahan = {hasil}"

    def pengurangan(self, angkaPertama, angkaKedua):
        hasil = angkaPertama - angkaKedua
        return f"\n{self.nama} sedang menghitung.. hasil pengurangan = {hasil}"

    def perkalian(self, angkaPertama, angkaKedua):
        hasil = angkaPertama * angkaKedua
        return f"\n{self.nama} sedang menghitung.. hasil pengurangan = {hasil}"
    
    def pembagian(self, angkaPertama, angkaKedua):
        if angkaKedua == 0 :
            return f"\npembagian di {self.nama} tidak bisa membagi 0  "
        hasil = angkaPertama / angkaKedua
        return f"{self.nama} \n sedang menghitung.. hasil pengurangan = {hasil}"
    
def input_ya_tidak():
    while True:
        pilihan = input("\nApakah Anda ingin menghitung lagi tuan ? (ya/tidak): ").lower()
        if pilihan == "ya":
            return True
        elif pilihan == "tidak":
            return False
        else:
            print("Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
while True:
    KalkulatorDigital = Kalkulator ("Kalkulator Digital")

    print("\nPilih Operasi yang anda butuhkan, Tuan :")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("3. Pembagian")

    pilihan = input("\nMasukkan nomor operasi (1-4): ")

    angkaPertama = float(input("\nMasukkan Angka Pertama yang ingin dihitung: "))
    angkaKedua = float(input("Masukkan Angka Kedua yang ingin dihitung: "))

    if pilihan == '1':
        print(KalkulatorDigital.pertambahan(angkaPertama, angkaKedua))
    elif pilihan == '2':
        print(KalkulatorDigital.pengurangan(angkaPertama, angkaKedua))
    elif pilihan == '3':
        print(KalkulatorDigital.perkalian(angkaPertama, angkaKedua))
    elif pilihan == '4':
        print(KalkulatorDigital.pembagian(angkaPertama, angkaKedua))
    else:
        print("\nHarap dipilih nomer 1-4 ya Tuanku, Terimakasih.")
    
    ulangi = input_ya_tidak()
    if not ulangi:
        print("\nTerima kasih telah menggunakan program ini tuan, Semoga Harimu Menyenangkan :)")
        break