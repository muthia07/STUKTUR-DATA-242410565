# variabel global untuk menyimpan data buku
buku = []

# Fungsi untuk menampilkan semua data buku
def show_data():
    if len(buku) <=0 :
        print("DATA BUKU BELUM ADA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))