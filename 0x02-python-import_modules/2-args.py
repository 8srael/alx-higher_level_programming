#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    args_number = len(sys.argv) - 1

    print("{} arguments".format(args_number), end='')

    if args_number == 0:
        print('.')
    else:
        print(':')
        for i in range(1, args_number + 1):
            print("{}: {}".format(i, sys.argv[i]))
