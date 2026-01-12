#main.py

from utils import *


while True:

    cls()

    print("1. Tambah Antrian")
    print("2. Panggil Antrian")
    print("3. Lihat Antrian")
    print("4. Keluar")

    pilihan = input("Pilihan : ")
  
    if pilihan == "1":
        nama = input("Nama: ")
        tambah_antrian(nama)
        print("Antrian berhasil ditambahkan")

        input("")

    elif pilihan == "2":
        hasil = panggil_antrian()
        if hasil is None:
            print("Tidak ada antrian")
        else:
            print("memanggil", hasil)

        input("")

    elif pilihan == "3":
        data = lihat_antrian()
        if len(data) == 0:
            print("Tidak ada antrian")
        else:
            print("Daftar Antrian:")
            for i, a in enumerate(data, start=1):
                print(f"{i}. {a}")

        input("")

    elif pilihan == "4":
        break

    else:
        print("Pilihan tidak valid")
