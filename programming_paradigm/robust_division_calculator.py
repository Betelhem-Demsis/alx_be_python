def safe_divide(numerator, denominator) -> float:
    try:
        num = float(numerator)
        num2 = float(denominator)
        if num2 != 0:
            result = num / num2
            return f"The result of the division is {result}"
        else:
            return "Error: Cannot divide by zero."       
    except ValueError:
        return "Error: Please enter numeric values only."
    
