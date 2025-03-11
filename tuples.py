'''In Python, a tuple is a built-in data structure that allows you to store a collection of items. Unlike lists, tuples are immutable, meaning that once a tuple is created, you cannot modify its elements. Tuples are ordered, and they can store elements of different data types.'''

#tuple is a collection of items separated by commas and enclosed within parentheses.
# A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
# A tuple can also have a single item, but it should be followed by a comma.
# Tuples are immutable, meaning that once a tuple is created, you cannot modify its elements.
# Tuples are ordered, meaning that the items in a tuple have a specific order.
# Tuples can store elements of different data types.
# Tuples can have nested tuples, lists, dictionaries, sets, etc.
# Tuples are faster than lists because they are immutable.
# Tuples are used to store related pieces of information that should not be modified, such as the coordinates of a point on a graph.
# Tuples are used to return multiple values from a function.
# Tuples are used as keys in dictionaries because they are immutable.
# Tuples are used as elements of a set because they are immutable.
# Tuples are used to store fixed-size data records.
# Tuples are used to store the values of a matrix.
# Tuples are used to store the values of a polynomial.
# Tuples are used to store the values of a vector.
# Tuples are used to store the values of a complex number.
# Tuples are used to store the values of a color.
# Tuples are used to store the values of a date and time.
# Tuples are used to store the values of a point in a three-dimensional space.
# Tuples are used to store the values of a rectangle.
# Tuples are used to store the values of a circle.
# Tuples are used to store the values of a triangle.
# Tuples are used to store the values of a polygon.



#-------------------------------------- Tuple --------------------------------------
print('-------------------------------------- Tuple --------------------------------------')

# Create a tuple
tuple1 = ('apple', 'banana', 'orange')
tuple2 = (1, 2, 3, 4)
tuple_with_all_datatypes = (1, 'hello', 2.9, True)
print(tuple1)
print(tuple2)
print(f"Tuple with all data types: {tuple_with_all_datatypes}")

#-------------------------------------- Tuple Conditional statement --------------------------------------
print('-------------------------------------- Tuple Conditional statement --------------------------------------')

# We can use the 'in' operator to check if an item is present in the tuple or not
if 'banana' in tuple2:
    print('Yes')
else:
    print('No')


#-------------------------------------- Tuple Length --------------------------------------
print('-------------------------------------- Tuple Length --------------------------------------')

# Check the tuple length
print(len(tuple1))
print(len(tuple2))
print(len(tuple_with_all_datatypes))


#-------------------------------------- Tuple Index Method --------------------------------------
print('-------------------------------------- Tuple Index Method --------------------------------------')

# Find the index of the item
print(tuple1.index('banana'))
print(tuple2.index(3))

#-------------------------------------- Tuple Count Method --------------------------------------
print('-------------------------------------- Tuple Count Method --------------------------------------')

# Count the number of occurrences of an item
tuple3 = (1, 2, 3, 4, 1, 2, 1)
print(f"count: {tuple3.count(1)}")

#-------------------------------------- Tuple Slicing --------------------------------------
print('-------------------------------------- Tuple Slicing --------------------------------------')

# Slicing
tuple4 = (1, 2, 3, 4, 5, 6, 7)
print(tuple4[1:5])  

#slice without specifying the start index
print(tuple4[:3])

#slice without specifying the end index
print(tuple4[4:])

# slice without specifying the start and end index
print(tuple4[:])

#reverse the tuple using slicing
print(tuple4[::-1])

#if you give a collection of values separated by commas, Python will automatically create a tuple
example = 1, 2, "vanakkam"
print(f"example: {example}")

#convert a list to a tuple
list1 = [1, 2, 3]
tuple5 = tuple(list1)
print(f"tuple5: {tuple5}")

#-------------------------------------- Tuple indexing --------------------------------------
print('-------------------------------------- Tuple indexing --------------------------------------')

# Indexing
tuple6 = (1, 2, 3, 4, 5)
print(tuple6[2])  

#we can give a negative index to access the elements from the end of the tuple
print(tuple6[-1])


#we cannot update the elements of a tuple
# tuple6[2] = 10  # This will raise an error
print(tuple6)


#-------------------------------------- Tuple Iteration --------------------------------------
print('-------------------------------------- Tuple Iteration --------------------------------------')

# Iterating through a tuple

for item in tuple6:
    print(item)


#-------------------------------------- Tuple Concatenation --------------------------------------
print('-------------------------------------- Tuple Concatenation --------------------------------------')

# Concatenation
tuple7 = (1, 2, 3)
tuple8 = (4, 5, 6)

concatenated_tuple = tuple7 + tuple8
print(f"catenated_tuple: {concatenated_tuple}")


#-------------------------------------- Tuple Unpacking --------------------------------------
print('-------------------------------------- Tuple Unpacking --------------------------------------')

# Unpacking
first, second, third = (1, False, "vvvv")
print(f"first: {first}")
print(f"second: {second}")
print(f"third: {third}")


#-------------------------------------- Tuple Comprehension --------------------------------------
print('-------------------------------------- Tuple Comprehension --------------------------------------')

# Tuple comprehension
tuple9 = (i for i in range(10))
print(tuple9)  # Output: <generator object <genexpr> at 0x000001F3A3C3F200>


#-------------------------------------- Tuple Methods --------------------------------------
print('-------------------------------------- Tuple Methods --------------------------------------')

# directory Methods
tuple10 = (1, 2, 3, 4, 5)
print(dir(tuple10))

#-------------------------------------- Tuple Packing --------------------------------------
print('-------------------------------------- Tuple Packing --------------------------------------')

# Tuple packing
tuple11 = 1, 2, 3, 4, 5
print(tuple11)

#-------------------------------------- Tuple Unpacking --------------------------------------
print('-------------------------------------- Tuple Unpacking --------------------------------------')

# Tuple unpacking
first, second, third, fourth, fifth = tuple11
print(f"first: {first}")
print(f"second: {second}")
print(f"third: {third}")
print(f"fourth: {fourth}")

#-------------------------------------- Tuple with one element --------------------------------------
print('-------------------------------------- Tuple with one element --------------------------------------')

# Tuple with one element
tuple12 = (1,)
print(tuple12)


#-------------------------------------- Tuple without parentheses --------------------------------------
print('-------------------------------------- Tuple without parentheses --------------------------------------')

# Tuple without parentheses
tuple13 = 1, 2, 3
print(tuple13)


#-------------------------------------- Tuple with multiple data types --------------------------------------
print('-------------------------------------- Tuple with multiple data types --------------------------------------')

# Tuple with multiple data types
tuple14 = (1, 'hello', 2.9, True)
print(tuple14)


#-------------------------------------- Tuple with nested tuples --------------------------------------

# Tuple with nested tuples
tuple15 = (1, 2, (3, 4), (5, 6, (7, 8)))

# Accessing the elements of the nested tuple
print(tuple15[2][1])
print(tuple15[3][2][1])


#-------------------------------------- Tuple with nested lists --------------------------------------
print('-------------------------------------- Tuple with nested lists --------------------------------------')

# Tuple with nested lists
nested_list_tuples = ([1, 2,3], [4, 5, 6], [7, 8, 9])
print(f"nested_list_tuples: {nested_list_tuples}")

# Accessing the elements of the nested list
print(nested_list_tuples[0][1])

#-------------------------------------- Tuple with nested dictionaries --------------------------------------
print('-------------------------------------- Tuple with nested dictionaries --------------------------------------')

# Tuple with nested dictionaries
nested_dict_tuples = ({'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30})
print(f"nested_dict_tuples: {nested_dict_tuples}")

# Accessing the elements of the nested dictionary
print(nested_dict_tuples[1]['age'])


#-------------------------------------- Tuple with nested sets --------------------------------------
print('-------------------------------------- Tuple with nested sets --------------------------------------')

# Tuple with nested sets
nested_set_tuples = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9})
print(f"nested_set_tuples: {nested_set_tuples}")

# Accessing the elements of the nested set
print(nested_set_tuples[2])

#-------------------------------------- Tuple with nested tuples --------------------------------------
print('-------------------------------------- Tuple with nested tuples --------------------------------------')

# Tuple with nested tuples
nested_tuple_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"nested_tuple_tuples: {nested_tuple_tuples}")

# Accessing the elements of the nested tuple
print(nested_tuple_tuples[1][2])




#-------------------------------------- compare the list and tuple --------------------------------------



import sys

list1 = [1, True, 'hello', 3.14]
tuple1 = (1, True, 'hello', 3.14)

print(sys.getsizeof(list1), "bytes")  
print(sys.getsizeof(tuple1), "bytes")


#-------------------------------------- check the time it --------------------------------------
print('-------------------------------------- check the time it --------------------------------------')

import timeit

list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print(f"List time: {list_time}")
print(f"Tuple time: {tuple_time}")
