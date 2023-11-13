
print("\n================================== Selamat Datang Di Menu Kasir Kami ! ===============================\n")
print("Silahkan pilih submenu yang tersedia pada Menu utama !")

import json
from abc import ABC, abstractmethod

# INTERFACE untuk Item
class InterfaceItem(ABC):
    @abstractmethod
    def get_info(self):
        pass

# ABSTRAK 
# Class abstrak untuk Item
class Barang(ABC):
    def __init__(self, nama, harga, stok, kategori):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

    @abstractmethod
    def get_info(self):
        pass
# INHERITANCE
# Class Produk adalah subclass dari Item
class Produk(Barang):
    def __init__(self, nama, harga, stok, kategori):
        super().__init__(nama, harga, stok, kategori)
    # POLIMORFISME
    # Overriding metode get_info dari kelas Barang
    def get_info(self):
        return f"{self.nama} - Harga: Rp.{self.harga:.3f} - Stok: {self.stok} - Kategori: {self.kategori}"

# Class Layanan adalah subclass dari Item
class Layanan(Barang):
    # Overriding metode get_info dari kelas Barang
    def get_info(self):
        return f"{self.nama} - Harga: Rp.{self.harga:.3f} - Persediaan: {self.stok} jam layanan"

# Class Kasir untuk mengelola pembelian dan item
class Kasir:
    def __init__(self):
        self.barang = []
        self.keranjang = []

        # Memanggil metode muat_dari_json saat objek Kasir dibuat
        self.muat_dari_json("barang.json")  # Ini akan memuat data barang dari file JSON saat program dimulai

    def tambah_barang_baru(self, barang):
        self.barang.append(barang)
        print(f"\nBarang baru {barang.nama} telah ditambahkan.")

    def tambah_item(self, barang, jumlah):
        item = [barang, jumlah]
        self.keranjang.append(item)
        print(f"\n{barang.nama} telah ditambahkan ke dalam keranjang belanja")

    def hapus_item(self, nama_barang):
        for barang in self.barang:
            if barang.nama == nama_barang:
                self.barang.remove(barang)
                print(f"\n{nama_barang} telah dihapus dari daftar belanja.")
                return
        print(f"{nama_barang} tidak ditemukan dalam daftar belanja.")

    def perbarui_stok(self, nama_barang, stok_baru):
        for barang in self.barang:
            if barang.nama == nama_barang:
                barang.stok = stok_baru
                print(f"\nStok {nama_barang} telah diperbarui menjadi {stok_baru}.")
                return
        print(f"\n{nama_barang} tidak ditemukan dalam daftar belanja.")

    def checkout(self):
        print("\n---------- Struk Pembelian ----------\n")
        total_harga = 0
        for barang, jumlah in self.keranjang:
            total_harga += barang.harga * jumlah
            print(f"{barang.nama} - Harga: Rp.{barang.harga * jumlah:.3f}")
        print(f"\nTotal Harga: Rp.{total_harga:.3f}")
        print("\nTerima kasih telah berbelanja ! Semoga Harimu Menyenangkan !")
        print("\n---------------------------------------")
        self.keranjang = []

    def simpan_ke_json(self, nama_file):
        data_barang = []
        for barang in self.barang:
            data_barang.append({
                "nama": barang.nama,
                "harga": barang.harga,
                "stok": barang.stok,
                "kategori": barang.kategori
            })

        with open(nama_file, "w") as file:
            json.dump(data_barang, file, indent=4)

    def tampilkan_keranjang(self):
        if not self.keranjang:
            print("Keranjang belanja anda kosong")
        else:
            print("Keranjang Belanja anda berisi :\n")
            for barang, jumlah in self.keranjang:
                print(f"{barang.nama} - Jumlah: {jumlah} - Harga: Rp.{barang.harga * jumlah:.3f}")

    def hitung_total_harga(self):
        total_harga = 0
        for barang, jumlah in self.keranjang:
            total_harga += barang.harga * jumlah
        return total_harga

    def muat_dari_json(self, nama_file):
        try:
            with open(nama_file, "r") as file:
                data = json.load(file)
                self.barang = []

                # Memproses data dari file JSON dan menambahkannya ke daftar barang
                for data_barang in data:
                    if data_barang["kategori"] == "Layanan":
                        barang = Layanan(data_barang["nama"], data_barang["harga"], data_barang["stok"], data_barang["kategori"])
                    else:
                        barang = Produk(data_barang["nama"], data_barang["harga"], data_barang["stok"], data_barang["kategori"])
                    self.barang.append(barang)

                print("Data telah dimuat dari file JSON.")
        except FileNotFoundError:
            print("File JSON tidak ditemukan.")

    def tampilkan_daftar_produk(self):
        print("\n========== Daftar Produk: ===========\n")
        for produk in self.barang:
            print(produk.get_info())
        print("\n")

# Kelas Pengguna (Admin/Kasir)
class Pengguna:
    def __init__(self, kasir):
        self.kasir = kasir

    def menu_admin(self):
        while True:
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

    def menu_kasir(self):
        while True:
            print("\n=============== Menu Kasir ===============:\n")
            print("1. Tambahkan Barang Ke Keranjang")
            print("2. Lihat Keranjang")
            print("3. Checkout")
            print("4. Keluar dari menu kasir")

            pilihan = input("\nSilahkan pilih menu antara (1/2/3/4): ")

            if pilihan == "1":
                self.kasir.tampilkan_daftar_produk()
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

            elif pilihan == "4":
                print("\nAnda telah Keluar dari menu Kasir.")
                break

            else:
                print("\nPilihan tidak tersedia, silahkan pilih nomer menu dengan benar, Terimakasih !")

# Program Utama
if __name__ == "__main__":
    kasir = Kasir()
    pengguna = Pengguna(kasir)

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
