# SPDX-License-Identifier: MIT
"""Write the entry word to /output/entry.txt.

The word this entry would erase from the dictionary forever: "delete".
Deleting "delete" is the joke itself: the dictionary loses the very word
for removing things, so nothing in it can ever be deleted again.
The entry is exactly one word, spelled correctly, with nothing added.
"""

import os

WORD = "delete"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
