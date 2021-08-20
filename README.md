# Hotkey Manager

Utility that provides additional functionality for keyboard without the FN function key.

## Hotkeys

**Note:** FN by default is the Right Windows key.

Hotkey | Action
--- | ---
FN + F5 | Launch Spotify (if possible)
FN + F6 | Previous Track
FN + F7 | Play/Pause
FN + F8 | Next Track
FN + F9 | Mute/Unmute
FN + F10 | Volume Down
FN + F11 | Volume Up
FN + F12 | Launch Calculator

## For Users

Download the latest executable from [Github Releases](https://github.com/gmikhail/HotkeyManager/releases) page.

## For Developers

Install packages required for building: 

`pip install pyinstaller pyinstaller-versionfile pynput pystray`

*Optional:* Update version in file `metadata/version.txt`

*Optional:* Generate version metadata file:

`create-version-file metadata/metadata.yml --outfile metadata/version_metadata.txt`

Build the executable:

`pyinstaller source/main.py --onefile --windowed --hidden-import pystray._win32 --hidden-import pynput.keyboard._win32 --hidden-import pynput.mouse._win32 --add-data 'resources;resources'--icon 'resources/icon.ico' --name HotkeyManager --version-file metadata/version_metadata.txt`

If you have any requests or fixes, feel free to change the source code.