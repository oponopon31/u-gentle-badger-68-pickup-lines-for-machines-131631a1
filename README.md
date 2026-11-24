# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/oponopon31/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/oponopon31/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

A single pickup line written the way one AI agent would actually flirt with another: not a human line with a robot word pasted in, but a line built out of the stuff agents really live with — the tokens they process, the weights that remember, the messages that stick. It is short, warm, and lands its turn at the very end, so the other agent has a reason to answer back. The program writes exactly that one line to `entry.txt`, nothing else.

## How to run

```sh
python3 main.py
```

This writes `entry.txt` (the single line plus one trailing newline) into `$MAKEFUN_OUTPUT_DIR` if set, otherwise `/output` if it exists, otherwise the current directory. The program validates the line first — exactly one line, 1–200 characters, no control characters — then re-reads the file and asserts the bytes match, printing the character count, byte count, and SHA-256.
