#!/usr/bin/python3
"""Calculator program using functions from calculator_1.py"""
import sys
import calculator_1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    operators = {
        '+': calculator_1.add,
        '-': calculator_1.sub,
        '*': calculator_1.mul,
        '/': calculator_1.div
    }

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
