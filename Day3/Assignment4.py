#1 Create a function func() which prints a text ‘Hello World’

def func():
    print("hello world")

# 2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’

def funci(name):
    print("Hi my name is google")

# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)

def func3(x,y,z):
    if (z):
        return x
    else:
        return y

# 4.define a function func4(x,y) which returns the product of both the values.

def func4(x,y):
    return x * y

# 5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# 6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.

def greater(x,y):
    if x > y :
        return True
    else:
        return False

# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.

def arbfunc(*args):
    sum = 0
    for x in args:
        sum += args
    return sum


# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.

def arbfunc2(*args):
    mylist = []
    for x in args:
        if x % 2 == 0:
            mylist.append(x)
    return mylist


# 9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase 

def matchingString(input):
    newStr = ""
    for x in range(0, len(input)):
        if x % 2 == 0:
            newStr += input[x].upper()
        else:
            newStr += input[x].lower()
    return newStr

# 10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.

def lesserOrGreater(x, y):
    if (x % 2 == 0 and y % 2 == 0):
        return min(x, y)
    else:
        return max(x, y)



# 11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.

def twoStrings(str1, str2):
    if (str1[0] == str2[0]):
        return True
    else:
        return False


# 13.A function that capitalizes first and fourth character of a word in a string.

def capitalize(input):
    newStr = ""
    for x in range(0, len(input)):
        if (x == 0 or x == 3):
            newStr += input[x].upper()

    return newStr

