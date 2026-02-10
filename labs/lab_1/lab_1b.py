"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.
on
"""
def check_valid(num:str):
    while num.isnumeric() == False:
        num=input("Please type valid number here:")
        return check_valid(num)
    return num


def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return [num1 + num2, operation]
    elif operation == "subtract":
        return [num1 - num2, operation]
    elif operation == "multiply":
        return [num1 * num2, operation]
    elif operation == "divide":
        if num2 != 0:
            return [num1 / num2, operation]
        else:
            print("Cannot divide by zero Please reenter fields.")
            return main()

    else:
        operation=input("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide':")
        return simple_calculator(operation, num1, num2)        

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = input("Enter the first number: ")
    num1=float(check_valid(num1))
    num2 = input("Enter the second number: ")
    #print("check_valid: ", check_valid(num1))
    num2=float(check_valid(num2))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {result[1]}ing {num1} and {num2} is: {result[0]}")


if __name__ == "__main__":
    main()