import  webbrowser as web  
import time  
import os  
import random  
count = random.randint(2,4)  
j = 0  
while j < count:  
    i = 0  
    while i <= 2:  
        web.open_new_tab('https://m.weibo.cn/p/1005051877190705')  
        i = i + 1  
        time.sleep(0.5)  
    else:  
#       os.system('taskkill /F /IM iexplore.exe')  
        print j,'times close Browser!'  
        j = j + 1#注意这个次数增1的位置！！  

