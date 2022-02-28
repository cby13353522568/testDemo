from xml.dom.minidom import parse
import xml.dom.minidom

dom = parse('./config.xml')  # 打开xml文件

root = dom.documentElement  # 获取文档对象元素
print(root.toxml())
tagNames = root.getElementsByTagName('bananer')   # nodeName为结点名字。
for i in range(len(tagNames)):
    if tagNames[i].nodeType == tagNames[i].ELEMENT_NODE:  # tag.TEXT_NODE:
        print(tagNames[i].childNodes[0].data)
    #for node in tag.childNodes:
        #print(node)

