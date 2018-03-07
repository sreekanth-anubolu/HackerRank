
weird = "Weird"
not_weird = "Not Weird"


def is_weird(number):
    is_even = number % 2 == 0
    if not is_even:
        print(weird)
    elif is_even and (number >= 2 and number <= 5):
        print(not_weird)
    elif is_even and (number >= 6  and number <= 20):
        print(weird)
    elif is_even and number > 20:
        print(not_weird)


if __name__ == '__main__':
    n = int(input())
    is_weird(n)
