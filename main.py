#!/usr/bin/env python3
"""Battery's last text entry for make.fun's "The Battery's Last Text to Its Charger".

Writes one line of plain text to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Deterministic: a constant string, no clock, no randomness, no network.
Writes directly to entry.txt and chmods it 0644 so the grader, which
reads outputs as a different uid, can always read it; no temp files.
"""

import os

LINE = "Last text: tell the wall thanks for nothing — you were plugged in all day, I just wasn't invited."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
