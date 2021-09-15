from tkinter import messagebox
import time
import sys
import os.path


# 保存相关信息
def SaveInfo(m_sid, m_pwd, m_var1, m_var2, m_var3, m_var4):
    fp = open("D:/Weblogin.txt", "w")
    sid = m_sid
    pwd = m_pwd
    var1 = m_var1
    var2 = m_var2
    var3 = m_var3
    var4 = m_var4
    print(sid, file=fp)
    print(pwd, file=fp)
    print(var1, file=fp)
    print(var2, file=fp)
    print(var3, file=fp)
    print(var4, file=fp)
    fp.close()


def ReadInfo():
    fp = open("D:/Weblogin.txt", "r")
    sid = fp.readline()
    sid.strip('\n')
    sid = sid.strip('\n')
    pwd = fp.readline()
    pwd = pwd.strip('\n')
    var1 = fp.readline()
    var1 = var1.strip('\n')
    var2 = fp.readline()
    var2 = var2.strip('\n')
    var3 = fp.readline()
    var3 = var3.strip('\n')
    var4 = fp.readline()
    var4 = var4.strip('\n')
    read_result = [sid, pwd, var1, var2, var3, var4]
    fp.close()
    return read_result


def find_isp(var3):
    import tkinter as tk

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


def Read_Var4():
    return int(ReadInfo()[5])


def Read_Var3():
    return int(ReadInfo()[4])


def Read_Var2():
    return int(ReadInfo()[3])


def isExist():
    return os.path.isfile('D:\Weblogin.txt')


def reset():
    os.system('del D:\Weblogin.txt')


def Read_Var1():
    return int(ReadInfo()[2])