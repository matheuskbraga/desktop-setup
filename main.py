# Bibliotecas necessárias
import pyautogui
import os  
from time import sleep                     
from dotenv import load_dotenv

from funcao_clicar_imagens import clicar_imagens


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


# Variáveis de ambiente
SENHA_GOOGLE = os.getenv("SENHA_GOOGLE") # campo se precisar armazena sua senha de forma segura para automação


# Abrir navegador Firefox
clicar_imagens("icone_firefox")
sleep(3)
pyautogui.hotkey("ctrl", "t")
sleep(1)
pyautogui.write("asimov.academy/", interval=0.10) 
pyautogui.press("enter")
sleep(2)
clicar_imagens("icone_entrar_asimov")
sleep(2)


# Abrir Spotify
clicar_imagens("icone_spotify")
sleep(5)
clicar_imagens("icone_playlist_spotify")
