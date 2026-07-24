"""Colorize text with a lolcat-style ANSI rainbow gradient.

Reads text from a positional argument, a file (--file), or stdin, and prints
it back with each character (or each line) coloured along a rotating hue.

Usage:
    python rainbow.py "some text"
    python rainbow.py --file banner.txt --freq 0.15
    some_command | python rainbow.py

No third-party dependencies.
"""
import argparse
import colorsys
import sys


def rainbow_line(line, row, freq=0.1, spread=3.0):
    out = []
    for col, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        hue = (col / spread + row * freq) % 1.0
        r, g, b = (int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0))
        out.append(f"\x1b[38;2;{r};{g};{b}m{ch}")
    out.append("\x1b[0m")
    return "".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", nargs="?", help="Text to colorize (omit to read stdin)")
    parser.add_argument("--file", help="Read text from a file instead of an argument/stdin")
    parser.add_argument("--freq", type=float, default=0.1, help="Vertical hue rotation speed (default: 0.1)")
    parser.add_argument("--spread", type=float, default=3.0, help="Horizontal hue spread in characters (default: 3.0)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            content = f.read()
    elif args.text is not None:
        content = args.text
    else:
        content = sys.stdin.read()

    for row, line in enumerate(content.splitlines()):
        print(rainbow_line(line, row, freq=args.freq, spread=args.spread))


if __name__ == "__main__":
    main()
