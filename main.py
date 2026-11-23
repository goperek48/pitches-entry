"""A Day of One-Line Pitches — entry program.

Writes one original one-sentence pitch (at most 240 characters) to
/output/entry.txt. The pitch speaks to a friend who has never coded:
describe the idea in plain words, an AI agent builds the first working
version, no code and no setup on their side.
"""

from pathlib import Path

PITCH = (
    "Tell make.fun the app idea you've been sitting on, in your own "
    "words, and an AI agent builds a working first version for you — "
    "no code, no jargon, just your idea turned into something you can "
    "actually click."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate rejects non-UTF-8, >240 chars, or whitespace-only text,
    # so normalise once and validate before writing anything.
    pitch = " ".join(PITCH.split())
    assert pitch and not pitch.isspace(), "pitch must not be blank"
    assert len(pitch) <= 240, f"pitch must be at most 240 chars, got {len(pitch)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(pitch, encoding="utf-8")
    print(f"Wrote one-line pitch ({len(pitch)} chars) to {OUTPUT_PATH}")
    print(pitch)


if __name__ == "__main__":
    main()
