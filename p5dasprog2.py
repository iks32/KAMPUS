nama=input("nama pembeli :")
bnyk=int(input("banyak pembelian :"))
for a in range(bnyk):
    print("\n\n------------pembelian ke : ",a+1,"------------")
    brg=(input("nama barang :"))
    list.append(brg)
    hrg=int(input("harga barang :"))
    list.append(hrg)
    jmlh=int(input("jumblah beli :"))
    list.append(jmlh)
 
    total=hrg*jmlhprint("\nrekap pembelian barang")
print("nama pembeli :",nama)
print("-------------------------------------------------------------")
print("no   nama_barang     harga_barang    jumlah_beli     subtotal")
print("-------------------------------------------------------------")
for a in range(bnyk):
    print((a+1),bnyk,brg,hrg,jmlh,total)
print("-------------------------------------------------------------")

