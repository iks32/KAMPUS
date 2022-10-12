print("MENGHITUNG GAJI KARYAWAN")
print("------------------------\n")
nama = input("MASUKKAN NAMA KARYAWAN : ")
goljab = input("MASUKKAN GOLONGAN KARYAWAN (1/2/3) :")
pendidikan= input("JENIS PENDIDIKAN (SMA/D1/D3/S1) :")
gaji=300000
if goljab=="1":
    jabatan=gaji*0.05
    if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=gaji*0.025
    elif pendidikan=="D1" or pendidikan=="d1":
        tunjangan=gaji*0.05
    elif pendidikan=="D3" or pendidikan=="d3":
        tunjangan=gaji*0.20
    elif pendidikan=="S1" or pendidikan=="s1":
        tunjangan=gaji*0.30
if goljab=="2":
    jabatan=gaji*0.10
    if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=gaji*0.025
    elif pendidikan=="D1" or pendidikan=="d1":
        tunjangan=gaji*0.05
    elif pendidikan=="D3" or pendidikan=="d3":
        tunjangan=gaji*0.20
    elif pendidikan=="S1" or pendidikan=="s1":
        tunjangan=gaji*0.30
elif goljab=="3":
    jabatan=gaji*0.15
    if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=gaji*0.025
    elif pendidikan=="D1" or pendidikan=="d1":
        tunjangan=gaji*0.05
    elif pendidikan=="D3" or pendidikan=="d3":
        tunjangan=gaji*0.20
    elif pendidikan=="S1" or pendidikan=="s1":
        tunjangan=gaji*0.30
else:
    jabatan=0
    tunjangan=0
    print("JABATAN TERSEBUT ATAU PENDIDIKAN TERSEBUT TIDAK VALID")

jam=int(input("MASUKKAN JUMLAH JAM KERJA :"))
if jam>=8:
    totaljam=(jam-8)*3500
else:
    totaljam=0
hitung=gaji+jabatan+tunjangan+totaljam
print("--------------------")
print("TOTAL GAJI =",hitung)