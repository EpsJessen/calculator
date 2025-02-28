from calculator import calculate
from operators import *

def get_input()-> list[str]:
    query: str = input("What do you want to calculate? ").strip() 
    return query.split(" ")

def print_error(long:bool=True) -> None:
    print("Calculation should be of the shape 'x operator y'")
    if long:
        print("...or 'operator y' if you want to reuse previous result")

def process_loop() -> None:
    first = None
    while True:
        print()
        operands = get_input()
        match len(operands):
            case 1:
                if operands[0] == 'q':
                    break
                operator = operands[0]
                operator_type = string_to_operator_type(operator)
                if (operator_type == OperatorType.UNARY) & (first != None):
                    result = calculate(operator, first)
                    if result == None:
                        continue
                    first = result
                else:
                    print_error()
                    continue
            case 2:
                operator, second = operands
                operator_type = string_to_operator_type(operator)
                match operator_type:
                    case OperatorType.BINARY if first != None:
                        result = calculate(operator, first, second)
                        if result == None:
                            continue
                        first = result
                    case OperatorType.UNARY:
                        result = calculate(operator, second)
                        if result == None:
                            continue
                        first = result
                    case _:
                        print_error(long = False)
                        continue
            case 3:
                first, operator, second = operands
                operator_type = string_to_operator_type(operator)
                match operator_type:
                    case OperatorType.UNARY:
                        print("Unitary operators can only be used in the form 'operator x'\n...or 'operator' if you want to reuse previous result.")
                        continue
                    case OperatorType.BINARY:
                        result = calculate(operator, first, second)
                        if result == None:
                            continue
                        first = result
                    case _:
                        print("Calculation not possible")
                        continue
            case _:
                print("Wrong number of arguments!")
        if first != None:
            print(first)
    

def main() -> None:
    print("\nStarting calculator, input q to quit")
    process_loop()
    print("quitting...")
    

if __name__ == "__main__":
    main()