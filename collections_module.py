'''In Python, the collections module is a built-in module that implements specialized container datatypes beyond the core Python data structures like list, tuple, dict, and set. These container datatypes offer additional functionality and improve performance for specific use cases. The collections module contains several useful classes and functions to make working with data more efficient and expressive.'''

#Counter, deque (Double-Ended Queue), defaultdict, OrderedDict, namedtuple, ChainMap


#--------------------------------------------------------------- Counter ---------------------------------------------------------------
print('--------------------------------------------------------------- Counter ---------------------------------------------------------------')

from collections import Counter, namedtuple, OrderedDict

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

#the .elements() method of a Counter object returns an iterator over elements in the counter, repeating each element as many times as it was counted.
print(f"Element method: {list(count.elements())}")



#--------------------------------------------------------------- namedtuple ---------------------------------------------------------------
print('------------------------------------------------------ namedtuple ---------------------------------------------------------')

'''"namedtuple" is a convenient way to create immutable objects with named fields, enhancing code readability and preventing errors.
It is especially useful when working with structured data that you want to treat like a lightweight class without the overhead of defining a full class.'''

#create a instance for the namedtuple
Point = namedtuple("Point", "a, b") #Point is a class
pt = Point(1, 3)#pass the arguments
print(f"get the class and feilds using the namedtuple: {pt}")

#Access the value
print(f"Access the a values: {pt.a}")
print(f"Access the b values: {pt.b}")


#--------------------------------------------------------------- Ordereddict ---------------------------------------------------------------
print('------------------------------------------------------ Ordereddict ---------------------------------------------------------')

'''An OrderedDict is a class from the collections module in Python that is similar to a regular dict, but with the added feature that it maintains the order in which items are inserted. In a standard Python dictionary (prior to Python 3.7), the order of items was not guaranteed. However, starting from Python 3.7, the built-in dict also preserves the insertion order, but OrderedDict provides some additional methods and functionality.'''

ordered_dict = OrderedDict()
ordered_dict['a'] = 6
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
ordered_dict['f'] = 1
print(f"ordered_dict: {ordered_dict}")

