from datetime import datetime

def format_waktu(waktu):
    if waktu:
        return waktu.strftime("%H:%M:%S")
    return "-"
