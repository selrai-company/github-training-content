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

This puts the kit inside Claude Code so it can answer your GitHub questions directly, look things up in
these guides, and take you through a task step by step.

### The short way, if you have Claude Code open

Ask it, in your own words:

```
Please install the GitHub training kit from
https://github.com/selrai-company/github-training-content
into my Claude Code skills folder, then tell me when it is done.
```

Claude Code can fetch it and put it in the right place. Read what it tells you it is about to do before
you approve it, which is a good habit generally and not only here.

### The manual way, if you would rather do it yourself

1. On [the front page of this repository](https://github.com/selrai-company/github-training-content),
   find the green button near the top that offers to give you the code, and choose the option to
   download it as a ZIP file. If the buttons have changed since this was written, read what they
   actually say and use the one that downloads.
2. Unzip the file you downloaded. You will get a folder.
3. Find your Claude Code skills folder. On Windows it is `C:\Users\<your name>\.claude\skills`. On a Mac
   it is `~/.claude/skills`. If the `skills` folder is not there, make one with exactly that name.
4. Copy the unzipped folder into it, and rename it to `github-wizard`.
5. Restart Claude Code.

You will know it worked when you ask Claude Code a GitHub question and it answers using these guides
rather than from general knowledge. A quick way to check is to ask it something specific to this kit,
such as "what does the practice folder in the GitHub training contain".

### Using it once it is installed

You do not need to remember a command. Ask your question the way you would ask a person:

- "Set my team up on GitHub"
- "I accidentally committed a password, what do I do"
- "What is a pull request"
- "Someone left, how do I remove their access"
- "Is my repository public"

It will ask you a couple of questions first, to find out where you actually are before it starts giving
instructions. Answer them plainly. It works one step at a time and waits to hear what you see on your
screen, because the point is to get you through the task rather than to recite a manual at you.

If it does not know something, it will say so rather than guess. That is deliberate. A confident wrong
instruction is worse than no instruction, because you cannot tell which of the earlier answers to trust
afterwards.

## The topics

Read these in order if you are starting from nothing. Jump straight to one if you have a specific
problem.

### Getting set up

| Topic | Read this when |
| --- | --- |
| [Your account, and locking it down](topics/01-accounts-and-security.md) | You are setting up, or you are worried about getting locked out |
| [Organizations](topics/02-organizations.md) | You want to know what an organization is and whether you actually need one |
| [Adding people, and the right access](topics/03-members-and-access.md) | Someone else needs in, or someone is leaving |
| [Repositories, public or private](topics/04-repositories-and-visibility.md) | You are making a place to keep work, and choosing who can see it |

### Doing the work

| Topic | Read this when |
| --- | --- |
| [The everyday workflow](topics/05-daily-workflow.md) | You want the normal loop: get a copy, change it, save it |
| [Branches](topics/06-branches.md) | You want to change something without breaking what everyone else sees |
| [Pull requests](topics/07-pull-requests.md) | You want a change looked at before it lands |
| [Merge conflicts](topics/08-merge-conflicts.md) | Two changes disagree and you are being asked to decide |
| [Markdown, and writing things people can read](topics/14-markdown-and-writing.md) | You are writing a README, an issue, or a description |

### Still being written

Forks and practising safely. Protecting the main copy. Using GitHub through Claude Code.
Troubleshooting. Issues and tracking work. Finding things again. Notifications. Releases and versions.
Automation. The security features. Licences and who owns what. Moving existing work in. Undoing things.
Backups and never being locked in. The rest of the platform.

They appear in the tables above as they land, so the tables are always the accurate list of what
exists.

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
was built from, so you can check any claim yourself rather than taking our word for it. There are
currently ninety-three such sources across the pages.

**Where GitHub does not publish something clearly, we do not guess on your behalf.** The page tells you
to look at your own screen and read what is actually there. That happens more than you might expect,
because GitHub changes its interface and does not document every corner of it. A confident wrong
instruction is worse than no instruction, because after you follow one you cannot tell which of the
earlier ones to trust.

**This kit is being written in the open and it is not finished.** The tables above are the accurate list
of what exists right now, and the section marked "still being written" is the honest list of what does
not. Where something is not covered yet, it is missing rather than covered badly. That is a deliberate
choice, and this note goes away when the last topic lands.
