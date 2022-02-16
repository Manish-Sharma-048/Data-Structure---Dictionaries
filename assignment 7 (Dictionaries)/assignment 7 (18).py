'''
Write a Python program to match key values in two dictionaries. 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
'''

d1 = {'key1':1, 'key2':3, 'key3':2}
d2 = {'key1': 1, 'key2': 2}

for k in d1:
    if k in d2:
        print(k,":",d1[k], "is present in both d1 and d2")
    else:
        print(k,":",d1[k], "is not present in either d1 or d2")
