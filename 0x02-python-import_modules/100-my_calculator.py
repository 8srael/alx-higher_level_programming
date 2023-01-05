#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    number_args = len(sys.argv) - 1

    if number_args != 3:
        sys.stderr.write("Usage: {} <a> <operator> <b>\n".format(sys.argv[0]))
        sys.exit(1)

    op = sys.argv[2]

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op in '+-*/':
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
