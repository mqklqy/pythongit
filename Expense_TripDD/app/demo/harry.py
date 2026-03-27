name = 'Harry Potter'
age = 10


def fight(tool=None):
    if tool:
        print('在魔法学校驾驶+tool+练习飞行课')
    else:
        print('走到魔法学校就会练习飞行课')


class Course:
    def __init__(self, name, c_list=[]):
        self.name = name
        self.c_list = []

    def add_course(self, c_name):
        if c_name:
            self.c_list.append(c_name)
        else:
            print('选修课不能为空哦')

    def remove_course(self, c_name):
        if c_name:
            self.c_list.remove(c_name)
        else:
            print('选修课不能为空啊')

# sites = ["Baidu", "Google", "Runoob", "Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!"+ site)
#         break
#     else:
#         print("循环数据2 " + site)
#         continue
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")


# sample_dict = {
#     "name": "张三",
#     "age": 25,
#     "city": "北京"
# }
# print(sample_dict)
# print(sample_dict.keys())
# print(sample_dict.values())
# print(sample_dict.items())
# print(sample_dict.get("city"))

# heros=['aaa','bbb','CCC','ddd']
# # print(type(heros))
# # print(len(heros))
# # print('CCC' in heros)
# # # print(heros[2::2])


# print("张三", "李四", sep="\n")
# name = input("请输入一个帐号")
# password = input("请输入一个密码")
# print(name, password)
# name='哈哈哈'
# amount =2.323232
# print(amount)
# # print(type(amount))

# money = float(input('你有多少钱？'))
#
# number = int(input('你想要多少盲盒?（35元/个）'))
#
# if money >= 35 * number:
#     print('买到{}个盲盒'.format(number))
# # elif 1==1 :
# #     print('aaaa')
# else:
#     print('买不到你想要的{}个盲盒'.format(number))


# if money != 35 * number:
#     print('aaaa')
