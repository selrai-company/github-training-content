#!/usr/bin/env python
"""
Builds dashboard.html from the topic files.

A generator rather than a hand-written page, because a hand-written index goes stale the moment a
topic lands, and this project has already shipped two stale counts exactly that way. Re-run it after
any topic is added or renamed and the dashboard is correct by construction.

Usage: python build-dashboard.py
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.join(HERE, "topics")

GROUPS = [
    ("Start here", "The setup. Do these in order if you are new.", 1, 4),
    ("Doing the work", "The everyday loop, and changing things without breaking them.", 5, 9),
    ("Keeping it safe and tidy", "Protecting work, tracking it, and finding it again.", 10, 16),
    ("Growing up", "The things you reach for as the business gets bigger.", 17, 21),
    ("Staying in control", "Undoing, backing up, and the rest of the platform.", 22, 24),
]

REFERENCE = [
    ("topics/GLOSSARY.md", "Glossary",
     "Every word this kit uses, in plain English, with the ones people mix up kept clearly apart."),
    ("STRATEGY-PACK.md", "Strategy pack",
     "What to do first, whether you need an organisation yet, and how much process is the right amount."),
    ("FAQ-PACK.md", "FAQ pack",
     "Straight answers, including the questions people would rather not ask out loud."),
    ("topics/GAPS.md", "What we could not verify",
     "Every fact GitHub does not publish clearly, so you check your own screen instead of trusting a guess."),
]


def read(path):
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def parse(path):
    text = read(path)
    m = re.search(r"^#\s+(.+)$", text, re.M)
    title = m.group(1).strip() if m else os.path.basename(path)

    blurb = ""
    m2 = re.search(r"^##\s*What this gets you\s*$(.*?)(?=^##\s)", text, re.M | re.S)
    body = m2.group(1) if m2 else text
    for para in body.split("\n\n"):
        line = " ".join(para.split())
        if line.startswith("#"):
            continue
        if line[:1] in ("|", "-", "*", ">", "`"):
            continue
        if len(line) > 40:
            blurb = line
            break
    if len(blurb) > 300:
        blurb = blurb[:297].rsplit(" ", 1)[0] + "..."

    questions = re.findall(r"^###\s+(.{6,140}\?)\s*$", text, re.M)
    return title, blurb, questions[:6]


def main():
    items = []
    if os.path.isdir(TOPICS):
        for name in sorted(os.listdir(TOPICS)):
            m = re.match(r"^(\d\d)-.*\.md$", name)
            if not m:
                continue
            title, blurb, questions = parse(os.path.join(TOPICS, name))
            items.append({
                "n": int(m.group(1)),
                "file": "topics/" + name,
                "title": title,
                "blurb": blurb,
                "qs": questions,
            })

    extras = []
    for rel, label, desc in REFERENCE:
        if os.path.exists(os.path.join(HERE, rel)):
            extras.append({"file": rel, "title": label, "blurb": desc, "qs": []})

    payload = json.dumps({"items": items, "extras": extras}, ensure_ascii=False)
    groups = json.dumps([[g[0], g[1], g[2], g[3]] for g in GROUPS], ensure_ascii=False)

    template = read(os.path.join(HERE, "dashboard-template.html"))
    out = template.replace("__DATA__", payload).replace("__GROUPS__", groups)
    io.open(os.path.join(HERE, "dashboard.html"), "w", encoding="utf-8").write(out)
    print("dashboard.html built: %d topics, %d reference pages" % (len(items), len(extras)))


if __name__ == "__main__":
    main()
