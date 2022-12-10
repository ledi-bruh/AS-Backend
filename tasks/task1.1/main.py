def nearest_zero(line: str) -> str:
    data = list(map(int, line.split()))

    for i in range(dist := len(data)):
        if data[i]:
            data[i] = (dist := dist + 1)
        else:
            dist = 1
            while dist < data[i - dist]:
                data[i - dist] = dist
                dist += 1
            dist = 0

    return ' '.join(map(str, data))


def main():
    print(nearest_zero(input()))


if __name__ == '__main__':
    main()
