# -*- coding: utf-8 -*-
# locate.py

import pyautogui
import time
import pyperclip
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True


def locate_and_click(png_file_name):
    try:
        # locate
        (x, y) = pyautogui.locateCenterOnScreen(png_file_name)
    
        # click
        pyautogui.click(x, y)
        time.sleep(0.5)
    except:
        print('Cannot locate:' + png_file_name)
    
def click_Blogger_tab():
    locate_and_click('BloggerTab.png')

def get_file_location(file_number, file_type='original'):
    if ((file_type is 'analysis') | (file_type is 'old')):
        x = 160
    else: # 'original'
        x = 53
    
    y = 80 + (file_number - 1) * 148
    return (x, y)

def get_file_name_location(file_number, file_type='original'):
    if ((file_type is 'analysis') | (file_type is 'old')):
        x = 160
    else: # 'original' or 'new'
        x = 53
    
    y = 114 + (file_number - 1) * 148
    return (x, y)

def get_file_name(file_number, file_type='original'):
    (file_x, file_y) = get_file_location(file_number, file_type)
    pyautogui.moveTo(file_x, file_y)
    pyautogui.click()

    (file_name_x, file_name_y) = get_file_name_location(file_number, file_type)
    pyautogui.moveTo(file_name_x, file_name_y)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.rightClick()
    for i in range(3):
        pyautogui.press('down')
    pyautogui.press('c') # copy file name to clipboard

    file_name = pyperclip.paste() # read file name from clipboard
    return file_name
