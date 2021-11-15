def bmi(*inputs):

    #first input is the number of people
    num = inputs[0]

    #string builder to output at end
    bmis = ""

    for x in range (0,num):

        #check the inputs and calculate the bmis
        bmi = inputs[x*2+1] / (inputs[x*2+2] * inputs[x*2+2])
        if (bmi < .185):
            bmis += "under "
        elif (bmi >= .185 and bmi < 25):
            bmis += "normal "
        elif (bmi >= 25 and bmi < 30):
            bmis += "over "
        elif (bmi > 30):
            bmis += "obese "

    print(bmis)

bmi(3,80,1.73,55,1.58,49,1.91)