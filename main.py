import base64
import os
import requests
import tkinter as tk
import Save_Info
from tkinter import messagebox
import win32api
import win32con
from tkinter import filedialog
from icon import img


# 自动登录
def AutoLogin():
    m_tuple = Save_Info.ReadInfo()
    u.set(m_tuple[0])
    p.set(m_tuple[1])
    var3.set(int(m_tuple[4]))
    login()


def AutoRun():
    if var5.get() == 1 and file_path != "" and ".exe" in file_path:
        name = 'GUET_Login'  # 要添加的项值名称
        path = file_path  # 要添加的exe路径
        # 注册表项名
        KeyName1 = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName1, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
            win32api.RegCloseKey(key)
            print('添加成功！')
        except:
            print('添加失败')

    else:
        name = 'GUET_Login'  # 要添加的项值名称
        # 注册表项名
        KeyName1 = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName1, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegDeleteValue(key, name)
            win32api.RegCloseKey(key)
            print('已移除')
        except:
            print('移除失败')


# 登陆实现函数
def login():
    global sid, pwd
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
        Save_Info.find_isp(var3)
        if var1.get() == 1:
            print('已保存')
            tk.messagebox.showinfo(title='提示', message='已保存')
            Save_Info.SaveInfo(sid, pwd, var1.get(), var2.get(), var3.get(), var4.get(), var5.get())
        else:
            Save_Info.SaveInfo(sid, pwd, var1.get(), var2.get(), var3.get(), var4.get(), var5.get())
    else:
        print('登录失败')
        tk.messagebox.showinfo(title='提示', message='登录失败\n账号或密码错误\n')


# --------------------------------------------------初始化

fp = open(r"D:\Weblogin.txt", "a+")
fp.close()
# tmp = open("tmp.ico", "wb+")
# tmp.write(base64.b64decode(img))
# tmp.close()
window = tk.Tk()
window.title("桂电网络登录认证")
window.geometry("400x300")  # 窗口大小
window.iconbitmap()
"""
l_1 = tk.Label(window, text="选中本程序路径，以此完成启动需要\n")
l_1.place(x=20, y=10)

if Save_Info.isEmpty() == 0:
    if Save_Info.Read_path() == 0:
        Save_Info.save_path()
        file_path = Save_Info.Read_path()
    else:
        file_path = Save_Info.Read_path()
else:
    file_path = filedialog.askopenfilename()

l_1.destroy()
"""
# ---------------------------------------------------
l1 = tk.Label(window, text="账号:")
l1.place(x=100, y=10)

u = tk.StringVar()
number = tk.Entry(window, textvariable=u)
number.place(x=140, y=10)

l2 = tk.Label(window, text="密码:")
l2.place(x=100, y=40)
p = tk.StringVar()
password = tk.Entry(window, show="*", textvariable=p)
password.place(x=140, y=40)

var1 = tk.IntVar()
Save = tk.Checkbutton(window, text='保存密码', variable=var1, onvalue=1, offvalue=0)  # 保存密码复选框
Save.place(x=10, y=70)

var2 = tk.IntVar()
Autologin = tk.Checkbutton(window, text='自动登录', variable=var2, onvalue=1, offvalue=0)
Autologin.place(x=10, y=100)

var4 = tk.IntVar()
AutoExit = tk.Checkbutton(window, text='登录成功后退出', variable=var4, onvalue=1, offvalue=0)
AutoExit.place(x=10, y=130)

var5 = tk.IntVar()
AutoStart = tk.Checkbutton(window, text='开机自启', variable=var5, onvalue=1, offvalue=0)#, command=AutoRun)
AutoStart.place(x=10, y=160)

"""
t = tk.Text(window,height=2)
t.pack()
"""
l3 = tk.Label(text="选择运营商（默认校园网）:")
l3.place(x=240, y=70)

var3 = tk.IntVar()

isp1 = tk.Radiobutton(window, text='校园网', variable=var3, value=1)
isp1.place(x=300, y=100)

isp2 = tk.Radiobutton(window, text='中国移动', variable=var3, value=2)
isp2.place(x=300, y=130)

isp3 = tk.Radiobutton(window, text='中国电信', variable=var3, value=3)
isp3.place(x=300, y=160)

isp4 = tk.Radiobutton(window, text='中国联通', variable=var3, value=4)
isp4.place(x=300, y=190)

b = tk.Button(window, text="登入网络", bg="green", command=login)  # 登录按钮
b.place(x=170, y=150)
b2 = tk.Button(window, text="一键重置", bg="red", command=Save_Info.reset)  # 清除按钮
b2.place(x=170, y=270)

if Save_Info.isExist():
    if Save_Info.isEmpty() == 0:
        var1.set(Save_Info.Read_Var1())
        var4.set(Save_Info.Read_Var4())
        var2.set(Save_Info.Read_Var2())
        var3.set(Save_Info.Read_Var3())
        var5.set(Save_Info.Read_Var5())
    if var1.get() == 1:
        m_tuple2 = Save_Info.ReadInfo()
        u.set(m_tuple2[0])
        p.set(m_tuple2[1])
    if var2.get() == 1:
        if var1.get() == 1:
            AutoLogin()

# os.remove("tmp.ico")
window.mainloop()
