mathScores = [60, 70, 10, 20, 81, 63, 4]
print(mathScores[2])
print(mathScores[1:6])
print(mathScores[-1])
print(mathScores[5:])
print(len(mathScores))
print(sum(mathScores))
print(max(mathScores))
print(min(mathScores))
print(sum(mathScores) / len(mathScores))
mathScores2 = []
print(mathScores2)
mathScores2.append(60)
print(mathScores2)
mathScores2.append(70)
print(mathScores2)
mathScores2.append(50)
print(mathScores2)
mathScores2.append(40)
print(mathScores2)
mathScores2.insert(3, 30)
print(mathScores2)

mathScores2[1] = 55
print(mathScores2)
mathScores2.pop(1)
print(mathScores2)
print(33 in mathScores2)
print(50 in mathScores2)
print(50 not in mathScores2)
mathScores2.append(70)
print(mathScores2)
mathScores2.append(40)
print(mathScores2)
mathScores2.append(70)
print(mathScores2)
print(mathScores2.count(70))
print(mathScores2.index(70))
print(sorted(mathScores2))
print(sorted(mathScores2, reverse=True))
print(mathScores + mathScores2)

grades = [5, 14, 7], [23, 36, 28], [88, 80, 92]
"""數學成績"""

gradesTuple = ([5, 14, 7], [23, 36, 28], [88, 80, 92])
print(gradesTuple[2])
avg1 = (sum(gradesTuple[0]) / len(gradesTuple[0]))
print(avg1)

"""練習3"""
# gradesDict={"chinese":"5,14,7","english":"23,36,28","math":"88,80,92"}
# print(gradesDict["math"])
# print(gradesDict.get('math'))
# age1=(sum(gradesDict['chinese'])/len(gradesDict['chinese']))
# print(age1)
fruits = {
    "apple",
    "banana",
    "guava",
    "guava"
}
fruits1 = {
    "strawberry"
    "papaya"
    "banana"
}
print(fruits | fruits1)
print(fruits & fruits1)
print(fruits - fruits1)
print(fruits)
fruits.add("watermelon")
print(fruits)
fruits.remove("banana")
fruits.remove("apple")
print(fruits)

guitarclub = {"john", "Eva", "jill", "Eric", "Andy"}
dance = {"Andy", "Eric", "Albert", "Polina", "Andy", "Kristin"}
allStudents3 = {"John", "Eva", "Jill", "Eric", "Andy", "Albert", "Polina", "Kristin", "Angela"}
print(guitarclub | dance)
print(guitarclub & dance)


x=3
pi=3.14
print(x**2*pi)

scores=[10,30,40,90,100,61]
average=sum(scores)/len(scores)
average=round(average)
print(average)

score=89
if score >= 60:
    print('及格了')
    if score >=90:
        print('你最棒')
    else:
        print('還好還好')
elif 55 <= score and score <60:
    print('教授拜託個分')
elif 50 <= score < 55:
    print('可誤差一點點')
else:
    print('被當了')

print('Hello','world','!')
print('Hello \nworld\n!')
print('123',end='456\n')
print('456',end='')
print('789')


x=42
print(f'Value of x is {x}')

mathScores = [60,70,10,20,81,63,4]
print(mathScores[0])
firstItem=f'first item in mathScore is {sum(mathScores)/len(mathScores)}'
print(firstItem)


#for i in range(0,10,3):
 #   print(i)

for i in range (len(mathScores)):
    print(i,mathScores[i])


for i in mathScores:
    print(i)


family={
    'dad':'Homer',
    'mom':'Marge',
    'son':'Bart',
    'daughter':'Lisa'
}
for member in family.items():
    print(member)

for key, value in family.items():
    print(f'my {key} is {value}')


import math
mathscores3=[60,70,10,20,81,63,4]
for abc in mathscores3:
    print(math.sqrt(abc)*10)

for i in range(10):
    print(i)
[print(i) for i in range(10)]

mathscores3=[60,70,10,20,81,63,4]
[print(math.sqrt(x)*10)for x in mathscores3]

count= 0
while count<10:
    print(count)
    count +=1
else:
    print('GG')

scores1=[60,70,10,20,81,63,4]
#-----
for score in scores1:
    if score>80:
        continue
    print(score)

for score in scores1:
    if score>80:
        break
    print(score)

import random
i=random.randint(1,99)
print(i)

#rows   = eval(input('How many rows : '))
#print(type(X))



for i in range(1,10):
    for o in range (1,10):
        print(f'{i}*{o}=',i*o)

count=0
while count<5:
    print("你好")
    count +=1
else:
    print('我完成拉')

#num=eval(input('Enter a number'))
#for i in range  (1,num+1):
 #   if i % 2 ==1:
  #      print(i)

# import random
# ls=[]
# rows =eval(input('How many rows:'))
# columns=eval(input('How many columns'))
# for i in range (rows):
#     ls.append([])
#     for j in range (columns):
#         num=random.randint (1,100)
#         ls[i].append(num)
# for row in ls:
#     for value in row:
#         print(f'{value}', end=' ')
#     print()


#ch4
import vending_service as machine
flag=True
while flag:
    print('\n============================')
    select=eval(input('1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇:'))

    if select==1: #儲值
        machine.deposit()
    elif select ==2: #購買
        # 印出品項
        machine.buy()
    elif select==3: #查詢餘額
        print(f'目前餘額為{machine.balance}元')
    elif  select ==4: #離開
        print('bye')
        flag= 0
        break

    else: #重新輸入
        print('====請輸入1-4之間====')
        continue
weight=100
weight1=80
def add_weight(w1,w2=1):
    result=w1+w2
    result1=w1/w2
    return result,result1

# x1,x2=add_weight(weight,weight1)
# print(x1,x2)
#
#
# y1,y2=add_weight(w2=weight,w1=weight1)
# print(y1,y2)


x=1
x1=2
print(x1)

