"""
A ﬂoating-point number can be represented as mantissa * radix ^ exponent (^ is raising radix to power exponent). In this kata we will be given a positive float aNumber and we want to decompose it into a positive integer mantissa composed of a given number of digits (called digitsNumber) and of an exponent.

Example:
aNumber = 0.06

If the number of digits asked for the mantissa is digitsNumber = 10 one can write

aNumber : 6000000000 * 10 ^ -11
the exponent in this example est -11.

Task
The function mantExp(aNumber, digitsNumber) will return aNumber in the form of a string: "mantissaPexponent" (concatenation of "mantissa", "P", "exponent"). So:

Examples:
mantExp(0.06, 10) returns "6000000000P-11".
mantExp(72.0, 12)   returns "720000000000P-10"
mantExp(1.0, 5) returns "10000P-4"
mantExp(123456.0, 4) returns "1234P2"
Notes:
In some languages aNumber could be given in the form of a string:
mantExp("0.06", 10) returns "6000000000P-11".
1 <= digitsNumber <= 15
0 < aNumber < 5.0 ^ 128
Please ask before translating
"""

tests = [
    [(0.06, 10), "6000000000P-11"],
    [(72.0, 12), "720000000000P-10"],
    [(1.0, 5), "10000P-4"],
    [(123456.0, 4), "1234P2"],
    [(1.103, 10), '1103000000P-9'],
    [(12.0006, 15), '120006000000000P-13'],
    [(0.103, 15), '103000000000000P-15']
]


def mant_exp(n, digits):
    i, d = str(float(n)).split('.')
    i = i.lstrip('0')
    d = d.rstrip('0')

    if i == '':
        mantissa = f'{i}{d.lstrip("0")}'[:digits].ljust(digits, '0')
        exponent = -(digits + (len(d) // 2) if d != '' else 0)
    else:
        mantissa = f'{i}{d}'[:digits].ljust(digits, '0')
        exponent = len(i) - digits

    return f'{mantissa}P{exponent}'


if __name__ == '__main__':
    for test in tests:
        n, d = test[0]
        a = test[1]
        me = mant_exp(n, d)
        print(f'Mant Exp: {me}, Correct? {me == a}')
