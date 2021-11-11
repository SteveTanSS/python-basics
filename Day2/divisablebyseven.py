# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
# 

rangenum = range(2002,3200,7)
rangenum = list(rangenum)

for n in rangenum:
    if n % 5 == 0:
        rangenum.remove(n)

print(rangenum)

#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

rangenum = range(1505,2700,7)
rangenum = list(rangenum)

for n in rangenum:
    if n % 5 == 0:
        rangenum.remove(n)

print(rangenum)