import pyautogui
import time


pyautogui.alert('o codigo vai comneçar nao usar nada enquanto o codigo esta rodando')
pyautogui.PAUSE = 0.5
# abrir google drive
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# entrar na area de trabalho
pyautogui.hotkey('win', 'd')
projetoPython
# clicar na area de trabalho
# enquanto estou arrastando eu vou mudar para meu google drive
# larquei o arquivo dentro
# esperar 5 segundos
