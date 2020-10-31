# instant_menssage_whatsapp
## Description
This program use the **pyautogui module to send whatsapp menssage** to your contacts.
You can **configure the menssage** to send **and** your destination **contacts**

## Install modules
``` bash
$ pip install PyAutoGUI
``` 

## How to use
Run main.py

The **first time** that you run the program, it **request to hover the mouse over the whatsapp web search bar.** You need to do this for **10 seconds** without moving the cursor.
Important to have the **window maximized.**

![seach bar image]()

(The configuration is saved in 'seach_bar.json' file. If you fail this step, you can delete the file and try again)

When the **time is up**, you will hear an **audio / alarm.**

Later, **when you use the program**, in the same way, with the window maximized, **the messages will be sent automatically.**

### Information

Inside the main.py file, you can **change the menssage and your contacts**

``` python
# Contacts and menssage
friends = ['friend1', 'friend2']
message = 'Hello'
``` 
## Use example

1. Frist time running the program. 

``` bash
$ python3 main.py
``` 

2. Hover the mouse over the whatsapp web search bar.

![gif hover the mouse]()

3. Modify information

``` python
# Contacts and menssage
friends = ['Alex Smith', 'John Connor']
message = 'Hello, how are you?'
``` 

4. Run the program again


``` bash
$ python3 main.py
``` 