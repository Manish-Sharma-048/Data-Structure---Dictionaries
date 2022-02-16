'''
Write a Python program to print a dictionary in table format.
'''

dic = {101:'Maruti',102:'Ford',103:'BMW',104:'Isuzu'}

print("\tCo. code :\t Co. name")

for k,v in dic.items():
    print('\t{}\t:\t {}'.format(k,v))
