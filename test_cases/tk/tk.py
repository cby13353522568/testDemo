import tkinter

win = tkinter.Tk()
win.title("标题")
win.geometry("600x600+200+20")

# 1.标签控件 text文本内容，bg背景色，fg字体颜色，wraplength文本text多宽换行, justify设置换行后的对齐方式，anchor 文本在lable中的位置 n北，s，w,e,center,ne
label = tkinter.Label(win, text="hello", bg="pink", fg="red", font=("宋体",20), width=10, height=4, wraplength=30, justify="left", anchor="nw")
label.pack()  #展示

# 2.按钮控件
def func():
    print("PASS")
button = tkinter.Button(win, text="打印按钮", command=func, width=10, height=2)
button2 = tkinter.Button(win, text="关闭按钮", command=win.quit, width=10, height=2)
button.pack()
button2.pack()


# 3.输入控件 show='*' 密文显示，密码框
e = tkinter.Variable()  # 绑定变量, e就相当于输入框内容的对象
entry = tkinter.Entry(win, textvariable=e)
entry.pack()
e.set("请输入：")  # 设置值
print(e.get())  # 取值。 也可用entry.get()，这时候不用绑定变量

# 4.文本控件，显示多行文本
text = tkinter.Text(win, width=50, height=4)
str = 'But at the end of the day, the circumstances of your life -- what you look like, where you come from, how much money you have, what you’ve got going on at home -- none of that is an excuse for neglecting your homework or having a bad attitude in school. That’s no excuse for talking back to your teacher, or cutting class, or dropping out of school. There is no excuse for not trying.'
text.insert(tkinter.INSERT, str)
scroll = tkinter.Scrollbar()  # 创建滚动条
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)  # side放置到窗体哪一侧， fill填充方向
# 绑定滚动条和文本框
scroll.config(command=text.yview)   # 滚动条动控制文本动
text.config(yscrollcommand=scroll.set)   # 文本动控制滚动条动
text.pack()

# 5.多选框
def update():
    message=''
    if l1.get() == True:
        message += 'python\n'
    if l2.get() == True:
        message += 'c\n'
    if l3.get() == True:
        message += 'java\n'
    textCheck.delete(0.0, tkinter.END)  # 清除text中的所有文本。否则会有重复数据
    textCheck.insert(tkinter.INSERT, message)

l1 = tkinter.BooleanVar()  # 绑定变量
l2 = tkinter.BooleanVar()
l3 = tkinter.BooleanVar()
checkbutton1 = tkinter.Checkbutton(win, text='python', variable=l1, command=update)
checkbutton2 = tkinter.Checkbutton(win, text='c', variable=l2, command=update)
checkbutton3 = tkinter.Checkbutton(win, text='java', variable=l3, command=update)
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

textCheck = tkinter.Text(win, width=20, height=3)
textCheck.pack()

# 6.单选框
def choose():
    print(r.get())
r = tkinter.IntVar()  # tkinter.StringVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=choose)
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=choose)
radio1.pack()
radio2.pack()

# 7.列表框控件
lbv = tkinter.StringVar()
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)  # 支持鼠标按下拖动选择，EXTENDED支持shift，ctrl, MULTIPLE 支持多选
lb2 = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack(side=tkinter.LEFT)
lb2.pack(side=tkinter.RIGHT)
for item in ['a','b','c','d']:
    lb.insert(tkinter.END, item)  # 按顺序添加
    lb2.insert(tkinter.END, item)  # 按顺序添加
'''
lb.delete(1,3)  #删除列表中的数据，下标从参数1到参数2，只有一个参数，则删除该下标的数据
lb.select_set(1,4)  # 选中下标从参数1到参数2
lb.select_clear(1,2)  # 取消选中
print(lb.size())   # 列表元素个数
print(lb.get(0,2))  # 取值
print(lb.curselection())  # 当前选中的索引项
print(lb.selection_includes(3))  # 当前索引是否选中
'''

print(lbv.get())
# 绑定事件, 需要传一个事件参数
def selectList(event):
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>", selectList)  # 鼠标左键双击


win.mainloop()