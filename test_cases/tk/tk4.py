import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry("600x600+200+0")

# 绝对布局，所在win的布局
label = tkinter.Label(win, text="绝对布局", bg='red')
label.place(x=30,y=30)

# 相对布局
label2 = tkinter.Label(win, text="相对布局", bg='yellow')
#label2.pack(side=tkinter.RIGHT,fill=tkinter.Y)

# 表格布局
label3 = tkinter.Label(win, text="表格布局1", bg='pink')
label4 = tkinter.Label(win, text="表格布局2", bg='grey')
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)  #  和pack()不能同时用

# <Button-1>  鼠标左键
# <Double_Button-1>  双击左键
# <B1-Motion> 左键移动
# <Enter>  光标进入时发生   <Leave> 光标离开时触发
# <Key> 键盘响应
def func(event):
    print("event.char:",event.char)
    print("event.keycode:",event.keycode)
label4.focus_set()  # 设置焦点,小控件不设置焦点 不行
label4.bind("<Key>",func)
# 特殊按键  <Return> 回车  <F5>  <BackSpace> 退格
# 响应 某一按键   label4.bind("a",func) 响应a按键



win.mainloop()