def somma(x,y):
    return x+y
def sottrazione(x,y):
    return x-y
def moltiplicazione(x,y):
    return(x*y)
def divisione(x,y):
    return(x/y)
while True:
    scelta =int(input("insert 1 to add , 2 to subtract, 3 to multiply, 4 to divde\n"))
    if scelta in (1,2,3,4):
        try:
            num1 = float(input("Enter first number: \n"))
            num2 = float(input("Enter second number: \n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if scelta == 1:
            print(num1, "+", num2, "=", somma(num1,num2))
        if scelta == 2:
            print(num1, "-", num2, "=", sottrazione(num1,num2))
        if scelta==3:
            print(num1, "*", num2,  "=", moltiplicazione(num1,num2))
        if scelta==4:
            print(num1, "/", num2, "=", divisione(num1,num2))
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
          break
    else:
        print("Invalid Input")