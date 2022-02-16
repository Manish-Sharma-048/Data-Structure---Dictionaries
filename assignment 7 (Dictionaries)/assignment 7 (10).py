'''
Write a Python program to remove a key from a dictionary.
'''

d = {1:10, 2:20, 3:30, 4:40, 5:50}
k = int(input("Enter the key number you wish to remove: "))

if k in d:
    d.pop(k)
    print("Key has been removed")
else:
    print("Key doesn't exist")
