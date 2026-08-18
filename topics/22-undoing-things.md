# Undoing things, and getting back to how it was

## What this gets you

The fear that stops most beginners from touching GitHub at all is that one wrong click will
destroy something. It won't. Almost every action covered in this kit has a way back, either a
documented button that reverses it, or a safe habit that means you never needed the button in the
first place. Once you know which situations are genuinely undoable, which ones need you to ask
someone, and which small handful are real and permanent, you can move faster everywhere else in
this kit, because you're no longer working scared. That's the actual business value here: less
hesitation, fewer people afraid to touch the file editor, and a clear answer the one time a year
something really does need fixing properly instead of panicking about it.

## Before you start

- You should already know what a commit is (a saved snapshot of a change, with a short message
  describing it) and what a branch is, both covered in `06-branches.md`. Everything on this page
  builds on those two ideas.
- You should already know what a pull request is (the request to bring one branch's changes into
  another, reviewed before it happens), covered in `07-pull-requests.md`. Several of the safest
  undo options on this page only exist because a change went through one.
- Some of the fixes below need Write access to the repository (the ability to push changes and
  click things like **Revert**). If you only have Read access, you can still see everything on
  this page, you just need to ask someone with more access to click the actual button.
- If you plan to use Claude Code for any of the local, on-your-machine steps below, it should
  already be set up against your repository, covered in `11-github-with-claude-code.md`.

## The words you need

**Uncommitted change.** An edit that exists only in an open file, in your browser or on your own
machine, and hasn't been saved into your project's history yet with a commit. Nothing is
permanent about it. It behaves the way an unsaved Word document does.

**Commit history.** The full, ordered list of every commit ever made to a repository. GitHub never
deletes an entry from this list on its own, even a commit you'd rather forget about stays in the
list forever, unless someone deliberately rewrites history (see below).

**Revert.** Adding a brand new commit that does the exact opposite of an earlier one, so the file
ends up back the way it was. The mistaken commit is still there in the history, sitting right next
to the one that cancels it out. Nothing about the past is erased.

**Rewriting history.** Editing or removing an entry from the commit history itself, rather than
adding a new commit that cancels it out. This kit does not teach how to do this. Where it would be
the answer, this page says so plainly and tells you to bring it to someone else, a mistake made
while rewriting history can do more damage than the thing you were trying to fix.

**Force-push.** Pushing a rewritten history up to GitHub, overwriting what was there before instead
of adding to it. This kit doesn't teach it as a routine action, covered further in
`11-github-with-claude-code.md`.

**Blame view.** A GitHub screen, opened from inside a file, that shows you who last changed each
line of that file and when, so you can trace how it got to its current state.

**Danger Zone.** The section at the bottom of a repository's **Settings** page where the genuinely
serious, hard-to-reverse actions live, changing visibility, transferring ownership, and deleting
the repository outright. It's laid out separately from everything else on purpose.

## How to do it

### Undoing a change you haven't saved yet

**In the browser.** If you're editing a file directly on github.com and haven't clicked **Commit
changes** yet, nothing has actually happened to your project. GitHub's own documented steps for
editing a file end with a deliberate action, filling in a commit message and clicking **Commit
changes** or **Propose changes**, and nothing before that point is described anywhere as saved.
Navigate away from the page, or close the tab, and the edit is gone as if you'd never made
it. **This kit could not find a specific "Cancel" button named in GitHub's own documentation for
this exact screen, confirm what your own edit screen offers before relying on a particular
button, navigating away works regardless.**

**On your own machine, through Claude Code.** If you're working from a clone and you've edited a
file but haven't committed it, ask Claude Code plainly:

```
Undo the changes I just made to homepage.html. I haven't committed them.
```

Claude Code runs the underlying git command for you (commonly `git restore` or the older `git
checkout --`) and tells you when it's done. GitHub's own engineering blog is direct about what
this means: the command "alters files in the working directory to a state previously known to
Git," back to the last commit. It also gives the honest warning that goes with it: changes undone
this way "are really gone. They were never committed, so Git can't help us recover them later."
Only ask for this when you're genuinely sure, there's no undo for the undo here, because there was
never a saved copy to go back to.

### Going back to how a file looked before, using its history

Every file on GitHub keeps a full record of every change ever made to it, and you can look at any
earlier version without changing anything about the current one.

1. Open the file on github.com.
2. Above the file's content, in the row of controls near the top right, click **Blame**. GitHub's
   own description of what you'll see: "a line-by-line revision history for an entire file," with
   each line attributed to the commit, author, and date that last touched it.
3. To see the file as it looked before a particular change, find the relevant line and click the
   control next to it for viewing an earlier revision, or click the commit message itself for more
   detail about that specific change.
4. When you're done, click back to the normal **Code** view above the file to leave Blame view.

This is entirely safe to click around in. Looking at history changes nothing, you're only ever
reading, and there's no button on this screen that alters the current file.

**If you want the whole file exactly as it looked at a specific past commit, not just one line's
history:** open that commit from the repository's commit list (covered in
`15-finding-things.md`) and view the file from inside it. What you're looking at there is a
read-only snapshot, if you want the project actually working from that older version again, that's
the revert steps below, not this one.

### Reverting a change that's already merged, and why revert instead of delete

If a change already went through a pull request and got merged into your default branch, the safe
way to undo it is a revert, not deleting the file or the branch by hand.

**Why revert is the safer direction.** Deleting something by hand, a file, a whole folder, risks
taking other changes with it if anything else has touched that area since, and it leaves no clear
record of what happened or why. A revert does one specific thing and nothing else: GitHub's own
documentation states plainly that "reverting a merged pull request creates a new pull request that
reverts the original merge commit." Nothing about the past is erased, the mistaken change and the
commit that cancels it out both sit in your history, side by side, forever. And because a revert is
itself just a normal commit, if it turns out you were wrong to revert, you can revert the revert.
There's no dead end.

**The steps, if the change went through a pull request:**

1. Open the repository's front page, and click the **Pull requests** tab.
2. Open the specific pull request you want to undo, the one that introduced the change.
3. Near the bottom of the page, click **Revert**. You'll know you're in the right place because
   this creates a brand new pull request for you automatically, already containing the reverse of
   the original change.
4. Review it like any other pull request (covered in `07-pull-requests.md`), then merge it the
   normal way to finish undoing the original change.

This needs Write access to the repository. GitHub's own wording is specific about what happens if
you don't have it: without write permissions, the **Revert** button won't be there for you
to click, and you'd ask a repository administrator to do it instead.

**If the mistaken change was a direct commit, with no pull request involved at all**, ask Claude
Code plainly:

```
Revert the commit that changed the pricing page, the one from Tuesday about the winter discount.
```

It will find that commit and push the inverse of it for you, the same result, without a pull
request in the middle.

**One thing worth knowing before you revert:** if other changes have landed on top of the one
you're undoing, and they touch the same lines, reverting can produce a conflict for you to resolve,
the same as any other conflict covered in `08-merge-conflicts.md`. That's git asking a genuine
question, not a sign the revert has failed or that anything is broken.

### Restoring a deleted branch

This only works if the branch went through a pull request that was later closed or merged, and you
still have that pull request to go back to.

1. Open the repository, click **Pull requests**, and filter to **Closed**.
2. Open the specific pull request that branch belonged to.
3. Near the bottom of the page, click **Restore branch**.

GitHub's own documentation confirms exactly what this covers: restoring works for "the head branch
of a closed pull request." It doesn't say how long that button stays available after the branch is
deleted, so don't sit on it if you change your mind, act as soon as you realise you want the branch
back.

**If the branch never went through a pull request at all**, there's no documented way to bring it
back through GitHub's interface. This is one of the real edges covered fully below, and it's the
single best reason to lean toward leaving an unused branch alone rather than deleting it the moment
you're not using it.

### Recovering a deleted repository, and being exact about the limits

Be exact here, because the limits are real and they matter more than any other undo action on this
page.

**The window.** GitHub's own wording: "a deleted repository can be restored within 90 days" of
deletion. It also notes a short delay before that option becomes available at all: "it can take up
to an hour after a repository is deleted before that repository is available for restoration."

**The steps, for a repository you owned personally:**

1. Click your profile picture, top right, then **Settings**.
2. In the "Code, planning, and automation" section of the sidebar, click **Repositories**, then
   **Deleted repositories**.
3. Next to the repository you want back, click **Restore**.
4. Read the warning shown on screen, then click **I understand, restore this repository**.

**For a repository owned by an organisation**, the equivalent screen sits under that
organisation's own **Settings then Deleted repositories** instead, and an organisation owner needs to
be the one to click it.

**Three limits worth knowing before you assume this always works:**

- **A repository that was part of a fork network may not be restorable at all.** GitHub's own
  wording: "if your repository was part of a fork network, it cannot be restored unless every
  other repository in the network is deleted or has been detached from the network." A fork
  network is the parent repository plus every fork of it, and every fork of those forks.
- **Restoring a repository does not restore team permissions.** GitHub states this plainly: "
  restoring a repository will not restore team permissions." You get the code and history back;
  you'll need to re-grant access to people afterward.
- **GitHub Support can only help with this on a paid GitHub plan.** If the 90-day self-service
  option above has already closed and you need GitHub itself to step in, that route needs a paid
  plan behind the account.

**Stop and act immediately if you realise you've deleted the wrong repository.** Don't spend time
deciding whether it's "bad enough" to bother with, go straight to the steps above. Minutes rarely
matter against a 90-day window, but the fork-network and permissions limits above are worth reading
properly before you assume it will come back exactly as it was.

### Closing something you opened by mistake

Closing an issue or a pull request doesn't delete anything. Everything you or anyone else wrote on
it stays exactly where it was, just marked closed instead of open, and it's still fully findable
through search (covered in `15-finding-things.md`).

**Closing an issue:**

1. Open the repository, click **Issues**, then open the specific issue.
2. Optionally, next to **Close issue**, choose a reason for closing it from the dropdown.
3. Click **Close issue**.

GitHub's own wording on who can do this: "anyone can close an issue they opened," and repository
owners, collaborators, or anyone with triage permissions or higher can close issues opened by
someone else.

**Closing a pull request without merging it:**

1. Open the repository, click **Pull requests**, then open the specific pull request.
2. At the bottom of the page, below the comment box, click **Close pull request**.
3. You'll be offered the option to delete the branch at the same time. GitHub's own framing: doing
   so "keeps the list of branches in your repository tidy." It's optional, and closing the pull
   request itself doesn't delete the branch automatically.

**Whether a closed issue or pull request can be reopened.** This kit could not find a documented
"Reopen" control described directly in GitHub's own published pages for either one. In practice,
look near the bottom of a closed issue or pull request for a **Reopen** option before assuming
there isn't one, and confirm what you actually see on your own screen rather than relying on this
page for that specific button.

## Strategy: how to actually use this

**The default should always be revert, not delete, for anything that's already shared with
anyone else.** Once a change has gone through a pull request and landed on your default branch,
treat it as part of the record. If it needs undoing, revert it. Deleting things by hand, editing a
merged file back to how it used to be, or removing a branch that others might reference, all throw
away the "why," and make it harder for the next person (including future you) to work out what
actually happened.

**Get into the habit of routing real changes through a pull request, even solo.** Every safe undo
option on this page, restoring a branch, reverting cleanly, comes from something having gone
through a pull request first. A direct commit straight to your default branch, with no pull
request involved, still has a revert available, but loses the branch-restore option entirely if
you ever delete that direct commit's branch. This costs you nothing extra as a solo operator
(covered in full in `05-daily-workflow.md`) and it's the single habit that keeps every door on this
page open.

**A solo operator can move fast and self-correct.** If it's just you, and you're confident about
what a change did, reverting it yourself the moment you notice a problem is the right call, don't
wait for permission you don't need to ask yourself for.

**A team of four or more needs one rule everyone actually follows: nobody deletes a repository, a
production branch, or a large amount of history alone.** Not because any one person isn't trusted,
but because the fastest way to turn a five-minute recoverable mistake into a genuine loss is one
person acting alone on incomplete information, at speed, under stress. Say the plan out loud to
someone else first, even a one-line message, before clicking **Delete this repository** or force-
pushing anything.

**What good looks like months later:** nobody on the team is afraid to open the file editor,
because everyone has actually watched a revert work once and knows what it looks like. Deleted
repositories in this kit's audience are rare precisely because nobody deletes one on a whim, the
90-day window and the Danger Zone's own warnings are both taken seriously the first time, not
learned about the hard way. And the one or two genuinely permanent mistakes that do happen, a
branch deleted with no pull request behind it, a secret that got committed once, get handled by
rotating a key or letting go of one branch's history, not by panic.

## A worked example

A small landscaping business, three people, has a repository holding their price list, their
seasonal service descriptions, and the copy for their website.

**Monday.** The owner is editing the spring price list directly in the browser, updating a mowing
rate. Halfway through typing, she realises she's editing the wrong season's section entirely. She
hasn't clicked **Commit changes** yet, so she just closes the tab. Nothing happened. She reopens
the file and starts again in the right place.

**Wednesday.** Her assistant opens a pull request that updates the "About us" page, and it gets
merged into the default branch that afternoon. Thursday morning, a client points out the new
wording accidentally dropped the business's ABN. The owner opens that merged pull request, scrolls
to the bottom, and clicks **Revert**. A new pull request appears automatically, containing exactly
the change needed to bring the ABN back. She merges it. The mistaken version and the fix both sit
in the repository's history now, nothing was hidden or deleted, and anyone looking back later can
see exactly what happened and when.

**The following Monday**, the assistant had been trying an idea on a branch called
`try-new-service-list`, decided it wasn't working, and deleted the branch. It had never gone
through a pull request. Two weeks later, it turns out one paragraph from that abandoned idea was
actually worth keeping. There's no documented way to bring that specific branch back. The owner
treats this as the lesson it is, not a crisis: from now on, even a branch someone expects to
throw away gets a pull request opened against it before it's deleted, closed without merging if it
genuinely isn't wanted, so the **Restore branch** option is always sitting there if anyone changes
their mind.

## If it goes wrong

**I deleted a repository and I'm not sure I meant to.** Go straight to the recovery steps above,
don't spend time first deciding whether you're sure. You have up to 90 days, but the fork-network
and team-permission limits are worth reading properly rather than assumed away.

**I reverted a pull request and now I've got a merge conflict.** That's git asking a genuine
question because something else has changed the same lines since, not a sign the revert has
failed. `08-merge-conflicts.md` covers resolving it, start to finish.

**I asked Claude Code to undo an uncommitted change and now I want it back.** There's nothing to
get back. An uncommitted change was never saved anywhere git could recover it from, that's the
honest edge, not a step you missed.

**I deleted a branch that never had a pull request, and I need it back.** There's no documented
GitHub feature that recovers this. Ask around, sometimes a teammate still has an old local copy on
their own machine with that branch on it, that's genuinely your best remaining chance, not
something GitHub's interface can do for you.

**I think history needs to be rewritten to fix this properly.** Stop there. This kit deliberately
doesn't teach that, a mistake made while rewriting history can do more damage than the original
problem. Bring it to the community rather than attempting it alone from a description on this page.

## FAQ

**Have I actually lost my work?** Almost never. If you had not committed the change yet, it
lives on in your last commit, and any of the steps above under "Undoing a change you haven't
saved yet" gets you back to it. If you had committed it, even merged it, it is still sitting in
the commit history, GitHub never removes an entry from that list on its own. The only genuine
loss is an uncommitted edit you deliberately asked Claude Code to discard, or work on a branch
that never went through a pull request and was then deleted. Both of those are real, and both
are covered in "What can genuinely never be undone" below.

**Can anyone tell I made a mistake?** Yes, and that's the point, not something to feel bad
about. Every commit stays in the history with your name on it, whether you fix the mistake with
a revert or leave it exactly as it happened. A revert is itself just a new, ordinary commit,
visible to anyone with access to the repository, sitting right next to the change it cancels
out. Treat that visibility as the safety net it actually is: it's what lets you, or anyone else
on your team, work out what happened and undo it cleanly, months later if needed.

**Is it really, permanently gone?** Depends what "it" is. A deleted repository is recoverable
for up to 90 days, with some limits worth reading properly (covered above). A merged change is
recoverable with a revert at any time, the mistaken commit is never removed from the history.
A deleted branch is only recoverable if it went through a pull request first. An uncommitted
change you asked Claude Code to discard, and a repository past its 90-day window, are not coming
back. Check which situation you're actually in before assuming either way.

**What can genuinely never be undone?** A short, honest list: a repository once its 90-day
restore window has passed, or one that was part of a fork network that can't be detached; a
branch deleted with no pull request ever opened against it; history that's been deliberately
rewritten; a force-push that overwrote commits nobody else had a copy of; an uncommitted change
you asked to have discarded; and a secret, a password or an API key, that was ever committed and
pushed, even once. Rotating that secret afterward stops it being useful to whoever finds it, but
it doesn't erase the fact that it was exposed. Everything else on this page has a documented way
back.

**Is there a general "Undo" button on GitHub, like Ctrl+Z?** No, and it wouldn't make sense the
way GitHub is built. Every change is its own separate, named commit, so "undo" always means
something specific: discard an unsaved edit, revert one particular commit, or restore one
particular branch. That specificity is actually the safety feature, you always know exactly what
you're undoing before you click anything.

**If I revert a pull request, does it touch anything anyone else did afterward?** No. A revert
only cancels out the one change it targets. Anything merged before or after it, on unrelated lines,
is untouched. If someone else's later change happened to depend on the one you're reverting, that's
exactly when you'd see a merge conflict, covered above, not a silent side effect.

**Can Claude Code do the deleted-repository restore for me?** No. That screen sits under your
account settings and is tied to you as a real, signed-in person, the same rule this whole kit
follows for anything tied to your identity, covered in `11-github-with-claude-code.md`. Claude Code
can do the git side of things, reverting a commit, checking where something landed, but this
particular action stays in your browser, signed in as yourself.

**Is closing an issue the same as deleting it?** No. Closing marks it as done or not going ahead;
nothing about it disappears, and it's still fully searchable. Deleting an issue is a separate,
much rarer action this kit doesn't cover, because closing is the right tool for almost every real
situation you'll hit.

**What's actually the difference between reverting and just editing the file back by hand?**
Reverting adds a clearly labelled commit that says, permanently, "this specific change was
undone, and here's exactly what changed." Editing it back by hand leaves no such record, and risks
missing part of the original change if it touched more than you remember. For anything that's
already shared with someone else, revert.

**Do I need to understand git commands like `restore`, `checkout`, or `reset` to use any of
this?** No. Every local, on-your-machine action on this page is written as something to ask Claude
Code in plain English. Knowing the command names helps you understand what's happening under the
surface, covered here because it makes the "why" clearer, but it was never required for you to
type one yourself.

## Quick reference

```
Haven't saved it yet (browser)         Navigate away without clicking Commit changes
Haven't saved it yet (your machine)    Ask Claude Code to undo the uncommitted change
See how a file looked before           Open the file, click Blame
Undo a change already merged           Open the pull request, click Revert (needs Write access)
Undo a direct commit, no pull request  Ask Claude Code to revert that specific commit
Get back a deleted branch              Only if it had a pull request: open it (Closed tab),
                                        click Restore branch
Get back a deleted repository          Settings > Repositories > Deleted repositories > Restore
                                        (within 90 days, some limits apply)
Closed something by mistake            Look for Reopen near the bottom, confirm on your screen
Genuinely cannot be undone             A repository past its restore window or ineligible;
                                        a branch deleted with no pull request behind it;
                                        rewritten history; a force-push over lost work;
                                        an uncommitted change you asked to discard;
                                        a secret already seen, even after it's rotated
```

---

## Sources

- https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository
- https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository
- https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/closing-a-pull-request
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request
- https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file
- https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files
- https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/
