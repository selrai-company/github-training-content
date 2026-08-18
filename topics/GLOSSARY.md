# Glossary

This is the one place in this kit where a word gets defined properly. If you hit a term you do
not know while reading another file, come here first.

Every entry has the same shape: the term, one plain sentence that answers the question on its
own, a few more lines of what it actually means in practice, and a "Not to be confused with"
line wherever two terms get mixed up often, because that mix-up is usually the actual source of
confusion, not the word itself. Each entry also points you to the topic file that covers it
properly, with the full click path.

Terms are in alphabetical order. Use your browser's find function (Ctrl+F or Cmd+F) if you know
roughly what you are looking for and do not want to scroll.

---

## A

**Action.** One ready-made, packaged step that someone else has already written, that a
workflow can reuse instead of the instruction being typed out by hand.

This is the confusing one, because the whole feature is also called "GitHub Actions." Think of
"an action" as one ingredient, and "GitHub Actions" as the kitchen the ingredient gets used in.
Actions are published in a catalogue GitHub calls the Marketplace. Adding someone else's action
to a workflow gives it real access to your repository, including any secrets stored on it, so
this kit treats picking one as a genuine decision, not a routine step.

Not to be confused with: **GitHub Actions**, the whole feature, or a **workflow**, the file that
uses one or more actions.

More detail: `18-automation-basics.md`.

**Alert.** GitHub's word for the notice it raises when a security feature finds something worth
your attention.

Every alert this kit covers, whether from secret scanning, push protection, or Dependabot,
lands in the same place: your repository's **Security and quality** tab. An alert is
information, not a deadline. Reading it, and knowing whether a fix already exists, is what
decides what you do next.

More detail: `19-security-features.md`.

**Approve.** The choice a reviewer makes on a pull request to say the proposed change is good
to merge.

You cannot approve your own pull request, that is a real GitHub rule. As the owner of your own
repository you can still merge your own work without an approval; you just will not see your
own name listed as an approving reviewer, and that is expected.

Not to be confused with: leaving a plain **Comment** on a pull request, which does not approve
or block anything, or **Request changes**, which flags a problem but only blocks a merge if the
repository specifically requires an approval first.

More detail: `07-pull-requests.md`.

**Asset.** A file attached to a release, sitting alongside the automatic source code archive
GitHub adds for you.

Each asset must be under 2 GiB (roughly 2,000 megabytes), and a release can hold up to 1,000 of
them. GitHub always adds a zip file and a tarball of your repository's contents automatically;
an asset is anything you add on top of that yourself.

More detail: `17-releases-and-versions.md`.

**Assignee.** The person, or people, marked as responsible for an issue or a pull request.

You can assign up to 10 people to one issue or pull request. Someone can only be assigned if
they already have access to the repository, or have already left a comment on that specific
issue.

More detail: `13-issues-and-tracking-work.md`.

**Authenticator app (TOTP).** A phone or desktop app that generates a fresh six-digit code every
30 seconds, used as your second proof when signing in with two-factor authentication.

TOTP stands for "time-based one-time password," a technical name for a code that changes every
half minute. GitHub recommends this over SMS as your second factor, because it does not depend
on phone signal and cannot be intercepted the way a text message can.

Not to be confused with: an **SMS code**, GitHub's weaker alternative second-factor method.

More detail: `01-accounts-and-security.md`.

## B

**Base permission.** The organisation-wide default access level applied to every member,
across every repository the organisation owns, unless something more specific overrides it.

There are four levels: No permission, Read, Write, and Admin. The trap worth knowing: setting
this to Write "so nobody has to be added repository by repository" quietly gives every current
and future member push access to everything the organisation owns. Most small teams should
leave this at Read or No permission and grant Write on individual repositories instead.

Not to be confused with: a **repository role**, which is set per person, per repository, and can
sit higher than the base permission without being pulled back down by it.

More detail: `03-members-and-access.md`.

**Billing manager.** An organisation-level role that can manage payment details and billing
settings, but cannot see or touch any code.

Most small businesses will not need this role; it exists for larger organisations that want
billing handled by someone who is not also a repository administrator.

More detail: `03-members-and-access.md`.

**Blame (the Blame view).** A way of looking at one file where every line is shown next to the
commit that last changed it, so you can see who wrote a specific line, and when.

Open a file, click **Blame** (or press the `b` key), and read the commit message next to any
line for the full detail, including the reasoning if whoever made the change wrote one. One
catch: if a file was ever reformatted in one big tidy-up commit, every line can end up crediting
that tidy-up rather than the change that actually put the words there.

Not to be confused with: a **file's history**, which shows every commit that ever touched a
file, in order, rather than showing you line by line.

More detail: `15-finding-things.md`.

**Branch.** A private, working copy of your repository's files that lets you make changes
without touching the version everyone else relies on.

A branch starts as an exact copy of whichever branch it was made from, usually your default
branch. Nothing you do on it affects anyone else until you deliberately bring it back in,
normally through a pull request. If your changes do not work out, you can stop using the branch
and leave it alone; the main copy was never touched.

Not to be confused with: a **fork**, which is a whole separate repository under your own
account, used when you do not already have Write access to the original.

More detail: `06-branches.md`.

**Branch protection rule.** An older GitHub mechanism that stops people pushing directly to an
important branch, and can require a pull request and a review before a change is allowed to
land.

Only one branch protection rule can apply to a branch at a time. This kit recommends its
newer replacement, a **ruleset**, as the one to reach for today, though branch protection rules
are still fully documented and supported. On a private repository, either mechanism needs at
least GitHub Pro (for a personal account) or GitHub Team and above (for an organisation); on a
public repository, both are free on every plan.

Not to be confused with: a **ruleset**, the newer mechanism that can apply more than one rule to
the same branch at once, and that anyone with Read access can see is active, not just
administrators.

More detail: `10-protecting-your-work.md`.

**Breadcrumb trail.** The row of clickable folder names across the top of a repository page,
showing the path to where you currently are.

Click an earlier part of the trail to jump back several folders in one click, instead of
clicking a browser Back button repeatedly.

More detail: `15-finding-things.md`.

## C

**Check.** The pass or fail result a workflow leaves behind, most often seen directly on a pull
request before anyone approves it.

A green tick means it succeeded; a red cross means it failed. This kit's advice: do not approve
or merge a pull request showing a failed check without asking whoever set the automation up what
it means, the same way you would not wave through an inspection you knew had failed.

More detail: `18-automation-basics.md`.

**Clone.** A full copy of a repository, including its entire commit history, that stays
connected to GitHub so you can pull down new changes later without downloading everything again.

You need at least Read access to clone something. A clone is different from a plain ZIP
download: a ZIP is a one-time snapshot with no history and no way to update it in place.

Not to be confused with: downloading a repository as a **ZIP file**, which has no history and
cannot be updated, only re-downloaded.

More detail: `05-daily-workflow.md`.

**CODEOWNERS.** A file you can add to a repository that names specific people, or teams, as
responsible for specific files or folders, so GitHub can automatically ask them to review a
pull request that touches those paths.

This file is referenced in a few places in this kit without ever being explained, so here it is
properly. GitHub's "Require review from Code Owners" setting, covered in
`10-protecting-your-work.md`, only does anything once a CODEOWNERS file exists naming who owns
what. Most small repositories in this kit's audience will not have set one up, and this kit does
not walk through writing one. If you rename your GitHub username, any CODEOWNERS file that
mentions your old username has to be updated by hand, it does not update itself. This kit could
not confirm the exact file name spelling rules or every folder GitHub looks in for this file from
its own documentation this session, so confirm the exact syntax on GitHub's own documentation, or
ask a technical teammate, before relying on one.

Not to be confused with: a **draft pull request**, where GitHub's own wording is that "code
owners are not automatically requested to review" it, even if a CODEOWNERS file exists.

More detail: `10-protecting-your-work.md`.

**Command Palette.** A single search box, opened with Ctrl+K (Windows and Linux) or Cmd+K (Mac)
from anywhere on GitHub, that lets you jump to a repository, a file, or an issue, or run an
action, without navigating any menu first.

More detail: `15-finding-things.md`.

**Commit.** A saved snapshot of a change, with its own unique ID, a timestamp, and the name of
whoever made it.

Once something is committed, that snapshot becomes permanent history. You can always come back
and see exactly what a file looked like at that point. A commit made on your own machine stays
only on your machine until it is pushed.

Not to be confused with: a **push**, the separate step that sends a commit you have already made
up to GitHub.

More detail: `05-daily-workflow.md`.

**Commit message.** The short piece of text, written at the moment you commit, that says what
the change actually did and why.

GitHub requires you to write something here, but does not enforce a length or format. This
kit's own recommendation: write it for the version of you, or a teammate, reading it six months
from now with no memory of today. "Fixed it" tells that person nothing; "corrected Saturday
opening hours" tells them everything.

More detail: `05-daily-workflow.md`.

**Conflict markers.** The three lines of symbols git inserts into a file to show you exactly
where two branches changed the same part of the same file in two different ways.

They look like `<<<<<<<`, `=======`, and `>>>>>>>`. Everything between the first and the middle
line is one version; everything between the middle and the last line is the other. You resolve
a conflict by deleting all three marker lines and deciding what the file should actually say.

More detail: `08-merge-conflicts.md`.

## D

**Default branch.** The one branch GitHub treats as the "main" branch of a repository, the
branch people see first when they visit it, and the branch a new branch copies from unless told
otherwise.

New repositories name this branch `main`. If you see a repository with a branch called `master`
instead, that is just an older repository from before GitHub's current naming convention; it
behaves exactly the same way.

Not to be confused with: **main**, which is only the name GitHub gives the default branch on a
new repository, not a separate concept.

More detail: `06-branches.md`.

**Dependabot.** GitHub's built-in tool that checks the outside software your project relies on
against a list of known security problems, and can tell you, or fix it for you, when one of
them has a hole in it.

It runs on top of two separate switches: **Dependabot alerts** (which notify you) and
**Dependabot security updates** (which goes further and opens a pull request with the fix).
Dependabot alerts are a free GitHub feature on every plan.

More detail: `19-security-features.md`.

**Dependabot alert.** A notice that one of your project's dependencies has a known security
problem.

An alert tells you which file is affected, how serious GitHub considers the problem, and
whether a fixed version already exists. If a fixed version exists, updating to it is usually the
whole answer.

More detail: `19-security-features.md`.

**Dependabot security update.** A feature that goes one step further than an alert: instead of
only telling you a problem exists, it opens a pull request that already contains the fix.

Treat that pull request like any other pull request, not something to merge on sight; a
dependency update can occasionally change other behaviour, not only patch the security hole.

More detail: `19-security-features.md`.

**Dependency.** A piece of software your project uses that someone else wrote and maintains,
rather than code you wrote yourself.

A website built with a shopping-cart library, or a script using a PDF-generating package, are
both relying on dependencies.

More detail: `19-security-features.md`.

**Dependency graph.** GitHub's internal map of every dependency your repository uses, and every
dependency those dependencies use in turn.

This is what Dependabot alerts are built on top of.

More detail: `19-security-features.md`.

**Draft pull request.** A pull request marked as not ready to be reviewed or merged yet.

Since 1 May 2025, draft pull requests are free on every GitHub plan, in public and private
repositories alike; older guides that say otherwise are out of date. Use one to start a
conversation, or back your work up on GitHub, before it is actually finished. Nobody can merge
it until you click **Ready for review**.

Not to be confused with: a **draft release**, a different feature that hides an unfinished
release rather than an unfinished pull request.

More detail: `07-pull-requests.md`.

**Draft release.** A release you have started but not yet published.

Nobody with only Read access to your repository can see a draft release. It is safe to leave one
half-finished while you gather everything that belongs in it, then click **Publish release**
when it is ready.

Not to be confused with: a **draft pull request**, a different feature that marks a proposed
code change as not ready for review.

More detail: `17-releases-and-versions.md`.

## E

**Event.** See **Trigger**.

## F

**Fetch.** The step where git downloads the latest information from somewhere else, usually the
repository you originally forked or cloned from, without changing any of your own files yet.

Fetching is one part of syncing a fork back up to date; the rest is comparing what came in
against your own work and merging the two. Claude Code can run this whole sequence for you from
a plain-English request, so you do not need to run the fetch step by hand.

Not to be confused with: **pull**, which fetches new changes and immediately merges them into
your current branch in one step.

More detail: `09-forks-and-contributing.md`.

**Fork.** Your own personal, separate copy of somebody else's repository, sitting under your own
account, with its own settings and its own permissions.

You can fork any public repository you can see, no Write access to the original needed. Once it
is yours, you do not need anyone's permission to change it. Proposing your changes back to the
original, through a pull request, is a separate step; merging that pull request is a decision
that belongs to whoever has Write access on the original repository, not to you.

Not to be confused with: a **branch**, which lives inside the same repository you already have
Write access to, rather than being a whole separate repository under your own account.

More detail: `09-forks-and-contributing.md`.

## G

**Gist.** A separate, smaller GitHub feature for sharing a snippet of text or code, similar in
spirit to a tiny one-file repository with its own shareable link.

This kit does not teach gists in depth. They come up mainly in two places worth knowing: your
profile page can pin up to six repositories and gists combined, and renaming your GitHub username
changes the links to any gist you own, so an old shared link can stop working afterwards.

More detail: this kit does not have a dedicated file on gists; the closest coverage is the
username-change consequences in `01-accounts-and-security.md`, and pinning in `15-finding-things.md`.

**GitHub Actions.** GitHub's built-in automation feature: instructions that run by themselves
the moment something specific happens in your repository, whether or not anyone is at a
computer.

GitHub's own description: "a continuous integration and continuous delivery (CI/CD) platform
that allows you to automate your build, test, and deployment pipeline." Most people using this
kit will never need to write one of these from scratch; the skill worth having is recognising
one, reading it well enough to know roughly what it does, and knowing how to turn it off.

Not to be confused with: an **action**, one single reusable ingredient a workflow can use, as
opposed to the whole feature.

More detail: `18-automation-basics.md`.

**GitHub Advisory Database.** GitHub's own running list of known security problems in publicly
available software packages, reviewed by GitHub staff before they count as confirmed.

This is where Dependabot alerts come from.

More detail: `19-security-features.md`.

**GitHub App manager.** An organisation-level role that lets someone manage the settings of
GitHub App connections without needing full organisation-owner access.

By default only organisation owners can do this; this role is how an owner can hand off just
that one slice of control.

More detail: `03-members-and-access.md`.

**GitHub CLI (`gh`).** GitHub's own command-line tool. It is what Claude Code uses, once
installed and signed in on your machine, to do GitHub tasks like cloning, pushing, creating
pull requests, or making releases from a plain-English request instead of a browser click path.

Signing in through the GitHub CLI's browser-based flow is GitHub's own recommended way to
connect a machine to your account, safer than a personal access token because it never shows
you a long string of characters that could end up somewhere it should not.

Not to be confused with: **Claude Code**, the assistant that runs `gh` commands on your behalf
once it is set up; `gh` is GitHub's tool, Claude Code is the one operating it for you.

More detail: `11-github-with-claude-code.md`.

**GitHub Flavored Markdown.** GitHub's own name for the version of Markdown it supports:
standard Markdown, plus a handful of GitHub-specific extras layered on top, like mentioning a
person with `@` and linking straight to an issue by typing its number.

More detail: `14-markdown-and-writing.md`.

**GitHub Pages.** A feature that can publish a simple website straight from the contents of a
repository.

This kit does not walk through setting one up. The one place it comes up directly in this kit:
if a repository with a published GitHub Pages site is switched from public to private, that site
gets unpublished as part of the change. Confirm the setup steps on GitHub's own documentation if
you want to use this feature.

More detail: the visibility-change side effect is covered in `04-repositories-and-visibility.md`
and `12-when-things-go-wrong.md`.

**.gitignore.** A file you add to your repository's root directory, named exactly `.gitignore`,
that tells git which files and folders to never track or commit.

This is your main defence against accidentally committing a secret. It only stops files it does
not already know about: a file already committed needs to be deliberately untracked first, and
even then it is not erased from earlier commits. `04-repositories-and-visibility.md` has a
ready-to-paste starting file.

More detail: `04-repositories-and-visibility.md`.

**Git versus GitHub.** Git is the underlying version-control tool that tracks changes to files
and their history. GitHub is a website and service built on top of git that hosts your
repositories, and adds the parts git itself does not have: pull requests, issues,
organisations, GitHub Actions, and everything else covered across this kit.

You will rarely need to know this distinction to use this kit, since the browser and Claude Code
both handle the underlying git commands for you. It matters mainly so a sentence like "run `git
pull`" and a sentence like "open a pull request on GitHub" do not sound like the same kind of
thing when they are not: one is the plumbing, the other is a feature GitHub itself built.

More detail: git commands appearing throughout this kit are always run for you, by the browser
or by Claude Code as described in `05-daily-workflow.md` and `11-github-with-claude-code.md`.

## H

**History.** The full, ordered record of every commit that has ever happened, either across a
whole repository or for one specific file.

A repository's full history and one file's history are different views: a file's history shows
only the commits that changed that particular file, while the repository's history shows
everything, across every file.

Not to be confused with: **Blame**, which shows you the file's current content line by line,
each line credited to the commit that last touched it, rather than a list of commits over time.

More detail: `15-finding-things.md`.

## I

**Issue.** A numbered note, with a title, a description, and a comment thread, attached to one
repository, used to track something that needs doing or something that is broken.

Anyone with Read access can open one. It stays a searchable record forever, unlike a message in
a chat app, so six months later you can still find out exactly what was asked for, who did it,
and how it was closed.

Not to be confused with: a **pull request**, which proposes an actual code or file change; an
issue only describes work, it does not contain the change itself.

More detail: `13-issues-and-tracking-work.md`.

**Issue template.** A pre-written starting point that asks the same set of questions every time
someone opens a new issue of a particular kind, such as a bug report.

More detail: `13-issues-and-tracking-work.md`.

## J

**Job.** One task inside a workflow, made up of one or more steps, all run on the same runner.

A workflow can have one job or several.

More detail: `18-automation-basics.md`.

## L

**Label.** A short, coloured tag attached to an issue to sort it into a category, like `bug` or
`question`.

Every new repository starts with ten labels already created. Applying one needs Triage access
or higher; creating a brand new label needs Write access.

More detail: `13-issues-and-tracking-work.md`.

## M

**Main.** See **Default branch**.

**Markdown.** Plain text with a small set of marks around it, like `**this**` or `# this`, that
GitHub turns into formatting (bold text, headings, lists) the moment it displays your writing.

You always type the plain marks; GitHub does the formatting. It works the same everywhere on
GitHub you can type: a comment, an issue, a pull request description, or a file ending in `.md`.

Not to be confused with: **GitHub Flavored Markdown**, GitHub's specific version of Markdown
with a few extra features layered on top.

More detail: `14-markdown-and-writing.md`.

**Member.** The default, non-administrative role for someone belonging to an organisation.

A member does not automatically get billing access or control over other people's access; that
belongs to an organisation owner. What repositories a member can actually open and change
depends on the organisation's base permission plus whatever has been granted on individual
repositories or through a team.

Not to be confused with: an **outside collaborator**, someone who has access to one or more of
an organisation's repositories without being a member of the organisation itself.

More detail: `03-members-and-access.md`.

**Merge.** The act of folding a branch's changes into another branch, usually your default
branch, so everyone sees them.

Merging is what a pull request is building toward. Nothing on a branch reaches your main copy
until a merge deliberately happens.

More detail: `07-pull-requests.md`.

**Merge commit.** One of the three ways to merge a pull request, and the one GitHub itself
documents as the default option. Every commit from the branch lands in the main copy
individually, plus one extra commit recording the merge itself.

This kit recommends **squash and merge** instead as its own preference for most small
businesses, but that is this kit's recommendation, not GitHub's default; the merge commit is
GitHub's documented default, and it is always available with nothing extra to turn on.

Not to be confused with: **squash and merge** (all of a branch's commits become one single
commit) and **rebase and merge** (the branch's original commits are replayed onto the main copy
with no extra merge commit added).

More detail: `07-pull-requests.md`.

**Merge conflict.** The moment git cannot automatically combine two branches, because the same
part of the same file was changed two different ways on each one, and stops to ask a person to
decide.

This is git asking a question, not an error you caused. Most changes merge automatically without
you ever seeing this; it only happens when two people's changes genuinely overlap on the same
lines.

More detail: `08-merge-conflicts.md`.

**Milestone.** A named group of issues and pull requests tracked together, usually because they
belong to the same piece of work or the same date.

A milestone's page shows how many of its issues are still open, and a completion percentage
worked out automatically.

More detail: `13-issues-and-tracking-work.md`.

**Moderator.** An organisation-level role that, on top of the normal member permissions, can
block or unblock non-member contributors, set interaction limits, and hide comments on public
repositories owned by the organisation.

Mostly relevant if your organisation has public repositories with open discussion; a small
private-repository team usually does not need this role.

More detail: `03-members-and-access.md`.

## N

**Notification.** An update GitHub sends because something happened that you are subscribed to,
either through deliberately watching a repository or automatically, because you were mentioned,
assigned, or asked to review something.

Notifications reach you in two places: your notifications inbox on GitHub, and, if switched on,
email. Each notification carries a reason label telling you in a word or two why you received
it.

More detail: `16-notifications.md`.

## O

**Organization.** A separate, shared account that sits above individual personal accounts, so a
group of people can collaborate across repositories without one person's own account holding
everything.

Nobody signs in to an organisation directly; people sign in with their own personal account and
are given access to the organisation. A new organisation is created on GitHub Free at no cost.
The one real signal you need one: a second person needs ongoing access to your repositories that
should keep working even if you are unavailable to grant it repo by repo.

Not to be confused with: a **team**, a smaller group inside an organisation used to grant the
same access to several people at once.

More detail: `02-organizations.md`.

**Origin.** The conventional name git and the GitHub CLI give to the connection back to the
repository you cloned or forked from, so later commands know where to push to or pull from
without you retyping the address each time.

You will rarely need to type this name yourself; the browser and Claude Code both handle it for
you.

Not to be confused with: **upstream**, GitHub's own name specifically for the repository a fork
was made from, which is a related but separate idea to the generic "origin" connection.

More detail: the underlying connection is set up automatically as part of cloning or forking, in
`05-daily-workflow.md` and `09-forks-and-contributing.md`.

**Outside collaborator.** A person who has access to one or more of an organisation's
repositories without being a member of the organisation itself.

An outside collaborator cannot be added to a team, no matter what. On any plan other than Free,
adding one to a private repository still uses up a paid seat, the same as adding a full member.
Use this role for a one-off contractor working on a single repository; use full membership for
someone becoming a regular part of the team.

Not to be confused with: a **member**, who belongs to the organisation itself and can be added
to teams.

More detail: `03-members-and-access.md`.

**Owner (organization owner).** The organisation-level role with complete administrative
control: billing, every repository, and every member's access.

Organisation owners automatically get admin-level access to every repository the organisation
owns, no matter what role is set for them on that specific repository. GitHub's own guidance is
to have at least two owners on any organisation that matters, because if the only owner ever
loses access, there is no documented emergency way back in for anyone else.

Not to be confused with: a **repository admin**, whose control is scoped to one repository only.
An organisation owner automatically has admin-level access to every repository anyway, but a
repository admin has no organisation-wide power at all.

More detail: `02-organizations.md`.

## P

**Passkey.** A credential stored on your device that can stand in for both your password and
your two-factor code at once, in a single step.

More detail: `01-accounts-and-security.md`.

**Permalink.** A link to a file that always shows the exact version it showed at the moment the
link was made, rather than whatever the file currently says.

Press the `y` key while viewing a file to turn the address in your browser into one of these.
Useful whenever you are pointing a teammate at exactly what you were looking at, even if the
file changes later.

More detail: `15-finding-things.md`.

**Personal access token.** A long string of characters that acts like a password, letting a
tool or a command line connect to your GitHub account without you typing your actual password
each time.

This kit does not teach creating one, and never will as part of normal use. GitHub's own
guidance treats a personal access token as risky in the same way a password is risky: "Personal
access tokens are like passwords, and they share the same inherent security risks." Instead,
this kit uses the GitHub CLI's own browser-based sign-in, which never shows you a long string of
characters you could accidentally paste somewhere it should not go. If anything you are doing
seems to require creating a token, treat that as a signal to stop and use the browser sign-in
path instead, not as a normal step to work through.

More detail: `11-github-with-claude-code.md`.

**Pin / Pinning.** Choosing up to six repositories, or gists, to display prominently on your own
GitHub profile page, so anyone visiting it sees them first.

Not to be confused with: **starring**, a private list you build for yourself of things you want
to find again, which does not show publicly on your profile the way pinning does.

More detail: `15-finding-things.md`.

**Pre-release.** A published release that is deliberately marked as not ready for everyday use.

Anyone who can see the repository can also see a pre-release; marking it this way changes its
label and whether it counts as "latest," not who is allowed to see it. If you need something
hidden from most people entirely, that is what a draft release is for instead.

Not to be confused with: a **draft release**, which is hidden from anyone without Write access
until it is published.

More detail: `17-releases-and-versions.md`.

**Pull.** The git action that downloads the newest changes from GitHub and merges them into your
current branch, in one step.

Commit any of your own unsaved changes before pulling, otherwise git can get confused about
which version of a file to keep.

Not to be confused with: a **pull request**, an entirely different thing, a proposal to merge a
change, reviewed and approved before it lands.

More detail: `05-daily-workflow.md`.

**Pull request.** A proposal to merge a branch's changes into another branch, usually your
default branch, so someone (possibly you, working alone) can look it over before it goes live.

Nothing on a branch reaches your main copy until its pull request is deliberately merged. GitHub
organises a pull request's page into tabs: Conversation, Commits, Checks, and Files changed are
the ones you will use most.

Not to be confused with: **pull**, the git command that downloads and merges the newest changes
from GitHub, an unrelated everyday action with a similar name.

More detail: `07-pull-requests.md`.

**Push.** The step that sends a commit you have already made, sitting on your own machine, up to
GitHub.

A commit made locally is invisible to anyone else, including your own GitHub account, until it
is pushed.

Not to be confused with: a **commit**, the saved snapshot itself, which happens before a push and
can sit unpushed on your machine indefinitely.

More detail: `05-daily-workflow.md`.

**Push protection.** A stricter version of secret scanning that stops a password, key, or token
from ever reaching GitHub in the first place, by refusing the push outright.

It has a real bypass: anyone with Write access can push past it anyway by giving a reason, so
treat it as a prompt to stop and check, not an absolute wall. On a public repository it runs
automatically for free; on a private repository, it is the same paid, organisation-only
availability as secret scanning.

Not to be confused with: **secret scanning**, the broader feature that looks at what has already
been pushed, rather than blocking a push before it lands.

More detail: `10-protecting-your-work.md` and `19-security-features.md`.

## R

**README.** A file, almost always named `README.md`, that GitHub automatically shows on a
repository's front page, underneath the file list.

GitHub's own guidance on what it should cover: what the project does, why it is useful, how to
get started, and where to get help. For GitHub to find it automatically, it needs to sit in one
of three places: the root of the repository, a hidden `.github` folder, or a `docs` folder. The
plain root is the right choice for almost every small project.

More detail: `04-repositories-and-visibility.md` and `14-markdown-and-writing.md`.

**Rebase.** One of the three ways to merge a pull request, where a branch's original commits are
replayed straight onto the main copy, with no extra merge commit added.

The result is a straight-line history, similar to a plain merge commit except without that one
extra commit recording the merge itself. This has to be specifically allowed on a repository
before it appears as an option.

Not to be confused with: **squash and merge**, which combines a branch's commits into a single
new one, rather than replaying the original commits individually.

More detail: `07-pull-requests.md`.

**Recovery codes.** A set of one-time backup codes GitHub gives you when you turn on two-factor
authentication, each one usable exactly once, whose entire purpose is getting you back into your
account if your phone, authenticator app, or SMS number is ever unavailable.

GitHub cannot restore access to a two-factor-protected account if both your two-factor device
and your recovery codes are lost. Save them in a password manager, not on the same phone that
holds your authenticator app, the moment you turn on two-factor authentication, not later.

More detail: `01-accounts-and-security.md`.

**Release.** A tag wrapped with a title, a description, and, optionally, downloadable files, all
gathered onto one page, marking one specific, permanent state of your repository as "this is
what went out."

A release answers a question that otherwise has no easy answer: "what exactly was live on a
given date." GitHub automatically adds a zip file and a tarball of your repository's contents to
every release, on top of anything you attach yourself.

Not to be confused with: a **tag**, the plain, permanent label underneath a release. Every
release has a tag; not every tag has a release built on top of it.

More detail: `17-releases-and-versions.md`.

**Release notes.** The written description on a release's page, explaining what changed and why
it matters.

GitHub can draft a starting point for you automatically, listing merged pull requests and
contributors, but that draft is written in technical terms. This kit's advice: keep it if your
audience is technical, or add a couple of plain-English lines above it if they are not.

More detail: `17-releases-and-versions.md`.

**Remote.** A connection your local copy of a repository keeps to a version of it sitting
somewhere else, usually on GitHub, so commands like push and pull know where to send or fetch
changes.

**Origin** is the conventional name given to the main remote connection; **upstream** is
GitHub's specific name for the remote connection a fork keeps back to the repository it was
forked from. Both are kinds of remote.

More detail: `09-forks-and-contributing.md`.

**Repository (repo).** The container everything else in this kit lives inside: your code, your
files, and every past version of them, kept and tracked.

GitHub's own description: "a place where you can store your code, your files, and each file's
revision history." A repository is either public, visible to everyone on the internet with no
account needed, or private, visible only to you and whoever you have explicitly given access to.

More detail: `04-repositories-and-visibility.md`.

**Repository role.** The access level a specific person has inside one specific repository,
separate from any organisation-wide role they hold.

Five levels, from least to most access, and GitHub's own recommendation for who each one fits:

| Role | Who it fits |
| --- | --- |
| **Read** | Non-code contributors who want to view or discuss the project |
| **Triage** | Contributors who manage issues and pull requests, without pushing changes themselves |
| **Write** | Contributors who actively push changes |
| **Maintain** | Project managers who need to manage the repository, without sensitive or destructive actions |
| **Admin** | People who need full control, including deleting the repository |

An organisation owner automatically gets Admin on every repository the organisation owns,
regardless of any role set for them individually.

Not to be confused with: an **organisation owner**, whose control spans the entire organisation,
not one repository.

More detail: `03-members-and-access.md`.

**Review.** Feedback left on a pull request by anyone with at least Read access, submitted as a
Comment, an Approve, or a Request changes.

By itself, "Request changes" is only a strong signal, not a block on merging, unless the
repository specifically requires an approval before a pull request can merge.

More detail: `07-pull-requests.md`.

**Ruleset.** The newer of GitHub's two mechanisms for enforcing rules on a branch, such as
requiring a pull request and a review before a change can land.

Multiple rulesets can apply to the same branch at once, and a ruleset can be switched off
without deleting it. A brand-new ruleset starts Disabled and enforces nothing until you switch it
to Active, which is the single most common reason a new ruleset "does not seem to work." Unlike
branch protection rules, a ruleset does not automatically exempt the repository owner from its
own requirements; you have to add yourself, or the admin role, to its bypass list if you do not
want to risk locking yourself out. On a private repository, this requires at least GitHub Pro or
GitHub Team and above; on a public repository, it is free on every plan.

Not to be confused with: a **branch protection rule**, the older mechanism, which only allows one
rule per branch but does exempt administrators by default.

More detail: `10-protecting-your-work.md`.

**Runner.** The computer that actually carries out a workflow's instructions, provided by
GitHub unless someone has deliberately set up their own.

Most small business workflows run on GitHub's own standard, cheapest option.

More detail: `18-automation-basics.md`.

## S

**Secret.** A password, key, or other sensitive value stored on a repository so a workflow can
use it, without that value ever appearing directly inside the workflow file itself, where anyone
with Read access could otherwise see it.

More detail: `18-automation-basics.md`.

**Secret scanning.** A GitHub feature that automatically reads what gets pushed to a repository,
looking for things that look like passwords, API keys, or tokens, and raises an alert if it
finds one.

On a public repository, this runs automatically for free. On a private repository owned by a
personal account (not an organisation), this kit could not find any tier, paid or otherwise,
that turns it on. On a private repository owned by an organisation, it is a paid add-on
available on GitHub Team or GitHub Enterprise Cloud. If you are a solo operator on a private,
personal-account repository, the honest fact is that nothing is watching for a leaked secret;
never typing one into a file in the first place is your actual defence.

Not to be confused with: **push protection**, the stricter version of this same feature that
blocks a secret before it ever lands, rather than scanning it after the fact.

More detail: `19-security-features.md`.

**Security and quality tab.** The one place on a repository's main page where every alert from
secret scanning, push protection, and Dependabot collects, so there is only one place to check.

Seeing this tab at all needs Write, Maintain, or Admin access to the repository, or organisation
owner status.

More detail: `19-security-features.md`.

**Security key.** A physical device, or a device's own built-in option like Touch ID or Windows
Hello, that proves it is you through a hardware check rather than a typed code.

More detail: `01-accounts-and-security.md`.

**Security manager.** An organisation-level role that gives read access to every repository plus
visibility into security alerts, without handing over full organisation-owner control.

More detail: `03-members-and-access.md`.

**SMS code.** A six-digit code sent by text message, used as an alternative second proof for
two-factor authentication.

GitHub recommends an authenticator app over this method where you have the choice, because SMS
can be intercepted, does not resist phishing, and is not supported in every country. Confirm
your own country is currently on GitHub's supported list before relying on it as your only
method.

Not to be confused with: an **authenticator app (TOTP)**, GitHub's recommended alternative.

More detail: `01-accounts-and-security.md`.

**Squash and merge.** One of the three ways to merge a pull request, where every commit on the
branch is combined into a single new commit on the main copy.

This is this kit's own recommendation for most small businesses, since it keeps a repository's
history readable, one line per real change, rather than cluttered with every small "fix typo"
commit made along the way. It is this kit's recommendation, not GitHub's default; the merge
commit is GitHub's documented default. Squash and merge has to be specifically allowed on a
repository before it appears as an option.

Not to be confused with: a **merge commit**, GitHub's actual default, which keeps every individual
commit from the branch rather than combining them into one.

More detail: `07-pull-requests.md`.

**Stage / staged changes.** The step, inside git, where a change is marked as ready to be
included in the next commit, sitting between "you edited a file" and "you committed it."

Nothing you do in this kit's browser or Claude Code workflows requires you to think about this
step directly; committing a change through the browser or through a plain-English request to
Claude Code stages and commits it together, in one motion.

Not to be confused with: a **commit**, the actual saved snapshot that happens once staged
changes are committed.

More detail: this staging step happens automatically as part of committing, covered in
`05-daily-workflow.md`.

**Star / Starring.** Marking a repository as one you want to find again easily, similar in
spirit to bookmarking a page in a browser.

Click **Star** on any repository's main page; find your starred repositories again at
`github.com/stars`.

Not to be confused with: **pinning**, a small, curated selection that shows publicly on your own
profile page, rather than a private list only you see.

More detail: `15-finding-things.md`.

**Step.** One instruction inside a job, run in order: either a plain command, or a call to a
pre-made action.

More detail: `18-automation-basics.md`.

## T

**Tag.** A permanent label attached to one specific point in a repository's history.

Once a tag exists, it always points at that same point, even as everything else keeps moving
forward. A release is built on top of a tag; a tag can exist entirely on its own with no release
attached to it.

Not to be confused with: a **release**, the fuller feature (a title, notes, and optional files)
that a tag can be wrapped up inside.

More detail: `17-releases-and-versions.md`.

**Team.** A group of organisation members that GitHub lets you grant the same access to all at
once, instead of person by person.

Only organisation members can be on a team; an outside collaborator cannot be added to one under
any circumstance. Teams can be nested, so a child team automatically inherits whatever access its
parent team has, and mentioning the parent team notifies everyone in the child teams too.

Not to be confused with: an **organisation**, the larger, separate account a team sits inside of.

More detail: `03-members-and-access.md`.

**Trigger, also called an event.** What starts a workflow running.

Common triggers: `push` (a commit is pushed), `pull_request` (a change is proposed), `schedule`
(runs at a set time), `issues` (an issue is opened or changed), and `workflow_dispatch` (adds a
manual button so a person can start it on demand).

More detail: `18-automation-basics.md`.

**Two-factor authentication (2FA).** Signing in with your password and a second proof that it is
really you, so a stolen password alone is not enough to get into your account.

GitHub supports several second-factor methods: an authenticator app, SMS, a security key, a
passkey, or GitHub Mobile. Turn this on before GitHub eventually requires it; publishing a
release or creating an organisation are exactly the kinds of actions that can trigger mandatory
enrolment.

More detail: `01-accounts-and-security.md`.

## U

**Upstream.** GitHub's own name for the repository a fork was originally made from.

A fork stays connected to its upstream, but the two are otherwise independent: nothing you do on
your fork changes the upstream, and nothing that changes on the upstream changes your fork,
until you deliberately sync the two, or open a pull request to bring your change back.

Not to be confused with: **origin**, the more general git term for the connection back to
wherever you cloned from, which is not specific to forking.

More detail: `09-forks-and-contributing.md`.

**Username.** Your public handle on GitHub, forming part of every profile link and every
repository address you own.

Usernames are first come, first served, and GitHub does not hold one for you. You can change it
later, but your old username becomes available for someone else to claim, and any CODEOWNERS
file or gist link that mentions your old username has to be updated by hand.

More detail: `01-accounts-and-security.md`.

## V

**Verification code (new-device check).** A separate code GitHub can ask for when you sign in
from a browser or device it does not recognise, sent by email or, if you have GitHub Mobile
installed, as a push notification.

This is not the same as your two-factor code, and it can happen even with two-factor
authentication switched off. If a code like this arrives and you did not just try to sign in
anywhere, GitHub is telling you plainly that your password may be compromised; change it
immediately.

Not to be confused with: your regular **two-factor authentication** code, which is a separate,
routine part of every sign-in once 2FA is turned on.

More detail: `01-accounts-and-security.md`.

**Verified email address.** An email address GitHub has confirmed belongs to you, by sending a
link you clicked.

GitHub blocks some basic actions, including creating a repository, until at least one email
address on your account is verified.

More detail: `01-accounts-and-security.md`.

## W

**Watch / Watching a repository.** Manually subscribing to a repository so you hear about
activity in it.

The default, quieter option after you stop watching a repository still lets a direct question to
you get through: GitHub's own rule is that unwatching "unsubscribes you from future updates
unless you participate in a conversation or are @mentioned." Only **Ignore**, a separate and
louder setting, removes that.

Not to be confused with: **starring**, which bookmarks a repository for yourself without
subscribing you to its activity.

More detail: `16-notifications.md`.

**Wiki.** A separate, lighter documentation space attached to a repository, for writing that
goes beyond what belongs in a README.

This kit does not walk through using one in depth. Where it comes up: GitHub's own README
guidance is that longer material belongs in a wiki rather than the README itself, and a wiki's
contents are affected the same way as issues and pull requests when a repository is archived,
transferred, or deleted.

More detail: mentioned in `02-organizations.md` and `04-repositories-and-visibility.md`; this
kit has no dedicated file on using a wiki.

**Workflow.** One specific set of automated instructions, made up of one or more jobs, that runs
when a trigger happens.

A repository can have several workflows, each doing something different. Every workflow is
written in a **workflow file**.

More detail: `18-automation-basics.md`.

**Workflow file.** The actual text file a workflow is written in, sitting in a folder named
`.github/workflows` inside the repository.

It is a different kind of formatted file to the Markdown covered elsewhere in this kit, but
reading one is still mostly plain English once you know the shape: `name:` is the label shown in
the Actions tab, `on:` is the trigger, `jobs:` lists what happens, and `steps:` is the ordered
list of instructions.

More detail: `18-automation-basics.md`.

**Working copy.** The actual files sitting on your own computer (or wherever you are editing
them), as opposed to the version of them saved inside git's history.

Editing a file changes your working copy only; nothing is tracked by git, and nothing reaches
GitHub, until that change is committed and pushed.

Not to be confused with: a **commit**, the saved snapshot that exists once a change in your
working copy has actually been recorded.

More detail: the distinction is implicit throughout `05-daily-workflow.md`, which covers
committing and pushing a change from your working copy.

---

## A note on how this file was built

This glossary was assembled by reading every numbered topic file in this kit (01 through 19)
plus `NAVIGATION-STYLE.md`, and pulling out every technical term used, especially the ones used
without ever being explained on the page where they appeared. Where a fact depends on a specific
GitHub behaviour or rule, this file states only what those topic files themselves could confirm
from GitHub's own documentation. Two entries, **CODEOWNERS** and **GitHub Pages**, needed more
explaining here than any single topic file gave them, because they were used in this kit before
being defined anywhere; both are marked above with what could and could not be confirmed.

No em-dashes were used anywhere in this file. It was checked by searching the finished file for
the em-dash character directly before this note was written, and again after this note was added.
