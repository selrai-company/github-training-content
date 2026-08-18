# Forks, and practising without breaking anything

A fork is your own personal copy of somebody else's repository, sitting under your own account,
with your name on it as the owner. This file covers what a fork actually is and how it differs
from a branch, why you'd fork a repository instead of asking to edit it directly, what access
forking needs and what access you get on the copy it creates, opening a pull request from your
fork back to the original, the honest limit on that (proposing a change and merging it are two
different levels of access, and that's not a flaw), forking a private repository (which behaves
differently and depends on a setting its owner controls), keeping your fork up to date with the
original, and deleting a fork once you're done with it.

If you haven't read `07-pull-requests.md` yet, read that first. Everything a fork is for leads
toward opening a pull request, so this file assumes you already know what one is and how reviewing
and merging work.

Most of what's below happens in your browser, the same as branches and pull requests. Wherever
Claude Code is genuinely faster or safer instead, this file says so.

## What a fork actually is

GitHub's own definition: "Forks are repositories that start as copies of another repository,
called the upstream repository. A fork has its own settings and permissions but stays connected
to the upstream repository." The repository you forked from keeps a name in GitHub's own
vocabulary too: it's your fork's **upstream**.

The difference from a branch, in GitHub's own words: "A branch is part of one repository. A fork
is a separate repository with its own settings and collaboration space." A branch lives inside the
repository you're already working in. A fork is a whole new repository, under your own account,
that happens to remember where it came from.

That separateness is real, not cosmetic. Per GitHub's own documentation, each fork independently
has its own branches, its own members and discussions, its own issues and pull requests, its own
Actions and projects, and its own tags, labels, and wikis. Nothing you do inside your fork touches
any of that on the upstream repository, and nothing that happens on the upstream repository
changes what's sitting in your fork, until you deliberately bring the two together (covered below,
in both directions: pulling their changes into your fork, and proposing your changes back to
them).

| | A branch | A fork |
|---|---|---|
| Lives inside | The same repository | A separate repository, under your own account |
| Who can create one | Anyone with Write access to that repository | Anyone with Read access to the repository, if its owner allows forking |
| What you can change | Only what you already have Write access to | Whatever you own, since the fork is now yours |
| How it comes home | A pull request, reviewed and merged by someone with access to that repository | A pull request, reviewed and merged by someone with access to the *upstream* repository, not by you |

**Screenshot placeholder:** a repository's page with the **Fork** button visible in the top-right
corner, showing the fork count next to it, so a reader recognises the button before clicking it.

## Why you fork instead of editing directly

GitHub documents two different ways people collaborate on a repository, and knowing both names
makes the rest of this file click into place.

**The shared repository model**, covered in `06-branches.md` and `07-pull-requests.md`: everyone
working on the repository has Write access to it directly, and works on branches inside that same
repository.

**The fork and pull model**, GitHub's own description: "In the fork and pull model, anyone can
fork an existing ('upstream') repository if they have read access and the owner of the upstream
repository allows it." The part that matters most: "You do not need permission from the upstream
repository to push to a fork you created." Once it's your fork, it's your repository. You don't
need anyone's sign-off to make changes on it, because you're not touching theirs at all.

GitHub's own framing of why this model exists: it's "popular with open-source projects because it
reduces friction for new contributors and lets people work independently without upfront
coordination." That's the honest reason to fork rather than ask for access: you don't have to wait
for anyone to grant you anything before you can start. You fork, you make your change on your own
copy, and only when it's ready do you propose it back, through a pull request, as covered later in
this file.

**In practice, for a small business:** if you want to change something in a repository you don't
have Write access to, whether that's a vendor's public template, an open-source tool your business
relies on, or another team's project inside your own organization that hasn't given you access,
forking is how you start working on it without asking anyone for anything first. The moment you're
ready to offer that change back, that's when the conversation with them begins, as a pull request,
not before.

**Practising is exactly this, at a smaller scale.** This kit's own practice repository, at
`https://github.com/selrai-company/github-training-content`, says it plainly in its own README:
"Fork it, break it, nothing here matters." Forking it gives you a copy that's entirely yours,
where nothing you do can affect the original, and nothing the original changes can silently break
whatever you're in the middle of trying. That's the safety net in both directions, and it's the
same safety net a fork gives you on real work: your experiment can't reach their repository, and
their repository can't reach into your experiment either, until you choose to connect the two
through a pull request.

## What access you need to fork, and what access you get on your own copy

**To fork a public repository, GitHub doesn't ask much of you.** Its own words: "You can fork any
public repository: To your personal account [or] To an organization where you have permission to
create repositories." No Write access to the original repository is needed, and per the fork and
pull model quoted above, Read access (which is what you already have on any public repository,
simply by being able to view it) is enough.

**What you get on the fork itself is not the same everywhere.** For a fork of a public repository,
GitHub's own wording is direct: "Fork owners control access to their forks." It's yours. You decide
who else gets to see or change it, the same as any repository you create.

**A fork of a private repository is different, and worth knowing before you rely on it.** GitHub's
own wording: "Private forks inherit the permissions structure of the upstream repository." Your
fork isn't fully independent in the way a public fork is. This has a real consequence covered in
`03-members-and-access.md`'s offboarding section, worth repeating here because it's specifically
about forks: "If you remove a person's access to a private repository, any of their forks of that
private repository are deleted." If you fork a private repository and later lose your access to
the original, your fork doesn't survive that on its own, it goes with it. (There's one documented
exception, also from that section: a private repository forked into a *different* organization can
survive under that organization's own control, independent of what happens to your access in the
original. That's an edge case most small-business readers won't hit, but it's real.)

**Visibility follows the same rule either way.** GitHub's own wording: "A fork's visibility is tied
to the upstream repository's repository network. Public repository forks are public, and private
repository forks are private." You can't fork a public repository into a private copy, or a private
repository into a public one. Whatever the original is, your fork matches it.

## Forking, step by step

**In the browser:**

1. On the repository's main page, click the **Fork** button in the top-right corner.
2. Choose an **Owner** for your new fork from the dropdown (your personal account, or an
   organization where you have permission to create repositories).
3. Optionally change the repository name and add a description.
4. Optionally tick **Copy the DEFAULT branch only**. Leave it unticked and every branch on the
   original comes with you; tick it and you get just the default branch (usually `main`), which is
   the lighter option if you only care about the current state of the project.
5. Click **Create fork**.

**Screenshot placeholder:** the fork creation screen, showing the Owner dropdown, the repository
name field, and the "Copy the DEFAULT branch only" checkbox, so a reader can match every field to
the steps above before clicking Create fork.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in** (the
same one-time setup mentioned in `04-repositories-and-visibility.md`, `05-daily-workflow.md`, and
`07-pull-requests.md`): ask it in plain English, or let it run something like this on your behalf:

```
gh repo fork OWNER/REPOSITORY --clone=true
```

The GitHub CLI's own flags: `--clone=true` also copies the fork onto your machine in the same step,
`--org "your-org-name"` forks it into an organization instead of your personal account, and
`--remote=true` (the default) sets up the connection back to the original so a later sync (covered
below) knows where to look. If `gh` isn't installed and signed in yet, use the browser path above
instead.

## Opening a pull request from a fork back to the original

Once you've made your change on your fork, bringing it back to the original repository works the
same way as the pull requests covered in `07-pull-requests.md`, with one extra step to bridge the
two repositories.

**Who can do this:** the same rule `07-pull-requests.md` already states, GitHub's own words: "you
must have write access to the head or the source branch." Here, the head branch is on your fork,
which you own, so you already have that. You do not need write access to the original repository
to open the pull request, only to propose it, which is exactly the point of forking in the first
place.

**The click path:**

1. On the *original* (upstream) repository's page, above the file list, click **Compare & pull
   request** if you see the yellow banner, or click the **Pull requests** tab and start a new one.
2. Click **compare across forks**. This is the step that's different from a same-repository pull
   request, it's what reveals the extra dropdowns needed to point at your fork instead of a branch
   in this same repository.
3. Use the **base repository** and **base** branch dropdowns to choose the original repository and
   the branch you want your change merged into (usually its default branch).
4. Use the **head repository** dropdown to choose your fork, and the **compare** branch dropdown to
   choose the branch on your fork that holds your change.
5. Type a title and description, the same guidance from `07-pull-requests.md` applies here.
6. Decide on **Allow edits from maintainers**, fully covered in `07-pull-requests.md`, it's this
   exact checkbox, it's specific to pull requests from a fork, and it's worth a genuine decision
   rather than a reflex.
7. Click **Create Pull Request**, or use the dropdown next to it for **Create Draft Pull Request**.

**Screenshot placeholder:** the pull request creation screen with **compare across forks** clicked,
showing the base repository/branch dropdowns on the left and the head repository/branch dropdowns
on the right, so a reader can see the exact layout before choosing theirs.

Everything after this point, the tabs on the pull request's page, reviewing, the three merge
methods, draft pull requests, closing without merging, is identical to a pull request from a branch
in the same repository. `07-pull-requests.md` covers all of it in full; nothing about it changes
just because the pull request started on a fork, except who is allowed to actually merge it, which
is the next section.

## The honest boundary: proposing is not merging

This is the part worth being direct about rather than glossing over.

GitHub's own wording, from its documentation on merge methods: "To merge pull requests, you must
have write permissions in the repository." That's write permission on the *original* repository,
not your fork. Having write access to your own fork, which you always have because you own it, is
what lets you open the pull request. It is not what lets you click the merge button on it.

**This is the normal shape of real collaboration, not a limitation of your account.** If forking
required the same access as merging, there would be no point to forking at all, you could just ask
for Write access and work on a branch instead, covered in `06-branches.md`. The entire value of the
fork and pull model is that proposing a change and approving it are two separate roles, held by two
different levels of access, so a repository's owner never has to hand out push access just to let
someone suggest an improvement. You propose. Whoever holds Write access (or higher) on the original
repository decides whether it merges. That's not you being locked out, that's the repository
owner's actual project staying under their actual control, the same way you'd want it to work if
someone else forked one of your own repositories.

**In practice, for a small business:** if you fork someone else's repository, open a pull request,
and the merge button doesn't do anything for you, that's expected, not an error. You've done your
part. What happens next is up to whoever maintains the repository you forked from: they review it
(the process `07-pull-requests.md` covers), and if they're satisfied, they're the ones who click
merge, because Write access on that repository is theirs, not yours. If you'd rather not wait on
that, and you have the standing to make the change yourself, that's the signal it should have been
a branch in a repository you already have Write access to, not a fork.

## Forking a private repository

Everything above is written with a public repository in mind, since that's the more common case.
Private repositories behave differently, and depend on a setting the repository's own owner
controls.

**What GitHub confirms plainly:** its own wording, "You cannot fork a private repository to an
organization using GitHub Free." And: "If you have access to a private repository and the owner
permits forking, you can fork the repository" to your personal account, or to a GitHub Team
organization where you have repository creation permissions. Two separate conditions have to be
true at once: you need access to the private repository in the first place, and its owner has to
have allowed forking.

**For a private repository owned by an organization, GitHub documents exactly what "the owner
permits forking" means, and it's a two-layer setting:**

**Layer one, the organization-wide switch.** GitHub's own wording for what it does: "Allow or
prevent the forking of any private repositories owned by your organization." This applies only to
private repositories, it has no effect on public ones. And its own stated default: "New
organizations are configured to disallow the forking of private repositories." Unless an
organization owner has turned this on, no private repository in that organization can be forked at
all, no matter what any individual repository's own setting says.

The click path to check or change it: profile picture (top right) → **Organizations** → the
organization → **Settings** → **Access** section of the sidebar → **Member privileges** →
**Repository forking** → tick **Allow forking of private repositories** → **Save**.

**Layer two, the specific repository's own switch.** GitHub's own wording: this setting lets you
"allow or prevent the forking of a specific private repository" owned by an organization. The click
path: the repository's page → **Settings** → **Features** section → tick **Allow forking**. And its
own stated dependency, worth reading twice: "An organization owner must allow forks of private
repositories on the organization level before you can allow or disallow forks for a specific
repository." Layer one has to be on before layer two does anything at all. If you tick **Allow
forking** on a repository and nothing changes, check the organization-level setting first, this is
the most likely reason.

**What this kit could not confirm, and what to check on your own screen instead:** GitHub's
documentation states the two-layer setting above specifically for repositories owned by an
*organization*. It does not, in what this kit could verify, spell out a separate forking toggle for
a private repository owned by an individual personal account rather than an organization. If you're
trying to fork (or allow forking of) a private repository that sits under someone's personal
account rather than an organization, the safest approach is to have the repository's owner check
its **Settings → Features** section on their own screen for an **Allow forking** option, the same
place the organization-owned version lives, and confirm from there rather than assuming either way.

**Visibility stays private either way.** As covered above, a fork of a private repository is
itself private, per GitHub's own wording quoted earlier: "private repository forks are private."
Forking a private repository never makes it, or your copy of it, visible to anyone who couldn't
already see the original.

## Keeping a fork up to date

Your fork is frozen at whatever state it was in the moment you created it, plus anything you've
changed on it since. It does not automatically follow along as the original repository keeps
moving. Bringing your fork up to date with those changes is called **syncing**.

**In the browser:**

1. On your fork's main page, above the file list, click the **Sync fork** dropdown.
2. Review the commits it shows you from the upstream repository.
3. Click **Update branch**.

**Screenshot placeholder:** the **Sync fork** dropdown open on a fork's main page, showing the
**Update branch** button and a short summary of how many commits it's about to bring in, so a
reader recognises it the first time they see it.

**If the upstream's changes conflict with your own,** GitHub's own wording: "If the changes from
the upstream repository cause conflicts, GitHub will prompt you to create a pull request to resolve
the conflicts." You'll be walked into the same kind of conflict resolution `08-merge-conflicts.md`
covers, rather than the sync silently failing or silently overwriting anything of yours.

**Through Claude Code, and this is genuinely the easier path for this specific task:** syncing on
the command line involves a short sequence of git commands (fetching the upstream repository,
switching to your branch, merging the two), none of which show you much worth looking at on screen
while they run. Rather than learning any of them, ask Claude Code directly, from inside your
project folder:

```
Bring my fork up to date with the original repository.
```

Claude Code runs the underlying steps for you and tells you if anything genuinely conflicts before
you need to look at a single line yourself. If you'd rather use the GitHub CLI directly instead of
plain English, `gh repo sync owner/your-fork -b branch-name` does the same job; add `--force` only
if you're deliberately choosing to overwrite your fork's branch with the upstream's version rather
than merge the two, GitHub's own documentation is clear that this is what `--force` is for when a
sync would otherwise conflict.

**One thing worth knowing if you ever do use the command line yourself:** GitHub's own note on this
is easy to miss, "Syncing your fork only updates your local copy of the repository. To update your
fork on GitHub.com, you must push your changes." A sync you run through git commands on your own
machine doesn't reach GitHub on its own, you (or Claude Code, on your behalf) still need to push
afterward. The browser's **Sync fork** button and the `gh repo sync` command both handle this for
you in one step; the plain git command-line path is the one place this catches people out.

## Deleting a fork

A fork is a repository, so deleting one uses exactly the steps in `04-repositories-and-visibility.md`'s
deletion section: the repository's **Settings** page, its **Danger Zone**, and typing the
repository's name to confirm. Read that section before deleting anything you're not fully sure
about, it covers the general safety net (some deleted repositories can be restored within 90 days,
though GitHub doesn't promise that for every case) in full.

Two things worth knowing that are specific to forks rather than repositories in general:

**Deleting your fork never touches the original repository.** Per GitHub's own wording quoted
earlier in this file, fork owners control their own fork. Deleting it is entirely your decision and
affects nothing upstream.

**Your commits don't necessarily vanish the instant your fork does.** GitHub's own wording: "If you
delete a fork, code contributions from that fork can remain accessible to the repository network."
If anything you committed on your fork was ever pulled into another repository in that same
network, a pull request that got merged, for instance, deleting your fork doesn't erase that
history. Treat anything you've ever pushed to a fork the same way this kit treats anything ever
made public: assume it can outlive the fork itself, rather than counting on deletion as a clean
undo.

**What this kit could not confirm:** whether deleting a fork automatically closes any pull requests
you'd opened from it that are still open. GitHub's own documentation on what happens to forks when
a repository is deleted or changes visibility doesn't state this either way for the fork side (only
for what happens when the *upstream* is deleted). If you have an open pull request from a fork
you're about to delete, close or merge that pull request first, on its own page, rather than
assuming deleting the fork will tidy it up for you.

---

## If it goes wrong

**I clicked Fork and got an error, or nothing happened.** If the repository is public, this
usually means you're trying to fork it into an organization where you don't have permission to
create repositories, try your personal account instead. If the repository is private, you either
don't have access to it at all, or its owner hasn't allowed forking, see the private repository
section above for the two-layer setting that controls this on an organization-owned repository.

**I don't see "compare across forks" when I try to open a pull request.** This usually means you're
looking at the pull request screen from inside your own fork rather than the original repository.
Navigate to the *original* repository's **Pull requests** tab and start a new pull request from
there instead.

**I forked a repository and now I can't find the connection back to the original.** Your fork's
main page shows a line just under the repository name reading something like "forked from
[owner/repository]," that's a real link to the upstream. If you're working through Claude Code
instead and it's lost track of which repository is upstream, ask it directly: "Which repository
did I fork this from?"

**I tried to sync my fork and it says there's a conflict.** That's expected when the same lines
have changed on both sides since you forked. Follow the prompt GitHub gives you to open a pull
request and resolve it, the process is the same one `08-merge-conflicts.md` walks through in full.

## Questions people ask here

**Can I fork a repository I already have Write access to?** Yes, nothing stops you, but there's
usually no reason to. If you already have Write access, a branch (`06-branches.md`) does the same
job with less overhead, since you don't need a separate repository just to make a change you're
already allowed to make directly.

**If I fork a repository, do I see updates the owner makes automatically?** No. Your fork is a
snapshot that only moves forward when you deliberately sync it, covered above. The original
repository can change indefinitely without your fork noticing, until you bring those changes in
yourself.

**Can the owner of the original repository see what I do on my fork?** For a public repository,
GitHub's own wording, quoted in the "Important security considerations" section of its forks
documentation, states that "Owners of an upstream repository can read all forks in the repository
network." Assume anything you do on a public fork is visible to the original repository's owner,
not just to you.

**Does forking cost me anything, or use up a seat on a paid plan?** This kit's research for this
file didn't turn up a direct statement either way. Forking is a repository-creation action, so if
you're already up against a repository or storage limit on your plan, that's the more likely place
it would show up, confirm on your own account's billing or usage page rather than assuming.

**I want to contribute to a project inside my own organization, but I don't have Write access to
it. Do I fork, or ask for access?** Either can work. Asking for access (`03-members-and-access.md`)
is simpler if you're going to be contributing regularly and the repository's owner is happy to grant
it. Forking is the better choice for a one-off contribution, or when you'd rather not wait on
someone else to grant you anything before you start.

---

## Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github
- https://docs.github.com/en/organizations/managing-organization-settings/managing-the-forking-policy-for-your-organization
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization
- https://cli.github.com/manual/gh_repo_fork
- https://cli.github.com/manual/gh_repo_sync
