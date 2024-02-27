import pyautogui
from time import sleep
palavra = 'escrever alguma coisa'

for letra in palavra:
    sleep(1.5)
    pyautogui.press(letra)