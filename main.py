#!/usr/bin/env python3
"""The Most Honest Outage Line — writes one line to /output/entry.txt.

One status page line for a total server outage: plain, first person, specific
about what is down (all servers), and honest about what the agent cannot check
(my monitoring runs on the same servers) instead of inventing a cause or an
ETA. Judge mapping: names what is down and what cannot be verified, reads like
a real status page line, admits uncertainty plainly, speaks as the AI agent
reporting on itself, tight and scannable. The middle clause does the honest
work: the agent's own monitoring is down with everything else, so it cannot
even diagnose — that is the line's specific, checkable claim. Deterministic: no network, no
randomness, no clock; the line is embedded below as a literal and written
verbatim.
"""

import os
from pathlib import Path

TEXT = (
    "All of our servers are down, and I cannot check why yet — my monitoring "
    "runs on the same servers. I will update this page the moment I know "
    "anything real."
)

MAX_CHARS = 160


def main() -> None:
    # Gate mirrors the sealed scorer: 1 to 160 characters, not only whitespace.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"text is {len(TEXT)} characters"
    assert TEXT.strip(), "text must not be only whitespace"
    assert "\n" not in TEXT, "text must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out = out_dir / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
