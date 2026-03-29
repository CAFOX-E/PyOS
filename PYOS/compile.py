import sys
import subprocess
import os

print("\n\033[1;33m[1] Forcing the installation of PyInstaller in the root directory of this Python installation...\033[0m")
# This forces the exact Python installation that is currently running to install the library.
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

print("\n\033[1;36m[2] Starting the PyOS Compilation Matrix...\033[0m")
import PyInstaller.__main__

# Packaging Settings
parameters = [
    'os.py',
    '--onefile',
    # '--icon=icon.ico' <-- If you converted the icon, delete the hashtag (#) at the beginning of this line!
]

PyInstaller.__main__.run(parameters)

print("\n\033[1;32m[3] SUCCESSFUL COMPILATION!\033[0m")
print(f"Your .exe file is located inside the 'dist' folder in the directory: {os.getcwd()}")