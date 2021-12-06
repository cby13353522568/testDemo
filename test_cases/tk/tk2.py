import tkinter

win = tkinter.Tk()
win.title("标题2")
win.geometry("600x600+200+0")

# 8.Scale 供用户拖拽指示器改变变量的值（音量）
# from_, to 起始和终止。 orient方向，默认竖直。tickinterval 选择值为该值的倍数
scale = tkinter.Scale(win, from_=0, to=100,orient=tkinter.HORIZONTAL, length=200, tickinterval=10)
scale.pack()
scale.set(20)  # 设置初始值
tkinter.Button(win, text="获取值",command=lambda:print(scale.get())).pack()

# 9.Spinbox 数值范围控件，会带个加减号
# increment 步长，默认1。 values 可选值，元组
spinboxE = tkinter.Variable()  # 绑定变量，spinbox没有set方法。
spinbox = tkinter.Spinbox(win, from_=0, to=100, increment=5, textvariable=spinboxE)
spinbox2 = tkinter.Spinbox(win, values=(2,4,6,8,10))
spinbox.pack()
spinbox2.pack()

spinboxE.set(20)
print(spinboxE.get(),spinbox.get())

# 10.Menu 顶层菜单
menubar = tkinter.Menu(win)
win.config(menu=menubar)
# 创建菜单选项，for 像菜单选项添加内容
menu1 = tkinter.Menu(menubar, tearoff=False)
for item in ['a','b','c','q']:
    if item == 'q':
        menu1.add_separator()  # 添加分割线
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item, command=lambda:print("11"))
#像菜单条添加菜单选项
menubar.add_cascade(label="字母",menu=menu1)

# 右键菜单
menubar_right = tkinter.Menu(win)
menu_right = tkinter.Menu(menubar_right, tearoff=False)
for item in ['a','b','c','q']:
    menu_right.add_command(label=item)
menubar_right.add_cascade(label="右键菜单", menu=menu_right)
def showMenuRight(event):
    menubar_right.post(event.x_root, event.y_root)
win.bind("<Button-3>",showMenuRight)


# 11.combobox 下拉控件
from tkinter import ttk
comboboxE = tkinter.Variable()
combobox = ttk.Combobox(win,textvariable=comboboxE)
combobox.pack()
combobox["value"] = ("你","我","他") # 设置下拉数据
combobox.current(1) #设置默认值
# 绑定事件 也可用combobox.get()
combobox.bind("<<ComboboxSelected>>",lambda x:print(comboboxE.get()))



win.mainloop()