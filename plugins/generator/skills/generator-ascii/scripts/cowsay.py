"""Wrap text in a speech bubble next to an ASCII cow (cowsay-inspired).

Usage:
    python cowsay.py "Hello world" [--width 40] [--eyes oo] [--think]

No third-party dependencies.
"""
import argparse
import textwrap


def build_bubble(text, width=40, think=False):
    lines = []
    for paragraph in text.splitlines() or [""]:
        wrapped = textwrap.wrap(paragraph, width=width) or [""]
        lines.extend(wrapped)
    inner = max(len(line) for line in lines)
    top = " " + "_" * (inner + 2)
    bottom = " " + "-" * (inner + 2)
    body = []
    left, right = ("(", ")") if think else ("<", ">")
    if len(lines) == 1:
        body.append(f"{left} {lines[0].ljust(inner)} {right}")
    else:
        body.append(f"/ {lines[0].ljust(inner)} \\")
        for line in lines[1:-1]:
            body.append(f"| {line.ljust(inner)} |")
        body.append(f"\\ {lines[-1].ljust(inner)} /")
    return "\n".join([top] + body + [bottom])


def build_cow(eyes="oo", think=False):
    connector = "o" if think else "\\"
    tail = "o   ^__^" if think else "\\   ^__^"
    return "\n".join([
        f"        {tail}",
        f"         {connector}  ({eyes})\\_______",
        "            (__)\\       )\\/\\",
        "                ||----w |",
        "                ||     ||",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="Message for the cow to say")
    parser.add_argument("--width", type=int, default=40, help="Bubble wrap width (default: 40)")
    parser.add_argument("--eyes", default="oo", help="Two-character eyes, e.g. 'oo', '--', '**' (default: oo)")
    parser.add_argument("--think", action="store_true", help="Use a 'thinking' bubble instead of speech")
    args = parser.parse_args()
    print(build_bubble(args.text, width=args.width, think=args.think))
    print(build_cow(eyes=args.eyes, think=args.think))


if __name__ == "__main__":
    main()
