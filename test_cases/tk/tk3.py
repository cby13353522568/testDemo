import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("标题3")
win.geometry("600x600+200+0")

# 12.容器控件
frm = tkinter.Frame(win)
frm.pack()

frm_l = tkinter.Frame(frm)
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_l, text="左上",bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右上",bg='blue').pack(side=tkinter.TOP)

frm_l.pack(side=tkinter.LEFT)
frm_r.pack(side=tkinter.RIGHT)

# 表格数据
table = ttk.Treeview(win)
table.pack()
table["columns"] = ("姓名","年龄","性别")  # 定义列
table.column("姓名", width=100)  # 设置列，这时候列还不展示
table.column("年龄", width=100)
table.column("性别", width=100)
table.heading("姓名",text="姓名") # 表头
table.heading("年龄",text="年龄")
table.heading("性别",text="性别")
table.insert("", 0, text="line1", values=('崔','22','男'))  # 添加数据
table.insert("", 1, text="line2", values=('云','21','女'))

# 树状数据
tree = ttk.Treeview(win)
tree.pack()
# 添加一级树枝
tree1 = tree.insert("", 0, text="中国", values=("F1"))
tree2 = tree.insert("", 1, "first2", text="英国", values=("F2"))
# 添加二级树枝
tree1_1 = tree.insert(tree1, 0, "second1_1",text="江苏")
tree1_2 = tree.insert(tree1, 1, "second1-2",text="安徽")
tree2_1 = tree.insert(tree2, 0, "second2_1",text="纽约")
def viewCity(event):
    item = tree.selection()
    name = tree.item(item, "text")
    print(item,name)
tree.bind('<Double-1>', viewCity)



win.mainloop()