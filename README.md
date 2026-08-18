# Practice repo

This is a practice sandbox. It exists so you can try out branches, commits and pull requests on
something that does not matter, before you try them on anything that does.

Nothing in here is part of your business. Nothing in here is software. Nothing in here runs. It is a
few text files about a pretend cafe, and they are here to be scribbled on.

## You cannot break anything

Three reasons, and all three are true at the same time.

1. You do not work on this copy. You make your own copy first, which is called a fork. Your changes
   land in your copy, not in this one.
2. There is nothing here to break. No app, no automation, no keys, no passwords, no connection to any
   account of yours. Just text files.
3. Even if you delete everything in your copy, this original is untouched, and you can throw your copy
   away and make a fresh one in about ten seconds.

If you feel nervous the first time, that is normal, and this repo is the right place to feel it.

## What is in here

| File | What it is for |
| --- | --- |
| `README.md` | This page. |
| `opening-hours.md` | The file to practise editing. Pretend opening hours for a pretend cafe. |
| `conflict-practice/saturday-note.md` | The file used for the merge conflict practice. Leave it alone until you get to that part. |
| `.gitignore` | A ready made list of files git should never upload. Copy it into your own projects. |

That is the whole repo. If you are looking for something else, it is not here on purpose.

## What to do here

You can do all of this in your web browser. You do not need to install anything.

1. Make your own copy of this repo, using the Fork button at the top of the page.
2. In your copy, open `opening-hours.md`.
3. Change something. Change the Sunday line, or put your first name on the last line. It does not
   matter what you change.
4. Save it as a new branch instead of saving straight to the main copy, and give the branch a short
   name like `my-first-change`.
5. Open a pull request from your branch back to this repo, and write one sentence saying what you
   changed.

That is the whole loop. When you have done it once, you have done the thing the lesson is teaching.

## The merge conflict practice

A merge conflict happens when two changes disagree about the same line, and git will not guess which
one you meant. It is not an error and it is not something you did wrong. It is git asking you a
question.

`conflict-practice/saturday-note.md` has one line in it that is deliberately undecided:

```
Saturday: hours not decided yet
```

To make the two sides disagree, in your own copy:

1. Edit that file and change only that line to `Saturday: 8am to 12pm`. Save it to a new branch named
   `saturday-morning`.
2. Go back to the main copy of your fork, edit the same file again, and change the same line to
   `Saturday: closed`. Save it to a new branch named `saturday-closed`.
3. Open a pull request from `saturday-closed` into `saturday-morning`, both inside your own copy.

You now have two branches that each changed the same line to something different, which is exactly
what a merge conflict is. Your lesson picks it up from there.

Two branches named `example-saturday-morning` and `example-saturday-closed` also already exist here,
so you can look at what the two sides of the disagreement look like before you make your own. They are
named differently from the branches you are asked to make above, on purpose, so they never clash with
yours.

## What happens to your pull request

We read it. Usually we leave a short comment and then close it, and closing it is not a rejection. It
keeps this repo sitting at the same starting point for the next person who arrives. Your copy and your
pull request stay in your account either way, so you keep the thing you made.

## The .gitignore, and why it is the important file here

`.gitignore` is a list of files git is told to leave alone. The line that matters is the one for
`.env`, because a `.env` file is where keys and passwords usually live, and uploading one by accident
is the single most expensive mistake a beginner makes with git.

Copy that file into your own projects. It is short on purpose so you can read all of it.

## Reuse

Everything in this repo is free for you to copy, change and reuse, in your own work or anywhere else.
There is nothing here we want back.

## If you get stuck

Post in the community and say which step you were on and what you saw on the screen. That is enough
for someone to help you.
