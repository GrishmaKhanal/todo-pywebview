## ToDo App in Qt + Webview
 - to check how well does it work

### Installation
    python 3.13
    pip install -r requirements.txt

### In wayland
    pacman -S qt5-wayland 

pyinstaller --onefile --add-data "src/frontend:frontend" src/main.py
