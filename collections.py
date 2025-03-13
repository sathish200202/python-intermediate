'''In Python, the collections module is a built-in module that implements specialized container datatypes beyond the core Python data structures like list, tuple, dict, and set. These container datatypes offer additional functionality and improve performance for specific use cases. The collections module contains several useful classes and functions to make working with data more efficient and expressive.'''

#Counter, deque (Double-Ended Queue), defaultdict, OrderedDict, namedtuple, ChainMap


#--------------------------------------------------------------- Counter ---------------------------------------------------------------
print('--------------------------------------------------------------- Counter ---------------------------------------------------------------')

from collections import Counter
#we can get the count of the all char
data = ['apple', 'banana', 'orange','apple', 'banana', 'orange', 'banana']
count = Counter(data)
print(f"Count: {count}")
#if i give a .items()
print(count.items())
print(count.keys())
print(count.values())

#count the particular char
data = ['apple', 'banana', 'orange','apple', 'banana', 'orange', 'banana']
count = Counter(data)
print(f"banana Count: {count['banana']}")

#not only list, e can use string and any data types
data = "hello world, welcome to the world"
count = Counter(data)
print(f"String Count: {count}")

data = (1, 2, 1, 2, 3, 5, 8, 8, 5)
count = Counter(data)
print(f"Count: {count}")


#most common method
data = "hello world, welcome to the world"
count = Counter(data)
print(f"most common: {count.most_common(2)}") #2 -- its used to get the how many are most common
#access the element
print(f"most common using index: {count.most_common(2)[0]}")
print(f"most common using index: {count.most_common(2)[0][0]}") 

