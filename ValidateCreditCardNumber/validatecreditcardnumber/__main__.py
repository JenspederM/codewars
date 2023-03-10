def isOdd(i) -> bool:
    return i % 2 == 1


def getDigit(number) -> int:
    if number < 9:
        return number
    else:
        return number // 10 + number % 10


def sumOfOddPlace(number) -> int:
    _sum = 0
    number = str(number)
    for i in range(len(number) - 1, -1, -2):
        _sum += int(number[i])
    return _sum


def sumOfDoubleEvenPlace(number) -> int:
    _sum = 0
    number = str(number)
    for i in range(len(number) - 2, -1, -2):
        _sum += getDigit(int(number[i]) * 2)
    return _sum


def validate(number) -> bool:
    return (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0


if __name__ == "__main__":
    number = input("Enter a credit card number as a long integer: ")
    if validate(number):
        print(number, "is valid")
    else:
        print(number, "is invalid")
