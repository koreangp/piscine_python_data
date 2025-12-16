"""ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

import ft_filter
import sys
from colors import RESET, RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE, BOLD


def main() -> int:
	print(f"{BOLD}{GREEN}{ft_filter.__doc__}{RESET}")
	return (0)


if __name__ == "__main__":
	main()
