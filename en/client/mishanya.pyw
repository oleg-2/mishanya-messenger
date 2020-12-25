from tkinter import *
import requests
import random
import base64
import os.path
import time
from cryptography.fernet import Fernet


def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)


def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


with open('key1.txt', 'r', encoding='utf-8') as f:
    key = f.read().encode()

with open('key2.txt', 'r', encoding='utf-8') as f:
    key2 = f.read().encode()

with open('server_route.txt', 'r', encoding='utf-8') as f:
    server_route = f.read()

root = Tk()
root.resizable(False, False)
root.geometry("357x500")
root.title("mishanya-messenger")

check_ico = os.path.exists('chat.ico')

if check_ico == True:
    root.iconbitmap('chat.ico')
else:
    img_data = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABa66wAWuusAFrrrABa66wAWuusAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFrrrABa66yUWuusVFrrrABa66wAWuusAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWuusAFrrrZBa665wWuusNFrrrABa66wAWuusAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABa66wAWuutlFrrr/ha664wWuusHFrrrABa66wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFrrrABa662QWuuv/Frrr+ha663sWuusDFrrrABa66wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFrrrABa66wAWuusAFrrrABa66wAWuusAFrrrZBa66/8Wuuv/Frrr9Ra662sWuusAFrrrABa66wAWuusAFrrrABa66wAWuusAFrrrABa66wAWuusAFrrrABa66wAWuusAAAAAAAAAAAAZiu0AGYrtABmK7QAZiu0AAAAAAAAAAAAWuusAFrrrABa66wAWuusAFrrrABa66wAWuutjFrrr/xa66/8Wuuv/Frrr7xa661sWuusAFrrrABa66wAWuusAFrrrABa66wAWuusAFrrrABa66wAWuusAFrrrABa66wAWuusAGY3tABmK7QAZiu0AGYrtABmK7QAAAAAAAAAAABa66wYWuutKFrrrhxa6648WuuuPFrrrjRa667sWuuv/Frrr/xa66/8Wuuv/Frrr6Ba665cWuuuNFrrrjRa664wWuuuMFrrrixa664oWuuuJFrrriBa664QWuutaFrrrDha66wAYnewAGYrtABmK7RwZiu0VGYrtAAAAAAAAAAAAFrrreBa66/IWuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/wWuuuXFrrrCRiU7QAZiu0cGYrtqhmK7TYZiu0AAAAAAAAAAAAWuuvqFrrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/EWvOs2GoDtEBmK7asZiu3yGYrtNRmK7QAAAAAAAAAAABa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr+haz61wZie2XGYrt/xmK7fAZiu01GYrtAAAAAAAAAAAAFrrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv6GJzsyxmJ7fkZiu3/GYrt8BmK7TUZiu0AGYrtABmK7QAWuuv/Frrr/xa66/8Wuuv/Frrr/xW66/8Vuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Vuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Vuuv/Frrr/xa66/8Wuuv/Frrr/xa56/4YmOz9GYnt/xmK7f8Ziu3wGYrtMhmK7QAZiu0AGYrtABa66/8Wuuv/Frrr/xa66/8Vuuv/Hrzs/yC97P8Vuuv/Frrr/xa66/8Vuuv/Hbzs/yG97P8Vuuv/Frrr/xa66/8Vuuv/HLzr/yG97P8Vuuv/Frrr/xa66/8Wuuv/Frnr/hiY7PwZie3/GYrt/xmK7fgZiu2bGYrtdhmK7T4Ziu0DFrrr/xa66/8Wuuv/FLnr/z3G7v+46vn/wu36/03K8P8Uuev/FLnr/zbD7v+y6Pj/xu76/1bN8P8Uuuv/Fbrr/zDC7f+r5vj/yu/6/1/Q8f8Vuuv/Frrr/xa66/8Wuev+GJjs/BmJ7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt7BmK7W0Wuuv/Frrr/xa66/8Tuev/jt71////////////qub4/xe66/8Suev/gNn0////////////uOr5/xq76/8Suev/ctXz////////////xO76/x+97P8Vuuv/Frrr/xa56/4YmOz8GYnt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt5ha66/8Wuuv/Frrr/xO56/9t1PL/9/3+//z+//+G2/X/Fbrr/xO56/9h0PH/8/v+//7///+T3/b/F7rr/xO56/9VzfD/7vr+//////+f4/f/Gbvr/xa66/8Wuuv/Frnr/hiY7PwZie3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/Frrr/xa66/8Wuuv/Fbrr/x287P9bzvH/YtHy/yO+7P8Vuuv/Frrr/xu86/9WzfH/ZtLy/ya/7P8Vuuv/Frrr/xm76/9SzPD/aNLy/yrA7f8Vuuv/Frrr/xa66/8Wuev+GJjs/BmJ7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Wuuv/Frrr/xa66/8Wuuv/Fbrr/xO56/8Suev/Fbrr/xa66/8Wuuv/Frrr/xO56/8Suev/Fbrr/xa66/8Wuuv/Frrr/xO56/8Suev/Fbrr/xa66/8Wuuv/Frrr/xa56/4YmOz8GYnt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frnr/hiY7PwZie3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuev+GJjs/BmJ7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa56/4YmOz8GYnt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xa66+gWuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wuuv/Frjr/hiV7f0Zie3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/Frrrcha66+4Wuuv/Frrr/xa66/8Wuuv/Frrr/xa66/8Wu+v/Frvr/xa76/8Wu+v/Frvr/xa76/8Wu+v/Frvr/xa76/8Wu+v/Frvr/xa76/8Wu+v/Frvr/xa66/4Xp+z8GYzt/hmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8WuusEFrrrQxa6638WuuuIFrrriBa664gWu+uHF7DrrBek7PoXpOz8F6Ts/Bek7P0XpOz9F6Ts/Rek7P4XpOz+F6Xs/hel7P8Xpez+F6Xs/hel7P0XpOz9GJzs/RmN7f4Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xa66wAWuusAFrrrABa66wAWuusAFrrrABic7AAZiO1NGYnt+hmJ7f8Zie3/GYnt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Zie3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/FrrrABa66wAWuusAFrrrABa66wAWuusAGYrtABmK7U8Ziu37GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZiu0AGYrtTxmK7fsZiu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmK7QAZiu08GYrt9BmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYrtABmK7QwZiu2nGYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt/xmK7f8Ziu3/GYrt9BmK7X0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZiu0AGYrtABmK7RYZiu1vGYrtmxmK7Z0Ziu2dGYrtnBmK7ZwZiu2bGYrtmxmK7ZoZiu2aGYrtmhmK7ZkZiu2ZGYrtmBmK7ZgZiu2XGYrtlxmK7ZYZiu2WGYrtlhmK7Y0Ziu1PGYrtBwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0AGYrtABmK7QAZiu0A+D////gf///4D///+A////gH//8AAADDAAAAAwAAAAMAAAADAAAAAwAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAPwAAAD8AAAA/AAAAPwAAAA='
    with open("chat.ico", "wb") as fh:
        fh.write(base64.decodebytes(img_data))
    root.iconbitmap('chat.ico')


def send(event):
    uname = str(imya.get())
    umsg = str(text2.get())

    if uname != '' and umsg != '':
        text2.set('')
        now_time = time.strftime("%H:%M")
        message = uname + ' (' + str(now_time) + '): ' + umsg
        token = encrypt(encrypt(message.encode(), key), key2)
        zapros = server_route + 'msg.php?msg=' + token.decode()
        requests.get(zapros)
        getmsg(event)
        if uname != now_name:
            open('mishanya_config.txt', 'w').close()
            with open('mishanya_config.txt', 'w', encoding='utf-8') as f:
                f.write(uname)


def getmsg(event):
    text.delete(1.0, END)
    response = requests.get(server_route + 'data.txt')
    r = response.text[:-1]
    l = r.split('\n')
    z = ""
    for i in l:
        if i != '':
            z += decrypt(decrypt(i.encode(), key2), key).decode() + '\n'
    text.insert(1.0, z)
    text.yview(END)


def comanda(event):
    if event.keysym == "F5":
        getmsg(event)


text = Text(width=42, height=25)
text.place(x=0, y=0)
text.configure(font='Arial 11')
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)

response = requests.get(server_route + 'data.txt')
r = response.text[:-1]
l = r.split('\n')
z = ""
for i in l:
    if i != '':
        z += decrypt(decrypt(i.encode(), key2), key).decode() + '\n'
text.insert(1.0, z)
text.yview(END)

l1 = Label(text="I'm", font="Arial 11")
l1.place(x=3, y=440)
imya = StringVar()
text_box = Entry(root, textvariable=imya, width=20)
text_box.place(x=32, y=442)
check_file = os.path.exists('mishanya_config.txt')

now_name = ''

if check_file == True:
    f = open("mishanya_config.txt", "r", encoding="utf-8")
    imya.set(f.read())
    now_name = f.read()
    f.close()
else:
    anon = "Anonymous" + str(random.randint(1, 999))
    now_name = anon
    with open('mishanya_config.txt', 'w', encoding='utf-8') as f:
        f.write(anon)
    imya.set(anon)

text2 = StringVar()
text_box2 = Entry(root, textvariable=text2, width=41)
text_box2.place(x=6, y=470)

b1 = Button(root, text='Send', width=8)
b1.place(x=263, y=466)

b1.bind('<Button-1>', send)
root.bind('<Key>', comanda)
root.bind('<Return>', send)

mainloop()
