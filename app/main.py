import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    cmd = input()
    sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
