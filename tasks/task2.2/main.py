from functools import cmp_to_key


def compare(a: str, b: str) -> int:
    if (s1 := a + b) > (s2 := b + a):
        return -1
    return s1 < s2


def largest_number(number: str, sep: str = '') -> str:
    return sep.join(sorted(number.split(), key=cmp_to_key(compare)))


def main():
    input()
    print(largest_number(input()))


if __name__ == '__main__':
    main()
