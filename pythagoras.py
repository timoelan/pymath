from math import sqrt

from sys import argv


def main():

    # print(argv[1:])
    a = None
    b = None
    c = None

    for v in argv[1:]:
        m = v.split('=')
        if m[0] == 'a':
            a = float(m[1])
        if m[0] == 'b':
            b = float(m[1])
        if m[0] == 'c':
            c = float(m[1])

    if a is not None and b is not None:
        c = calculate_c(a, b)
        print(c)

    elif c is not None and b is not None:
        a = calculate_a(b, c)
        print(a)

    elif c is not None and a is not None:
        b = calculate_b(a, c)
        print(b)


def calculate_c(a, b):
    return sqrt(a*a + b*b)


def calculate_a(b, c):
    return sqrt(c*c - b*b)


def calculate_b(a, c):
    return sqrt(c*c - a*a)


if __name__ == '__main__':
    main()
