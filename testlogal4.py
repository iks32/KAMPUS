print("Masukkan banyak produk yang terjual")

banyak_produk = int(input())

print("Masukkan harga satuan produk")

harga_satuan = int(input())

omzet = banyak_produk * harga_satuan

if banyak_produk > 100

gaji = 5000000 + 0.2*omzet

else 
gaji = 5000000 + 0.1*omzet

print("Besar gaji adalah Rp "+str(gaji))