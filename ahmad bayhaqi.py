import time
siswa = int(input("masukkan jumlah siswa : "))
i = (1)
hasil = int()
while i <= siswa : 
    rata = int(input("inputkan nilai : "))
    i += 1 
    hasil += rata
jumlah = (hasil/siswa)
time.sleep (0.5)
print ()

print ("jumlah nilai : ", hasil )
print ("rata rata nilai : ", jumlah)