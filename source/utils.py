import os, sys

def absolute_path(path):
    try: 
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError: 
        base_path = os.getcwd()
    return os.path.join(base_path, path)