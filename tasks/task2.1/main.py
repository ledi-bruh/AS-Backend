def psp(n: int, string: str = '', left: int = 0, right: int = 0) -> None:
    if left == n == right:
        print(string)
        return
    if left < n:
        psp(n, string + '(', left + 1, right)
    if right < left:
        psp(n, string + ')', left, right + 1)


def main():
    psp(int(input()))


if __name__ == '__main__':
    main()
