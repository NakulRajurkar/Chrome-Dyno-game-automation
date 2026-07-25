from datetime import date

import pyautogui
import time
from PIL import Image,ImageGrab
# from numpy import asarray
def hit(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
def iscollide(data):
    for i in range(250,300):
                     for j in range(410,563):
                          if data[i,j]<100:
                            hit("Down")
                            return True
    for i in range(275,325):
              for j in range(563,650):
                  
                  if data[i,j]<100:
                      hit("up")
                      return True
    return False
        
    

    # Image.show()
    
if __name__=="__main__":
    print("heyy... the dyno game about to start in 3 seconds")
    time.sleep(3)
    hit('up')
    while True:
        
       Image=ImageGrab.grab().convert('L')
    #    Image=takesscreenshot()
       data=Image.load()
       iscollide(data)
           
    # print(asarray(Image))
    #    for i in range(300,410):
    #       for j in range(600,650):
    #           data[i,j]=0
    #    for i in range(300,410):
    #              for j in range(410,610):
    #                  data[i,j]=171
    # Image.show()
    
    