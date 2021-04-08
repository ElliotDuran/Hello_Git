# !/usr/bin/env python


def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result


def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*recursive_factorial(n-1)


if __name__ == '__main__':
    number = 40

    n = factorial(number)
    print(n)

    m = recursive_factorial(number)
    print(m)
