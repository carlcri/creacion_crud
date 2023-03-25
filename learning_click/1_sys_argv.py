import sys, os

if __name__ == '__main__':

    for indx, item in enumerate(sys.argv):
        if indx == 0:
            print("Name of the program {}".format(sys.argv[0]))
        else:
            print("argument: {}".format(item))