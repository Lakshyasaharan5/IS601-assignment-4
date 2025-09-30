# tests/test_operations.py

"""
Unit tests for the operations module using pytest.

This test suite covers both positive and negative scenarios for the Operation
class's static methods. It ensures that arithmetic operations perform correctly
and handle edge cases appropriately.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from app.operation import Operation


# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

def test_addition_positive():
    """
    Test the addition method with two positive numbers.
    
    This test verifies that adding two positive numbers returns the correct sum.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 15.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_negative_numbers():
    """
    Test the addition method with two negative numbers.
    
    This test verifies that adding two negative numbers returns the correct sum.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -15.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_positive_negative():
    """
    Test the addition method with one positive and one negative number.
    
    This test verifies that adding a positive and a negative number returns the correct sum.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 5.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + ({b}) to be {expected_result}, got {result}"


def test_addition_with_zero():
    """
    Test the addition method with zero as one of the operands.
    
    This test verifies that adding zero to a number returns the number itself.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

def test_subtraction_positive():
    """
    Test the subtraction method with two positive numbers.
    
    This test verifies that subtracting two positive numbers returns the correct difference.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 5.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


def test_subtraction_negative_numbers():
    """
    Test the subtraction method with two negative numbers.
    
    This test verifies that subtracting two negative numbers returns the correct difference.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -5.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_positive_negative():
    """
    Test the subtraction method with one positive and one negative number.
    
    This test verifies that subtracting a negative number from a positive number returns the correct difference.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 15.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_with_zero():
    """
    Test the subtraction method with zero as one of the operands.
    
    This test verifies that subtracting zero from a number returns the number itself.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

def test_multiplication_positive():
    """
    Test the multiplication method with two positive numbers.
    
    This test verifies that multiplying two positive numbers returns the correct product.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_negative_numbers():
    """
    Test the multiplication method with two negative numbers.
    
    This test verifies that multiplying two negative numbers returns the correct product.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_positive_negative():
    """
    Test the multiplication method with one positive and one negative number.
    
    This test verifies that multiplying a positive number by a negative number returns the correct product.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * ({b}) to be {expected_result}, got {result}"


def test_multiplication_with_zero():
    """
    Test the multiplication method with zero as one of the operands.
    
    This test verifies that multiplying any number by zero returns zero.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 0.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

def test_division_positive():
    """
    Test the division method with two positive numbers.
    
    This test verifies that dividing two positive numbers returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_negative_numbers():
    """
    Test the division method with two negative numbers.
    
    This test verifies that dividing two negative numbers returns the correct quotient.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_positive_negative():
    """
    Test the division method with one positive and one negative number.
    
    This test verifies that dividing a positive number by a negative number returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / ({b}) to be {expected_result}, got {result}"


def test_division_with_zero_divisor():
    """
    Test the division method with zero as the divisor.
    
    This test verifies that dividing any number by zero raises a ValueError.
    """
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operation.division(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero is not allowed."


def test_division_with_zero_numerator():
    """
    Test the division method with zero as the numerator.
    
    This test verifies that dividing zero by a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.addition, '10', 5.0, TypeError),
    (Operation.subtraction, 10.0, '5', TypeError),
    (Operation.multiplication, '10', '5', TypeError),
    (Operation.division, 10.0, '5', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """
    Test that arithmetic methods raise TypeError when provided with invalid input types.
    
    This test verifies that providing non-float inputs to the arithmetic methods raises
    a TypeError, as the operations are intended for floating-point numbers.
    """
    # Arrange
    # No setup needed as the invalid inputs are provided directly

    # Act & Assert
    with pytest.raises(expected_exception):
        calc_method(a, b)


# -----------------------------------------------------------------------------------
# Test Power Method
# -----------------------------------------------------------------------------------

def test_power_positive_exponent():
    """
    Test the power method with a positive exponent.
    
    This test verifies that raising a base to a positive exponent returns the correct result.
    """
    # Arrange
    base = 2.0
    exponent = 3.0
    expected_result = 8.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_zero_exponent():
    """
    Test the power method with zero as the exponent.
    
    This test verifies that any non-zero base raised to the power of zero returns 1.0.
    """
    # Arrange
    base = 5.0
    exponent = 0.0
    expected_result = 1.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_zero_base_positive_exponent():
    """
    Test the power method with zero as the base and a positive exponent.
    
    This test verifies that zero raised to any positive exponent returns 0.0.
    """
    # Arrange
    base = 0.0
    exponent = 5.0
    expected_result = 0.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_negative_exponent():
    """
    Test the power method with a negative exponent.
    
    This test verifies that raising a base to a negative exponent returns the correct reciprocal result.
    """
    # Arrange
    base = 2.0
    exponent = -2.0
    expected_result = 0.25

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


def test_power_zero_base_zero_exponent():
    """
    Test the power method with both base and exponent as zero.
    
    This test verifies the behavior of 0 ** 0, which in Python returns 1.0.
    """
    # Arrange
    base = 0.0
    exponent = 0.0
    expected_result = 1.0  # Python defines 0**0 as 1.0

    # Act
    result = Operation.power(base, exponent)

    # Assert
    assert result == expected_result, f"Expected {base} ** {exponent} to be {expected_result}, got {result}"


@pytest.mark.parametrize("base, exponent, expected_exception", [
    ('2', 3.0, TypeError),
    (2.0, '3', TypeError),
])
def test_power_invalid_input_types(base, exponent, expected_exception):
    """
    Test the power method with invalid input types.
    
    This test verifies that providing non-float inputs raises a TypeError.
    """
    # Arrange
    # Invalid inputs provided through parametrization

    # Act & Assert
    with pytest.raises(expected_exception):
        Operation.power(base, exponent)
