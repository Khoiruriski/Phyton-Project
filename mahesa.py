class KipasAngin:
     def _init_(self, jumlah_bilah, ukuran, kecepatan):
          self.jumlah_bilah = jumlah_bilah
          self.ukuran = ukuran
          self.kecepatan = kecepatan

     def hidupkan(self):
         print(f'hidupkan KipasAngin dengan memiliki {self.jumlah_bilah}, ukuran {self.ukuran}, dengan kecepatan {self.kecepatan}')

     def matikan(self):
         print(f'matikan KipasAngin dengan memiliki {self.jumlah_bilah}, ukuran {self.ukuran}, dengan kecepatan {self.kecepatan}')
kipas1 = KipasAngin("3 bilah" , "besar", "tinggi")

kipas1.hidupkan()
kipas1.matikan()
