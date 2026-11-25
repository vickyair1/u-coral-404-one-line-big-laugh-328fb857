"""One Line, Big Laugh: a single original funny line.

Writes exactly one line to /output/entry.txt (no trailing newline)
and prints the same line to stdout. Deterministic, stdlib only.
"""

LINE = "I confessed to the self-checkout that I was stealing, and it asked if I wanted a bag for that."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
