def factorial(num):
    sum = 1
    for x in range(1,num + 1):
        sum *= x
    
    print(sum)

factorial(8)