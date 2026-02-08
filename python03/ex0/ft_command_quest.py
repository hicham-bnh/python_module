"""
Command Quest

This program displays the program name, the number of command-line
arguments provided, and lists each argument passed to the script.
"""
import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {(len(sys.argv) - 1)}")
        for n in range(len(sys.argv) - 1):
            n += 1
            print(f"Argument {n}: {sys.argv[n]}")
    print(f"Total arguments: {len(sys.argv)}")
