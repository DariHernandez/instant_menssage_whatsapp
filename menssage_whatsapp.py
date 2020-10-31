#! python3
# Send and intsnat menssage for facebook

import pyautogui, time, os, subprocess
import webbrowser
from rwJson import readJsonFile, writeJsonFile


def getSearchBarInfo (json_file, alarm_sound): 
    """ Get position and color of seach bar"""
    print ('Hover the mouse over whatsapp web search bar for 10 seconds. ')
    counter = 0
    # Get position and color
    x, y = pyautogui.position()
    color = pyautogui.screenshot().getpixel((x,y))

    # loop each second
    while counter < 10: 
        time.sleep (1)
        # Get new position and color
        last_x, last_y = x, y
        last_color = pyautogui.screenshot().getpixel((x,y))
        x, y = pyautogui.position()
        color = pyautogui.screenshot().getpixel((x,y))

        # Check if colors or positions change
        if x == last_x and y == last_y and color == last_color: 
            counter += 1
        else: 
            counter = 0
        
        print_counter = 10 - counter 
        if print_counter < 10: 
            print_counter = '0' + str(print_counter)
        print (print_counter, end='')
        print ('\b' * 3, end='', flush=True) # Delate the las print
    
    # play alarm
    subprocess.Popen(['see', alarm_sound])

    # Write json and return data
    return_dic = {'xy': (x, y),
                    'rgb': color}
    writeJsonFile(json_file, return_dic)

    # return data
    return return_dic

def send_message (friends, message):
    """ Read information and send message"""
    # Files
    path = os.path.dirname (__file__)
    json_file = os.path.join (path, 'search_bar.json')
    alarm_sound = os.path.join (path, 'sound.mp3')

    # Open page 
    webbrowser.open ("https://web.whatsapp.com/")

    # Cordenates
    data = readJsonFile (json_file)
    if not data: 
        data = getSearchBarInfo(json_file, alarm_sound)
    seaarchBar = data['xy']
    seaarchBarColor = data['rgb']

    # Wait web page
    print ('Whait for the whatsapp web window...')
    while not pyautogui.pixelMatchesColor (seaarchBar[0], seaarchBar[1], seaarchBarColor):
        time.sleep (0.5)

    # Send menssage
    for friend in friends: 
        print ('Sending menssage to %s' % (friend))
        pyautogui.click (seaarchBar)
        time.sleep (1)
        pyautogui.typewrite (friend)
        time.sleep (1)
        pyautogui.typewrite (['enter'])
        time.sleep (1)
        pyautogui.typewrite (message)
        time.sleep (1)
        pyautogui.typewrite (['enter'])
        time.sleep (1)
