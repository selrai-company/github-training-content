# The practice folder

This is where you try things without any risk at all.

## What is actually in here

Two files about a cafe that does not exist. One holds its opening hours. The other holds a note about
Saturday. That is the whole thing.

They are deliberately pointless. Nobody uses them, nothing depends on them, and no part of your business
touches them. That is what makes them useful. You can change anything here, get it wrong, and it costs
nothing.

## Why practise at all

The first time you change something on GitHub, the screen asks you questions you have not seen before,
and it is hard to tell which answer is safe. That is a bad moment to be having on a real file that
matters to your business.

So have it here first, on a cafe that does not exist.

## The words you will meet, in the order you will meet them

You do not need to memorise these. They are here so that when the screen says one of them, you know what
it is talking about.

**Repository.** A folder for one project, kept online, where a record is saved every time anyone changes
anything. People often shorten it to "repo". This page you are reading is inside one.

**Fork.** Your own complete copy of somebody else's repository, kept in your own account. Changing your
copy has no effect at all on theirs. This is how you practise on someone else's work without touching
it.

**Branch.** A working copy inside a repository, where you can change things without those changes showing
up for anyone else yet. You make a branch, change what you want, and only then decide whether it should
become part of the main version.

**Commit.** Saving a change, with a short note about what you changed and why. Every commit is kept, so
you can always see what happened and when.

**Pull request.** Asking for your changes to be added to the main version. It is a request, not an
action: someone looks at it, and it only becomes real when it is approved and merged. On a repository
you own, that someone is you.

**Merge conflict.** When two people change the same line to two different things, and the system cannot
work out which one is correct. It is not an error and you have not broken anything. It is the system
asking you a question it cannot answer on its own.

## Four things to try, in this order

Each one builds on the last. Do them in order. The first one takes about two minutes.

### One: make your own copy

Go to the front page of this repository:
https://github.com/selrai-company/github-training-content

Look for a button labelled **Fork**. Use it to make your own copy. Everything after this happens in
**your** copy, not in this one, so nothing you do can affect anybody else.

If you cannot find that button, the page layout may have changed since this was written. Read what the
buttons near the top of the page actually say, and use the one that offers to make you a copy.

You will know it worked because the name at the top of the page changes to your own account name.

### Two: change one line

In your copy, open `practice/opening-hours.md`.

Find the line near the bottom that reads `Last changed by: nobody yet` and put your own first name
there instead.

Save it. GitHub will ask you a couple of questions when you save, including a box for a short note about
what you changed. Write anything. "Added my name" is fine.

You have now made a commit. That is the whole of it.

### Three: do it properly, on a branch

Change the same line again, to anything else.

This time, when GitHub asks how you want to save it, choose the option that creates a **new branch**
rather than saving straight to the main version. Give the branch a short name, such as `my-first-change`.

Then open a pull request from that branch. GitHub usually offers this straight after you save, with a
button that mentions a pull request. Write one sentence saying what you changed.

You have now done the thing this training is mostly about. Everything else is a variation on it.

Because it is your own copy, you can approve and merge your own pull request. In a real team, somebody
else would look at it first.

### Four: cause a conflict on purpose, then fix it

This is the one people find frightening, so do it here where it does not matter.

In your copy, open `practice/conflict-practice/saturday-note.md`. One line in it reads
`Saturday: hours not decided yet`. That line, and only that line, is the one to change.

1. Change that line to `Saturday: 8am to 12pm` and save it to a new branch called `saturday-morning`.
2. Go back to the main version of your copy, open the same file again, and change the same line to
   `Saturday: closed`. Save that to a different new branch called `saturday-closed`.
3. Open a pull request from `saturday-closed` into `saturday-morning`.

Both branches changed the same line to two different things, so the system cannot decide which is
correct. It will tell you there is a conflict.

From there, the topic guide on merge conflicts walks you through fixing it.

## A worked example you can look at first

If you would rather see a conflict before you make one, there is one sitting here permanently:

https://github.com/selrai-company/github-training-content/pull/1

It is two branches disagreeing about the Saturday line, left open on purpose so there is always an
example to look at. It is not waiting on anyone and it is not going to be fixed.

## What you cannot break

Worth saying plainly, because the fear of breaking something stops people trying.

You cannot damage this repository by working in your own copy. You have not been given the access
required to change this one, so the system will refuse it rather than let you make a mistake.

You cannot lose your own work either. Every save is kept, so an earlier version is always there.

And if you make such a mess of your own copy that you would rather start again, delete it and make a
fresh copy. It takes about ten seconds and nobody is notified.

## If you get stuck

Post in the community, say which of the four steps you were on, and say what the screen actually said.
That last part is the one that lets somebody help you quickly.
