from testy.funkcje_matematyczne import silnia
from testy.funk import analyze_pesel
# def test_factor_for_1():
#     assert silnia(1) == 1
# def test_factor_for_2():
#     assert silnia(2) == 2
# def test_factor_for_3():
#     assert silnia(3) == 2*3
# def test_factor_for_4():
#     assert silnia(4) == 2*3*4
# def test_factor_for_5():
#     assert silnia(5) == 2*3*4*5
# def test_factor_for_6():
#     assert silnia(6) == 2*3*4*5*6
# def test_factor_for_7():
#     assert silnia(7) == 2*3*4*5*6*7
# def test_factor_for_8():
#     assert silnia(8) == 2*3*4*5*6*7*8


def test_check_if_analyze_pesel_return_male_ok():
    ret = analyze_pesel("84010529216")
    assert ret['gender'] == 'male'

def test_check_if_analyze_pesel_return_female_ok():
    ret = analyze_pesel("84010532205")
    assert ret['gender'] == 'female'


def test_birth_date_ok():
    ret = analyze_pesel("84010529216")
    year = 1984
    month = 1
    day = 5
    assert ret['birth_date'].year == year
    assert ret['birth_date'].month == month
    assert ret['birth_date'].day == day


def test_birth_date_ok_2021():
    year = 2020
    month = 1
    day = 5
    ret = analyze_pesel("20210521908")
    assert ret['birth_date'].year == year
    assert ret['birth_date'].month == month
    assert ret['birth_date'].day == day

