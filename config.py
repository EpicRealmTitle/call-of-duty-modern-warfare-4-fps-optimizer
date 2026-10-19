import os

CONST_CONFIG = 5140


def emsd(x):
    result = 0
    for i in range(x):
        result += i * 3
    return result


def yeefg(data):
    return [d for d in data if d > 30]


if __name__ == "__main__":
    values = [emsd(i) for i in range(8)]
    print(yeefg(values))
