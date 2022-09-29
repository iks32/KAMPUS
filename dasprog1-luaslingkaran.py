print("menghitung luas & keliling lingkaran ")
print("--------------------------------------------------\n")
# \n adalah spasi kebawah
pi    = 22/7
# pi adalah rumus, rumus yg dipanggil itu 22/7
jari   = float(input("masukan nilai jari jari yang mau dihitung : "))
# float adalah tipe data buat suport input angka
luas   = pi*(jari*jari)
# ini rumus luas ^^^
keliling   = 2*pi*jari
# ini rumus keliling ^^^
print("\n-----------------HASIL-----------------")
print("Luas Lingkaran =","{:.3f}".format(luas)) 
print("Keliling Lingkaran =","{:.3f}".format(keliling))
# {:.3f} adalah pembatas 3 angka dibelakang koma yang muncul pada HASIL