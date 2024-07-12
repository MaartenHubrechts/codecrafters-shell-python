import logging
import os
import sys
from enum import Enum


class Commands(Enum):
    EXIT = "exit"
    ECHO = "echo"
    TYPE = "type"


def find_in_path(cmd: str):
    paths = os.environ.get("PATH", "").split(":")
    for path in paths:
        if os.path.isdir(path) and cmd in os.listdir(path):
            return path
    return None


def main():
    try:
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
                sys.stdout.flush()
            elif tokens[0] == Commands.TYPE.value:
                if tokens[1] in Commands:
                    sys.stdout.write(f"{tokens[1]} is a shell builtin\n")
                    sys.stdout.flush()
                elif find_in_path(tokens[1]):
                    sys.stdout.write(f"{tokens[1]} is {find_in_path(tokens[1])+"/"+tokens[1]}\n")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(f"{tokens[1]}: not found\n")
                    sys.stdout.flush()
            else:
                sys.stdout.write(f"{cmd}: command not found\n")
                sys.stdout.flush()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
