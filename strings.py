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