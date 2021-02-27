# n! = 1*2*3*...*(n-2)*(n-1)*n

def silnia(n):
    counter = 1
    wynik = 1
    while counter <= n:
        wynik *= counter
        counter += 1
    return wynik

print("jeste sobie w ciele funkcie matematycznych")
if __name__ == "__main__":
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(4) == 24
    assert silnia(5) == 1120
    assert silnia(6) == 2 * 3 * 4 * 5 * 6
    assert silnia(7) == 2 * 3 * 4 * 5 * 6 * 7
    assert silnia(8) == 2 * 3 * 4 * 5 * 6 * 7 * 8
