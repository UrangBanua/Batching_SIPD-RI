# ~~~~~~~~~~~~~~~~~~~~ MENU UTAMA ~~~~~~~~~~~~~~~~~~~~
def main_menu():
    print("\n~~~~~~~~~~~~~~~~~~~~ Menu Utama ~~~~~~~~~~~~~~~~~~~~")
    print("1. Proporsi Anggaran vs Realisasi")
    print("2. BUD - Review")
    print("3. Tatausaha - Validasi")
    print("4. Bendahara - Review")
    print("5. Akuntansi - Posting")
    print("6. Akuntansi - Laporan")
    print("9. Keluar")

    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        print("menu 1")
    elif choice == "2":
        print("menu 2")
    elif choice == "3":
        print("menu 3")
    elif choice == "4":
        print("menu 4")
    elif choice == "5":
        print("menu 5")
    elif choice == "6":
        print("menu 6")
    elif choice == "9":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        return
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

    return_to_menu()

# ~~~~~~~~~~~~~~~~~~~~ KEMBALI ke MENU UTAMA ~~~~~~~~~~~~~~~~~~~~ 
def return_to_menu():
    print("\n")
    choice = input("Ketik 'menu' untuk kembali ke menu utama atau 'keluar' untuk keluar: ")
    
    if choice.lower() == "menu":
        main_menu()
    elif choice.lower() == "keluar":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        exit()
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        return_to_menu()