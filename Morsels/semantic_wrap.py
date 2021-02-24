# semantic wrap
from argparse import ArgumentParser
from pathlib import Path
import re


# SENTENCE_END_RE = re.compile(r'(?<=[.?!])[ ]+')
SENTENCE_END_RE = re.compile(r'([.?!]"?)[ ]+')


def semantic_wrap(text):
    return SENTENCE_END_RE.sub(r"\1\n", text)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    print(semantic_wrap(args.path.read_text()), end='')
