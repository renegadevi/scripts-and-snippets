#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


def fibonacci(x: int) -> int:
    return 1 if x <= 1 else fibonacci(x-1) + fibonacci(x-2)


def generate_fibonacci(range_end: int = 0, range_start: int = 0) -> list:
    """ Generate a fibonacci list """

    fibonacci_list = []
    for i in range(range_start, range_end):
        fibonacci_list.append(fibonacci(i))

    return fibonacci_list


if __name__ == "__main__":
    while True:
        try:
            range_end = int(input("How many values to generate? "))
            print(exit(generate_fibonacci(range_end)))
        except ValueError:
            print("- Please enter a integer\n")
