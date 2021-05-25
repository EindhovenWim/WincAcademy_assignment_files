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
    print('start')
    clean_cache()
    cache_zip('C:\\python_progs\\WincAcademy\\files\\data.zip','C:\\python_progs\\WincAcademy\\files\\cache')
    list_of_files = cached_files()
    print(find_password(list_of_files))

def clean_cache():
    print('cleaning cache')
    print(os.getcwd())
    if os.getcwd() == 'cache':
        print('wrong dir, you are in cache!')       # just a check if program is stuck in cache dir
    
    if os.path.exists('cache'):                     # check if chache dir exists, if so, delete it
        print('dir exists')
        shutil.rmtree('cache')    
    
    os.mkdir('cache')                               # create a new cache directory

def cache_zip(source, target):
    print('unzip files')
    clean_cache()                                   # clear cache folder just to make sure it will be empty
    with zipfile.ZipFile(source,'r') as zipObj:     # extract the files
        zipObj.extractall(target)

def cached_files():
    print('listing files')
    os.chdir('C:\\python_progs\\WincAcademy\\files\\cache') #to make sure that we are listing the correct folder
    file_list = []
    for root, dirs, files in os.walk('.'):
        #file_list = [os.path.abspath(name) for name in files] #list comprehension eruit gehaald, wellicht dat dit roet in het eten gooit bij wincpy check?
        for name in files:
            file_list.append(os.path.abspath(name))
    print(file_list[0:2])
    return file_list

def find_password(file_list):
    print('finding password')
    print('where are we looking for password?',os.getcwd())
    for file in file_list:
        with open(file) as f:
            content = f.read().lower().splitlines()
            for lines in content:
                if 'password' in lines:
                    print(lines)
                    password = lines.split(': ')[1]
                    return password

    print('password not found')

if __name__ == '__main__':
    main()
