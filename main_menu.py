from typing import Dict, List, Optional
from rest_call import capaian_serapan_realisasi

def main_menu(data_login: Dict[str, str], data_user: List[Dict[str, str]]) -> None:
    """
    Display the main menu and handle user input.

    Args:
        data_login (Dict[str, str]): The login data.
        data_user (List[Dict[str, str]]): The user data.

    Returns:
        None
    """
    print("\n~~~~~~~~~~~~~~~~~~~~ Menu Utama ~~~~~~~~~~~~~~~~~~~~")
    print("1. Capaian Serapan Realisasi SKPD")
    print("3. Register - STBP Pendapatan")
    print("2. Register - SP2D Belanja")
    print("4. LPJ Fungsional")
    print("5. Akuntansi - Posting")
    print("6. Akuntansi - Laporan")
    print("9. Keluar")

    choice = input("Masukkan pilihan Anda: ")

    if choice == "1":
        capaian_serapan_realisasi(data_login['service'], data_user[0]['token'])
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

    return_to_menu(data_login, data_user)

def return_to_menu(data_login: Optional[Dict[str, str]] = None, data_user: Optional[List[Dict[str, str]]] = None) -> None:
    """
    Handle user input to return to the main menu or exit the program.

    Args:
        data_login (Optional[Dict[str, str]]): The login data. Defaults to None.
        data_user (Optional[List[Dict[str, str]]]): The user data. Defaults to None.

    Returns:
        None
    """
    print("\n")
    choice = input("Ketik 'menu' untuk kembali ke menu utama atau 'keluar' untuk keluar: ")
    
    if choice.lower() == "menu":
        main_menu(data_login, data_user)
    elif choice.lower() == "keluar":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        exit()
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        return_to_menu(data_login, data_user)
