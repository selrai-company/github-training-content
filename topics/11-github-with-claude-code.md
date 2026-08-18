# Using GitHub through Claude Code

Every member of this kit has Claude Code on the Max plan. That changes how you can do GitHub:
alongside every browser click path this kit teaches, you can describe what you want in plain
English and let Claude Code do the underlying work for you. This page is the one place that pulls
all of that together: what it can actually do, how it proves it's you to GitHub, how to ask it for
the everyday things, how to read what it's about to do before you let it, when the browser is
still the better choice, and what to do if it stalls.

This page assumes you've read `05-daily-workflow.md`, which is where clones, commits, and pulling
updates are explained from the ground up. If branches, pull requests, or forks come up below and
you haven't met them yet, read `06-branches.md`, `07-pull-requests.md`, and
`09-forks-and-contributing.md` first, this page shows you how to ask Claude Code for each of them,
not what each one is.

By the end of this page, you'll know exactly what's safe to hand to Claude Code and what genuinely
needs your own hands on GitHub, you'll have it signed in to GitHub properly, once, using a browser
rather than a token, and you'll know the one habit, reading what it's about to do before you say
yes, that makes the whole thing safe to rely on.

## What Claude Code can actually do with GitHub for you

Claude Code already has the underlying tool (git) available, so it can carry out the everyday
GitHub steps from a plain-English request instead of you typing a command:

- Get a full, connected copy of a repository onto your machine (a **clone**).
- Pull down the newest changes to a copy you already have.
- Create a new branch and switch you onto it.
- Save a change you've made as a commit, with a message it can write or you can dictate.
- Push your commits up to GitHub, to the branch you're currently working on.
- Open a pull request that describes the change you asked for. Anthropic's own documentation
  confirms this directly: "You can create pull requests by asking Claude directly ('create a pr
  for my changes')."
- If the GitHub CLI is installed and signed in (covered below), create a brand-new repository with
  an explicit public or private flag, or fork someone else's repository.
- Bring a fork up to date with the original repository, a task that's a short sequence of git
  commands with nothing worth watching on screen, so it's genuinely easier through Claude Code
  than typing it yourself.

Every one of these is covered step by step, with the exact plain-English phrasing, in
`05-daily-workflow.md`, `06-branches.md`, `07-pull-requests.md`, and `09-forks-and-contributing.md`.
This page's job is the layer underneath: authentication, and the judgement calls around letting it
act on your behalf.

## What Claude Code will never do, on purpose

**Anything tied to your identity as a real person stays in the browser, signed in as yourself.**
Turning on two-factor authentication, saving your recovery codes, creating an organization,
inviting or removing a member, transferring or deleting a repository, changing billing. GitHub
needs to see you specifically click the button, scan the code, or type the number. A terminal
assistant has no way to do that part, and it shouldn't be trusted to. `01-accounts-and-security.md`
covers all of these, and every one of them stays a browser-only step in this kit deliberately.

**It will never ask you to create or paste a personal access token**, and if anything you're doing
seems to need one, that's a sign to stop and use the browser sign-in path below instead, or bring
it to someone who can advise properly. More on why in the next section.

**It won't quietly merge a pull request nobody has reviewed, and it won't force-push (a push that
overwrites history) without you being genuinely involved.** These are two of the specific,
named actions Anthropic's own documentation lists as things Claude Code treats as needing a
person's decision, not something it decides alone even when it's otherwise working through a task
without stopping to ask about every small step. That's a deliberate safeguard, not a gap you need
to work around.

## How it signs in to GitHub, and why this matters

There are two separate sign-ins happening here, and it's worth being clear about which one is
which.

**Signing in to Claude Code itself** you've already done, since you're using it. Anthropic's own
documentation describes it plainly: "On first launch, Claude Code opens a browser window for you
to log in." That's your Claude account, and it's separate from GitHub entirely.

**Signing in to GitHub** is the one this page is actually about, because it's what lets Claude Code
clone a private repository, push a branch, or open a pull request as you. Claude Code doesn't have
its own separate GitHub identity. It uses whatever GitHub sign-in already exists on your machine,
the same one a plain `git` command would use, and the standard way to set that up is the **GitHub
CLI**, GitHub's own command-line tool, known as `gh`.

### Setting it up, once

You only do this once per machine. Ask Claude Code, in plain English:

```
Check whether the GitHub CLI is installed and signed in, and set it up if it isn't.
```

Here's what happens, so you recognise each step:

1. **If `gh` isn't installed yet**, Claude Code installs it. On Windows, that's the single command
   `winget install --id GitHub.cli --source winget`; on a Mac, it's `brew install gh`, GitHub's own
   published commands for each. Read what it proposes before you approve it, exactly as you would
   for anything else, covered in the next section.
2. **It checks whether you're already signed in** using `gh auth status`, GitHub's own command
   for this, described in its own documentation as testing "the authentication state of each known
   account" and reporting any issues. If you're already signed in, you're done, nothing else
   happens.
3. **If you're not signed in, it starts the sign-in process.** GitHub's own documentation is
   direct that the default here is "a web-based browser flow," not a token. A short code appears,
   an 8-character code with a hyphen in the middle, per GitHub's own description of this step, and
   a browser window opens (or you're told the address to open) at `github.com/login/device`. Sign
   in there if you're not already, type or paste the code you were shown, and confirm.
4. **Claude Code tells you when it's connected.** From here on, cloning, pushing, and opening pull
   requests against repositories you have access to work without asking you to sign in again.

**Screenshot placeholder:** the `github.com/login/device` confirmation page, showing the field
where the short code goes and the **Continue** or **Authorize** button, so a reader recognises it
the first time they see it.

**Why this beats a personal access token, and this is GitHub's own guidance, not just this kit's
preference.** GitHub's documentation opens its token-management page with a direct warning: "Treat
your access tokens like passwords," going on to say "Personal access tokens are like passwords, and
they share the same inherent security risks." Its own recommendation for exactly this situation:
"To access GitHub from the command line, you can use GitHub CLI or Git Credential Manager instead
of creating a personal access token." The browser sign-in above is that safer path. It never shows
you a long string of characters you could accidentally paste somewhere it shouldn't go, and if you
ever need to revoke access, you do it from your own GitHub account settings rather than hunting for
where a token got typed or saved. If anything you're doing seems to be pushing you toward creating
a token instead, stop and ask this kit's guide, or the browser sign-in above, rather than doing it.

**If a repository is public**, none of this is needed just to look at it or get a copy of it,
public means no sign-in is required to read. It only matters the moment you want to push a change
back, to a public or a private repository either way.

## Asking it for the everyday things, in plain language

You never need to know the underlying git command. Describe the outcome, the way you'd say it out
loud. A few you'll use constantly, each covered in full in its own file:

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

## Reading what it proposes before you approve it

This is the one habit that makes everything above safe to actually use, so it earns its own
section rather than a passing mention.

Anthropic's own security documentation states the principle plainly: "Claude Code only has the
permissions you grant it. You're responsible for reviewing proposed code and commands for safety
before approval." In practice, that plays out two ways:

**Sometimes it stops and shows you exactly what it wants to do, and waits for a yes.** When that
happens, actually read it, the file it's about to touch, the command it's about to run, the branch
it's about to push to, before you approve. A proposal that goes further than what you asked (a
second file you didn't expect, a different branch than the one you named) is exactly the moment
this step exists to catch. Saying yes without reading is the same risk as clicking through a dialog
box without reading it: usually fine, occasionally the one time it wasn't.

**Sometimes, on the Max plan, it just goes ahead with routine, low-risk steps without stopping to
ask each time**, because a separate background check reviews the action instead of interrupting
you. This is the normal, built-in way Claude Code behaves on this plan, not a setting you turned on
by accident. It's what makes everyday steps like committing or pushing to your own branch feel
instant rather than click-by-click. The two boundaries mentioned above, no unreviewed pull request
merges, no quiet force-pushes, still hold regardless.

**If you'd rather see every single step while you're still learning**, you can ask for that
directly: press `Shift+Tab` inside the Claude Code window to cycle to the mode Anthropic labels
**Manual**, which stops and asks before anything that edits a file, runs a command, or reaches the
network. Note that asking Claude Code in chat to switch modes doesn't work, per Anthropic's own
documentation, `Shift+Tab` is the way. Switch back the same way once you're comfortable.

## When the browser is the better tool, not Claude Code

Both are legitimate. This page adds three situations specific to working through Claude Code, on
top of the general table already in `05-daily-workflow.md`:

| Situation | Use |
|---|---|
| Anything on this page's "will never do" list: 2FA, org membership, billing, deleting or transferring a repository | Browser, signed in as yourself |
| Actually reviewing a pull request, reading a diff line by line before you approve it | Browser, per `07-pull-requests.md`, it's built for exactly this |
| You're not sure what a proposal is about to do and reading it back to yourself didn't clarify it | Ask Claude Code to explain it in plain English first; if that still doesn't land, do the step in the browser instead where you can see it happen |
| First time doing something on this page | Do it once in the browser so you've seen the click path, then let Claude Code handle it from then on |

## What to do when it gets stuck

**If it seems frozen mid-step**, press `Ctrl+C` to cancel whatever it's currently doing. This
doesn't lose your conversation, and you can tell it to try again, or try a different way.

**If closing the window feels like the only option**, that's fine too. Anthropic's own
documentation confirms directly: "Restarting doesn't lose your conversation." Reopen Claude Code
from the same project folder and ask it to pick back up where you left off.

**If it's specifically stuck on a GitHub step**, ask it directly what's blocking it and read the
answer back rather than guessing. A few genuinely common causes:

- **It says it can't push, or can't see a private repository.** This is almost always the
  authentication step above not having been completed, or completed for a different GitHub
  account than the one that actually has access. Ask it to run the `gh auth status` check again
  and tell you what account it's signed in as.
- **It's hit a merge conflict it can't resolve on its own.** That's expected sometimes, not a
  failure. `08-merge-conflicts.md` covers what a conflict actually is and how to work through one,
  whether you finish it with Claude Code's help or switch to the browser to see it laid out
  visually.
- **It genuinely doesn't know what to do next.** Tell it plainly, and it will usually tell you
  plainly back rather than guess. If two or three attempts at explaining still haven't unstuck it,
  that's the moment to fall back to the matching browser steps in this kit instead, they'll always
  get you there even when the shortcut doesn't.

---

## If it goes wrong

**It asked me to approve something and I don't understand what it's about to do.** Ask it to
explain in one plain sentence what will actually change, and where. If the explanation still
doesn't make sense, say no and do that specific step in the browser instead, where you can see it
happen directly.

**I set up the GitHub CLI sign-in once already, and it's asking me to sign in again.** Sign-ins can
expire or be revoked on GitHub's side. Ask Claude Code to run the check again ("check whether I'm
signed in to GitHub") and follow the browser prompt the same way as the first time, it's the same
short process, not a sign anything's broken.

**It made a change I didn't ask for, or touched a file I wasn't expecting.** This is exactly what
reading its proposal before approving is for. If it already happened, ask it to undo just that
specific change and explain what it did, rather than guessing yourself. If you're not confident the
undo is clean, that's a good moment to check the file in the browser directly before doing anything
else.

---

## Questions people ask here

**Do I have to use Claude Code at all? Can I just do everything in the browser?** Yes, entirely.
Nothing in this kit requires Claude Code. It's offered because it's genuinely faster for some tasks
and because every member here already has it on the Max plan, not because the browser path is
second-best.

**Is Claude Code acting as a separate GitHub account, or as me?** As you. It uses your own GitHub
sign-in on your machine, so any commit, push, or pull request it makes shows up under your account,
exactly as if you'd typed the commands yourself.

**What if I'm on a shared or work computer and don't want to leave GitHub signed in there?** Sign
out when you're done, from GitHub's own settings covered in `01-accounts-and-security.md`, or ask
Claude Code to sign you out of the GitHub CLI. The sign-in above is tied to that machine, not to
Claude Code itself.

**Does it cost anything extra to have Claude Code do GitHub work instead of me clicking through the
browser?** That's a question about your specific Claude plan and usage, not something this training
kit tracks, check your own account's usage or billing page for a current answer.

**Can it do something to GitHub I didn't ask for, on its own, out of nowhere?** No. Anthropic's own
documentation is direct on this: "Claude Code only has the permissions you grant it." Everything it
does on GitHub traces back to something you asked for, which is exactly why reading what it
proposes, covered above, is worth the ten seconds it takes.

---

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
