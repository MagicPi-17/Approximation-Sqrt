import math
import time


class Count:
    def div_str(self, n, am):
        find = n.find('.')
        n = n.replace('.', '')
        if find > am:
            find -= am
            return n[:find] + '.' + n[find:]
        else:
            find = am - find
            return '0.' + '0' * find + n

    def cc(self, u, d, n):
        return u ** 2 + n * d ** 2, 2 * u * d

    def countDigits(self, n):
        Up = math.floor(n ** 0.5)
        Down = 1

        for r in range(25):
            if len(str(Up)) > 100000:
                return Up, Down
            Up, Down = self.cc(Up, Down, n)
        return Up, Down

    @staticmethod
    def longDivision(number, divisor):
        # As result can be very large
        # store it in string
        ans = ""

        # Find prefix of number that
        # is larger than divisor.
        idx = 0;
        temp = ord(number[idx]) - ord('0');
        while (temp < divisor):
            temp = (temp * 10 + ord(number[idx + 1]) -
                    ord('0'));
            idx += 1;

        idx += 1;

        # Repeatedly divide divisor with temp.
        # After every division, update temp to
        # include one more digit.
        t = time.time()
        while ((len(number)) > idx):
            t = time.time()

            # Store result in answer i.e. temp / divisor
            ans += chr(math.floor(temp // divisor) + ord('0'));

            # Take next digit of number
            temp = ((temp % divisor) * 10 + ord(number[idx]) -
                    ord('0'))
            idx += 1

        ans += chr(math.floor(temp // divisor) + ord('0'));

        # If divisor is greater than number
        if (len(ans) == 0):
            return "0";

            # else return ans
        return ans

    def sqrt_with_eq(self, n, digits):
        if n.find('.') != -1:
            if n[-2:] != '.0':
                n = str(int(n.split('.')[0])) + '.' + n.split('.')[1]

                mlt = math.ceil(len(n.split('.')[0]) / 2)
                n = int(int(n.replace('.', '')) * 10 ** (len(n.split('.')[1]) % 2))
        else:
            n = str(int(n))
            mlt = math.ceil(len(n) / 2)
            n = int(n)

        number, divisor = self.countDigits(n)

        result1 = self.longDivision(str(number) + '0' * digits, divisor)
        result2 = result1[:mlt] + '.' + result1[mlt:]
        if int(result2.split('.')[1]) == 0:
            result2 = result2.split('.')[0]

        return result2, result1, mlt

    def eq_sqrt1(self, n, mlt):
        eq_sqrt = str(10 ** len(n) - int(n))
        eq_sqrt = eq_sqrt[:mlt] + '.' + eq_sqrt[mlt:]
        eq = str(int(eq_sqrt.replace('.', '')) ** 2)
        eq = eq[:len(str(int(eq_sqrt.split('.')[0]) ** 2))] + '.' + eq[len(str(int(eq_sqrt.split('.')[0]) ** 2)):]

        if int(eq.split('.')[1]) == 0:
            eq = eq.split('.')[0]
        if int(eq_sqrt.split('.')[1]) == 0:
            eq_sqrt = eq_sqrt.split('.')[0]

        return eq, eq_sqrt

    def example(self, n, digits):
        # number as str, digits as int
        n_sqrt = self.sqrt_with_eq(n, int(digits))
        eq_sqrt = self.eq_sqrt1(n_sqrt[1], n_sqrt[2])
        return n_sqrt[0], eq_sqrt[0], eq_sqrt[1]

    def sqrt(self, n, digits):
        # number as str, digits as int
        n_sqrt = self.sqrt_with_eq(n, int(digits))
        return n_sqrt[0]


if __name__ == '__main__':
    n = input('Number = ')
    Digits = input('Digits = ')
    Number_sqrt, Equivalent_number, Equivalent_sqrt = Count().example(n, Digits)
    Number_sqrt_only = Count().sqrt(n, Digits)
    print(Number_sqrt_only)
    print(Number_sqrt)
    print(Equivalent_number)
    print(Equivalent_sqrt)
