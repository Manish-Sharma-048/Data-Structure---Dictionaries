'''
Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
'''

dic = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
li = list(dic.values())
li.sort(reverse = True)

for i in range(3):
    for k,v in dic.items():
            if li[i] == v:
                print('{} {}'.format(k,v))
