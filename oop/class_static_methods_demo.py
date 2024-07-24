'''
Objective: Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences.

Task Description:
Create a Python script named class_static_methods_demo.py. In this script, define a class Calculator that includes both a class method and a static method to perform calculations.
This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, highlighting their differences and practical applications.

class_static_methods_demo.py:

Calculator Class:
Static Method - add(a, b): Returns the sum of two numbers. Use the @staticmethod decorator.
Class Method - multiply(cls, a, b): Returns the product of two numbers. Use the @classmethod decorator and
ensure it prints a class attribute named calculation_type before performing the multiplication.

Class Attribute:
Define a class attribute calculation_type with a value of "Arithmetic Operations" that the multiply class method will reference.

Expected Output:
When you run main.py, it should produce the following output, which includes the printed message from the class method and the results of the calculations:

The sum is: 15
Calculation type: Arithmetic Operations
The product is: 50
'''

class Calculator:

    calculation_type = "Arithmetic Operations"
    
    @classmethod
    def multiply(cls, a, b):
        cls.a = a
        cls.b = b

        print(f"Calculation type: {cls.calculation_type}")
        return a * b

    @staticmethod
    def add(a, b):
        sum = a + b
        return a + b