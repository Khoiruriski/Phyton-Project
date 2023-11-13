# Input User
# Setiap kali data yang dimasukan pasti bernilai string

print("===============Welcome to my project=======================")
dataString = input("Masukan Data: ")
print("Data berisi : " + dataString, " dengan type = ", type(dataString))
# Setiap data bernilai string
# jika ingin menjadikan int, maka haru di casting dengan format

# Variabel = tipeData(input("masukan angka : "))
dataInt = int(input("Masukan data int : "))
print("data = ", dataInt)

dataFloat = float(input("Masukan data float : "))
print("data = ", str(dataFloat) , "Bertipe : " , type(dataFloat))

dataBoolean = bool(input("masukan Nilai boolean : "))
print("data = " , dataBoolean,'bertipe : ', type(dataBoolean))



