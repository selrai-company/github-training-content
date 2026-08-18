# Repositories, and the public or private choice

A repository is the container everything else in this kit lives inside of: your code, your
files, your history. Get the visibility choice right when you create one (public or private)
and you'll rarely think about it again. Get it wrong, especially by committing a password or an
API key into one, and it can be the single most expensive mistake you make on GitHub. This file
covers both: what a repository actually is, how to create one, the public/private choice in
GitHub's own words, what to put in one and what to keep out, and what to do later if you need to
change your mind, archive something, or delete it entirely.

Most of this happens in your browser. A few steps have a genuinely faster path through Claude
Code, and this file says so plainly when that's true, and just as plainly when it isn't.

## What a repository actually is

GitHub's own words: "A repository is the most basic element of GitHub. It's a place where you
can store your code, your files, and each file's revision history." Put simply, it's a folder
that GitHub knows how to track. Every change you or anyone else makes to a file inside it is
kept, so you can always see what changed, when, and who changed it.

Think of it like a shared project folder with a very good memory. A normal folder on your
computer only shows you the current state of your files. A repository remembers every version
that came before, and lets you (or a teammate) look back at any of them.

**Screenshot placeholder:** a repository's main page on github.com, showing the file list, the
README displayed underneath it, and the commit count near the top, so a reader can see what a
repository actually looks like before creating their own.

## Creating a repository

**The browser path** (the one to use the first few times, so you can see every field on the
actual screen rather than trust a description of it):

1. In the upper-right corner of any github.com page, click the **+** icon, then click **New
   repository**.
2. Choose the **Owner** (your personal account, or an organization if you've created one, see the
   organizations file in this kit).
3. Type a short, memorable **Repository name**.
4. Optionally add a **Description**.
5. Choose the repository's **visibility** (public or private). Read the next section before you
   click either one.
6. Toggle **Add a README file** on. There's more on why below.
7. Optionally add a `.gitignore` template and a license (this file's gitignore section below
   covers `.gitignore` in more depth than the dropdown here does).
8. Click **Create repository**.

**Screenshot placeholder:** the "Create a new repository" form, showing every field currently on
it, so a reader can match what they see to this list before they click Create.

**The Claude Code path**, if you already have the GitHub CLI (`gh`) installed and signed in on
your machine: ask Claude Code to run `gh repo create your-repo-name --public` or
`gh repo create your-repo-name --private`, add `--clone` if you want it copied onto your machine
at the same time. This is a genuinely good shortcut once `gh` is set up, because the command
makes you type the visibility flag explicitly. There's no ambiguous radio button to misread. If
you haven't got `gh` installed and signed in yet, use the browser path above instead; getting
`gh` authenticated for the first time is its own one-time setup step and isn't covered in this
file.

## The choice that matters most: public or private

GitHub's own definitions, verbatim:

- **Public:** "Public repositories are accessible to everyone on the internet."
- **Private:** "Private repositories are only accessible to you, people you explicitly share
  access with, and, for organization repositories, certain organization members."

Read the public definition again. Not "anyone who knows the link." Not "anyone signed in to
GitHub." **Everyone on the internet**, with no account and no invitation needed. If you make a
repository public, assume a stranger can and eventually will find it, even if you never share the
link yourself.

There's a third visibility option, **internal**, but it only exists for organizations that use
GitHub Enterprise Cloud under an enterprise account. If you're on GitHub Free (which is where
almost every solo owner and small team starts, see the organizations file for what a new
organization lands on by default), you won't see it as an option, and that's expected, not a bug.

**Do not assume which one is pre-selected on the creation form.** GitHub's own documentation
describes the field as "Choose a repository visibility" without stating which option is
pre-selected, and neither of GitHub's two published walkthroughs for creating a repository names
a default either. **Read your own screen at the moment you create the repository, and pick
deliberately.** Don't click through this step on autopilot.

**A practical default worth adopting for yourself, not GitHub's:** if you're not certain, start
private. You can make it public later if you decide to (the next section below covers exactly
what that changes). Going the other way, from public back to private, doesn't undo whoever
already saw or copied it while it was public.

**One private-repository nuance worth knowing.** The definition above says a private
organization repository is visible to "certain organization members," not just to people you've
explicitly invited. Exactly who that includes depends on your organization's own permission
settings, which is covered in this kit's organizations file, not here. For a private repository
under your own personal account (not an organization), it's just you and whoever you've
explicitly added as a collaborator, covered later in this file.

**The one thing public is never the right answer for: sharing with your team.** If you want a
teammate, a contractor, or a client to see a repository, the correct move is to add them as a
collaborator (or, for an organization, give them access through the organization, see the
organizations file). Making the repository public "so they can see it" also hands it to everyone
else on the internet at the same time. There is no visibility setting that means "just the people
I've shared it with, plus anyone who happens to find it," only private (explicit access) and
public (everyone).

## What belongs in a repository, and what doesn't

**Belongs:**

- Your actual project files (code, configuration, documents that are part of the project itself).
- A `README` file. GitHub's own recommendation: "we recommend that you create a README file for
  every repository." More on this below.
- A `.gitignore` file, so the things that shouldn't be tracked never get the chance to be.
  Covered in its own section below.
- Optionally, a `SECURITY.md` file, which GitHub describes as a file that "provides instructions
  to collaborators on how to report security vulnerabilities found in your project." Worth
  adding once you have collaborators; not urgent for a solo repository.

**Doesn't belong:**

- **Secrets.** Passwords, API keys, tokens, database credentials. None of these should ever be
  typed directly into a file that gets committed. The `.gitignore` section below is built
  specifically around keeping these out from the start.
- **Very large files.** GitHub's own stated limits: files over 100 MiB are blocked outright, a
  push that includes a file over 50 MiB triggers a warning (though it still goes through), and
  browser uploads are capped at 25 MiB. Beyond the hard limits, GitHub's own guidance on overall
  repository size is to keep it "ideally less than 1 GB, and less than 5 GB is strongly
  recommended," because smaller repositories are faster to clone and work with. For anything that
  genuinely needs to be large (a big design file, a database export), GitHub's own suggestion is
  Git Large File Storage (Git LFS), or, for distributing a large file to other people rather than
  tracking its changes, a GitHub Release, not a normal commit.
- **Personal files that have nothing to do with the project.** Not a GitHub rule, just good
  hygiene: a repository is easier to understand, for you and for anyone you share it with, when
  everything in it is actually part of the project.

## The README, and why it's worth writing

A README is the file GitHub shows automatically on a repository's main page, right underneath the
file list. GitHub's own framing of its purpose: it's there to "communicate important information
about your project," typically the first thing a visitor reads, explaining "what the project does,
why the project is useful, how users can get started with the project, and where users can get
help."

GitHub looks for a file named `README` (in one of a few common formats, `README.md` being the
usual choice) in three specific locations, checked in this order: the hidden `.github` directory,
then the repository's root directory, then a `docs` directory. Wherever it finds one first, that's
the one it displays. For almost every small-business repository, putting `README.md` straight in
the root directory (where you'd naturally expect it) is the simplest choice and needs no special
setup.

Keep it focused. GitHub's own guidance: "a README should only contain information necessary for
developers to get started using and contributing to your project," and anything longer belongs in
a wiki instead. For a small business repository, that usually means: one or two lines on what this
project is, and enough for you (or whoever inherits it later) to remember how to use it six months
from now, not a full manual.

**Screenshot placeholder:** a repository's main page with a short README rendered underneath the
file list, so a reader can see how plain text turns into a formatted page automatically.

## Keeping secrets out in the first place: .gitignore

A `.gitignore` file is, in GitHub's own words, "a file in your repository's root directory to tell
Git which files and directories to ignore when you make a commit." Anything listed in it never
gets tracked, never gets committed, and never ends up visible to anyone the repository is shared
with (or, if the repository is public, visible to the entire internet).

Create a file named exactly `.gitignore` (the leading dot matters) in your repository's root
directory, and paste something like this into it as a starting point:

```gitignore
# Secrets and environment files. Never commit these.
.env
.env.local
.env.*.local

# Operating system clutter
.DS_Store
Thumbs.db

# Installed dependencies (these get reinstalled automatically, no need to track them)
node_modules/

# Build output and log files
dist/
build/
*.log
```

**Why the `.env` line matters more than anything else in this file:** a `.env` file (or similar,
`.env.local`, `.env.production`, and so on) is the standard place a project keeps its secrets
while you're working on it locally, API keys, passwords, tokens, connection strings. The three
lines at the top of that block stop Git from ever tracking any file with that pattern. If you add
nothing else from this list, add those three lines, before your first commit, not after.

**The catch, and why "before" matters:** `.gitignore` only stops files it doesn't already know
about. GitHub's own guidance is direct about a file that's already been committed: "If you want to
ignore a file that is already checked in, you must untrack the file before you add a rule to
ignore it," using `git rm --cached FILENAME`. Untracking it removes it going forward, but it does
**not** erase it from your history, every earlier commit that included it still holds a copy.

**If a real secret has already been committed, the fix isn't deleting the file.** GitHub's own
first-step guidance, worded exactly like this: "if the sensitive data you need to remove is a
secret (e.g. password/token/credential)... as a first step you need to revoke and/or rotate that
secret." Rotate it in whatever service issued it (get a new key, invalidate the old one)
immediately. That single step removes the danger, because the leaked value stops working the
moment it's rotated, regardless of how many places it's still sitting in your history. Cleaning
the committed value out of your repository's history after that is a real but separate job, one
this kit deliberately does not walk you through solo: bring it to the community rather than
attempting a history rewrite yourself, because a botched one can cause more damage than the
leaked secret did. Rotating the secret is the part that actually closes the hole; treat the
history cleanup as optional tidying after that, not the urgent step.

## Changing visibility later, and what that actually exposes

You can flip a repository between public and private at any time, if you have the right
permissions (an organization can restrict this to organization owners only). The click path is
the same for either direction:

1. Open the repository's main page, click **Settings**.
2. Scroll to the **Danger Zone**.
3. Click **Change visibility**.
4. Select the visibility you want.
5. Confirm you're changing the correct repository, click **I have read and understand these
   effects**.
6. Click **Make this repository public** or **Make this repository private**, whichever applies.

**Going private to public exposes exactly what you'd expect, stated by GitHub itself:** the code
becomes visible to everyone who can visit GitHub.com, all push rulesets on the repository are
disabled, and Actions history and logs become visible to everyone too. Once something has been
public, even briefly, treat it the same way this file treats a leaked secret above: assume it may
already have been seen or copied, and flipping back to private does not undo that.

**Going public to private has its own side effects, also stated by GitHub itself:** stars and
watchers on the repository are erased (this affects how the repository ranks in GitHub's own
listings), any GitHub Pages site published from it is unpublished, and existing forks stay public
and get detached from your repository rather than turning private with it. If other people had
already forked your public repository, making the original private does not make their copies
private too.

Both directions also erase the repository's stars and watchers. Neither direction is
reversible in the sense of undoing what already happened while the old setting was live; it only
changes what happens going forward.

## Archiving a repository

Archiving is for a project that's finished, but that you want to keep around exactly as it is,
without the risk of an accidental edit. GitHub's own description of what it does: it makes the
repository "read-only for all users and indicate[s] that it's no longer actively maintained."
Once archived, its "issues, pull requests, code, labels, milestones, projects, wiki, releases,
commits, tags, branches, reactions... comments and permissions become read-only."

1. Open the repository's main page, click **Settings**.
2. Scroll to the **Danger Zone**, click **Archive this repository**.
3. Read the warnings on screen.
4. Type the repository's name to confirm.
5. Click **I understand the consequences, archive this repository**.

You can reverse this. From the same **Danger Zone**, click **Unarchive this repository**, review
the warnings, type the repository's name to confirm, and click **I understand the consequences,
unarchive this repository**.

**Screenshot placeholder:** an archived repository's main page, showing the "This repository has
been archived" banner GitHub displays, so a reader knows what it looks like from the outside.

## Deleting a repository

Different from archiving: deletion removes the repository, not just makes it read-only. GitHub's
own wording is blunt: "Deleting a repository will permanently delete team permissions. This
action cannot be undone." For a private repository specifically, deleting it also deletes every
fork of it; public repository forks are preserved even after the original is deleted.

**You need admin access to the specific repository, or owner privileges on the organization it
belongs to, to delete it.** This isn't a button every collaborator can see.

1. Open the repository's main page, click **Settings**.
2. On the General settings page, scroll to the **Danger Zone**.
3. Click **Delete this repository**.
4. Click **I want to delete this repository**.
5. Click **I have read and understand these effects**.
6. Type the repository's name in the text box.
7. Click **Delete this repository**.

**One partial safety net, worded carefully because GitHub words it carefully:** GitHub's own
documentation says "some deleted repositories can be restored within 90 days of deletion," not
every deleted repository. Don't treat that window as a guarantee for your specific case; if you
think you deleted something by mistake, act immediately and contact GitHub support rather than
assuming the 90 days definitely covers you.

**In practice:** if you're not certain you'll never need a repository again, archive it instead
of deleting it. Archiving costs you nothing but a little clutter, and it can be undone with
certainty. Deletion cannot.

## Repository settings worth a look, and the ones to leave alone

**Worth knowing about:**

- **General settings and the Danger Zone**, covered above: rename, transfer (see the
  organizations file), change visibility, archive, delete.
- **Access → Collaborators**, for a repository under your own personal account (not an
  organization). This is the correct way to share a private repository with one or a few specific
  people, not making it public. GitHub's own click path: repository **Settings** → **Access**
  section → **Collaborators** → **Add people** → search for and select the person → confirm the
  invite. GitHub's own screen also lets you choose exactly what that person is allowed to do once
  they accept; read that part of the screen rather than accepting a default without looking.
- **Features**, a toggle list for things like Issues, Wikis, and Discussions. Turn on what you
  actually plan to use; leave the rest off rather than guessing you might need it later.

**Leave alone unless you have a specific reason:** GitHub's settings also include categories for
things like Webhooks, GitHub Actions secrets and variables, and Actions policies. These exist for
specific technical needs, connecting other tools to your repository, automating tasks, controlling
what automated workflows are allowed to run. If a kit, tool, or another file in this training set
tells you to configure one of these for a specific purpose, follow that instruction. Otherwise,
leave them at whatever they were set to when the repository was created rather than experimenting
with settings you don't yet have a reason to change.

**Screenshot placeholder:** a repository's Settings page with the left sidebar visible, showing
the General, Access, and Danger Zone sections named in this file, so a reader can find them
without hunting.

---

## If it goes wrong

**I made a repository public and I meant to make it private (or the other way around).** Follow
the "Changing visibility later" steps above, they work in either direction. If it was briefly
public and held anything sensitive, treat that content as seen: rotate any secret it contained
(see the `.gitignore` section above) rather than assuming flipping it back to private undoes
anything.

**I committed a real password, key, or token by mistake.** Don't just delete the file in a new
commit, that leaves it sitting in every earlier commit. Rotate the secret first, immediately, in
whatever service issued it. That's the step that actually closes the hole. Full history cleanup
is a separate job to bring to the community, not a solo fix to attempt.

**I deleted a repository and I need it back.** Some deleted repositories can be restored within
90 days, but GitHub doesn't say all of them can. Act immediately and reach out to GitHub support
rather than assuming you have time to spare.

---

## Questions people ask here

**Can I share a private repository with just one contractor, without creating an organization?**
Yes. Add them as a collaborator on that specific repository, using the click path in the settings
section above. An organization is only worth setting up once several people need ongoing, shared
access to more than one repository; see the organizations file in this kit for that trigger.

**What's actually different between archiving and deleting?** Archiving keeps everything, makes
it read-only, and can be undone at any time. Deleting removes it, is described by GitHub as
something that "cannot be undone," and only "some" deleted repositories get a 90-day restore
window, not a guaranteed one. If you're unsure, archive.

**Does Claude Code need any special access to create a repository for me?** Only if you're using
the `gh repo create` path from the creation section above, and only in the sense that `gh` itself
needs to already be installed and signed in to your GitHub account before Claude Code can run it
on your behalf. If that's not already set up, use the browser path instead.

**I don't see "Internal" as a visibility option when I create a repository. Is something broken?**
No. Internal visibility only exists for organizations using GitHub Enterprise Cloud under an
enterprise account. On GitHub Free, which is where almost every small business starts, you'll
only ever see public and private, and that's expected.

**If my repository is private, does that mean absolutely nobody else can ever see it?** It means
nobody can see it except you, people you've explicitly given access to, and, for an organization
repository, certain organization members depending on that organization's own permission
settings (covered in the organizations file). It is not the same guarantee as "no other human
being anywhere could ever access it under any circumstance", that's a broader question about
GitHub's own trust and support practices that this file's research didn't confirm one way or the
other, so it isn't asserted here either way. What this file can confirm, directly from GitHub's
own wording, is the access boundary quoted at the top of the visibility section above.

---

## Sources

- https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
- https://cli.github.com/manual/gh_repo_create
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories
- https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository
- https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features
