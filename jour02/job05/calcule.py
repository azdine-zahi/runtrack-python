def calcule (num1, operator, num2)
    if operator == "+"
        print(num1+num2)

    elif operator == "-"
        print(num1-num2)

    elif operator == "*"
        print(num1*num2)
    
    elif operator == "/"
        print(num1/num2)
    
    elif operator == "%"
        print(num1%num2)
    

print(calcule(16, "+", 40))
print(calcule(12, "-", 6))
print(calcule(13, "*", 3))
print(calcule(16, "/", 2))
print(calcule(20, "%", 4))