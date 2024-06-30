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


# Contoh penggunaan
try:
    data_login = baca_config("login.config")
    print(f"Service: {data_login['service']}")
    print(f"Tahun: {data_login['tahun']}")
    print(f"Username: {data_login['username']}")
    print(f"Password: {data_login['password']}")
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {str(e)}")