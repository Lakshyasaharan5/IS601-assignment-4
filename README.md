# IS601-assignment-4
Advanced Calculator built on Factory Design Pattern

### Start the calculator

```bash
Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.

>> 
```

### Display help message

```bash
>> help

Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
    pow 2 3
```

### Add operation

```bash
>> add 5 8
Result: AddCalculation: 5.0 Add 8.0 = 13.0
```

### Subtract operation

```bash
>> subtract -5 -10.8
Result: SubtractCalculation: -5.0 Subtract -10.8 = 5.800000000000001
```

### Multiplication operation

```bash
>> multiply 10 55
Result: MultiplyCalculation: 10.0 Multiply 55.0 = 550.0
```

### Division operation with error message

```bash
>> divide 6 2
Result: DivideCalculation: 6.0 Divide 2.0 = 3.0

>> divide 4 0
Cannot divide by zero.
Please enter a non-zero divisor.
```

### Error handling in REPL 

```bash
>> add 4 5 6
Invalid input. Please follow the format: <operation> <num1> <num2>
Type 'help' for more information.

>> sdlfsdl;fk
Invalid input. Please follow the format: <operation> <num1> <num2>
Type 'help' for more information.
```

### Power operation

```bash
>> pow 2 3
Result: PowerCalculation: 2.0 Power 3.0 = 8.0
```

### Display history

```bash
>> history
Calculation History:
1. AddCalculation: 1.0 Add 2.0 = 3.0
2. PowerCalculation: 5.0 Power 3.0 = 125.0
3. AddCalculation: 5.0 Add 8.0 = 13.0
4. SubtractCalculation: -5.0 Subtract -10.8 = 5.800000000000001
5. MultiplyCalculation: 10.0 Multiply 55.0 = 550.0
6. DivideCalculation: 6.0 Divide 2.0 = 3.0
7. PowerCalculation: 2.0 Power 3.0 = 8.0
```

### Exit

```bash
>> exit
Exiting calculator. Goodbye!
```
### Check 100% test coverage

```bash
$pytest --cov=app tests/
========================================================= test session starts =========================================================
platform darwin -- Python 3.13.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/lakshyasaharan/projects/IS601/module-4/IS601-assignment-4
plugins: cov-5.0.0, pylint-0.21.0
collected 77 items                                                                                                                    

tests/test_calculation.py ................................                                                                      [ 41%]
tests/test_calculator.py .................                                                                                      [ 63%]
tests/test_operations.py ............................                                                                           [100%]

---------- coverage: platform darwin, python 3.13.3-final-0 ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
app/calculation/__init__.py      55      0   100%
app/calculator/__init__.py       65      0   100%
app/operation/__init__.py        18      0   100%
-------------------------------------------------
TOTAL                           138      0   100%


========================================================= 77 passed in 0.07s ==========================================================


$coverage report --fail-under=100
Name                          Stmts   Miss  Cover
-------------------------------------------------
app/calculation/__init__.py      55      0   100%
app/calculator/__init__.py       65      0   100%
app/operation/__init__.py        18      0   100%
-------------------------------------------------
TOTAL                           138      0   100%

$pytest --cov=app --cov-report=html
```


### Setup and Installation

Clone the repo using Github url

```bash 
git clone git@github.com:Lakshyasaharan5/IS601-assignment-4.git
```

Create a python virtual environment

```bash
python3 -m venv venv
```

Install all the dependencies using requirements.txt

```bash
pip3 install -r requirements.txt
```

Run pytest to check everything is fine

```bash
pytest
```

Run the calculator from root folder

```bash
python3 main.py
```