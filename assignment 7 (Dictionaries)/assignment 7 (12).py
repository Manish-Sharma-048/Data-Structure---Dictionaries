'''
Write a Python program to sort a dictionary by key.
'''

d = {1:10, 5:50, 6:60, 2:20, 4:40, 3:30}
li = list(d.keys())

li.sort()

for i in range(len(li)):
    for k,v in d.items():
        if li[i] == k:
            print('{} {}'.format(k,v))
