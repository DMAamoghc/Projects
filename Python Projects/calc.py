import sys
import math

def pythag(a, b):
    a_squared = math.pow(a ,2)
    b_squared = math.pow(b ,2)

    added = a_squared + b_squared

    return math.sqrt(added)


def main():
    userInput = sys.argv[1]

    if  (sys.argv[1] == "add"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x + y)

    if  (sys.argv[1] == "sub"):
        print(int(sys.argv[2]) -int(sys.argv[3]))

    if (userInput == "countto"):
        x = int(sys.argv[2])

        for i in range(x):
            print(i)

    if (userInput == "hypot"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(pythag(x ,y))


if __name__ == "__main__":
            main ()