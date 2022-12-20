def largest_number(numbers: str) -> str:
    return ''.join(sorted(numbers.split(), key=lambda x: x + x[-1] * (4 - len(x)), reverse=True))


def main():
    print(largest_number(input()))


if __name__ == '__main__':
    main()
