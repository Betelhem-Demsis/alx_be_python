def safe_divide(numerator, denominator)->float:
    try:
        num = float(numerator)
        num2= float(denominator)
        if denominator != 0:
           print(f"the result of the division is {num/num2}")
        else:
            print("Error: Cannot divide by zero.")
    except ValueError:
         print("Error: Please enter numeric values only.")