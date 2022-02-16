'''
Write a Python script to add an item to a dictionary
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

s_d = {0:10, 1:20}
n_i = {2:30}

s_d.update(n_i)

print(s_d)
