# GitHub training kit

Start on this page. Everything else in this folder builds on it.

## What this kit actually is

A step by step guide to running your business on GitHub: setting up your account safely,
deciding whether you need a shared organisation, adding your team with the right access, and
the everyday habit of making a change, getting it looked at, and landing it without breaking
what everyone else sees. It is written for a business owner, not a developer. Nothing in it
requires you to write code.

Every fact that comes from GitHub itself is checked against GitHub's own published pages, not
guessed. Where GitHub's own screen might say something different by the time you get there,
the file tells you so and says exactly what to look at on your own screen instead of trusting
the page blindly.

## You already have Claude Code, and that changes which path you take

Every member of this kit has Claude Code on the Max plan. Almost every task below can be done
two ways: clicking through your browser, or describing what you want to Claude Code in plain
English and letting it type the commands for you. Each file tells you, task by task, which one
to use and why, and sometimes both. You do not need to know git or the command line either
way. Two things always stay in your browser, signed in as yourself, no matter what: anything
tied to your identity (two-factor authentication, recovery codes) and anything tied to billing
or account creation (making an organisation, inviting or removing a member). Those files say so
plainly each time.

## New to GitHub? Start here, in this order

Read these twelve, in order, over however many sittings you need. Each one says at the top what
you should already know before you start it.

1. **`01-accounts-and-security.md`** - Create your account and lock it down. Do this first,
   always, even if you plan to work alone. About fifteen minutes.
2. **`02-organizations.md`** - What a shared organisation account is, and the one real reason
   you'd want one. Most solo owners can skip creating one for now and come back once the
   trigger in this file actually happens to them.
3. **`04-repositories-and-visibility.md`** - Create your first repository, and get the public
   versus private choice right the first time.
4. **`03-members-and-access.md`** - Add your team, and give each person the narrowest access
   that lets them do this week's job. Skip this one if you're working alone for now.
5. **`05-daily-workflow.md`** - The everyday loop: getting a copy of a repository, making a
   change, saving it properly, and keeping your copy current.
6. **`06-branches.md`** - Working on a private copy of your project so a mistake can never
   reach the version everyone else sees.
7. **`07-pull-requests.md`** - Getting a change looked at, and the three ways to bring it in.
8. **`08-merge-conflicts.md`** - What to do when two people change the same thing at once. It
   is not an error, and this file shows you exactly what to click.
9. **`10-protecting-your-work.md`** - Stopping people (including yourself, if you want) from
   pushing straight to your main copy without a second look first.
10. **`09-forks-and-contributing.md`** - What to do when you want to change something you don't
    own, like a template or another team's project.
11. **`11-github-with-claude-code.md`** - Everything above, pulled together as what Claude Code
    can and cannot do for you, and how to check its work before you approve it.
12. **`12-when-things-go-wrong.md`** - Bookmark this one before you need it. Ten real situations,
    what to do about each right now, and exactly when to stop and ask rather than guess.

Once those twelve feel comfortable, five more files cover things you'll want the first time a
specific need comes up, not before: `13-issues-and-tracking-work.md` (tracking what needs
doing), `14-markdown-and-writing.md` (writing something people can actually scan),
`15-finding-things.md` (search, once you have more than a couple of repositories),
`16-notifications.md` (keeping your inbox useful instead of noise), and
`17-releases-and-versions.md` (marking "this exact version is what went out").

Two more files sit underneath all of this rather than in the reading order:

- **`STRATEGY-PACK.md`** teaches judgement, not clicks: whether you need an organisation yet,
  how much process is worth the friction at your team's size, and three real setups followed
  through end to end. Read it once you're actually deciding something, not while you're still
  learning where the buttons are.
- **`FAQ-PACK.md`** is a lookup, not a lesson. Search it for the exact question you have, get
  one answer, and stop. It does not need to be read in order or in full.

## Know what you're stuck on? Jump straight there

If you already know your problem, skip the reading order and go straight to the file that
answers it.

| What's going on | Open this |
|---|---|
| I'm locked out of my account, or lost my two-factor device | `01-accounts-and-security.md`, then `12-when-things-go-wrong.md` |
| I don't know if my business needs a shared organisation yet | `02-organizations.md`, or `STRATEGY-PACK.md` |
| I need to add someone, remove someone, or fix who can see what | `03-members-and-access.md` |
| I'm not sure whether my repository should be public or private | `04-repositories-and-visibility.md` |
| I made a change and don't know how to save it or send it up | `05-daily-workflow.md` |
| I want to try something risky without touching the real work | `06-branches.md`, or the practice repository linked below |
| Someone needs to check my change before it goes live | `07-pull-requests.md` |
| My screen is showing weird lines with `<<<<<<<` and `=======` | `08-merge-conflicts.md` |
| I want to change something I don't own, like a vendor's template | `09-forks-and-contributing.md` |
| I want to stop changes landing on the main copy without a second look | `10-protecting-your-work.md` |
| I want Claude Code to do the GitHub part instead of me clicking | `11-github-with-claude-code.md` |
| Something broke, or I'm not sure what to click next | `12-when-things-go-wrong.md` |
| I need to track a task, a bug, or a "someone please fix this" | `13-issues-and-tracking-work.md` |
| My text, table, or checklist isn't rendering right | `14-markdown-and-writing.md` |
| I know something exists but I can't find it again | `15-finding-things.md` |
| My notifications are noise and I've stopped checking them | `16-notifications.md` |
| I need to mark "this exact version is what we shipped" | `17-releases-and-versions.md` |
| I typed a specific question and just want one answer | `FAQ-PACK.md` |
| I'm deciding something (org or not, how much process, what to name things) | `STRATEGY-PACK.md` |

## Practising without risk

There is a public practice repository built for exactly this, at
`https://github.com/selrai-company/github-training-content`. It holds nothing real. Get a copy
of it, break it, open a pull request against it, build yourself a merge conflict on purpose,
before you try any of this on work that actually matters. Several of the files above point you
here directly when the moment is right.

## Before you record anything

`GAPS.md`, in this same folder, lists every fact in this kit that could not be confirmed word
for word against GitHub's own documentation and was instead left as "check your own screen."
Skim it before you go live or record a walkthrough, so you already know which exact screens to
look at rather than read a line from this kit and assume it still matches what GitHub shows
today.
