#Reverse a String
def reverse_a_string(string):
    return string[::-1]

string = input('Enter a string: ')
result = reverse_a_string(string)
print(result)


#Palindrome
#A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward

def is_palindrome(string):
    if string == string[::-1]:
        return f"Yes! {string} is a palindrome"
    else:
        return f"{string} is not a palindrome"
    
string = input('Enter your string: ')
result = is_palindrome(string)
print(result)


#factorial calculation
# 5 --> 5 * 4 * 3 * 2 * 1 = some ans is there, that is a factorial

def factorial(num):
    if num == 0:
        return "invalid"
    elif num == 1:
        return 1
    else :
        return num * factorial(num -1)

number = int(input("Enter a number: "))
result = factorial(number)
print(result)


#Fibonacci Sequence
#The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones. It typically starts with 0 and 1.

def fibonacci(num):
    return



#find the largest number

def find_the_largest_number(numbers):
    largest_number = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest_number:
            largest_number = numbers[i]
       
    print(largest_number)

find_the_largest_number([1, 5, 8, 9, 2, 12])


#count vowels in a string

def count_vowels(string):
    vowels = ("a", "e", "i", "o", "u")
    count = 0
    for char in string:
        if char in vowels:
            count +=1
    print(count)


string = "hello"
count_vowels(string)


#remove duplicate from the list
def remove_the_dublicate(value):
    my_set = set(value)
    print(list(my_set))

my_list1 = [1, 2, 3, 1, 2, 5, 3]
my_list2 = ["apple", "banana", "cherry", "apple", "cherry", "mangoo"]
remove_the_dublicate(my_list1)
remove_the_dublicate(my_list2)


#Anagram
#An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
#example --> listen -- silent 

def anagram(string1, string2):
    if len(string1) != len(string2):
        return "Not anagram"
    string1_list = list(string1)
    string2_list = list(string2)

    for char in string1_list:
        if char in string2_list:
            string2_list.remove(char)
    
    if not string2_list:
        return f"{string1} and {string2} are anagrams"
    else:
        return "Not a anagram"

string1 = "silent"
string2 = "listen"

result = anagram(string1, string2)
print(result)



#Merge Two Sorted Lists
#Prime Number Check
#Prime Number
def prime_Number(num):
    if num <= 1:
        print("not prime number")
    if num % 2 == 0:
        print("not prime number")
    return

#will be continue................

#Fibonacci Sequence


#FizzBuzz program

def fizz_buzz(num):
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


number = int(input("Number: "))
if number > 0:
    fizz_buzz(number)
else:
    print("Please! Enter the positive number only")


#Count Occurrences of a Character in a String
def count_occurrences_string(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
            
    return count

string = "aaalllssss"
char = input("Enter a char: ")
if char in string:
    result = count_occurrences_string(string, char)
    print(result)
else:
    print("The character not in a String")


#Password checker
def Password_Checker(password):
    if len(password) < 6:
        return "Password should be atleast 6 characters"
    has_upper = False
    has_lower = False
    has_digits = False
    has_special = False
    special_char = "!@#$%&*:"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digits = True
        elif char in special_char:
            has_special = True
        
    if not has_upper:
        return "Password should have atleast one uppercase letter"
    if not has_lower:
        return "Password should have atleast one lowercase letter"
    if not has_digits:
        return "Password should have atleast one digit"
    if not has_special:
        return "Password should have atleast one special character(like: !,@,#,$,%,&,*,:)"
    
    return "Password is Strong!"

password = input("Enter your password: ")
result = Password_Checker(password)
print(result)

 