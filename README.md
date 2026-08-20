# GitHub training

Everything you need to use GitHub properly, written for people who run a business rather than write
software.

You can use this two ways. Read it like a set of guides, in your browser, with nothing installed. Or
install it into Claude Code, and then just ask your questions out loud and it walks you through the
answer one step at a time. The second way is the better way, and the setup takes a few minutes.

## Before you start

You need very little. Listed here so you can check rather than find out halfway through.

**For reading the guides**

- A web browser. That is genuinely all.
- A GitHub account, if you want to follow along and do the steps rather than only read them. If you do
  not have one, [the first topic](topics/01-accounts-and-security.md) starts by making one.
- An email address you check regularly and will still have in a year. This matters more than it sounds.
  Every invitation and every security message goes there, and changing it later is a nuisance.

**For the interactive version, additionally**

- Claude Code, on the Max plan. Everyone in this community has this already.
- About five minutes for the setup below.

**What you do not need**

- You do not need to know how to code.
- You do not need to install git, or a terminal, or any developer software. Everything in the guides is
  done in a normal web browser.
- You do not need to pay GitHub anything to follow this. Where a paid plan changes what you can do, the
  guides say so at that point.

## Setting up the interactive version

This puts the kit inside Claude Code, so it can answer your GitHub questions directly, look things up
in these guides, and take you through a task one step at a time.

There are two ways in. The first one is better, because it can update itself later. The kit gets
corrections and new material, and you want those without doing the setup again.

### The recommended way

If you have Claude Code open, ask it in your own words:

```
Please install the GitHub training kit by cloning
https://github.com/selrai-company/github-training-content
into my Claude Code skills folder, in a folder named github-wizard.
```

Read what it says it is about to do before you approve it. That is a good habit everywhere, not only
here.

If you would rather run it yourself, this is the whole thing:

```
git clone https://github.com/selrai-company/github-training-content ~/.claude/skills/github-wizard
```

On Windows that same command works in Git Bash. If you have never used a terminal, use the Claude Code
route above instead and let it do this part.

Then restart Claude Code.

### The fallback, if the above will not work

You can download the kit as a file instead. It works exactly the same, with one real cost: **it cannot
update itself.** When the kit changes, you have to download it again and replace the folder.

1. On [the front page of this repository](https://github.com/selrai-company/github-training-content),
   look near the top for a green button offering to give you the code, and choose the option to
   download a ZIP file. If the buttons do not match this description, read what they actually say and
   use the one that downloads.
2. Unzip it. You will get a folder.
3. Find your Claude Code skills folder. On Windows it is `C:\Users\<your name>\.claude\skills` and on a
   Mac it is `~/.claude/skills`. If there is no `skills` folder, make one with exactly that name.
4. Put the unzipped folder inside it and rename the folder to `github-wizard`.
5. Restart Claude Code.

### Checking it worked

Ask Claude Code something only this kit would know, such as:

```
What is in the practice folder of the GitHub training?
```

If it tells you about a pretend cafe's opening hours, it is installed. If it gives you a general answer
about GitHub, it is not, and the most common reason is that Claude Code has not been restarted since
you put the folder in place.

### Keeping it up to date

The kit gets corrections. When something in GitHub changes, or a mistake is found, the fix lands here
and you want it.

If you installed the recommended way, one command brings you current:

```
cd ~/.claude/skills/github-wizard && git pull
```

Then start a new Claude Code conversation. This part matters: the kit is read when a conversation
starts, so updating in the middle of one will not change the answers you are already getting. If you
update and keep going in the same window, you will still see the old behaviour and think the update
failed.

If you installed the fallback way, download the ZIP again and replace the folder, then restart.

### Using it once it is installed

You do not need to remember a command. Ask the way you would ask a person:

- "Set my team up on GitHub"
- "I accidentally committed a password, what do I do"
- "What is a pull request"
- "Someone left, how do I remove their access"
- "Is my repository public"

And if you do not know what to ask, which is the normal starting point rather than a problem, say so:

- "I do not know where to start with GitHub"

It will ask where you are, put you on a short path of five things that everyone needs, and take the
first one with you. At the end of every answer it tells you the next question to ask, so you never have
to work out what to want next.

It works one step at a time and waits to hear what is on your screen, because the point is to get you
through the task rather than to recite a manual at you.

If it does not know something, it will say so rather than guess. That is deliberate. A confident wrong
instruction is worse than no instruction, because afterwards you cannot tell which of the earlier
answers to trust.

## The topics

Twenty-four topics. Work down them in order if you are new, or jump straight to the
one that matches your problem. The [dashboard](dashboard.html) does the same thing with a search box.

### Start here

Do these four in order. They are the setup everything else assumes.

| Topic | Read this when |
| --- | --- |
| [Your GitHub account, and locking it down](topics/01-accounts-and-security.md) | You are setting up, or you are worried about getting locked out |
| [Organizations, and when you actually need one](topics/02-organizations.md) | You want to know what an organization is and whether you actually need one |
| [Adding people, and giving them the right access](topics/03-members-and-access.md) | Someone else needs access, or someone is leaving |
| [Repositories, and the public or private choice](topics/04-repositories-and-visibility.md) | You are making a place to keep work, and choosing who can see it |

### Doing the work

The everyday loop, and changing things without breaking them.

| Topic | Read this when |
| --- | --- |
| [The everyday workflow, and getting work in and out](topics/05-daily-workflow.md) | You want the normal loop: get a copy, change it, save it |
| [Branches, and changing things without breaking them](topics/06-branches.md) | You want to change something without breaking what everyone else sees |
| [Pull requests, and getting a change reviewed](topics/07-pull-requests.md) | You want a change looked at before it lands |
| [Merge conflicts, and what to do when git asks you a question](topics/08-merge-conflicts.md) | Two changes disagree and you are being asked to decide |
| [Forks, and practising without breaking anything](topics/09-forks-and-contributing.md) | You want to practise, or contribute to something that is not yours |

### Keeping it safe and tidy

Protecting the work, tracking it, and finding it again.

| Topic | Read this when |
| --- | --- |
| [Protecting the main copy, and what it costs](topics/10-protecting-your-work.md) | You want to stop changes landing on the main copy unchecked |
| [Issues, and keeping track of what needs doing](topics/13-issues-and-tracking-work.md) | You are losing track of what needs doing |
| [Finding things again, without hunting](topics/15-finding-things.md) | You cannot find something you know is in there |
| [Notifications, and not drowning in them](topics/16-notifications.md) | Your inbox is drowning you, or you are missing things that matter |
| [Markdown, and writing things people can actually read](topics/14-markdown-and-writing.md) | You are writing a README, an issue, or a description |

### Growing up

What you reach for as the business gets bigger.

| Topic | Read this when |
| --- | --- |
| [Releases and versions, marking what you shipped](topics/17-releases-and-versions.md) | You need to mark which version went out, and when |
| [Automation, what GitHub can do while you sleep](topics/18-automation-basics.md) | You are wondering what GitHub can do automatically for you |
| [The security features that watch your back](topics/19-security-features.md) | You want to know what is watching your back, and what is not |
| [Who owns what you put on GitHub, and how licences work](topics/20-licences-and-ownership.md) | You want to know who owns the work, and what a licence decides |
| [Moving work you already have into GitHub](topics/21-moving-your-work-in.md) | Your work is stuck on one laptop and needs to move |

### Staying in control

Undoing, backing up, and knowing what else exists.

| Topic | Read this when |
| --- | --- |
| [Undoing things, and getting back to how it was](topics/22-undoing-things.md) | You made a mistake and want to know if it can be undone |
| [Backups, exports, and never being locked in](topics/23-backups-and-leaving.md) | You want to know you are not locked in, and could leave |
| [The rest of GitHub, and what is worth your time](topics/24-the-rest-of-github.md) | You want to know what else is there and whether to bother |

### When you are stuck

The two to bookmark.

| Topic | Read this when |
| --- | --- |
| [When it goes wrong, and how to get unstuck](topics/12-when-things-go-wrong.md) | Something has broken and you need it fixed now |
| [Using GitHub through Claude Code](topics/11-github-with-claude-code.md) | You would rather ask Claude Code than click around a browser |

## Beyond the step by step

Two documents that cut across all the topics:

- **[The strategy pack](STRATEGY-PACK.md)** is the judgement layer rather than the mechanics: what to do
  first, whether you even need an organization yet, what changes at three people and at five, how much
  process is the right amount, and what good looks like months later. It carries three worked scenarios,
  including a sole operator and a six week contractor.
- **[The FAQ pack](FAQ-PACK.md)** answers the questions directly, including the ones people would rather
  not ask out loud: what actually is git and how is it different from GitHub, can anyone see my work,
  will this cost me money without warning, do I need to know how to code.

## The written guides

If you would rather follow one page start to finish than read by topic:

- [GitHub 101, written guide](guides/github-101-written-guide.md) and its
  [checklist](guides/github-101-checklist.md)
- [Branching and pull requests, written guide](guides/branching-and-pull-requests-written-guide.md) and
  its [checklist](guides/branching-and-pull-requests-checklist.md)

The checklists are meant to be copied and kept beside you while you work.

## Practise without breaking anything

The [practice folder](practice/) holds two files about a cafe that does not exist. Nothing uses them and
nothing depends on them, which is exactly the point: you can change anything in there, get it wrong, and
it costs nothing.

The first time you change something on GitHub, the screen asks questions you have not seen before and it
is hard to tell which answer is safe. Better to have that moment here, on a cafe that is not real, than
on something your business depends on.

**[Open the practice folder](practice/)** and it walks you through four things to try, in order, starting
with a two minute one. It explains each new word at the point you first need it, so you are not expected
to already know what a fork or a branch is.

You cannot damage anything by doing this. You work in your own copy, and you have not been given the
access needed to change this original, so the system refuses rather than letting you make a mistake.

## How this was built, and how far to trust it

**Everything here comes from GitHub's own documentation.** Every topic page ends with the exact pages it
was built from, so you can check any claim yourself rather than taking our word for it.

**Where GitHub does not publish something clearly, we do not guess on your behalf.** The page tells you
to look at your own screen and read what is actually there. That happens more than you might expect,
because GitHub changes its interface and does not document every corner of it. A confident wrong
instruction is worse than no instruction, because after you follow one you cannot tell which of the
earlier ones to trust.

**All twenty-four topics are written.** The tables above are the complete list. Where GitHub does
not publish something clearly, the relevant page says so and tells you to read your own screen,
and every one of those is collected in [what we could not verify](topics/GAPS.md).
