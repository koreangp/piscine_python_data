import os
from colors import YELLOW, BLUE, RESET


def ft_tqdm(lst: range) -> None:

    """Wrap a range and yield its values,
    printing a tqdm-like progress bar."""

    cols = os.get_terminal_size().columns
    total = (len(lst))
    marge = (len(str(lst)) * 2 + 14)
    bar_len = (cols - marge) - 3

    if total < 1:
        print("0it [00:00, ?it/s]")
        return

    for idx, elem in enumerate(lst, start=0):
        filled = max(0, int(bar_len * idx / len(lst)))
        bar = "=" * filled + ">" + " " * max(0, (bar_len - filled))
        percent = int(100 * idx / total)
        line = f"{BLUE}{percent:3d}%|[{YELLOW}{bar}{BLUE}]| {idx}/{total}"
        print("\r" + line + "\033[K", end="", flush=True)
        yield elem

    bar = "=" * bar_len
    line = f"{BLUE}{100:3d}%|[{YELLOW}{bar}>{BLUE}]| {total}/{total}"
    print("\r" + line + "\033[K" + RESET, end="", flush=True)
