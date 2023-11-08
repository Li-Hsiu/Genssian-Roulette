import tkinter as tk
import random
import os
import webbrowser
import threading
import time

links = ['https://www.baidu.com/baidu?ie=utf-8&wd=%E5%8E%9F%E7%A5%9E',
         'https://baike.baidu.com/item/%E5%8E%9F%E7%A5%9E/23583622?fr=ge_ala',
         'https://ys.mihoyo.com/?utm_source=adbdpz&from_channel=adbdpz#/',
         'https://www.biligame.com/detail/?id=105667&sourceFrom=2000040011&spm_id_from=333.337.0.0',
         'https://tieba.baidu.com/f?kw=%D4%AD%C9%F1&fr=ala0&tpl=5&dyTabStr=MCwxLDMsMiw2LDQsNSw4LDcsOQ%3D%3D',
         'https://weibo.com/n/%E5%8E%9F%E7%A5%9E',
         'https://space.bilibili.com/401742377?spm_id_from=333.337.0.0',
         'https://genshin.hoyoverse.com/en/',
         'https://www.youtube.com/c/GenshinImpact',
         'https://en.wikipedia.org/wiki/Genshin_Impact',
         'https://twitter.com/GenshinImpact',
         'https://www.facebook.com/Genshinimpact/',
         'https://www.instagram.com/genshinimpact/',
         'https://www.twitch.tv/directory/category/genshin-impact',
         'https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_adbdpz']

window = tk.Tk()

value = 1
count = 0
bullets = [1,0,0,0,0,0]
stage = 0

def generate_list(num):
    global bullets
    bullets = [0,0,0,0,0,0]
    for i in range(num):
        bullets[i] = 1
        
def open(sec,link):
    time.sleep(sec)
    webbrowser.open(link)

def reload(num):
    global count
    count = 0
    generate_list(num)
    label.config(text=("子弹数: "+str(value)+"/"+str(6-count)))
    button.config(text="开火")
    label2.config(text="勇敢扣下扳机")

def lose():
    global links
    for i in range(len(links)):
        threading.Thread(target=open(i/5,links[i]))

def fire():
    global bullets
    global count
    global value
    global stage
    if (count == 6):
        return
    if (random.choice(bullets) == 0):
        bullets.remove(0)
        count += 1
        label.config(text=("子弹数: "+str(value)+"/"+str(6-count)))
        label2.config(text="运气还不错x"+str(count))
    else:
        bullets.remove(1)
        count += 1
        label.config(text=("子弹数: "+str(value-1)+"/"+str(6-count)))
        label2.config(text="完蛋!我被原神包围了")
        button.config(text="上膛")
        stage = 0
        lose()
        #os.system("shutdown /s /t 1")
        
def click():
    global stage
    global value
    if (stage == 0):
        reload(value)
        stage = 1
    else:
        fire()
        
def increment_value():
    global value
    global count
    global stage
    if value>=6:
        return
    value += 1
    label.config(text=("子弹数: "+str(value)+"/6"))
    label2.config(text="准备开始新一轮吧")
    button.config(text="上膛")
    stage = 0

def decrement_value():
    global value
    global count
    global stage
    if value <= 1:
        return
    value -= 1
    label.config(text=("子弹数: "+str(value)+"/6"))
    label2.config(text="准备开始新一轮吧")
    button.config(text="上膛")
    stage = 0
    
label = tk.Label(window, text=("子弹数: "+str(value)+"/6"))
label.grid(row=0, column=1, padx=10, pady=10)

decrement_button = tk.Button(window, text=" - ", command=decrement_value)
decrement_button.grid(row=0, column=0, padx=10, pady=10)

increment_button = tk.Button(window, text=" + ", command=increment_value)
increment_button.grid(row=0, column=2, padx=10, pady=10)

button = tk.Button(window, text="上膛", command=click)
button.grid(row=1, column=0, padx=10, pady=10)

label2 = tk.Label(window, text="准备开始新一轮吧")
label2.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.geometry("220x100")
window.title("赌")
window.mainloop()
