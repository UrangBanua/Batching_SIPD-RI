import os
import time
import json
import locale
import pickle
import getpass
import requests
import configparser
#import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from colorama import Fore, Style

# Set lokalisasi atau regional ke Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

# START FUNGSI
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
    print(Fore.GREEN + f"Pre-login response: {data_user[0]}" + Style.RESET_ALL + '\n')
    return data_user

# END FUNGSI

# print variable config
try:
    print("Reading login config")
    data_login = baca_config("login.config")
    print(f"Service: {data_login['service']}")
    print(f"Tahun: {data_login['tahun']}")
    print(f"Username: {data_login['username']}")
    # print password in dots
    print(f"Password: {'*' * len(data_login['password'])}")
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {str(e)}")

# START PROGRAM
print("Starting program")
pre_login(data_login['service'], data_login['username'], data_login['password'], data_login['tahun'])

# END PROGRAM

