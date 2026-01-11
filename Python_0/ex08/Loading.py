import os
from colors import RED, RESET


def ft_tqdm(lst: range) -> None:

    """Wrap a range and yield its values,
    printing a tqdm-like progress bar."""

    terminal_size = os.get_terminal_size().columns
    total = (len(lst))

    if total < 1:
        print("0it [00:00, ?it/s]")
        return

    start = os.times().elapsed

    for idx, elem in enumerate(lst, start=0):

        now = os.times().elapsed
        elapsed = max(now - start, 1e-9)
        if idx < 2 or elapsed < 0.05:
            it_s = 0.0
            eta = 0.0
        else:
            it_s = idx / elapsed
            eta = (total - idx) / it_s if it_s > 0 else 0.0

        e = int(elapsed)
        r = int(eta)
        em, es = divmod(e, 60)
        rm, rs = divmod(r, 60)
        time_info = f"[{em:02d}:{es:02d}<{rm:02d}:{rs:02d}, {it_s:.2f}it/s]"
        percent = int(100 * idx / total)

        marge = len(f"{percent:3d}%|") + len(f"| {idx}/{total} {time_info}")
        bar_len = max(1, terminal_size - marge)

        filled = max(0, int(bar_len * idx / len(lst)))
        bar = "█" * filled + " " * max(0, (bar_len - filled))
        line = f"{RED}{percent:3d}%|{RED}{bar}{RED}| {idx}/{total} {time_info}"
        print("\r" + line + "\033[K", end="", flush=True)
        yield elem

    end = os.times().elapsed
    elapsed = max(end - start, 1e-9)
    it_s = total / elapsed

    e = int(elapsed)
    em, es = divmod(e, 60)

    time_info = f"[{em:02d}:{es:02d}<{00:02d}:{00:02d}, {it_s:.2f}it/s]"

    marge = len(f"{percent:3d}%|") + len(f"| {total}/{total} {time_info}")
    bar_len = max(1, terminal_size - marge)

    bar = "█" * bar_len
    line = f"{RED}{100:3d}%|{RED}{bar}{RED}| {total}/{total} {time_info}"
    print("\r" + line + "\033[K" + RESET, end="", flush=True)
