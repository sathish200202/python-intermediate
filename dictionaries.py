#dictionarioes is a collection data type in python
#dictionaries are enclosed in curly braces
#dictionaries are key value pairs
#dictionaries are mutable
#dictionaries are unordered
#dictionaries are indexed
#dictionaries are written as key:value pairs
#dictionaries are used to store data values in key:value pairs
#

#------------------------------------creating a dictionary------------------------------------
print("---------------------------------creating a dictionary---------------------------------")

#creating a dictionary
my_dict = {
    "name": "John",
    "age": 30, 
}

print(my_dict)

#------------------------------------ convert the dict ------------------------------------
print("---------------------------------convert the dict---------------------------------")

#convert the dict
my_dict = dict(name="John", age=30)
print(my_dict)

#------------------------------------accessing items------------------------------------
print("---------------------------------accessing items---------------------------------")

#accessing items
my_dict = {
    "name": "John",
    "age": 30, 
}

access_name = my_dict['name']
access_age = my_dict['age']
print(f"Name: {access_name}")
print(f"Age: {access_age}")

#------------------------------------add new value and update the value------------------------------------
print("---------------------------------add new value and update the value---------------------------------")

#add new value and update the value
my_dict["city"] = "chennai"
print(f"Add new value: {my_dict}")

#update the value
my_dict["name"] = "John Doe"
print(f"Update the value: {my_dict}")

#------------------------------------remove the value------------------------------------
print("---------------------------------remove the value---------------------------------")

#remove the value
my_dict = {
    "name": "John",
    "age": 30, 
    "city": "chennai"
}

#pop method to remove the value
my_dict.pop("city")
print(f"Remove the value: {my_dict}")

#del method to remove the value
del my_dict["age"]
print(f"Remove the value: {my_dict}")

#del keyword to delete the dictionary completely
# del my_dict
print(f"Remove the value: {my_dict}") 

my_dict = {
    "name": "John",
    "age": 30, 
    "city": "chennai"
}
#popitem method to remove the last item
my_dict.popitem()
print(f"Remove the last item: {my_dict}")

#------------------------------------ get method ------------------------------------
print("---------------------------------get method---------------------------------")

#get method
my_dict = {
    "name": "John",
    "age": 30, 
    "city": "chennai"
}

access_name = my_dict.get("name")
print(f"Get method: {access_name}")


#------------------------------------ in statement in dict ------------------------------------
print("---------------------------------in statement in dict---------------------------------")

#in statement in dict
my_dict = {
    "name": "John",
    "age": 30, 
    "city": "chennai"
}

if "city" in my_dict:
    print("Yes, 'city' is one of the keys in the my_dict dictionary", my_dict['city'])

#if key is not present in the dict
if "lastname" in my_dict:
    print("Yes, 'lastname' is one of the keys in the my_dict dictionary")
else:
    print("No, 'lastname' is not one of the keys in the my_dict dictionary")

#------------------------------------ loop through a dictionary ------------------------------------
print("---------------------------------loop through a dictionary---------------------------------")

#loop through a dictionary
my_dict = {
    "name": "John",
    "age": 30, 
    "city": "chennai"
}

for data in my_dict:
    print(f"data: {data}")

print("---------------------------------loop through a dictionary values and get the data ---------------------------------")
#loop through a dictionary values
for data in my_dict:
    print(f"data: {my_dict[data]}")

print("---------------------------------loop through a dictionary values---------------------------------")

#loop through a dictionary values
for data in my_dict.values():
    print(f"data: {data}")

print("---------------------------------loop through a dictionary keys---------------------------------")
#loop through a dictionary keys
for data in my_dict.keys():
    print(f"data: {data}")

print("---------------------------------loop through a dictionary items---------------------------------")
#loop through a dictionary items
for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")


#------------------------------------ copy a dictionary ------------------------------------
print("---------------------------------copy a dictionary---------------------------------")

my_dict = {"name": "John", "age": 30, "city": "chennai"}

#copy a dictionary
cpy_dict = my_dict
cpy_dict['country'] = 'India'
#this copy method will change the original dictionary
print(f"Original dictionary: {my_dict}")
print(f"Copy a dictionary: {cpy_dict}")

#copy method
dict2 = {"name": "John", "age": 30}
cpy_dict = dict2.copy()
print(f"coping a dictionary: {cpy_dict}")
print(f"original dictionary: {dict2}")

cpy_dict['city'] = 'chennai'

print(f"original dictionary: {dict2}")
print(f"copy dictionary: {cpy_dict}")

#we can use dict() method to copy a dictionary
cpy_dict = dict(my_dict)
cpy_dict['email'] = "abc@gmail.com"
print(f"copy dictionary: {cpy_dict}")
print(f"original dictionary: {my_dict}")


#------------------------------------ nested dictionary ------------------------------------
print("---------------------------------nested dictionary---------------------------------")

nested_dict = {
    "dict1": {"name": "John", "age": 30},
    "dict2": {"name": "Doe", "age": 40} 
}

print(f"nested dictionary: {nested_dict}")

#accesing the nested dictionary
print(f"accessing the nested dictionary: {nested_dict['dict1']}")

#access the nested dictionary element
print(f"access the nested dictionary element: {nested_dict['dict1']['name']}")

#------------------------------------ create a tuple as a dict key ------------------------------------
print("---------------------------------create a tuple as a dict key---------------------------------")

#tuple as a dict key
tuple_key_dict = {(1,2): 3, (4,5): 9}
print(f"tuple as a dict key: {tuple_key_dict}")
#we can create a number as a dict key

#we can't create a list as a dict key

#------------------------------------ dictionary methods ------------------------------------
print("---------------------------------dictionary methods---------------------------------")

#dictionary methods
my_dict = {
    "name": "John",
    "age": 30, 
    "city": "chennai"
}

#clear method --> clear method will remove all the elements in the dictionary
#clear method will not delete the dictionary
my_dict.clear()
print(f"clear method: {my_dict}")



