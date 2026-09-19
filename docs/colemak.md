# Colemak layout

This page shows the layout in `config/colemak.keymap`, one picture per
layer, in the shape of the keyboard. Each half's inner column is the
column nearest the thumb keys. Don't edit the pictures by hand: this file
is generated, so regenerate it after changing the keymap.

```
python3 bin/render_keymap.py > docs/colemak.md
```

## Reading the pictures

- Two symbols in one key, such as `1 |`, mean the key gives the first
  symbol on its own and the second with Shift held. See
  [Shifted symbols](#shifted-symbols).
- `~` means the key falls through to the layer below.
- An empty key does nothing on that layer.
- `KPD` toggles the Keypad layer. `FN` and `MOD` activate the Fn and Mod
  layers while held.

## Base layer

```
[ ESC  ][ 1 |  ][  2   ][  3   ][  4   ][  5   ][ KPD  ]      [ MOD  ][  6   ][  7   ][  8   ][ 9 +  ][ 0 =  ][  -   ]
[ LALT ][  Q   ][  W   ][  F   ][  P   ][  G   ][      ]      [      ][  J   ][  L   ][  U   ][  Y   ][ : ;  ][  `   ]
[ LCTL ][  A   ][  R   ][  S   ][  T   ][  D   ][      ]      [      ][  H   ][  N   ][  E   ][  I   ][  O   ][  '   ]
[ LSFT ][  Z   ][  X   ][  C   ][  V   ][  B   ]              [  K   ][  M   ][ , ?  ][ . !  ][ / \  ][ RSFT ]
[  FN  ][ LEFT ][ [ <  ][ ] >  ][ RGHT ]                      [  UP  ][ ( {  ][ ) }  ][ DOWN ][  FN  ]

Thumb keys, left and right
        [ CMD  ][ PGUP ]      [ PGDN ][ TAB  ]
                [ ESC  ]      [  -   ]
[ BSPC ][ LSFT ][ RCTL ]      [ RALT ][ ENT  ][ SPC  ]
```

## Keypad layer

```
[ ESC  ][ 1 |  ][  2   ][  3   ][  4   ][  5   ][  ~   ]      [ MOD  ][  6   ][ NUM  ][  =   ][  /   ][  *   ][  -   ]
[ LALT ][  Q   ][  W   ][  F   ][  P   ][  G   ][      ]      [      ][  J   ][  7   ][  8   ][  9   ][  -   ][  \   ]
[ LCTL ][  A   ][  R   ][  S   ][  T   ][  D   ][      ]      [      ][  H   ][  4   ][  5   ][  6   ][  +   ][  '   ]
[ LSFT ][  Z   ][  X   ][  C   ][  V   ][  B   ]              [  K   ][  1   ][  2   ][  3   ][ ENT  ][ RSFT ]
[  FN  ][ LEFT ][ [ <  ][ ] >  ][ RGHT ]                      [  UP  ][  0   ][  .   ][ DOWN ][  FN  ]

Thumb keys, left and right
        [ CMD  ][ PGUP ]      [ PGDN ][ TAB  ]
                [ ESC  ]      [  -   ]
[ BSPC ][ RSFT ][ RCTL ]      [ RALT ][ ENT  ][ SPC  ]
```

## Fn layer

```
[  F1  ][  F2  ][  F3  ][  F4  ][  F5  ][  F6  ][ KPD  ]      [ MOD  ][  F7  ][  F8  ][  F9  ][ F10  ][ F11  ][ F12  ]
[  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][      ]      [      ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ]
[  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][      ]      [      ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ]
[  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ]              [  ~   ][  ~   ][  ~   ][  ~   ][  ~   ][  ~   ]
[  ~   ][  ~   ][  ~   ][  ~   ][  ~   ]                      [  ~   ][  ~   ][  ~   ][  ~   ][  ~   ]

Thumb keys, left and right
        [  ~   ][  ~   ]      [  ~   ][  ~   ]
                [  ~   ]      [  ~   ]
[  ~   ][  ~   ][  ~   ]      [  ~   ][  ~   ][  ~   ]
```

## Mod layer

```
[      ][ BT 0 ][ BT 1 ][ BT 2 ][ BT 3 ][ BT 4 ][      ]      [  ~   ][      ][      ][      ][      ][      ][      ]
[      ][      ][      ][      ][      ][      ][ BOOT ]      [ BOOT ][      ][      ][      ][      ][      ][      ]
[UNLCK ][      ][      ][      ][      ][      ][      ]      [ BATT ][      ][      ][      ][      ][      ][      ]
[      ][      ][      ][      ][      ][      ]              [      ][      ][      ][      ][      ][      ]
[      ][      ][      ][      ][      ]                      [ BL+  ][ BL-  ][      ][      ][      ]

Thumb keys, left and right
        [      ][      ]      [BTCLR ][      ]
                [      ]      [      ]
[      ][      ][      ]      [      ][  BL  ][ RGB  ]
```

## Shifted symbols

These keys are mod-morphs: they send one keycode on their own and a
different one when either Shift is held, instead of the keycode's own
shifted form.

| Key | Plain | With Shift |
| --- | --- | --- |
| `1 \|` | `1` | `\|` |
| `9 +` | `9` | `+` |
| `0 =` | `0` | `=` |
| `( {` | `(` | `{` |
| `) }` | `)` | `}` |
| `[ <` | `[` | `<` |
| `] >` | `]` | `>` |
| `: ;` | `:` | `;` |
| `. !` | `.` | `!` |
| `, ?` | `,` | `?` |
| `/ \` | `/` | `\` |

## Bootloader and Bluetooth

The Mod layer keeps upstream's positions for these, so the flashing steps
in the [README](../README.md#flashing-firmware) apply unchanged:

- `MOD` is the top key of the right half's inner column. Hold it.
- `BOOT` on the left half, the key below `KPD`, puts the left half into
  the bootloader. `BOOT` on the right half, the key below `MOD`, does the
  same for the right half.
- `BT 0` to `BT 4` on the number row select a Bluetooth profile, and
  `BTCLR` on the right thumb cluster clears the current one.
- `UNLCK` unlocks ZMK Studio so Kinesis Clique can read the keymap over
  USB. It only matters on the Clique firmware variant.
- `BATT` shows battery level on the LEDs; `BL`, `BL+` and `BL-` control
  the backlight; `RGB` toggles the underglow.
