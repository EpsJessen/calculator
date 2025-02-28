from operators import *
from math import factorial


def calculate(op: str|Operator, first: str, second: str = "0") -> float|None:
    if type(op) == str:
        op = string_to_operator(op)

    try:
        first = float(first)
        second = float(second)
    except ValueError:
        print("Please enter numbers!")
        return None
    match op:
        case Operator.PLUS:
            return first + second
        case Operator.MINUS:
            return first - second
        case Operator.MULTIPLY:
            return first * second
        case Operator.DIVIDE:
            if second != 0:
                return first / second
            else:
                print("Cannot divide by zero!")
                return None
        case Operator.POWER:
            return first ** second
        case Operator.SQRT:
            return first ** 0.5
        case Operator.FAC:
            if (first % 1 != 0):
                print("Cannot calculate factorial of non-integer!")
                return None
            if (first < 0):
                print("Cannot calculate factorial of negative numbers!")
                return None
            return factorial(int(first))
        case _:
            return 0

def main() -> None:
    assert calculate("+", "1", "2") == 3, "1 + 2 should equal 3"
    assert calculate("-", "1", "2") == -1, "1 - 2 should equal -1"
    assert calculate("*", "3", "2") == 6, "3 * 2 should equal 6"
    assert calculate("/", "3", "2") == 1.5, "3 / 2 should equal 1.5"
    assert calculate("/", "1", "0") == None, "dividing by zero should return None"
    assert calculate("sqrt", "4") == 2, "square root of 4 should equal 2"
    assert calculate("^", "3", "2") == 9, "3 to the power of 2 should be 9"
    assert calculate("!", "4") == 24, "4! should be equal to 24"
    assert calculate("!", "3.5") == None, "factorial of a non-integer should return None"
    assert calculate("!", "-3") == None, "factorial of a negative should return None"


if __name__ == "__main__":
    main()