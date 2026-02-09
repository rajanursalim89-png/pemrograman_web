from core.constants import NILAI

def nilai_dengan_status(kkm=60):
    hasil = []
    for item in NILAI:
        data = item.copy()
        if item["nilai"] >= kkm:
            data["status"] = "Lulus"
        else:
            data["status"] = "Tidak Lulus"
        hasil.append(data)
    return hasil


def rata_rata():
    total = sum(item["nilai"] for item in NILAI)
    return total / len(NILAI)


def nilai_min_max():
    nilai_list = [item["nilai"] for item in NILAI]
    return min(nilai_list), max(nilai_list)