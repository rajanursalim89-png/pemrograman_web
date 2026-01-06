def konversi_nilai_ke_label(nilai_angka):
    if nilai_angka >= 85:
        return "A"
    elif nilai_angka >= 80:
        return "A-"
    elif nilai_angka >= 75:
        return "B+"
    elif nilai_angka >= 70:
        return "B"
    elif nilai_angka >= 65:
        return "B-"
    elif nilai_angka >= 60:
        return "C+"
    elif nilai_angka >= 55:
        return "C"
    elif nilai_angka >= 45:
        return "D"
    else:
        return "E"


def konversi_label_ke_bobot(label):
    data_bobot = {
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "D": 1.0,
        "E": 0.0
    }
    return data_bobot.get(label, 0)
