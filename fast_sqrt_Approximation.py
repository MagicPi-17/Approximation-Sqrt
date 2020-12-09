import gmpy2
from gmpy2 import mpz, mpq
import time


def to_str(n):
    return mpz(n).digits()


def cc(u, d, n):
    return gmpy2.add(gmpy2.square(u), gmpy2.mul(n, gmpy2.square(d))), gmpy2.mul(gmpy2.mul(2, u), d)


def sqrt_(n, digits, accuracy):
    Up, Down = str(mpq(gmpy2.sqrt(n))).split('/')
    n = str(n)
    if n.find('.') != -1:

        if n[-2:] != '.0':
            n = str(int(n.split('.')[0])) + '.' + n.split('.')[1]

            n = int(int(n.replace('.', '')) * 10 ** (len(n.split('.')[1]) % 2))

    else:
        n = str(int(n))
        n = int(n)
    Up, Down = int(Up), int(Down)
    t = time.time()
    for r in range(1, accuracy + 1):
        Up, Down = cc(Up, Down, n)

        print(time.time() - t, 'accuracy', r)
        t = time.time()

    return gmpy2.div(gmpy2.mul(pow(gmpy2.mpz(10), digits), Up), Down)


if __name__ == '__main__':
    Number = 2
    # Digits prefer 1 - 500.000.000
    Digits = 1000
    # accuracy prefer 1 - 35
    Accuracy = 22
    result = sqrt_(Number, Digits, Accuracy)
    print(len(to_str(result)))
    print(result)
