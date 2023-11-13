
print("\n================================== Selamat Datang Di Menu Kasir Kami ! ===============================\n")
print("Silahkan pilih submenu yang tersedia pada Menu utama !")

import json #Ini mengimpor modul JSON yang diperlukan untuk bekerja dengan data JSON.
from abc import ABC, abstractmethod #ini mengimpor kelas ABC dan dekorator abstractmethod dari modul abc yang digunakan untuk mendefinisikan kelas abstrak dan metode abstrak.

# INTERFACE untuk Item
class InterfaceItem(ABC): # Ini mendefinisikan kelas abstrak InterfaceItem yang menggambarkan sebuah antarmuka (interface) dengan satu metode abstrak get_info.
    @abstractmethod #Ini adalah dekorator yang digunakan untuk mendeklarasikan metode get_info dibawah sebagai metode abstrak dalam kelas InterfaceItem.
    def get_info(self):
        pass

# ABSTRAK 
# Class abstrak untuk Item
class Barang(ABC): #class Barang(ABC):: Ini mendefinisikan kelas abstrak Barang yang mewakili barang dengan atribut seperti nama, harga, stok, dan kategori.
    def __init__(self, nama, harga, stok, kategori): #Ini adalah konstruktor kelas Barang yang menerima parameter nama, harga, stok, dan kategori. Tujuannya adalah untuk menginisialisasi atribut-atribut objek.
        self.nama = nama #Ini menginisialisasi atribut nama objek dengan nilai dari parameter nama.
        self.harga = harga #harga: Ini menginisialisasi atribut harga objek dengan nilai dari parameter harga.
        self.stok = stok # Ini menginisialisasi atribut stok objek dengan nilai dari parameter stok.
        self.kategori = kategori #Ini menginisialisasi atribut kategori objek dengan nilai dari parameter kategori.

    @abstractmethod #Ini mendeklarasikan metode get_info dibawah sebagai metode abstrak dalam kelas Barang.
    def get_info(self): 
        pass
# INHERITANCE
# Class Produk adalah subclass dari Item
class Produk(Barang): # Ini mendefinisikan kelas Produk yang merupakan subclass dari Barang. Produk adalah salah satu jenis barang.
    def __init__(self, nama, harga, stok, kategori): #Ini adalah konstruktor kelas Produk yang menerima parameter yang sama seperti kelas Barang. Itu juga memanggil konstruktor superclass menggunakan super().
        super().__init__(nama, harga, stok, kategori) #Ini memanggil konstruktor kelas Barang superclass untuk menginisialisasi atribut dari Barang
    # POLIMORFISME
    # Overriding metode get_info dari kelas Barang
    def get_info(self): #Ini mendefinisikan metode get_info yang digantikan (overriding) dari kelas Barang. Ini mengembalikan informasi tentang produk.
        return f"{self.nama} - Harga: Rp.{self.harga:.3f} - Stok: {self.stok} - Kategori: {self.kategori}"

# Class Layanan adalah subclass dari Item
class Layanan(Barang): #Ini mendefinisikan kelas Layanan yang juga merupakan subclass dari Barang. Layanan adalah jenis barang lainnya, dan kelas ini menggantikan metode get_info dari kelas `Barang.
    # Overriding metode get_info dari kelas Barang
    def get_info(self):
        return f"{self.nama} - Harga: Rp.{self.harga:.3f} - Persediaan: {self.stok} jam layanan"

# Class Kasir untuk mengelola pembelian dan item
class Kasir: #Ini adalah definisi kelas Kasir yang bertanggung jawab untuk mengelola pembelian dan item dalam toko.
    def __init__(self): #Ini adalah konstruktor kelas Kasir. Ketika objek Kasir dibuat, metode ini akan dijalankan. Ini menginisialisasi dua atribut, self.barang dan self.keranjang, dan memanggil metode muat_dari_json untuk memuat data barang dari file JSON saat program dimula
        self.barang = [] #ini menginisialisasi atribut barang dengan daftar kosong yang akan digunakan untuk menyimpan barang-barang yang dijual.
        self.keranjang = [] #Ini menginisialisasi atribut keranjang dengan daftar kosong yang akan digunakan untuk menyimpan item dalam keranjang belanja

        # Memanggil metode muat_dari_json saat objek Kasir dibuat
        self.muat_dari_json("barang.json")  # Ini akan memuat data barang dari file JSON saat program dimulai

    def tambah_barang_baru(self, barang): # Ini adalah metode yang memungkinkan pengguna untuk menambahkan barang baru ke daftar barang di toko. Ini menerima objek barang dan menambahkannya ke self.barang.
        self.barang.append(barang) # Ini menambahkan objek barang ke daftar self.barang
        print(f"\nBarang baru {barang.nama} telah ditambahkan.") #Ini mencetak pesan konfirmasi bahwa barang baru telah ditambahkan ke daftar.

    def tambah_item(self, barang, jumlah): #Ini adalah metode yang memungkinkan pengguna untuk menambahkan barang ke keranjang belanja. Ini menerima objek barang dan jumlah yang diinginkan, kemudian menambahkannya ke self.keranjang.
        item = [barang, jumlah] #Ini membuat item baru yang berisi objek barang dan jumlahnya.
        self.keranjang.append(item) # Ini menambahkan item ke dalam keranjang belanja.
        print(f"\n{barang.nama} telah ditambahkan ke dalam keranjang belanja")  #: Ini mencetak pesan konfirmasi bahwa barang telah ditambahkan ke keranjang.

    def hapus_item(self, nama_barang): # Ini adalah metode yang memungkinkan pengguna untuk menghapus barang dari daftar belanja dengan menyebutkan nama barang.
        for barang in self.barang: #Ini mengulang semua barang dalam daftar self.barang.
            if barang.nama == nama_barang: # Ini memeriksa apakah nama barang yang diberikan cocok dengan nama barang dalam daftar.
                self.barang.remove(barang) #Jika ada kecocokan, maka barang tersebut dihapus dari daftar.
                print(f"\n{nama_barang} telah dihapus dari daftar belanja.")
                return #ini mencetak pesan konfirmasi bahwa barang telah dihapus dari daftar.
        print(f"{nama_barang} tidak ditemukan dalam daftar belanja.") #Jika tidak ada barang yang cocok, maka mencetak pesan bahwa barang tidak ditemukan.

    def perbarui_stok(self, nama_barang, stok_baru): # Ini adalah metode yang memungkinkan pengguna untuk memperbarui stok suatu barang dalam daftar belanja dengan menyebutkan nama barang dan jumlah stok baru.
        for barang in self.barang: #Ini mengulang semua barang dalam daftar self.barang.
            if barang.nama == nama_barang: # Ini memeriksa apakah nama barang yang diberikan cocok dengan nama barang dalam daftar.
                barang.stok = stok_baru #Jika ada kecocokan, maka stok barang tersebut diperbarui dengan nilai yang baru.
                print(f"\nStok {nama_barang} telah diperbarui menjadi {stok_baru}.")
                return# Ini mencetak pesan konfirmasi bahwa stok barang telah diperbarui.
        print(f"\n{nama_barang} tidak ditemukan dalam daftar belanja.") #Jika tidak ada barang yang cocok, maka mencetak pesan bahwa barang tidak ditemukan.

    def checkout(self): #Ini adalah metode yang digunakan untuk menyelesaikan transaksi belanja dan menghasilkan struk pembelian.
        print("\n---------- Struk Pembelian ----------\n")
        total_harga = 0 #Inisialisasi variabel total_harga yang akan digunakan untuk menghitung total harga.
        for barang, jumlah in self.keranjang: #Ini mengulang semua item dalam keranjang belanja.
            total_harga += barang.harga * jumlah # Ini menghitung total harga dengan mengalikan harga barang dengan jumlah yang dibeli.
            print(f"{barang.nama} - Harga: Rp.{barang.harga * jumlah:.3f}")# Ini mencetak informasi tentang barang yang dibeli dan harganya dalam format yang rapi.
        print(f"\nTotal Harga: Rp.{total_harga:.3f}")#Ini mencetak total harga belanja dalam format yang rapi.
        print("\nTerima kasih telah berbelanja ! Semoga Harimu Menyenangkan !")
        print("\n---------------------------------------")

    def simpan_ke_json(self, nama_file): # Ini adalah metode yang digunakan untuk menyimpan data barang ke dalam file JSON.
        data_barang = [] #Inisialisasi list data_barang yang akan digunakan untuk menyimpan data barang.
        for barang in self.barang: # Ini mengulang semua barang dalam daftar self.barang.
            data_barang.append({
                "nama": barang.nama,
                "harga": barang.harga,
                "stok": barang.stok,
                "kategori": barang.kategori
            }) #Ini menambahkan informasi tentang barang (nama, harga, stok, dan kategori) ke dalam list data_barang.

        with open(nama_file, "w") as file: #Ini membuka file JSON dengan mode penulisan.
            json.dump(data_barang, file, indent=4) #Ini menyimpan data dalam format JSON ke dalam file dengan indentasi 4.

    def tampilkan_keranjang(self):# Ini adalah metode yang digunakan untuk menampilkan isi keranjang belanja kepada pengguna.
        if not self.keranjang: #Ini memeriksa apakah keranjang belanja kosong.
            print("Keranjang belanja anda kosong")
        else: #Jika keranjang tidak kosong, mencetak header yang menunjukkan keranjang belanja ada barang.
            print("Keranjang Belanja anda berisi :\n")
            for barang, jumlah in self.keranjang: #Ini mengulang semua item dalam keranjang belanja.
                print(f"{barang.nama} - Jumlah: {jumlah} - Harga: Rp.{barang.harga * jumlah:.3f}") # Ini mencetak informasi tentang barang yang ada dalam keranjang belanja.

    def hitung_total_harga(self): #: Ini adalah metode yang digunakan untuk menghitung total harga dari barang-barang dalam keranjang belanja.
        total_harga = 0# Inisialisasi variabel total_harga yang akan digunakan untuk menghitung total harga.
        for barang, jumlah in self.keranjang: #Ini mengulang semua item dalam keranjang belanja.
            total_harga += barang.harga * jumlah #Ini menghitung total harga dengan mengalikan harga barang dengan jumlah yang dibeli.
        return total_harga # Ini mengembalikan total harga.

    def muat_dari_json(self, nama_file): # Ini adalah metode yang digunakan untuk memuat data barang dari file JSON ke dalam daftar barang toko.
        try: #Ini memulai blok percobaan untuk menangani pengecualian jika file JSON tidak ditemukan.
            with open(nama_file, "r") as file: # Ini membuka file JSON dengan mode baca ("r").
                data = json.load(file) #Ini membaca data dari file JSON.
                self.barang = [] # Ini mengosongkan daftar self.barang untuk persiapan pengisian ulang data.

                # Memproses data dari file JSON dan menambahkannya ke daftar barang
                for data_barang in data: # Ini mengulang semua data barang yang ada dalam file JSON.
                    if data_barang["kategori"] == "Layanan": # Ini memeriksa kategori barang.
                        barang = Layanan(data_barang["nama"], data_barang["harga"], data_barang["stok"], data_barang["kategori"]) # Jika kategori adalah "Layanan", maka membuat objek Layanan dan menambahkannya ke daftar barang.
                    else: # Jika kategori bukan "Layanan", maka barang adalah "Produk", dan objek Produk yang sesuai dibuat.
                        barang = Produk(data_barang["nama"], data_barang["harga"], data_barang["stok"], data_barang["kategori"])
                    self.barang.append(barang) # Ini menambahkan objek barang ke daftar self.barang.

                print("Data telah dimuat dari file JSON.") # Ini mencetak pesan konfirmasi bahwa data telah dimuat dari file JSON.
        except FileNotFoundError: #ni menangani pengecualian jika file JSON tidak ditemukan.
            print("File JSON tidak ditemukan.")

    def tampilkan_daftar_produk(self): #Ini adalah metode yang digunakan untuk menampilkan daftar produk yang tersedia di toko.
        print("\n========== Daftar Produk: ===========\n")
        for barang in self.barang: #Ini mengulang semua barang yang ada dalam daftar self.barang.
            print(barang.get_info()) # Untuk setiap barang, mencetak informasi tentang barang tersebut dengan memanggil metode get_info() yang ada pada objek barang. Metode ini telah diimplementasikan untuk setiap jenis barang yang dapat berbeda dalam struktur dan kontennya.
        print("\n") # Ini mencetak baris kosong untuk memisahkan setiap entri produk.

# Kelas Pengguna (Admin/Kasir)
class Pengguna: #ini adalah definisi kelas Pengguna yang digunakan untuk mengelola interaksi antara pengguna (Admin/Kasir) dan sistem kasir.
    def __init__(self, kasir): #Ini adalah metode konstruktor yang menerima parameter kasir yang akan digunakan untuk mengakses objek Kasir.
        self.kasir = kasir # Menyimpan objek Kasir sebagai atribut self.kasir untuk digunakan dalam kelas ini.

    def menu_admin(self): # Ini adalah metode yang mengatur tampilan dan logika untuk menu admin.
        while True: #Ini memulai loop tak terbatas untuk menu admin.
            print("\n========== Menu Admin ===========:\n")
            print("1. Tambah Produk Baru")
            print("2. Perbarui Stok")
            print("3. Lihat Daftar Produk")
            print("4. Hapus Produk")
            print("5. Simpan semua item ke JSON")
            print("6. Keluar dari menu admin")

            pilihan = input("\nSilahkan pilih menu (1/2/3/4/5/6): ")

            if pilihan == "1":
                nama = input("\nMasukkan Nama Produk: ")
                harga = float(input("\nMasukkan Harga Produk: "))
                stok = int(input("Masukkan stok produk: "))
                kategori = input("Masukkan Kategori Produk: ")
                produk = Produk(nama, harga, stok, kategori)
                self.kasir.tambah_barang_baru(produk)

            elif pilihan == "2":
                nama_barang = input("Masukkan Nama Barang yang akan diperbarui stoknya: ")
                stok_baru = int(input(f"Masukkan jumlah stok baru pada {nama_barang}: "))
                self.kasir.perbarui_stok(nama_barang, stok_baru)

            elif pilihan == "3":
                self.kasir.tampilkan_daftar_produk()  # Menampilkan daftar produk

            elif pilihan == "4":
                nama_barang = input("Masukkan Nama Barang yang akan dihapus: ")
                self.kasir.hapus_item(nama_barang)  # Menghapus produk dari daftar

            elif pilihan == "5":
                self.kasir.simpan_ke_json("barang.json")
                print("\nBarang Telah Disimpan ke dalam JSON")

            elif pilihan == "6":
                print("\nAnda Keluar Dari Menu Admin.")
                break

            else:
                print("Pilihan tidak tersedia, silahkan pilih nomer menu dengan benar, Terimakasih !")

    def menu_kasir(self): #Ini adalah metode yang memungkinkan kasir untuk mengelola keranjang belanja dan melakukan checkout.
        while True: #Memulai loop tak terbatas sehingga kasir dapat terus menggunakan menu kasir.
            print("\n=============== Menu Kasir ===============:\n")
            print("1. Tambahkan Barang Ke Keranjang")
            print("2. Lihat Keranjang")
            print("3. Checkout")
            print("4. Keluar dari menu kasir")

            pilihan = input("\nSilahkan pilih menu antara (1/2/3/4): ") #Mengambil pilihan menu dari input kasir.

            if pilihan == "1":
                nama_barang = input("\nMasukkan nama barang: ")
                for barang_tersedia in self.kasir.barang:
                    if barang_tersedia.nama == nama_barang:
                        barang = barang_tersedia
                        break
                if barang:
                    jumlah = int(input(f"\nMasukkan jumlah untuk {nama_barang}: "))
                    if jumlah <= barang.stok:
                        barang.stok -= jumlah
                        self.kasir.tambah_item(barang, jumlah)
                        print(f"\n{jumlah} {nama_barang} ditambahkan dalam keranjang.")
                    else:
                        print(f"\nStok {nama_barang} tidak mencukupi.")
                else:
                    print(f"\n{nama_barang} tidak ditemukan dalam daftar produk.")

            elif pilihan == "2":
                print("\n============ Menu Keranjang Belanja: ================\n")
                self.kasir.tampilkan_keranjang()

            elif pilihan == "3":
                if not self.kasir.keranjang:
                    print("\nTidak bisa checkout. Keranjang kosong.")
                else:
                    total_harga = self.kasir.hitung_total_harga()
                    print(f"\nTotal harga: Rp. {total_harga:.3f}")
                    metode_pembayaran = input("\nPilih metode pembayaran (tunai/debit): ")
                    if metode_pembayaran == "debit":
                        info_kartu = input("\nMasukkan informasi kartu debit: ")

                        # Implementasikan pembayaran dengan kartu debit di sini
                    print("\nTerima kasih telah berbelanja ! Semoga Harimu Menyenangkan !\n")
                    self.kasir.checkout()
                    self.kasir.simpan_ke_json("barang.json")  # ini akan menyimpan stok yang diperbarui ke file JSON

            elif pilihan == "4": #Menangani kasus jika kasir memilih untuk keluar dari menu kasir.
                print("\nAnda telah Keluar dari menu Kasir.")
                break #Mengakhiri loop dan kembali ke menu utama.

            else: #: Ini mencetak pesan jika pilihan yang dimasukkan oleh kasir tidak valid.
                print("\nPilihan tidak tersedia, silahkan pilih nomer menu dengan benar, Terimakasih !")

# Program Utama
if __name__ == "__main__": #ini adalah blok yang menjalankan program jika file ini dijalankan sebagai program utama (bukan sebagai modul yang diimpor).
    kasir = Kasir() #Membuat objek kasir dari kelas Kasir untuk memulai program.
    pengguna = Pengguna(kasir) #Membuat objek pengguna dari kelas Pengguna dan memberikan objek kasir ke dalamnya.

    while True:
        print("\n========== Menu Utama: ==============\n")
        print("1. Menu Admin")
        print("2. Menu Kasir")
        print("3. Keluar")

        pilihan = input("\nSilahkan pilih menu antara (1/2/3): ")

        if pilihan == "1":
            pengguna.menu_admin()

        elif pilihan == "2":
            pengguna.menu_kasir()

        elif pilihan == "3":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak tersedia, silahkan pilih nomor menu dengan benar, Terimakasih !")
