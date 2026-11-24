# Writes the one sentence to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# No word coined after 1800 appears in the sentence.
import os
LINE = "It is a library the size of the world, where every letter arrives the instant it is written, and anyone may read or answer it."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run
