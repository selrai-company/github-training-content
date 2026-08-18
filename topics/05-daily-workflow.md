# The everyday workflow, and getting work in and out

## What this gets you

This is the loop you run every time you need to change something and keep it safe: get a
working copy of your files, make the change, save it with a note about what changed, and
keep that copy current as anyone else changes things too. For a small business, it replaces
emailing a document back and forth, saving five copies with "final," "final2," and
"final_ACTUAL" in the name, and never being sure which one is the one that's actually live.
Every change is saved with its own timestamp, its own author, and its own note explaining
what happened, so nothing gets lost and nobody has to guess which file is the real one.

By the end of this page you'll be able to get a repository onto your machine two different
ways, make a small change through the browser and commit it properly, explain in one
sentence what a commit message is for, and pull the latest version down without overwriting
your own work.

## Before you start

**You need somewhere to work from.** Your own repository, or one you've been given access
to. If you haven't created one yet, `04-repositories-and-visibility.md` covers that first.

**You need Claude Code available as a second option alongside the browser.** This page
assumes it's already running, on the Max plan, the same as every page in this kit. If you
haven't opened Claude Code before, its own setup isn't covered here, this page only covers
what to ask it once it's running.

**You need at least Read access to get a copy of anything at all**, and Write access if you
want to commit a change directly the way this page describes. `03-members-and-access.md`
covers checking your own access level if you're not sure what it is.

**You don't need to already know what git is, or what a branch or a pull request are.**
Nothing on this page requires typing a git command yourself, and the loop this page covers
works whether or not anyone else is involved. `06-branches.md` and `07-pull-requests.md`
build on this page for the team version of the loop; they're not required reading before it.

**One naming convention used throughout this page:** wherever it says "the repository's main
page," that means an address shaped like `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY`.
Replace both capitalised parts with your own organisation or username, and your own
repository's name, since a real repository address is unique to you and can't be given here
as a working link.

## The words you need

**Branch.** A private copy of the work you can change without touching the version everyone
else sees, until you decide it's ready to be brought back in. This page covers the loop that
doesn't use one, changing the main version directly. `06-branches.md` covers branching in
full.

**Pull request.** A request to bring a branch's changes into the main version, with a chance
for someone else to look at it first before it lands. Covered in full in
`07-pull-requests.md`; this page only touches it in passing, to say when you'd reach for it
instead of the direct loop.

**Clone.** A full copy of a repository, including its entire history, that stays connected to
GitHub so you can pull down new changes into the same folder later, rather than downloading
it all again from scratch.

**Terminal.** The text-based window where git commands are normally typed by hand. You won't
need to open one for anything on this page. Claude Code runs the underlying commands for you
and tells you what it did.

**GitHub CLI (`gh`).** GitHub's own command-line tool. It's the thing that needs to be
installed and signed in on your machine before Claude Code, acting as you, can clone or work
with a repository that isn't public.

**Fork.** Your own personal copy of a repository, made automatically by GitHub the moment you
try to edit a file you don't have Write access to, so your change can be proposed back as a
pull request instead of committed directly into the original. Covered fully in
`09-forks-and-contributing.md`.

**Commit.** A saved snapshot of a change. GitHub's own description: it "records changes to
one or more files," and every commit gets its own unique ID, a timestamp, and the name of
whoever made it. Once committed, that snapshot is permanent history, you can always come back
and see exactly what a file looked like at that point.

**Commit message.** The one line, or few lines, that says what a commit actually changed and
why. GitHub requires you to write something here, its own wording: you "must include a commit
message that briefly describes the changes." It doesn't enforce a length, a format, or any
specific wording, that part is up to you.

**`git pull`.** The underlying command Claude Code runs when you ask it to fetch the newest
version of a repository you've already cloned. GitHub's own documentation describes it
plainly: it "grabs online updates and merges them with your local work" in one step.

**Merge conflict.** What happens when you and someone else changed the same part of the same
file, and GitHub can't automatically decide which version to keep. Covered fully in
`08-merge-conflicts.md`; this page only tells you when you're likely to run into one.

## How to do it

### The basic loop, in plain English

Every team using GitHub, no matter how small, runs some version of the same loop: **someone
changes something, it gets looked at, and then it lands.**

There are two honest versions of that loop, and which one you're running depends on who else
is involved.

**Solo, or a change nobody needs to check first.** You edit a file, you commit it, it's live.
No review step. This is normal and fine for your own repository, or for small changes to a
repository you fully control. The rest of this section covers exactly this loop, start to
finish.

**A team, or a change that should get a second pair of eyes first.** The change happens on
its own branch, gets proposed for review as a pull request, someone looks at it, and only
then does it land in the version everyone else sees. That's the loop most small businesses
grow into once more than one person is touching the same repository regularly. It's covered
in full in `06-branches.md` and `07-pull-requests.md`, and what to do when two people change
the same thing at once is `08-merge-conflicts.md`.

You don't have to pick one forever. Plenty of small teams run the simple loop for quick fixes
and the reviewed loop for anything bigger. What matters today is knowing which loop you're in
before you start, not partway through.

### Getting a copy of a repository onto your machine

There are two genuinely different ways to do this, and they're not interchangeable. Pick
based on whether you'll ever need to update this copy later.

**Option 1: Download it as a ZIP (browser, no install, no history)**

1. Open the repository's main page on github.com, the landmark every step below starts from.
2. Along the top of the file list, look for the green **Code** button.
3. Click it, then click **Download ZIP** in the panel that opens.

GitHub's own words: this gives you "a compressed (zipped) copy of all the files in that
repository as it currently exists," and no git installation is required for this method at
all. You'll know it worked because a `.zip` file appears in your browser's usual download
location a few seconds after you click, most setups save it into a folder literally named
**Downloads**.

The one thing worth knowing before you rely on it: GitHub's own documentation is direct that
"snapshots don't contain the entire repository history," so a ZIP is a one-time photo of the
files as they are right now, not a copy that remembers how they got that way, or that can be
updated in place.

**Screenshot placeholder:** the green Code button clicked open, showing the HTTPS, SSH,
GitHub CLI tabs and the separate Download ZIP link underneath, so a reader can see all the
options in one place before choosing.

**If the Code button offers connection options but you can't find Download ZIP at all,**
scroll the same panel, it's usually the last item underneath the other tabs rather than a tab
of its own. If the button isn't there in any form, you likely don't have at least Read access
to this repository, `03-members-and-access.md` covers checking that.

Use this when you just need the files once, to look at or use right now, and you're not
planning to come back for updates.

**Option 2: Ask Claude Code to clone it (keeps a live connection, full history)**

Getting a clone normally means typing a `git clone` command in a terminal. You don't have to
do that yourself.

1. On the repository's main page, click the green **Code** button and copy the **HTTPS**
   link, the copy icon sits next to it.
2. Tell Claude Code, in plain English: "Clone this repository for me: " and paste the link.
3. Claude Code runs the clone for you and reports back where it put the folder.

You'll know it worked because Claude Code's reply names a specific folder path, not just a
confirmation that it's "done." Read that path, don't skip past it, the next section covers
why.

For a public repository, this needs nothing signed in, just Claude Code and the link. For a
private repository, you, and by extension Claude Code acting as you, need to already be
signed in to GitHub on that machine, which usually means the GitHub CLI (`gh`) is installed
and authenticated. That's a genuinely good one-time setup to have, but getting it working the
first time isn't covered in this file. If it's not set up yet, use the ZIP path above instead
for now.

**Either way, you need at least Read access to the repository to get a copy of it at all.**
GitHub's own requirement, stated plainly: "you have permission to access the repository you
want to clone." If you can't see the repository, or the Code button doesn't offer you a clone
link, that's a permissions question, covered in `03-members-and-access.md`, not something
wrong with these steps.

Use this when you expect to come back to this repository more than once, want to keep it
current, or think you might eventually contribute a change back to it.

### Where the files actually end up (don't lose the folder)

This is the part that quietly derails more beginners than anything else on this page. GitHub
tells you where a browser download or a Claude Code clone landed. Your job is to actually
read that, and write it down if you need to.

**If you downloaded the ZIP:** it lands wherever your browser normally saves downloads, on
most setups that's a folder literally named **Downloads**. A ZIP file isn't usable as-is, you
need to extract it first, which creates a new folder with the repository's name inside
whatever folder the ZIP itself was saved to. Check your own browser's download settings if
you're not sure where that is, this is a setting specific to your computer, not something
GitHub controls.

**If Claude Code cloned it:** the folder lands wherever you were working when you asked, or
wherever you told it to put it, and it's named after the repository. Claude Code tells you the
full path when it finishes. If you lose track of it later, just ask: "Where did you put the
copy of [repository name] you cloned earlier?" and it will tell you again, or find it for you.
Don't rely on memory for this one, ask.

**A habit worth building either way:** the first time you get a copy of something you'll want
to work in more than once, decide on one place on your machine for GitHub-related folders (a
folder called `GitHub` inside your Documents, for instance) and always point Claude Code there
when you ask it to clone something. That one habit is the entire fix for "I don't know where
any of my repos went."

### Making a change through the browser

For a quick, single-file edit, the browser is faster than asking Claude Code to do it, and
it's the right tool for this specific job.

1. Open the file you want to change, inside the repository, on github.com, this is your
   landmark.
2. In the upper right of the file view, click the pencil icon labelled **Edit file**.
3. Make your change in the text box. Click the **Preview** tab if you want to check how it
   will render before you commit.
4. Scroll down and fill in the **commit message** box, the next section covers what to
   actually write here.
5. Check the **email address** dropdown if it's shown. This picks which of your verified email
   addresses gets recorded as the author of this change, worth a glance if you have more than
   one on your account.
6. Choose **Commit directly to the [branch name] branch**, or **Create a new branch for this
   commit and start a pull request**. For your own solo repository, direct is normal. If
   you're not sure which to pick because other people are also working in this repository, use
   the second option and read `07-pull-requests.md` before you go further.
7. Click **Commit changes**, the button reads **Propose changes** instead if you chose the
   branch-and-pull-request option.

**Screenshot placeholder:** the commit dialog at the bottom of the browser file editor,
showing the message field, the email dropdown, and the two branch radio buttons, so a reader
recognises it before they get there.

You'll know it worked because you're taken back to the file's normal view, now showing your
updated text, and the file's commit history shows one more entry than it did before.

**If you don't have Write access to the repository at all**, clicking Edit still works, but
GitHub changes what happens next: it automatically makes you a personal copy of the repository
(a fork) and proposes your change there as a pull request, rather than committing straight
into the original. That's expected, not an error, and it's covered properly in
`09-forks-and-contributing.md`.

**When the browser is the wrong tool:** more than one file at once, anything you want to test
before it goes live, or code you're not confident reading a diff of in a small text box. For
any of those, ask Claude Code to make the change locally instead, where it can show you
exactly what changed before anything gets committed.

### Commits, and what the commit message is actually for

A commit is a saved snapshot of a change, defined in full above under "The words you need."
The commit message is the part worth taking seriously, because GitHub requires something here
but doesn't tell you how to write it well.

**Our recommendation, not a GitHub rule:** write the message for the version of you, or your
teammate, who looks at this six months from now with zero memory of today. "Fixed it" or
"update" tells that person nothing. A message that says what changed and, briefly, why, saves
them from having to open the file and guess.

**A pattern worth pasting in and adapting, every time:**

```
What changed: [one short phrase]
Why: [one short phrase, only if it's not obvious]
```

For example, `What changed: corrected Saturday opening hours` beats `update` every time
someone other than you, including future you, has to read it.

### Keeping your copy up to date

How you update depends entirely on how you got your copy in the first place.

**If you downloaded a ZIP:** there's no ongoing connection to the repository, so there's no
"update" step, only "download it again." Go back to the Code button and click Download ZIP a
second time. The trap: if you extract it into the same folder as before without renaming
anything, you can end up with two folders that look identical and no way to tell which one is
current just by looking. If you expect to check for updates more than once, switch to the
clone path instead, it's built for exactly this.

**If Claude Code cloned it:** ask Claude Code, in plain English, to "pull the latest changes."
This runs `git pull`, defined above under "The words you need." One thing worth knowing before
you pull: GitHub's own guidance is that "you should ensure that your local work is committed
before running the pull command." If you've made edits you haven't committed yet, commit them
first, or ask Claude Code to do it for you, otherwise the update can get confused about which
version of a file to keep.

**If the update runs into a merge conflict**, because you and someone else changed the same
part of the same file, that's covered fully in `08-merge-conflicts.md`. It's a normal,
recoverable situation, not a sign anything broke.

### Browser or Claude Code: which one to use

Both are legitimate. Use whichever fits the job, and say to yourself which one you're choosing
and why, the same habit this whole kit tries to build.

| Situation | Use |
|---|---|
| A quick edit to one file you can already see and understand on screen | Browser |
| You want to see exactly what a click does before you commit to it, while you're still learning | Browser |
| Getting a full, connected copy of a repository, especially one you'll come back to | Claude Code |
| More than one file needs to change together | Claude Code |
| You want to review a change before it's committed anywhere | Claude Code |
| Pulling down the latest updates to a copy you already have | Claude Code |
| You're not sure git is even installed, or don't want to find out | Either, the browser needs nothing installed, Claude Code handles the rest for you |

### Practising this safely

If you want to try any of this, getting a copy, making a small edit, committing it, without
any risk to real work, this kit's practice repository is built for exactly that. It's public,
and its own README says it plainly: "Fork it, break it, nothing here matters." Get a copy of
it using either method above and try the loop end to end before you do it somewhere that
counts.

## Strategy: how to actually use this

**Default to a clone the moment you're not sure you'll only look once.** A ZIP costs nothing
extra today, but the second visit is where it starts costing you, redownloading, re-extracting,
and guessing which folder is current. Cloning through Claude Code costs about the same effort
as the ZIP path and never puts you in that position. Reserve the ZIP for the genuine one-off,
a file someone sent you a link to that you'll read once and never touch again.

**A solo operator should stay on the direct loop, no branch, no pull request, until there's a
second person to hand work to.** Adding a review step to a one-person repository is friction
with nobody on the other end to benefit from it. That changes the day a second person starts
touching the same repository regularly, not before.

**A team of two to four should default to a branch and a pull request the moment more than one
person touches the same repository in the same week**, even if you're the one approving your
own pull request most of the time. The value isn't the review itself, it's the habit of
describing a change before it lands, which is the same habit a good commit message is for at
smaller scale. `06-branches.md` and `07-pull-requests.md` cover setting that up.

**The browser-versus-Claude-Code decision comes down to one question: can you read the whole
change on screen, in one text box, and trust yourself to spot a mistake in it?** If yes, the
browser is faster and there's no reason to reach for anything else. The moment a change
touches more than one file, or you'd feel better seeing a diff before anything is saved,
switch to Claude Code. It shows you the change before it commits, the browser edit box does
not.

**Enforce the commit message pattern from day one, not once it becomes a problem.** The cost
of a bad message is invisible today, you know what you just did, and expensive in six months,
when you don't. Two lines pasted in and adapted each time costs seconds. Retrofitting six
months of "update" and "fix" after the fact costs a lot more than that.

**What good looks like months later:** a commit history that reads like a diary. "Corrected
Saturday opening hours." "Removed the old menu PDF link." "Updated holiday closure dates on
three pages." That's the same return issues give you for tracked work, a searchable record
that answers "what happened and when" without anyone having to remember it or explain it
again.

**What would change my mind:** if your business genuinely will always be one person touching
one repository, don't add branches and pull requests just because a bigger team would.
There's no reviewer, so there's no benefit, only an extra click every time. Add the review
step back the day a second person starts committing to the same repository, and not a day
before.

## A worked example

A hairdresser runs her own booking page as a small repository, and no one else touches it.
She works from both her laptop and, some days, a shared desktop at the front counter.

On the laptop, she asked Claude Code to clone the repository weeks ago, into a folder called
`GitHub` inside her Documents, the habit this page recommends. Today she wants to update her
holiday closure dates on three pages at once: the homepage, the booking page, and the contact
page.

She tells Claude Code: "Update the closure dates on the homepage, booking page, and contact
page to 24 December through 2 January." Claude Code makes the change across all three files
and shows her exactly what it changed before anything is committed. She reads it, it matches
what she asked for, and she tells it to commit, with a message along the lines of "What
changed: updated holiday closure dates on three pages." Because this is her own repository and
nobody else needs to review it first, it lands directly, no branch, no pull request.

The next morning, from the front-counter desktop, a separate copy she cloned months earlier,
she notices a single misspelled suburb name on the homepage. This is a one-file, one-line fix
she can see clearly on screen, so she opens the file on github.com, clicks the pencil icon
labelled **Edit file**, fixes the spelling, writes a commit message, and clicks **Commit
directly to the main branch**.

That evening, back on the laptop, before she makes any further changes, she asks Claude Code
to pull the latest changes, so her laptop's copy picks up the spelling fix she made from the
front counter that morning. Both machines now show the same, current version, and nothing was
overwritten on either side.

## If it goes wrong

**I downloaded the ZIP twice and now I've got two folders and no idea which is newer.** Check
each folder's "date modified" in your file browser, the more recent one is the one you just
downloaded. Going forward, switch to the Claude Code clone path for anything you'll revisit,
it avoids this entirely because there's only ever one folder that updates in place.

**I asked Claude Code to clone something and now I can't find the folder.** Ask it directly:
"Where did you clone [repository name] to?" It knows the exact path it used and will tell you
again, or you can ask it to open the folder for you.

**I clicked Edit and there was no Commit changes button, or it said Propose changes instead
and I didn't expect that.** You likely have Read access but not Write access to this
repository. That's not broken, GitHub is offering to fork the repository and open a pull
request with your change instead of committing it directly, since it isn't yours to commit
to. Read `09-forks-and-contributing.md` for what happens next, or `03-members-and-access.md`
if you think you should have Write access and don't.

**I made a mistake in a commit I already made.** This page doesn't cover undoing or rewriting
a commit, that's the kind of change worth getting help with rather than doing on your own the
first time you hit it. The safe, everyday fix on the direct loop this page covers is to make a
new commit that corrects the mistake, GitHub's history is additive by design, and fixing
forward keeps every step visible instead of hidden. If you're on a repository that uses
branches and pull requests, `06-branches.md` and `07-pull-requests.md` cover the version of
this loop with more room to catch something before it lands.

**Claude Code told me it can't pull because I have uncommitted changes.** This is exactly the
situation GitHub's own guidance warns about. Commit what you've changed first, or ask Claude
Code to commit it for you, then pull again.

## FAQ

**Do I need to actually know git to do any of this?** No. Everything on this page is either a
browser click path or a plain-English request to Claude Code. Claude Code runs the underlying
git commands for you; knowing what they're called isn't required to use them.

**What's actually different between the ZIP download and the Claude Code clone?** The ZIP is
a one-time snapshot with no history and no way to update it in place, you have to redownload
it. A clone keeps the full history and stays connected to GitHub, so you can pull new changes
into the same folder whenever you want.

**Can I edit a code file through the browser the same way I'd edit a text file?** Yes, the
click path is identical. This page focuses on the everyday habit; anything bigger than a
small, single-file change is usually better handled through a branch and a pull request,
covered in `06-branches.md` and `07-pull-requests.md`.

**Why does my commit show my email address, and can I change which one?** GitHub records the
verified email tied to the commit as its author. If your account has more than one verified
email, the commit dialog in the browser shows a dropdown to pick which one, check it on your
own screen before you commit if it matters to you.

**I just want to look at some files, I'm never going to change anything. Which option should I
use?** Either works, since Read access can't push changes back either way. The ZIP is the
simplest choice if this is genuinely a one-off look.

**What if I want to undo a change entirely, not just fix it forward?** That's not covered on
this page on purpose. Undoing or rewriting history is something worth doing with help the
first few times, not something to try alone from a summary like this one. Fixing forward with
a new commit, covered under "If it goes wrong" above, is the safe everyday option.

## Quick reference

- **One-time copy, no history:** repository's main page, green **Code** button, **Download
  ZIP**
- **Connected copy you can update:** ask Claude Code, "Clone this repository for me:" plus the
  HTTPS link from the **Code** button
- **Edit one file in the browser:** open the file, pencil icon **Edit file**, make the change,
  fill in the commit message, **Commit changes**
- **Edit more than one file, or want to review first:** ask Claude Code
- **Update a copy you already have:** ask Claude Code, "pull the latest changes"
- **Commit message pattern:** `What changed: ___. Why: ___ (if not obvious)`
- **Solo repository:** commit directly, no branch needed
- **More than one person touching the same repository:** use a branch and a pull request,
  `06-branches.md` and `07-pull-requests.md`
- **Made a mistake in a commit:** fix forward with a new commit, don't try to rewrite history
  on your own

## Sources

- https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- https://cli.github.com/manual/gh_repo_clone
- https://docs.github.com/en/get-started/using-git/about-git
- https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository
- https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files
- https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
- https://github.com/selrai-company/github-training-content
