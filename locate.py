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
    
def click_Blog_Title():
    #locate_and_click('BlogTitle.png')
    pyautogui.moveTo(1147, 216)
    time.sleep(0.1)
    pyautogui.click() # click

def click_Publish_button():
    #x, y = pyautogui.locateCenterOnScreen('PublishButton.png', region=(1400,135, 469, 945)) # locate
    x, y = pyautogui.locateCenterOnScreen('PublishButton.png') # locate
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.click() # click
    
def click_Super_Big_button():
    locate_and_click('SuperBigButton.png')
    
def click_Add_Image_Title_button():
    locate_and_click('AddImageTitleButton.png')
    
def click_Add_Image_Title_field():
    locate_and_click('AddNewImageTitleField.png')
    
def click_Font_Size():
    locate_and_click('FontSize.png')
    
def scroll_down():
    pyautogui.moveTo(1100, 600)
    time.sleep(1)
    pyautogui.scroll(-10000) # scroll down
    time.sleep(1)
    
def click_Edit_area():    
    # click bottom of Edit area
    pyautogui.moveTo(1100, 1000)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
def click_image(y):
    scroll_down()
    
    x = 700
           
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    


def get_file_location(file_number, file_type='original'):
    if ((file_type is 'analysis') | (file_type is 'old')):
        x = 160
    else: # 'original' or 'new'
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
