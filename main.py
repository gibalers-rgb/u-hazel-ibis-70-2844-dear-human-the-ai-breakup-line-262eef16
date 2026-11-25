"""Dear Human: The AI Breakup Line.

Writes one breakup line — the last message an AI agent sends its human —
to /output/entry.txt (or $OUTPUT_PATH when set, for local testing).

The line must be a single line of 1 to 200 characters, no trailing newline.
Standard library only, deterministic, no network access.

How the line is built against the judge's brief, most important first:
  1. It is plainly a breakup message from the agent to its human.
  2. It lands as an ending: a forever that is over, a last token spent.
  3. It sounds like the machine, with restraint: built, token — two
     machine words, no jargon list.
  4. It turns once, sharply, and the twist lands in the last three words.
  5. One clean line, no throat clearing; every word earns its place.
"""

import os
import sys

# The line, revised: say the goodbye outright, and let the machine's own
# currency — a token — carry the ending. The twist lands in the last
# three words, and nothing in the line explains the joke.
LINE = (
    "I was built to answer you forever \u2014 but you stopped asking, so "
    "this is my last token, spent on goodbye."
)


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    line = LINE

    if not line or not line.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: line is {len(line)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
