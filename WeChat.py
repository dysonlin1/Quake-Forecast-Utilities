# -*- coding: utf-8 -*-
# WeChat.py
import pyautogui
import time
import locate

def click_WeChat_icon():
    pyautogui.moveTo(1500, 1079)
    time.sleep(1)
    pyautogui.moveTo(564, 1058)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

def click_WeChat_Edit_area():
    pyautogui.moveTo(1090, 935)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
# Paste a file's name to WeChat and then drag it to WeChat
def drag_to_WeChat(file_number, file_type='original'):
    # copy file name to clipboard
    locate.get_file_name(file_number, file_type)
    
    click_WeChat_icon()
    click_WeChat_Edit_area()

    # paste file name from clipboard
    pyautogui.hotkey('ctrl', 'v')

    (x, y) = locate.get_file_location(file_number, file_type)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.dragTo(1090, 935, 2)
    pyautogui.click()
    time.sleep(1)

    pyautogui.press('enter')