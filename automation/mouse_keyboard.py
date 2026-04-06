import pyautogui
import time

def click(x, y):
    pyautogui.click(x, y)

def write(text):
    pyautogui.write(text, interval=0.05)

def press(key):
    pyautogui.press(key)

def abrir_pesquisa_windows():
    pyautogui.press("win")
    time.sleep(1)
