#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    argv = argv[1:]
    argc = len(argv)

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")

    count = 1
    for arg in argv:
        print(f"{count}: {arg}")
        count += 1
