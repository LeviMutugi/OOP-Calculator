#Levi Mutugi Mutharimi
#SCT211-0067/2022

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result:", calculator.add(num1, num2))
            elif user_input == "subtract":
                print("Result:", calculator.subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", calculator.multiply(num1, num2))
            elif user_input == "divide":
                print("Result:", calculator.divide(num1, num2))
        else:
            print("Invalid input. Please try again.")
