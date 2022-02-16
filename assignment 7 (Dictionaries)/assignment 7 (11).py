'''
Write a Python program to map two lists into a dictionary.
'''

li = [1,2,3,4,5,6,7]
li2 = [10,20,30,40,50,60,70]
dic = {}

for i in range(len(li)):
    dic[li[i]] = li2[i]

print(dic)
