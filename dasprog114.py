print("PROGRAM HITUNG GAJI KARYAWAN")
print("-----------------------------------\n")
nama=input("MASUKKAN NAMA     =")
golongan=input("GOLONGAN JABATAN [1/2/3] =")
pendidikan=input("PENDIDIKAN [SMA/D1/D3] =")
if golongan=="1":
   jabatan=300000*0.05
   if pendidikan=="SMA" or pendidikan=="sma":
      tunjangan=300000*0.25
   elif pendidikan=="D1" or pendidikan=="d1":
        tunjangan=300000*0.05
   elif pendidikan=="D3" or pendidikan=="d3":
        tunjangan=300000*0.20
   else:
        tunjangan=300000*0.30
elif golongan=="2":
     jabatan=300000*0.05
     if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=300000*0.25
     elif pendidikan=="D1" or pendidikan=="d1":
          tunjangan=300000*0.05
     elif pendidikan=="D3" or pendidikan=="d3":
          tunjangan=300000*0.20
     else:
          tunjangan=300000*0.30
else:
    tunjangan=300000*0.15
    if pendidikan=="SMA" or pendidikan=="sma":
       tunjangan=300000*0.25
    elif pendidikan=="D1" or pendidikan=="d1":
         tunjangan=300000*0.05
    elif pendidikan=="D3" or pendidikan=="d3":
         tunjangan=300000*0.20
    else:
         tunjangan=300000*0.30
jam=int(input("JUMLAH JAM KERJA     ="))
if jam>=8:
    total=(jam-8)*3500
else:
    total=0
a=300000+jabatan+tunjangan+total
print("---------------------------------------\n")
print("KARYAWAN YANG BERNAMA     =",nama)
print("HONOR YANG DITERIMA")
print("     TUNJANGAN JABATAN      Rp.",jabatan)
print("     TUNJANGAN PENDIDIKAN   Rp.",tunjangan)
print("     HONOR LEMBUR           Rp.",total)
print("----------------------------------------+")
print("TOTAL GAJI                  Rp.%.0f"%a)