def is_palindrome(phrase: str) -> bool:
    phrase = ''.join(i for i in phrase.lower() if i.isalnum())
    return phrase == phrase[::-1]


def main():
    print(is_palindrome(input()))


if __name__ == '__main__':
    main()
