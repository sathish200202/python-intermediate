''' In Python, a list is a built-in data structure that allows you to store a collection of items.
Lists are ordered, mutable (i.e., you can change their content), and can contain elements of different data types.'''

'''List:'
Lists are mutable, meaning that you can modify the elements of a list after creating it.
Lists are created using square brackets [] or the list() constructor.
Lists are slower than tuples because they are mutable.
Lists are used when you need to modify the elements of the collection.
 Lists are used when you need to store a collection of items that can change over time.'''

#-------------------------------------- List Conditional statement --------------------------------------
print('-------------------------------------- List Conditional statement --------------------------------------')

# We can use the 'in' operator to check if an item is present in the list or not
list1 = ['apple', 'banana', 'orange']
if 'banana' in list1:
    print('Yes')
else:
    print('No')


#-------------------------------------- List Length --------------------------------------
print('-------------------------------------- List Length --------------------------------------')

# Check the list length
print(len(list1))  # Output: 3

#-------------------------------------- List Append Method --------------------------------------
print('-------------------------------------- List Append Method --------------------------------------')

# Append method adds a new item to the list at the last position
list1.append("lemon")
print(list1)  # Output: ['apple', 'banana', 'orange', 'lemon']

#-------------------------------------- List Insert Method --------------------------------------
print('-------------------------------------- List Insert Method --------------------------------------')

# Insert method inserts the item at the specified index
list1.insert(3, 'grapes')
print(list1)  # Output: ['apple', 'banana', 'orange', 'grapes', 'lemon']

#-------------------------------------- List Pop Method --------------------------------------
print('-------------------------------------- List Pop Method --------------------------------------')

# Pop method removes the last element by default
list1.pop()
print(list1)  # Output: ['apple', 'banana', 'orange', 'grapes']

#-------------------------------------- List Remove Method --------------------------------------
print('-------------------------------------- List Remove Method --------------------------------------')

# Remove method removes the first occurrence of an item
list1.remove('grapes')
print(list1)  # Output: ['apple', 'banana', 'orange']

#-------------------------------------- List Clear Method --------------------------------------
print('-------------------------------------- List Clear Method --------------------------------------')

# Clear method removes all items from the list
list1.clear()
print(list1)  # Output: []

#-------------------------------------- List Index Method --------------------------------------
print('-------------------------------------- List Index Method --------------------------------------')

# Find the index of the item
list2 = ['apple', 'banana', 'orange']
print(list2.index('apple'))  # Output: 0

#-------------------------------------- List Count Method --------------------------------------
print('-------------------------------------- List Count Method --------------------------------------')

# Count method counts the number of times the item is present in the list
list2 = ['apple', 'banana', 'orange', 'apple']
print(list2.count('apple'))  # Output: 2

#-------------------------------------- List Sort Method --------------------------------------
print('-------------------------------------- List Sort Method --------------------------------------')

# Sort method sorts the list in ascending order
list3 = [4, 3, 2, 1, -8, 1, 2, 5]
list3.sort()
print(list3)  # Output: [-8, 1, 1, 2, 2, 3, 4, 5]

#-------------------------------------- List Reverse Method --------------------------------------
print('-------------------------------------- List Reverse Method --------------------------------------')

# Reverse method reverses the list
list3.reverse()
print(list3)  # Output: [5, 4, 3, 2, 2, 1, 1, -8]

#-------------------------------------- List Copy Method --------------------------------------
print('-------------------------------------- List Copy Method --------------------------------------')

# Copy method copies the list
list4 = list3.copy()
print(list4)  # Output: [5, 4, 3, 2, 2, 1, 1, -8]

#-------------------------------------- List Extend Method --------------------------------------
print('-------------------------------------- List Extend Method --------------------------------------')

# Extend method adds another list to the current list
list4 = ['apple', 'banana', 'orange']
list5 = ['lemon', 'grapes']
list4.extend(list5)
print(list4)  # Output: ['apple', 'banana', 'orange', 'lemon', 'grapes']

#-------------------------------------- List Comprehension --------------------------------------
print('-------------------------------------- List Comprehension --------------------------------------')

# List comprehension: creating a list of numbers from 0 to 9
list6 = [i for i in range(10)]
print(list6)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a new list with sorted values
new_list = sorted(list6)
print(f"Sorted list: {new_list}")  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a new list with repeated values
created_list = [10] * 5
print(f"Created list: {created_list}")  # Output: [10, 10, 10, 10, 10]

#-------------------------------------- List Concatenation --------------------------------------
print('-------------------------------------- List Concatenation --------------------------------------')

# List concatenation
first_list = [1, 2, 3]
second_list = [4, 5, 6]
concatenated_list = first_list + second_list
print(f"Concatenated list: {concatenated_list}")  # Output: [1, 2, 3, 4, 5, 6]

#-------------------------------------- List Slicing --------------------------------------
print('-------------------------------------- List Slicing --------------------------------------')

# Slicing of list
mylist = [i for i in range(10)]
print(f"My list: {mylist}")
sliced_list = mylist[1:5]
print(f"Sliced list: {sliced_list}")  # Output: [1, 2, 3, 4]

# Don't specify the start index
sliced_list = mylist[:3]
print(f"Sliced list: {sliced_list}")  # Output: [0, 1, 2]

# Don't specify the end index
sliced_list = mylist[6:]
print(f"Sliced list: {sliced_list}")  # Output: [6, 7, 8, 9]

# Slicing with step
sliced_list = mylist[1:7:2]
print(f"Sliced list: {sliced_list}")  # Output: [1, 3, 5]

# Start with 0 index and end with 7 index, step is 2
sliced_list = mylist[::2]
print(f"Sliced list: {sliced_list}")  # Output: [0, 2, 4, 6, 8]

# Reverse the list using slicing
reversed_list = mylist[::-1]
print(f"Reversed list: {reversed_list}")  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#-------------------------------------- List Unpacking --------------------------------------
print('-------------------------------------- List Unpacking --------------------------------------')

# List unpacking
numbers = [1, 2, 3]
print(f"Numbers: {numbers}")
first, second, third = numbers
print(f"First: {first}")  # Output: 1
print(f"Second: {second}")  # Output: 2
print(f"Third: {third}")  # Output: 3

#-------------------------------------- Using * Operator for Unpacking --------------------------------------
print('-------------------------------------- Using * Operator for Unpacking --------------------------------------')

# Using the * operator
numbers = [1, 2, 3, 4, 5, 6]
first, second, *others = numbers
print(f"First: {first}")  # Output: 1
print(f"Second: {second}")  # Output: 2
print(f"Others: {others}")  # Output: [3, 4, 5, 6]

# Using the * operator in the middle
first, *others, last = numbers
print(f"First: {first}")  # Output: 1
print(f"Others: {others}")  # Output: [2, 3, 4, 5]
print(f"Last: {last}")  # Output: 6

# Using the * operator in the first
*first, others, last = numbers
print(f"First: {first}")  # Output: [1, 2, 3, 4, 5]
print(f"Others: {others}")  # Output: 5
print(f"Last: {last}")  # Output: 6

#-------------------------------------- Copying the List --------------------------------------
print('-------------------------------------- Copying the List --------------------------------------')

# Copying the list
org_list = [1, 2, 'apple', True, 2.4]
print(f"Original list: {org_list}")
copy_list = org_list.copy()
print(f"Copy list: {copy_list}")

# Modifying the copied list will not affect the original list
copy_list[0] = 10
print(f"Copy list after modification: {copy_list}")
print(f"Original list after modification: {org_list}")

# Using the list() constructor to copy a list
copy_list = list(org_list)
print(f"Copy list: {copy_list}")

# Using slicing to copy the list
copy_list = org_list[:]
print(f"Copy list: {copy_list}")

#-------------------------------------- List Comprehension Examples --------------------------------------
print('-------------------------------------- List Comprehension Examples --------------------------------------')

# List comprehension
new_list = [i * 20 for i in mylist]
print(f"New list: {new_list}")

# List comprehension with condition
new_list = [i for i in mylist if i % 2 == 0]
print(f"New list with condition: {new_list}")

# List comprehension with an if-else condition
new_list = [i * 2 if i % 2 == 0 else i for i in mylist]
print(f"New list with if-else condition: {new_list}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_matrix = [i for row in matrix for i in row]
print(f"Flattened matrix: {flatten_matrix}")

# Nested list comprehension with expression
new_matrix = [[i * 2 for i in row] for row in matrix]
print(f"New matrix with expression: {new_matrix}")
