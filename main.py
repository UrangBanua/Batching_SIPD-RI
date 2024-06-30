import time
import json
import locale
import pickle
import getpass
#import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from colorama import Fore, Style
from rest_call import baca_config, pre_login, login
from main_menu import main_menu

# Set lokalisasi atau regional ke Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

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

# Menambahkan loading text
print(Fore.GREEN + f"Proses Pre-login ..." + Style.RESET_ALL)

# try to set data_user jika berhasil maka langsung set data_token dan call main menu
try:
    # set variable data_user
    data_user = pre_login(data_login['service'], data_login['username'], data_login['password'], data_login['tahun'])
    # tambahkan data token
    #data_user['token'] = 'ok'
    # login untuk mendapatkan nilai token
    data_token = login(data_login['service'], data_user[0]['id_daerah'], data_user[0]['id_role'], data_user[0]['id_skpd'], 
                       data_user[0]['id_pegawai'], data_login['password'], int(data_login['tahun']), data_login['username'])

    # tambahkan data token pada data_user
    data_user[0]['token'] = data_token['refresh_token']
    print(Fore.GREEN + f"Sebagai: {json.dumps(data_user[0]['nama_role'], indent=4)}" + Style.RESET_ALL + '\n')
    # call main menu
    #main_menu()
except Exception as e:
    print(f"Error: {str(e)}")
