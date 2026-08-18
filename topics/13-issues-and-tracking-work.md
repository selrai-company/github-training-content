# Issues, and keeping track of what needs doing

## What this gets you

An issue is a numbered note about something that needs doing, or something that is broken,
that anyone with access to your repository can see, comment on, and mark done. It lives next
to the work itself rather than in a separate app, so nothing gets tracked in one place and
built in another.

For a small business, this replaces the sticky note, the "can you fix the thing on the
website" text message nobody can find again, and the spreadsheet tab everyone forgets to
open. Every issue has its own page, its own number, and a record of who said what and when.
Six months from now, you can search for it and find out exactly what was asked for, who did
it, and how it was closed. That searchable record is the actual value here, more than any
single issue on its own.

## Before you start

**You need a repository.** Issues belong to one repository at a time. If you have not created
one yet, `04-repositories-and-visibility.md` covers that first.

**You need to know your access level.** GitHub's own permissions table for a repository role
states that the **Read** role can "open issues," "close issues they opened themselves,"
"reopen issues they closed themselves," and "have an issue assigned to them." Closing or
reopening an issue someone else opened, applying a label, or assigning an issue to another
person needs the **Triage** role or higher, which GitHub's own table lists as able to "close,
reopen, and assign all issues and pull requests" and "apply/dismiss labels." If you are not
sure what your own role is, `03-members-and-access.md` covers checking it.

**It does not matter what the repository is for.** Issues work the same on a repository full
of code, a repository that only holds documents, or an empty repository with nothing in it
yet. Tracking work and building the work are two separate things, and GitHub keeps them
separate on purpose.

**You do not need to have read the branches or pull requests files first**, unless you want
the section below on closing an issue from a pull request to make full sense. Everything else
here stands on its own.

## The words you need

**Issue.** A numbered note, with a title, a description, and a comment thread underneath it,
attached to one repository. GitHub's own description: "Issues can track bug reports, new
features and ideas, and anything else you need to write down or discuss with your team."

**Assignee.** The person, or people, marked as responsible for an issue. An issue can have more
than one.

**Label.** A short coloured tag you attach to an issue to sort it into a category, like `bug`
or `question`.

**Milestone.** A named group of issues and pull requests you are tracking together, usually
because they all belong to the same piece of work or the same date.

**Closing.** Marking an issue as done. GitHub records a reason alongside the close: whether the
work was completed, or the issue is not going to be actioned at all.

**Linking keyword.** A word like `Closes` or `Fixes`, typed in front of an issue number inside
a pull request, that closes the issue automatically the moment that pull request merges.

**Search qualifier.** A short piece of text you type into the issue search box, like
`is:open` or `label:bug`, that narrows the list down to exactly what you are looking for.

**Issue template.** A pre-written form, or a pre-written starting point, that asks the same set
of questions every time someone opens a new issue of a particular kind, like a bug report.

## How to do it

### Creating an issue

**In the browser:**

1. On the repository's front page, along the top, in the row of tabs that starts with **Code**,
   click **Issues**.
2. Click the green **New issue** button.
3. If the repository has issue templates set up (covered below), pick the one that matches what
   you are reporting. If it does not, or none of the templates fit, click **Open a blank issue**.
4. Type a title, and a description underneath it.
5. Click **Submit new issue**.

You will know it worked because the issue opens on its own page with a number next to its title,
starting from 1 the first time you use Issues on that repository, and counting up from there
every time after.

**One thing worth knowing before you start:** GitHub's own documentation notes that
"Repository administrators can disable issues for a repository." If you do not see an **Issues**
tab at all on a repository where you expect one, that is the most likely reason, not a fault on
your end. Whoever administers that repository can turn it back on from its settings.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in** (the
same one-time setup covered in `04-repositories-and-visibility.md` and `05-daily-workflow.md`):

```
gh issue create --title "Homepage shows last year's opening hours" --body "The long weekend hours are wrong on the homepage banner." --label bug
```

The GitHub CLI's own flags: `--title` and `--body` for the issue itself, `--label` to attach a
label straight away (the label needs to already exist in the repository, covered below),
`--assignee` to assign someone at the same time (use `@me` to assign yourself), and `--milestone`
to add it to a milestone by name. This is a genuinely fast way to log something the moment you
notice it, without switching to the browser.

### Titles that are useful in six months

GitHub does not enforce any particular format for a title, it is free text. The habit worth
having is writing the title as the problem or the request, in plain words, specific enough that
you could search for it later and find it without opening the issue. "Homepage shows last year's
opening hours" tells you everything at a glance. "Website bug" does not, and if you have ten
issues all titled some version of "bug" or "fix this," the search box stops being useful to you.

Put the specific detail in the title, not just the description. A person scanning a list of
thirty issue titles is deciding what to open based on the title alone.

### Assigning someone

**The click path:**

1. Open the issue.
2. In the right-hand sidebar, click **Assignees**.
3. Start typing the person's username, then click their name when it appears.

**Who can be assigned:** GitHub's own wording: "You can assign multiple people to each issue or
pull request, including: yourself, anyone who has commented on the issue or pull request, anyone
with write permissions to the repository, and organization members with read permissions to the
repository." In practice, if someone is not showing up in the assignee list, they either have not
been added to the repository yet (`03-members-and-access.md` covers adding someone), or they need
to leave a comment on the issue first before they can be assigned to it.

**How many people can be assigned to one issue:** GitHub's own limit, "Both issues and pull
requests support up to 10 assignees." Most small teams will never come close to that.

### Labels, and what they are for

A label is a short answer to "what kind of thing is this," attached to the issue as a coloured
tag. GitHub's own description of the feature: you use labels to "classify issues, pull requests,
and discussions."

**Every new repository starts with ten labels already created.** GitHub's own descriptions of
each:

| Label | GitHub's own description |
|---|---|
| `bug` | "Indicates an unexpected problem or unintended behavior" |
| `documentation` | "Indicates a need for improvements or additions to documentation" |
| `duplicate` | "Indicates similar issues, pull requests, or discussions" |
| `enhancement` | "Indicates new feature requests" |
| `good first issue` | "Indicates a good issue for first-time contributors" |
| `help wanted` | "Indicates that a maintainer wants help on an issue or pull request" |
| `invalid` | "Indicates that an issue, pull request, or discussion is no longer relevant" |
| `question` | "Indicates that an issue, pull request, or discussion needs more information" |
| `wontfix` | "Indicates that work won't continue on an issue, pull request, or discussion" |
| `accessibility` | "Indicates a barrier affecting people with disabilities" |

For a small business, `bug` and `question` usually get the most use. The rest are there if you
want them, and nothing forces you to use any label at all.

**Applying a label to an issue:** open the issue, and in the right-hand sidebar click **Labels**,
then tick the ones that apply.

**Creating your own label:**

1. On the repository's front page, click **Issues**.
2. Above the list, click **Labels**.
3. Click **New label**.
4. Type a name and, if you want one, a short description, then pick a colour.
5. Click **Create label**.

**Who can do each of these:** GitHub's own wording, "Anyone with write access to a repository can
create a label," and "triage access to a repository" is enough to "apply and dismiss labels" on
an existing issue without needing to create new ones.

### Milestones

A milestone groups a set of issues and pull requests together, usually because they belong to
the same piece of work. GitHub's own description: "You can use milestones to track progress on
groups of issues or pull requests in a repository." Once you have created one, its page shows
the number of open and closed issues attached to it, and its own completion percentage, worked
out automatically from how many of its issues are closed.

**Creating one:**

1. On the repository's front page, click **Issues**.
2. Above the list, click **Milestones**.
3. Click **New Milestone**.
4. Type a title and, if you want one, a description.
5. Click **Create milestone**.

GitHub's own milestone page lists a due date among what it displays. This kit could not confirm
the exact field name on the creation screen itself from GitHub's own documentation text, so
confirm on your own screen whether a due date field is offered when you create one, or only once
you go back in to edit it.

**Attaching an issue to a milestone:** open the issue, and in the right-hand sidebar click
**Milestone**, then pick it from the list.

A milestone is worth setting up once you have several issues that only make sense together, a
website relaunch, a season's worth of menu changes. For a handful of loose, unrelated issues, a
milestone adds a layer you do not need yet.

### Closing an issue

**The click path:**

1. Open the issue.
2. At the bottom, below the comment box, choose a close reason from the dropdown next to the
   close button if you want to record one, then click **Close issue**.

GitHub's own framing of why you would close one: "You can close an issue when bugs are fixed,
feedback is acted on, or to show that work is not planned." Those are the two reasons GitHub
lets you record: the work is done, or it is not happening. Recording the right one matters for
your own future searching, an issue closed as "not planned" and one closed as "completed" mean
very different things when you come back to it later.

### Closing an issue from a pull request, so the two link up

This is the part that makes issues and pull requests work together instead of as two separate
lists. Typing a linking keyword in front of an issue number, inside a pull request's description
or a commit message, closes that issue automatically the moment the pull request merges, and
GitHub links the two pages to each other permanently.

GitHub's own list of keywords: `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`,
`resolves`, and `resolved`. Typing `Fixes #7` in a pull request's description does exactly that,
when this pull request merges, issue 7 closes with it.

**This only works for a pull request merging into the repository's default branch.** GitHub's
own wording: "When you merge a linked pull request into the default branch of a repository, its
linked issue is automatically closed."

**A plain `#7` on its own, with no keyword in front of it, does not close anything.** GitHub
turns any `#` followed by a number into a clickable link automatically, "references to issues
and pull requests are automatically converted to shortened links," but a link on its own is just
a cross-reference. Only a keyword in front of the number closes the issue.

**Linking manually, without typing a keyword:** open the issue, click **Development** in the
right-hand sidebar, choose the repository, then choose the pull request or branch, and click
**Apply**. Both the issue and the pull request need to be in the same repository for this
particular method.

### Searching and filtering your issues

The **Issues** tab opens with a search box above the list, already filled with a starting query.
GitHub's own documented example of that starting query is `is:issue is:open`, showing you
everything open and nothing closed. You edit that text directly, or use the dropdown buttons
above the list.

**The dropdown buttons above the list, GitHub's own layout:** an **Assignee** dropdown to "find
items based on who's working on them," and a **Labels** button to filter by label.

**Typing search qualifiers directly, GitHub's own examples:**

- `is:open` or `is:closed` for status.
- `assignee:octocat` for who it is assigned to.
- `author:octocat` for who opened it.
- `label:"bug"` for a single label. GitHub's own note on combining more than one: `label:"bug"
  label:"wip"` finds issues with both labels, while `label:"bug","wip"` finds issues with
  either one.
- `-author:octocat` to exclude someone, the minus sign works in front of most qualifiers.

**Sharing a filtered view with someone else:** GitHub's own wording, "your browser's URL is
automatically updated to match the new view" as you filter. Copy the address bar once you have
the list looking the way you want, and it takes anyone else with access straight to the same
filtered list.

### Issue templates, so the same questions get asked every time

An issue template is a pre-written starting point that asks the same questions every time someone
opens a new issue of a particular kind. GitHub's own description: templates are helpful "when you
want to provide guidance for opening issues while allowing contributors to specify the content of
their issues."

**Setting one up through the browser, without touching any code:**

1. On the repository's front page, click **Settings**.
2. Find the **Issues** section on the General settings page, and click **Set up templates**. If
   you do not see this option, Issues may need to be turned on for the repository first.
3. Use the **Add template** dropdown to choose a starting point, such as "Bug report" or
   "Feature request," or start from a blank custom template.
4. Click **Preview and edit**, and use the pencil icon to change the wording to match your own
   business.
5. Click **Propose changes**, add a short commit message, choose whether to commit it directly or
   open it as a pull request, then click **Commit changes**.

GitHub's own note on where these live once created: "Issue templates are stored on the
repository's default branch, in a hidden `.github/ISSUE_TEMPLATE` directory. If you create a
template in another branch, it will not be available for collaborators to use." You do not need
to know that folder exists to use the browser setup above, it is worth knowing only so you
understand why a template made on a side branch will not show up for anyone yet.

## Strategy: how to actually use this

**An issue is the right tool when the answer needs to survive the conversation that created it.**
If you would be upset to lose the message in six weeks because you cannot remember who was meant
to do what, write an issue. If the answer is genuinely disposable, "can you grab lunch on the way
in," a conversation is still just a conversation, and turning every message into an issue is how
this stops getting used at all.

**A useful rule of thumb: one issue, one outcome.** If you cannot describe what "done" looks like
for the issue in a sentence, it is probably two issues, or it is not ready to be written down yet.

**A solo operator working alone** gets less out of issues day to day, since there is nobody else
to hand work to and no comment thread to wait on. It is still worth opening one for anything you
would otherwise forget between now and when you get to it, the running list beats the mental
list, and it costs nothing extra to keep.

**A two-person business should use issues for anything that crosses between the two of you**,
and skip them for anything that stays with one person and gets done the same day. If your business
partner needs to know something happened, or needs to do something themselves, write it down as
an issue with their name in the assignee field. If it is a two-minute fix you are doing yourself
right now, doing it is faster than filing it. The failure mode at this size is not too few
issues, it is opening one for everything and ending up with a list nobody reads because half of
it was never worth writing down.

**Do not reach for labels or milestones before you need them.** A team of two or three people
with a dozen open issues can read the whole list in one glance, a label buys them nothing yet. Add
labels once scanning the raw list stops being fast enough, and add a milestone once you have a
genuine batch of issues that only make sense finished together, not because a template says you
should have one.

**What good looks like months later:** a closed issue is a record, not just a task ticked off.
Coming back and reading "Homepage shows last year's opening hours, closed as completed, fixed in
pull request 14" tells you exactly what happened and when, without anyone having to remember it
or explain it again. That record is the actual return on the small amount of extra typing an
issue costs over a text message.

## A worked example

A café owner runs an online ordering site, built and kept running by her nephew. A staff member
updates the menu text and opening hours from time to time. This is the same team of three
described in the strategy pack for this kit.

Over the long weekend, the staff member notices the ordering site's homepage still shows last
week's opening hours. She does not have Write access to the repository, so she cannot fix the
homepage text herself, but her Read access is enough to open an issue about it.

She opens **Issues**, clicks **New issue**, and titles it "Homepage shows last week's opening
hours instead of the long weekend hours." In the description, she writes what she saw and when.
She clicks **Submit new issue**. It becomes issue number 23.

The nephew sees it, since he checks the repository's Issues tab most mornings. He assigns himself
by opening the issue and clicking **Assignees**, then applies the `bug` label so it is easy to
find later among everything else in the repository. He fixes the homepage text on a branch, opens
a pull request, and types `Fixes #23` in the pull request's description.

When he merges the pull request, issue 23 closes on its own, and GitHub links the two pages to
each other. Three months later, if the same mistake happens again, either of them can search
`is:closed label:bug` on the Issues tab, find issue 23, and see exactly what fixed it last time
instead of starting from nothing.

## If it goes wrong

**I cannot find the Issues tab on a repository where I expect one.** A repository administrator
can turn Issues off entirely, per GitHub's own documentation. Ask whoever administers that
repository whether it has been switched off, rather than assuming you are looking in the wrong
place.

**I typed someone's username into the assignee box and nothing appears.** GitHub only offers
people who already have access to the repository, or who have already left a comment on that
specific issue, as options. Check they have been added to the repository at all
(`03-members-and-access.md`), or ask them to leave a comment on the issue first.

**I closed an issue by mistake and want it back.** This kit could not confirm a documented
reopen button from GitHub's own pages. Open the closed issue and look near the bottom of the
page for a way to reopen it before assuming there is not one, GitHub's interface changes, and
what is actually on your screen is the real answer here.

**I deleted an issue and now regret it.** GitHub's own documentation does not describe any way
to undo a deleted issue, so treat deleting one as final. It is also deliberately hard to do by
accident: GitHub's own wording is that "only accounts with admin or owner permissions can delete
issues" in an organization's repository, and on a personal account's repository, "the only
account that can delete issues in a repository owned by a personal account is that account."
Closing, not deleting, is almost always what you actually want.

**The "Set up templates" button is not there on the Settings page.** Confirm Issues is switched
on for the repository first, this option lives under the Issues section of General settings and
will not appear if Issues itself is off.

## FAQ

**Do I need Write access to open an issue?** No. GitHub's own permissions table lists opening
an issue as something the **Read** role can do. Anyone you have given access to the repository
at all can open one.

**Can two people be assigned to the same issue?** Yes. GitHub's own limit is up to 10 assignees
on a single issue, so more than one person can share responsibility for it.

**Does mentioning an issue number somewhere close it?** Only if a closing keyword like `Closes`
or `Fixes` comes directly before the number, and only inside a pull request or commit that then
merges into the default branch. A plain `#23` on its own turns into a clickable link, GitHub does
this automatically for any issue or pull request number, but it does not close anything by
itself.

**Can I turn an issue into a pull request, or the other way around?** This kit could not confirm
a documented, direct way to convert one into the other from GitHub's own pages. Treat
them as two related but separate things: open a pull request as normal and link it to the issue
with a closing keyword instead.

**Do issues cost anything extra?** This kit did not find a plan restriction on Issues in GitHub's
own documentation, unlike some other features covered elsewhere in this kit. Confirm your own
plan's feature list on GitHub's own pricing page if you want certainty before relying on it.

**What happens to an issue's number if I delete the issue?** Not confirmed from GitHub's own
documentation text. Assume the number is not reused, and check your own repository's next new
issue if you want to be certain.

## Quick reference

- **New issue:** Issues tab, **New issue**, title and description, **Submit new issue**
- **Assign someone:** open the issue, **Assignees** in the sidebar, pick a name
- **Apply a label:** open the issue, **Labels** in the sidebar, tick one
- **Create a label:** Issues tab, **Labels**, **New label**
- **Create a milestone:** Issues tab, **Milestones**, **New Milestone**
- **Close an issue:** open the issue, pick a close reason, **Close issue**
- **Close from a pull request:** type `Fixes #7` (or `Closes`, `Resolves`, and their other forms)
  in the pull request's description
- **Default search:** `is:issue is:open` in the search box above the issue list
- **Set up templates:** repository **Settings**, Issues section, **Set up templates**
- **Through Claude Code:** `gh issue create --title "..." --body "..." --label bug --assignee @me`

## Sources

- https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/assigning-issues-and-pull-requests-to-other-github-users
- https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels
- https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones
- https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/creating-and-editing-milestones-for-issues-and-pull-requests
- https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue
- https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/deleting-an-issue
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls
- https://cli.github.com/manual/gh_issue_create
- https://cli.github.com/manual/gh_issue_list
- https://cli.github.com/manual/gh_issue_close
