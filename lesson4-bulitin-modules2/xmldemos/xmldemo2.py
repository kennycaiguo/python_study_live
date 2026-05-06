import xml.etree.ElementTree as et

tree = et.parse("student.xml")
root = tree.getroot()
# # 遍历所有学生并打印他们的信息
# for stu in root.findall("student"):
#     rollno = stu.get("rollno") # 获取属性
#     first = stu.find("firstname").text
#     last = stu.find("lastname").text
#     marks = stu.find("marks").text
#     print(f"Student Roll No: {rollno}, Name: {first} {last}, Marks: {marks}")

# 修改信息
# 修改学生信息
for student in root.findall('student'):
    if student.get('rollno') == '101':
        # 修改第一个学生的成绩
        student.find('marks').text = '98'

# 写入到新的XML文件
tree.write('modified_stu.xml')