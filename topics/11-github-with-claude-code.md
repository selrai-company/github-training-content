# Using GitHub through Claude Code

## What this gets you

Every member of this kit has Claude Code on the Max plan already running. That means most of
the day-to-day GitHub work in this kit, cloning a repository, saving a change, opening a pull
request, does not need you to learn a single git command or open a terminal window. You
describe what you want in plain English, Claude Code carries out the actual GitHub steps, and
it tells you what it did. For a small business, that is the difference between GitHub work
being something only the technical person on the team can do, and something anyone who can
describe a task in a sentence can do too, without becoming the kind of person who memorises
command-line flags.

This page is the layer underneath everything else in this kit that touches GitHub: how Claude
Code proves to GitHub that it is really you, what it will do without stopping to ask each time
and what it will never do at all, and the one habit, reading what it proposes before you say
yes, that makes handing any of this over safe rather than risky.

## Before you start

**You need Claude Code already running, on the Max plan.** Every reader of this kit has it. If
you have not opened it before, getting it installed is not covered on this page, only what to
ask it once it is open.

**You should have read `05-daily-workflow.md` first.** That is where clones, commits, and
pulling updates are explained from the ground up, in the browser and through Claude Code both.
This page assumes you already know what those words mean and builds on top of them.

**If branches, pull requests, or forks come up below and you have not met them yet**, read
`06-branches.md`, `07-pull-requests.md`, and `09-forks-and-contributing.md` first. This page
shows you the plain-English phrasing to ask Claude Code for each of those, not what each one is
or why you would use it.

**You need a GitHub account that already has access to whatever repository you are working
with.** Claude Code acts as you. It does not have a separate GitHub identity or separate access
of its own. `03-members-and-access.md` covers checking, or getting, your own access if you are
not sure you have it.

**You do not need to know a single git command, and you never need to open a terminal
yourself.** Claude Code runs the underlying commands and reports back, in plain English, what it
did.

## The words you need

Some of these are covered fully elsewhere in this kit, this page only needs the plain-English
version, and says where the full explanation lives. Others belong to this page alone.

**Clone.** A full, connected copy of a repository, including its entire history, on your own
machine. Covered fully in `05-daily-workflow.md`; this page only shows the sentence you say to
Claude Code to get one.

**Branch.** A private copy of the work you can change without touching what everyone else sees,
until it is ready. Covered fully in `06-branches.md`.

**Commit.** A saved snapshot of a change, with a note explaining what it was. Covered fully in
`05-daily-workflow.md`.

**Pull request.** A request to bring a branch's changes into the main version, with a chance for
someone to look at it first. Covered fully in `07-pull-requests.md`.

**Fork.** Your own personal copy of someone else's repository, so you can propose a change back
without having Write access to the original. Covered fully in `09-forks-and-contributing.md`.

**GitHub CLI (`gh`).** GitHub's own command-line tool. It is the thing that has to be installed
and signed in on your machine before Claude Code, acting as you, can reach a private repository
at all. Why it matters: everything below about signing in, cloning something private, and
pushing a change runs through it.

**Sign-in, or authentication.** Proving to GitHub that the requests coming from your machine are
genuinely from you, so it will show you private work and accept a push from you. This is
separate from signing in to Claude Code itself, covered below.

**Device flow (the short code you type into a browser).** GitHub's way of signing a tool like
the GitHub CLI in without it ever seeing your password. It shows you a short code, you type that
code into a normal GitHub page in a browser tab, and confirm it is really you. It is the same
idea as the code you type on your phone when a smart TV app asks you to "activate" it at a
website: the TV app never touches your password, the code is just a short-lived link between the
two.

**Personal access token (PAT).** A long, password-like string GitHub can generate that stands in
for your username and password for a specific purpose. GitHub's own guidance treats it exactly
like a password, and this page explains below why the browser sign-in above is the better
one-time choice for what you are doing here.

**`gh auth status`.** GitHub's own command for checking whether you are already signed in on a
machine, and which account. It comes up more than once below, because it is the first thing
worth checking whenever something GitHub-related seems wrong.

**Force-push.** A push that overwrites the history already on GitHub instead of adding to it,
which can erase someone else's work if it lands on the wrong branch. It is one of two things
this page lists below as staying under your genuine control, never something Claude Code decides
alone.

**Approval prompt.** The moment Claude Code stops, shows you exactly what it is about to do, a
file it will change, a command it will run, a branch it will push to, and waits for you to say
yes before going further.

**Manual mode.** One of Claude Code's permission modes. Switching to it makes it stop and ask
before every single file edit, command, or network request, rather than only the higher-risk
ones. Useful while you are still learning what a normal proposal looks like.

**Diff.** A side-by-side, line-by-line view of exactly what changed in a file, the old text next
to the new text. It is what the browser shows you when you review a pull request properly, and
it is why the browser stays the right tool for that particular step.

## How to do it

Everything below works the same way: you describe the outcome in plain English, Claude Code
proposes exactly what it is about to do, and you decide whether to let it. The sections below
cover what it can do, what it stays out of on purpose, how it proves it is you to GitHub, the
everyday phrasing to use, the habit that keeps the whole thing safe, and what to do when it does
not go to plan.

### What Claude Code can actually do with GitHub for you

Claude Code already has the underlying tool (git) available, so it can carry out the everyday
GitHub steps from a plain-English request instead of you typing a command:

- Get a full, connected copy of a repository onto your machine (a **clone**).
- Pull down the newest changes to a copy you already have.
- Create a new branch and switch you onto it.
- Save a change you have made as a commit, with a message it can write or you can dictate.
- Push your commits up to GitHub, to the branch you are currently working on.
- Open a pull request that describes the change you asked for. Anthropic's own documentation
  confirms this directly: "You can create pull requests by asking Claude directly ('create a pr
  for my changes')."
- If the GitHub CLI is installed and signed in (covered below), create a brand-new repository
  with an explicit public or private flag, or fork someone else's repository.
- Bring a fork up to date with the original repository, a task that is a short sequence of git
  commands with nothing worth watching on screen, so it is genuinely easier through Claude Code
  than typing it yourself.

Every one of these is covered step by step, with the exact plain-English phrasing, in
`05-daily-workflow.md`, `06-branches.md`, `07-pull-requests.md`, and
`09-forks-and-contributing.md`. This page's job is the layer underneath: authentication, and the
judgement calls around letting it act on your behalf.

### What Claude Code will never do, and what it genuinely cannot do

These are two different things, and it matters which is which. One is a safeguard someone
switched on for you. The other is a real limit, no setting or clever phrasing gets past it.
Mixing the two up is exactly how a member ends up over-trusting it, approving something they
never actually read because "it always gets this right."

**By design, it stops itself, on purpose. This is a safeguard, not a gap you need to work
around.**

Anything tied to your identity as a real person stays in the browser, signed in as yourself.
Turning on two-factor authentication, saving your recovery codes, creating an organization,
inviting or removing a member, transferring or deleting a repository, changing billing. GitHub
needs to see you specifically click the button, scan the code, or type the number. A terminal
assistant has no way to do that part, and it should not be trusted to. `01-accounts-and-security.md`
covers all of these, and every one of them stays a browser-only step in this kit deliberately.

It will never ask you to create or paste a personal access token, and if anything you are
doing seems to need one, that is a sign to stop and use the browser sign-in path below instead,
or bring it to someone who can advise properly. More on why in the next section.

It will not quietly merge a pull request nobody has reviewed, and it will not force-push
(a push that overwrites history) without you being genuinely involved. These are two of the
specific, named actions Anthropic's own documentation lists as things Claude Code treats as
needing a person's decision, not something it decides alone even when it is otherwise working
through a task without stopping to ask about every small step.

**Separate from any safeguard, some things it has no way to do at all, whatever you ask it and
however you phrase the request.**

It cannot judge whether a change is actually a good idea for your business. It can carry out
the git and GitHub mechanics of a request precisely, and describe exactly what it changed, but
deciding whether that change should happen, whether it is the right fix, whether now is the
right time, is a judgement call that stays with the person reading the proposal, every time.
Anthropic's own security documentation puts the responsibility in exactly those words: "Claude
Code only has the permissions you grant it. You're responsible for reviewing proposed code and
commands for safety before approval."

It cannot act with more access than your own GitHub sign-in already gives it. If you do not
have Write access to a repository, it cannot get you Write access by working around your
account, because it does not have "a separate GitHub identity or separate access of its own",
covered above. Whatever you are personally allowed to do on GitHub is the ceiling on what it
can do for you, not a starting point it can push past.

It cannot look at a rendered page the way you do. Reading a diff properly, checking that a
pull request is exactly what it claims to be before it merges, is a seeing-and-judging task,
not a typing task, and that is genuinely outside what a terminal assistant does. That is why the
table below still sends you to the browser for that specific step, regardless of who or what
proposed the change.

It cannot know what you actually meant if you did not say it. A vague request ("clean up the
homepage text") gets one specific interpretation, not a guess it checks with you first unless
it is genuinely unsure. That is exactly why reading what it proposes, covered next, is not a
backup for when something goes wrong. It is the only place an ambiguous request going the wrong
way ever gets caught, because nothing else in this setup is checking for that on your behalf.

### How it signs in to GitHub, and why this matters

There are two separate sign-ins happening here, and it is worth being clear about which one is
which.

**Signing in to Claude Code itself** you have already done, since you are using it. Anthropic's
own documentation describes it plainly: "On first launch, Claude Code opens a browser window for
you to log in." That is your Claude account, and it is separate from GitHub entirely.

**Signing in to GitHub** is the one this page is actually about, because it is what lets Claude
Code clone a private repository, push a branch, or open a pull request as you. Claude Code does
not have its own separate GitHub identity. It uses whatever GitHub sign-in already exists on
your machine, the same one a plain `git` command would use, and the standard way to set that up
is the **GitHub CLI**, GitHub's own command-line tool, known as `gh`.

**Setting it up, once.** You only do this once per machine. Ask Claude Code, in plain English:

```
Check whether the GitHub CLI is installed and signed in, and set it up if it isn't.
```

Here is what happens, so you recognise each step:

1. **If `gh` is not installed yet**, Claude Code installs it. On Windows, that is the single
   command `winget install --id GitHub.cli --source winget`; on a Mac, it is `brew install gh`,
   GitHub's own published commands for each. Read what it proposes before you approve it, exactly
   as you would for anything else, covered in the next section.
2. **It checks whether you are already signed in** using `gh auth status`, GitHub's own command
   for this, described in its own documentation as testing "the authentication state of each
   known account" and reporting any issues. If you are already signed in, you are done, nothing
   else happens.
3. **If you are not signed in, it starts the sign-in process.** GitHub's own documentation is
   direct that the default here is "a web-based browser flow," not a token. Claude Code shows you
   an 8-character code with a hyphen in the middle, per GitHub's own description of this step,
   and a browser window opens (or you are told the address to open) at `github.com/login/device`.
   - If you are not already signed in to GitHub in that browser, you land on GitHub's ordinary
     sign-in screen first, with the usual username-or-email and password fields. Sign in there as
     you normally would.
   - Once you are signed in, GitHub asks for the short code. Type or paste the one Claude Code
     showed you, then confirm.
   - You will know it worked because Claude Code, back in its own window, tells you it is
     connected and carries on with the step you actually asked for. If instead you land on a page
     that does not match either of these two (the sign-in screen, or a field for the code), that
     is the moment to read what is actually on your screen rather than assume, GitHub's own pages
     change their wording from time to time.

**Screenshot placeholder:** the `github.com/login/device` code page, the one you land on once you
are signed in to GitHub in that browser, showing the field where the short code goes and the
**Continue** or **Authorize** button, so a reader recognises it the first time they see it.

**Why this beats a personal access token, and this is GitHub's own guidance, not just this
kit's preference.** GitHub's documentation opens its token-management page with a direct
warning: "Treat your access tokens like passwords," going on to say "Personal access tokens are
like passwords, and they share the same inherent security risks." Its own recommendation for
exactly this situation: "To access GitHub from the command line, you can use GitHub CLI or Git
Credential Manager instead of creating a personal access token." The browser sign-in above is
that safer path. It never shows you a long string of characters you could accidentally paste
somewhere it should not go, and if you ever need to revoke access, you do it from your own GitHub
account settings rather than hunting for where a token got typed or saved. If anything you are
doing seems to be pushing you toward creating a token instead, stop and ask this kit's guide, or
use the browser sign-in above, rather than doing it.

**If a repository is public**, none of this is needed just to look at it or get a copy of it,
public means no sign-in is required to read. It only matters the moment you want to push a
change back, to a public or a private repository either way.

### Asking it for the everyday things, in plain language

You never need to know the underlying git command. Describe the outcome, the way you would say
it out loud. A few you will use constantly, each covered in full in its own file:

**Getting a copy of a repository** (`05-daily-workflow.md`):

```
Clone this repository for me: [paste the repository's HTTPS link]
```

**Making a branch to work in** (`06-branches.md`):

```
Make me a new branch called fix-homepage-typo, based on main.
```

**Saving a change as a commit** (`05-daily-workflow.md`):

```
Commit this change with the message "corrected Saturday opening hours".
```

**Pulling down the newest changes** (`05-daily-workflow.md`):

```
Pull the latest changes.
```

**Opening a pull request once your change is ready** (`07-pull-requests.md`):

```
Create a pull request for my changes.
```

Claude Code writes the title and description from what actually changed. Ask it to adjust either
one before it goes further, the same way Anthropic's own guidance puts it: "Review Claude's
generated PR before submitting and ask Claude to highlight potential risks or considerations."

**Bringing a fork up to date** (`09-forks-and-contributing.md`):

```
Bring my fork up to date with the original repository.
```

If you ever lose track of where a copy landed on your machine, just ask: "Where did you clone
[repository name] to?" It knows the exact path and will tell you again.

### Reading what it proposes before you approve it

This is the one habit that makes everything above safe to actually use, so it earns its own
section rather than a passing mention.

Anthropic's own security documentation states the principle plainly: "Claude Code only has the
permissions you grant it. You're responsible for reviewing proposed code and commands for safety
before approval." In practice, that plays out two ways:

**Sometimes it stops and shows you exactly what it wants to do, and waits for a yes.** When that
happens, actually read it, the file it is about to touch, the command it is about to run, the
branch it is about to push to, before you approve. A proposal that goes further than what you
asked (a second file you did not expect, a different branch than the one you named) is exactly
the moment this step exists to catch. Saying yes without reading is the same risk as clicking
through a dialog box without reading it: usually fine, occasionally the one time it was not.

**Sometimes, on the Max plan, it just goes ahead with routine, low-risk steps without stopping to
ask each time**, because a separate background check reviews the action instead of interrupting
you. This is the normal, built-in way Claude Code behaves on this plan, not a setting you turned
on by accident. It is what makes everyday steps like committing or pushing to your own branch
feel instant rather than click-by-click. The two boundaries mentioned above, no unreviewed pull
request merges, no quiet force-pushes, still hold regardless.

**If you would rather see every single step while you are still learning**, ask for that
directly: press `Shift+Tab` inside the Claude Code window to cycle to the mode Anthropic labels
**Manual**, which stops and asks before anything that edits a file, runs a command, or reaches
the network. Note that asking Claude Code in chat to switch modes does not work, per Anthropic's
own documentation, `Shift+Tab` is the way. Claude Code shows which mode you are in inside its own
window; if you are not sure what you are looking at after pressing it, ask it directly which mode
it is in rather than guess. Switch back the same way once you are comfortable.

### When the browser is the better tool, not Claude Code

Both are legitimate. This page adds three situations specific to working through Claude Code, on
top of the general table already in `05-daily-workflow.md`:

| Situation | Use |
|---|---|
| Anything on this page's "will never do" list: 2FA, org membership, billing, deleting or transferring a repository | Browser, signed in as yourself |
| Actually reviewing a pull request, reading a diff line by line before you approve it | Browser, per `07-pull-requests.md`, it is built for exactly this |
| You are not sure what a proposal is about to do and reading it back to yourself did not clarify it | Ask Claude Code to explain it in plain English first; if that still does not land, do the step in the browser instead where you can see it happen |
| First time doing something on this page | Do it once in the browser so you have seen the click path, then let Claude Code handle it from then on |

### What to do when it gets stuck

**If it seems frozen mid-step**, press `Ctrl+C` to cancel whatever it is currently doing. This
does not lose your conversation, and you can tell it to try again, or try a different way.

**If closing the window feels like the only option**, that is fine too. Anthropic's own
documentation confirms directly: "Restarting doesn't lose your conversation." Reopen Claude Code
from the same project folder and ask it to pick back up where you left off.

**If it is specifically stuck on a GitHub step**, ask it directly what is blocking it and read
the answer back rather than guessing. A few genuinely common causes:

- **It says it can't push, or can't see a private repository.** This is almost always the
  authentication step above not having been completed, or completed for a different GitHub
  account than the one that actually has access. Ask it to run the `gh auth status` check again
  and tell you what account it is signed in as.
- **It's hit a merge conflict it can't resolve on its own.** That is expected sometimes, not a
  failure. `08-merge-conflicts.md` covers what a conflict actually is and how to work through
  one, whether you finish it with Claude Code's help or switch to the browser to see it laid out
  visually.
- **It genuinely doesn't know what to do next.** Tell it plainly, and it will usually tell you
  plainly back rather than guess. If two or three attempts at explaining still have not unstuck
  it, that is the moment to fall back to the matching browser steps in this kit instead, they
  will always get you there even when the shortcut does not.

## Strategy: how to actually use this

**Use Claude Code for anything mechanical, and read the proposal anyway.** Cloning, committing,
pulling, opening a pull request, bringing a fork up to date, none of these need your judgement
about what to do, only your permission to go ahead. That is exactly the shape of task worth
handing over. The ten seconds it takes to read what it is about to do is not optional, it is the
whole reason handing this over is safe rather than reckless.

**Use the browser for anything that needs your judgement, not your typing speed.** Actually
reviewing a pull request line by line, deciding whether a change is ready, is not made faster by
Claude Code, because the slow part was never the clicking. `07-pull-requests.md` is built for
reading a diff properly. Use it there every time, regardless of who or what proposed the change.

**A solo operator gets the most out of this page, and carries the most risk from skipping the
reading habit.** There is nobody else who would catch a mistake before it lands. If you are
working alone, it is worth staying in Manual mode for your first week or two of using Claude Code
and GitHub together, even though the Max plan does not require it, until you have a feel for what
a normal proposal looks like. After that, switch back. The point of Manual mode is to build the
habit, not to live in it forever.

**A team of three or four should split by who reviews, not by who types.** The person who is not
the technical owner of the codebase can do everything through Claude Code in plain English and
never learn a git command, that is the entire value of this page for them. The pull request
itself should still get a real look from whoever understands what the change could break, in the
browser, before it merges, exactly the same as if nobody had used Claude Code at all. Handing
typing over to Claude Code is not the same as handing over judgement, and this kit never treats
it that way.

**The decision rule for a branch and pull request versus the direct loop is the same with or
without Claude Code.** If the change is small, clearly safe, and yours alone to make, the
direct loop from `05-daily-workflow.md` is fine, ask Claude Code to commit and push straight to
the branch you are on. The moment more than one person needs to see a change before it lands, or
it touches more than one file, ask for a branch and a pull request instead, `06-branches.md` and
`07-pull-requests.md` cover why.

**What good looks like months later:** nobody on the team remembers a git command, the person who
was never comfortable with a terminal is opening pull requests confidently on their own, and the
GitHub sign-in has needed refreshing once or twice without anyone treating it as a problem.

**What would change my mind, and the sign worth watching for:** if you notice you are approving
every proposal without actually reading what changed, because nothing has gone wrong yet, that is
not evidence it is safe, it is evidence the reading habit has quietly worn off. That is the moment
to go back to Manual mode for a week, not the moment to relax further.

## A worked example

This continues the same fix from `13-issues-and-tracking-work.md`: the café's ordering site
homepage is showing last week's opening hours instead of the long weekend hours, and the staff
member has already opened issue 23 about it. The nephew has Write access to the ordering site's
repository; the staff member does not, which is exactly why she opened an issue instead of fixing
it herself.

The nephew is not at his desk, he is on his laptop between deliveries, with Claude Code open and
the GitHub CLI already signed in from months ago. He tells it:

```
Make me a new branch called fix-homepage-hours, based on main.
```

Claude Code creates the branch, switches him onto it, and tells him so. He opens the homepage
file and corrects the dates himself, he already knows exactly what to change, then tells it:

```
Commit this with the message "corrected the long weekend opening hours on the homepage", and
push it.
```

It shows him what it is about to commit, the exact lines that changed, before it does anything.
He reads it, it is just the three date fields he meant to touch, so he approves it. Then he asks:

```
Create a pull request for my changes, and put "Fixes #23" in the description.
```

Claude Code writes the title and description from what actually changed, adds the line linking
it to issue 23, and opens the pull request. The nephew does not merge it from inside Claude Code.
He opens the browser, reads the finished pull request the way `07-pull-requests.md` describes,
confirms it is exactly the three dates he expected and nothing else, and merges it there. Issue
23 closes on its own the moment it merges, exactly as `13-issues-and-tracking-work.md` describes.
The whole loop, branch to commit to pull request, took him about the length of one red light.

## If it goes wrong

**It asked me to approve something and I don't understand what it's about to do.** Ask it to
explain in one plain sentence what will actually change, and where. If the explanation still
does not make sense, say no and do that specific step in the browser instead, where you can see
it happen directly.

**I set up the GitHub CLI sign-in once already, and it's asking me to sign in again.** Sign-ins
can expire or be revoked on GitHub's side. Ask Claude Code to run the check again ("check whether
I'm signed in to GitHub") and follow the browser prompt the same way as the first time, it is the
same short process, not a sign anything is broken.

**It made a change I didn't ask for, or touched a file I wasn't expecting.** This is exactly what
reading its proposal before approving is for. If it already happened, ask it to undo just that
specific change and explain what it did, rather than guessing yourself. If you are not confident
the undo is clean, that is a good moment to check the file in the browser directly before doing
anything else.

**I'm not sure whether what it's proposing includes a force-push.** Ask it directly: "does this
involve a force-push?" Force-pushing, and merging an unreviewed pull request, are the two actions
this page already says Claude Code treats as needing you genuinely involved, not something it
decides alone, so it should answer plainly rather than leave you guessing.

**It seems to be signed in as the wrong GitHub account.** Ask it to run `gh auth status` and read
back which account it reports. If it is the wrong one, ask it to sign you in again the same way
as the first time, through the browser, not by pasting anything.

## FAQ

**Do I have to use Claude Code at all? Can I just do everything in the browser?** Yes, entirely.
Nothing in this kit requires Claude Code. It is offered because it is genuinely faster for some
tasks and because every member here already has it on the Max plan, not because the browser path
is second-best.

**Is Claude Code acting as a separate GitHub account, or as me?** As you. It uses your own GitHub
sign-in on your machine, so any commit, push, or pull request it makes shows up under your
account, exactly as if you had typed the commands yourself.

**What if I'm on a shared or work computer and don't want to leave GitHub signed in there?** Sign
out when you are done, from GitHub's own settings covered in `01-accounts-and-security.md`, or
ask Claude Code to sign you out of the GitHub CLI. The sign-in above is tied to that machine, not
to Claude Code itself.

**Does it cost anything extra to have Claude Code do GitHub work instead of me clicking through
the browser?** That is a question about your specific Claude plan and usage, not something this
training kit tracks. Check your own account's usage or billing page for a current answer.

**Can it do something to GitHub I didn't ask for, on its own, out of nowhere?** No. Anthropic's
own documentation is direct on this: "Claude Code only has the permissions you grant it."
Everything it does on GitHub traces back to something you asked for, which is exactly why reading
what it proposes, covered above, is worth the ten seconds it takes.

**Do I need the GitHub CLI set up if every repository I use is public?** No. As covered above,
reading or copying a public repository needs no sign-in at all. The GitHub CLI setup only matters
the moment you want to push a change back, to a public or a private repository either way.

**Can I tell Claude Code to switch to Manual mode instead of pressing Shift+Tab myself?** No. Per
Anthropic's own documentation, asking it in chat to switch modes does not work, `Shift+Tab` inside
the Claude Code window is the way, covered above.

## Quick reference

- **Set up sign-in, once per machine:** "Check whether the GitHub CLI is installed and signed in,
  and set it up if it isn't."
- **Clone a repository:** "Clone this repository for me: [link]"
- **New branch:** "Make me a new branch called ___, based on main."
- **Commit a change:** "Commit this with the message '...'."
- **Pull the newest changes:** "Pull the latest changes."
- **Open a pull request:** "Create a pull request for my changes."
- **Update a fork:** "Bring my fork up to date with the original repository."
- **Check who it's signed in as:** "Run gh auth status and tell me what account you're signed in
  as."
- **See every step before it happens:** press `Shift+Tab` for Manual mode; press it again to
  leave.
- **Stop something mid-step:** press `Ctrl+C`.
- **It will never:** ask you to create or paste a personal access token, merge an unreviewed pull
  request quietly, or force-push without you.

## Sources

- https://code.claude.com/docs/en/common-workflows
- https://code.claude.com/docs/en/security
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/authentication
- https://code.claude.com/docs/en/troubleshooting
- https://cli.github.com/manual/gh_auth_login
- https://cli.github.com/manual/gh_auth_status
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
- https://github.com/cli/cli/blob/trunk/docs/install_windows.md
- https://github.com/cli/cli/blob/trunk/docs/install_macos.md
