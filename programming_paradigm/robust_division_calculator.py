def safe_divide(numerator, denominator):
    division = float(numerator / denominator)
    return f"{division:.2f}"
try:
    print(safe_divide(5, 3))
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter numeric values only.")