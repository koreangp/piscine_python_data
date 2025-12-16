"""building.py: count upper/lower/punct/spaces/digits in a text."""

# import building
import sys
from colors import RESET, RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE, BOLD


def analyze_text(object: str):

    str_size = len(object)
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punct = 0
    i = 0

    while i < str_size:
        c = object[i]
        if c.isdigit():
            digit += 1
        elif c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        else:
            punct += 1
        i += 1

    print(f"{GREEN}The text contains {str_size} characters:")
    print(f"{BOLD}{BLUE}{upper} upper letter(s)")
    print(f"{CYAN}{lower} lower letter(s)")
    print(f"{MAGENTA}{punct} punctuation mark(s)")
    print(f"{WHITE}{space} space(s)")
    print(f"{YELLOW}{digit} digit(s){RESET}")


def main() -> int:
    """Entry point of the program."""

    if len(sys.argv) == 1:
        print(f"{BLUE}What is the text to count?{RESET}")
        text = sys.stdin.readline()

    elif len(sys.argv) == 2:
        text = sys.argv[1]

    else:
        print(f"{RED}AssertionError: more than 1 argument is provided{RESET}")
        return (1)
    print(f"{GREEN}\ntext: {YELLOW}{text}{RESET}")

    analyze_text(text)
    # print(building.__doc__)
    return (0)


if __name__ == "__main__":
    main()
