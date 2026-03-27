# 绝对路径 E://user/hello/main.py
# 相对路径 ./main.py

with open('./text.txt', mode='r', encoding='utf-8') as stream:
    content = stream.read()
    print(content)

# content = None
# stream = open(file='./text.txt', mode='r', encoding='utf-8')
# print(stream)
# content = stream.read()
# print(content)
# recode='dsadfasfdafda'
# stream.write(recode)
# stream.close()

# import os

# print(os.getcwd())
# result = os.listdir(os.getcwd())
# print(result)

# os.mkdir('images')
# import time, datetime

# t1=time.time()
# print(t1)
# print(time.ctime(t1))

# print(datetime.datetime.now())

# for i in range(5):
#     print(i)
#     time.sleep(1)


# import harry as hy
# print(hy.name)
# hy.fight()
#
# c=hy.Course('哈利')
# c.add_course('黑魔法防御术')
# print(c.name)
# print(c.c_list)
# ***********************************************
# from harry import *
#
# print(name)
# fight()
#
# c=Course('哈利')
# c.add_course('黑魔法防御术')
# print(c.name)
# print(c.c_list)
