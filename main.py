__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

'''
Assignment WincAcademy Files
Created by Wim Brouwer
Date created 24/05/2021
'''

import os
import shutil
import zipfile


main_path = os.path.dirname(os.path.realpath(__file__))
cache_path = os.path.join(main_path, 'cache')

def clean_cache():
    # this function will delete any files that are in
    # the dir "cache" and creates an empty chache dir
    os.chdir(main_path)
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)

    os.mkdir(cache_path)


def cache_zip(source, target):
    # extract the files
    with zipfile.ZipFile(source, 'r') as zipObj:
        zipObj.extractall(target)


def cached_files():
    # fuction will return a list of files in the cache dir
    os.chdir(cache_path)
    for root, dirs, files in os.walk('.'):
        file_list = [os.path.abspath(name) for name in files]

    return file_list


def find_password(file_list):
    # function will search for the word
    # "password" in the file list and
    # returns the word that follows on password: ....
    for file in file_list:
        with open(file) as f:
            content = f.read().lower().splitlines()
            for line in content:
                if 'password' in line:
                    password = line.split(': ')[1]
                    os.chdir(main_path)  #@ Thomas --> deze is wel degelijk noodzakelijk, anders werkt de laatste functie van wincpy check niet: https://winc-campus.slack.com/archives/C01SYQNPJD8/p1621938185196900
                    return password

    print('password not found')