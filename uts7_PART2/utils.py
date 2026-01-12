# utils.py
parkir = []

def kendaraan_masuk(plat, jenis, merk):
    # cek plat sudah ada atau belum
    for k in parkir:
        if k["plat"] == plat:
            return False  # plat sudah ada

    parkir.append({
        "plat": plat,
        "jenis": jenis,
        "merk": merk
    })

    return True  

def kendaraan_keluar(plat):
    if len(parkir) == 0:
        return None 

    for i, k in enumerate(parkir):
        if k["plat"] == plat:
            return parkir.pop(i)
    return False

def get_parkir():
    return parkir
