#print_screen_3

#importing the libraries
import pyautogui as p
import time as t


#declarations
def contagem():
    t.sleep(2)
    print('5')
    t.sleep(1)
    print('4')
    t.sleep(1)
    print('3')
    t.sleep(1)
    print('2')
    t.sleep(1)
    print('1')
    t.sleep(1)
    print('SORRIA!!')
    t.sleep(2)

def print_screen_3():
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('print_screen.png')

#execution
contagem()
print_screen_3()