# Pull requests, and getting a change reviewed

## What this gets you

A pull request is a proposal, not a live change. It lets you, or anyone you work with, put a
finished piece of work in front of someone else before it reaches the version everyone relies on.
Nothing on a branch reaches your main copy until a pull request is deliberately merged, so a
mistake never quietly becomes everyone's problem.

For a small business, this is the difference between "I hope that update was right" and "someone
actually looked at it first." A pull request also becomes a permanent record: what changed, why,
who looked at it, and when it went live. Months later, that record answers "why does the site say
that" without anyone having to remember or explain it again.

## Before you start

**You need a repository with a branch that already has commits on it.** A pull request proposes
merging one branch into another, so there has to be a branch with a real change on it first.
`06-branches.md` covers creating one and committing to it. If you have not read that file yet,
read it before this one, this file assumes a branch with commits already exists.

**You need Write access to the branch you are proposing changes from.** GitHub's own requirement,
for a public repository: "you must have write access to the head or the source branch or, for
organization-owned repositories, you must be a member of the organization that owns the
repository." If you cannot push to a branch, you cannot open a pull request from it. If that is
you, you are either missing access (`03-members-and-access.md` covers checking and requesting it),
or you are contributing to a project you do not have Write access to, which is a fork, covered in
`09-forks-and-contributing.md`.

**You do not need GitHub Issues set up to use pull requests.** They work independently. If your
repository also uses Issues, this file covers a feature that links the two together automatically,
but nothing here depends on Issues existing.

## The words you need

**Pull request.** A proposal to merge one branch's changes into another branch, usually your
default branch, so someone (possibly you, working alone) can look it over before it goes live.
GitHub's own definition: "Pull requests are proposals to merge code changes into a project."
Think of it as attaching a cover note to your branch that says "here's a change I'd like to make,
take a look before it goes anywhere."

**Base branch.** The branch you want your changes merged into, almost always your default branch.

**Compare branch.** The branch your changes are actually sitting on, the one being proposed for
merging into the base branch.

**Conversation, Commits, Checks, Files changed, and Findings.** The five tabs a pull request's
page is organised into, so you always know where to look for a given kind of information. GitHub's
own list: the **Conversation** tab shows the description, timeline, comments, and reviews; the
**Commits** tab shows how the branch changed over time; the **Checks** tab shows automated tests,
builds, and other validations; the **Files changed** tab shows the diff reviewers use; and, where
code scanning is set up, a **Findings** tab shows automated code review results. You will use
Conversation and Files changed the most.

**Linking keyword.** A word like `Closes` or `Fixes`, typed in front of an issue number inside a
pull request's title or description, that closes that issue automatically the moment the pull
request merges. Covered in `13-issues-and-tracking-work.md` from the issue's side; covered here
from the pull request's side.

**Draft pull request.** A pull request marked as not ready to be reviewed or merged yet. GitHub's
own description: "Draft pull requests cannot be merged, and code owners are not automatically
requested to review them." It is the same proposal, just flagged as still in progress.

**Code owner.** A person, or team, named in a repository's CODEOWNERS file as responsible for
reviewing changes to specific files or folders. Most small repositories will not have one set up.
Where this word appears in this file, it only matters if your repository has that file configured.

**Diff.** The actual lines that changed, shown side by side or one after another, which is what
the Files changed tab displays. This is what a reviewer is actually reading when they review a
pull request.

**Reviewer.** Anyone leaving feedback on a pull request. GitHub's own rule: "Anyone with read
access can review and comment on proposed changes." Reviewing does not need Write access, only the
ability to see the repository at all.

**Approve, Comment, and Request changes.** The three things a reviewer can choose when submitting
a review. GitHub's own wording for each: **Comment** is to "leave general feedback without
explicitly approving," **Approve** is to "submit your feedback and approve merging the changes,"
and **Request changes** is to "submit feedback that must be addressed before the pull request can
be merged."

**Merge commit, squash and merge, and rebase and merge.** The three different ways GitHub can
combine a pull request's changes into the base branch once you are ready. Each is covered in full,
with this kit's own recommendation, further down this file.

**Maintainer.** Someone with push access to a repository you are proposing a change to. This word
mostly matters for the "allow edits from maintainers" checkbox, covered below, which only appears
on pull requests opened from a fork.

**Fork.** Your own separate copy of somebody else's repository, sitting under your own account.
Covered in full in `09-forks-and-contributing.md`. It is mentioned once in this file, since one
checkbox only appears on a pull request opened from a fork.

## How to do it

Most of what follows happens in your browser, because reviewing a change is exactly the kind of
task where seeing it matters. Wherever Claude Code is genuinely faster, this file says so.

### Opening a pull request

**In the browser, once you have committed on a branch:**

1. On the repository's main page, near the top left of the file list, click the **Branch**
   dropdown and choose your branch. You will know it worked because the file list refreshes to
   show that branch's contents instead of the default branch's.
2. GitHub often shows a yellow banner above the file list at this point, with a button labelled
   **Compare & pull request**. Click it.
3. On the page that opens, use the **base** dropdown to choose the branch you want your changes
   merged into (usually your default branch), and check the **compare** dropdown shows the branch
   your changes are actually on.
4. Type a title and description for your pull request. The next section covers what to actually
   write here.
5. Click **Create Pull Request**.

You will know it worked because the pull request opens on its own numbered page, with your title
at the top and the Conversation tab showing your description underneath it.

**If you do not see the yellow banner** (you navigated away, or it has been a while since you
committed), open the **Pull requests** tab near the top of the repository instead, and look for a
button to start a new one there. Pick your base and compare branches from that screen. The exact
label on that button is worth confirming on your own screen, this kit could not pin down the
precise wording from GitHub's own documentation.

**If you made your change through the browser's file editor** and picked "Create a new branch for
this commit and start a pull request" (covered in `05-daily-workflow.md`), you have already skipped
this whole step. Clicking **Propose changes** there opens the pull request for you. Go straight to
writing the title and description below.

**Screenshot placeholder:** the yellow "Compare & pull request" banner above a repository's file
list, so a reader recognises it the first time they see it.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in** (the
same one-time setup covered in `04-repositories-and-visibility.md` and `05-daily-workflow.md`):
ask it in plain English, or let it run something like this on your behalf.

```
gh pr create --title "Update the menu prices" --body "Raises the mains section by two dollars, matches the new supplier cost." --base main
```

That's the GitHub CLI's own flags: `--title`, `--body`, and `--base` for the branch you're merging
into. Add `--draft` to open it as a draft (covered below) instead of ready for review. This is a
genuinely good shortcut once `gh` is set up, particularly if you are already asking Claude Code to
make the change for you and do not want to switch to the browser mid-task. If `gh` is not installed
and signed in yet, use the browser path above instead.

### Writing a title and description someone can actually review

GitHub does not enforce any particular format here, the title and description fields are free
text. **A practical convention worth adopting, not a GitHub rule:** write the title as what the
change does, in plain words, the way you'd say it out loud, "Update the menu prices" rather than
"changes" or your own name. In the description, say what changed and why, in a sentence or two. A
reviewer who was not in the room with you should be able to read the description and know what
they are about to look at before they open a single file.

**One real feature worth knowing, if this repository also uses GitHub Issues:** typing a linking
keyword followed by an issue number in the description links the two, and closes the issue
automatically the moment the pull request merges. GitHub's own list of keywords includes `close`,
`closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves`, and `resolved`. Typing
`Fixes #10` in your description does exactly what it says: when this pull request merges, issue 10
closes with it, and GitHub links the two pages to each other on both sides.

**If you need to change the title or description after opening it:** there is an edit control near
the top of the pull request, next to the title. Confirm the exact click on your own screen the
first time you need it, this kit has not pinned it down word for word, but the option to edit
after the fact is real, you are not locked into what you typed when you clicked Create.

### Draft pull requests

A draft pull request is the same proposal, marked as not ready yet. Use one when you want to start
the conversation, or back your work up on GitHub, before the change is actually finished.

**This is genuinely free, on every plan, in every repository, as of a specific date, and older
guides get this wrong.** Draft pull requests used to be limited to public repositories on GitHub's
Free plan. That changed on 1 May 2025. GitHub's own changelog entry for that date: "You can now
create draft pull requests in any repository, public or private, completely free of charge." If
you have read an older tutorial that says draft pull requests need a paid plan, or only work on
public repositories, that is out of date. It does not matter what plan you are on or whether your
repository is public or private, drafts work the same everywhere now.

**Opening one:** from the same "Create Pull Request" screen above, click the dropdown arrow next
to the **Create Pull Request** button and choose **Create Draft Pull Request**, then click **Draft
Pull Request**. You will know it worked because the pull request's page shows a grey **Draft**
label next to its title instead of the usual green **Open**.

**One message you might see, and it is real:** GitHub's own documentation includes this line: "If
you are the member of an organization, you may need to request access to draft pull requests from
an organization owner." If that message shows up, it is a genuine organization-level setting, not
an error on your end, ask whoever owns your organization to sort it out.

**Marking a draft ready for review:** open the pull request and, in the merge box near the bottom
of the Conversation tab, click **Ready for review**. GitHub's own note on what that does: "Marking
a pull request as ready for review will request reviews from any code owners." Until you do this,
GitHub's own words are direct: "No one can merge the pull request until you mark the pull request
as ready for review again." You will know it worked because the grey **Draft** label changes to
the usual green **Open** label.

**Sending a ready pull request back to draft:** open the pull request, and in the right-hand
sidebar under Reviewers, click **Convert to draft**, then confirm.

### Reviewing a pull request

**Who can review:** GitHub's own rule, "Anyone with read access can review and comment on proposed
changes." You do not need Write access just to look and comment, Read access to the repository is
enough.

**The click path:**

1. Click the **Pull requests** tab under the repository name, and open the one you want to review.
2. Click the **Files changed** tab to see the diff, the actual lines that changed.
3. **To comment on a specific line:** hover over that line, and click the blue comment icon that
   appears next to it. **To comment on a range of lines:** click the line number of the first line,
   then hold Shift and click the line number of the last one (or drag from the first to the last),
   then click the blue comment icon. **To comment on the whole file** rather than one line, click
   the comment icon next to the file's header instead.
4. When you are done looking, click **Review changes** near the top right of the Files changed tab.
5. Type a summary comment if you have one, then choose one of three options before submitting:
   **Comment**, to leave general feedback without approving; **Approve**, to submit your feedback
   and approve merging the change; or **Request changes**, to flag something that needs fixing
   before it can merge.
6. Click **Submit review**. You will know it worked because your review appears in the pull
   request's timeline on the Conversation tab, labelled with which of the three options you chose.

**Screenshot placeholder:** the Files changed tab with the blue comment icon showing next to one
line, and the Review changes button visible above the diff, so a reader can match both controls to
what is on their own screen.

**One rule worth knowing before you try it:** GitHub's own documentation is direct that "Pull
request authors cannot approve their own pull requests." If you are working alone, on your own
repository, this matters, you genuinely cannot approve your own change through the review button.
It does not lock you out of merging, though. GitHub's own words: "Repository owners and
administrators can merge a pull request even if it hasn't received an approving review." As the
owner of your own repository, you can still merge your own pull request, you just will not see your
own name as an approving reviewer on it, and that is expected, not a fault.

**What "Request changes" actually blocks:** by itself, GitHub's own wording is that it is "purely
informational and will not prevent merging," unless your repository is specifically set up to
require an approval before merging on a private repository, which needs at least GitHub Pro for a
personal account or GitHub Team and above for an organization (covered in
`10-protecting-your-work.md`). Without that setup, a "Request changes" review is a strong signal to
the person who opened the pull request, not a lock on the merge button.

**Why the browser is the right tool for this step, not Claude Code:** reviewing means reading a
diff and leaving comments on exact lines, and that is a visual, click-driven task GitHub's browser
interface is built for. Use Claude Code to make and describe changes; use the browser to look at
and comment on them.

### The three merge methods, and which one this kit recommends

When you are ready to bring a pull request's changes into your main copy, GitHub offers three
different ways to do it. All three are real, documented GitHub features. This kit teaches all
three, and recommends one of them, clearly labelled as this kit's own recommendation, not
GitHub's.

**Merge commit, GitHub's documented default:** GitHub's own wording names this the default option
outright: "When you click the default **Merge pull request** option on a pull request, all commits
from the feature branch are added to the base branch in a merge commit." Every commit from your
branch lands in your main copy individually, plus one extra commit recording the merge itself.
This is the option that is always available, with nothing to turn on first.

**Squash and merge:** GitHub's own wording, "the pull request's commits are squashed into a single
commit." However many separate commits you made on your branch (including any "fix typo" or "try
again" commits along the way), they become one single commit on your main copy. This requires the
repository to allow it, GitHub's own words, "the repository must allow squash merging," a setting
covered below.

**Rebase and merge:** GitHub's own wording, "all commits from the topic branch (or head branch) are
added onto the base branch individually without a merge commit." Similar to a plain merge commit,
except there is no extra merge commit added, just your original commits, replayed straight onto the
main copy. This also requires the repository to allow it, "the repository must allow rebase
merging."

**Squash and merge is this kit's recommendation for your default choice. It is not GitHub's
default, and it is not GitHub's own advice either** (GitHub presents all three as equally valid,
depending on your workflow). The reason we recommend squash and merge specifically for a small
business, usually a single person or a small team: one pull request is usually one change worth
naming, "update the menu prices," "fix the homepage typo," and squashing keeps your main copy's
history as one line per change, instead of every small "fix typo," "fix typo again" commit along
the way cluttering it permanently. Merge commit and rebase and merge both exist and both work, you
are not doing anything wrong if you use them instead, squash and merge is this kit's own
recommendation for keeping a readable history without needing to think about it.

**Where to check or change which methods are available:** on the repository's main page, click
**Settings**, then on the General page scroll down to the **Pull Requests** section. The checkboxes
for **Allow merge commits**, **Allow squash merging**, and **Allow rebase merging** live there. You
will know you are in the right place because all three checkboxes sit together with the merge
button preview beneath them. Which ones are ticked on your own repository right now is worth
checking on your own screen rather than assuming, this kit has not confirmed what a brand-new
repository ships with by default.

**Through Claude Code, once you are ready to merge and have already reviewed the change:**

```
gh pr merge 12 --squash --delete-branch
```

The GitHub CLI's own flags: `--merge` for a merge commit, `--squash` for squash and merge,
`--rebase` for rebase and merge, and `--delete-branch` to delete the branch straight after, in one
step. The number is the pull request's number, shown on its page next to the title.

### "Allow edits from maintainers," and why it deserves a deliberate tick

You will see this checkbox when you open a pull request from a fork of a repository under your own
personal account, not from a plain branch inside the same repository. If you are working the way
this kit teaches by default (a branch inside the same repository you already have Write access to,
covered in `06-branches.md`), you will not see this checkbox at all, because Write access already
covers every branch in that repository, there is nothing extra to grant.

**What it does, when it does apply:** GitHub's own wording, ticking it lets "anyone with push
access to the upstream repository" commit directly to your pull request's branch. In practice, it
means a maintainer of the repository you are proposing changes to can fix a small thing on your
branch themselves, a typo in your commit, a merge conflict, rather than asking you to do it and
waiting.

**Why the tick deserves a genuine decision, not a reflex:** if your fork contains GitHub Actions
workflows, this checkbox's own label changes to warn you, GitHub's own wording, "Allow edits and
access to secrets by maintainers," because granting it in that case "allows a maintainer to edit
the forked repository's workflows, which can potentially reveal values of secrets and grant access
to other branches." Tick it when you trust the repository's maintainers to touch your branch
directly and want the convenience. Leave it unticked if you would rather review and make every
change yourself before it merges, or if your fork carries anything you would not want a stranger
editing.

The checkbox itself sits at the bottom right of the pull request's page, when it applies.

### Closing a pull request without merging

**The click path:**

1. Click **Pull requests** under the repository name.
2. Click the pull request you want to close.
3. At the bottom of the pull request, below the comment box, click **Close pull request**.

You will know it worked because the pull request's status label changes from the green **Open** to
a red **Closed**, and the merge box disappears.

GitHub's own reason this exists: "Close a pull request without merging it to manage unnecessary
changes or address alternative solutions in other branches."

**Closing does not mean the change was rejected.** It means this particular pull request is not
merging as it stands right now. You might close one because the idea changed, because you decided
to redo the work differently on a new branch, or because it turned out you did not need the change
after all. None of those are a verdict on you or the work, closing is just "not this one, not like
this."

**If the only thing wrong is the base branch,** GitHub's own advice is not to close it and start
over: "instead of closing it and opening a new one, you can change the base branch." Look for an
edit control near the title, choose the correct base branch from the dropdown that appears, then
click **Change base**. Confirm the exact click on your own screen the first time, this kit has not
pinned down the precise wording, but the option is real and saves you from redoing the whole pull
request over one wrong dropdown choice.

**Deleting the branch at the same time:** the close screen offers this as a separate, optional
step, GitHub's own wording, "Optionally, delete the branch. This keeps the list of branches in your
repository tidy." Closing the pull request and deleting its branch are two different actions, doing
one does not automatically do the other.

### Deleting the branch afterwards

Once a pull request has merged, or you have closed it without merging and are sure you are done
with it, the branch itself has finished its job. `06-branches.md` covers the full steps, including
the one safety net worth knowing here too: if you delete the branch of a pull request that has
since been closed or merged, GitHub keeps a **Restore branch** button on that pull request's page
for a while, so deleting it is not as final as it feels. Read that file's "Deleting a branch once
it's landed" section before you delete anything you are not fully sure about.

## Strategy: how to actually use this

**A pull request is worth opening whenever someone other than you will look at the change, or
whenever you personally want a deliberate pause to reread your own work before it goes live.**
Neither of those is about the size of the change. A one-line price fix and a full page rebuild are
both worth a pull request if a second person needs to see them first. The reverse is also true: a
large change you are doing entirely alone, that nobody else needs to weigh in on, does not become
more correct just because it went through a pull request.

**A solo operator working alone** loses nothing by skipping pull requests entirely and committing
straight to the default branch, `05-daily-workflow.md` already recommends this at that size. It is
still worth opening one occasionally, specifically when you want the moment of rereading your own
change on the Files changed tab before it goes live, the same value a second pair of eyes gives
someone else, borrowed for yourself. That is a genuine use of the feature even with nobody else on
the repository, not a wasted step.

**A team of two** should use an informal review habit, not an enforced one. One person opens the
pull request, the other glances at the Files changed tab before it merges, and either of them can
merge it. Nothing stops the fix going live immediately if the other person is unavailable and the
change cannot wait. This matches level 2 on the process ladder in this kit's strategy pack: real
value, no subscription cost, nothing that locks you out of your own work.

**A team of three or four, with one technical person**, usually settles into the technical person
reviewing anything that reaches customers, while smaller internal changes merge without waiting on
anyone. Decide once who that person is for which kind of repository, rather than deciding fresh
every time a pull request opens. The failure mode at this size is not too few reviews, it is
opening a pull request and then nobody ever actually looking at the Files changed tab before
merging it, which gives you all the delay of a review process and none of the benefit.

**A team of five or more, or anyone genuinely worried about a mistake reaching customers unseen**,
is the point where an informal habit stops being enough on its own, since a habit only works while
everyone remembers to follow it. That is when to look at requiring an approval before merging is
even possible, a setting covered in `10-protecting-your-work.md`, which on a private repository
needs at least GitHub Pro for a personal account or GitHub Team and above for an organization.
Below that size, the same enforced rule usually buys very little over the habit you already have,
while still costing a subscription and real waiting time.

**What good looks like months later:** your default branch's history reads as one line per real
change, "update the menu prices," "fix the homepage typo," not a scroll of "fix," "fix again,"
"actually fix this time." Every non-trivial change has a description a stranger to the moment could
read and understand. Where a change fixed something someone reported as an issue, the two are
linked, so searching later finds both sides of the story in one place.

**What would change our recommendation:** if squash and merge is genuinely hiding information you
need, for instance a team that relies on reading many small individual commits for a reason
specific to their own work, that is a real reason to use merge commit or rebase and merge instead.
For almost every small business this kit is written for, that reason does not apply, and squash and
merge stays the right default.

## A worked example

The café's staff member, from the team of three described in this kit's strategy pack, is updating
the summer menu. Two mains prices are going up two dollars each, and she is waiting on the supplier
to confirm a third. She already made her edits on a branch called `update-summer-prices`, per
`06-branches.md`, and pushed it.

She opens the menu repository's main page, chooses `update-summer-prices` from the **Branch**
dropdown, and clicks **Compare & pull request** in the yellow banner. For the title she writes
"Update summer menu prices," and in the description, "Mains up two dollars per the new supplier
cost. Still waiting on confirmation for the seafood special before that price is final." Because
one price is not confirmed yet, she opens it as a draft: she clicks the dropdown arrow next to
**Create Pull Request**, chooses **Create Draft Pull Request**, then clicks **Draft Pull Request**.

The supplier confirms the third price the next morning. She updates the file on her branch, commits
the change, and opens the pull request again. In the merge box near the bottom of the Conversation
tab, she clicks **Ready for review**.

The nephew, who reviews anything customer-facing per their informal level-2 habit, opens the
**Files changed** tab. He spots one price typo, "12.50" where it should read "14.50," hovers over
that line, clicks the blue comment icon, and leaves a note. He clicks **Review changes** near the
top of the tab, selects **Request changes**, and submits.

She fixes the typo on the same branch and pushes the correction, which updates the same open pull
request automatically. The nephew opens **Files changed** again, sees the fix, clicks **Review
changes**, selects **Approve**, and submits.

She has Write access on this repository, so she merges it herself. On the pull request's page, she
clicks the dropdown arrow next to the merge button, chooses **Squash and merge**, confirms the
commit message, and clicks **Confirm squash and merge**. On the same screen, she ticks the option
to delete the branch, since its job is done. The menu repository's history now shows one line,
"Update summer menu prices," instead of the draft commit, the typo, and the fix as three separate
entries.

## If it goes wrong

**I don't see the yellow "Compare & pull request" banner, and I can't find a way to start one.**
Click the **Pull requests** tab near the top of the repository, and look for a button to start a
new pull request there instead. If that tab shows nothing at all and you expected to see your
branch, check you are looking at the right repository and that you actually pushed or committed to
that branch, an uncommitted change on your machine does not show up on GitHub yet.

**The merge button is greyed out and I can't click it.** This usually means one of a few things:
your repository requires an approving review before merging and you don't have one yet (see
`10-protecting-your-work.md`), a required check is still running or has failed (look at the
**Checks** tab), or there's a merge conflict between your branch and the base branch (covered in
`08-merge-conflicts.md`). The pull request page itself usually tells you which one, look just above
the merge button for the reason.

**I clicked "Request changes" by mistake, or I want to withdraw a review I already submitted.**
Open the pull request's **Conversation** tab, find your review in the timeline, click the small
chevron or "Show options" control next to it, and choose **Dismiss review**. GitHub's own note:
"Repository administrators or people with write access can dismiss a review." You will be asked to
type a short reason before it dismisses.

**I opened a draft pull request and cannot find "Ready for review" anywhere.** It sits in the merge
box near the bottom of the Conversation tab, below the description and any comments. If your
organization has restricted draft pull requests, per the note above, that same restriction can hide
this option too, ask whoever owns your organization to check.

**My pull request shows a merge conflict and I do not know what that means.** It means git found a
spot where your branch and the base branch changed the same lines in two different ways, and it
needs a person to decide which version is right. `08-merge-conflicts.md` covers the browser's own
conflict resolver and its limits.

## FAQ

**Can I just merge my own pull request if I'm working alone?** Yes. You can't approve your own
pull request through the review button, that's a real GitHub restriction, but as the owner of your
own repository you can merge it without a formal approval anyway. Working solo doesn't lock you
out of your own work.

**Do I even need to open a pull request if it's just me?** No, not strictly. `05-daily-workflow.md`
already covers this: for your own solo repository, committing directly to your branch and merging
is normal. Opening a pull request even when you're alone is still worth doing when you want a
deliberate pause to read your own change back before it goes live, or when you're using Claude Code
to make the change and want to look it over in the browser first.

**What happens if there's a conflict between my branch and the base branch?** `08-merge-conflicts.md`
covers this in full, including the browser's own conflict resolver and its limits.

**Can I reopen a pull request I closed by mistake?** This kit couldn't confirm a documented reopen
button from GitHub's own pages. Open the closed pull request and look near the bottom of the page
for a way to reopen it before assuming there isn't one, GitHub's interface changes and what's on
your own screen is the real answer here.

**Can two people review the same pull request?** Yes, nothing stops more than one person leaving
a review on the same pull request, and if your repository requires more than one approval before
merging, that's exactly how it gets satisfied.

**Does GitHub tell the other person when I've reviewed their pull request?** Confirm this on your
own screen, GitHub's notification behaviour wasn't part of what this kit checked, and it's the kind
of thing that depends on each person's own notification settings.

**Which merge method should I pick if I'm not sure?** Squash and merge, this kit's own
recommendation for most small businesses, covered in full above. Use it unless you already have a
specific reason to want every individual commit preserved on your main copy.

**Does closing a pull request also delete its branch?** No, they're two separate actions. The
close screen offers deleting the branch as an optional extra step, ticking it or not is your
choice each time.

## Quick reference

- **Open a pull request:** repository main page, **Branch** dropdown, **Compare & pull request**,
  choose base and compare, title and description, **Create Pull Request**
- **Open as a draft:** dropdown arrow next to **Create Pull Request**, **Create Draft Pull
  Request**, **Draft Pull Request**
- **Mark a draft ready:** open it, **Ready for review** near the bottom of the Conversation tab
- **Close an issue automatically:** type `Fixes #10` (or `Closes`, `Resolves`, and their other
  forms) in the description
- **Review a change:** **Files changed** tab, **Review changes**, choose Comment, Approve, or
  Request changes, **Submit review**
- **Merge, this kit's recommendation:** dropdown arrow next to the merge button, **Squash and
  merge**
- **Close without merging:** open it, **Close pull request** near the bottom
- **Through Claude Code:** `gh pr create --title "..." --body "..." --base main` to open,
  `gh pr merge 12 --squash --delete-branch` to merge and clean up

## Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
- https://github.blog/changelog/2025-05-01-draft-pull-requests-are-now-available-in-all-repositories/
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/dismissing-a-pull-request-review
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/closing-a-pull-request
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-base-branch-of-a-pull-request
- https://cli.github.com/manual/gh_pr_create
- https://cli.github.com/manual/gh_pr_merge
