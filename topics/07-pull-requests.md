# Pull requests, and getting a change reviewed

A pull request is how a change on your branch gets looked at, discussed, and folded back into your
main copy on purpose. This file covers what a pull request actually is, opening one, writing a
title and description someone can actually review, draft pull requests, reviewing someone else's
pull request, the three ways a pull request can be merged and which one this kit recommends,
the "allow edits from maintainers" tick box, closing a pull request without merging, and deleting
the branch once you're done with it.

Most of what's below happens in your browser, because reviewing a change is exactly the kind of
task where seeing it matters. Wherever Claude Code is genuinely faster instead, this file says so.

If you haven't read `06-branches.md` yet, read that first. A pull request is what you do with a
branch once you want its changes back in your main copy, so branches are assumed knowledge here.

## What a pull request actually is

GitHub's own definition: "Pull requests are proposals to merge code changes into a project." Its
own framing of why the feature exists: "A pull request is GitHub's key collaboration feature,
letting you discuss and review changes before merging them. This helps teams work together, catch
issues early, and maintain code quality."

**In practice, for a small business:** a pull request is you saying "here's a change I want to
make, take a look before it goes live." Nothing on your branch reaches your main copy until someone
(possibly you, working alone) deliberately merges that pull request. Right up until that point, the
change is still just a proposal.

Every pull request's page is organised into tabs, so you always know where to look for a given
kind of information. GitHub's own list: the **Conversation** tab shows the description, timeline,
comments, and reviews; the **Commits** tab shows how the branch changed over time; the **Checks**
tab shows automated tests, builds, and other validations; the **Files changed** tab shows the diff
reviewers use to see exactly what changed; and, where code scanning is set up, a **Findings** tab
shows automated code review results. You'll use Conversation and Files changed the most.

**Screenshot placeholder:** an open pull request's page, with the row of tabs (Conversation,
Commits, Checks, Files changed) visible along the top, so a reader can see where each one sits
before clicking through them.

## Opening a pull request

**Who can do this:** GitHub's own requirement, for a public repository: "you must have write access
to the head or the source branch or, for organization-owned repositories, you must be a member of
the organization that owns the repository." In plain terms, the same rule as branches: if you can't
push to the branch, you can't open a pull request from it. If that's you, you're either missing
access (see `03-members-and-access.md`) or you're contributing to someone else's project rather
than your own team's, which is a fork, covered in `09-forks-and-contributing.md`.

**The click path, once you've committed on a branch:**

1. On the repository's main page, choose your branch from the **Branch** menu.
2. Above the file list, click **Compare & pull request** in the yellow banner GitHub shows you.
3. Use the **base** branch dropdown to choose the branch you want your changes merged into (usually
   your default branch), and the **compare** branch dropdown to confirm the branch your changes are
   on.
4. Type a title and description for your pull request (the next section covers what to actually
   write here).
5. Click **Create Pull Request**.

**If you don't see the yellow banner** (you navigated away, or it's been a while since you
committed), it's still there under the **Pull Requests** tab near the top of the repository. Open
that tab and look for a button to start a new one, then pick your base and compare branches from
there. The exact label on that button is worth confirming on your own screen, since this kit
couldn't pin down the precise wording from GitHub's own documentation.

**If you made your change through the browser file editor** and picked "Create a new branch for
this commit and start a pull request" (covered in `05-daily-workflow.md`), you've already skipped
this whole step. Clicking **Propose changes** there opens the pull request for you. Go straight to
writing the title and description below.

**Screenshot placeholder:** the yellow "Compare & pull request" banner above a repository's file
list, so a reader recognises it the first time they see it.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in** (the
same one-time setup mentioned in `04-repositories-and-visibility.md` and `05-daily-workflow.md`):
ask it in plain English, or let it run something like this on your behalf:

```
gh pr create --title "Update the menu prices" --body "Raises the mains section by two dollars, matches the new supplier cost." --base main
```

That's the GitHub CLI's own flags: `--title`, `--body`, and `--base` for the branch you're merging
into. Add `--draft` to open it as a draft (covered below) instead of ready for review. This is a
genuinely good shortcut once `gh` is set up, particularly if you're already asking Claude Code to
make the change for you and don't want to switch to the browser mid-task. If `gh` isn't installed
and signed in yet, use the browser path above instead.

## Writing a title and description someone can actually review

GitHub doesn't enforce any particular format here, the title and description fields are free text.
**A practical convention worth adopting, not a GitHub rule:** write the title as what the change
does, in plain words, the way you'd say it out loud, "Update the menu prices" rather than "changes"
or your own name. In the description, say what changed and why, in a sentence or two. A reviewer
who wasn't in the room with you should be able to read the description and know what they're
about to look at before they open a single file.

**One real feature worth knowing, if this repository also uses GitHub Issues:** typing a keyword
followed by an issue number in the description links the two, and closes the issue automatically
the moment the pull request merges. GitHub's own list of keywords includes `close`, `closes`,
`closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves`, and `resolved`. Typing `Fixes #10` in your
description does exactly what it says: when this pull request merges, issue 10 closes with it, and
GitHub links the two on both pages automatically.

**If you need to change the title or description after opening it:** there's an edit control near
the top of the pull request, next to the title. Confirm the exact click on your own screen the
first time you need it, this kit hasn't pinned it down word for word, but the option to edit
after the fact is real, you're not locked into what you typed when you clicked Create.

## Draft pull requests

A draft pull request is the same proposal, marked as not ready yet. GitHub's own description:
"Draft pull requests cannot be merged, and code owners are not automatically requested to review
them." Use one when you want to start the conversation, or back your work up on GitHub, before
the change is actually finished.

**This is genuinely free, on every plan, in every repository, as of a specific date, and older
guides get this wrong.** Draft pull requests used to be limited: only available in public
repositories on GitHub's Free plan. That changed on 1 May 2025. GitHub's own changelog entry for
that date: "You can now create draft pull requests in any repository, public or private, completely
free of charge." If you've read an older tutorial that says draft pull requests need a paid plan,
or only work on public repositories, that's out of date. It doesn't matter what plan you're on or
whether your repository is public or private, drafts work the same everywhere now.

**Opening one:** from the same "Create Pull Request" screen above, click the dropdown arrow next to
the **Create Pull Request** button and choose **Create Draft Pull Request**, then click **Draft
Pull Request**.

**One message you might see, and it's real:** GitHub's own documentation includes this line: "If
you are the member of an organization, you may need to request access to draft pull requests from
an organization owner." If that message shows up, it's a genuine organization-level setting, not
an error on your end, ask whoever owns your organization to sort it out.

**Marking a draft ready for review:** open the pull request and, in the merge box near the bottom,
click **Ready for review**. GitHub's own note on what that does: "Marking a pull request as ready
for review will request reviews from any code owners." Until you do this, GitHub's own words are
direct: "No one can merge the pull request until you mark the pull request as ready for review
again."

**Sending a ready pull request back to draft:** open the pull request, and in the right sidebar
under Reviewers, click **Convert to draft**, then confirm.

## Reviewing a pull request

**Who can review:** GitHub's own rule, "Anyone with read access can review and comment on proposed
changes." You don't need Write access just to look and comment, Read access to the repository is
enough.

**The click path:**

1. Click the **Pull requests** tab under the repository name, and open the one you want to review.
2. Click the **Files changed** tab to see the diff, the actual lines that changed.
3. **To comment on a specific line:** hover over that line, and click the blue comment icon that
   appears next to it. **To comment on a range of lines:** click the line number of the first line,
   then hold Shift and click the line number of the last one (or drag from the first to the last),
   then click the blue comment icon. **To comment on the whole file** rather than one line, click
   the comment icon next to the file's header instead.
4. When you're done looking, click **Review changes** near the top of the Files changed tab.
5. Type a summary comment if you have one, then choose one of three options before submitting:
   - **Comment:** GitHub's own wording, "leave general feedback without explicitly approving."
   - **Approve:** "submit your feedback and approve merging the changes."
   - **Request changes:** "submit feedback that must be addressed before the pull request can be
     merged."
6. Click **Submit review**.

**Screenshot placeholder:** the Files changed tab with the blue comment icon showing next to one
line, and the Review changes button visible above the diff, so a reader can match both controls to
what's on their own screen.

**One rule worth knowing before you try it:** GitHub's own documentation is direct that "Pull
request authors cannot approve their own pull requests." If you're working alone, on your own
repository, this matters, you genuinely cannot approve your own change through the review button.
It doesn't lock you out of merging, though, GitHub's own words: "Repository owners and
administrators can merge a pull request even if it hasn't received an approving review." As the
owner of your own repository, you can still merge your own pull request, you just won't see your
own name as an approving reviewer on it, and that's expected, not a bug.

**What "Request changes" actually blocks:** by itself, GitHub's own wording is that it's "purely
informational and will not prevent merging," unless your repository is specifically set up to
require an approval before merging (covered in `10-protecting-your-work.md`). Without that setup,
a "Request changes" review is a strong signal to the person who opened the pull request, not a
lock on the merge button.

**Why the browser is the right tool for this step, not Claude Code:** reviewing means reading a
diff and leaving comments on exact lines, and that's a visual, click-driven task GitHub's browser
interface is built for. Use Claude Code to make and describe changes; use the browser to look at
and comment on them.

## The three merge methods, and which one this kit recommends

When you're ready to bring a pull request's changes into your main copy, GitHub offers three
different ways to do it. All three are real, documented GitHub features. This kit teaches all
three, and recommends one of them, clearly labelled as this kit's own recommendation, not
GitHub's.

**Merge commit, GitHub's documented default:** GitHub's own wording names this the default option
outright: "When you click the default **Merge pull request** option on a pull request, all commits
from the feature branch are added to the base branch in a merge commit." Every commit from your
branch lands in your main copy individually, plus one extra commit recording the merge itself. This
is the option that's always available, with nothing to turn on first.

**Squash and merge:** GitHub's own wording, "the pull request's commits are squashed into a single
commit." However many separate commits you made on your branch (including any "fix typo" or "try
again" commits along the way), they become one single commit on your main copy. This requires the
repository to allow it, GitHub's own words, "the repository must allow squash merging," a setting
covered below.

**Rebase and merge:** GitHub's own wording, "all commits from the topic branch (or head branch) are
added onto the base branch individually without a merge commit." Similar to a plain merge commit,
except there's no extra merge commit added, just your original commits, replayed straight onto the
main copy. This also requires the repository to allow it, "the repository must allow rebase
merging."

**Squash and merge is our recommendation for your default choice. It is not GitHub's default, and
it is not GitHub's own advice either** (GitHub presents all three as equally valid, depending on
your workflow). The reason we recommend squash and merge specifically for a small business, usually
a single person or a small team: one pull request is usually one change worth naming, "update the
menu prices," "fix the homepage typo," and squashing keeps your main copy's history as one line per
change, instead of every small "fix typo," "fix typo again" commit along the way cluttering it
permanently. Merge commit and rebase and merge both exist and both work, you're not doing anything
wrong if you use them instead, squash and merge is this kit's own recommendation for keeping a
readable history without needing to think about it.

**Where to check or change which methods are available:** on the repository's main page, click
**Settings**, then on the General page scroll to the **Pull Requests** section. The checkboxes for
**Allow merge commits**, **Allow squash merging**, and **Allow rebase merging** live there. Which
ones are ticked on your own repository right now is worth checking on your own screen rather than
assuming, this kit hasn't confirmed what a brand-new repository ships with by default.

**Through Claude Code, once you're ready to merge and have already reviewed the change:**

```
gh pr merge 12 --squash --delete-branch
```

The GitHub CLI's own flags: `--merge` for a merge commit, `--squash` for squash and merge, `--rebase`
for rebase and merge, and `--delete-branch` to delete the branch straight after, in one step. The
number is the pull request's number, shown on its page next to the title.

## "Allow edits from maintainers," and why it deserves a deliberate tick

You'll see this checkbox when you open a pull request from a fork of a repository under your own
personal account, not from a plain branch inside the same repository. If you're working the way
this kit teaches by default (a branch inside the same repository you already have Write access to,
covered in `06-branches.md`), you won't see this checkbox at all, because Write access already
covers every branch in that repository, there's nothing extra to grant.

**What it does, when it does apply:** GitHub's own wording, ticking it lets "anyone with push access
to the upstream repository" commit directly to your pull request's branch. In practice, it means a
maintainer of the repository you're proposing changes to can fix a small thing on your branch
themselves, a typo in your commit, a merge conflict, rather than asking you to do it and waiting.

**Why the tick deserves a genuine decision, not a reflex:** if your fork contains GitHub Actions
workflows, this checkbox's own label changes to warn you, GitHub's own wording, "Allow edits and
access to secrets by maintainers," because granting it in that case "allows a maintainer to edit
the forked repository's workflows, which can potentially reveal values of secrets and grant access
to other branches." Tick it when you trust the repository's maintainers to touch your branch
directly and want the convenience. Leave it unticked if you'd rather review and make every change
yourself before it merges, or if your fork carries anything you wouldn't want a stranger editing.

The checkbox itself sits at the bottom right of the pull request's page, when it applies.

## Closing a pull request without merging

**The click path:**

1. Click **Pull requests** under the repository name.
2. Click the pull request you want to close.
3. At the bottom of the pull request, below the comment box, click **Close pull request**.

GitHub's own reason this exists: "Close a pull request without merging it to manage unnecessary
changes or address alternative solutions in other branches."

**Closing doesn't mean the change was rejected.** It means this particular pull request isn't
merging as it stands right now. You might close one because the idea changed, because you decided
to redo the work differently on a new branch, or because it turned out you didn't need the change
after all. None of those are a verdict on you or the work, closing is just "not this one, not like
this."

**If the only thing wrong is the base branch,** GitHub's own advice is not to close it and start
over: "instead of closing it and opening a new one, you can change the base branch." Look for an
edit control near the title, choose the correct base branch from the dropdown that appears, then
click **Change base**. Confirm the exact click on your own screen the first time, this kit hasn't
pinned down the precise wording, but the option is real and saves you from redoing the whole pull
request over one wrong dropdown choice.

**Deleting the branch at the same time:** the close screen offers this as a separate, optional
step, GitHub's own wording, "Optionally, delete the branch. This keeps the list of branches in your
repository tidy." Closing the pull request and deleting its branch are two different actions, doing
one doesn't automatically do the other.

## Deleting the branch afterwards

Once a pull request has merged, or you've closed it without merging and you're sure you're done
with it, the branch itself has finished its job. `06-branches.md` covers the full steps, including
the one safety net worth knowing here too: if you delete the branch of a pull request that's since
been closed or merged, GitHub keeps a **Restore branch** button on that pull request's page for a
while, so deleting it isn't as final as it feels. Read that file's "Deleting a branch once it's
landed" section before you delete anything you're not fully sure about.

---

## If it goes wrong

**I don't see the yellow "Compare & pull request" banner, and I can't find a way to start one.**
Click the **Pull requests** tab near the top of the repository, and look for a button to start a
new pull request there instead. If that tab shows nothing at all and you expected to see your
branch, check you're looking at the right repository and that you actually pushed or committed to
that branch, an uncommitted change on your machine doesn't show up on GitHub yet.

**The merge button is greyed out and I can't click it.** This usually means one of a few things:
your repository requires an approving review before merging and you don't have one yet (see
`10-protecting-your-work.md`), a required check is still running or has failed (look at the
**Checks** tab), or there's a merge conflict between your branch and the base branch (covered in
`08-merge-conflicts.md`). The pull request page itself usually tells you which one, look just above
the merge button for the reason.

**I clicked "Request changes" by mistake, or I want to withdraw a review I already submitted.**
Open the pull request's **Conversation** tab, find your review in the timeline, click the small
chevron or "Show options" control next to it, and choose **Dismiss review**. GitHub's own note:
"Repository administrators or people with write access can dismiss a review." You'll be asked to
type a short reason before it dismisses.

## Questions people ask here

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

---

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
