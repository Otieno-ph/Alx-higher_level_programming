#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv) - 1
    word = "arguments"

    if length == 0:
        print(f"{length} {word}.")
    elif length != 1:
        print(f"{length} {word}:")
    else:
        word = "argument"
        print(f"{length} {word}:")
