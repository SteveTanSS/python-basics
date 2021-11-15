# [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 

booklist = [
    [34587,"Learning Python", "Mark Lutz",4,40.95],
    [98762,"Programming Python","Mark Lutz",5,56.80],
    [77226,"Head First Python", "Paul Barry",3,32.95],
    [88112,"Einführung in Python3","Bernd Klein",3,24.99]
]

def accounting(inputlist):
    tuplelist = []

    #create a tuple and put it in the tuplelist
    for x in inputlist:
        value = x[3] * x[4]
        if (value < 100):
            x[3] += 10
        tuple1 = (x[0], x[3] * x[4])
        tuplelist.append(tuple1)
    
    return tuplelist

booklist2 = [
    [34587,("Learning Python","Mark Lutz",4,40.95)],
    [98762,("Programming Python","Mark Lutz",5,56.80)],
    [77226,("Head First Python", "Paul Barry",3,32.95)],
    [88112,("Einführung in Python3","Bernd Klein",3,24.99)]
]

def accounting2(inputlist):
    tuplelist = []

    #create a tuple and put it in the tuplelist
    for x in inputlist:
        
        tuple1 = (x[0], x[1][2] * x[1][3])
        tuplelist.append(tuple1)
    
    return tuplelist

#call function
print(accounting2(booklist2))