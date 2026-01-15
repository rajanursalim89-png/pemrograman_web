from datetime import datetime

TARIF = {
    "motor": 100,
    "mobil": 300
}

class Parkir:
    def __init__(self):
        self.data = []
        self.pendapatan_motor = 0
        self.pendapatan_mobil = 0

    def analisis(self):
        hasil = {
            "harian":   {"motor": 0, "mobil": 0, "pend_motor": 0, "pend_mobil": 0},
            "mingguan": {"motor": 0, "mobil": 0, "pend_motor": 0, "pend_mobil": 0},
            "bulanan":  {"motor": 0, "mobil": 0, "pend_motor": 0, "pend_mobil": 0},
            "tahunan":  {"motor": 0, "mobil": 0, "pend_motor": 0, "pend_mobil": 0},
        }

        now = datetime.now()
        minggu_ini = now.isocalendar().week

        for log in self.data:
            if log["keluar"] is None:
                continue

            jenis = log["jenis"]
            biaya = log["biaya"]
            keluar = log["keluar"]

            if keluar.date() == now.date():
                hasil["harian"][jenis] += 1
                hasil["harian"][f"pend_{jenis}"] += biaya

            if keluar.isocalendar().week == minggu_ini:
                hasil["mingguan"][jenis] += 1
                hasil["mingguan"][f"pend_{jenis}"] += biaya

            if keluar.month == now.month and keluar.year == now.year:
                hasil["bulanan"][jenis] += 1
                hasil["bulanan"][f"pend_{jenis}"] += biaya

            if keluar.year == now.year:
                hasil["tahunan"][jenis] += 1
                hasil["tahunan"][f"pend_{jenis}"] += biaya

        return hasil

    def masuk(self, plat, jenis, merek):
        data = {
            "plat": plat.strip().upper(),
            "jenis": jenis.lower(),
            "merek": merek,
            "masuk": datetime.now(),
            "keluar": None,
            "menit": 0,
            "biaya": 0
        }
        self.data.append(data)
        return data

    def keluar(self, plat):
        plat = plat.strip().upper()

        for k in self.data:
            if k["plat"] == plat and k["keluar"] is None:
                k["keluar"] = datetime.now()
                k["menit"] = max(
                    1,
                    int((k["keluar"] - k["masuk"]).total_seconds() // 60)
                )
                k["biaya"] = k["menit"] * TARIF[k["jenis"]]

                if k["jenis"] == "motor":
                    self.pendapatan_motor += k["biaya"]
                else:
                    self.pendapatan_mobil += k["biaya"]

                return k
        return None

    def aktif(self):
        return [k for k in self.data if k["keluar"] is None]
