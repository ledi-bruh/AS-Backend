def largest_number(numbers: str, sep: str = '') -> str:
    return sep.join(sorted(numbers.split(), key=lambda x: x + x[-1] * (4 - len(x)), reverse=True))


def main():
    input()
    print(largest_number(input()))


if __name__ == '__main__':
    main()
