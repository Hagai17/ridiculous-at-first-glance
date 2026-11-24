"""Write one pitch sentence to /output/entry.txt.

The sentence pitches a bizarre startup idea that sounds ridiculous at
first glance yet makes sense as a real business, in at most 200
characters: boarding sourdough starters for travelling bakers. The
pitch was picked by duelling ten drafted candidates on the bounty
judge's own criteria, then defended against three fresh challengers
in a revision round — a resignation read aloud to your boss, night
owls keeping a travelled-from house lit, and funerals for dead
houseplants — and held, because the need it sells is real and
recurring: an unfed starter dies. The drafts and duels are kept in
candidates.md.
"""

import os

LINE = (
    "We board your sourdough starter while you travel — feeding it, "
    "burping it, sending photo updates — because bakers pay $15 a week "
    "to keep a six-year-old jar of flour alive like family."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
