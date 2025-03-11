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
#Fibonacci Sequence