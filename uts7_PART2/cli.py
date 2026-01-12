# cli.py
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    cls()
    print("1. Kendaraan Masuk")
    print("2. Kendaraan Keluar")
    print("3. Lihat Parkir")
    print("4. Keluar")

def input_pilihan():
    return input("Pilihan : ")

def input_kendaraan():
    plat = input("Plat : ")
    jenis = input("Jenis : ")
    merk = input("Merk : ")
    return plat, jenis, merk

def tampil_sukses_masuk():
    print("berhasil menambahkan kendaraan")


def tampil_plat_sudah_ada(plat):
    print(f'Kendaraan dengan plat "{plat}" sudah ada dalam parkiran')


def input_plat_keluar():
    return input("Plat Kendaraan : ")


def tampil_kendaraan_keluar(data):
        print(f"{data['plat']} {data['jenis']} {data['merk']}")


def tampil_parkiran_kosong():
    print("Parkiran Kosong")


def tampil_kendaraan_tidak_ditemukan():
    print("Kendaraan tidak ditemukan")


def tampil_parkir(data):
    if len(data) == 0:
        print("Parkiran kosong")
    else:
        print("Daftar Parkir:")
        for i, d in enumerate(data, start=1):
            print(f"{i}. {d['plat']}")

def pause():
    input()
