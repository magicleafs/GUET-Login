import requests
import tkinter as tk
import sys
import os
import SaveLoginInfo
from tkinter import messagebox


# 自动登录
def AutoLogin():
    global sid, pwd
    m_tuple = SaveLoginInfo.ReadInfo()
    sid = m_tuple[0]
    pwd = m_tuple[1]
    m_var3 = int(m_tuple[4])
    # 判断运营商
    if m_var3 == 2:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "%40cmcc" + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    elif m_var3 == 3:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "%40telecom" + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    elif m_var3 == 4:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "%40unicom" + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    else:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "

    req = requests.get(url)
    req = str(req.text)
    find_str = 'result":1'
    if find_str in req:
        if var4.get() == 1:
            sys.exit()
        else:
            SaveLoginInfo.find_isp2(m_var3)
    else:
        print('登录失败')
        tk.messagebox.showinfo(title='提示', message='登录失败\n账号或密码错误')


# 登陆实现函数
def login():
    global sid, pwd, var1
    sid = u.get()
    pwd = p.get()
    # 判断运营商
    if var3.get() == 2:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "%40cmcc" + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    elif var3.get() == 3:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "%40telecom" + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    elif var3.get() == 4:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "%40unicom" + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    else:
        url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=" + sid + "&upass=" + pwd + "&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=1058&lang=zh "
    req = requests.get(url)
    req = str(req.text)
    find_str = 'result":1'
    if find_str in req:
        SaveLoginInfo.find_isp(var3)
        if var1.get() == 0:
            print('已保存')
            tk.messagebox.showinfo(title='提示', message='已保存')
            SaveLoginInfo.SaveInfo(sid, pwd, var1.get(), var2.get(), var3.get(), var4.get())
    else:
        print('登录失败')
        tk.messagebox.showinfo(title='提示', message='登录失败\n账号或密码错误')


window = tk.Tk()
window.title("桂电网络登录认证")
window.geometry("400x300")  # 窗口大小

sid = '?'
l1 = tk.Label(text="账号:")
l1.pack()
u = tk.StringVar()
number = tk.Entry(window, textvariable=u)
number.pack()

pwd = '?'
l2 = tk.Label(text="密码:")
l2.pack()
p = tk.StringVar()
password = tk.Entry(window, show="*", textvariable=p)
password.pack()

var1 = tk.IntVar()
Save = tk.Checkbutton(window, text='保存密码', variable=var1, onvalue=0, offvalue=1)  # 保存密码复选框
Save.pack()

var2 = tk.IntVar()
Autologin = tk.Checkbutton(window, text='自动登录', variable=var2, onvalue=1, offvalue=0)
Autologin.pack()

var4 = tk.IntVar()
AutoExit = tk.Checkbutton(window, text='登录成功后退出', variable=var4, onvalue=1, offvalue=0)
AutoExit.pack()

"""
t = tk.Text(window,height=2)
t.pack()
"""
l3 = tk.Label(text="选择运营商（默认校园网）:")
l3.pack()

var3 = tk.IntVar()
if SaveLoginInfo.isExist():
    var4.set(SaveLoginInfo.Read_Var4())
    var2.set(SaveLoginInfo.Read_Var2())
    var3.set(SaveLoginInfo.Read_Var3())
    if var2.get() == 1:
        AutoLogin()

isp1 = tk.Radiobutton(window, text='校园网', variable=var3, value=1)
isp1.pack(side='left')

isp2 = tk.Radiobutton(window, text='中国移动', variable=var3, value=2)
isp2.pack(side='right')

isp3 = tk.Radiobutton(window, text='中国电信', variable=var3, value=3)
isp3.pack(side='left')

isp4 = tk.Radiobutton(window, text='中国联通', variable=var3, value=4)
isp4.pack(side='right')

b = tk.Button(window, text="登入网络", bg="green", command=login)  # 登录按钮
b.pack()
b2 = tk.Button(window, text="一键重置", bg="red", command=SaveLoginInfo.reset)  # 登录按钮
b2.pack()

window.mainloop()
