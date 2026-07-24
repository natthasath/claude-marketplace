# /// script
# requires-python = ">=3.9"
# dependencies = ["Pillow"]
# ///
"""Convert an image to ASCII art (jp2a-style) or ANSI-truecolor art (chafa-style).

Usage:
    uv run image_to_ascii.py photo.jpg --width 100
    uv run image_to_ascii.py photo.jpg --width 100 --color

Requires Pillow. Running via `uv run` installs it automatically in an
ephemeral environment (see the inline script metadata above) — no manual
`pip install` needed. If Pillow is already installed for your interpreter,
plain `python image_to_ascii.py ...` also works.
"""
import argparse

from PIL import Image

RAMP = " .:-=+*#%@"


def load_cells(path, width):
    img = Image.open(path).convert("RGB")
    # Terminal character cells are roughly twice as tall as wide, so shrink
    # the row count to keep the aspect ratio looking correct.
    aspect_correction = 0.5
    height = max(1, int(img.height / img.width * width * aspect_correction))
    return img.resize((width, height))


def render_plain(img):
    lines = []
    for y in range(img.height):
        row = []
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
            row.append(RAMP[int(lum * (len(RAMP) - 1))])
        lines.append("".join(row))
    return "\n".join(lines)


def render_color(img):
    lines = []
    for y in range(img.height):
        row = []
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
            ch = RAMP[int(lum * (len(RAMP) - 1))]
            row.append(f"\x1b[38;2;{r};{g};{b}m{ch}")
        row.append("\x1b[0m")
        lines.append("".join(row))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", help="Path to a JPG/PNG/etc. image file")
    parser.add_argument("--width", type=int, default=100, help="Output width in characters (default: 100)")
    parser.add_argument("--color", action="store_true", help="Emit ANSI truecolor output (chafa-style) instead of plain ASCII (jp2a-style)")
    args = parser.parse_args()

    cells = load_cells(args.image, args.width)
    print(render_color(cells) if args.color else render_plain(cells))


if __name__ == "__main__":
    main()
