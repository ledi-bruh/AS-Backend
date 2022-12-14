def largest_number(n: int, numbers: str) -> str:
    return ' '.join(sorted(numbers.split(), key=lambda x: x + '9' * (4 - len(x)), reverse=True))


def main():
    print(largest_number(int(input()), input()))


if __name__ == '__main__':
    main()
