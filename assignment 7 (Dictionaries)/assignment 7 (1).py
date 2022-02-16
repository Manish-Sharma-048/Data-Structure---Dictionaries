'''
Write a Python script to sort (ascending and descending) a dictionary by key.
'''

choice = input("For ascending order enter ASC and for descending order enter DESC: ") 
d = {1:10, 5:50, 6:60, 2:20, 4:40, 3:30}
li = list(d.keys())

if (choice == 'ASC'):
    li.sort()
elif (choice == 'DESC'):
    li.sort(reverse = True)
    
for i in range(len(d)):
    for k,v in d.items():
            if li[i] == k:
                print('{} {}'.format(k,v))
