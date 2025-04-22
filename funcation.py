# membuat funcation sederhana
def sapa():
    print("halo,selamat datang!")

sapa()  # memanggil fungsi 1
sapa()  # memanggil fungsi 2
sapa()  # memanggil fungsi 3

# funcation dengan parameter
# funcation dengan 1 parameter
# funcation dengan 1 parameter
def sapa_nama(nama):
    print(f"halo, {nama}!")

# pemanggil funcation
sapa_nama("adam")

       # function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)

# Pemanggilan Function
luas_segitiga(4, 6)


# funcation dengan return(nilai kembali)
def tambah(a, b):
    return a + b

 # pemanggilan fungsi
hasil =tambah(3, 5)
print("hasil:", hasil)

# fungsi yang di gunakan di dalam fungsi lainnya
# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print (f"volume persegi = {vol_persegi}")

      
def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')

    # pemanggilan function, dengan 1 argumen
student("Wallberg") # hanya firsname

# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

def kali(a: int, b: int) -> int:
    return a * b


# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))

# *args untuk argumen bervariasi
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Selamat Datang', 'Di', 'PTI UNDIKMA')

def info_mahasiswa(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

# Pemanggilan function
info_mahasiswa(nama="Rina", jurusan="TI", angkatan=2022)