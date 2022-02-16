'''
Write a Python program to remove duplicates(based on values) from Dictionary.
'''

dic = {1:10, 2:20, 3:30, 4:40, 5:10, 6:20}

dic2 = {}

for k,v in dic.items():
    if v not in dic2.values():
        dic2[k] = v

print(dic2)
