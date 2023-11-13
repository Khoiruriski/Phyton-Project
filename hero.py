class Hero :
    
    def __init__(self,name,health,Attack,Armor) :
        self.name = name
        self.health = health
        self.Attack = Attack
        self.Armor = Armor

    def serang (self,lawan):
        print(self.name + ' Menyerang ' + lawan.name) 
        lawan.diserang(self, self.Attack)

    def diserang(self,lawan,AttackLawan):
        print(self.name + ' Diserang ' + lawan.name)
        AttackDiterima = AttackLawan/self.Armor
        print('Serangan Terasa '  + str(AttackDiterima))
        self.health -= AttackDiterima
        print('Darah '+ self.name + ' tersisa '+ str(self.health))

Adam = Hero ('Adam',999,800,1)
Iblis= Hero ('Iblis',898,100,1)
naga= Hero ('naga',898,100,1)
jeki= Hero ('jeki',898,100,1)
print("Tes")
Adam.serang(Iblis)
print("\n")
Iblis.serang(Adam)
print("\n")
jeki.serang(naga)


print("Game Selesai")

