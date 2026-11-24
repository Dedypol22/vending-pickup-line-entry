"""Vending-machine pickup line entry for make.fun.

One line, spoken by the machine itself: its coils have held a thousand
snacks, and not one of them ever made its lights flicker -- until this
passing human. The joke lives in the machine's own world -- coils, snacks,
lights -- and the punch lands in the last few words.
"""

LINE = "My coils have held a thousand snacks, but none of them ever made my lights flicker like you just did."

OUTPUT_FILENAME = "entry.txt"


def output_dir():
    """Return the directory the entry line is written to.

    Honours MAKEFUN_OUTPUT_DIR when set; defaults to /output.
    """
    import os

    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the pickup line to entry.txt with no trailing newline."""
    import os

    # The line must be a single speakable breath: 1-200 chars, one line,
    # no leading/trailing whitespace, and no hidden control characters.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE and LINE, "line must be non-whitespace"
    assert all(ord(ch) >= 32 or ch == "\t" for ch in LINE), "no control chars"

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what landed on disk is exactly the line, no newline.
    with open(path, "rb") as f:
        assert f.read() == LINE.encode("utf-8"), "entry.txt mismatch"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
