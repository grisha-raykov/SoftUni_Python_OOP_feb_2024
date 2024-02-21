stars = int(input())


def print_upper_rhombus(size):
    for row in range(1, size + 1):
        print(' ' * (size - row), '* ' * row)


def print_bottom_rhombus(size):
    for row in range(size-1, 0, -1):
        print(' ' * (size - row), '* ' * row)


def print_rhombus(size):
    print_upper_rhombus(size)
    print_bottom_rhombus(size)


print_rhombus(stars)
