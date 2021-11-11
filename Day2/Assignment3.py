import random

#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

def divisible_by_seven():

    rangenum = range(1505,2700,7)
    rangenum = list(rangenum)

    for n in rangenum:
        if n % 5 == 0:
            rangenum.remove(n)
    print(rangenum)

# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor

def f_to_c(f):
    return (f - 32) * 5/9


def c_to_f(c):
    return ((c * 9/5) + 32)

# 3.	 Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

def numberGuess():
    ran = random.randint(1,9)

    while 1:
        num = int(input("number from 1 to 9: "))
        if num == ran:
            print("Well guessed!")
            break
        



# 4. Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def printstars():
    n=5;
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')



# 6. Write a Python program that accepts a word from the user and reverse it. Go to the editor

def reverseword():
    word = input("Word to reverse: ")
    word = word[::-1]
    print(word)


# Write a Python program to count the number of even and odd numbers from a series of numbers. 

def count(numbers):
    numOdd = 0
    numEven = 0
    for x in numbers:
        if x % 2 == 1:
            numOdd += 1
        if x % 2 == 0:
            numEven += 1
    print("Number of Even Numbers:" + str(numEven))
    print("Number of Odd Numbers:" + str(numOdd))

#8.	Write a Python program that prints each item and its corresponding type from the following list.
#   Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def print_each():
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for x in datalist:
        print(str(x) + "- " + str(type(x)))

def print_zero_to_six():

    for x in range (0,6):
        if x % 3 == 0:
            continue
        else:
            print(x)