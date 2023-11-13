print("\n ================== Welcome to Ragnarok Of Adam ====================")
class Hero(object) :
    print("\n                      Game !!!! Start !!!                       ")
    def __init__(self, inputNama, inputDarah, inputLevel, inputSkill, inputSenjata, inputDamage, InputArmor):

        self.nama    = inputNama
        self.darah   = inputDarah
        self.level   = inputLevel
        self.skill   = inputSkill
        self.senjata = inputSenjata
        self.damage  = inputDamage
        self.vest    = InputArmor

    def menyerang(self, lawan):
        print("\n" + self.nama, "Menyerang", lawan.nama, "dengan", self.senjata + ",", lawan.nama, "langsung terkena", self.damage, "damage")
        lawan.diserang(self)

    def diserang(self, lawan):
        damageSerangan = lawan.damage
        self.darah    -= damageSerangan
        print(self.nama, "diserang", lawan.nama, "dan mendapat", lawan.damage, "damage ( Darah", self.nama, "tersisa", self.darah, ")")

Nesya = Hero("Nesya", 1000, "Max", 3, "Menyantetnya", 999, 350)
Iblis = Hero("Iblis", 1000, "Max", 2, "Menyesatkanya", 1, 350)

while True:

    Nesya.menyerang(Iblis)
    Iblis.menyerang(Nesya)

    if Nesya.darah <= 0:
        print("\n=================== Nesya Mati  ===================")
        break
    elif Iblis.darah <= 0:
        print("\n=================== Iblis Mati Dengan Sekali Serang ===================")
        break