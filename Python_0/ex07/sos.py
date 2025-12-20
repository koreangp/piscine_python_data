
import sys
from colors import RESET, RED, YELLOW, BOLD, NESTED_MORSE


def main() -> int:
    """entry point"""

    if len(sys.argv) != 2:
        print(f"{BOLD}{RED}AssertionError: the arguments are bad{RESET}")
        return (1)

    text = sys.argv[1]
    bad = [c for c in text if (not c.isalnum() and c != " ")]
    if bad:
        print(f"{BOLD}{RED}AssertionError: the arguments are bad{RESET}")
        return (1)

    text_in_morse = [NESTED_MORSE[c] for c in text.upper()]
    print(f"{BOLD}{YELLOW}{' '.join(text_in_morse)}{RESET}")

    return (0)


if __name__ == "__main__":
    raise SystemExit(main())
