# 1.	Create a list with one number, one word and one float value. Display the output of the list.

mylist = ["1", "word", "1.231"]
print(mylist)

# 2.	I have a nested list [1,1,[1,2]], how to grab the value of 2 from the list.
nestedlist = [1,1,[1,2]]
print(nestedlist[2][1])

# 3.	lst=['a','b','c'] What is the result of lst[1:]?
lst = ['a','b','c']
print(lst[1:])

# 4.	Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable

weekdays = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',

}

# 5.	D={‘k1’:[1,2,3]} what is the output of d[k1][1]

d = {
    'k1' : [1,2,3]
}

# output is error

# 6.	Can you create a list [1,[2,3]] into a tuple

print(tuple([[1,[2,3]]]))

# 7.	With a single set function can you turn the word ‘Mississippi’ to distinct character word.

newset = set('mississipi')
print(newset)

# 8.	Can you add an element ‘X’ to the above created set

newset.add('x')
print(newset)

# 9.	Output of set([1,1,2,3])

set([1,1,2,3])

