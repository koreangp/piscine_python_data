"""ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

from ft_filter import ft_filter
import sys
from colors import RESET, RED, GREEN, YELLOW, BOLD


def main() -> int:
    """entry point"""

    if len(sys.argv) != 3:
        print(f"{RED}AssertionError: the arguments are bad{RESET}")
        return (1)

    try:
        size = int(sys.argv[2])
    except ValueError:
        print(f"{RED}AssertionError: the arguments are bad{RESET}")
        return (1)
    if size < 0:
        print(f"{RED}AssertionError: the arguments are bad{RESET}")
        return (1)

    text = sys.argv[1]
    bad = [c for c in text if (not c.isalnum() and c != " ")]
    if bad:
        print(f"{RED}AssertionError: the arguments are bad{RESET}")
        return (1)

    words = text.split()

    lst = list(ft_filter(lambda x: len(x) > size, words))
    print(f"{BOLD}{YELLOW}{lst}{RESET}")

    new_lst = ft_filter(None, words)
    print(list(new_lst))
    print(list(new_lst))
    print(f"{BOLD}{GREEN}{filter.__doc__}{RESET}")
    print(f"\n{BOLD}{YELLOW}{ft_filter.__doc__}{RESET}")

    return (0)


if __name__ == "__main__":
    main()
