import pytest

from numerals import roman, _find_greatest_lower_bound


def test_negative_is_invalid():
    with pytest.raises(TypeError):
        roman(-7)


def test_zero_is_invalid():
    with pytest.raises(TypeError):
        roman(0)


def test_5000_is_invalid():
    with pytest.raises(TypeError):
        roman(5000)


def test_float_is_invalid():
    with pytest.raises(TypeError):
        roman(2.5)


def test_zero_not_found():
    with pytest.raises(TypeError):
        _find_greatest_lower_bound(0)


def test_find_one():
    assert (1, 'I') == _find_greatest_lower_bound(1)


def test_one_is_converted():
    assert "I" == roman(1)


def test_49_is_converted():
    assert "XLIX" == roman(49)


def test_4000_is_converted():
    assert "MMMM" == roman(4000)


def test_2216_is_converted():
    assert "MMCCXVI" == roman(2216)


def maximum_three_consecutive(numeral):
    for i in range(len(numeral) - 3):
        if numeral[i] != 'M':
            assert len(set(numeral[i:])) != 1


def all_subtractions_allowed(numeral):
    for i in range(len(numeral) -1 ):
        if numeral[i + 1] == 'X':
            assert numeral[i] != 'V'
        elif numeral[i + 1] == 'L':
            assert numeral[i] not in ["I", "V"]
        elif numeral[i + 1] == 'C':
            assert numeral[i] not in ["I", "V", "L"]
        elif numeral[i + 1] == 'D':
            assert numeral[i] not in ["I", "V", "X", "L"]
        elif numeral[i + 1] == 'M':
            assert numeral[i] not in ["I", "V", "X", "L", "D"]


def arithmetic_equivalence(n, numeral):
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    x = 0
    for i in range(len(numeral) - 1):
        a = map[numeral[i]]
        b = map[numeral[i + 1]]
        if a < b:
            x -= a
        else:
            x += a
    x += map[numeral[-1]]
    assert x == n


def test_invariants():
    for n in range(1, 5000):
        numeral = roman(n)
        maximum_three_consecutive(numeral)
        arithmetic_equivalence(n, numeral)
        all_subtractions_allowed(numeral)
