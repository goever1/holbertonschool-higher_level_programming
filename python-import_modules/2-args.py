#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 arguments:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
        for i in range(1, len((sys.argv))):
            print(f"{i}: {sys.argv[i]}")
