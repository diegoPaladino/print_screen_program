#print_screen
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

def print_screen():
    p.keyDown('fn')
    p.keyDown('printscreen')
    p.keyUp('fn')
    p.keyUp('printscreen')
#execution
contagem()
print_screen()
