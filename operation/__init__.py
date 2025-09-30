# operations.py

class Operation:
    """
    The Operation class encapsulates basic arithmetic operations as static methods.
    This design groups related functions (addition, subtraction, multiplication, and division) 
    in a single class, making the code more modular and organized.

    **Object-Oriented Programming (OOP) Principles Illustrated:**
    - **Encapsulation:** This class groups all arithmetic operations together, making it easier 
      to maintain, test, and reuse these methods in other parts of the code.
    - **Abstraction:** Users of this class only need to know the function names and purpose, 
      not how they work internally.
    - **Reusability:** Static methods can be called directly on the class without creating an instance, 
      making it straightforward to reuse these methods anywhere.
    - **Organization:** By placing all basic operations in a single class, the code becomes 
      more structured and readable.
    
    **Why Static Methods?**
    - **Statelessness**: These methods do not rely on any instance-specific data; they only 
      depend on input parameters. Static methods are ideal for utility functions that 
      perform independent operations.
    - **Ease of Access**: Because we don’t need to create an instance of Operation to call 
      these methods, it’s easy to use them across different parts of the program.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Adds two floating-point numbers and returns the result.

        **Parameters:**
        - `a (float)`: The first number to add.
        - `b (float)`: The second number to add.
        
        **Returns:**
        - `float`: The sum of `a` and `b`.

        **Example:**
        >>> Operation.addition(5.0, 3.0)
        8.0

        **Why Use Static Method for Addition?**
        - Static methods are suitable for functions like addition because they are 
          independent of any instance-specific data, relying only on the parameters.
        """
        return a + b  # Performs addition of two numbers and returns the result.
    
