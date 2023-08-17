#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    line = len(sys.argv) - 1

    if line == 0:
        print("0 arguments.")
    elif line == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(line))
    for i in range(line):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
