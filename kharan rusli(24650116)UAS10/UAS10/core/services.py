from core.constants import LAYANG_LAYANG

def hitung_layang_layang(d1, d2, a, b):
    luas = LAYANG_LAYANG["LUAS"](d1, d2)
    keliling = LAYANG_LAYANG["KELILING"](a, b)

    return {
        "luas": luas,
        "keliling": keliling
    }
