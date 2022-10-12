print("\nPROGRAM HITUNG TOTAL GAJI KARYAWAN")
print("MASUKKAN DATA DIBAWAH INI\n")
nama=input("NAMA KARYAWAN :")
goljab=input("GOLONGAN JABATAN [1/2/3] :")
pendidikan=input("PENDIDIKAN [SMA/D1/D3/S1] :")
gaji=300000
if goljab=="1":
    jabatan=gaji*0.05
    if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=gaji*0.025
    if pendidikan=="D1" or pendidikan=="d1":
        tunjangan=gaji*0.05
    if pendidikan=="D3" or pendidikan=="d3":
        tunjangan=gaji*0.20
    if pendidikan=="S1" or pendidikan=="s1":
        tunjangan=gaji*0.30
if goljab=="2":
    jabatan=gaji*0.05
    if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=gaji*0.025
    if pendidikan=="D1" or pendidikan=="d1":
        tunjangan=gaji*0.05
    if pendidikan=="D3" or pendidikan=="d3":
        tunjangan=gaji*0.20
    if pendidikan=="S1" or pendidikan=="s1":
        tunjangan=gaji*0.30
if goljab=="3":
    jabatan=gaji*0.05
    if pendidikan=="SMA" or pendidikan=="sma":
        tunjangan=gaji*0.025
    if pendidikan=="D1" or pendidikan=="d1":
        tunjangan=gaji*0.05
    if pendidikan=="D3" or pendidikan=="d3":
        tunjangan=gaji*0.20
    if pendidikan=="S1" or pendidikan=="s1":
        tunjangan=gaji*0.30

jam=int(input("JUMLAH JAM KERJA :"))
if jam>8:
    totaljam=(jam-8)*3500

total=gaji+totaljam+tunjangan+jabatan

print("\n-----------HASIL----------")
print("KARYAWAN YANG BERNAMA",nama)
print("HONOR YANG DITERIMA\n")
print("TUNJANGAN JABATAN RP.",jabatan)
print("TUNJANGAN PENDIDIKAN RP.",tunjangan)
print("HONOR LEMBUR RP.",totaljam)
print("\nTOTAL GAJI RP.",total)
print("--------------------------")