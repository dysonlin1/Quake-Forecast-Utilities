# -*- coding: utf-8 -*-
# quake_forecast.py

import locate
import pyautogui
import time
import pyperclip
from WeChat import drag_to_WeChat
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

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

def get_date_stamp():
    date_stamp = time.strftime("%Y-%m-%d")
    return date_stamp

def get_time_stamp():
    time_stamp = time.strftime("%Y-%m-%d")
    time_stamp += ' '
    time_stamp += time.strftime("%H:%M")
    time_stamp += ' UTC+8'
    return time_stamp

def get_new_file_name(old_file_name):   
    old_date_stamp = old_file_name[0:10]
    # print('Old date stamp: ' + old_date_stamp)
  
    new_date_stamp = get_date_stamp()
    # print('New date stamp: ' + new_date_stamp)
  
    new_file_name = old_file_name.replace(old_date_stamp, new_date_stamp)
    #print('New file name: ' + new_file_name)
  
    return new_file_name

def name_file(file_number, new_file_name):
    (x, y) = locate.get_file_location(file_number, 'new')
    pyperclip.copy(new_file_name) # copy new file name to clipboard
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(1)
    
    (x, y) = locate.get_file_name_location(file_number, 'new')
    #pyautogui.moveRel(0, 42)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(1)
  
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('p') # paste new file name from clip board
    time.sleep(1)
    pyautogui.press('enter')
 
# Name new file
def name_new_file(file_number):
    old_file_name = locate.get_file_name(file_number, 'old')
    time.sleep(1)
    new_file_name = get_new_file_name(old_file_name)
    time.sleep(1)
    name_file(file_number, new_file_name)

def name_new_files(file_number=1, to_WeChat=False):
    for i in range(file_number):
        name_new_file(i+1)
        
    if to_WeChat:
        for i in range(file_number):
            drag_to_WeChat(i+1)

def insert_Analysis_file(file_number):    
    locate.click_Blogger_tab()
    locate.click_Edit_area()
    
    if (file_number is 1):
        pyautogui.press('enter')
        
    pyautogui.press('up')
    
    analysis_file_name = locate.get_file_name(file_number, 'analysis')    
    (x, y) = locate.get_file_location(file_number, 'analysis')
    
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    
    if (file_number is 1):
        (x, y) = (700, 400)
    else:
        (x, y) = (700, 957)
        
    pyautogui.dragTo(x, y, 2)
    time.sleep(5)

    locate.scroll_down()

    locate.click_Edit_area()
    
    if (file_number is 1):
        locate.click_image(500)
    else:
        locate.click_image(957)
        
    locate.scroll_down()
    
    locate.click_Super_Big_button()
    locate.scroll_down()
    
    locate.click_Add_Image_Title_button()
    locate.scroll_down()
    
    locate.click_Add_Image_Title_field()
    pyautogui.tripleClick()
 
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)

    locate.click_Font_Size()

    pyautogui.moveRel(0, 93)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    locate.scroll_down()
    locate.click_Edit_area()
    pyautogui.press('up')

def insert_original_file(file_number):
    locate.click_Blogger_tab()
    locate.click_Edit_area()
    pyautogui.press('up')
    
    original_file_name = locate.get_file_name(file_number, 'original')
    (x, y) = locate.get_file_location(file_number, 'original')
    
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.5)
    
    pyautogui.dragTo(700, 957, 2)
    time.sleep(5)
    locate.scroll_down()
    
    locate.click_Edit_area()
    locate.click_image(957)
    locate.scroll_down()   
    
    locate.click_Super_Big_button()
    locate.scroll_down()
    
    locate.click_Add_Image_Title_button()
    locate.scroll_down()
    
    locate.click_Add_Image_Title_field()
    pyautogui.tripleClick()
 
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)

    locate.click_Font_Size()

    pyautogui.moveRel(0, 93)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    locate.scroll_down()
    locate.click_Edit_area()
    pyautogui.press('up')

def insert_files(file_number=1):
    for i in range(file_number):
        insert_Analysis_file(i+1)
        
    for i in range(file_number):
        insert_original_file(i+1)

quake_forecast_title = {
    'Chinese': '地震預報：',
    'Japanese': '地震予報：',
    'English': 'Quake Forecast: '
}

quake_signals_title = {
    'Chinese': '地震訊號：',
    'Japanese': '地震信号：',
    'English': 'Quake Signals: '
}

author = {
    'Chinese': '台灣地震預測研究所 所長\n林湧森',
    'Japanese': '台湾地震予測研究所 所長\n林湧森',
    'English': 'Dyson Lin\nFounder & CEO, Taiwan Quake Forecast Institute'}

Already_happened = {
    'Chinese': '已經發生：',
    'Japanese': '発生しました：',
    'English': 'Already happened: '}

Within = {
    'Chinese': '',
    'Japanese': '',
    'English': 'Within '}

Days = {
    'Chinese': '日以內，',
    'Japanese': '日以內に、',
    'English': ' days, '}

Red = {
    'Chinese': '紅：',
    'Japanese': '赤：',
    'English': 'Red: '}

Orange = {
    'Chinese': '橙：',
    'Japanese': 'オレンジ：',
    'English': 'Orange: '}

Yellow = {
    'Chinese': '黃：',
    'Japanese': '黃：',
    'English': 'Yellow: '}

Green = {
    'Chinese': '綠：',
    'Japanese': '綠：',
    'English': 'Green: '}

Blue = {
    'Chinese': '藍：',
    'Japanese': '青：',
    'English': 'Blue: '}

Purple = {
    'Chinese': '紫：',
    'Japanese': '紫：',
    'English': 'Purple: '}



station = {}

station['台灣各站'] = {
    'Chinese': '台灣各站', 
    'Japanese': '台湾各局', 
    'English': 'Taiwan Stations '}

station['宜蘭站'] = {
    'Chinese': '宜蘭站', 
    'Japanese': '宜蘭局', 
    'English': 'Yilan Station '}

station['上海站'] = {
    'Chinese': '上海站', 
    'Japanese': '上海局', 
    'English': 'Shanghai Station '}

station['洛杉磯站'] = {
    'Chinese': '洛杉磯站', 
    'Japanese': 'ロサンゼルス局', 
    'English': 'Los Angeles Station '}

station['新竹綠光站'] = {
    'Chinese': '新竹綠光站', 
    'Japanese': '新竹綠光局', 
    'English': 'Hsinchu Green Light Station '}

station['南投草屯站'] = {
    'Chinese': '南投草屯站', 
    'Japanese': '南投草屯局', 
    'English': 'Nantou Caotun Station '}

station['台南熱心站'] = {
    'Chinese': '台南熱心站', 
    'Japanese': '台南熱心局', 
    'English': 'Tainan Hot Heart Station '}

station['台南喜福站'] = {
    'Chinese': '台南喜福站', 
    'Japanese': '台南喜福局', 
    'English': 'Tainan Joy & Luck Station '}

station['台南新生站'] = {
    'Chinese': '台南新生站', 
    'Japanese': '台南新生局', 
    'English': 'Tainan Xinsheng Station '}

station['高雄站'] = {
    'Chinese': '高雄站', 
    'Japanese': '高雄局', 
    'English': 'Kaohsiung Station '}

station['台中潭子站'] = {
    'Chinese': '台中潭子站', 
    'Japanese': '台中潭子局', 
    'English': 'Taichung Tantzu Station '}

station['桃園站'] = {
    'Chinese': '桃園站', 
    'Japanese': '桃園局', 
    'English': 'Taoyuan Station '}

station['台中大里站'] = {
    'Chinese': '台中大里站', 
    'Japanese': '台中大里局', 
    'English': 'Taichung Dali Station '}

station['南非德本站'] = {
    'Chinese': '南非德本站', 
    'Japanese': '南アフリカ ダーバン局', 
    'English': 'Durban, South Africa Station '}

station['義大利法恩扎站'] = {
    'Chinese': '義大利法恩扎站', 
    'Japanese': 'イタリア ファエンツァ局', 
    'English': 'Faenza, Italy Station '}

station['義大利卡爾塔尼塞塔站'] = {
    'Chinese': '義大利卡爾塔尼塞塔站', 
    'Japanese': 'イタリア カルタニッセッタ局', 
    'English': 'Caltanissetta, Italy Station '}

station['紐西蘭奧克蘭站'] = {
    'Chinese': '紐西蘭奧克蘭站', 
    'Japanese': 'ニュージーランド オークランド局', 
    'English': 'Auckland, New Zealand Station '}

station['智利伊基克站'] = {
    'Chinese': '智利伊基克站', 
    'Japanese': 'チリ イキケ局', 
    'English': 'Iquique, Chile Station '}

station['加拿大列治文站'] = {
    'Chinese': '加拿大列治文站', 
    'Japanese': 'カナダ リッチモンド局', 
    'English': 'Richmond BC Canada Station '}
