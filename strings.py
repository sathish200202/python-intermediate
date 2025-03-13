#String is a data type in python which is used to store text data in python. 
#String is a collection of characters
#String is ordered
#String is immutable
#String is indexed
#String is enclosed in single quotes or double quotes
#String is written as characters

#------------------------------------creating a string------------------------------------
print("---------------------------------creating a string---------------------------------")

#creating a string
new_string = "Hello, World!"

print(new_string)

name = 'i\'am a programmer'
print(name)

name = "i'am a programmer"
print(name)


#----------------------------------------- Access the characters in string using index -----------------------------------------
print("----------------------------------------- Access the characters in string using index -----------------------------------------")

my_string = "vanakkam da mapla"
print(f"my_string: {my_string}")

#using index for access the string value
char = my_string[1]
print(f"char: {char}")

#we can use negative value for index, it'll starts from end
char = my_string[-3]
print(f"char: {char}")


#String can't accept the item assignment
string = "Hello"
string = "wolrd"
print(string) #it's okay, we can change the string, but we can't change the string character

string = "Hello"
# string[0] ="w"
print(string) #so, we cannot reasign a value to a string characters

#----------------------------------------- String Slicing -----------------------------------------
print("----------------------------------------- String Slicing -----------------------------------------")

#slice the string using start and end values
characters = my_string[1:4]
print(f"characters: {characters}")

#get the all characters
all_char = my_string[:]
print(f"all_char: {all_char}")

#without start value --> start with very begining
without_start_value = my_string[:4]
print(f"without_start_value: {without_start_value}")

#without end value --> end with very end
without_end_value = my_string[4:]
print(f"without_end_value: {without_end_value}")

#get the all characters
get_the_all_char = my_string[::]
print(f"get_the_all_char: {get_the_all_char}")

#if i put this --> its return every second character
return_the_char = my_string[::2]
print(f"return_the_char: {return_the_char}")


#reverse the string
reverse_the_string = my_string[::-1]
print(f"reverse the string: {reverse_the_string}")


#----------------------------------------- String Methods -----------------------------------------
print("----------------------------------------- String Methods -----------------------------------------")

#concatination
print("concatination:")
str1 = "vanakkam da mapla!"
str2 = " theni la irunthu"

print(str1 + str2)

#iterate
print("iterate:")
strings = "hello, world!"
for i in strings:
    print(i)

#condition
print("condition:")

if "l" in strings:
    print("Yes")
else:
    print("No")

#strip() method for removing white spaces before and after the string
my_string = "    namma Ooru Chennai   "
my_string = my_string.strip()
print(my_string)

#convert to upper and loWer case
my_string = "namma ooru chennai"
print(my_string.upper()) #for uppercase

print(my_string.lower()) #for lowercase

#check starts with --
print(my_string.startswith('n'))

#check ends with --
print(my_string.endswith('i'))

#find method -- this will return the index of the characters, we can also check the substring
string = "hello world"
print(f"find: {string.find('h')}")

#count method -- returns the how many char in the string
print(f"count: {string.count('l')}")

#replace method - we can replace the char
print(f"replace: {string.replace('world', 'mark')}")


#convert the string to list
my_string = "how are you doing?"
my_list = list(my_string) # this method the string as a list by letters, its not fair
#print(f"List: {my_list}")

#use split() for convert the list
my_string = "how are you doing?"
my_list = my_string.split()
print(f"List: {my_list}")

#join() method for cancatinate the list
my_string = " ".join(my_list)
print(f"join: {my_string}")

#join is a very very important and very use full function...


#----------------------------------------- String Fromating -----------------------------------------
print("----------------------------------------- String Formating -----------------------------------------")

# %, .format(), f-Strings

# first -- % - it means indicate to the intepreter the variable is a this or that(string, digits,...) datatypes
var = "tom"
print("the name is %s" % var) # s means string

var = 5
print("the value is %d" % var) # d means digit

var = 8.8942020
print("the value is %f" % var) # f means floating value

#we can also mention, how many digits we want
var = 7.890392898423424214
print("the value is %.2f" % var) # by default, its shows only 6 digits, %.2f means, we want 2 digits

#.format() method
var1 = "tom"
var2 = 5
var3 = 3.8998
print("the variable is {} and {}".format(var1, var2))
print("the variable is {}".format(var2))
print("the variable is {:.2f}".format(var3))


#f-String method
var1 = "tom"
var2 = 10
print(f"the variable is {var1} and {var2}")
#we can use some math functions here
print(f"the variable is {var1} and {var2 % 5}") # +, -, *, %, //

