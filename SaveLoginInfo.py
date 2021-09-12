import tkinter as tk
from tkinter import messagebox
import time
import sys


def SaveInfo(m_sid, m_pwd):
    fp = open("D:/Weblogin.txt", "w")
    sid = m_sid
    pwd = m_pwd
    print(sid, file=fp)
    print(pwd, file=fp)
    fp.close()


def ReadInfo():
    fp = open("D:/Weblogin.txt", "r")
    read_ = fp.read()
    sid = read_[0:read_.find('\n')]
    pwd = read_[read_.find('\n') + 1:len(read_) - 1]


def find_isp(var3):
    flag = var3.get()
    if flag == 2:
        print('登录成功')
        tk.messagebox.showinfo(title='提示', message='登录成功\n当前运营商：中国移动')
    elif flag == 3:
        print('登录成功')
        tk.messagebox.showinfo(title='提示', message='登录成功\n当前运营商：中国电信')
    elif flag == 4:
        print('登录成功')
        tk.messagebox.showinfo(title='提示', message='登录成功\n当前运营商：中国联通')
    else:
        print('登录成功')
        tk.messagebox.showinfo(title='提示', message='登录成功\n当前运营商：校园网')


def AutoExit():
    t = time.time()
    while (time.time() - t) > 100:
        sys.exit()
    else:
        print(time.time())