# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

def generateDictionary(num):
    d = {}
    for x in range (1,num + 1):
        d[x] = x * 2
    return d

print(generateDictionary(8))