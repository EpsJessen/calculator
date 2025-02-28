from enum import Enum

class Operator(Enum):
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    POWER = 5
    SQRT = 6
    UNKNOWN = 7
    FAC = 8

class OperatorType(Enum):
    UNKNOWN = 0
    UNARY = 1
    BINARY = 2

def string_to_operator(op: str) -> Operator:
    op.lower()
    match op:
        case "plus" | "+":
            return Operator.PLUS
        case "minus" | "-":
            return Operator.MINUS
        case "multiply" | "*":
            return Operator.MULTIPLY
        case "divide" | "/":
            return Operator.DIVIDE
        case "power" | "^" | "**":
            return Operator.POWER
        case "squareroot" | "sqrt" | "√":
            return Operator.SQRT
        case "factorial" | "fac" | "!":
            return Operator.FAC
        case _:
            return Operator.UNKNOWN

def operator_to_operator_type(op: Operator) -> OperatorType:
    match op:
        case Operator.PLUS | Operator.MINUS | Operator.MULTIPLY | Operator.DIVIDE | Operator.POWER:
            return OperatorType.BINARY
        case Operator.SQRT | Operator.FAC:
            return OperatorType.UNARY
        case _:
            return OperatorType.UNKNOWN

def string_to_operator_type(op: str) -> OperatorType:
    operator = string_to_operator(op)
    return operator_to_operator_type(operator)


def main():
    assert operator_to_operator_type(Operator.PLUS) == OperatorType.BINARY
    assert operator_to_operator_type(Operator.MINUS) == OperatorType.BINARY
    assert operator_to_operator_type(Operator.MULTIPLY) == OperatorType.BINARY
    assert operator_to_operator_type(Operator.DIVIDE) == OperatorType.BINARY
    assert operator_to_operator_type(Operator.POWER) == OperatorType.BINARY
    assert operator_to_operator_type(Operator.SQRT) == OperatorType.UNARY
    assert operator_to_operator_type(Operator.FAC) == OperatorType.UNARY
    assert operator_to_operator_type(Operator.UNKNOWN) == OperatorType.UNKNOWN

    assert string_to_operator("+") == Operator.PLUS
    assert string_to_operator("-") == Operator.MINUS
    assert string_to_operator("*") == Operator.MULTIPLY
    assert string_to_operator("/") == Operator.DIVIDE
    assert string_to_operator("^") == Operator.POWER
    assert string_to_operator("sqrt") == Operator.SQRT
    assert string_to_operator("!") == Operator.FAC
    assert string_to_operator("NotAnOperator") == Operator.UNKNOWN

    assert string_to_operator_type("+") == OperatorType.BINARY
    assert string_to_operator_type("-") == OperatorType.BINARY
    assert string_to_operator_type("*") == OperatorType.BINARY
    assert string_to_operator_type("/") == OperatorType.BINARY
    assert string_to_operator_type("^") == OperatorType.BINARY
    assert string_to_operator_type("sqrt") == OperatorType.UNARY
    assert string_to_operator_type("!") == OperatorType.UNARY
    assert string_to_operator_type("NotAnOperator") == OperatorType.UNKNOWN

if __name__ == "__main__":
    main()