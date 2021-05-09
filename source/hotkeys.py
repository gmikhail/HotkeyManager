from pynput.keyboard import Key, Listener, Controller, KeyCode
from subprocess import Popen
from os import path
from tray import get_state as state

FN = Key.cmd_r# Functional key
isFN = False
keyboard = Controller()

def on_press(key):
    #print('on_press {}'.format(key))
    global FN, isFN, keyboard
    if key == FN: isFN = True
    if isFN and state():
        # Media
        if key == Key.f5: 
            try: Popen(path.expandvars(r'%AppData%\Spotify\Spotify.exe')) 
            except: print('App not found')
        elif key == Key.f6: press_key(key.media_previous)
        elif key == Key.f7: press_key(key.media_play_pause)
        elif key == Key.f8: press_key(key.media_next)
        # Volume
        elif key == Key.f9: press_key(key.media_volume_mute)
        elif key == Key.f10: press_key(key.media_volume_down)
        elif key == Key.f11: press_key(key.media_volume_up)
        # Other
        elif key == Key.f12: Popen(('calc'))
        #elif key == Key.f12: press_key(KeyCode.from_vk(0xA9))
        # https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

def on_release(key):
    #print('on_release {}'.format(key))
    global FN, isFN
    if key == FN: isFN = False

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)
    print('Key press: {}'.format(key))

def start_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    start_listener()

# https://pynput.readthedocs.io/en/latest/keyboard.html