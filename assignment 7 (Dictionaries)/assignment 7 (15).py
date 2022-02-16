'''
Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = dict(d2)
d3.update(d1) 

for k, v in d2.items():
    for x, y in d1.items():
        if k == x:
            d3[k]=(v+y)

print(d3)

