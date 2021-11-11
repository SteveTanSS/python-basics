# •	Make a list of names that includes at least four people.
# •	Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
# •	Modify your list so that there are only two people in it. Use one of the methods for removing people from the list, don't just redefine the list.
# •	Run your if test again. There should be no output this time, because there are less than three people in the list.
# •	Bonus: Store your if test in a function called something like crowd_test.

def threeisacrowd(inputlist):
    if len(inputlist) > 3 :
        print("Room is crowded")


def crowd_test():
    mylist = ["harry", "sally", "dog", "john"]

    threeisacrowd(mylist)
    mylist.pop()
    mylist.pop()
    threeisacrowd(mylist)

crowd_test()