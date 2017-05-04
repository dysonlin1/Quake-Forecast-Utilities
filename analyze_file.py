# -*- coding: utf-8 -*-
# analyze_file.py
import locate
import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True


# Duplicate file
def duplicate_file():
    pyautogui.rightClick()
    time.sleep(1)
    for i in range(5):
        pyautogui.press('up')
    pyautogui.press('c')
    
    pyautogui.moveRel(100, 0)
    pyautogui.rightClick()
    for i in range(4):
        pyautogui.press('down')
    pyautogui.press('p')
    time.sleep(1)
    
# Ramane file_name to file_name - Analysis
def rename_file():
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveRel(0, 34)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('end')
    for i in range(4):
        pyautogui.press('left')
    for i in range(2):
        pyautogui.press('backspace')
    pyautogui.typewrite('Analysis')
    pyautogui.press('enter')
    
# Open file with Painter
def open_file():
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.moveTo(445, 65)
    pyautogui.click() # select Rectangle
    time.sleep(1)
    pyautogui.moveTo(814, 63)
    pyautogui.click() # select Red
    
# Duplicate file, ramane it and open it with Painter
def analyze_file(file_number):
    (x, y) = locate.get_file_location(file_number, 'original')
    pyautogui.moveTo(x, y)
    duplicate_file()
    rename_file()
    open_file()