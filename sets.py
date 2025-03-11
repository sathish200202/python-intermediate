#set is a collection data type in python
#set is enclosed in curly braces
#set is unordered
#set is mutable
#set is indexed
#set is written as elements separated by comma
#set is used to store multiple items in a single variable
#set does not allow duplicate values
#set is used to perform mathematical set operations like union, intersection, symmetric difference, etc.

#------------------------------------creating a set------------------------------------
print("---------------------------------creating a set---------------------------------")

#creating a set
new_set = {1, 2, 3}
print(new_set)

new_set = {1, 2, 3, 1, 2}
print(new_set)
#set does not allow duplicate values
set1 = { True, False} #True and False are considered as 1 and 0 in python, so it will consider only one value
#set1 = { True, False, 1, 0} #it will consider only one value

print(set1)

#------------------------------------convert the set------------------------------------
print("---------------------------------convert the set---------------------------------")

#convert the set
new_set = set(("apple", 100, True, 4.9, False))
print(f"convert the tuple to set: {new_set}")

#------------------------------------add elements------------------------------------
print("---------------------------------add elements---------------------------------")
new_set2 = set()
print(f"new_set2: {new_set2}")
#add elements
new_set2.add('apple')
new_set2.add('banana')
new_set2.add(2)
print(f"set after adding elements: {new_set2}")

#------------------------------------remove elements------------------------------------
print("---------------------------------remove elements---------------------------------")
new_set2.remove('banana')
print(f"remove the element: {new_set2}")

#------------------------------------clear the set------------------------------------
print("---------------------------------clear the set---------------------------------")
#clear the set
new_set2.clear()
print(f"clear the set: {new_set2}")

#------------------------------------discard set------------------------------------
print("---------------------------------discard set---------------------------------")
#remove the element using discard
new_set2 = {1, 2, 'apple', 'banana'}

new_set2.discard(1)
print(f"discard the element: {new_set2}")

#if the element is not present in the set, it will not raise an error
new_set2.discard(3)
print(f"discard the element: {new_set2}")
#------------------------------------pop the element------------------------------------
print("---------------------------------pop the element---------------------------------")
#pop the element
new_set2.pop()
print(f"pop the element: {new_set2}")

#------------------------------------ delete the set ------------------------------------
print("---------------------------------delete the set---------------------------------")

#delete the set
del new_set2
#print(f"delete the set: {new_set2}") #it will raise an error

#------------------------------------ set iteration ------------------------------------
print("---------------------------------set iteration---------------------------------")

#set iteration
new_set3 = {1, 2, 3, 4, 5}

#------------------------------------ in statement ------------------------------------
print("---------------------------------in statement---------------------------------")
#in statement in set
for i in new_set3:
    print(f"set iteration: {i}")

if 5 in new_set3:
    print("5 is present in the set")


#------------------------------------ set methods ------------------------------------
print("---------------------------------set methods---------------------------------")

#set methods
odd_numbers = {1, 3, 5, 7, 9}
even_numbers = {0, 2, 4, 6, 8, 10}
prime_numbers = {2, 3, 5, 7}

#union method
#union method will return a new set with all the elements from both the sets
#union method will not modify the original sets
#union method will not allow duplicate values

union = odd_numbers.union(even_numbers)
print(f"union method: {union}")

union2 = union.union(prime_numbers)
print(f"union method: {union2}")


#intersection method
#intersection method will return a new set with common elements from both the sets
#intersection method will not modify the original sets
#intersection method will not allow duplicate values
#intersection method will return an empty set if there are no common elements

intersection = odd_numbers.intersection(prime_numbers)
print(f"intersection method: {intersection}")


#difference method
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
#difference method will return a new set with elements that are present in setA but not in setB
#difference method will not modify the original sets
#difference method will not allow duplicate values
#its only return the elements that are present in setA but not in setB

differences = setA.difference(setB)
print(f"difference method: {differences}")

#symmetric_difference method

#symmetric_difference method will return a new set with elements that are present in either setA or setB but not in both
#symmetric_difference method will not modify the original sets
#symmetric_difference method will not allow duplicate values
#symmetric_difference method will return an empty set if there are no common elements

sym_differ = setA.symmetric_difference(setB)
print(f"symmetric_difference method: {sym_differ}")

#update method
#update method will update the set with elements from another set
#update method will modify the original set

setA.update(setB)
print(f"update method: {setA}")

#intersection_update method
#intersection_update method will update the set with common elements from another set
#intersection_update method will modify the original set
setC = {1,2,3,4,5}
setD = {1,2,3,6,7,8}
setC.intersection_update(setD)
print(f"intersection_update method: {setC}")

#difference_update method
#difference_update method will update the set with elements that are present in setA but not in setB
#difference_update method will modify the original set
setE = {1,2,3,4,5}
setF = {1,2,3,6,7,8}

setE.difference_update(setF)
print(f"difference_update method: {setE}")

#symmetric_difference_update method
#symmetric_difference_update method will update the set with elements that are present in either setA or setB but not in both
#symmetric_difference_update method will modify the original set
setG = {1,2,3,4,5}
setH = {1,2,3,6,7,8}

setG.symmetric_difference_update(setH)
print(f"symmetric_difference_update method: {setG}")

#subset method
#subset method will return True if all the elements in the set are present in another set
#subset method will return False if all the elements in the set are not present in another set
#subset method will return True if the set is a subset of another set
#subset method will return False if the set is not a subset of another set

setI = {1,2,3}
setJ = {1,2,3,4,5}

print(f"subset method: {setJ.issubset(setI)}")

#superset method
#superset method will return True if all the elements in another set are present in the set
#superset method will return False if all the elements in another set are not present in the set
#superset method will return True if the set is a superset of another set
#superset method will return False if the set is not a superset of another set

print(f"superset method: {setI.issuperset(setJ)}")

#disjoint method
#disjoint method will return True if there are no common elements between the sets
#disjoint method will return False if there are common elements between the sets

setK = {1,2,3}
setL = {4,5,6}

print(f"disjoint method: {setK.isdisjoint(setL)}")


#------------------------------------ set copy methods ------------------------------------
print("---------------------------------set copy methods---------------------------------")

#copy method
new_set = {1, 2, 3, 4, 5}

cpy_set = new_set

print(f"copy method: {cpy_set}")

#update the copied set
cpy_set.add(6)
print(f"original set: {new_set}")
print(f"copied set: {cpy_set}")
#it will update the original set also

#to avoid this we can use copy() method

new_set = {1, 2, 3, 4, 5}

cpy_set = new_set.copy()
print(f"copy method: {cpy_set}")

#update the copied set
cpy_set.add(6)
print(f"original set: {new_set}")
print(f"copied set: {cpy_set}")
#so, we can use copy() method to avoid updating the original set

#set() method
new_set = {1, 2, 3, 4, 5}
cpy_set = set(new_set)

print(f"copy method: {cpy_set}")

#update the copied set
cpy_set.add(6)
print(f"original set: {new_set}")
print(f"copied set: {cpy_set}")

#------------------------------------ frozen set ------------------------------------
print("---------------------------------frozen set---------------------------------")

#frozen set
#frozen set is immutable

frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"frozen set: {frozen_set}")

#frozen_set.add(6) #it will raise an error

#frozen_set.remove(1) #it will raise an error
print(f"frozen set: {frozen_set}")
#frozen set is immutable, so we can't add or remove elements from the frozen set


#frozen set methods

#union method

frozen_set1 = frozenset([1, 2, 3, 4, 5])
frozen_set2 = frozenset([4, 5, 6, 7, 8])

union = frozen_set1.union(frozen_set2)
print(f"union method: {union}")


#we cannot use any update methods in frozen set