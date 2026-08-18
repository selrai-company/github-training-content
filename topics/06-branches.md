# Branches, and changing things without breaking them

A branch is how you change things on GitHub without any risk of breaking what everyone else is
already relying on. This file covers what a branch actually is, why you'd use one instead of
editing the main copy directly, what the default branch is, both of GitHub's documented ways to
create a branch in your browser, naming conventions worth adopting, how to switch between
branches, deleting a branch once it's done its job, what happens if someone else changes the main
copy while you're still working, and the shortcut of asking Claude Code to do the git work for
you.

Most of what's below happens in your browser, so you can see every field on the actual screen.
Wherever asking Claude Code to do it instead is genuinely faster, this file says so, and shows
exactly what to type.

## What a branch actually is

Picture the main version of your project as the master copy of an important document, sitting
somewhere everyone in the business relies on. If you want to try rewording a section, you don't
scribble directly on the master copy. You photocopy it, mark up the photocopy, and leave the
original completely untouched while you work. If your changes turn out well, you swap them into
the master copy later. If they don't, you bin the photocopy and the master was never at risk.

A branch is that photocopy. It starts as an exact copy of whichever branch you made it from
(usually your default branch, covered below), and every change you make stays on that copy.
Nobody else's work changes because of what you're doing on your branch, and they can keep working
from the main copy the whole time you're experimenting on yours.

GitHub's own description of what a branch is for: "Branches let you develop features, fix bugs, or
safely experiment with new ideas in a contained area of your repository."

**Screenshot placeholder:** a repository's branch dropdown open, showing the current branch name
at the top and a short list of other branches underneath it, so a reader can see what a branch
actually looks like from the outside before creating their own.

## Why you work on a branch instead of the main copy

The point of a branch is that mistakes on it can't reach anyone else. GitHub's own wording:
"Rather than modifying the default branch directly, you create a separate branch to develop
features or test ideas. This prevents your experimental or incomplete work from affecting the
main codebase that others depend on."

And, just as importantly, mistakes on a branch are cheap to fix. GitHub's own framing of this:
"Your branch is a safe place to make changes. If you make a mistake, you can revert your changes
or push additional changes to fix the mistake. Your changes will not end up on the default branch
until you merge your branch." Merging (folding your branch's changes into the main copy on
purpose, usually through a pull request) is covered in this kit's pull requests file, not here.
Until you take that deliberate step, whatever you do on your branch stays on your branch.

**In practice, for a small business:** if you want to update a page on your website, try a new
version of a document, or test a change to a template, do it on a branch. If it works, you bring
it across later. If it doesn't, you've lost nothing and nobody else ever saw the mess.

## The default branch

Every repository has one branch that GitHub treats as the "main" one. GitHub's own definition:
"The default branch is the base branch for pull requests and code commits." It's also, per
GitHub's own wording, "the branch that GitHub displays when anyone visits your repository," and
"the initial branch that Git checks out locally when someone clones the repository." In new
repositories, GitHub names this branch `main` by default.

Two things worth knowing about it:

- When you create a new branch, you're asked to pick a **branch source**, meaning which branch to
  copy from. Unless you have a specific reason to branch off something else, that's your default
  branch.
- Changing which branch is the default one is possible, but it needs admin access to the
  repository, and, if your organization or enterprise has rulesets targeting branches, an
  organization or enterprise administrator has to approve the change too. The click path, if you
  ever need it: repository **Settings** → find **Default branch** → click the switch icon next to
  the current branch name → choose the new branch from the dropdown → click **Update** → confirm
  by clicking **I understand, update the default branch**. Your repository needs more than one
  branch before this option does anything, there has to be something to switch to.

Most small-business repositories never need to touch this. It's here so that when someone
mentions "the default branch" or you see it named on a settings screen, you know what it means and
why it matters.

## Creating a branch in the browser

GitHub documents two ways to do this. Either one works; use whichever feels more natural.

**Method 1, from the full branches list:**

1. On the repository's main page, find the branch dropdown (it shows your current branch name,
   usually near the file list).
2. Click it, then click **View all branches**.
3. Click **New branch**.
4. Under "Branch name," type a name for the branch.
5. Under "Branch source," choose the repository and branch to base your new branch on (usually
   your default branch, see above).
6. Click **Create branch**.

**Method 2, the quick way, straight from the dropdown:**

1. On the repository's main page, click the branch dropdown (also available at the top of the
   file editor if you're already looking at a file).
2. In the "Find or create a branch..." text field, type a unique name for your new branch.
3. Click **Create branch**.

Either method needs at least Write access to the repository you're branching in. If you're a
collaborator or on the team already, you have this. If you're only looking at a repository someone
else owns and you don't have that access, see this kit's members and access file for how access
gets granted, or the forks file for a different path entirely.

**Screenshot placeholder:** the "New branch" form from Method 1, showing the "Branch name" and
"Branch source" fields, so a reader can match what they see to the steps above before clicking
Create.

## Naming conventions worth having

GitHub doesn't force any particular naming style on you, but its own guidance is worth following:
"A short, descriptive branch name enables your collaborators to see ongoing work at a glance," and
its own examples are things like `increase-test-timeout` or `add-code-of-conduct`.

**A practical convention worth adopting for yourself, not a GitHub rule:** name the branch after
what it does, in a few words, with hyphens instead of spaces. For a small business, that might
look like `update-menu-prices`, `fix-homepage-typo`, or `new-refund-policy-draft`. Avoid vague
names like `test` or `changes` or your own name on its own, they tell nobody (including future
you) what the branch was actually for once you're looking at a list of ten of them.

**If you name one badly and only realise afterwards, you don't have to start over.** You can
rename a branch, and GitHub handles the tidy-up automatically: "any URLs that contain the old
branch name are automatically redirected," branch protection settings move with the new name, and
the base branch is updated on any open pull requests, including ones from forks. Most branches can
be renamed by anyone with Write access; renaming your repository's default branch, or a branch
covered by a protection rule or ruleset, needs admin access instead. Two things worth knowing
before you rename one: if the branch is the source of an open pull request, renaming it closes that
pull request, and if a teammate already has that branch on their own computer, GitHub won't
redirect their next `git pull`, they'll need to update their own copy manually, so it's worth
telling them before you rename a branch they're also using.

## Switching between branches

Switching branches just means changing which one you're currently looking at. It doesn't need any
special access, viewing a branch only needs the same access you already have to view the
repository at all.

**In the browser:** click the branch dropdown on the repository's main page (or at the top of the
file editor if you're inside a file). GitHub organizes the full list under a few tabs to make it
easier to find what you want: **Yours** (branches you've personally pushed to, other than the
default one), **Active** (branches with commits in the last three months), **Stale** (branches
with no commits in the last three months), and **All** (the default branch plus everything else).
There's also a search field in the top right if you know part of the name. Click the branch you
want, and the page reloads showing that branch's files instead.

**Through Claude Code:** ask it in plain English, something like:

```
Switch me to the branch called update-menu-prices.
```

Claude Code runs the underlying git command for you (`git switch` or `git checkout`, depending on
your setup) and tells you when it's done. You don't need to remember either command yourself.

## Deleting a branch once it's landed

Once a branch's work has been folded back into your main copy (covered in the pull requests file),
the branch itself has done its job. Deleting it at that point is tidying up, not destroying
anything, the changes it made are already safely part of your main copy.

**The steps:**

1. On the repository's main page, click the branch dropdown, then click **View all branches**.
2. Next to the branch you want to delete, click the delete (trash) icon.
3. If the branch is associated with at least one open pull request, deleting it will close that
   pull request. Read the warning GitHub shows you, then click **Delete**.

Two things GitHub won't let you do by accident:

- **You can't delete your repository's current default branch.** Pick a different default branch
  first (see above) if that's genuinely what you're trying to do, which is rare.
- **You can't delete a branch that's tied to an open pull request** until that pull request is
  merged or closed. This is a real safeguard, not red tape, it stops a branch from vanishing while
  someone is still actively reviewing the change on it.

**Why this is safe to do without much second-guessing, if the branch went through a pull
request:** GitHub keeps a way back for a little while. If you delete the head branch of a *closed*
pull request (closed either by merging or by closing it directly), you can restore it: open the
repository, click **Pull requests**, filter to **Closed**, open the pull request that branch
belonged to, and click **Restore branch** near the bottom of the page. This works specifically for
"the head branch of a closed pull request," per GitHub's own wording, GitHub's own documentation
doesn't state how long that restore option stays available, so don't sit on it if you change your
mind.

**The one case that restore option doesn't cover:** a branch you created, worked on, and deleted
without ever opening a pull request from it. There's no documented "undo" button for that path.
If you're not sure yet whether you'll want a branch's work again, the safe move is to leave the
branch alone rather than delete it, deleting costs you nothing to defer, and an unused branch just
sitting there does no harm.

## What happens to your branch when someone else changes main underneath you

Nothing happens to your branch itself. Your commits, and the state of every file on your branch,
stay exactly as you left them, that's the whole point of the isolation covered above. What changes
is the relationship between your branch and the main copy: your branch is now "behind," because
main has moved on since you branched off it.

This matters at the point you're ready to bring your branch's work back into main. If you've
opened a pull request (covered in the next file) and main has since had other changes merged into
it, GitHub calls this being "out of sync," and it shows you an **Update branch** button on the
pull request page. Two ways to use it: click **Update branch** for a traditional merge (folds
main's new changes into your branch, keeping full history of both), or use the dropdown next to it
to **Update with rebase** instead (replays your branch's changes on top of the latest main, for a
straight-line history with no merge commit). Either way, if the same lines of the same file were
changed on both sides, you'll get a merge conflict to resolve before you can update; that's covered
in this kit's merge conflicts file, not here.

**If you haven't opened a pull request yet and just want your branch caught up with the latest
main**, the easiest route for a non-technical member is Claude Code: ask it to bring your branch up
to date, and let it tell you if anything actually conflicts before you touch a thing yourself.

## Doing this through Claude Code instead

Every member of this kit has Claude Code on the Max plan, which means it already has git available
and can run these steps for you. You don't need to know a single git command. Just describe what
you want in plain English, from inside your project folder:

```
Make me a new branch called fix-homepage-typo, based on main.
```

Claude Code creates the branch and switches you onto it, then tells you what it did. If you'd
rather see the click path happen on screen (worth doing at least once, so you know what it looks
like), use the browser method above instead. Neither path is more "correct" than the other, they
produce the same branch either way. Use the browser the first few times so you can see it, and
Claude Code once you're comfortable and just want it done.

---

## If it goes wrong

**I created a branch and now I can't find it again.** Open the branch dropdown and click **View
all branches**, then check the **Yours** tab, that filters the full list down to branches you've
personally pushed to. If you know part of the name, the search field in the top right narrows it
further.

**I tried to create a branch and nothing happened, or I got an error.** This usually means you
don't have Write access to that repository, only Read. Check with whoever owns the repository, see
this kit's members and access file for how that gets granted. If you don't have write access and
you're trying to contribute to someone else's project rather than your own team's, see the forks
file instead, that's a different and correct path for that situation.

**I deleted a branch and I'm not sure I meant to.** If that branch was the head branch of a pull
request you'd already closed or merged, open that pull request and click **Restore branch** near
the bottom. If the branch never went through a pull request, there's no documented way to bring it
back through GitHub's interface, treat that as the reason to lean toward leaving branches alone
rather than deleting when you're not fully sure.

## Questions people ask here

**Do I need to ask permission before creating a branch?** No, beyond already having Write access to
the repository. Creating a branch doesn't touch anyone else's work, so there's nothing to ask
permission for. The moment that does involve other people is bringing your branch's changes back
into main, and that's the pull request step, covered in the next file.

**What's the difference between a branch and a fork?** A branch is a copy inside the same
repository, and everyone with access to that repository can see it. A fork is a whole separate copy
of the repository under your own account, typically used when you don't have write access to the
original at all. This kit's forks file covers that path in full; use a branch, not a fork, whenever
you already have write access to the repository you're working in.

**If I don't touch my branch for months, does GitHub delete it automatically?** No. GitHub's own
branch listing does separate "Active" branches from "Stale" ones (no commits in the last three
months) purely for your own visibility, so old branches are easier to spot and clean up. Being
labelled stale doesn't delete anything or change any of its settings on its own.

**Can two people work on the same branch at the same time?** Yes, technically, but it's not
usually the right setup for this kit's audience. It's simpler, and much easier to keep track of,
to have each person work on their own branch and bring the two together later through a pull
request (covered next), rather than both editing the same branch at once.

**I see a branch called `master` in an older project instead of `main`. Is that a problem?**
No, that's just an older repository that predates GitHub's current default naming. It behaves
exactly like any other default branch, this kit's guidance about the default branch above applies
to it the same way regardless of what it's named.

---

## Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/viewing-branches-in-your-repository
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
- https://docs.github.com/en/get-started/using-github/github-flow
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request
