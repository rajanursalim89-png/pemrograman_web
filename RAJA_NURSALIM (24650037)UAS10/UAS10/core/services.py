from core.constants import biodata, hobi

def isi_biodata(nama, tempat_lahir, tanggal_lahir, jenis_kelamin, daftar_hobi):
    biodata["nama"] = nama
    biodata["tempat_lahir"] = tempat_lahir
    biodata["tanggal_lahir"] = tanggal_lahir
    biodata["jenis_kelamin"] = jenis_kelamin

    hobi.clear()
    hobi.extend(daftar_hobi)
    biodata["hobi"] = hobi

    return biodata
