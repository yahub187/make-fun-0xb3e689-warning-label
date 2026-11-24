"""Warning Label for Humans — one-line entry.

Writes a single-line safety warning label (the kind that should come
printed on every human being) to /output/entry.txt. The joke is built
like a real printed label: an iconic "do not operate heavy machinery"
instruction whose list quietly slides from machinery to group chats to
old grudges, then a spec-sheet second sentence whose punch — unlimited
confidence, no undo button — lands in the last few words.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 160

ENTRY_LINE = (
    "WARNING: Do not operate heavy machinery, group chats, or old grudges "
    "after midnight. This model ships with unlimited confidence and no undo button."
)


def checked_entry() -> str:
    """Return the entry line after asserting it fits the sealed gate."""
    assert ENTRY_LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY_LINE) <= MAX_ENTRY_CHARS, "entry must be 1-160 characters"
    ENTRY_LINE.encode("utf-8")  # must be valid UTF-8 text
    return ENTRY_LINE


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(checked_entry())


if __name__ == "__main__":
    main()
