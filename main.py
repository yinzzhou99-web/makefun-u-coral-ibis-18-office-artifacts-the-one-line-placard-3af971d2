"""One-line museum placard for an ordinary office object as an ancient artifact.

Writes the placard to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, deterministic, no network.
"""

import os

LINE = "Catalogue no. 047: Stapler of the Middle Managers, c. 1987. Pressed steel and quiet resentment. Donated by D. Kettle, who stapled his resignation to the fridge and left."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
