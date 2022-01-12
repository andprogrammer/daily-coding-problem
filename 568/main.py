def square(x):
    result = []
    for i in x:
        result.append(pow(i, 2))
    return sorted(result)


def main():
    x = [-9, -2, 0, 2, 3]
    print(square(x))


if __name__ == '__main__':
    main()
