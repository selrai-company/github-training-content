# The everyday workflow, and getting work in and out

This page covers the loop you'll actually run week to week: getting a copy of a repository onto
your machine, making a change, committing it with a message that explains what you did, and
keeping your copy current as other people change things too. It also covers something that trips
up almost every beginner and nobody warns them about: where the files actually land on your
computer, and how not to lose track of that folder.

By the end, you'll be able to get any repository onto your machine two different ways, make a
small change through the browser and commit it properly, explain in one sentence what a commit
message is for, and pull the latest version down without overwriting your own work.

This page assumes you already have somewhere to work from: your own repository, or one you've
been given access to. If you haven't created a repository yet, read `04-repositories-and-visibility.md`
first. This page also assumes Claude Code, on the Max plan, is available to you as a second option
alongside the browser. If you haven't opened Claude Code before, its own setup isn't covered here,
this page only covers what to ask it once it's running.

## The basic loop, in plain English

Every team using GitHub, no matter how small, runs some version of the same loop: **someone changes
something, it gets looked at, and then it lands.**

There are two honest versions of that loop, and which one you're running depends on who else is
involved.

**Solo, or a change nobody needs to check first.** You edit a file, you commit it, it's live. No
review step. This is normal and fine for your own repository, or for small changes to a repository
you fully control. The rest of this page covers exactly this loop, start to finish.

**A team, or a change that should get a second pair of eyes first.** The change happens on its own
private copy of the work (a **branch**), gets proposed for review (a **pull request**), someone
looks at it, and only then does it land in the version everyone else sees. That's the loop most
small businesses grow into once more than one person is touching the same repository regularly. It's
covered in full in `06-branches.md` and `07-pull-requests.md`, and what to do when two people change
the same thing at once is `08-merge-conflicts.md`.

You don't have to pick one forever. Plenty of small teams run the simple loop for quick fixes and
the reviewed loop for anything bigger. What matters today is knowing which loop you're in before you
start, not partway through.

## Getting a copy of a repository onto your machine

There are two genuinely different ways to do this, and they're not interchangeable. Pick based on
whether you'll ever need to update this copy later.

### Option 1: Download it as a ZIP (browser, no install, no history)

1. Open the repository's main page on github.com.
2. Click the green **Code** button, above the file list.
3. Click **Download ZIP**.

GitHub's own words: this gives you "a compressed (zipped) copy of all the files in that repository
as it currently exists," and no git installation is required for this method at all. The one thing
worth knowing before you rely on it: GitHub's own documentation is direct that "snapshots don't
contain the entire repository history," so a ZIP is a one-time photo of the files as they are right
now, not a copy that remembers how they got that way or that can be updated in place.

**Screenshot placeholder:** the green Code button clicked open, showing the HTTPS, SSH, GitHub CLI
tabs and the separate Download ZIP link underneath, so a reader can see all the options in one
place before choosing.

Use this when you just need the files once, to look at or use right now, and you're not planning
to come back for updates.

### Option 2: Ask Claude Code to clone it (keeps a live connection, full history)

A **clone** is a full copy of the repository, including its entire history, that stays connected to
GitHub so you can pull down new changes later without downloading everything again. Getting one
normally means typing a `git clone` command in a terminal. You don't have to do that yourself.

1. On the repository's page, click the green **Code** button and copy the **HTTPS** link (click the
   copy icon next to it).
2. Tell Claude Code, in plain English: "Clone this repository for me: " and paste the link.
3. Claude Code runs the clone for you and tells you where it put the folder. Read that path, don't
   skip past it, the next section covers why.

For a public repository, this needs nothing signed in, just Claude Code and the link. For a private
repository, you (and by extension Claude Code, acting as you) need to already be signed in to
GitHub on that machine, which usually means the GitHub CLI (`gh`) is installed and authenticated.
That's a genuinely good one-time setup to have, but getting it working the first time isn't covered
in this file. If it's not set up yet, use the browser ZIP path above instead for now.

**Either way, you need at least Read access to the repository to get a copy of it at all.** GitHub's
own requirement, stated plainly: "you have permission to access the repository you want to clone."
If you can't see the repository, or the Code button doesn't offer you a clone link, that's a
permissions question, covered in `03-members-and-access.md`, not something wrong with these steps.

Use this when you expect to come back to this repository more than once, want to keep it current,
or think you might eventually contribute a change back to it.

## Where the files actually end up (don't lose the folder)

This is the part that quietly derails more beginners than anything else in this page. GitHub tells
you where a browser download or a Claude Code clone landed. Your job is to actually read that, and
write it down if you need to.

**If you downloaded the ZIP:** it lands wherever your browser normally saves downloads. On most
setups that's a folder literally named **Downloads**. A ZIP file isn't usable as-is, you need to
extract (unzip) it first, which creates a new folder with the repository's name inside whatever
folder the ZIP itself was saved to. Check your own browser's download settings if you're not sure
where that is, this is a setting specific to your computer, not something GitHub controls.

**If Claude Code cloned it:** the folder lands wherever you were working when you asked, or wherever
you told it to put it, and it's named after the repository. Claude Code will tell you the full path
when it finishes. If you lose track of it later, just ask: "Where did you put the copy of
[repository name] you cloned earlier?" and it will tell you again or find it for you. Don't rely on
memory for this one, ask.

**A habit worth building either way:** the first time you get a copy of something you'll want to
work in more than once, decide on one place on your machine for GitHub-related folders (a folder
called `GitHub` inside your Documents, for instance) and always point Claude Code there when you ask
it to clone something. That one habit is the entire fix for "I don't know where any of my repos
went."

## Making a change through the browser

For a quick, single-file edit, the browser is faster than asking Claude Code to do it, and it's the
right tool for this specific job.

1. Open the file you want to change, inside the repository, on github.com.
2. Click the pencil icon labelled **Edit file**, in the upper right of the file view.
3. Make your change in the text box. Click the **Preview** tab if you want to check how it will
   render before you commit.
4. Scroll down and fill in the **commit message** box (the next section covers what to actually
   write here).
5. Check the **email address** dropdown if it's shown. This picks which of your verified email
   addresses gets recorded as the author of this change, worth a glance if you have more than one on
   your account.
6. Choose **Commit directly to the [branch name] branch**, or **Create a new branch for this commit
   and start a pull request**. For your own solo repository, direct is normal. If you're not sure
   which to pick because other people are also working in this repository, use the second option and
   read `07-pull-requests.md` before you go further.
7. Click **Commit changes** (the button reads **Propose changes** if you chose the branch-and-pull-request
   option instead).

**Screenshot placeholder:** the commit dialog at the bottom of the browser file editor, showing the
message field, the email dropdown, and the two branch radio buttons, so a reader recognises it
before they get there.

**If you don't have Write access to the repository at all**, clicking Edit still works, but GitHub
changes what happens next: it automatically makes you a personal copy of the repository (a **fork**)
and proposes your change there as a pull request, rather than committing straight into the original.
That's expected, not an error, and it's covered properly in `09-forks-and-contributing.md`.

**When the browser is the wrong tool:** more than one file at once, anything you want to test before
it goes live, or code you're not confident reading a diff of on a small text box. For any of those,
ask Claude Code to make the change locally instead, where it can show you exactly what changed
before anything gets committed.

## Commits, and what the commit message is actually for

A **commit** is a saved snapshot of a change. GitHub's own description: it "records changes to one
or more files," and every commit gets its own unique ID, a timestamp, and the name of whoever made
it. Once it's committed, that snapshot is permanent history, you can always come back and see
exactly what this file looked like at that point.

The **commit message** is the one line (or few lines) that says what that snapshot actually changed
and why. GitHub requires you to write something here, its own wording: you "must include a commit
message that briefly describes the changes." It does not enforce a length, a format, or any specific
wording, that part is genuinely up to you.

**Our recommendation, not a GitHub rule:** write the message for the version of you (or your
teammate) who looks at this six months from now with zero memory of today. "Fixed it" or "update"
tells that person nothing. A message that says what changed and, briefly, why, saves them from
having to open the file and guess.

**A pattern worth pasting in and adapting, every time:**

```
What changed: [one short phrase]
Why: [one short phrase, only if it's not obvious]
```

For example: `What changed: corrected Saturday opening hours` beats `update` every time someone
other than you (including future you) has to read it.

## Keeping your copy up to date

How you update depends entirely on how you got your copy in the first place.

**If you downloaded a ZIP:** there's no ongoing connection to the repository, so there's no
"update" step, only "download it again." Go back to the Code button and click Download ZIP a second
time. The trap: if you extract it into the same folder as before without renaming anything, you
can end up with two folders that look identical and no way to tell which one is current just by
looking. If you expect to check for updates more than once, switch to the clone path below instead,
it's built for exactly this.

**If Claude Code cloned it:** ask Claude Code, in plain English, to "pull the latest changes." This
runs `git pull`, which GitHub's own documentation describes plainly: it "grabs online updates and
merges them with your local work" in one step. One thing worth knowing before you pull: GitHub's own
guidance is that "you should ensure that your local work is committed before running the pull
command." If you've made edits you haven't committed yet, commit them first (or ask Claude Code to
do it for you), otherwise the update can get confused about which version of a file to keep.

**If the update runs into a conflict** because you and someone else changed the same part of the
same file, that's covered fully in `08-merge-conflicts.md`. It's a normal, recoverable situation, not
a sign anything broke.

## Browser or Claude Code: which one to use

Both are legitimate. Use whichever fits the job, and say to yourself which one you're choosing and
why, the same habit this whole kit tries to build.

| Situation | Use |
|---|---|
| A quick edit to one file you can already see and understand on screen | Browser |
| You want to see exactly what a click does before you commit to it, while you're still learning | Browser |
| Getting a full, connected copy of a repository, especially one you'll come back to | Claude Code |
| More than one file needs to change together | Claude Code |
| You want to review a change before it's committed anywhere | Claude Code |
| Pulling down the latest updates to a copy you already have | Claude Code |
| You're not sure git is even installed, or don't want to find out | Either, browser needs nothing installed, Claude Code handles the rest for you |

## Practising this safely

If you want to try any of this, getting a copy, making a small edit, committing it, without any
risk to real work, this kit's practice repository is built for exactly that. It's public, and its
own README says it plainly: "Fork it, break it, nothing here matters." Get a copy of it using either
method above and try the loop end to end before you do it somewhere that counts.

---

## If it goes wrong

**I downloaded the ZIP twice and now I've got two folders and no idea which is newer.** Check each
folder's "date modified" in your file browser, the more recent one is the one you just downloaded.
Going forward, switch to the Claude Code clone path for anything you'll revisit, it avoids this
entirely because there's only ever one folder that updates in place.

**I asked Claude Code to clone something and now I can't find the folder.** Ask it directly: "Where
did you clone [repository name] to?" It knows the exact path it used and will tell you again, or you
can ask it to open the folder for you.

**I clicked Edit and there was no Commit changes button, or it said Propose changes instead and I
didn't expect that.** You likely have Read access but not Write access to this repository. That's
not broken, GitHub is offering to fork the repository and open a pull request with your change
instead of committing it directly, since it isn't yours to commit to. Read `09-forks-and-contributing.md`
for what happens next, or `03-members-and-access.md` if you think you should have Write access and
don't.

---

## Questions people ask here

**Do I need to actually know git to do any of this?** No. Everything on this page is either a
browser click path or a plain-English request to Claude Code. Claude Code runs the underlying git
commands for you; knowing what they're called isn't required to use them.

**What's actually different between the ZIP download and the Claude Code clone?** The ZIP is a
one-time snapshot with no history and no way to update it in place, you have to redownload it. A
clone keeps the full history and stays connected to GitHub, so you can pull new changes into the
same folder whenever you want.

**Can I edit a code file through the browser the same way I'd edit a text file?** Yes, the click
path is identical. This page focuses on the everyday habit; anything bigger than a small, single-file
change is usually better handled through a branch and a pull request, covered in `06-branches.md`
and `07-pull-requests.md`.

**Why does my commit show my email address, and can I change which one?** GitHub records the
verified email tied to the commit as its author. If your account has more than one verified email,
the commit dialog in the browser shows a dropdown to pick which one, check it on your own screen
before you commit if it matters to you.

**I just want to look at some files, I'm never going to change anything. Which option should I
use?** Either works, since Read access can't push changes back either way. The ZIP is the simplest
choice if this is genuinely a one-off look.

---

## Sources

- https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- https://cli.github.com/manual/gh_repo_clone
- https://docs.github.com/en/get-started/using-git/about-git
- https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository
- https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files
- https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
- https://github.com/selrai-company/github-training-content
