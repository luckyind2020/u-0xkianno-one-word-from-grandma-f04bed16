"""One Word From Grandma — the single word a grandma would text about AI."""

from pathlib import Path


def load_word() -> str:
    path = Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return "Witchcraft"
    # The entry must be exactly one word; keep only the first token.
    return text.split()[0]


if __name__ == "__main__":
    print(load_word())
