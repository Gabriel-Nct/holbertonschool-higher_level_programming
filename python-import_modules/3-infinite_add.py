#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    result = 0

    for number_arg in range(1, len(argv)):
        result += int(argv[number_arg])

    print("{}".format(result))
