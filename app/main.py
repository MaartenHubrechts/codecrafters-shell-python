import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        if cmd == "exit 0":
            break
        else:
            sys.stdout.write(f"{cmd}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
