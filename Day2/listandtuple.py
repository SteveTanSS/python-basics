# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

def listandtuple(input):
    editted_input = input.split(",")

    print(editted_input)
    print(tuple(editted_input))

listandtuple("34,67,55,33,12,98")

