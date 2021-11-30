from tkinter import messagebox, filedialog
import time
import sys
import os
import base64


# 保存相关信息
def SaveInfo(m_sid, m_pwd, m_var1, m_var2, m_var3, m_var4, m_var5):  # , file_path):
    fp = open(r"D:\Weblogin.txt", "w")
    sid = m_sid
    pwd = m_pwd
    var1 = m_var1
    var2 = m_var2
    var3 = m_var3
    var4 = m_var4
    var5 = m_var5
    # path = file_path
    print(sid, file=fp)
    print(pwd, file=fp)
    print(var1, file=fp)
    print(var2, file=fp)
    print(var3, file=fp)
    print(var4, file=fp)
    print(var5, file=fp)
    # print(path, file=fp)
    fp.close()


def save_path():
    path_ = filedialog.askopenfilename()
    fp = open(r"D:\Weblogin.txt", "a+")
    print(path_, file=fp)
    fp.close()


def ReadInfo():
    fp = open(r"D:\Weblogin.txt", "r")
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
    var5 = fp.readline()
    var5 = var5.strip('\n')
    read_result = [sid, pwd, var1, var2, var3, var4, var5]
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


def Read_Var5():
    return int(ReadInfo()[6])


def Read_Var4():
    return int(ReadInfo()[5])


def Read_Var3():
    return int(ReadInfo()[4])


def Read_Var2():
    return int(ReadInfo()[3])


# def Read_File_path():
# return ReadInfo()[7]


def isExist():
    return os.path.isfile(r'D:\Weblogin.txt')


def isEmpty():
    fp = open(r"D:\Weblogin.txt", "r")
    sid = fp.readline()
    fp.close()
    if os.path.getsize(r"D:\Weblogin.txt") == 0:
        return 1
    else:
        return 0


def reset():
    os.system(r'del D:\Weblogin.txt')





def Read_Var1():
    if isExist():
        if isEmpty() == 0:
            return int(ReadInfo()[2])


def Read_path():
    with open(r"D:\Weblogin.txt", 'r') as x:
        lines = x.readlines()
    try:
        lines[7] = lines[7].strip('\n')
        x.close()
        return lines[7]
    except:
        return 0


def start_run(path_):
    shell = 'shell:start '+ path_
    print(shell)
    return shell
"""
对图片进行转码，否则打包后的文件无法使用
open_icon = open("denglu.ico", "rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = %s" % b64str
f = open("icon.py", "w+")
f.write(write_data)
f.close()
"""
