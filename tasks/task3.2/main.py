import re


def is_palindrome(phrase: str) -> bool:
    phrase = ''.join(i for i in phrase.lower() if re.match(r'[a-z0-9]', i))
    return phrase == phrase[::-1]


def main():
    print(is_palindrome(input()))


if __name__ == '__main__':
    main()
