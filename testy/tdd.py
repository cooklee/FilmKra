def prime_factors(number):
    ret_lst = []
    devider = 2
    while number > 1:
        while number % devider == 0:
            ret_lst.append(devider)
            number /= devider
        devider += 1
    return ret_lst


def test_prime_1():
    assert prime_factors(1) == []


def test_prime_2():
    assert prime_factors(2) == [2]


def test_prime_3():
    assert prime_factors(3) == [3]


def test_prime_4():
    assert prime_factors(4) == [2, 2]


def test_prime_5():
    assert prime_factors(5) == [5]


def test_prime_6():
    assert prime_factors(6) == [2, 3]


def test_prime_7():
    assert prime_factors(7) == [7]


def test_prime_8():
    assert prime_factors(8) == [2, 2, 2]


def test_prime_9():
    assert prime_factors(9) == [3, 3]


def test_prime_10():
    assert prime_factors(10) == [2, 5]


def test_prime_18():
    assert prime_factors(18) == [2, 3, 3]


def test_prime_big():
    assert prime_factors(2 * 2 * 3 * 3 * 5 * 7 * 11 * 17) == [2, 2, 3, 3, 5, 7, 11, 17]
