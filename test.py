"作业题"
# import random
# def guessing_game():
#     guess = input("You can choose from numpy,seaborn,pandas,pantab,spacy,requests,tensorflow:")
#     words = ("numpy","seaborn","pandas","pantab","spacy","requests","tensorflow")
#     answer = random.choice(words)
#     if guess in words:
#         for count in range(1, 3):
#             if  guess == answer:
#                 break
#             else:
#                 if guess in words:
#                     guess = input("Try again:")
#                     count + 1
#                 else:
#                     print("THe word is not in Vol")
#         if guess != answer:
#             print("game over")
#         else:
#             print("Correct!Well Done")
#         return
#     else:
#         print("THe word is not in Vol")
#         return
# # 调用函数
# guessing_game()
# str = "42.42525,-98.2514352";
# a = str.split(',') # 以空格为分隔符，分隔成两个
# lat = float(a[0])
# lon = float(a[1])
# print(lat,lon)
# print(type(lon),type(lat))
jokes = [{'type': 'success', 'value': {'categories': ['plain'], 'id': 100, 'joke': 'Chuck Norris grinds his coffee with his teeth and boils the water with his own rage.'}},
         {'type': 'success', 'value': {'categories': ['dad joke'], 'id': 150, 'joke': 'Superman once watched an episode of Walker, Texas Ranger. He then cried himself to sleep.'}},
         {'type': 'success', 'value': {'categories': ['bad joke'], 'id': 250, 'joke': 'The truth will set you free. Unless Chuck Norris has you, in which case, forget it buddy!'}},
         {'type': 'success', 'value': {'categories': ['nerdy'], 'id': 480, 'joke': 'The class object inherits from Chuck Norris'}},
         {'type': 'success', 'value': {'categories': ['nerdy'], 'id': 490, 'joke': "Chuck Norris doesn't need to use AJAX because pages are too afraid to postback anyways."}}]
#aList = []

# fList=[]
# for index in range(len(jokes)): #0-4
#     a = jokes[index]['value']['joke']
#     a= a.replace(".","").replace('!','').replace(',','').lower().split()
#     fList.extend(a)
# #print(fList)
# result={word:fList.count(word) for word in set(fList)}
# print(result)
    #print(a)
    #aList.append(jokes[index]['value']['jokes'])

# print(jokes[index]["value"])
# print(aList)
# str = "12,3abcrunoob321"
# print (str.strip( ',12' ))
# str = "i am your father!And,please";
# print (str.strip());  # 去除首尾字符 0
# list1 = ['A','B','C']
# dict1 = {}
# for i in range(3):
#     order = int(input('你要把'+list1[i]+'放在第几位？（请输入数字1,2,3)'))
#     dict1[order] = list1[i]
# print(dict1)
#
# list1 = []
# # 清空原本列表list1的元素
# for i in range(1,4):
#     list1.append(dict1[i])
# print(list1)

# from collections import Counter
#sentence='i think i can jump you can not jump'
# counts=Counter(sentence.split())
# print(counts)

# sentence='i think i can jump you can not jump'
# a = sentence.split()
# print(a)
# print(type(a))
# result={word:sentence.split().count(word) for word in set(sentence.split())}
# print(result)
"作业题结束"

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

练习1
将华氏温度转换为摄氏温度
"""
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.2f华氏度 = %.1f摄氏度' % (f, c))

"""
练习2
输入圆的半径计算计算周长和面积
"""
# rad = float(input('请输入半径: '))
# zc = 2*3.1415*rad
# mj = 3.1315*rad*rad
# print('周长是%.2f米 , 面积是%.2f平方米' % (zc, mj))

"""
练习3
输入年份 如果是闰年输出True 否则输出False
"""
# year = int(input('请输入年份: '))
# print(year%4 == 0 or year%400 == 0 )