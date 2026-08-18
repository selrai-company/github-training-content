# Repositories, and the public or private choice

## What this gets you

A repository is where one project's files live on GitHub: the code, the documents, and a
complete record of every change ever made to them. Creating one, and choosing whether it's
public or private, is the first real step in putting any project onto GitHub at all. Every
other file in this kit, branches, pull requests, issues, access, happens inside a repository
you've already created.

Get the visibility choice right at creation, private unless you deliberately want the whole
internet reading it, and you'll rarely think about it again. Get it wrong, especially by
committing a password or an API key into a public one, and it can be the single most expensive
mistake you make on GitHub. A leaked secret in a public repository isn't a "delete the file"
problem. It needs the credential rotated, immediately, in whatever service issued it, and this
file covers exactly why and how below.

## Before you start

**You need a GitHub account, signed in, with two-factor authentication turned on.**
`01-accounts-and-security.md` covers creating one.

**You do not need an organization to create a repository.** A personal account holds
repositories perfectly well on its own. If you already know several people need ongoing,
shared access to more than one repository, `02-organizations.md` covers whether that trigger
has actually been hit. Most solo owners haven't hit it yet, and nothing in this file requires
deciding that first.

**Decide, before you click Create, whether this repository should be public or private.** The
section below explains the difference in GitHub's own words. If you're not sure, this file's
practical default is private, covered under Strategy further down.

**The GitHub CLI (`gh`) path mentioned in this file is optional.** It only works if `gh` is
already installed and signed in to your GitHub account on your machine. Getting it authenticated
for the first time is its own one-time setup step and isn't covered here. If you haven't done
that yet, use the browser path throughout, it needs nothing extra.

## The words you need

**Repository.** GitHub's own words: "A repository is the most basic element of GitHub. It's a
place where you can store your code, your files, and each file's revision history." Think of it
like a shared project folder with a very good memory. A normal folder on your computer only
shows the current state of your files. A repository remembers every version that came before,
and lets you, or a teammate, look back at any of them.

**Commit.** One saved snapshot of your files at a specific point in time. Every commit is kept
forever as part of the repository's history, which is what lets you look back at any earlier
version later.

**Owner.** Who a repository belongs to when it's created: either your own personal account, or
an organization, if you've created one. You choose this on the creation screen, covered below.

**Visibility.** Whether a repository is public or private (a third option, internal, only
applies to certain organizations, also covered below). This is the single most consequential
choice you make when creating a repository, because it decides who can see everything inside
it, forever, until you deliberately change it.

**Collaborator.** A specific person you've given access to one of your repositories, added by
username, without making them part of an organization. Covered in full further down this file.

**Fork.** A separate copy of someone else's public repository, created under your own account,
that starts out linked to the original but is its own independent copy from that point on.

**README.** The file GitHub automatically displays on a repository's main page, right underneath
the file list, explaining what the project is and how to use it. Covered in its own section
below.

**`.gitignore`.** A file that tells Git which files to never track, so things like passwords and
API keys never get the chance to be committed in the first place. Covered in its own section
below.

**Danger Zone.** The section near the bottom of a repository's Settings page that holds its most
consequential actions: changing visibility, archiving, and deleting. Every one of them needs an
extra confirmation click, precisely because a mistake here can be hard to undo.

**Archiving.** Making a repository permanently read-only, for a finished project you want to
keep exactly as it is without the risk of an accidental edit. Reversible, unlike deleting,
covered in its own section below.

**Git LFS, and a GitHub Release.** Two different answers to "this file is too big." Git LFS
(Git Large File Storage) tracks a large file's changes over time, the same way a repository
tracks a normal file. A GitHub Release is for handing someone a large file to download once,
without tracking its changes at all. Both are covered briefly below. Neither is something most
small-business repositories need on day one.

**GitHub CLI (`gh`).** GitHub's own command-line tool. If it's installed and signed in on your
machine, Claude Code can carry out GitHub actions, like creating a repository, by typing a
command instead of clicking through the browser.

## How to do it

Most of this happens in your browser. A few steps have a genuinely faster path through Claude
Code, and each subsection below says so plainly when that's true, and just as plainly when it
isn't.

**Screenshot placeholder:** a repository's main page on github.com, showing the file list, the
README displayed underneath it, and the commit count near the top, so you can see what a
repository actually looks like before creating your own.

### Creating a repository

**Landmark:** any page on github.com, signed in.
**Path:** in the upper-right corner, click the **+** icon, then click **New repository**.
**Confirmation:** the "Create a new repository" form opens, with fields for Owner, Repository
name, Description, and visibility running down the page.
**Direct address**, since this exact screen looks the same for every signed-in reader:
`https://github.com/new`. Going there skips the click above.
**Fallback:** if the **+** icon isn't there at all, confirm you're signed in first, it only
appears once you are.

From there:

1. Choose the **Owner** (your personal account, or an organization if you've created one, see
   `02-organizations.md`).
2. Type a short, memorable **Repository name**.
3. Optionally add a **Description**.
4. Choose the repository's **visibility** (public or private). Read the next section before you
   click either one.
5. Toggle **Add a README file** on. There's more on why below.
6. Optionally add a `.gitignore` template and a license (this file's `.gitignore` section below
   covers `.gitignore` in more depth than the dropdown here does).
7. Click **Create repository**.

You'll know it worked because GitHub takes you straight to the new repository's own main page,
mostly empty apart from the README you just added.

**Screenshot placeholder:** the "Create a new repository" form, showing every field currently on
it, so you can match what you see to this list before you click Create.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in:** ask
Claude Code to run `gh repo create your-repo-name --public` or
`gh repo create your-repo-name --private`, adding `--clone` if you want it copied onto your
machine at the same time. This is a genuinely good shortcut once `gh` is set up, because the
command makes you type the visibility flag explicitly. There's no ambiguous radio button to
misread. If you haven't got `gh` installed and signed in yet, use the browser path above
instead.

### The choice that matters most: public or private

GitHub's own definitions, verbatim:

- **Public:** "Public repositories are accessible to everyone on the internet."
- **Private:** "Private repositories are only accessible to you, people you explicitly share
  access with, and, for organization repositories, certain organization members."

Read the public definition again. Not "anyone who knows the link." Not "anyone signed in to
GitHub." **Everyone on the internet**, with no account and no invitation needed. If you make a
repository public, assume a stranger can and eventually will find it, even if you never share
the link yourself.

There's a third visibility option, **internal**, but it only exists for organizations that use
GitHub Enterprise Cloud under an enterprise account. If you're on GitHub Free (which is where
almost every solo owner and small team starts, see `02-organizations.md` for what a new
organization lands on by default), you won't see it as an option, and that's expected, not a
bug.

**Do not assume which one is pre-selected on the creation form.** GitHub's own documentation
describes the field as "Choose a repository visibility" without stating which option is
pre-selected, and neither of GitHub's two published walkthroughs for creating a repository names
a default either. **Read your own screen at the moment you create the repository, and pick
deliberately.** Don't click through this step on autopilot.

**A practical default worth adopting for yourself, not GitHub's:** if you're not certain, start
private. You can make it public later if you decide to (the "Changing visibility later" section
below covers exactly what that changes). Going the other way, from public back to private,
doesn't undo whoever already saw or copied it while it was public.

**One private-repository nuance worth knowing.** The definition above says a private
organization repository is visible to "certain organization members," not just to people you've
explicitly invited. Exactly who that includes depends on your organization's own permission
settings, covered in `02-organizations.md` and `03-members-and-access.md`, not here. For a
private repository under your own personal account (not an organization), it's just you and
whoever you've explicitly added as a collaborator, covered later in this file.

**The one thing public is never the right answer for: sharing with your team.** If you want a
teammate, a contractor, or a client to see a repository, the correct move is to add them as a
collaborator (or, for an organization, give them access through the organization, see
`02-organizations.md` and `03-members-and-access.md`). Making the repository public "so they can
see it" also hands it to everyone else on the internet at the same time. There is no visibility
setting that means "just the people I've shared it with, plus anyone who happens to find it,"
only private (explicit access) and public (everyone).

### What belongs in a repository, and what doesn't

**Belongs:**

- Your actual project files (code, configuration, documents that are part of the project
  itself).
- A `README` file. GitHub's own recommendation: "we recommend that you create a README file for
  every repository." More on this below.
- A `.gitignore` file, so the things that shouldn't be tracked never get the chance to be.
  Covered in its own section below.
- Optionally, a `SECURITY.md` file, which GitHub describes as a file that "provides instructions
  to collaborators on how to report security vulnerabilities found in your project." Worth
  adding once you have collaborators, not urgent for a solo repository.

**Doesn't belong:**

- **Secrets.** Passwords, API keys, tokens, database credentials. None of these should ever be
  typed directly into a file that gets committed. The `.gitignore` section below is built
  specifically around keeping these out from the start.
- **Very large files.** GitHub's own stated limits: files over 100 MiB are blocked outright, a
  push that includes a file over 50 MiB triggers a warning (though it still goes through), and
  browser uploads are capped at 25 MiB. Beyond the hard limits, GitHub's own guidance on overall
  repository size is to keep it "ideally less than 1 GB, and less than 5 GB is strongly
  recommended," because smaller repositories are faster to clone and work with. For anything
  that genuinely needs to be large (a big design file, a database export), GitHub's own
  suggestion is Git Large File Storage (Git LFS), or, for distributing a large file to other
  people rather than tracking its changes, a GitHub Release, not a normal commit.
- **Personal files that have nothing to do with the project.** Not a GitHub rule, just good
  hygiene: a repository is easier to understand, for you and for anyone you share it with, when
  everything in it is actually part of the project.

### The README, and why it's worth writing

A README is the file GitHub shows automatically on a repository's main page, right underneath
the file list. GitHub's own framing of its purpose: it's there to "communicate important
information about your project," typically the first thing a visitor reads, explaining "what
the project does, why the project is useful, how users can get started with the project, and
where users can get help."

GitHub looks for a file named `README` (in one of a few common formats, `README.md` being the
usual choice) in three specific locations, checked in this order: the hidden `.github`
directory, then the repository's root directory, then a `docs` directory. Wherever it finds one
first, that's the one it displays. For almost every small-business repository, putting
`README.md` straight in the root directory (where you'd naturally expect it) is the simplest
choice and needs no special setup.

Keep it focused. GitHub's own guidance: "a README should only contain information necessary for
developers to get started using and contributing to your project," and anything longer belongs
in a wiki instead. For a small business repository, that usually means: one or two lines on what
this project is, and enough for you (or whoever inherits it later) to remember how to use it six
months from now, not a full manual.

**Screenshot placeholder:** a repository's main page with a short README rendered underneath the
file list, so you can see how plain text turns into a formatted page automatically.

### Keeping secrets out in the first place: `.gitignore`

A `.gitignore` file is, in GitHub's own words, "a file in your repository's root directory to
tell Git which files and directories to ignore when you make a commit." Anything listed in it
never gets tracked, never gets committed, and never ends up visible to anyone the repository is
shared with (or, if the repository is public, visible to the entire internet).

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
lines at the top of that block stop Git from ever tracking any file with that pattern. If you
add nothing else from this list, add those three lines, before your first commit, not after.

**The catch, and why "before" matters:** `.gitignore` only stops files it doesn't already know
about. GitHub's own guidance is direct about a file that's already been committed: "If you want
to ignore a file that is already checked in, you must untrack the file before you add a rule to
ignore it," using `git rm --cached FILENAME`. Untracking it removes it going forward, but it
does **not** erase it from your history. Every earlier commit that included it still holds a
copy.

**If a real secret has already been committed, the fix isn't deleting the file.** GitHub's own
first-step guidance, worded exactly like this: "if the sensitive data you need to remove is a
secret (e.g. password/token/credential)... as a first step you need to revoke and/or rotate that
secret." Rotate it in whatever service issued it (get a new key, invalidate the old one)
immediately. That single step removes the danger, because the leaked value stops working the
moment it's rotated, regardless of how many places it's still sitting in your history. Cleaning
the committed value out of your repository's history after that is a real but separate job, one
this kit deliberately does not walk you through solo: bring it to the community rather than
attempting a history rewrite yourself, because a botched one can cause more damage than the
leaked secret did. Rotating the secret is the part that actually closes the hole. Treat the
history cleanup as optional tidying after that, not the urgent step.

### Changing visibility later, and what that actually exposes

You can flip a repository between public and private at any time, if you have the right
permissions (an organization can restrict this to organization owners only). The click path is
the same for either direction.

**Landmark:** open the repository's main page.
**Path:** click **Settings**.
**Confirmation:** the repository's own Settings page opens, General settings shown first, with a
list of setting groups down the left-hand side.
For any repository you administer, the direct pattern is
`https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings` (use your own personal account
name in place of `YOUR-ORGANISATION` if it isn't under an organization).
**Fallback:** if there's no **Settings** tab at all, you most likely don't have admin access to
this specific repository. `03-members-and-access.md` covers checking your access level.

From Settings:

1. Scroll to the **Danger Zone**.
2. Click **Change visibility**.
3. Select the visibility you want.
4. Confirm you're changing the correct repository, click **I have read and understand these
   effects**.
5. Click **Make this repository public** or **Make this repository private**, whichever
   applies.

**Going private to public exposes exactly what you'd expect, stated by GitHub itself:** the code
becomes visible to everyone who can visit GitHub.com, all push rulesets on the repository are
disabled, and Actions history and logs become visible to everyone too. Once something has been
public, even briefly, treat it the same way this file treats a leaked secret above: assume it
may already have been seen or copied, and flipping back to private does not undo that.

**Going public to private has its own side effects, also stated by GitHub itself:** stars and
watchers on the repository are erased (this affects how the repository ranks in GitHub's own
listings), any GitHub Pages site published from it is unpublished, and existing forks stay
public and get detached from your repository rather than turning private with it. If other
people had already forked your public repository, making the original private does not make
their copies private too.

Both directions also erase the repository's stars and watchers. Neither direction is reversible
in the sense of undoing what already happened while the old setting was live. It only changes
what happens going forward.

### Archiving a repository

Archiving is for a project that's finished, but that you want to keep around exactly as it is,
without the risk of an accidental edit. GitHub's own description of what it does: it makes the
repository "read-only for all users and indicate[s] that it's no longer actively maintained."
Once archived, its "issues, pull requests, code, labels, milestones, projects, wiki, releases,
commits, tags, branches, reactions... comments and permissions become read-only."

**Landmark:** open the repository's main page.
**Path:** click **Settings**, then scroll to the **Danger Zone**, then click **Archive this
repository**.
**Confirmation:** GitHub shows a page of warnings about what archiving does before letting you
proceed.
Same direct pattern as above: `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings`.

1. Read the warnings on screen.
2. Type the repository's name to confirm.
3. Click **I understand the consequences, archive this repository**.

You'll know it worked because the repository's main page now shows a banner stating it's been
archived, and every action inside it, editing, commenting, merging, is disabled.

You can reverse this. From the same **Danger Zone**, click **Unarchive this repository**, review
the warnings, type the repository's name to confirm, and click **I understand the consequences,
unarchive this repository**.

**Screenshot placeholder:** an archived repository's main page, showing the "This repository has
been archived" banner GitHub displays, so you know what it looks like from the outside.

### Deleting a repository

Different from archiving: deletion removes the repository, not just makes it read-only. GitHub's
own wording is blunt: "Deleting a repository will permanently delete team permissions. This
action cannot be undone." For a private repository specifically, deleting it also deletes every
fork of it. Public repository forks are preserved even after the original is deleted.

**You need admin access to the specific repository, or owner privileges on the organization it
belongs to, to delete it.** This isn't a button every collaborator can see.

**Landmark:** open the repository's main page.
**Path:** click **Settings**, then, on the General settings page, scroll to the **Danger Zone**.
**Confirmation:** the Danger Zone lists **Delete this repository** as its last, most prominent
option.
Same direct pattern: `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings`.
**Fallback:** if you don't see this option, or clicking it does nothing, you don't have the
admin access needed. Ask whoever administers the repository, or the organization's owners, to do
it, or to grant you that access first.

1. Click **Delete this repository**.
2. Click **I want to delete this repository**.
3. Click **I have read and understand these effects**.
4. Type the repository's name in the text box.
5. Click **Delete this repository**.

**One partial safety net, worded carefully because GitHub words it carefully:** GitHub's own
documentation says "some deleted repositories can be restored within 90 days of deletion," not
every deleted repository. Don't treat that window as a guarantee for your specific case. If you
think you deleted something by mistake, act immediately and contact GitHub support rather than
assuming the 90 days definitely covers you.

**In practice:** if you're not certain you'll never need a repository again, archive it instead
of deleting it. Archiving costs you nothing but a little clutter, and it can be undone with
certainty. Deletion cannot.

### Repository settings worth a look, and the ones to leave alone

**Worth knowing about:**

- **General settings and the Danger Zone**, covered above: rename, transfer (see
  `02-organizations.md`), change visibility, archive, delete.
- **Access, then Collaborators**, for a repository under your own personal account (not an
  organization). This is the correct way to share a private repository with one or a few
  specific people, not making it public.

  **Landmark:** open the repository's Settings page (the same one covered above).
  **Path:** in the left sidebar, under **Access**, click **Collaborators**, then click **Add
  people**.
  **Confirmation:** a search box appears where you can look up the person by username, full
  name, or email.
  1. Search for and select the person.
  2. Choose what they're allowed to do, GitHub's own screen lists the options here directly.
     Read that part rather than accepting a default without looking.
  3. Confirm the invite.

  They'll get an invitation to accept before their access actually starts.
- **Features**, a toggle list for things like Issues, Wikis, and Discussions. Turn on what you
  actually plan to use, leave the rest off rather than guessing you might need it later.

**Leave alone unless you have a specific reason:** GitHub's settings also include categories for
things like Webhooks, GitHub Actions secrets and variables, and Actions policies. These exist
for specific technical needs, connecting other tools to your repository, automating tasks,
controlling what automated workflows are allowed to run. If a kit, tool, or another file in this
training set tells you to configure one of these for a specific purpose, follow that
instruction. Otherwise, leave them at whatever they were set to when the repository was created
rather than experimenting with settings you don't yet have a reason to change.

**Screenshot placeholder:** a repository's Settings page with the left sidebar visible, showing
the General, Access, and Danger Zone sections named in this file, so you can find them without
hunting.

## Strategy: how to actually use this

**A solo operator** creates every repository private by default and rarely thinks about it
again. There's nobody to add as a collaborator yet, so most of this file's settings section
doesn't apply to you. The one habit worth keeping regardless of team size: README and
`.gitignore`, every single repository, before the first real file goes in. It costs nothing
solo, and it's already in place the day someone else needs to join.

**A team of four**, one or two of them technical, is where the repository-level decisions in
this file start compounding. Adding each person as a collaborator to each repository they need,
one by one, still works fine at this size, but it's already the point where forgetting to add
someone to a new repository, or forgetting to remove a contractor once their work is done,
becomes a real, if small, risk instead of a hypothetical one. This is close to the size where an
organization (`02-organizations.md`) starts paying for itself: access lives in one place instead
of scattered across every repository's own Collaborators list.

**The decision rule for public or private: default to private, every time.** Almost no
small-business repository needs to be public. Go public only for a specific, deliberate reason,
an open-source tool you genuinely want outside contributions on, or a project where the code
itself is meant to be seen by strangers. "So a client can see it" is never that reason. A
collaborator invite does the same job without handing the repository to the entire internet.

**What would change my mind about staying private:** genuinely wanting people who are not your
team to be able to see and propose changes to the code itself. That's a real, specific use for
public. Wanting a repository to "look more professional" or "look active" is not, and it costs
you the one thing private buys for free: nobody stumbling across a mistake before you've had the
chance to fix it.

**Archive versus delete, the actual rule:** archive by default. It costs nothing but a slightly
longer repository list, and it's fully reversible. Reach for delete only when you're genuinely
certain that nothing in that repository, no history, no old issue, no old branch, will ever be
worth looking back at. If there's any doubt at all, that doubt is the answer: archive it instead.

**What good looks like months later:** every active repository still has the README and
`.gitignore` it started with, not added later after a scare. No repository was ever made public
"so someone could see it", that should be a permanent count of zero. If a secret was ever
committed by mistake, it happened once, was rotated within the hour, and became a permanent
`.gitignore` rule afterward, not a repeat incident. Finished projects sit archived, not deleted
and not cluttering the active list either.

## A worked example

A café owner's nephew builds and maintains her online ordering site. This is the same team of
three, the café owner, her nephew, and a staff member, described throughout this kit's strategy
pack.

Before he writes a single line of the ordering site, the nephew creates a new repository under
his own personal account (the business hasn't set up an organization yet, since there's no
second person needing ongoing push access at this point). He types `ordering-site` as the name,
leaves the description blank, and picks private. The site will eventually hold a connection to
the café's payment provider, and there's no reason for that to be visible to a stranger before
it's even launched. He toggles on **Add a README file**, and before writing anything else,
creates a `.gitignore` in the repository's root with the `.env` lines from this file's starting
template already in it.

A few weeks in, he needs to test the payment provider's connection, which means using a real
test API key while he develops. He drops it into a local `.env` file on his own machine rather
than typing it anywhere near the actual code, exactly the pattern the `.gitignore` is there to
protect. Because `.env` was already ignored before his first commit, the key never gets the
chance to end up in the repository's history at all.

The site launches. Months later, the café takes on a bookkeeper who needs to see the ordering
numbers but has no reason to touch the code. The owner doesn't make the repository public to
give her that access, that would hand the payment logic to the entire internet along with it.
She adds the bookkeeper as a collaborator instead, with the narrowest access that lets her see
what she needs.

Separately, an early test repository the nephew made while first learning GitHub, `menu-test`,
hasn't been touched in a year. He's not certain he'll never want to look back at how he
originally structured it, so he archives it rather than deleting it. It drops out of his active
list, becomes fully read-only, and stays recoverable if he ever wants it again.

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

**I added a file to `.gitignore`, but Git is still tracking changes to it.** `.gitignore` only
stops files Git doesn't already know about. If the file was committed before you added the rule,
untrack it first with `git rm --cached FILENAME`, then commit that change. That stops it being
tracked going forward, it does not remove it from earlier commits, see the note on real secrets
above if the file held one.

**I don't see a Settings tab, or the Danger Zone options, on a repository I expect to
administer.** You most likely don't have admin access to that specific repository.
`03-members-and-access.md` covers checking your access level, and who can grant you a higher
one.

**I deleted a repository and I need it back.** Some deleted repositories can be restored within
90 days, but GitHub doesn't say all of them can. Act immediately and reach out to GitHub support
rather than assuming you have time to spare.

## FAQ

**Can I share a private repository with just one contractor, without creating an organization?**
Yes. Add them as a collaborator on that specific repository, using the click path in the
settings section above. An organization is only worth setting up once several people need
ongoing, shared access to more than one repository, see `02-organizations.md` for that trigger.

**What's actually different between archiving and deleting?** Archiving keeps everything, makes
it read-only, and can be undone at any time. Deleting removes it, is described by GitHub as
something that "cannot be undone," and only "some" deleted repositories get a 90-day restore
window, not a guaranteed one. If you're unsure, archive.

**Does Claude Code need any special access to create a repository for me?** Only if you're using
the `gh repo create` path from the creation section above, and only in the sense that `gh`
itself needs to already be installed and signed in to your GitHub account before Claude Code can
run it on your behalf. If that's not already set up, use the browser path instead.

**I don't see "Internal" as a visibility option when I create a repository. Is something
broken?** No. Internal visibility only exists for organizations using GitHub Enterprise Cloud
under an enterprise account. On GitHub Free, which is where almost every small business starts,
you'll only ever see public and private, and that's expected.

**If my repository is private, does that mean absolutely nobody else can ever see it?** It means
nobody can see it except you, people you've explicitly given access to, and, for an organization
repository, certain organization members depending on that organization's own permission
settings (covered in `02-organizations.md` and `03-members-and-access.md`). It is not the same
guarantee as "no other human being anywhere could ever access it under any circumstance," that's
a broader question about GitHub's own trust and support practices that this file's research
didn't confirm one way or the other, so it isn't asserted here either way. What this file can
confirm, directly from GitHub's own wording, is the access boundary quoted earlier in the
visibility section.

**Can I move a repository from my personal account into an organization later, without
recreating it?** Yes. GitHub calls this a transfer, and it moves the repository's history,
issues, and pull requests with it, rather than starting fresh. `02-organizations.md` covers the
steps in full, including the access you need to do it.

**Do I need to think about Git LFS or GitHub Releases when I first create a repository?** No.
Both only matter once you actually have a specific large file to deal with, covered in "What
belongs in a repository, and what doesn't" above. Nothing about creating a repository requires a
decision about either one up front.

## Quick reference

- **Create (browser):** **+** icon (top right) or `https://github.com/new`, pick Owner, name,
  and visibility, toggle **Add a README file**, **Create repository**
- **Create (Claude Code):** `gh repo create your-repo-name --public` (or `--private`), add
  `--clone` to copy it locally
- **Public means:** everyone on the internet, no account or invitation needed
- **Private means:** you, plus whoever you explicitly add
- **Practical default if unsure:** private
- **`.gitignore` starter:** block `.env`, `.env.local`, `.env.*.local` before your first commit
- **If a secret leaks:** rotate it immediately in whatever service issued it, then treat history
  cleanup as a separate job, not a solo one
- **Change visibility:** repository **Settings**, **Danger Zone**, **Change visibility**
- **Archive (reversible):** repository **Settings**, **Danger Zone**, **Archive this
  repository**
- **Delete (not reversible, needs admin access):** repository **Settings**, **Danger Zone**,
  **Delete this repository**
- **Add a collaborator:** repository **Settings**, **Access**, **Collaborators**, **Add people**

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
