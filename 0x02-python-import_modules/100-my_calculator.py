#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    length = len(argv) - 1
    operation = 0

    if length != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(exit(1))

    for count, args in enumerate(argv):
        if count == 0:
