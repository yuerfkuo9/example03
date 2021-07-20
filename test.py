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
fList=[]
for index in range(len(jokes)): #0-4
    a = jokes[index]['value']['joke']
    a= a.replace(".","").replace('!','').replace(',','').lower().split()
    fList.extend(a)
#print(fList)
result={word:fList.count(word) for word in set(fList)}
print(result)
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