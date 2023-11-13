# Nama : Khoiru Rizki Bani Adam
# NIM : 22051204135
# Kelas : TI - D 2022

print("\n============================================ 1. Object Mobil ==========================================================\n")
class Mobil: # Membuat Objek Mobil
    def __init__(self, pemilik, merk, kecepatan, model, bahan_bakar):
        self.pemilik = pemilik
        self.merk = merk
        self.kecepatan = kecepatan
        self.model = model
        self.bahan_bakar = bahan_bakar
        self.mesin_hidup = False #Keadaan Mati

    def kenalkan(self):  # Mengenalkan Mobil
        print(f"{self.pemilik} seorang pemilik mobil ini dengan bermerk {self.merk} dengan kecepatan maksimal {self.kecepatan} km/jam, Memiliki Desain Model {self.model} dengan bahan bakar {self.bahan_bakar}\n")

    def nyalakan_mesin(self): # Membuat fungsi untuk menyalakan mesin

        if not self.mesin_hidup: # Jika keadaan mesim mati maka hidupkan !
            print(f"Mobil {self.merk} anda telah dihidupkan tuan.")
            self.mesin_hidup = True

        else:
            print(f"Mobil {self.merk} sudah dalam keadaan menyala tuanku.") # Jika keadaan mesin sudah hidup maka munculkan pemberitahuan bahwa mesin sudah hidup

    def matikan_mesin(self): # Membuat Fungsi untuk mematikan mesin

        if self.mesin_hidup: # jika mesin dalam kondisi hidup maka matikan
            print(f"Mobil bugati anda {self.merk} sudah dimatikan tuan.")
            self.mesin_hidup = False # inisialisasi kondisi mesin mati

        else: #Jika keadaan sudah mati maka print pemberitahuan dalam keadaan mati
            print(f"Mobil {self.merk} sudah dalam keadaan mati.") 

    def mengisi_bahan_bakar(self, liter):

        if self.mesin_hidup: #Jika mesin hidup maka beri pemberitahuan untuk mematikannya
            print(f"Harap matikan mesin terlebih dahulu sebelum mengisi bahan bakar.")

        else: #Jika sudah mati dapat di isi
            print(f"Sedang mengisi bahan bakar {liter} liter ke dalam mobil {self.merk}.")
            self.bahan_bakar += str(liter)

    def bergerak(self): #Membuat fungsi untuk menjalankan mobil kembali
        
        if not self.mesin_hidup:
            print(f"Mobil {self.merk} anda saat ini sedang bergerak dengan kecepatan {self.kecepatan} km/jam.")

        else:
            print(f"Matikan mesin terlebih dahulu sebelum mobil bisa bergerak.")

    def berhenti(self): #Fungsi untuk memberhentikan mobil

        if not self.mesin_hidup:
            print(f"Baik Tuan ! Mobil {self.merk} telah berhenti tuan {self.pemilik} semoga hari anda menyenangkan.")

        else:
            print(f"Matikan mesin terlebih dahulu sebelum mobil bisa berhenti.")


# Membuat objek Mobil
mobil1 = Mobil("Adam","Bugati", 180, "Sport", "Bensin")

# Menggunakan method untuk berinteraksi dengan objek Mobil
mobil1.kenalkan()
mobil1.nyalakan_mesin()
mobil1.matikan_mesin()
mobil1.mengisi_bahan_bakar(10)
mobil1.bergerak()
mobil1.berhenti()

print("\n============================================ 2. User(Pengguna) ==========================================================\n")
class User: #Membuat Objek User dengan Class
    def __init__(self, nama, umur, alamat_email, password, role): #Deklarasi variabel yang dipakai
        self.nama = nama
        self.umur = umur
        self.alamat_email = alamat_email
        self.password = password
        self.role = role
        self.logged_in = False

    def login(self, email, password): #Membuat Fungsi Login
        
        if self.alamat_email == email and self.password == password: #Saya Menggunakan logika And Agar bisa masuk kektika keduanya bernilai benar
            print(f"Selamat datang tuan {self.nama} !")
            self.logged_in = True
        else:
            print("Login gagal. Silakan cek kembali alamat email dan password Anda.")

    def logout(self): #Membuat fungsi log out

        if self.logged_in:
            print(f"{self.nama}, Anda telah berhasil logout.")
            self.logged_in = False #Menjadi log out
        else:
            print("Anda belum login.")

    def ganti_password(self, password_lama, password_baru): # Membuat Fungsi untuk Mengganti Password
        if self.logged_in: #Jika telah login maka jalankan

            if self.password == password_lama : #Memasukkan password harus sama dengan Password lama
                self.password = password_baru
                print("Password berhasil diganti.")

            else:
                print("Password lama salah. Gagal mengganti password.")
        else: #Jika Belum maka munculkan Pemberitahuan
            print("Anda belum login.")

    def akses_data(self):
        if self.logged_in:
            
            if self.role == "admin":
                print(f"Anda sebagai admin dapat mengakses semua data.")

            else:
                print("Anda sebagai user biasa hanya dapat mengakses data tertentu.")
                
        else:
            print("Anda belum login.")


# Membuat objek User
user1 = User("Adam", 30, "khoiru.22135@mhs.unesa.ac.id", "passwordtersulit", "user")

# Memanggil method untuk berinteraksi dengan objek User
user1.login("khoiru.22135@mhs.unesa.ac.id", "passwordtersulit")
user1.akses_data()
user1.login("khoiru.22135@mhs.unesa.ac.id", "passwordtersulit")
user1.ganti_password("passwordtersulit", "newpassword456")
user1.logout()

print("\n============================================ 3.Buku =====================================================================\n")
class Buku:
    def __init__(self, judul, penulis, tahun_terbit, penerbit, jumlah_halaman):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = str(tahun_terbit)
        self.penerbit = penerbit
        self.jumlah_halaman = str(jumlah_halaman)
        self.dipinjam = False

    def membaca(self):
        if self.dipinjam:
            print(f"Anda sedang membaca buku '{self.judul}' karya {self.penulis}.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam, Anda tidak dapat membacanya.")

    def meminjam(self):
        if not self.dipinjam:
            print(f"Anda meminjam buku '{self.judul}'.")
            self.dipinjam = True
        else:
            print(f"Buku '{self.judul}' sudah dipinjam.")

    def mengembalikan(self):
        if self.dipinjam:
            print(f"Anda mengembalikan buku '{self.judul}'.")
            self.dipinjam = False
        else:
            print(f"Buku '{self.judul}' tidak sedang dipinjam.")

    def melihat_detail(self):
        print("Detail Buku :")
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Penerbit: {self.penerbit}")
        print(f"Jumlah Halaman: {self.jumlah_halaman}")
        if self.dipinjam:
            print("Status: Sedang Dipinjam")
        else:
            print("Status: Tersedia\n")

    def cekPengembalian(self) :
        
        if self.dipinjam : True
        print("Pengembalian berhasil")



# Membuat objek Buku berdasarkan input pengguna
buku1 = Buku("Filosofi Teras", "Khoiru Rizki", 2022, "Gramedia", 540)

# Interaksi dengan objek Buku
buku1.melihat_detail()
buku1.meminjam()
buku1.membaca()
buku1.mengembalikan()
buku1.cekPengembalian()

print("\n============================================ 4. HP(Handphone) ==========================================================\n")
class Handphone:
    def __init__(self, merek, model, sistem_operasi, kapasitas_baterai, ukuran_layar):
        self.merek = merek
        self.model = model
        self.sistem_operasi = sistem_operasi
        self.kapasitas_baterai = kapasitas_baterai
        self.ukuran_layar = ukuran_layar

    def spesifikasi (self):
        print(f"Merk handphone : {self.merek}")
        print(f"Model : {self.model}")
        print(f"Sistem Operasi : {self.sistem_operasi}")
        print(f"Kapasitas Baterai : {self.kapasitas_baterai} mAh")
        print(f"Ukuran layar : {self.ukuran_layar}\n")

    def mengirim_pesan(self, pesan, penerima):
        print(f"Mengirim pesan: '{pesan}' kepada {penerima} menggunakan handphone {self.merek} {self.model}.")

    def menerima_panggilan(self, pemanggil):
        print(f"Terima panggilan dari {pemanggil} pada handphone {self.merek} {self.model}.")

    def mengambil_foto(self):
        print(f"Ckrekkkk !!!, Mengambil foto dengan handphone {self.merek} {self.model}.")

    def memutar_musik(self, lagu):
        print(f"Memutar lagu: '{lagu}' di handphone {self.merek} {self.model}.")


# Membuat objek Handphone
handphone1 = Handphone("Samsung", "Galaxy S21", "Android", 4000, "6.2 inch")

# Interaksi dengan objek Handphone
handphone1.spesifikasi()
handphone1.menerima_panggilan("Adam")
handphone1.mengirim_pesan("Halo, apa kabar?", "Hawa")
handphone1.mengambil_foto()
handphone1.memutar_musik("Raja Dangdut")


print("\n =========================================== 5. Hero =========================================================")
class Hero(object) :
    print("\n                             Game !!!! Start !!! Bismillah !!!                                 ")
    def __init__(self, inputNama, inputDarah, inputLevel, inputSkill, inputSenjata, inputDamage, InputArmor):

        self.nama    = inputNama
        self.darah   = inputDarah
        self.level   = inputLevel
        self.skill   = inputSkill
        self.senjata = inputSenjata
        self.damage  = inputDamage
        self.armor    = InputArmor

    def menyerang(self, lawan):
        print("\n" + self.nama, "Menyerang", lawan.nama, "dengan", self.senjata + ",", lawan.nama, "langsung terkena", self.damage, "damage")
        lawan.diserang(self)

    def diserang(self, lawan):
        damageSerangan = lawan.damage
        self.darah    -= damageSerangan
        print(self.nama, "diserang", lawan.nama, "dan mendapat", lawan.damage, "damage ( Darah", self.nama, "tersisa", self.darah, ")")

Adam = Hero("Adam", 1000, "Max", 3, "Meruqyahnya", 999, 350)
Iblis = Hero("Iblis", 1000, "Max", 2, "Menyesatkanya", 1, 350)

while True:

    Adam.menyerang(Iblis)
    Iblis.menyerang(Adam)

    if Adam.darah <= 0:
        print("\n=================== Adam Mati  ===================")
        break
    elif Iblis.darah <= 0:
        print(f"\n=================== Iblis Mati ditangan Adam  ===================")
        break

class KipasAngin:
    def _init_(self, jumlah_bilah, ukuran, kecepatan):
        self.jumlah_bilah = jumlah_bilah
        self.ukuran = ukuran
        self.kecepatan = kecepatan
        self.dalam_keadaan_hidup = False  # Awalnya dalam keadaan mati

    def hidupkan(self):
        if not self.dalam_keadaan_hidup:
            self.dalam_keadaan_hidup = True
            print("Kipas angin telah dihidupkan.")
        else:
            print("Kipas angin sudah dalam keadaan hidup.")

    def matikan(self):
        if self.dalam_keadaan_hidup:
            self.dalam_keadaan_hidup = False
            print("Kipas angin telah dimatikan.")
        else:
            print("Kipas angin sudah dalam keadaan mati.")

    def berputar(self):
        if self.dalam_keadaan_hidup:
            print("Kipas angin sedang berputar dengan kecepatan", self.kecepatan)
        else:
            print("Nyalakan kipas angin terlebih dahulu untuk membuatnya berputar.")


# Contoh penggunaan class KipasAngin
kipas = KipasAngin(jumlah_bilah =3, ukuran ="medium", kecepatan ="tinggi")

kipas.hidupkan()
kipas.berputar()
kipas.matikan()
kipas.berputar()