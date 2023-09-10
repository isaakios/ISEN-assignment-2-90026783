def numbers():
    num_one = int(input("Enter the first number: "))
    num_two = int(input("Enter the second number: "))
    return num_one, num_two

def operation():
    input_operation = input("Please choose an operation between +, -, *, and /: ")
    return input_operation

def check_operation(operation):
    while operation not in ("+", "-", "*", "/"):
        print("Invalid operation")
        operation = input("Re-enter operation: ")
    return operation

def add(num_one, num_two):
    """Add two numbers."""
    return num_one + num_two

def subtract(num_one, num_two):
    """Subtract num_two from num_one."""
    return num_one - num_two

def multiply(num_one, num_two):
    """Multiply two numbers."""
    return num_one * num_two

def divide(num_one, num_two):
    """Divide num_one by num_two."""
    if num_two == 0:
        raise ValueError("Division by zero is not allowed")
    return num_one / num_two

def calculate(num_one, num_two, selected_operation):
    if selected_operation == "+":
        return add(num_one, num_two)
    elif selected_operation == "-":
        return subtract(num_one, num_two)
    elif selected_operation == "*":
        return multiply(num_one, num_two)
    elif selected_operation == "/":
        return divide(num_one, num_two)

def main():
    num_one, num_two = numbers()
    selected_operation = operation()
    selected_operation = check_operation(selected_operation)
    result = calculate(num_one, num_two, selected_operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
