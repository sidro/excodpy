#!/usb/bin/python3


def doua_val():
    a = 6
    b = 9
    return a, b


def lista(val):
    # a, b = [x for x in val]
    a, b = val
    return a + b


def main():
    a = doua_val()
    print(lista(a))


if __name__ == '__main__':
    main()
