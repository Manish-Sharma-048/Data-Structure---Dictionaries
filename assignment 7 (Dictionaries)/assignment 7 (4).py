'''
Write a Python script to check if a given key already exists in a dictionary.
'''

dic = {1:10, 2:20, 3:30, 4:40, 5:50}

k = int(input("Enter key you wish to check: "))

if k in dic:
    print('Key already exists')
else:
    print("Key doesn't exists")
