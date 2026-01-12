# controller.py
import cli
from utils import *

def jalankan():
    while True:
        cli.menu()
        pilihan = cli.input_pilihan()

        if pilihan == "1":
            plat, jenis, merk = cli.input_kendaraan()
            hasil = kendaraan_masuk(plat, jenis, merk)

            if hasil:
                cli.tampil_sukses_masuk()
            else:
                cli.tampil_plat_sudah_ada(plat)

            cli.pause()

        elif pilihan == "2":
            data_parkir = get_parkir()

            if len(data_parkir) == 0:
                cli.tampil_parkiran_kosong()
            else:
                plat = cli.input_plat_keluar()
                data = kendaraan_keluar(plat)

                if data is False:
                    cli.tampil_kendaraan_tidak_ditemukan()
                else:
                    cli.tampil_kendaraan_keluar(data)

            cli.pause()

        elif pilihan == "3":
            data = get_parkir()
            cli.tampil_parkir(data)
            cli.pause()

        elif pilihan == "4":
            break
