#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} argument(s):".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, arg[i]))

    elif size == 1:
        print("{} argument(s):".format(size)) 
        print("{}: {}".format(size, arg[1]))

    else:
        print("{} argument(s).".format(size)
