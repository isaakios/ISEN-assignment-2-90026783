#fuction to multiply or divide
def times_or_divide(operation):
    global num_one, num_two
    if operation == "*":
        return num_one * num_two
    elif operation == "/":
        return num_one / num_two
    else:
        raise ValueError("Invalid operation")
    
#function to add or subtract
def add_or_subtract(operation):
    global num_one, num_two
    if operation =="+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    else:
        raise ValueError("Invalid operation")