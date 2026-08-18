# Branching and Pull Requests: Change Something Without Breaking What Everyone Else Pulls

This is the written, step by step version of the branching and pull requests deep dive. It is for
anyone already in the community, already pulling builds, and ready to change something of their
own. You do not need to have watched the video to follow this page.

Everything here happens in your browser. Nothing to install, no command line.

---

## The rule that matters most, read this first

> "Your access to the repo your drops come from is read-only, and it stays that way: you practise
> in your own repo or in the practice repo, because write access to the place everyone else
> installs from is the one thing nobody should be handed just to learn."

What that means in practice:

- You will **never** fork, branch, or open a pull request against the community repository your
  weekly builds come from. Your access to it is Read, and it stays that way, permanently.
- You practise the real mechanics of branching and pull requests in two other places instead:
  1. **A repository you own yourself.**
  2. **A dedicated public practice repository**, built just for this.

If you ever try to save a change directly in the community repository, GitHub will refuse it.
That is not a bug, and it is not just you, every member's account works exactly the same way.

**Why Read is enough.** The only things this guide needs you to be able to do on a shared
repository are: clone or download it, fork it, and send a pull request from that fork. GitHub's own
role table places all of those at the Read level, not Write. You cannot push directly to a
repository you only have read access to, and that limit is exactly what keeps the community
repository safe while you practise elsewhere.

---

## Before you start

You have completed GitHub 101 (`github-101-written-guide.md`), you are a member of the community
organization, and you have your own GitHub account. Browser only, nothing to install.

If you have never touched a branch or a pull request before, GitHub has its own free, official
course called **"Introduction to GitHub"**, at `github.com/skills/introduction-to-github`. It walks
through repositories, branches, commits, and pull requests hands-on, and GitHub itself says it
takes less than an hour. This page covers what that course does not: exactly which repositories in
this community you can write to, and which you cannot.

---

## Part A: Your own repository (the full loop)

This is the fastest, fully self-contained path. You own this repository, so you hold every
permission each step needs, and nothing here depends on anyone else.

1. **Have your own practice repository ready.** If you do not already have one, create a new
   repository under your own GitHub account. When you reach the visibility choice on the creation
   page, read what it actually shows and choose deliberately, GitHub does not state a default
   there.
2. **Make a branch before you touch anything.** Create a new branch, named after the change you
   are about to make, so your main branch stays untouched while you work.
3. **Save your change on that branch, not on main.** Commit your edit. It is now visible only on
   your branch.
4. **Open a pull request against your own repository**, comparing your branch to main. Give it a
   title that describes the change.
5. **Merge it.** GitHub gives you three ways to bring a pull request in: a **merge commit**, which
   is GitHub's own default, a **squash**, and a **rebase**. We recommend squash and merge for a
   community this size, because it keeps one pull request as one clean line in your history. That
   is our own recommendation, not GitHub's default, the other two options are sitting right there
   if a project ever needs them.
6. **Clean up.** Once merged, the temporary branch is no longer needed.

Because this is your own repository, GitHub will not stop you at any of these steps, you own every
permission involved. The exact button wording for creating a branch, committing a change, and
opening a pull request within your own repository is worth reading directly off your own screen as
you go.

---

## Hit the planted conflict, on purpose

Before you try this on a real change, see what a conflict actually looks like. Make one yourself,
on purpose, in a spare file, on two branches you create just for this. Nobody's real work is
anywhere near it.

GitHub's own documentation says: **"You can resolve simple competing line change conflicts on
GitHub"**, and **"for other conflicts, use the command line."** The steps below are the simple
case.

1. Open the pull request with the conflict. You will see a banner saying it cannot be merged
   automatically. Click **Resolve conflicts**.
2. In the editor that opens, pick the line you actually want to keep, and delete the conflict
   markers GitHub added around it.
3. Click **Mark as resolved** for that file.
4. Click **Commit merge**. This is the step that actually finishes it, not the "resolved" mark by
   itself.

If you ever hit a conflict the browser will not let you finish, that is not you doing something
wrong. It is a documented limit, and it is the one moment this workflow needs an actual git install
on a computer. The line to remember: **"this one needs a person, not me."** Post it in the
community, say which files, and someone will help you the rest of the way. That is not a failure,
that is exactly what the rule is for.

You can see a real, worked example of exactly this kind of conflict in the practice repository:
`https://github.com/selrai-company/github-training-content`, pull request 1.

---

## Part B: The practice repository (fork and propose)

This is the mechanic for a repository you do not own. It uses the community's dedicated public
practice repository, which is separate from the community's actual build repository and never
carries anything you install.

1. **Fork the practice repository.** Go to
   `https://github.com/selrai-company/github-training-content` and use GitHub's own Fork option.
   This puts a copy of it under your own account. GitHub's role table places forking a repository
   at the Read level, so your membership is enough, you do not need any special access.
2. **Branch and commit on your fork**, the same way you did in Part A: a new branch, then your
   change committed on it.
3. **Open the pull request back to the practice repository:**
   - Go to the original practice repository, the one you forked from.
   - Above the file list, in the yellow banner, click **Compare & pull request**.
   - On the page that opens, click **compare across forks**.
   - In the "base branch" dropdown, choose the branch of the practice repository you want to merge
     into.
   - In the "head fork" dropdown, choose your own fork, then use "compare branch" to choose the
     branch with your change.
   - Type a title and description for your pull request.
   - If you want, tick **Allow edits from maintainers**. Only tick this on a repository like the
     practice repository, which carries no automated workflows and no secrets. GitHub's own
     warning is that on a repository that does have workflows, this tick also lets a maintainer
     edit those workflows, which can expose secrets. It is safe here specifically because this
     repository does not have any.
   - Click **Create Pull Request**.
4. **Wait for a maintainer.** On this repository, you propose and a maintainer merges. You will not
   be able to merge your own fork's pull request here yourself, and that is expected, not a bug or
   something stuck. Once it is merged, copy the pull request's URL, that is your proof.

---

## Two habits worth keeping

1. **Only merge changes you actually understand.** If a pull request touches a file you do not
   recognise, stop and ask before you click merge, do not click merge to be polite.
2. **Why Read is enough, stated plainly:** Read grants every capability this guide needs you to
   have on a shared repository, cloning or downloading it, forking it, and sending a pull request
   from that fork. Write grants nothing this guide needs, and everything an attacker would want.

---

## What to post

Once you have one pull request merged, either on your own repository or the practice repository,
post the link in the community: `[LINK: where members post their proof]`.

That is the proof you did the thing, not just watched.

---

## Quick reference: what Read gives you versus what Write gives you

You do not need to memorise this. Come back to it if you are ever unsure why something did or did
not work.

| What it lets you do | Read | Write |
|---|---|---|
| Pull from a repository | Yes | Yes |
| Fork a repository | Yes | Yes |
| Send a pull request from your own fork | Yes | Yes |
| Submit reviews on a pull request | Yes | Yes |
| Push directly to a repository | No | Yes |
| Merge a pull request | No | Yes |
| Approve or request changes on a pull request with required reviews | No | Yes |
| Create, edit, run, or cancel GitHub Actions workflows | No | Yes |
| Create, update, or delete GitHub Actions secrets | No | Yes |

---

## If something goes wrong

- **Tried to push to the community repository and it was refused?** That is correct, expected
  behaviour. Practise in your own repository or the practice repository instead.
- **Opened a branch or a pull request against the wrong repository?** Check the name in your
  browser's address bar before you start. It should be your own repository, or the practice
  repository, never the community's build repository.
- **Stuck on a conflict bigger than the simple case?** Do not keep clicking. Post in the community,
  name the files, and ask for a person to help. This is expected, not a personal failure.
- **Your fork's pull request has not merged after a while?** That is normal, a maintainer merges
  it, not you. It is not stuck.
