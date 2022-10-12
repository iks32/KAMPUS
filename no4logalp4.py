### TUGAS PERTEMUAN 4 IKBAL FADILLAH NIM:17221114 ###
### PROGRAM SOAL NOMOR 4 ###
print("\n--------------------------------------------------")
print("Menghitung Gaji Salesmen\n")
produk = int(input("Masukkan Banyak Produk Terjual = "))
harga = int(input("Masukkan harga = "))
omset = produk * harga
gaji1 = 5000000 + 0.2*omset
gaji2 = 5000000 + 0.1*omset
print("\n-----------------HASIL-----------------")
print("Total gaji jika penjualan diBAWAH 100 adalah = Rp.","{:,.2f}".format(gaji2))
print("Total gaji jika penjualan diATAS 100 adalah = Rp.","{:,.2f}",gaji1)
print("\n--------------------------------------------------")