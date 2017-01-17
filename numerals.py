import operator

SYMBOLS = [
    (1, 'I'),
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M'),
]


def _find_greatest_lower_bound(x):
    for n, symbol in reversed(SYMBOLS):
        if n <= x:
            return (n, symbol)
    raise TypeError("Impossible to find number")


def roman(x):
    x = operator.index(x)
    if not (0 < x < 5000):
        raise TypeError("Only numbers in (0, 5000) interval are accepted")
    numeral = ''
    while x > 0:
        n, symbol = _find_greatest_lower_bound(x)
        numeral += symbol
        x -= n
    return numeral
