import sys
import calculator
import func

func.clear_terminal()

print("Welcome to the calculator!")
print("You can use x, y, and z as variables in your equation.")
print("You can use +, -, *, /, ^, %, and // as operators.")
print("You can use parentheses to group operations.")
print("Please put a space after each number and symbol.")
print("Example: 2 + 2 * ( 3 - 1 )")
input("\nPress ENTER to continue")
func.clear_terminal()
    
while True:
    print("Note: You can type 'exit' to exit the calculator.")
    equation = input("\nEnter an equation (Put space after each number and symbols): ")
    func.clear_terminal()

    if equation.lower() == "exit":
        print("Exiting calculator...")
        sys.exit()

    x = 0
    y = 0
    z = 0

    if "x" in equation:
        x = input("Enter a value for x: ")
        while not func.isDigit(x):
            x = input("\nInvalid value for x. Please enter a valid number: ")
        x = float(x)

    if "y" in equation:
        y = input("Enter a value for y: ")
        while not func.isDigit(y):
            y = input("\nInvalid value for y. Please enter a valid number: ")
        y = float(y)

    if "z" in equation:
        z = input("Enter a value for z: ")
        while not func.isDigit(z):
            z = input("\nInvalid value for z. Please enter a valid number: ")
        z = float(z)

    print("The answer to "+str(equation)+"; Where x = "+str(x)+", y = "+str(y)+", and z = "+str(z)+" is: "+str(calculator.eqCal(equation,x,y,z)))
    print("\nWould you like to calculate another equation? (y/n)")
    if input().lower() != "y":
        print("Exiting calculator...")
        sys.exit()
    func.clear_terminal()