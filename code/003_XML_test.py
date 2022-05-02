
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
def write_test1():
    root = ET.Element('routes')       # 创建节点

    for i in range(5):
        element = ET.Element('flow')
        element.set('id', str(i))
        element.set('id', 'flow'+str(i))
        element.set('begin', str(i))
        element.set('end', str(i))
        element.set('from', 'edge_f'+str(i))
        element.set('to', 'edge_t'+str(i))
        element.set('number', str(i*10))

        element.text = "default_text"
        root.append(element)

    pretty_xml(root)          # 增加换行符

    tree = ET.ElementTree(root)     # 创建文档
    tree.write(os.path.join(os.path.dirname(__file__),'test1.xml')
                , encoding='utf-8', xml_declaration=True)


# #! 测试2
def write_test2():
    root = ET.Element("root")

    a = ET.Element("A")
    a_child1 = ET.SubElement(a, "child1") #增加元素A的子元素 child1
    a_child1.text = "I'm child of A"
    
    a_child2 = ET.SubElement(a,"child2") #增加元素A的子元素 child2
    a_child2.set('name','hahaha_1')
 
    b = ET.Element("B")
    b_child = ET.SubElement(b, "child1")
    b_child.text = "I'm child of B"
    b_child.set("name","book") #set() 接收的是 key,value 形式

    c = ET.Element("C")
    c.set('name', 'name_c')
    c.set('age', 'age_c')
    
   
    #将a和b 组成一个元组传入extend()方法中，元素 A和B作为根元素的子元素
    root.extend((a,b))
    root.append(c)

    pretty_xml(root)
    trees = ET.ElementTree(root)
    #将trees 写入到文件 test4.xml
    trees.write(os.path.join(os.path.dirname(__file__),"test2.xml"))


def read_test1(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    print(root.text)

    for child in root:
        print(child.items)

    # 遍历xml文档的第二层
    for child in root:
        for children in child:
            # 第三层节点的标签名称和属性
            print(children.tag, ":", children.attrib)
            # print(children.tag, ":", children.attrib,children.text)
    # 过滤出所有 z直接和间接的子元素 neighbor标签
    for neighbor in root.iter("neighbor"):
        print(neighbor.tag, ":", neighbor.attrib)

    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(name, rank)



if __name__ == '__main__':

    # write_test1()
    # write_test2()

    read_test1(os.path.join(os.path.dirname(__file__),'country.xml'))