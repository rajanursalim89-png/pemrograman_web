#utils.py

import os
from constants import antrian

def tambah_antrian(nama):
    antrian.append(nama)
    return True

def panggil_antrian():
    if len(antrian) == 0:
        return None
    return antrian.pop(0)

def lihat_antrian():
    return antrian

def cls():
    os.system("cls" if os.name == "nt" else "clear")
