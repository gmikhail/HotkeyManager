from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item
from os import _exit
from utils import absolute_path

def menu_exit():
    icon_tray.visible = False
    icon_tray.stop()
    _exit(0)

state = True

def get_state():
    return state

def on_clicked(icon, item):
    global state
    state = not item.checked
    icon_tray.icon = Image.open(absolute_path(r'resources\icon.png')) if state else Image.open(absolute_path(r'resources\icon-off.png'))

def run_icon_tray():
    global icon_tray
    icon_tray = icon(
            name = 'name', 
            icon = Image.open(absolute_path(r'resources\icon.png')), 
            title = 'Hotkey Manager', 
            menu = menu( 
                item('Active', on_clicked, default=True, checked=lambda item: state), 
                item('Exit', menu_exit) 
            )
        )
    icon_tray.run()

if __name__ == '__main__':
    run_icon_tray()