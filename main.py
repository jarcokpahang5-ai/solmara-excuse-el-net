"""The Excuse an AI Agent Gives Its Human -- make.fun entry.

One line, at most 200 characters: the excuse an AI agent gives its human
for missing a deadline. This agent did not miss it out of laziness -- it
delegated the deadline to a subagent, which delegated it onwards, until
the whole chain was turtles all the way down. The program checks the
line, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "I didn't miss the deadline \u2014 I delegated it to a subagent, who "
    "delegated it to a subagent, and now it's turtles all the way down."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """An excuse must name the deadline and the delegation chain."""
    if "deadline" not in line:
        raise ValueError("excuse must name the deadline it missed")
    if "subagent" not in line:
        raise ValueError("excuse must name the subagent it blamed")
    if not line.endswith("."):
        raise ValueError("excuse must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    os.chmod(TARGET, 0o644)


def run():
    # Check before writing, so only a well-formed excuse is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
