def convert(num: str, k: int = 2) -> str:
    result, minus = '', ''
    number = int(num)

    if number < 0:
        minus = '-'
        number *= -1

    while number >= k:
        number, ost = divmod(number, k)
        result = str(ost) + result

    return minus + str(number) + result


def main():
    print(convert(input()))


if __name__ == '__main__':
    main()
