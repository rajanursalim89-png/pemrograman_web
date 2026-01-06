import os  # Tambahkan ini di paling atas
from utils import konversi_nilai_ke_label, konversi_label_ke_bobot

def clear_screen():
    # Menghapus layar terminal (cls untuk Windows, clear untuk Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("\n--------- MENU UTAMA ---------")
    print("1. Konversi Nilai ke Label")
    print("2. Konversi Label ke Bobot")
    print("3. Hitung Total SKS yang Diambil")
    print("4. Hitung Total Nilai")
    print("5. Hitung IPS")
    print("6. Exit")

def jalankan_menu():
    while True:
        clear_screen() # Layar akan bersih setiap kembali ke menu
        tampilkan_menu()
        pilihan = input("\nPilihan: ")

        if pilihan == "1":
            try:
                nilai = int(input("Nilai Mahasiswa: "))
                label = konversi_nilai_ke_label(nilai)
                print("Label:", label)
            except ValueError:
                print("Error: Masukkan angka untuk nilai!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2":
            label = input("Masukkan label nilai: ").upper()
            bobot = konversi_label_ke_bobot(label)
            print("Bobot:", bobot)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "5":
            try:
                jumlah = int(input("Jumlah mata kuliah: "))
                total_bobot = 0
                total_sks = 0
                for i in range(jumlah):
                    print(f"\n--- Data ke-{i+1} ---")
                    sks = int(input(f"SKS (Angka): ")) 
                    label = input(f"Label (Huruf A/B/C): ").upper()
                    bobot = konversi_label_ke_bobot(label)
                    
                    if bobot is not None:
                        total_bobot += bobot * sks
                        total_sks += sks
                    else:
                        print(f"Label '{label}' tidak valid!")

                ips = total_bobot / total_sks if total_sks != 0 else 0
                print(f"\nTOTAL SKS: {total_sks}")
                print(f"HASIL IPS: {round(ips, 2)}")
            except ValueError:
                print("Error: SKS harus diisi angka!")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "6":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")