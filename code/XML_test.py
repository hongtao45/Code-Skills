
import xml.etree.ElementTree as ET
import os

def pretty_xml(elem, level=0):
    '''
    XML 文档写入文件的时候
    增加换行符
    '''
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            pretty_xml(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


#! 测试1
root = ET.Element('Root')       # 创建节点


for i in range(5):
    element = ET.Element('Name')
    element.set('age', str(i))
    element.text = 'default'
    root.append(element)

pretty_xml(root)          # 增加换行符
tree = ET.ElementTree(root)     # 创建文档
tree.write('test3.xml', encoding='utf-8', xml_declaration=True)


# #! 测试2
#生成根元素
root=ET.Element("root")
#生成子元素 A
a=ET.Element("A")
#增加元素A的子元素 child1
a_child=ET.SubElement(a,"child1")
a_child.text="I'm child of A"
#增加元素A的子元素 child2
a_child1=ET.SubElement(a,"child2")
#生成子元素B
b=ET.Element("B")
#增加元素B的子元素child1
b_child=ET.SubElement(b,"child1")
b_child.text="I'm child of B"
b_child.set("name","book") #set() 接收的是 key,value 形式

#将a和b 组成一个元组传入extend()方法中，元素 A和B作为根元素的子元素
root.extend((a,b))

pretty_xml(root)
trees=ET.ElementTree(root)
#将trees 写入到文件 test4.xml, 内容为 <root><A><child1>I'm child of A</child1><child2 /></A><B><child1 name="book">I'm child of B</child1></B></root>
trees.write(os.path.join(os.path.dirname(__file__),"test4.xml"))
