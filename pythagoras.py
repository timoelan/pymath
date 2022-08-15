
from math import sqrt
from emoji import emojize
from sys import argv

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def bluetext(text):
    return f'{OKBLUE}{text}{ENDC}'


def error(message):
    return f'{WARNING}{message}{ENDC}'


def main():

    # print(argv[1:])
    a = None
    b = None
    c = None
    h = None
    A = None

    print(bluetext('Eingabe:'))

    for v in argv[1:]:
        m = v.split('=')
        if m[0] == 'a':
            a = float(m[1])
        if m[0] == 'b':
            b = float(m[1])
        if m[0] == 'c':
            c = float(m[1])
        if m[0] == 'h':
            h = float(m[1])
        if m[0] == 'A':
            A = float(m[1])

    if a is not None:
        print(a)

    if b is not None:
        print(b)

    if c is not None:
        print(c)

    if h is not None:
        print(h)

    if A is not None:
        print(A)

    print(bluetext('Ausgabe:'))

    if A is not None and h is not None:

        c = calculate_c(A, h)
        print(f'Länge c: {c}')

    if a is not None and b is not None:

        c = calculate_c(a, b)
        print(f'Länge c: {c}')

    if c is not None and b is not None:

        a = calculate_a(b, c)
        print(f'Länge a: {a}')

    if c is not None and a is not None:

        b = calculate_b(a, c)
        print(f'Länge b: {b}')

    if c is not None and h is not None:

        A = calculate_A(c, h)
        print(f'Fläche: {A}')

    if a is not None and b is not None:

        A = calculate_A(a, b)
        print(f'Fläche: {A}')

    if A is not None and c is not None:

        h = calculate_h(A, c)
        print(f'Höhe: {h}')

    print(bluetext(emojize('Great Jop:thumbs_up:')))


def calculate_c(a, b):

    return sqrt(a*a + b*b)


def calculate_a(b, c):
    if c <= b:
        raise Exception('C cant be smaler than b')
    return sqrt(c*c - b*b)


def calculate_b(a, c):
    if c <= a:
        raise Exception('C cant be smaler than a')
    return sqrt(c*c - a*a)


def calculate_A(a, b):
    return (a*b/2)


def calculate_h(A, c):
    return (A*2/c)


def calculate_A(c, h):
    return (c*h/2)


def calculate_c_from_h_and_A(A, h):
    return (A*2/h)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(error(f'Error: {e}'))
