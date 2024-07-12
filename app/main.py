import sys
from enum import Enum


class Commands(Enum):
    EXIT = "exit"
    ECHO = "echo"
    TYPE = "type"


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        tokens = cmd.split()
        if tokens[0] == Commands.EXIT.value:
            break
        elif tokens[0] == Commands.ECHO.value:
            sys.stdout.write(" ".join(tokens[1:]) + "\n")
        elif tokens[0] == Commands.TYPE.value:
            if tokens[1] in Commands:
                sys.stdout.write(f"{tokens[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{tokens[1]}: not found\n")
        else:
            sys.stdout.write(f"{cmd}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
