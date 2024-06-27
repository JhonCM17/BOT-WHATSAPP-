import pandas as pd
import pyautogui as pg
import webbrowser
import time

# Proporciona la ruta completa del archivo
ruta_archivo = 'C:/Users/JhonCM/Documents/Proyectos Python/BOT WHATSAP/DATA.xlsx'
excel = pd.read_excel(ruta_archivo)
contactos = excel['NUMEROS']



mensaje = "Hola, soy un bot de WhatsApp 🤖👾"


def enviar_mensaje(contacto, mensaje):
    url = f'https://web.whatsapp.com/send?phone={contacto}&text={mensaje}'
    webbrowser.open_new_tab(url)
    time.sleep(9)  
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl', 'w')

print("Asegúrate de haber iniciado sesión en WhatsApp Web.")
time.sleep(5)

for contacto in contactos:
    enviar_mensaje(contacto, mensaje)
