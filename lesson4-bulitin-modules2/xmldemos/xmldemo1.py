import xml.etree.ElementTree as et

# 1.read xml file
## 1》create a ElementTree object
tree = et.parse("example.xml")
## 2》get the root element
root = tree.getroot()
## 3>iteration
for child in root:
    print(child.tag,child.attrib)
    for c in child:
        print(c.tag,c.attrib,c.text)

