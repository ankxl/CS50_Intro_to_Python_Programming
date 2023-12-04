import re
import sys


def main():
    print(parse(input("HTML: ")))
    # str = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0?si=QbzGkeRL1tLDo3FV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    # parse(str)


def parse(s):
    if matches := re.search(r'^<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_?=]+)".*</iframe>$',s,re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()
