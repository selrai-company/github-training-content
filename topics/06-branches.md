# Branches, and changing things without breaking them

## What this gets you

A branch lets you try a change on GitHub with zero risk to the version everyone else is already
relying on. Update a page on your website, draft a new price list, test a rewrite of a policy
document, or build a new feature, and if it works you bring it across; if it doesn't, you've lost
nothing and nobody else ever saw the mess. This is also what lets more than one person work on the
same project at the same time without stepping on each other's changes.

## Before you start

**You need a repository.** A branch lives inside one repository. If you haven't created one yet,
`04-repositories-and-visibility.md` covers that first.

**You need Write access to create or delete a branch.** GitHub's own documentation: "You can only
create a branch in a repository to which you have write access." If you only have Read access, you
can still view a repository's branches and switch between them, you just can't create, rename, or
delete one yourself. `03-members-and-access.md` covers checking your own role and how someone grants
you a higher one.

**You do not need to know any git commands.** Every member of this kit has Claude Code on the Max
plan, and it already has git available. Everything below either happens by clicking around your
browser, or by describing what you want to Claude Code in plain English.

**You don't need to have read the pull requests file first**, unless you want the section below on
what happens when someone else changes main to make full sense before you get there. Everything
else here stands on its own.

## The words you need

**Branch.** A private, working copy of your repository's files that lets you change things without
touching the version everyone else relies on. Picture the main version of your project as the
master copy of an important document, sitting somewhere everyone in the business relies on.
Instead of scribbling directly on the master copy, you photocopy it, mark up the photocopy, and
leave the original completely untouched while you work. That photocopy is a branch. Why it
matters: a mistake on a branch can't reach anyone else, and it costs nothing to throw away if the
change doesn't work out.

**Default branch.** The one branch GitHub treats as the "main" branch of a repository: the branch
people see first when they visit it, and the branch a new branch copies from unless you tell it
otherwise. GitHub's own definition: "The default branch is the base branch for pull requests and
code commits." New repositories name this branch `main`. Why it matters: it's the version
everyone else is relying on, which is exactly why you protect it by working on a branch instead of
editing it directly.

**Branch source.** The branch you're copying from when you create a new branch. GitHub asks you to
pick one every time you create a branch. Why it matters: unless you have a specific reason to
branch off something else, your branch source should be your default branch, so knowing what the
question means saves you a moment of confusion the first time you see it.

**Write access.** The permission level that lets you push changes to a repository, including
creating, renaming, and deleting branches. Read access lets you look and copy; Write access lets
you change. Why it matters: without it, creating a branch directly in that repository isn't
possible, and `09-forks-and-contributing.md` covers the path that works instead.

**Merge.** Folding one branch's changes into another, usually your default branch, so everyone
sees them. Why it matters: nothing you do on a branch reaches anyone else until a merge happens on
purpose. This is covered in full in `07-pull-requests.md`, not here; until that deliberate step,
whatever you do on your branch stays on your branch.

**Head branch.** The branch that holds the changes being proposed, most often seen in the phrase
"restore the head branch of a closed pull request." Why it matters: you'll see this exact term on
GitHub's own restore-branch screen, and it just means "the branch this pull request was built
from."

**Out of sync.** GitHub's own term for when your branch has fallen behind the default branch,
because other changes have been merged into the default branch since you branched off it. Why it
matters: it isn't a problem with your branch, but it does mean you'll want to catch up before you
merge, and GitHub shows an **Update branch** button on the pull request page when this happens.

**Rebase.** One of two ways to catch your branch up with, or merge it into, the default branch,
where your branch's changes are replayed on top of the latest default branch instead of recording a
separate merge. The alternative is a traditional merge, which keeps a record of both histories.
Why it matters: GitHub offers you this choice through its own **Update branch** button, covered
below, and neither option is wrong, they just leave a different-looking history behind.

**Branch protection rule, and ruleset.** GitHub's two mechanisms (an older one and a newer
replacement) for stopping people pushing directly to an important branch, and for requiring things
like a review before a change is allowed to land. Why it matters: you'll see these mentioned
wherever a branch needs more than ordinary Write access to touch, changing which branch is the
default one, or renaming a branch that's covered by one. Full detail, including what these cost on
a private repository, is in `10-protecting-your-work.md`.

**Fork.** A separate copy of somebody else's repository, sitting under your own account, used when
you don't have Write access to the original at all. Why it matters: a fork is the alternative to a
branch when you don't have Write access to the repository you want to change. Full detail in
`09-forks-and-contributing.md`.

**Merge conflict.** The moment GitHub can't automatically combine two branches, because the same
part of the same file was changed two different ways on each one, and stops to ask a person to
decide. Why it matters: it can come up either when you update your branch with the latest main, or
when you merge your branch in. Covered in full in `08-merge-conflicts.md`.

## How to do it

GitHub's own framing of why any of this is worth doing at all: "Rather than modifying the default
branch directly, you create a separate branch to develop features or test ideas. This prevents your
experimental or incomplete work from affecting the main codebase that others depend on." And, just
as importantly, GitHub's own wording on why it's a low-stress way to work: "Your branch is a safe
place to make changes. If you make a mistake, you can revert your changes or push additional
changes to fix the mistake. Your changes will not end up on the default branch until you merge
your branch."

### Creating a branch in the browser

GitHub documents two ways to do this. Either one works; use whichever feels more natural.

**Method 1, from the full branches list:**

1. On the repository's main page, look for the branch dropdown. It shows your current branch's
   name, usually near the file list, and clicking it opens a small menu rather than taking you
   anywhere.
2. Click it, then click **View all branches**. You'll know it worked because you land on a page
   listing every branch in the repository, organized under tabs labelled **Yours**, **Active**,
   **Stale**, and **All**. The direct address, if you'd rather go straight there, is
   `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/branches`.
3. Click **New branch**.
4. Under "Branch name," type a name for the branch.
5. Under "Branch source," choose the repository and branch to base your new branch on (usually
   your default branch, see "Branch source" above).
6. Click **Create branch**.

**Method 2, the quick way, straight from the dropdown:**

1. On the repository's main page, click the branch dropdown (this is also available at the top of
   the file editor if you're already looking at a file).
2. In the "Find or create a branch..." text field, type a unique name for your new branch.
3. Click **Create branch**.

Either method you'll know worked because the page reloads showing your new branch's name in the
dropdown where the old one used to be, and the file list underneath now belongs to that branch.

**If nothing happens, or you get an error creating a branch:** this almost always means you don't
have Write access to that repository, only Read. GitHub's own wording is direct on this: "You can
only create a branch in a repository to which you have write access." Check with whoever owns the
repository (`03-members-and-access.md` covers how access gets granted), or, if you're trying to
contribute to a repository someone else owns and were never meant to have Write access to,
`09-forks-and-contributing.md` covers the path that's actually meant for that situation.

**Screenshot placeholder:** the "New branch" form from Method 1, showing the "Branch name" and
"Branch source" fields, so a reader can match what they see on screen to the steps above before
clicking Create.

### Creating a branch through Claude Code

If you already have Claude Code open in your project's folder, this is usually faster than the
browser, and you don't need to remember any of the click paths above. Describe what you want in
plain English:

```
Make me a new branch called fix-homepage-typo, based on main.
```

Claude Code creates the branch and switches you onto it, then tells you what it did. If you'd
rather see the click path happen on screen at least once, so you know what it looks like, use the
browser method above instead. Neither path is more "correct" than the other, they produce the same
branch either way.

### Naming conventions worth having, and renaming one later

GitHub doesn't force any particular naming style on you, but its own guidance is worth following:
"A short, descriptive branch name enables your collaborators to see ongoing work at a glance," and
its own examples are things like `increase-test-timeout` or `add-code-of-conduct`.

**A practical convention worth adopting for yourself, not a GitHub rule:** name the branch after
what it does, in a few words, with hyphens instead of spaces. For a small business, that might look
like `update-menu-prices`, `fix-homepage-typo`, or `new-refund-policy-draft`. Avoid vague names like
`test` or `changes` or your own name on its own, they tell nobody, including future you, what the
branch was actually for once you're looking at a list of ten of them.

**If you name one badly and only realise afterwards, you don't have to start over.** You can rename
a branch. On the repository's main page, click the branch dropdown, then click **View all
branches**. Next to the branch you want to rename, click its own dropdown menu, then click
**Rename branch**. Type the new name, review the note GitHub shows about anyone else's local copy
of that branch, then click **Rename branch** again to confirm. You'll know it worked because the
branch's new name appears in the list where the old one was.

GitHub handles the tidy-up automatically once you do: "any URLs that contain the old branch name are
automatically redirected," branch protection settings move with the new name, and the base branch is
updated on any open pull requests, including ones from forks. GitHub's own wording on who can do
this: "Most branches can be renamed by any user with write permission to the repository," but
"some branches can only be renamed by a repository administrator," specifically the repository's
default branch, and any branch covered by a branch protection rule or a ruleset.

Two things worth knowing before you rename one: if the branch is the source of an open pull
request, renaming it closes that pull request. And if a teammate already has that branch on their
own computer, GitHub won't redirect their next `git pull`, they'll need to update their own copy
manually, so it's worth telling them before you rename a branch they're also using.

### Switching between branches

Switching branches just means changing which one you're currently looking at. It doesn't need any
special access beyond what you already have to view the repository at all, Read is enough.

**In the browser:** click the branch dropdown on the repository's main page (or at the top of the
file editor if you're already inside a file). GitHub organizes the full list under a few tabs to
make it easier to find what you want: **Yours** ("in repositories that you have push access to,"
GitHub's own wording, branches you've personally pushed to, other than the default one), **Active**
(branches with commits in the last three months), **Stale** (branches with no commits in the last
three months), and **All** (the default branch plus everything else). There's also a search field
in the top right if you know part of the name. Click the branch you want, and you'll know it
worked because the page reloads showing that branch's files instead of the one you came from.

**Through Claude Code:** ask it in plain English, something like:

```
Switch me to the branch called update-menu-prices.
```

Claude Code runs the underlying git command for you (`git switch` or `git checkout`, depending on
your setup) and tells you when it's done. You don't need to remember either command yourself.

### Keeping your branch up to date with main

Nothing happens to your branch itself when someone else changes the default branch while you're
working. Your commits, and the state of every file on your branch, stay exactly as you left them,
that's the whole point of the isolation covered above. What changes is the relationship between
your branch and the default branch: your branch is now "out of sync," because main has moved on
since you branched off it.

This matters most at the point you're ready to bring your branch's work back into main. If you've
opened a pull request (covered in the next file) and main has since had other changes merged into
it, GitHub shows you an **Update branch** button on the pull request page, near where the merge
status is shown. You'll know you need it because the page tells you your branch is out of sync
before you even look for the button. Two ways to use it: click **Update branch** for a traditional
merge (folds main's new changes into your branch, keeping a full history of both), or use the
dropdown arrow next to it to choose **Update with rebase** instead (replays your branch's changes
on top of the latest main, for a straight-line history with no separate merge commit). Either way,
if the same lines of the same file were changed on both sides, you'll get a merge conflict to
resolve before you can update; that's covered in `08-merge-conflicts.md`, not here.

**If you haven't opened a pull request yet and just want your branch caught up with the latest
main**, the easiest route for a non-technical member is Claude Code: ask it to bring your branch up
to date, and let it tell you if anything actually conflicts before you touch a thing yourself.

### Deleting a branch once it's landed

Once a branch's work has been folded back into your main copy (covered in `07-pull-requests.md`),
the branch itself has done its job. Deleting it at that point is tidying up, not destroying
anything, the changes it made are already safely part of your main copy.

**The steps:**

1. On the repository's main page, click the branch dropdown, then click **View all branches**.
2. Next to the branch you want to delete, click the delete (trash) icon.
3. If the branch is associated with at least one open pull request, deleting it will close that
   pull request. Read the warning GitHub shows you, then click **Delete**.

You'll know it worked because the branch disappears from the list, and the branch dropdown no
longer offers it.

Two things GitHub won't let you do by accident:

- **You can't delete your repository's current default branch.** Pick a different default branch
  first (see below) if that's genuinely what you're trying to do, which is rare.
- **You can't delete a branch that's tied to an open pull request** until that pull request is
  merged or closed. This is a real safeguard, not red tape, it stops a branch from vanishing while
  someone is still actively reviewing the change on it.

**Why this is safe to do without much second-guessing, if the branch went through a pull
request:** GitHub keeps a way back for a little while. If you delete the head branch of a *closed*
pull request (closed either by merging or by closing it directly), you can restore it: open the
repository, click **Pull requests**, filter to **Closed**, open the pull request that branch
belonged to, and click **Restore branch** near the bottom of the page. This works specifically for
"the head branch of a closed pull request," per GitHub's own wording. GitHub's own documentation
doesn't state how long that restore option stays available, so don't sit on it if you change your
mind.

**The one case that restore option doesn't cover:** a branch you created, worked on, and deleted
without ever opening a pull request from it. There's no documented "undo" for that path. If you're
not sure yet whether you'll want a branch's work again, the safe move is to leave the branch alone
rather than delete it, deleting costs you nothing to defer, and an unused branch just sitting there
does no harm.

### Changing your repository's default branch

Most small-business repositories never need to touch this. It's here so that when someone mentions
"the default branch" or you see it named on a settings screen, you know what it means and, on the
rare occasion you do need to change it, how.

Changing which branch is the default one needs admin access to the repository, and, if your
organization or enterprise has rulesets targeting branches, an organization or enterprise
administrator has to approve the change too (`10-protecting-your-work.md` covers rulesets in full).
Your repository needs more than one branch before this option does anything, there has to be
something to switch to.

**The steps:**

1. On the repository's main page, click **Settings**, near the right-hand end of the row of tabs
   that starts with **Code**. On a narrower screen, look for a **More** dropdown instead, and click
   **Settings** from inside it.
2. Look for a section named **Default branch**. You'll know you're in the right place because it
   shows your current default branch's name with a small switch icon beside it.
3. Click the switch icon.
4. Choose the new branch from the dropdown that appears.
5. Click **Update**.
6. GitHub shows a warning before this takes effect. Read it, then click **I understand, update the
   default branch** to confirm.

**If you don't see a Default branch section at all:** either your repository only has one branch,
in which case there's nothing to switch to yet, or you don't have admin access to that repository,
in which case `03-members-and-access.md` covers checking your own role.

## Strategy: how to actually use this

**A solo operator working alone gets less immediate benefit from a branch**, since there's nobody
else's work to protect and nobody waiting to review anything. It's still worth reaching for one
before anything genuinely risky, a pricing change, a rewrite of a page that's actually driving
traffic, rather than committing straight to your default branch and hoping. For small everyday
edits with nothing riding on them, committing directly is faster, and a branch buys you very
little when there's no one else's work it could break.

**The moment a second person starts touching the same repository regularly, branches stop being
optional.** This is the point where an informal review habit, someone glancing at a change before
it lands, starts paying for itself. It costs a little waiting and a little coordination, and in
return a second pair of eyes catches mistakes before they become everyone's problem, without
needing anyone's formal permission to skip it in a genuine hurry.

**A team of three or four is usually still better served by that informal habit than by an
enforced GitHub setting.** A ruleset that blocks a change from landing until someone approves it
(covered in `10-protecting-your-work.md`) needs a paid plan on a private repository, and at this
size the enforced rule and the habit tend to produce the same outcome nearly every time. The
enforced version earns its cost once mistakes have actually started costing money or reputation,
not on a hunch that they probably should.

**The decision rule worth keeping:** grant the narrowest access and use the smallest amount of
process that gets this week's job done safely. That means: work on a branch whenever more than one
person touches the repository, or whenever a mistake would be visible to a customer. Skip the
branch for a same-day fix you're doing alone with nothing riding on it. Add an enforced review rule
only once an informal one has genuinely failed you, not before.

**What good looks like months later:** a list of branches whose names still mean something on
their own, not ten branches called `test` or somebody's first name, and a list where the **Stale**
tab is mostly empty because branches get merged or deleted once their work has landed, rather than
piling up forever. If your branch list has become something nobody can read at a glance, that's the
signal to tidy it up, not to add more process on top of it.

**What would change my mind about any of the above:** if an informal review consistently turns into
a rubber stamp nobody actually reads, that's over-investment, drop back to working straight on
branches without ceremony. If a mistake has already landed in something a customer saw because
nobody happened to look at it first, that's the signal to add enforced review, not a one-off bad
day to shrug off.

## A worked example

The café owner's ordering site, her nephew, and her staff member are the same team of three
described in this kit's strategy pack. The nephew wants to add a "gluten-free" filter to the
online ordering menu, without touching the version customers are placing orders through right now
while he builds it. He has Write access to the site's repository, since he's the one who built it
and keeps it running.

He opens the repository's main page, clicks the branch dropdown, types `add-gluten-free-filter`
into the "Find or create a branch" field, and clicks **Create branch**. He could just as easily
have asked Claude Code, already open in the project's folder: "Make me a new branch called
add-gluten-free-filter, based on main." Either way, he's now working on his own copy, and the
version customers are ordering from hasn't changed at all.

Over the next few days he commits his changes to that branch, while the staff member keeps editing
opening hours directly on main, since her changes and his don't touch the same files and neither of
them needs to wait on the other. Partway through, her small fix merges into main. His branch is now
"out of sync," since main has moved since he branched off it. He isn't ready to open a pull request
yet, so he just asks Claude Code to bring his branch up to date with main, and it tells him nothing
actually conflicts before he touches a thing.

When the filter works the way he wants, he opens a pull request (covered in the next file). The
café owner glances over it, since a mistake here is something a customer would see, and it merges
into main. Back on the repository's main page, he clicks the branch dropdown, clicks **View all
branches**, finds `add-gluten-free-filter` in the list, and clicks the trash icon next to it. Its
work is already safely part of main, so deleting it is tidying up, not a risk.

## If it goes wrong

**I created a branch and now I can't find it again.** Open the branch dropdown and click **View
all branches**, then check the **Yours** tab, that filters the full list down to branches you've
personally pushed to. If you know part of the name, the search field in the top right narrows it
further.

**I tried to create a branch and nothing happened, or I got an error.** This usually means you
don't have Write access to that repository, only Read. Check with whoever owns the repository, see
this kit's members and access file for how that gets granted. If you don't have Write access and
you're trying to contribute to someone else's project rather than your own team's, see the forks
file instead, that's a different and correct path for that situation.

**I deleted a branch and I'm not sure I meant to.** If that branch was the head branch of a pull
request you'd already closed or merged, open that pull request and click **Restore branch** near
the bottom. If the branch never went through a pull request, there's no documented way to bring it
back through GitHub's interface, treat that as the reason to lean toward leaving branches alone
rather than deleting when you're not fully sure.

**I renamed a branch and its pull request disappeared.** It didn't disappear, GitHub closes the
pull request automatically the moment its source branch is renamed. Open your **Pull requests**
tab and filter to **Closed** to find it, then reopen it if you still want it, or open a fresh one
from the branch under its new name.

**I tried to delete a branch and GitHub won't let me.** Two situations cause this on purpose, not
by accident. If it's your repository's current default branch, you have to make a different branch
the default one first before you can delete this one. If it's tied to an open pull request, merge
or close that pull request first, GitHub blocks the delete specifically so a branch can't vanish
while someone is still reviewing the change on it.

## FAQ

**Do I need to ask permission before creating a branch?** No, beyond already having Write access to
the repository. Creating a branch doesn't touch anyone else's work, so there's nothing to ask
permission for. The moment that does involve other people is bringing your branch's changes back
into main, and that's the pull request step, covered in the next file.

**Do I need admin access for an ordinary branch?** No. Write access is enough to create, rename, or
delete a branch you made. Admin access only comes into it for changing which branch is the default
one, or renaming a branch that's covered by a branch protection rule or a ruleset.

**What's the difference between a branch and a fork?** A branch is a copy inside the same
repository, and everyone with access to that repository can see it. A fork is a whole separate copy
of the repository under your own account, typically used when you don't have Write access to the
original at all. This kit's forks file covers that path in full; use a branch, not a fork, whenever
you already have Write access to the repository you're working in.

**If I branch off a branch instead of my default branch, is that a problem?** No, "branch source"
can be any existing branch, and it's a legitimate thing to do, for example when you're deliberately
building on top of a teammate's unfinished work. For most everyday changes at this kit's scale,
branching off your default branch is what you want unless someone specifically asks you to build on
theirs instead.

**If I don't touch my branch for months, does GitHub delete it automatically?** No. GitHub's own
branch listing does separate **Active** branches from **Stale** ones (no commits in the last three
months) purely for your own visibility, so old branches are easier to spot and clean up. Being
labelled stale doesn't delete anything or change any of its settings on its own.

**Can two people work on the same branch at the same time?** Yes, technically, but it's not usually
the right setup for this kit's audience. It's simpler, and much easier to keep track of, to have
each person work on their own branch and bring the two together later through a pull request
(covered next), rather than both editing the same branch at once.

**I see a branch called `master` in an older project instead of `main`. Is that a problem?** No,
that's just an older repository that predates GitHub's current default naming. It behaves exactly
like any other default branch, this kit's guidance about the default branch applies to it the same
way regardless of what it's named.

## Quick reference

- **Create a branch (browser, full list):** branch dropdown, **View all branches**, **New branch**,
  fill in Branch name and Branch source, **Create branch**
- **Create a branch (browser, quick way):** branch dropdown, type a name into "Find or create a
  branch...", **Create branch**
- **Create a branch (Claude Code):** "Make me a new branch called ..., based on main."
- **Switch branches:** branch dropdown, click the branch you want
- **Switch branches (Claude Code):** "Switch me to the branch called ..."
- **Update your branch with the latest main:** ask Claude Code, or use **Update branch** /
  **Update with rebase** on an open pull request
- **Rename a branch:** branch dropdown, **View all branches**, that branch's own dropdown menu,
  **Rename branch**
- **Delete a branch:** branch dropdown, **View all branches**, trash icon next to the branch
- **Restore a deleted branch:** only works for the head branch of a closed pull request, open that
  pull request, **Restore branch**
- **Change the default branch (needs admin access):** repository **Settings**, **Default branch**
  section, switch icon, choose the new branch, **Update**, confirm
- **Branches list, direct address:** `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/branches`

## Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/viewing-branches-in-your-repository
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
- https://docs.github.com/en/get-started/using-github/github-flow
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request
