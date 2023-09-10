# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#

# Exercises

# Lists
list1: list[str] = ['apple', 'orange', 'banana', 'strawberry']
print(list1)

list2 = ['apple', [2, 4, 6], 'orange', 'banana']
print(list2)

# print(list1[3])

# list in list - the order is the same for the second list, starting with 0
# print(list2[1][2])

# reverse
# print(list1[-1])

# Append
# list1.append('lemon')
# print(list1)

# Insert
# list1.insert(1,'lemon')
# print(list1)

# Extend
# list1.extend(list2)
# print(list1)

# list1.extend(['watermelon', 'guava'])
# print(list1)

# Index
# print(list1.index('apple'))
# or
# list1.index('apple')
# print(list1)

# Reverse
# list1.reverse()
# print(list1)

# Slices
# print(list1[1:3]) # elem 1 and second, because the last one does not show
# print(list2[0:2]) # elem 0 and second, because the last one does not show

# print(list1[3:])

# Sort
# list1.sort()
# print(list1)

# Remove
# list1.remove('banana')
# print(list1)

# Delete an element from a list
# del list1[1]
# print(list1)

#  POP same as Delete
# print(list1.pop(1))
# print(list1)
# or
# list1.pop(1)
# print(list1)

# CLEAR - deletes all the elements from a list
# list2.clear()
# print(list2)

# COUNT - counts the no of times our elem is visible in a list
# print(list1.count('apple'))

# Tuples
# tup1 = ('apple', 'orange', 'banana', 'lemon')
# print(tup1)
#
# tup2 = ('apple')
# print(type(tup2)) # this is a string
# tup2 = ('apple',)
# print(tup2)
# print(type(tup2))

# Index
# print(tup1[0])
# or
# print(tup1.index('lemon'))

# Append in list/tuples
# y=list(tup1)
# y.append('guava')
# tup1=tuple(y) # assigned the y list to tup1
# print(tup1)

# Adding a tuple to a tuple
# tup3=('cherry',)
# tup1+=tup3
# print(tup1)

# FOR
# for x in tup1:
#     print(x)

# Reverse
# print(tup1[-1])

# Slicing
# print(tup1[1:3])

# Repeat
# print(tup1*3)

# print(('repeat',)*2)

# Count
# print(tup1.count('apple'))

# Dictionaries
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# print(dict1)
# dict2 = {1:'apple', 2:'orange', 3:'cherry'}
# print(dict2)

# Methods:

# Clear
# dict1.clear()
# print(dict1)

# Get
# dict1.get(keyname)
# print(dict2.get(3))

# Keys
# dict1.keys()
# print(dict2[2])
# print(dict2.keys)

# Pop
# dict1.pop(keyname)
# print(dict2.pop(1))
# print(dict2)
# or
# dict2.pop(1)
# print(dict2)

# Popitem - removes the last item
# dict1.popitem()
# dict2.popitem()
# print(dict2)

# Len - length
# print(len(dict2))

# Sorted
# print(sorted(dict2))

# Showing values
# print(dict2.values())
# or
# for x in dict2:
#     print(dict2[x])

# Update
# dict2.update({1:'watermelon'})
# print(dict2)
# or
# dict2.update({4:'kiwi'})
# print(dict2)

# Showing the keys and values
# for x, y in dict2.items():
#     print(x,y)

# Copy a dict into another dict
# mydict=dict2.copy()
# print(dict2)

a = {'nume': 'George','filme': ['Shrek', 'Bond', 'Fight Club']}
print(a)

b = {'nume': 'Cristian','filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']}
print(b)

c = {'nume': 'Stefan','filme': ['Fight Club', 'Slumdog Milionare']}
print(c)

for key_common(r, s, t):
    for i in r.keys():
        for j in s.keys():
            for n in t.keys():
                if i==j==n:
                    print(i, 'is indedified as the common key')
a = {'nume': 'George','filme': ['Shrek', 'Bond', 'Fight Club']}
b = {'nume': 'Cristian','filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']}
c = {'nume': 'Stefan','filme': ['Fight Club', 'Slumdog Milionare']}
key_common(a, b, c)







