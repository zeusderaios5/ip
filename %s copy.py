
import os
import pyautogui
import time



num2 = 0
protocol = 'com.epicgames.launcher://social/friends/add?'
protocol2 = ''
while num2 < 200:
    num = 0
    protocol3 = ''
    protocol2 += 'aaaaaa'
    while num < 70:
        protocol3 += '%ff%ff%ff'
        os.startfile(protocol+protocol2+protocol3)

        time.sleep(0.3)
        pyautogui.keyDown('alt')
        pyautogui.press('f4')
        pyautogui.keyUp('alt')



        print(num2)
        num += 1
    num2 += 1
