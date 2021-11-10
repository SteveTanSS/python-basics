#mortage calculator takes the borrowed sum which is the large chunk of money
#interest rates is the banks interest rate
#length is the number of months that Joel wants to 

import math

def mortgage_Calc(borrowedSum, interestRate, length):
    monthlyRate = interestRate/12
    loanAmmount = float(borrowedSum)
    l = float(length)


    # formula for calcualting monthly payment
    monthlyPayment = loanAmmount * (monthlyRate * (1+ monthlyRate) ** l)/ ((1 + monthlyRate)**l - 1)
    
    #round up to nearest dollar
    return math.ceil(monthlyPayment)
    

print(mortgage_Calc(200000,.05,360))
print(mortgage_Calc(1000000,.08,240))
