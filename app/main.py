import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        tokens = cmd.split()
        if tokens[0] == "exit":
            break
        elif tokens[0] == "echo":
            sys.stdout.write(" ".join(tokens[1:]) + "\n")
        else:
            sys.stdout.write(f"{cmd}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
