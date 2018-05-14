import pyautogui
import time
import pyperclip
pyautogui.PAUSE = 0.4
pyautogui.FAILSAFE = True

def locate_and_click(png_file_name):
    try:
        # locate
        (x, y) = pyautogui.locateCenterOnScreen(png_file_name)
        
        # move mouse
        pyautogui.moveTo(x, y)
        
        # click
        pyautogui.click(x, y)
    except:
        print('Cannot locate:' + png_file_name)
    
def click_Blogger_tab():
    try:
        locate_and_click('BloggerTab.png')
        #pyautogui.moveTo(831, 31)
        pyautogui.click()
    except:
        print('Cannot click Blogger tab.')
        
def click_Blog_Title():
    pyautogui.moveTo(1147, 216)
    pyautogui.click()

def click_Facebook_Publish_button():
    locate_and_click('FacebookPublishButton.png')    
    
def click_Super_Big_button():
    #locate_and_click('SuperBigButton.png')
    locate_and_click('new_super_big_button.png')
    
def click_Add_Image_Title_button():
    locate_and_click('AddImageTitleButton.png')
    
def click_Add_Image_Title_field():
    locate_and_click('AddNewImageTitleField.png')
    
def click_Font_Size():
    pyautogui.moveTo(775, 295)
    pyautogui.click()
    
def scroll_down():
    pyautogui.moveTo(1100, 600)
    pyautogui.scroll(-10000) # scroll down
    
def click_Edit_area():    
    # click bottom of Edit area
    pyautogui.moveTo(1100, 1000)
    pyautogui.click()
    
def click_image(y):
    scroll_down()
    x = 700       
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
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
    #time.sleep(0.5)
    pyautogui.click()

    (file_name_x, file_name_y) = get_file_name_location(file_number, file_type)
    pyautogui.moveTo(file_name_x, file_name_y)
    pyautogui.click()
    time.sleep(0.5)
    
    pyautogui.rightClick()
    for i in range(3):
        pyautogui.press('down')
        
    pyautogui.press('c') # copy file name to clipboard
    time.sleep(0.5)
    
    file_name = pyperclip.paste() # read file name from clipboard
    return file_name

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
    #time.sleep(7)
    time.sleep(3)
    pyautogui.moveTo(445, 65)
    pyautogui.click() # select Rectangle
    
    # select Red
    #pyautogui.moveTo(814, 62)
    
    # select Green
    #pyautogui.moveTo(880, 62)
    
    # select Purple
    pyautogui.moveTo(946, 62)
    
    # select Yellow
    pyautogui.moveTo(858, 62)
    
    pyautogui.click() 
    
# Duplicate file, ramane it and open it with Painter
def analyze_file(file_number):
    (x, y) = get_file_location(file_number, 'original')
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

def get_new_file_name(old_file_name, date_stamp):
    splt_old_file_name = old_file_name.split()
    old_date_stamp = splt_old_file_name[0]
    old_date = old_date_stamp[0:10]
    
    if date_stamp is None:
        new_date_stamp = get_date_stamp()
    else:
        new_date_stamp = date_stamp
    
    new_date = new_date_stamp[0:10]
    
    if (new_date == old_date):
        new_date_stamp = new_date + '-2'
  
    new_file_name = old_file_name.replace(old_date_stamp, new_date_stamp)
    #print('New file name: ' + new_file_name)
  
    return new_file_name

def name_file(file_number, new_file_name):
    (x, y) = get_file_location(file_number, 'new')
    pyperclip.copy(new_file_name) # copy new file name to clipboard
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    
    (x, y) = get_file_name_location(file_number, 'new')
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
  
    pyautogui.rightClick()
    time.sleep(1)
    for i in range(4):
        pyautogui.press('down')
        #time.sleep(0.5)
    pyautogui.press('p') # paste new file name from clip board
    time.sleep(1)
    pyautogui.press('enter')

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
    get_file_name(file_number, file_type)
    
    click_WeChat_icon()
    click_WeChat_Edit_area()

    # paste file name from clipboard
    pyautogui.hotkey('ctrl', 'v')

    (x, y) = get_file_location(file_number, file_type)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.dragTo(1090, 935, 2)
    pyautogui.click()
    time.sleep(1)

    pyautogui.press('enter')    
    
def name_new_file(file_number, date_stamp):
    old_file_name = get_file_name(file_number, 'old')
    time.sleep(1)
    new_file_name = get_new_file_name(old_file_name, date_stamp)
    time.sleep(1)
    name_file(file_number, new_file_name)

def name_new_files(file_number=1, to_WeChat=False, date_stamp=None):
    for i in range(file_number):
        name_new_file(i+1, date_stamp)
        
    if to_WeChat:
        for i in range(file_number):
            drag_to_WeChat(i+1)

def insert_Analysis_file(file_number):    
    click_Blogger_tab()
    click_Edit_area()
    
    if (file_number is 1):
        pyautogui.press('enter')
        
    pyautogui.press('up')
    
    analysis_file_name = get_file_name(file_number, 'analysis')    
    (x, y) = get_file_location(file_number, 'analysis')
    
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    
    if (file_number is 1):
        (x, y) = (700, 400)
        pyautogui.dragTo(x, y, 2)
    else:
        (x, y) = (700, 957)
        pyautogui.dragTo(x, y, 2)
    
    #time.sleep(7)
    #time.sleep(6)
    time.sleep(15)

    scroll_down()

    click_Edit_area()
    
    if (file_number is 1):
        click_image(500)
    else:
        click_image(957)
        
    scroll_down()
    
    click_Super_Big_button()
    scroll_down()
    
    click_Add_Image_Title_button()
    scroll_down()
    time.sleep(1)
    
    click_Add_Image_Title_field()
    pyautogui.tripleClick()
    time.sleep(1)
    
    # paste file name from clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    click_Font_Size()

    pyautogui.moveRel(0, 93)
    time.sleep(1)
    pyautogui.click()
    #time.sleep(1)

    scroll_down()
    click_Edit_area()
    pyautogui.press('up')

def insert_original_file(file_number):
    click_Blogger_tab()
    click_Edit_area()
    pyautogui.press('up')
    
    original_file_name = get_file_name(file_number, 'original')
    (x, y) = get_file_location(file_number, 'original')
    
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    
    pyautogui.dragTo(700, 957, 2)
    #time.sleep(7)
    #time.sleep(6)
    time.sleep(15)
    
    scroll_down()
    
    click_Edit_area()
    click_image(957)
    scroll_down()   
    
    click_Super_Big_button()
    scroll_down()
    
    click_Add_Image_Title_button()
    scroll_down()
    
    click_Add_Image_Title_field()
    pyautogui.tripleClick()
    time.sleep(1)
    
    # paste file name from clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    click_Font_Size()

    pyautogui.moveRel(0, 93)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    scroll_down()
    click_Edit_area()
    pyautogui.press('up')

def insert_files(file_number=1):
    for i in range(file_number):
        insert_Analysis_file(i+1)
        
    for i in range(file_number):
        insert_original_file(i+1)

def set_blog_title():
    click_Blogger_tab()
    click_Blog_Title()
    
    # paste from clipboard
    pyautogui.rightClick()
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('p')
    pyautogui.press('enter')

def get_Quake_Forecast_title(quake_forecast, station_name, languages, time_stamp):
    blog_title = {}
    for language in languages:
        blog_title[language] = station_name[language]
        blog_title[language] += quake_forecast_title[language]
        quake_number = 0
        for quake in quake_forecast:
            quake_number += 1
            blog_title[language] += '('
            blog_title[language] += str(quake_number)
            blog_title[language] += ')'
            blog_title[language] += quake['color'][language]
            blog_title[language] += Within[language]
            blog_title[language] += str(quake['time'])
            blog_title[language] += Days[language]
            blog_title[language] += quake['location'][language]
            blog_title[language] += quake['magnitude']
            blog_title[language] += ' '
    
    blog_title_str = (time_stamp + ' ')
    
    for language in languages:
        blog_title_str += (blog_title[language])
    
    blog_title_str = blog_title_str.strip() # remove extra white space
    #print(blog_title_str)
    pyperclip.copy(blog_title_str) # copy to clipboard
    
    return (blog_title, blog_title_str)

def get_Quake_Forecast_text(quake_forecast, station_name, languages, time_stamp):
    blog_text = {}
    for language in languages:
        blog_text[language] = station_name[language]
        blog_text[language] += quake_forecast_title[language] + '\n'
        quake_number = 0
        for quake in quake_forecast:
            quake_number += 1
            blog_text[language] += '('
            blog_text[language] += str(quake_number)
            blog_text[language] += ')'
            blog_text[language] += quake['color'][language]
            blog_text[language] += Within[language]
            blog_text[language] += str(quake['time'])
            blog_text[language] += Days[language]
            blog_text[language] += quake['location'][language]
            blog_text[language] += quake['magnitude']
            blog_text[language] += '\n'
        blog_text[language] += '\n'    
        blog_text[language] += author[language]
        blog_text[language] += '\n'
        blog_text[language] += time_stamp
        blog_text[language] += '\n\n\n'

    blog_text_str = ''        
    for language in languages:
        blog_text_str += blog_text[language]
    blog_text_str = blog_text_str.strip() # remove extra white space
    #print(blog_text_str)
    pyperclip.copy(blog_text_str) # copy to clipboard
    
def get_Quake_Signals_title(signals, station_name, languages, time_stamp): 
    blog_title = {}
    for language in languages:
        blog_title[language] = station_name[language]
        blog_title[language] += quake_signals_title[language]
        blog_title[language] += Already_happened[language]
        quake_number = 0
        for quake in signals:
            quake_number += 1
            blog_title[language] += '('
            blog_title[language] += str(quake_number)
            blog_title[language] += ')'
            blog_title[language] += quake['color'][language]
            #blog_title[language] += Within[language]
            blog_title[language] += str(quake['time'])
            blog_title[language] += ' '
            blog_title[language] += quake['location'][language]
            blog_title[language] += ' '
            blog_title[language] += quake['magnitude']
            blog_title[language] += ' '
    
    blog_title_str = (time_stamp + ' ')
    
    for language in languages:
        blog_title_str += (blog_title[language])
    
    blog_title_str = blog_title_str.strip() # remove extra white space
    #print(blog_title_str)
    pyperclip.copy(blog_title_str) # copy to clipboard
    
    return (blog_title, blog_title_str)

def get_Quake_Signals_text(signals, station_name, languages, time_stamp):
    blog_text = {}
    for language in languages:
        blog_text[language] = station_name[language]
        blog_text[language] += quake_signals_title[language] + '\n'
        blog_text[language] += Already_happened[language] + '\n'
        quake_number = 0
        for quake in signals:
            quake_number += 1
            blog_text[language] += '('
            blog_text[language] += str(quake_number)
            blog_text[language] += ')'
            blog_text[language] += quake['color'][language]
            #blog_text[language] += Within[language]
            blog_text[language] += str(quake['time'])
            blog_text[language] += ' '
            #blog_text[language] += Days[language]
            blog_text[language] += quake['location'][language]
            blog_text[language] += ' '
            blog_text[language] += quake['magnitude']
            blog_text[language] += '\n'
        blog_text[language] += '\n'    
        blog_text[language] += author[language]
        blog_text[language] += '\n'
        blog_text[language] += time_stamp
        blog_text[language] += '\n\n\n'

    blog_text_str = ''        
    for language in languages:
        blog_text_str += blog_text[language]
    blog_text_str = blog_text_str.strip() # remove extra white space
    #print(blog_text_str)
    pyperclip.copy(blog_text_str) # copy to clipboard
    
def get_blog_address():
    click_Blogger_tab()

    pyautogui.moveTo(710, 61)
    pyautogui.tripleClick()
    pyautogui.rightClick()
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('c') # copy blog address to clipboard
    blog_address = pyperclip.paste() # read blog address from clipboard
    return blog_address

def set_blog_text():
    click_Blogger_tab()
    scroll_down()
    click_Edit_area()
    pyautogui.press('backspace')

    pyautogui.rightClick()
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('p') # paste from clipboard
    
def click_Facebook_tab(tab_number):
    global Facebook_tab_1_x
    global Facebook_tab_2_x
    global Facebook_tab_3_x
    
    if tab_number is 1:
        (x, y) = (520, 30)
    elif tab_number is 2:
        (x, y) = (630, 30)
    elif tab_number is 3:
        (x, y) = (733, 30)
    else:
        print('Wrong tab number:', str(tab_number))
    
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click() # click
    
def click_WeChat_icon():
    pyautogui.moveTo(1000, 1079)
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
    
def post_to_WeChat():
    click_WeChat_icon()
    click_WeChat_Edit_area()
    
    # paste Quake Forecast from clipboard
    pyautogui.hotkey('ctrl', 'v')
    
    # darg analysis file 1 to WeChat
    x = 160
    y = 70
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.dragTo(1090, 935, 2)
    pyautogui.click()
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(3)
    
def click_Twitter_tab():
    (x, y) = (404, 30)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click() # click
    
def click_Twit_button():
    (x, y) = (1808, 122)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click() # click

def click_Twitter_Edit_area():
    (x, y) = (1068, 466)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click() # click

def post_to_Twitter():
    click_Twitter_tab()
    click_Twit_button()

    # paste Quake Forecast from clipboard
    pyautogui.hotkey('ctrl', 'v')

    # darg analysis file 1 to Twitter
    x = 160
    y = 70
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.dragTo(1068, 466, 2)
    pyautogui.click()
    time.sleep(1)

    for i in range(0, 6):
        pyautogui.press('tab')
    pyautogui.press('enter')
    
    time.sleep(3)
    
    #pyautogui.scroll(-100) # scroll down

def publish_blog():
    #pyautogui.moveTo(1717, 237)
    pyautogui.moveTo(1715, 219)
    time.sleep(5)
    pyautogui.click()
    #time.sleep(5)
    time.sleep(1)
    
def view_blog():
    click_Blogger_tab()
    time.sleep(1)
    pyautogui.moveTo(833, 504)
    time.sleep(1)
    pyautogui.moveTo(833, 506)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

def close_Blogger_article_list():
    click_Blogger_tab()
    time.sleep(1)
    
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.rightClick()
    time.sleep(1)

    for i in range(0, 6):
        pyautogui.press('down')
    
    time.sleep(1)
    pyautogui.press('enter')

    pyautogui.moveRel(80, 0)
    time.sleep(2)
    
def post_Quake_Forecast(quake_forecast, station_name, time_stamp,
            blog_address, blog_title_str):
    # Post to Facebook, WeChat and Twitter

    Twitter_languages = ['Japanese']
    (blog_title_Twitter, blog_title_str_Twitter) = get_Quake_Forecast_title(quake_forecast,
                                                station_name, Twitter_languages, time_stamp)
    post_text_Twitter = blog_title_str_Twitter + '\n' + blog_address
    pyperclip.copy(post_text_Twitter) # copy to clipboard
    post_to_Twitter()
    
    
    post_text = blog_title_str + '\n' + blog_address    
    pyperclip.copy(post_text) # copy to clipboard
    post_to_WeChat()

    pyperclip.copy(post_text) # copy to clipboard
    post_to_Facebook(1)

    pyperclip.copy(post_text) # copy to clipboard
    post_to_Facebook(2)

    pyperclip.copy(post_text) # copy to clipboard
    post_to_Facebook(3)

def publish_Quake_Forecast(quake_forecast, station_name, languages, time_stamp):
    (blog_title, blog_title_str) = get_Quake_Forecast_title(quake_forecast, 
                                          station_name, languages, time_stamp)
    set_blog_title()
    get_Quake_Forecast_text(quake_forecast, station_name, languages, time_stamp)
    set_blog_text()
    publish_blog()
    time.sleep(15)
    return (blog_title, blog_title_str)    

def post_to_Facebook(tab_number):
    click_Facebook_tab(tab_number)
    
    # click Post field
    if tab_number is 1:
        (x, y) = (1244, 945)
    elif tab_number is 2:
        (x, y) = (720, 980)
    elif tab_number is 3:
        (x, y) = (780, 950)
    else:
        print('Wrong tab number:', str(tab_number))
        
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.scroll(10000) # scroll up
    time.sleep(1)

    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    # paste Quake Forecast from clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(4)
    
    if tab_number is 1:
        pyautogui.moveTo(x+100, y)
        time.sleep(1)
        pyautogui.scroll(-700) # scroll down
        time.sleep(2)
        
        for i in range(0, 16):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
    elif tab_number is 2:
        pyautogui.moveTo(x+100, y)
        time.sleep(1)
        pyautogui.scroll(-700) # scroll down
        time.sleep(2)
        
        for i in range(0, 15):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
    elif tab_number is 3:
        for i in range(0, 12):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
    else:
        print('Wrong tab number:', str(tab_number))
    
    time.sleep(1)
    
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

station['嘉義站'] = {
    'Chinese': '嘉義站', 
    'Japanese': '嘉義局', 
    'English': 'Chiayi Station '}

station['日本輻射值'] = {
    'Chinese': '日本輻射值', 
    'Japanese': '日本の放射線値', 
    'English': 'Japan Radiation Value '}

station['高雄前鎮站'] = {
    'Chinese': '高雄前鎮站', 
    'Japanese': '高雄前鎮局', 
    'English': 'Kaohsiung Cianjhen Station '}

station['高雄前鎮南站'] = {
    'Chinese': '高雄前鎮南站', 
    'Japanese': '高雄前鎮南局', 
    'English': 'Kaohsiung Cianjhen South Station '}

station['高雄小港站'] = {
    'Chinese': '高雄小港站', 
    'Japanese': '高雄小港局', 
    'English': 'Kaohsiung Xiaogang Station '}

station['智利聖地牙哥站'] = {
    'Chinese': '智利聖地牙哥站', 
    'Japanese': 'チリ サンディエゴ局', 
    'English': 'Santiago, Chile Station '}

station['屏東站'] = {
    'Chinese': '屏東站', 
    'Japanese': '屏東局', 
    'English': 'Pingtung Station '}

station['成都站'] = {
    'Chinese': '成都站', 
    'Japanese': '成都局', 
    'English': 'Chengdu Station '}

station['蘇州站'] = {
    'Chinese': '蘇州站', 
    'Japanese': '蘇州局', 
    'English': 'Suzhou Station '}

station['彰化站'] = {
    'Chinese': '彰化站', 
    'Japanese': '彰化局', 
    'English': 'Changhua Station '}

station['台中北區站'] = {
    'Chinese': '台中北區站', 
    'Japanese': '台中北區局', 
    'English': 'Taichung North Station '}

station['台南安南站'] = {
    'Chinese': '台南安南站', 
    'Japanese': '台南安南局', 
    'English': 'Tainan Annan Station '}

station['日本宇都宮站'] = {
    'Chinese': '日本宇都宮站', 
    'Japanese': '日本宇都宮局', 
    'English': 'Utsunomiya, Japan Station '}

station['日本東京站'] = {
    'Chinese': '日本東京站', 
    'Japanese': '日本東京局', 
    'English': 'Tokyo, Japan Station '}

station['新北站'] = {
    'Chinese': '新北站', 
    'Japanese': '新北局', 
    'English': 'New Taipei Station '}

station['台南東區站'] = {
    'Chinese': '台南東區站', 
    'Japanese': '台南東區局', 
    'English': 'Tainan East Station '}

station['花蓮吉安站'] = {
    'Chinese': '花蓮吉安站', 
    'Japanese': '花蓮吉安局', 
    'English': 'Hualien Jian Station '}

station['台北站'] = {
    'Chinese': '台北站', 
    'Japanese': '台北局', 
    'English': 'Taipei Station '}

station['竹北豆子埔公園站'] = {
    'Chinese': '竹北豆子埔公園站', 
    'Japanese': '竹北豆子埔公園局', 
    'English': 'Zhubei Douzipu Park Station '}

station['台東站'] = {
    'Chinese': '台東站', 
    'Japanese': '台東局', 
    'English': 'Taitung Station '}