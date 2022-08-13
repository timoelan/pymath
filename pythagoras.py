
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


def main():

    # print(argv[1:])
    a = None
    b = None
    c = None

    print(bluetext('Eingabe:'))

    for v in argv[1:]:
        m = v.split('=')
        if m[0] == 'a':
            a = float(m[1])
        if m[0] == 'b':
            b = float(m[1])
        if m[0] == 'c':
            c = float(m[1])

    if a is not None:
        print(a)

    if b is not None:
        print(b)

    if c is not None:
        print(c)

    print(bluetext('Ausgabe:'))

    if a is not None and b is not None:
        c = calculate_c(a, b)
        print(f'Variable c: {c}')

    elif c is not None and b is not None:
        a = calculate_a(b, c)
        print(f'Variable a: {a}')

    elif c is not None and a is not None:
        b = calculate_b(a, c)
        print(f'Variable b: {b}')

    A = calculate_A(a, b)
    print(f'Fläche: {A}')

    h = calculate_h(A, c)
    print(f'Höhe: {h}')

    print(bluetext(emojize('Great Jop:thumbs_up:')))


def calculate_c(a, b):
    return sqrt(a*a + b*b)


def calculate_a(b, c):
    return sqrt(c*c - b*b)


def calculate_b(a, c):
    return sqrt(c*c - a*a)


def calculate_A(a, b):
    return (a*b/2)


def calculate_h(A, c):
    return (A*2/c)


if __name__ == '__main__':
    main()
