import os
import time
from plyer import notification

def clear():
    # Cek OS dan clear terminal
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS/Linux
        os.system('clear')

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Helper Mahasiswa", 
        timeout=5  # Durasi notifikasi
    )

def validate_isalpha(prompt):
    while True:
        string = input(prompt).strip()
        if not string:
            print("Input tidak boleh kosong! Coba lagi.")
            time.sleep(1)
            clear()
        elif all(char.isalpha() or char.isspace() for char in string):       
            return string
        else:
            print("Input tidak valid! Silakan coba lagi.")
            time.sleep(1)
            clear()

def validate_isalnum(prompt):
    while True:
        string = input(prompt).strip()
        if not string:
            print("Input tidak boleh kosong! Coba lagi.")
            time.sleep(1)
            clear()
        elif all(char.isalnum() or char.isspace() for char in string):       
            return string
        else:
            print("Input tidak valid! Silakan coba lagi.")
            time.sleep(1)
            clear()