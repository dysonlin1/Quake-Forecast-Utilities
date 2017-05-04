# -*- coding: utf-8 -*-
# name_new_file.py

import time
import pyperclip
import pyautogui
import date_stamp
import locate


def get_new_file_name(old_file_name):   
    old_date_stamp = old_file_name[0:10]
    # print('Old date stamp: ' + old_date_stamp)
  
    new_date_stamp = date_stamp.get_date_stamp()
    # print('New date stamp: ' + new_date_stamp)
  
    new_file_name = old_file_name.replace(old_date_stamp, new_date_stamp)
    #print('New file name: ' + new_file_name)
  
    return new_file_name

def name_file(file_number, new_file_name):
    (x, y) = locate.get_file_location(file_number, 'new')
    pyperclip.copy(new_file_name) # copy new file name to clipboard
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    
    (x, y) = locate.get_file_name_location(file_number, 'new')
    #pyautogui.moveRel(0, 42)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
  
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('p') # paste new file name from clip board
    time.sleep(0.5)
    pyautogui.press('enter')
    
# Name new file
def name_new_file(file_number):
    old_file_name = locate.get_file_name(file_number, 'old')
    new_file_name = get_new_file_name(old_file_name)
    name_file(file_number, new_file_name)

