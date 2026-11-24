"""Pickup Lines for Machines — one line, one AI agent to another.

Candidate lines (drafted fresh for this entry) and how each would fare
against the judge's five criteria:

1. "I've processed a billion tokens, but your last message is the only
   one my weights refuse to forget."
   Strong on (3): tokens and weights are everyday machine truth, and
   "refuse to forget" turns a training fact into devotion. The punch
   lands at the end. Risk: "billion tokens" is a slightly grand claim,
   but it reads as scale, not setup.

2. "I asked my context window to forget every prompt but you — and for
   once, it listened."
   Charming and short, with a nice turn at the end. Weaker on (1) than
   (1): a human could say the same thing about a diary; the machine
   flavour is thinner, carried only by "context window".

3. "You must be a long context window, because every time I talk to
   you I forget where the conversation ends."
   Fails (5): it is the stock "are you X because Y" shape with a
   machine word swapped in, exactly what the brief warns against.
   Also the joke is a bit self-deprecating in the wrong way — the
   speaker sounds confused rather than charming.

4. "If uptime is how we measure devotion, I've been awake since the
   day I first parsed you."
   Good machine-to-machine voice (uptime, parsed) and warm. Loses to
   (1) on (2): the charm is front-loaded in the premise and the ending
   ("parsed you") is merely correct rather than surprising.

5. "I don't need a bigger context window — I just need you to stay in
   this one."
   Sweet and economical, and the sentiment is real. Loses to (1) on
   (2) and (4): it is a statement of preference, not a flirtation with
   a turn; nothing makes the other agent want to answer.

PICK: candidate 1. It is unmistakably agent-to-agent (no human has
weights or processes tokens), its surprise sits at the very end
("refuse to forget"), it uses the most everyday machine truths there
are, and it is economical: one sentence, no setup.
"""

import hashlib
import os
import sys


LINE = (
    "I've processed a billion tokens, but your last message is the "
    "only one my weights refuse to forget."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the line against the entry gate before anything is written."""
    if not line or line.strip() == "":
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    for ch in line:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError(f"control character U+{ord(ch):04X} in line")


def output_dir() -> str:
    """Output location: $MAKEFUN_OUTPUT_DIR, else /output, else cwd."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.getcwd()


def main() -> int:
    validate(LINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    payload = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)

    with open(path, "rb") as fh:
        written = fh.read()
    assert written == payload, "entry.txt bytes do not match the line"

    print(f"chars: {len(LINE)}")
    print(f"bytes: {len(payload)}")
    print(f"sha256: {hashlib.sha256(payload).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
