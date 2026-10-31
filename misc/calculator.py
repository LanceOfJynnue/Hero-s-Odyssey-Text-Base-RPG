import func

def calculateEqu(equ1):
    #Calculation
    print(equ1)
    
    while len(equ1) > 1:
        a = False
        b = False
        op = False
        num1 = False
        num2 = False
        
        for j in range(len(equ1)):
            if func.isDigit(equ1[j]):
                if a == False:
                    a = int(equ1[j])
                    num1 = j
                    print("assign num1")
                elif b == False:
                    b = int(equ1[j])
                    num2 = j
                    print("assign num2")
                    break
            elif equ1[j] == "+":
                op = "add"
                print(op)
            elif equ1[j] == "-":
                op = "sub"
                print(op)
            elif equ1[j] == "*":
                op = "mult"
                print(op)
            elif equ1[j] == "/":
                op = "div"
                print(op)
            elif equ1[j] == "^":
                op = "expo"
                print(op)
            elif equ1[j] == "%":
                op = "mod"
                print(op)
            elif equ1[j] == "//":
                op = "truncDiv"
                print(op)
        
        if op == "add":
            del equ1[num1:num2]
            equ1[num1] = a + b
        elif op == "sub":
            del equ1[num1:num2]
            equ1[num1] = a - b
        elif op == "mult":
            del equ1[num1:num2]
            equ1[num1] = a * b
        elif op == "div":
            del equ1[num1:num2]
            equ1[num1] = a / b
        elif op == "expo":
            del equ1[num1:num2]
            equ1[num1] = a ** b
        elif op == "mod":
            del equ1[num1:num2]
            equ1[num1] = a % b
        elif op == "truncDiv":
            del equ1[num1:num2]
            equ1[num1] = a // b
    
    return equ1[0]

def eqCal(equation,x=0,y=0,z=0):
    equation = equation.split()
    print(equation)
    for i in range(len(equation)):
        if equation[i] == "x":
            equation[i] = x
        elif equation[i] == "y":
            equation[i] = y
        elif equation[i] == "z":
            equation[i] = z
    
    print(equation)
    
    while len(equation) > 1:
        open = 0
        close = 0
        i = 0
        checkEqu = True
        print("First")
        while checkEqu == True:
            if equation[i] == "(":
                print("Open Parenthesis")
                open = i
                i += 1
            elif equation[i] == ")":
                print("Close Parenthesis")
                close = i
                equ1 = equation[open+1:close]
                result = calculateEqu(equ1)
                del equation[open:close]
                equation[open] = result
                checkEqu = False
            elif i == len(equation)-1:
                print("Last Term")
                close = i
                equ1 = equation[:]
                result = calculateEqu(equ1)
                del equation[open:close]
                equation[open] = result
                checkEqu = False
            else: i += 1
        #
    return equation[0]