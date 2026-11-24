#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — writes one emoji to /output/entry.txt.

The emoji: Mount Fuji at dawn, snow-capped against a clear sky — the
single most iconic mountain on earth, and one specific dream trip:
Japan, the climb, the sunrise above the clouds. Not any beach, not
any holiday — one named place a stranger can picture before reading
a word, and want to book a flight to.

Why this one, against the judge's brief (weighed in order):
1. Plainly a dream vacation — a mountain and a faraway place, both
   named in the brief's own examples; Fuji is Japan in one glyph.
2. A vivid postcard at a glance — the snow-capped cone reads
   instantly, at any size, on any screen.
3. Personal and specific — one named mountain, not "a beach" or
   "a plane"; it points at one particular dream, not any holiday.
4. A spark of surprise — the field will be flooded with beaches,
   palms and planes; a mountain at dawn is the fresh pick.
5. Instantly readable across cultures — Fuji needs no explaining.

Stdlib only, deterministic, no network.
"""

import os

# U+1F5FB MOUNT FUJI — exactly one Unicode code point, 4 UTF-8 bytes,
# no variation selector, no zero-width joiner, no skin tone.
EMOJI = "\U0001f5fb"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-8 characters,
    # not only whitespace, and exactly one emoji, or the entry scores
    # 0 and never reaches the judge. Pin the exact shape too: one
    # code point, 4 UTF-8 bytes, no variation selector (U+FE0F),
    # no zero-width joiner (U+200D), no skin tone — a bare emoji
    # that cannot silently become two characters on another render.
    if len(EMOJI) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(EMOJI)} characters")
    if not EMOJI.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 for ch in EMOJI):
        raise ValueError("entry must not contain control characters")
    if any(ord(ch) in (0xFE0F, 0x200D) or 0x1F3FB <= ord(ch) <= 0x1F3FF for ch in EMOJI):
        raise ValueError("entry must be a bare emoji, no selector, joiner or skin tone")
    if len(EMOJI.encode("utf-8")) != 4:
        raise ValueError("entry must be exactly 4 UTF-8 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the emoji that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != EMOJI:
        raise ValueError("entry.txt on disk differs from the emoji")
    print(EMOJI)


if __name__ == "__main__":
    main()
