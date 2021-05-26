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


def main():
    # here you can add commands for running standalone
    pass


def clean_cache():
    # this function will delete any files that are in
    # the dir "cache" and creates an empty chache dir
    os.chdir('C:\\python_progs\\WincAcademy\\files\\')
    if os.path.exists('C:\\python_progs\\WincAcademy\\files\\cache'):
        shutil.rmtree('C:\\python_progs\\WincAcademy\\files\\cache')

    os.mkdir('C:\\python_progs\\WincAcademy\\files\\cache')


def cache_zip(source, target):
    # extract the files
    with zipfile.ZipFile(source, 'r') as zipObj:
        zipObj.extractall(target)


def cached_files():
    # fuction will return a list of files in the cache dir
    os.chdir('C:\\python_progs\\WincAcademy\\files\\cache')
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
            f.close()
            for lines in content:
                if 'password' in lines:
                    password = lines.split(': ')[1]
                    os.chdir('C:\\python_progs\\WincAcademy\\files\\')
                    return password

    print('password not found')


if __name__ == '__main__':
    main()
