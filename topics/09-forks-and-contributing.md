# Forks, and practising without breaking anything

## What this gets you

A fork is your own personal copy of somebody else's repository, sitting under your own account,
with your name on it as the owner. Forking lets you start changing something you do not have
Write access to, a vendor's public template, an open-source tool your business relies on, another
team's project inside your own organization, without asking anyone for permission first, and
without any risk of what you do touching their copy until you choose to propose it back.

For a small business, that means the person who wants to try a fix does not have to wait on an
access request, a phone call, or someone else's calendar before they can start. It is also the
lowest-stakes way to practise everything else this kit teaches, on a copy that cannot break
anything real, before you touch a repository that matters.

## Before you start

**Read `07-pull-requests.md` first, if you have not already.** Everything a fork is for leads
toward opening a pull request, and this file assumes you already know what one is and how
reviewing and merging one works.

**You do not need anyone's permission to fork a public repository.** Read access, which is what
you already have on any public repository the moment you can view it, is enough. There is no
request to send and no approval to wait on before you can start.

**If you want to practise without any real stakes first**, this kit's own practice repository, at
`https://github.com/selrai-company/github-training-content`, says so plainly in its own README:
"Fork it, break it, nothing here matters." Forking it gives you a copy that is entirely yours,
where nothing you do can affect the original, and nothing the original changes can silently break
whatever you are in the middle of trying. Every step below works the same on that practice
repository as it does on a real one.

**Forking a private repository is a different, narrower case**, covered in its own section below.
If the repository you want to fork is private, read that section before you start, since it
depends on a setting its owner controls, and you may not be able to fork it at all yet.

## The words you need

**Fork.** Your own personal copy of somebody else's repository, sitting under your own account,
with your name on it as the owner. GitHub's own definition: "Forks are repositories that start as
copies of another repository, called the upstream repository. A fork has its own settings and
permissions but stays connected to the upstream repository." A fork is a separate repository, not
a branch inside the one you are looking at. Per GitHub's own documentation, it independently has
its own branches, its own members and discussions, its own issues and pull requests, its own
Actions and projects, and its own tags, labels, and wikis. Nothing you do inside your fork touches
any of that on the original repository, and nothing that happens on the original repository
changes what is sitting in your fork, until you deliberately bring the two together.

| | A branch | A fork |
|---|---|---|
| Lives inside | The same repository | A separate repository, under your own account |
| Who can create one | Anyone with Write access to that repository | Anyone with Read access to the repository, if its owner allows forking |
| What you can change | Only what you already have Write access to | Whatever you own, since the fork is now yours |
| How it comes home | A pull request, reviewed and merged by someone with access to that repository | A pull request, reviewed and merged by someone with access to the *upstream* repository, not by you |

**Upstream.** GitHub's own name for the repository your fork came from. Your fork stays connected
to it, and every mention of "the original repository" in this file means the same thing as
"upstream."

**Shared repository model.** The collaboration style covered in `06-branches.md` and
`07-pull-requests.md`: everyone working on a repository has Write access to it directly, and works
on branches inside that same repository.

**Fork and pull model.** The collaboration style this file covers. GitHub's own description: "In
the fork and pull model, anyone can fork an existing ('upstream') repository if they have read
access and the owner of the upstream repository allows it." Its own words on what that buys you:
"You do not need permission from the upstream repository to push to a fork you created." Once it
is your fork, it is your repository, and nobody needs to sign off on what you do inside it.

**Base repository, and base branch.** The repository, and the branch on it, you want your change
merged into. When you propose a change from a fork rather than from a branch in the same
repository, GitHub asks you to choose both explicitly. It is almost always the original (upstream)
repository, and its default branch.

**Head repository, and compare branch.** The repository, and the branch on it, that actually holds
your change. When proposing a change from a fork, this is your fork, and the branch on your fork
where you made the change.

**Maintainer.** Someone with push access to the repository you are proposing a change to, covered
in full in `07-pull-requests.md`. This word matters here for one reason: the "Allow edits from
maintainers" checkbox, covered below, only appears on a pull request opened from a fork.

**Syncing.** Bringing your fork up to date with whatever has changed on the upstream repository
since you forked it, or since you last synced. Covered in full below.

**Repository network.** The original repository and every fork of it, all connected to each other.
GitHub uses this term for two facts worth knowing before you rely on a fork: the original
repository's owner can see every fork in its network, and something you contributed can survive
inside that network even after you delete the fork it came from. Both are covered below.

## How to do it

Most of what follows happens in your browser, the same as branches and pull requests. Wherever
Claude Code is genuinely faster or safer instead, this file says so.

### Forking, step by step

**In the browser:**

1. On the repository's main page, click the **Fork** button in the top-right corner. A count next
   to it shows how many forks already exist.
2. Choose an **Owner** for your new fork from the dropdown: your personal account, or an
   organization where you have permission to create repositories.
3. Optionally change the repository name and add a description.
4. Optionally tick **Copy the DEFAULT branch only**. Leave it unticked and every branch on the
   original comes with you; tick it and you get just the default branch (usually `main`), the
   lighter option if you only care about the project's current state.
5. Click **Create fork**.

You will know it worked because your new repository opens automatically, with a line just under
its name reading something like "forked from OWNER/REPOSITORY," a real link back to the original.
If nothing happens, or you see an error, see "If it goes wrong" below.

**Screenshot placeholder:** the fork creation screen, showing the Owner dropdown, the repository
name field, and the "Copy the DEFAULT branch only" checkbox, so a reader can match every field to
the steps above before clicking Create fork.

**What forking a public repository needs from you:** GitHub's own wording: "You can fork any
public repository: To your personal account [or] To an organization where you have permission to
create repositories." No Write access to the original is needed. What you get on the copy itself
is entirely yours: GitHub's own wording, "Fork owners control access to their forks." You decide
who else gets to see or change it, the same as any repository you create. Forking a private
repository works differently, covered below.

**Visibility always matches the original.** GitHub's own wording: "A fork's visibility is tied to
the upstream repository's repository network. Public repository forks are public, and private
repository forks are private." You cannot fork a public repository into a private copy, or a
private repository into a public one. Whatever the original is, your fork matches it.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in** (the
same one-time setup mentioned in `04-repositories-and-visibility.md`, `05-daily-workflow.md`, and
`07-pull-requests.md`): ask it in plain English, or let it run something like this on your behalf.

```
gh repo fork OWNER/REPOSITORY --clone=true
```

The GitHub CLI's own flags: `--clone=true` also copies the fork onto your machine in the same
step, `--org "your-org-name"` forks it into an organization instead of your personal account, and
`--remote=true` (the default) sets up the connection back to the original so a later sync knows
where to look. If `gh` is not installed and signed in yet, use the browser path above instead.

### Opening a pull request from a fork back to the original

Once you have made your change on your fork, bringing it back to the original repository works the
same way as the pull requests `07-pull-requests.md` covers, with one extra step to bridge the two
repositories.

**Who can do this:** the same rule `07-pull-requests.md` already states, GitHub's own words: "you
must have write access to the head or the source branch." Here, the head repository is your fork,
which you own, so you already have that. You do not need write access to the original repository
to open the pull request, only to propose it, which is the entire point of forking in the first
place.

**The click path:**

1. On the *original* (upstream) repository's page, above the file list, click **Compare & pull
   request** if you see the yellow banner, or click the **Pull requests** tab and start a new one.
2. Click **compare across forks**. This is the step that differs from a same-repository pull
   request: it reveals the extra dropdowns needed to point at your fork instead of a branch in this
   same repository.
3. Use the **base repository** and **base** branch dropdowns to choose the original repository and
   the branch you want your change merged into (usually its default branch).
4. Use the **head repository** dropdown to choose your fork, and the **compare** branch dropdown to
   choose the branch on your fork that holds your change.
5. Type a title and description; the same guidance `07-pull-requests.md` covers applies here.
6. Decide on **Allow edits from maintainers**, fully covered in `07-pull-requests.md`. It is this
   exact checkbox, it is specific to pull requests from a fork, and it is worth a genuine decision
   rather than a reflex.
7. Click **Create Pull Request**, or use the dropdown next to it for **Create Draft Pull Request**.

You will know it worked because the pull request opens on its own numbered page, sitting on the
*original* repository, not your fork, with your title at the top. If you cannot find **compare
across forks**, see "If it goes wrong" below.

**Screenshot placeholder:** the pull request creation screen with **compare across forks** clicked,
showing the base repository/branch dropdowns on the left and the head repository/branch dropdowns
on the right, so a reader can see the exact layout before choosing theirs.

Everything after this point, the tabs on the pull request's page, reviewing, the three merge
methods, draft pull requests, closing without merging, is identical to a pull request from a branch
in the same repository. `07-pull-requests.md` covers all of it in full. Nothing about it changes
just because the pull request started on a fork, except who is allowed to actually merge it, which
is the next section.

### The honest boundary: proposing is not merging

This is the part worth being direct about rather than glossing over.

GitHub's own wording, from its documentation on merge methods: "To merge pull requests, you must
have write permissions in the repository." That is write permission on the *original* repository,
not your fork. Having write access to your own fork, which you always have because you own it, is
what lets you open the pull request. It is not what lets you click the merge button on it.

**This is the normal shape of real collaboration, not a limitation of your account.** If forking
required the same access as merging, there would be no point to forking at all, you could just ask
for Write access and work on a branch instead, covered in `06-branches.md`. The entire value of the
fork and pull model is that proposing a change and approving it are two separate roles, held by two
different levels of access, so a repository's owner never has to hand out push access just to let
someone suggest an improvement. You propose. Whoever holds Write access (or higher) on the original
repository decides whether it merges. That is not you being locked out, that is the repository
owner's actual project staying under their actual control, the same way you would want it to work
if someone else forked one of your own repositories.

**In practice, for a small business:** if you fork someone else's repository, open a pull request,
and the merge button does nothing for you, that is expected, not an error. You have done your
part. What happens next is up to whoever maintains the repository you forked from: they review it
(the process `07-pull-requests.md` covers), and if they are satisfied, they are the ones who click
merge, because Write access on that repository is theirs, not yours. If you would rather not wait
on that, and you have the standing to make the change yourself, that is the signal it should have
been a branch in a repository you already have Write access to, not a fork.

### Forking a private repository

Everything above assumes a public repository, the more common case. Private repositories behave
differently, in two ways worth knowing before you rely on a fork of one.

**Your fork does not fully separate from the original the way a public fork does.** GitHub's own
wording: "Private forks inherit the permissions structure of the upstream repository." This has a
real consequence, covered in `03-members-and-access.md`'s offboarding section and worth repeating
here because it is specifically about forks: "If you remove a person's access to a private
repository, any of their forks of that private repository are deleted." If you fork a private
repository and later lose your access to the original, your fork does not survive that on its own,
it goes with it. There is one documented exception: a private repository forked into a *different*
organization can survive under that organization's own control, independent of what happens to
your access in the original. That is an edge case most small-business readers will not hit, but it
is real.

**Forking a private repository at all needs its owner's permission, and that permission is a
two-layer setting.** GitHub's own wording on what is required: "You cannot fork a private
repository to an organization using GitHub Free." And: "If you have access to a private repository
and the owner permits forking, you can fork the repository" to your personal account, or to a
GitHub Team organization where you have repository creation permissions. Two conditions have to be
true at once: you need access to the private repository in the first place, and its owner has to
have allowed forking.

For a private repository owned by an organization, here is exactly what "the owner permits
forking" means.

**Layer one, the organization-wide switch.** GitHub's own wording for what it does: "Allow or
prevent the forking of any private repositories owned by your organization." This applies only to
private repositories, it has no effect on public ones. Its own stated default: "New organizations
are configured to disallow the forking of private repositories." Unless an organization owner has
turned this on, no private repository in that organization can be forked at all, no matter what any
individual repository's own setting says.

To check or change it: from any github.com page, click your **profile picture** in the top right
corner, then click **Organizations**. The direct address, if you would rather go straight there,
is `https://github.com/settings/organizations`. Click your organization's name. Along the top of
the organization's own page, click its **Settings** tab. In the sidebar, under the **Access**
heading, click **Member privileges**, then find the **Repository forking** section, tick **Allow
forking of private repositories**, and click **Save**.

You will know it worked because the checkbox still shows ticked the next time you load the page.
If you do not see an **Access** heading in that sidebar at all, you are most likely not signed in
as an organization owner; `03-members-and-access.md` covers organization roles in full.

**Layer two, the specific repository's own switch.** GitHub's own wording: this setting lets you
"allow or prevent the forking of a specific private repository" owned by an organization. On the
repository's page (the address follows the pattern
`https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings`), click **Settings**, then in the
**Features** section, tick **Allow forking**. Its own stated dependency, worth reading twice: "An
organization owner must allow forks of private repositories on the organization level before you
can allow or disallow forks for a specific repository." Layer one has to be on before layer two
does anything at all. If you tick **Allow forking** on a repository and nothing changes, check the
organization-level setting first, this is the most likely reason.

**What this kit could not confirm, and what to check on your own screen instead:** GitHub's
documentation states the two-layer setting above specifically for repositories owned by an
*organization*. It does not, in what this kit could verify, spell out a separate forking toggle for
a private repository owned by an individual personal account rather than an organization. If you
are trying to fork (or allow forking of) a private repository that sits under someone's personal
account rather than an organization, the safest approach is to have the repository's owner check
its **Settings** page, in the **Features** section, for an **Allow forking** option on their own
screen, the same place the organization-owned version lives, and confirm from there rather than
assuming either way.

**Visibility stays private either way.** As covered above, a fork of a private repository is
itself private, per GitHub's own wording quoted earlier: "private repository forks are private."
Forking a private repository never makes it, or your copy of it, visible to anyone who could not
already see the original.

### Keeping a fork up to date

Your fork is frozen at whatever state it was in the moment you created it, plus anything you have
changed on it since. It does not automatically follow along as the original repository keeps
moving. Bringing your fork up to date with those changes is called syncing.

**In the browser:**

1. On your fork's main page, above the file list, click the **Sync fork** dropdown.
2. Review the commits it shows you from the upstream repository.
3. Click **Update branch**.

You will know it worked because the dropdown closes and your fork's file list now reflects the
commits you just brought in.

**Screenshot placeholder:** the **Sync fork** dropdown open on a fork's main page, showing the
**Update branch** button and a short summary of how many commits it is about to bring in, so a
reader recognises it the first time they see it.

**If the upstream's changes conflict with your own,** GitHub's own wording: "If the changes from
the upstream repository cause conflicts, GitHub will prompt you to create a pull request to resolve
the conflicts." You will be walked into the same kind of conflict resolution `08-merge-conflicts.md`
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
you need to look at a single line yourself. If you would rather use the GitHub CLI directly instead
of plain English, `gh repo sync owner/your-fork -b branch-name` does the same job; add `--force`
only if you are deliberately choosing to overwrite your fork's branch with the upstream's version
rather than merge the two, GitHub's own documentation is clear that this is what `--force` is for
when a sync would otherwise conflict.

**One thing worth knowing if you ever do use the command line yourself:** GitHub's own note on this
is easy to miss, "Syncing your fork only updates your local copy of the repository. To update your
fork on GitHub.com, you must push your changes." A sync you run through git commands on your own
machine does not reach GitHub on its own, you (or Claude Code, on your behalf) still need to push
afterward. The browser's **Sync fork** button and the `gh repo sync` command both handle this for
you in one step; the plain git command-line path is the one place this catches people out.

### Deleting a fork

A fork is a repository, so deleting one uses exactly the steps in
`04-repositories-and-visibility.md`'s deletion section: the repository's **Settings** page, its
**Danger Zone**, and typing the repository's name to confirm. Read that section before deleting
anything you are not fully sure about, it covers the general safety net (some deleted repositories
can be restored within 90 days, though GitHub does not promise that for every case) in full.

Two things worth knowing that are specific to forks rather than repositories in general:

**Deleting your fork never touches the original repository.** Per GitHub's own wording quoted
earlier in this file, fork owners control their own fork. Deleting it is entirely your decision and
affects nothing upstream.

**Your commits do not necessarily vanish the instant your fork does.** GitHub's own wording: "If
you delete a fork, code contributions from that fork can remain accessible to the repository
network." If anything you committed on your fork was ever pulled into another repository in that
same network, a pull request that got merged, for instance, deleting your fork does not erase that
history. Treat anything you have ever pushed to a fork the same way this kit treats anything ever
made public: assume it can outlive the fork itself, rather than counting on deletion as a clean
undo.

**What this kit could not confirm:** whether deleting a fork automatically closes any pull requests
you had opened from it that are still open. GitHub's own documentation on what happens to forks
when a repository is deleted or changes visibility does not state this either way for the fork side
(only for what happens when the *upstream* is deleted). If you have an open pull request from a
fork you are about to delete, close or merge that pull request first, on its own page, rather than
assuming deleting the fork will tidy it up for you.

## Strategy: how to actually use this

**Fork when you do not have Write access and are not going to get it quickly, or ever.** That is
the whole decision. If you already have Write access to a repository, or could reasonably ask for
it today and expect a yes, a branch (`06-branches.md`) does the same job with one repository
instead of two, and nothing about opening a pull request changes. Fork when the repository belongs
to someone else entirely, a vendor, an open-source project, another team inside your own
organization that has not (and may not) grant you access, and forking is the only way to start
working on it at all.

**A solo operator working alone** has one genuine use for forking: contributing back to something
outside their own business. If your website runs on an open-source tool and you find a bug, or a
fix you need, forking that tool's repository, making the change, and opening a pull request is how
you get it back to the people who maintain it, instead of quietly patching your own copy forever
and having to redo the patch every time you update. Practising on this kit's own training
repository is the other genuine solo use: a safe copy to try branches, commits, and pull requests
on before you touch anything that matters.

**A team of three or four** rarely forks each other's work. Everyone inside the same small
business who has been added to a repository already has, or can quickly be given, Write access to
it, so a branch is the right tool, not a fork: if you already have the standing to make the change
yourself, forking adds a second repository to keep track of for no reason. The team-of-three case
where forking genuinely applies is the same as the solo case, scaled up: the nephew who builds and
maintains a café's ordering site, contributing a fix back to an open-source library the site
depends on, does so from his own personal account, as a fork, the same as he would for any other
outside project, regardless of how many people are on the café's own team.

**The decision rule, in one sentence: if you would need to ask someone outside your own team for
access, fork; if you would only need to ask someone on your own team, use a branch.** That single
question resolves almost every case. The rare exception is a large organization where "your own
team" and "the repository owner" are technically the same company but different people who do not
know each other; that situation behaves like forking from a stranger even though you both work for
the same business, and this file's fork-and-pull steps are still the right ones to follow.

**What good looks like months later:** a fork you opened to fix or add one specific thing has
either been merged into the original, and you have deleted the fork since its job is done, or is
still open with a clear reason why, not sitting forgotten with commits nobody remembers making. A
fork you keep around for ongoing customization of a vendor's template gets synced regularly enough
that bringing in the vendor's own updates is a small, easy step, not a rare, dreaded one with weeks
of drift to reconcile.

**What would change our recommendation:** if your organization forks the same handful of outside
repositories often enough that setting up and syncing each one by hand becomes real, recurring
work, that is worth a conversation with a developer about automating the sync, not something this
kit teaches solo. For nearly every small business this kit is written for, forking stays an
occasional, deliberate action, not a routine one.

## A worked example

The café's ordering site, built and kept running by the owner's nephew (the same team of three
described in this kit's strategy pack), runs on an open-source booking widget he did not write. He
notices the widget shows the wrong currency symbol when a customer's browser is set to a language
other than English, a real bug affecting real customers, and he does not have Write access to the
widget's own repository, nobody outside its own maintainers does.

He opens the widget's repository on GitHub, clicks **Fork** in the top-right corner, leaves the
owner as his own personal account, leaves the branch option unticked so he gets the full history,
and clicks **Create fork**. His copy opens with "forked from theirname/booking-widget" under its
title.

He clones his fork, following `05-daily-workflow.md`, and creates a branch called
`fix-currency-symbol`, following `06-branches.md`. He finds the line that hard-codes the dollar
sign, corrects it to read the browser's own locale instead, commits the change, and pushes the
branch to his fork.

Back on the *original* widget repository, he opens a new pull request, clicks **compare across
forks**, sets the **head repository** to his own fork and the **compare** branch to
`fix-currency-symbol`, and leaves the **base repository** and **base** branch as the original
project's default. He titles it "Fix currency symbol for non-English locales" and describes what
he saw and how he tested the fix. He leaves **Allow edits from maintainers** ticked, since he would
rather the widget's own maintainers fix a small style issue themselves than wait on him.

Two days later, one of the widget's maintainers reviews it, asks him to adjust one line, he pushes
the fix to the same branch on his fork, and the pull request updates automatically. The maintainer
approves and merges it, since Write access on that repository is theirs, not his. His fork's job is
done: he deletes it, following `04-repositories-and-visibility.md`'s deletion steps, and the café's
ordering site picks up the fix the next time he updates the widget in the site's own repository.

If he had needed to keep customizing the widget's own copy on an ongoing basis, rather than a
one-off fix, he would have kept the fork instead of deleting it, and synced it periodically using
the **Sync fork** button to stay current with the maintainers' own updates.

## If it goes wrong

**I clicked Fork and got an error, or nothing happened.** If the repository is public, this
usually means you are trying to fork it into an organization where you do not have permission to
create repositories, try your personal account instead. If the repository is private, you either
do not have access to it at all, or its owner has not allowed forking, see the private repository
section above for the two-layer setting that controls this on an organization-owned repository.

**I don't see "compare across forks" when I try to open a pull request.** This usually means you
are looking at the pull request screen from inside your own fork rather than the original
repository. Navigate to the *original* repository's **Pull requests** tab and start a new pull
request from there instead.

**I forked a repository and now I can't find the connection back to the original.** Your fork's
main page shows a line just under the repository name reading something like "forked from
[owner/repository]," that is a real link to the upstream. If you are working through Claude Code
instead and it has lost track of which repository is upstream, ask it directly: "Which repository
did I fork this from?"

**I tried to sync my fork and it says there's a conflict.** That is expected when the same lines
have changed on both sides since you forked. Follow the prompt GitHub gives you to open a pull
request and resolve it, the process is the same one `08-merge-conflicts.md` walks through in full.

## FAQ

**Can I fork a repository I already have Write access to?** Yes, nothing stops you, but there is
usually no reason to. If you already have Write access, a branch (`06-branches.md`) does the same
job with less overhead, since you do not need a separate repository just to make a change you are
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
file did not turn up a direct statement either way. Forking is a repository-creation action, so if
you are already up against a repository or storage limit on your plan, that is the more likely
place it would show up, confirm on your own account's billing or usage page rather than assuming.

**I want to contribute to a project inside my own organization, but I don't have Write access to
it. Do I fork, or ask for access?** Either can work. Asking for access (`03-members-and-access.md`)
is simpler if you are going to be contributing regularly and the repository's owner is happy to
grant it. Forking is the better choice for a one-off contribution, or when you would rather not
wait on someone else to grant you anything before you start.

## Quick reference

- **Fork a repository:** its main page, **Fork** button (top right), choose an owner, **Create
  fork**
- **Fork through Claude Code:** `gh repo fork OWNER/REPOSITORY --clone=true`
- **Open a pull request from your fork:** the *original* repository's **Pull requests** tab, new
  pull request, **compare across forks**, set the head repository to your fork
- **Sync your fork:** its main page, **Sync fork** dropdown, **Update branch**
- **Sync through Claude Code:** ask in plain English, or `gh repo sync owner/your-fork -b
  branch-name`
- **Allow forking of a private organization repository (both layers needed):** **Organizations** >
  the organization > **Settings** > **Access** > **Member privileges** > **Repository forking**
  (organization-wide), then the repository's own **Settings** > **Features** > **Allow forking**
- **Delete a fork:** its **Settings** page, **Danger Zone**, type the repository's name to confirm

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
