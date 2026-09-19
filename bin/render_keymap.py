#!/usr/bin/env python3
"""Render config/colemak.keymap as docs/colemak.md.

Reads the bindings of every layer in the keymap and lays them out in the
Advantage 360's shape using the key positions documented in
assets/key-positions.md. Run it from the repository root after editing the
keymap, and commit the result:

    python3 bin/render_keymap.py > docs/colemak.md

Pass a layer name to print just that layer's picture without the page
around it:

    python3 bin/render_keymap.py Base
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYMAP = ROOT / "config" / "colemak.keymap"

# Positions per physical row, from assets/key-positions.md. Each row is
# (left keys, left thumb keys, right thumb keys, right keys).
ROWS = [
    ([0, 1, 2, 3, 4, 5, 6], [], [], [7, 8, 9, 10, 11, 12, 13]),
    ([14, 15, 16, 17, 18, 19, 20], [], [], [21, 22, 23, 24, 25, 26, 27]),
    ([28, 29, 30, 31, 32, 33, 34], [35, 36], [37, 38], [39, 40, 41, 42, 43, 44, 45]),
    ([46, 47, 48, 49, 50, 51], [52], [53], [54, 55, 56, 57, 58, 59]),
    ([60, 61, 62, 63, 64], [65, 66, 67], [68, 69, 70], [71, 72, 73, 74, 75]),
]

# Mod-morphs defined in the keymap: (plain, with Shift held).
MORPHS = {
    "n1_pipe": ("1", "|"), "n9_plus": ("9", "+"), "n0_equal": ("0", "="),
    "lparen_lbrace": ("(", "{"), "rparen_rbrace": (")", "}"),
    "lbracket_lt": ("[", "<"), "rbracket_gt": ("]", ">"),
    "colon_semicolon": (":", ";"), "dot_exclamation": (".", "!"),
    "comma_question": (",", "?"), "fslh_bslh": ("/", "\\"),
}

KEYS = {
    "ESC": "ESC", "ESCAPE": "ESC", "TAB": "TAB", "GRAVE": "`", "SQT": "'",
    "MINUS": "-", "BSLH": "\\", "BSPC": "BSPC", "ENTER": "ENT", "SPACE": "SPC",
    "LALT": "LALT", "RALT": "RALT", "LCTRL": "LCTL", "RCTRL": "RCTL",
    "LSHFT": "LSFT", "LSHIFT": "LSFT", "LEFT_SHIFT": "LSFT",
    "RSHFT": "RSFT", "RSHIFT": "RSFT", "LCMD": "CMD",
    "PAGE_UP": "PGUP", "PG_UP": "PGUP", "PAGE_DOWN": "PGDN", "PG_DN": "PGDN",
    "LEFT": "LEFT", "RIGHT": "RGHT", "UP": "UP", "DOWN": "DOWN", "DOWN_ARROW": "DOWN",
    "KP_NUM": "NUM", "KP_EQUAL": "=", "KP_DIVIDE": "/", "KP_MULTIPLY": "*",
    "KP_MINUS": "-", "KP_PLUS": "+", "KP_ENTER": "ENT", "KP_DOT": ".",
}

LAYER_KEYS = {"0": "BASE", "1": "KPD", "2": "FN", "3": "MOD"}

WIDTH = 6
GAP = "      "


def label(binding):
    """Short text for one binding such as '&kp Q' or '&mo 2'."""
    parts = binding.split()
    name, args = parts[0], parts[1:]
    if name == "none":
        return ""
    if name == "trans":
        return "~"
    if name == "kp":
        key = args[0]
        if key in KEYS:
            return KEYS[key]
        if re.fullmatch(r"(KP_)?N\d", key):
            return key[-1]
        return key
    if name in MORPHS:
        return " ".join(MORPHS[name])
    if name in ("tog", "mo"):
        return LAYER_KEYS.get(args[0], "L" + args[0])
    if name == "bt":
        return "BTCLR" if args[0] == "BT_CLR" else "BT " + args[1]
    if name == "bootloader":
        return "BOOT"
    if name == "studio_unlock":
        return "UNLCK"
    if name == "rgb_ug":
        return "BATT" if args[0] == "RGB_MEFS_CMD" else "RGB"
    if name == "bl":
        return {"BL_TOG": "BL", "BL_INC": "BL+", "BL_DEC": "BL-"}.get(args[0], "BL")
    return name.upper()[:WIDTH - 1]


def layers(text):
    """Yield (display name, list of 76 bindings) for each layer."""
    pattern = r"(\w+)\s*\{\s*display-name\s*=\s*\"([^\"]+)\";\s*bindings\s*=\s*<(.*?)>;"
    for m in re.finditer(pattern, text, re.S):
        bindings = [b.strip() for b in m.group(3).split("&") if b.strip()]
        if len(bindings) != 76:
            sys.exit(f"{m.group(2)}: expected 76 bindings, found {len(bindings)}")
        yield m.group(2), bindings


def cell(text):
    return "[" + text.center(WIDTH) + "]"


def picture(bindings):
    """The main rows, then the thumb clusters, as lines of text."""
    left_full = 7 * (WIDTH + 2)
    lines = []
    for left, _, _, right in ROWS:
        row = "".join(cell(label(bindings[i])) for i in left).ljust(left_full)
        lines.append((row + GAP + "".join(cell(label(bindings[i])) for i in right)).rstrip())
    lines.append("")
    lines.append("Thumb keys, left and right")
    pad = " " * (WIDTH + 2)
    l2, r2 = ROWS[2][1], ROWS[2][2]
    l3, r3 = ROWS[3][1], ROWS[3][2]
    l4, r4 = ROWS[4][1], ROWS[4][2]
    lines.append(pad + "".join(cell(label(bindings[i])) for i in l2) + GAP + "".join(cell(label(bindings[i])) for i in r2))
    lines.append(pad * 2 + cell(label(bindings[l3[0]])) + GAP + cell(label(bindings[r3[0]])))
    lines.append("".join(cell(label(bindings[i])) for i in l4) + GAP + "".join(cell(label(bindings[i])) for i in r4))
    return [line.rstrip() for line in lines]


def page(all_layers):
    out = []
    p = out.append
    p("# Colemak layout")
    p("")
    p("This page shows the layout in `config/colemak.keymap`, one picture per")
    p("layer, in the shape of the keyboard. Each half's inner column is the")
    p("column nearest the thumb keys. Don't edit the pictures by hand: this file")
    p("is generated, so regenerate it after changing the keymap.")
    p("")
    p("```")
    p("python3 bin/render_keymap.py > docs/colemak.md")
    p("```")
    p("")
    p("## Reading the pictures")
    p("")
    p("- Two symbols in one key, such as `1 |`, mean the key gives the first")
    p("  symbol on its own and the second with Shift held. See")
    p("  [Shifted symbols](#shifted-symbols).")
    p("- `~` means the key falls through to the layer below.")
    p("- An empty key does nothing on that layer.")
    p("- `KPD` toggles the Keypad layer. `FN` and `MOD` activate the Fn and Mod")
    p("  layers while held.")
    p("")
    for name, bindings in all_layers:
        p(f"## {name} layer")
        p("")
        p("```")
        out.extend(picture(bindings))
        p("```")
        p("")
    p("## Shifted symbols")
    p("")
    p("These keys are mod-morphs: they send one keycode on their own and a")
    p("different one when either Shift is held, instead of the keycode's own")
    p("shifted form.")
    p("")
    p("| Key | Plain | With Shift |")
    p("| --- | --- | --- |")
    for plain, shifted in MORPHS.values():
        # A pipe breaks a GitHub table cell even inside a code span.
        row = [f"`{plain} {shifted}`", f"`{plain}`", f"`{shifted}`"]
        p("| " + " | ".join(c.replace("|", "\\|") for c in row) + " |")
    p("")
    p("## Bootloader and Bluetooth")
    p("")
    p("The Mod layer keeps upstream's positions for these, so the flashing steps")
    p("in the [README](../README.md#flashing-firmware) apply unchanged:")
    p("")
    p("- `MOD` is the top key of the right half's inner column. Hold it.")
    p("- `BOOT` on the left half, the key below `KPD`, puts the left half into")
    p("  the bootloader. `BOOT` on the right half, the key below `MOD`, does the")
    p("  same for the right half.")
    p("- `BT 0` to `BT 4` on the number row select a Bluetooth profile, and")
    p("  `BTCLR` on the right thumb cluster clears the current one.")
    p("- `UNLCK` unlocks ZMK Studio so Kinesis Clique can read the keymap over")
    p("  USB. It only matters on the Clique firmware variant.")
    p("- `BATT` shows battery level on the LEDs; `BL`, `BL+` and `BL-` control")
    p("  the backlight; `RGB` toggles the underglow.")
    return "\n".join(out) + "\n"


def main():
    text = KEYMAP.read_text()
    all_layers = list(layers(text))
    if len(sys.argv) > 1:
        want = sys.argv[1]
        for name, bindings in all_layers:
            if name == want:
                print("\n".join(picture(bindings)))
                return
        sys.exit(f"no layer named {want!r}")
    sys.stdout.write(page(all_layers))


if __name__ == "__main__":
    main()
