import os
import time
import configparser
import json
import requests
import locale
from colorama import Fore, Style
from tqdm import tqdm

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')  # Set Indonesian locale (change if needed)

# Fungsi untuk baca file login.config dengan isi variabel tahun, username & password
def baca_config(file_config):
    config = configparser.ConfigParser()
    if os.path.isfile(file_config):
        config.read(file_config)
        if config.has_section("Login"):
            service = config.get("Login", "service")
            tahun = config.get("Login", "tahun")
            username = config.get("Login", "username")
            password = config.get("Login", "password")
            return {"service": service, "tahun": tahun, "username": username, "password": password}
        else:
            raise ValueError("Section 'Login' not found in config file.")
    else:
        raise FileNotFoundError("Config file not found.")

# Fungsi pre-login ke SIPD-RI untuk mendapatkan data json berupa id_user, id_pegawai, id_user, id_daerah, id_skpd, kode_skpd, nama_skpd, id_role, nama_role
def pre_login(service, username, password, tahun):
    url = service + '/auth/auth/pre-login'
    payload = {'username': username, 'password': password, 'tahun': tahun}
    response = requests.post(url, data=payload)
    data_user = json.loads(response.text)
    data_user[0]['token'] = '****************'
    
    # Menambahkan loading text
    for _ in tqdm(range(100), desc="Loading pre-login", ascii=True, unit_scale=True, ncols=70, bar_format='{desc}: |{bar}| {percentage:3.0f}%'):
        time.sleep(0.01)
    
    print(Fore.GREEN + f"Proses login pengambilan token" + Style.RESET_ALL)
    #print(Fore.GREEN + f"Pre-login response: {json.dumps(data_user[0], indent=4)}" + Style.RESET_ALL + '\n')
    
    return data_user

# Fungsi login ke SIPD-RI untuk mendapatkan barier token dengan paremeter berupa id_daerah, id_role, id_skpd, id_pegawai, password, tahun
def login(service, id_daerah, id_role, id_skpd, id_pegawai, password, tahun, username):
    url = service + '/auth/auth/login'
    payload = {'id_daerah': id_daerah, 'id_role': id_role, 'id_skpd': id_skpd, 'id_pegawai': id_pegawai, 'password': password, 'tahun': tahun, 'username': username}
    response = requests.post(url, data=payload)
    data_token = json.loads(response.text)
    
    # Menambahkan loading text
    for _ in tqdm(range(100), desc="Loading login", ascii=True, unit_scale=True, ncols=70, bar_format='{desc}: |{bar}| {percentage:3.0f}%'):
        time.sleep(0.01)
    
    print(Fore.GREEN + f"Login berhasil" + Style.RESET_ALL)
    print(Fore.CYAN + f"Barear token: {json.dumps(data_token['refresh_token'], indent=4)}" + Style.RESET_ALL + '\n')
    
    return data_token

# Fungsi baca data json berupa capaian serapan realisasi SKPD dari SIPD-RI menggunakan rest api dengan header token
def capaian_serapan_realisasi(service, token):
    url = service + '/pengeluaran/strict/dashboard/statistik-belanja'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    data_serapan = json.loads(response.text)
    filter_data_serapan = [skpd for skpd in data_serapan if skpd["id_skpd"] == 65]
 
    # print data serapan
    print(Fore.GREEN + f"Serapan Realisasi ")
    print(f"SKPD : {filter_data_serapan[0]['kode_skpd'] + ' - ' + filter_data_serapan[0]['nama_skpd']}")
    print(f"Anggaran  : {locale.currency(filter_data_serapan[0]['anggaran'], grouping=True)}")
    
    anggaran = filter_data_serapan[0]['anggaran']
    realisasi_rencana = filter_data_serapan[0]['realisasi_rencana']
    realisasi_rill = filter_data_serapan[0]['realisasi_rill']
    pengajuan_percentage = (realisasi_rencana / anggaran) * 100 if anggaran != 0 else 0
    pengajuan_percentage_str = f"{pengajuan_percentage:.2f}"
    pencairan_percentage = (realisasi_rill / anggaran) * 100 if anggaran != 0 else 0
    pencairan_percentage_str = f"{pencairan_percentage:.2f}"

    print(f"Pengajuan : {locale.currency(realisasi_rencana, grouping=True)} ({pengajuan_percentage_str}%)")
    print(f"Pencairan : {locale.currency(realisasi_rill, grouping=True)} ({pencairan_percentage_str}%)" + Style.RESET_ALL + '\n')

    return data_serapan
