def Integration(degree1,cof1): 
    cof3 = []
    counter = 0
    y = 0
    solution = []

    while counter <= degree1:
        cof3.append(cof1[counter]/((degree1+1)-counter))
        counter = counter + 1
    
    while y <= degree1:
        s = ""
        s=s.join((str(cof3[y]),"x^",str(((degree1+1)-y))))
        solution.append(s)
        y = y + 1
    
    return print (solution)

def Derivative(degree1, cof1):
    cof3 = []
    counter = 0
    solution = []
    y = 0

    while counter < degree1:
        cof3.append((degree1-counter)*cof1[counter])
        counter = counter + 1

    while y < degree1:
        s = ""
        s=s.join((str(cof3[y]),"x^",str(((degree1-1)-y))))
        solution.append(s)
        y = y + 1
    
    return print(solution)

def Division(degree1,cof1,degree2,cof2):
    cof3 = []
    cof4 = []
    remainder = []
    x = 0
    y = 0
    counter = 0
    solution = []
    solution2 =[]
    counter1 = 0
    if degree1 == degree2:
        z = cof1[0]/cof2[0]
        cof3.append(z)
        
        while x <= degree1:
            cof4.append(cof2[x]*z)
            x = x + 1
        while counter1 <= degree1:
            remainder.append(cof1[counter1]-cof4[counter1])
            counter1 = counter1 + 1
        
        while y <= degree1:
            s = ""
            s=s.join((str(remainder[y]),"x^",str((degree1-y))))
            solution2.append(s)
            y = y + 1
        
        y = 0
        difference = 0

        while y <= difference:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((difference-y))))
            solution.append(s)
            y = y + 1
    
    else:
        degree3 = degree1 - degree2
        c = 0
        quotient = []
        f = 0
        newPoly = []
        
        while c <= degree3:
            quotient.append(0)
            c = c + 1
        
        
        while f <= degree1: 
            newPoly.append(cof1[f])
            f = f + 1
        
        difference = degree3 
        
        while difference >= 0:
            quotient1 = newPoly[0]/cof2[0]
            quotient[degree3 - difference] = quotient1 
            temp1 = []
            temp2 = []
            counter4 = 0
            counter2 = 0
            counter3 = 0
            counter5 = 0
            counter6 = 0
            counter7 = 0
            counter8 = 0
            counter9 = 0
            counter10 = 0
            
            while counter4 <= difference:
                temp1.append(0)
                counter4 = counter4 + 1
            
            while counter5 <= (difference + degree2):
                temp2.append(0)
                counter5 = counter5 + 1
        
            temp1[0] = quotient1

            for counter2 in range(difference+1):
                for counter3 in range(degree2+1):
                    temp2[counter2+counter3] += (temp1[counter2]*cof2[counter3])


            while counter6 <= (difference + degree2):
                temp2[counter6] = newPoly[counter6] - temp2[counter6]
                counter6 = counter6 + 1



            
            while counter9 <= (difference + degree2):
                if temp2[counter9] != 0:
                    break
                counter9 = counter9 + 1
            length = len(temp2)

            newdegree = length - counter9 -1

            newPoly =[]

            while counter8 <= newdegree:
                newPoly.append(0)
                counter8 = counter8 + 1

            while counter7 <= newdegree:
                newPoly[counter7] = temp2[counter7 + counter9]
                counter7 = counter7 + 1

            difference = newdegree - degree2
        
        while counter10 <= degree3:
            s = ""
            s=s.join((str(quotient[counter10]),"x^",str((degree3-counter10))))
            solution.append(s)
            counter10 = counter10 + 1
        counter10 = 0
        while counter10 <= newdegree:
            s = ""
            s=s.join((str(newPoly[counter10]),"x^",str((newdegree-counter10))))
            solution2.append(s)
            counter10 = counter10 + 1
    
    return print ("the remainder is: ", solution2,"the solution is: ", solution)


def Multiplication(degree1, cof1, degree2, cof2):
       
    highestdegree = degree1 + degree2
    counter=0
    cof3 = []
    y = 0
    solution=[]
    
    while(counter <= highestdegree):
        cof3.append(0)
        counter = counter + 1
        
    for x in range(degree1+1):
        for z in range(degree2+1):
            cof3[x+z] += (cof1[x]*cof2[z])
        
    while y <= highestdegree:
        s = ""
        s=s.join((str(cof3[y]),"x^",str((highestdegree-y))))
        solution.append(s)
        y = y + 1
        
    return print (solution)
   
    
def Addition(degree1,cof1,degree2,cof2):
    cof3 = []
    counter = 0
    x = 0
    y = 0
    solution = []
    
    if degree1 == degree2 :
        while counter <= degree1:
            cof3.append(cof1[counter]+cof2[counter])
            counter = counter + 1
        while y <= degree1:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((degree1-y))))
            solution.append(s)
            y = y + 1
     
    elif degree1 > degree2:
        difference = degree1 - degree2
        while counter < difference:
            cof3.append(cof1[counter])
            counter = counter + 1
        while x <= degree2:
            cof3.append(cof1[x+difference]+cof2[x])
            x = x + 1
        while y <= degree1:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((degree1-y))))
            solution.append(s)
            y = y + 1
    else:
        difference = degree2 - degree1
        while counter < difference:
            cof3.append(cof2[counter])
            counter = counter + 1
        while x <= degree1:
            cof3.append(cof1[x]+cof2[x+difference])
            x = x + 1
        while y <= degree2:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((degree2-y))))
            solution.append(s)
            y = y + 1
    return print(solution)


def Subtraction(degree1,cof1,degree2,cof2):
    cof3 = []
    counter = 0
    x = 0
    y=0
    solution=[]

    if degree1 == degree2 :
        while counter <= degree1:
            cof3.append(cof1[counter]-cof2[counter])
            counter = counter + 1
        while y <= degree1:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((degree1-y))))
            solution.append(s)
            y = y + 1
            
    
    elif degree1 > degree2:
        difference = degree1 - degree2
        while x < difference:
            cof3.append(cof1[x])
            x = x + 1
        while counter <= degree2:
            cof3.append(cof1[counter+difference]-cof2[counter])
            counter = counter + 1
        while y <= degree1:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((degree1-y))))
            solution.append(s)
            y = y + 1
    
    else:
        difference = degree2 - degree1
        while x < difference:
            cof3.append(0-cof2[x])
            x += 1
        while counter <= degree1:
            cof3.append(cof1[counter]-cof2[counter+difference])
            counter += 1
        while y <= degree2:
            s = ""
            s=s.join((str(cof3[y]),"x^",str((degree2-y))))
            solution.append(s)
            y = y + 1
            
        
    
    return print (solution)

print("Menu of Operations:" + "\n" "1. Addition" +"\n" "2. Subtraction" + "\n" "3. Multiplication" + '\n' "4. Division" + '\n' "5. Derivativation" + '\n' "6. Integration")

operation = int(input("Which operation would you like to perform?(1-6): "))

if operation == 1 :
    
    
    degree1 = int(input("What is the degree of the first polynomial?: "))
    if degree1 < 0:
        print("Invalid Polynomial, please try again!")
        degree1 = int(input("What is the degree of the first polynomial?: "))

    cof1 = []
    x = 0
    while (x <= degree1):
        cof1.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        x = x + 1
    
    
    
    degree2 = int(input("What is the degree of the second polynomial?: "))
    if degree2 < 0:
        print("Invalid Polynomial, please try again!")
        degree2 = int(input("What is the degree of the second polynomial?: "))

    cof2 = []
    y = 0
    while (y <= degree2):
        cof2.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        y = y + 1
    
    
    Addition(degree1,cof1,degree2,cof2)

    
elif operation == 2 :
    degree1 = int(input("What is the degree of the first polynomial?: "))
    if degree1 < 0:
        print("Invalid Polynomial, please try again!")
        degree1 = int(input("What is the degree of the first polynomial?: "))

    cof1 = []
    x = 0
    while (x <= degree1):
        cof1.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        x = x + 1
    
        
    degree2 = int(input("What is the degree of the second polynomial?: "))
    if degree2 < 0:
        print("Invalid Polynomial, please try again!")
        degree2 = int(input("What is the degree of the second polynomial?: "))

    cof2 = []
    y = 0
    while (y <= degree2):
        cof2.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        y = y + 1
    
    Subtraction(degree1,cof1,degree2,cof2)

elif operation == 3 :
    degree1 = int(input("What is the degree of the first polynomial?: "))
    if degree1 < 0:
        print("Invalid Polynomial, please try again!")
        degree1 = int(input("What is the degree of the first polynomial?: "))

    cof1 = []
    x = 0
    while (x <= degree1):
        cof1.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        x = x + 1
    
        
    degree2 = int(input("What is the degree of the second polynomial?: "))
    if degree2 < 0:
        print("Invalid Polynomial, please try again!")
        degree2 = int(input("What is the degree of the second polynomial?: "))

    cof2 = []
    y = 0
    while (y <= degree2):
        cof2.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        y = y + 1
    
    Multiplication(degree1,cof1,degree2,cof2)

elif operation == 5:
    degree1 = int(input("What is the degree of the first polynomial?: "))
    if degree1 < 0:
        print("Invalid Polynomial, please try again!")
        degree1 = int(input("What is the degree of the first polynomial?: "))
    
    cof1 = []
    x = 0
    while (x <= degree1):
        cof1.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        x = x + 1
    Derivative(degree1,cof1)


elif operation == 6:
    degree1 = int(input("What is the degree of the first polynomial?: "))
    if degree1 < 0:
        print("Invalid Polynomial, please try again!")
        degree1 = int(input("What is the degree of the first polynomial?: "))
    
    cof1 = []
    x = 0
    
    while (x <= degree1):
        cof1.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        x = x + 1
    
    Integration(degree1,cof1)        

else:
    degree1 = int(input("What is the degree of the dividend?: "))
    
    if degree1 < 0:
        print("Invalid dividend, please try again!")
        degree1 = int(input("What is the degree of the dividend?: "))
    
    cof1 = []
    
    x = 0
    while (x <= degree1):
        cof1.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        x = x + 1
    
        
    degree2 = int(input("What is the degree of the divisor?: "))
    if degree2 < 0:
        print("Invalid divisor, please try again!")
        degree2 = int(input("What is the degree of the divisor?: "))
    
    if degree1 < degree2:
        print("Invalid Polynomial, please try again!")
        degree2 = int(input("What is the degree of the divisor?: "))
        
    cof2 = []
    y = 0
    while (y <= degree2):
        cof2.append(int(input("List your coefficients from highest degree to lowest degree(one by one): ")))
        y = y + 1


    Division(degree1,cof1,degree2,cof2)

