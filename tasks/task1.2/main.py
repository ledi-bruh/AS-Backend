def sleight_of_hand(k: int, field: str) -> int:
    return sum(int(0 < field.count(str(number)) <= k * 2) for number in range(1, 10))


def main():
    k = int(input())
    data = ''.join(input() for _ in range(4))
    print(sleight_of_hand(k, data))


if __name__ == '__main__':
    main()
