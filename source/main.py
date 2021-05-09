from hotkeys import start_listener
from tray import run_icon_tray
from threading import Thread

if __name__ == "__main__":
    Thread(target=start_listener).start()
    Thread(target=run_icon_tray).start()