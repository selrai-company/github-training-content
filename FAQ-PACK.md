# GitHub FAQ: your questions answered

This page is a lookup, not a lesson. Find the question closest to yours and read that one answer.
You do not need to read this page in order, and you do not need to read the rest of it to
understand any single entry.

Every fact on this page that comes from GitHub itself is checked against GitHub's own published
documentation, most recently on 17 to 18 August 2026. GitHub's screens change over time. Where this
page cannot confirm something from GitHub's own words, it says so plainly and tells you what to
look at on your own screen instead of guessing.

**A few words used throughout this page, explained once:**

- **Repository** ("repo" for short): a folder GitHub tracks for you. Every change anyone makes to a
  file inside it is kept, so you can always see what changed, when, and who changed it.
- **Organization**: a shared account that sits above your personal account, so a team can hold
  access to code together instead of it belonging to one person.
- **Commit**: a saved snapshot of a change, with a note (the commit message) saying what changed.
- **Branch**: a private copy of a repository's contents that you can change without touching what
  everyone else sees, until you deliberately bring your changes back in.
- **Pull request**: a proposal to bring a branch's changes into the main version, so someone can
  look at it before it lands.
- **Fork**: your own separate copy of someone else's repository, used when you do not have
  permission to change the original directly.
- **Clone**: a full copy of a repository on your own computer that stays connected to GitHub, so you
  can pull down new changes later.
- **Two-factor authentication (2FA)**: signing in needs your password and a second proof it is
  really you, usually a six-digit code.

## Jump to a section

1. [Getting started and signing in](#getting-started-and-signing-in)
2. [Accounts, security, and being locked out](#accounts-security-and-being-locked-out)
3. [Organizations, and whether I need one](#organizations-and-whether-i-need-one)
4. [People, access, and who can see what](#people-access-and-who-can-see-what)
5. [Repositories, and public versus private](#repositories-and-public-versus-private)
6. [Everyday work: getting files, changing them, saving them](#everyday-work-getting-files-changing-them-saving-them)
7. [Branches and pull requests](#branches-and-pull-requests)
8. [When something goes wrong](#when-something-goes-wrong)
9. [Money and plans](#money-and-plans)
10. [Privacy, security, and what I am exposing](#privacy-security-and-what-i-am-exposing)
11. [Doing it through Claude Code](#doing-it-through-claude-code)
12. [Questions people are embarrassed to ask](#questions-people-are-embarrassed-to-ask)

---

## Getting started and signing in

### How do I create a GitHub account?

Go to github.com/signup and follow the prompts, or use the "Continue with Google" shortcut if you
have a Google account. Verify your email address when GitHub asks. GitHub's own words are direct
about this step: "Without a verified email address, you won't be able to complete some basic GitHub
tasks, such as creating a repository." Do this first, not last. Full detail on choosing an email and
a username is in this kit's accounts and security guide.

### What email address should I use?

Use one you expect to control for years, not one tied to a job or a phone number you might lose. You
can always add a second address to the same account later. If you want your real email kept out of
public view when you commit through the browser, turn on "Keep my email addresses private" in your
email settings, and GitHub generates a stand-in address for you automatically.

### What username should I pick, and can I change it later?

Pick something you are reasonably happy to keep. Usernames are first-come, first-served, and GitHub
does not hold names for you or release a taken one except in a trademark dispute. You can change it
later, but GitHub is specific that it is not free of cleanup: your old username becomes available for
anyone else to claim, most links to your repositories redirect automatically but not everything does,
and any gist or profile links using the old name stop working with a 404 error. Change it if you need
to, just know there is real tidy-up attached.

### Do I need to install anything before I start?

No. Every member of this kit has Claude Code on the Max plan, and everything in this training set is
either a browser click or a plain-English request to Claude Code. Nothing requires you to install
git yourself, open a command line, or know what either of those things is.

### I was told to get this week's build. Where do I start?

This depends on how your specific community currently delivers it, and that varies. Check the most
recent posting or pinned instructions in your community for the current method rather than assuming
one, since the exact delivery mechanic is something this page cannot confirm as a single fixed
answer. If you are handed a link to a repository and told to "get a copy," the everyday work section
of this page covers both ways to do that.

### Someone sent me a link to a GitHub repository. What do I do with it?

Open the link. If you only need to look at the files once, use the green Code button and Download
ZIP, covered in the everyday work section below. If you expect to come back to it, ask Claude Code to
clone it for you instead, so it stays connected and you can pull new changes later without
downloading everything again.

---

## Accounts, security, and being locked out

### How do I turn on two-factor authentication, and should I?

Yes, turn it on today, even if you are working alone with no releases planned. It takes about two
minutes. Go to your profile picture, top right, then Settings, then Password and authentication in
the Access section of the sidebar, then Enable two-factor authentication. Pick an authenticator app
if you can. GitHub says so directly: "We strongly recommend using a TOTP application for two-factor
authentication instead of SMS, and using security keys as backup methods instead of SMS."

### What are recovery codes, and why do they matter so much?

They are one-time backup codes GitHub gives you when you turn on 2FA. Each one works exactly once.
They exist for one job: getting you back into your account if you lose your phone or your
authenticator app. Save them the day you turn on 2FA, in a password manager or printed somewhere
safe, never a screenshot on the same phone that holds your authenticator app. GitHub's own wording is
the reason this matters: "GitHub Support will not be able to restore access to accounts with
two-factor authentication enabled if you lose your two-factor authentication credentials or lose
access to your account recovery methods." Not difficult. Not "contact us." Cannot.

### I lost my phone and I don't have my recovery codes. What do I do?

Work through this in order. Try any recovery codes you saved. Try another method you already set up,
such as a passkey or a security key. If neither works, GitHub Support genuinely cannot get your old
account back for you, by its own stated policy. The only documented path left is unlinking the email
address tied to the locked account so you can use that same address to start a new account. That
does not hand back your old repositories or history, it only frees the email address. This is why
recovery codes are step one in the accounts guide, not an afterthought.

### GitHub is asking me to verify a new device. Is that normal?

Yes, if you are signing in from a computer or browser GitHub does not recognize. A code goes to your
email, or to the GitHub Mobile app if you have it installed. Once you have verified a device, GitHub
only asks again on that same device if you clear your cookies or switch browsers. One thing worth
knowing: if a verification code arrives and you did not just try to sign in anywhere, that means your
password may have been compromised. Change it immediately.

### Will GitHub eventually force me to use 2FA?

For some actions, yes. Since March 2023, GitHub requires 2FA for accounts that publish a release,
publish an app others can use, contribute to certain high-importance repositories, or become an
organization owner. If your account is selected, you get a 45-day window to enable it, plus a further
7-day grace period. After that, GitHub's own wording is direct: "You will not be able to access
GitHub.com until you enable 2FA." Creating an organization is one of the actions that can trigger
this, so turning 2FA on voluntarily now means you never see that clock start.

### Is SMS two-factor safe to use in Australia?

It depends on GitHub's currently supported country list, which changes over time and is not a fixed
rule, so confirm your own country is on it at the moment you set it up rather than trusting a past
answer. Even where SMS works, GitHub's own guidance recommends an authenticator app over it, stating
SMS "is susceptible to interception, does not provide resistance against phishing attacks, has
unreliable deliverability, and is not supported in all countries." An authenticator app takes about
the same two minutes to set up and avoids all of that.

### Someone is asking for my GitHub code or password to "verify" my account. Is that real?

No. Nobody legitimate ever needs your 2FA code, your recovery codes, or your password read aloud to
them, not a client, not "GitHub verification," not a support agent. GitHub's own documentation
confirms that its own Support team "cannot assist with troubleshooting your 2FA methods." If a
message asks you to hand over a code, that request is the attack, not a fix for one. The safer habit
for sign-in links generally: never click a sign-in link from an email. Open a new tab and type
github.com yourself, every time.

### Can Claude Code set up my 2FA or hold my recovery codes for me?

No, and this is deliberate, not a limitation to work around. 2FA exists to prove a human is
physically present with a phone or a security key. A terminal assistant cannot scan your QR code or
hold your device, and it should not be trusted with your recovery codes even if it could. Every
identity and security action in this kit happens in your own browser, signed in as yourself.

### Is it OK to reuse a password I already use elsewhere?

Confirm GitHub's current password rules on your own screen at sign-up, since that can change and this
page will not repeat a number that could go stale. As a habit regardless of the minimum rule, do not
reuse a password across sites. If one site the password was used on ever leaks, every account sharing
it becomes exposed too, GitHub included.

---

## Organizations, and whether I need one

### What is an organization, in plain terms?

Your normal GitHub account is a personal account, with your name and face on it. An organization is a
separate, shared account that sits above personal accounts, so a team can share ongoing access to
code that does not disappear if one person leaves. Think of the difference between your own email
address and a shared company inbox. Nobody signs in to an organization directly; people sign in with
their own personal accounts and are given access to it.

### Do I actually need one?

Probably not, if you are working alone. A personal account already covers everything else in this
kit. The one real trigger for creating an organization is a second person needing ongoing, shared
access to your repositories, access that keeps working even when you are not around to grant it
yourself. "It looks more professional" or "I have a business name" is not that trigger. Skip it
until you actually have a second person to bring onto the code.

### What does a new organization cost?

A brand new organization lands on GitHub Free automatically, at no cost. On Free you get unlimited
collaborators on unlimited public repositories with the full feature set, unlimited private
repositories with a limited feature set, and 2,000 GitHub Actions minutes a month. You would only
look at a paid plan the day you specifically want a required check before a change lands on the main
version, which is a concrete reason, not "wanting more just in case."

### How do I create one?

Click your profile picture, top right, then Settings, then Organizations in the Access section of the
sidebar, then New organization, then follow the on-screen prompts. This is a browser-only step tied to
your billing and identity, so there is no shortcut through Claude Code for it, and GitHub's own
documentation does not publish the exact field list on that screen beyond "follow the prompts."
Confirm on your own screen what it actually asks for when you get there.

### Who becomes the owner?

Do not assume creating it automatically makes you the owner in a way you can rely on without
checking. Read your own role directly off the organization's People page once it exists, right next
to your name. Whoever sets it up through the normal flow does hold owner-level control, but confirm
it on screen rather than assuming from this page.

### Why do I need a second owner, and how soon?

Add one on day one, not eventually. GitHub's own wording is specific: the owner role "should be
limited, but to no less than two people, in your organization." If you are the sole owner and lose
access, your two-factor device, your password reset inbox, anything, there is nobody left with
authority to fix it. GitHub does not describe an emergency override for this. To promote someone:
Settings, Organizations, your organization, People tab, tick their name, open the "members selected"
dropdown, Change role.

### Can I rename an organization later?

Yes, only organization owners can. Most existing repository links keep working through an automatic
redirect. The old organization profile page stops working and shows a 404. The old name becomes
available for someone else once you have moved off it, so do not plan on reclaiming it later.

### How do I move an existing repository into my new organization?

Use a transfer, not a fresh copy, so history, issues, and pull requests all move with it. You need
administrator access to the repository and permission to create a repository in the target
organization. Open the repository's Settings, scroll to the Danger Zone, click Transfer, choose your
organization as the new owner, type the repository's name to confirm. This is browser-only; there is
no command-line shortcut for it.

### What happens if I leave an organization I created?

You can leave at any time, from Settings, Organizations, Leave. One gap worth knowing: if you were
responsible for billing, leaving does not hand that off to anyone else automatically. GitHub's own
wording: leaving "does not update the billing information on file for the organization." Sort out who
is paying before you click Leave, not after.

### How do I delete an organization completely?

Different from leaving: deletion removes it for everyone, and GitHub calls it irreversible, wiping
"all repositories, forks of private repositories, wikis, issues, pull requests, and project or
organization pages." Back up anything you want to keep first. From Settings, scroll to Danger zone,
Delete this organization, type the name to confirm. Treat this as an owner-only action.

---

## People, access, and who can see what

### What's the difference between an organization role and a repository role?

An organization role controls what someone can do to the organization itself, its billing, its
settings, its member list. A repository role controls what they can do inside one specific
repository. For a small business you will mostly choose between organization Owner and Member, and
between repository Read, Write, and Admin. One rule worth knowing: an organization owner automatically
gets admin access to every repository the organization owns, regardless of any lower role you set for
them individually.

### What's the "base permission" trap everyone falls into?

Base permissions are the org-wide default applied to every member on every repository. If you set it
to Write "so everyone can push without me adding each person to each repo," you have just given every
current and future member push access to everything, current and future, with no per-repo decision
involved. Most small teams should leave this at Read or No permission, and grant Write only on the
specific repositories where it is actually needed.

### How do I invite someone to my organization?

Profile picture, Organizations, your organization's name, People tab, Invite member, type their
username or email, pick their role, Send invitation. They get an emailed invite that expires after
seven days if not accepted. If it does not arrive, have them check spam first; if it has genuinely
expired, find it under Failed invitations on the People tab and retry.

### What's an outside collaborator, and when should I use one instead of a full member?

An outside collaborator has access to one or more of your repositories without being part of your
organization at all, the right fit for a one-off contractor with no ongoing relationship to your
team. Two facts change how you should use one: they cannot be added to a team under any circumstance,
and unless you are on the Free plan, they still use up one of your paid seats the same as a full
member would.

### What's a team, and how does access cascade?

A team grants the same access to a group of people at once instead of person by person. Only
organization members can be on one; outside collaborators cannot. If you nest a smaller team under a
larger one, the smaller team inherits the larger team's access automatically, and mentioning the
larger team notifies everyone in both.

### How do I remove someone, and what does that actually undo?

Profile picture, Organizations, your organization, People tab, tick their name, Remove from
organization. Removal stops future access. It does not reach onto their computer and delete anything
they already copied down. GitHub's own words: "Removed members will lose access to private forks of
your organization's private repositories, but they may still have local copies." If that matters,
that is a conversation to have with the person, not a button GitHub provides.

### If I remove someone, can they still see my code?

Not on GitHub going forward, and any private fork they personally made of your repository gets
deleted at the same time. But a copy already on their own computer is untouched, and if your private
repository had previously been forked into a different organization, that other organization
controls access to that copy independently of anything you do.

### Can I bring someone back after removing them?

Yes, within three months. GitHub keeps their old membership data for that window, so you can invite
them again and restore their previous role, access, and any private forks they owned. Past three
months, you are rebuilding their access from scratch.

### Does removing someone delete their personal GitHub account?

No. Your organization is a separate account they belong to, not their whole GitHub identity. Removing
them only removes access to your organization's repositories and settings. Their own account, and
anything on it unrelated to your organization, is untouched.

---

## Repositories, and public versus private

### What is a repository?

GitHub's own words: "A repository is the most basic element of GitHub. It's a place where you can
store your code, your files, and each file's revision history." It behaves like a shared project
folder with a very good memory, remembering every earlier version, not just the current one.

### How do I create one?

Click the plus icon, top right of any github.com page, New repository. Choose the owner, type a name,
choose visibility (read the next answer before you click), optionally turn on Add a README file. If
you already have the GitHub CLI installed and signed in, Claude Code can run `gh repo create
your-repo-name --public` or `--private` instead, which is a genuinely good shortcut because the
command makes you type the visibility explicitly rather than trust a radio button.

### Public or private, what's actually the difference?

GitHub's own definitions, exact: "Public repositories are accessible to everyone on the internet."
"Private repositories are only accessible to you, people you explicitly share access with, and, for
organization repositories, certain organization members." Read the public definition again: not
"anyone with the link," everyone on the internet, no account needed. If you are not certain, start
private. Going private to public later is reversible in the setting, but not in who has already seen
it.

### Which one is selected by default when I create a repository?

GitHub's own documentation for this screen never states a default, and the field is only described as
"Choose a repository visibility." Do not click through this step on autopilot. Look at your own screen
at the moment you create the repository and pick deliberately.

### What belongs in a repository, and what doesn't?

Belongs: your actual project files, a README explaining what the project is, a `.gitignore` file so
secrets never get tracked in the first place. Does not belong: passwords, API keys, tokens, or any
credential typed directly into a file that gets committed, and very large files, GitHub blocks
anything over 100 MiB outright and warns on anything over 50 MiB.

### How do I stop secrets from ever being committed?

Create a file named exactly `.gitignore` in your repository's root, before your first commit, and put
your `.env` files in it (`.env`, `.env.local`, `.env.*.local`). A `.env` file is the standard place a
project keeps its secrets while you work, so this one habit closes the most common leak before it
happens. `.gitignore` only stops files it does not already know about; a file already committed needs
a separate step to untrack, and that step alone does not erase it from earlier history.

### I already committed a password. What do I do?

Do not just delete the file in a new commit, it still sits in every earlier commit. Rotate the secret
first, immediately, in whatever service issued it. GitHub's own guidance says exactly this: as a first
step, "you need to revoke and/or rotate that secret." That single step closes the actual danger. Full
history cleanup afterward is a separate job, and this kit deliberately does not walk you through doing
it alone, since a botched rewrite can cause more damage than the leak did. Bring that part to the
community.

### Can I change a repository from private to public later, and back?

Yes, from Settings, Danger Zone, Change visibility, if you have the right permissions. Going private
to public exposes exactly what you would expect: the code becomes visible to everyone, and Actions
history becomes visible too. Going public to private erases stars and watchers and unpublishes any
GitHub Pages site, and existing forks stay public rather than turning private with you. Neither
direction undoes what already happened while the old setting was live.

### What's archiving, and how is it different from deleting?

Archiving makes a repository read-only without removing it, meant for a finished project you want to
keep exactly as it is. It can be reversed at any time from the same Danger Zone. Deleting removes it
entirely, and GitHub calls that action one that "cannot be undone." If you are not certain you will
never need something again, archive it instead.

### How do I delete a repository, and can I undo it?

You need admin access to the repository, or owner privileges on its organization. From Settings,
Danger Zone, Delete this repository, then confirm by typing its name. GitHub's own wording is careful
here: "some deleted repositories can be restored within 90 days of deletion," not every one. Do not
treat that window as a guarantee. If you delete something by mistake, act immediately and contact
GitHub support rather than assuming you have time.

### Can I share a private repository with one contractor without creating an organization?

Yes. Add them as a collaborator on that specific repository, from the repository's Settings, Access,
Collaborators, Add people. An organization is only worth the setup once several people need ongoing
access to more than one repository.

---

## Everyday work: getting files, changing them, saving them

### How do I get a copy of a repository onto my computer?

Two genuinely different ways, pick based on whether you will ever need to update the copy later. For
a one-time look, use the green Code button on the repository's page, then Download ZIP, no
installation needed. For anything you will come back to, ask Claude Code, in plain English, to clone
it for you, and read the folder path it tells you, do not skip past that.

### What's the difference between downloading a ZIP and cloning?

A ZIP is a one-time snapshot of the files as they exist right now. GitHub's own words: "snapshots
don't contain the entire repository history." There is no built-in way to update it, only to download
it again. A clone keeps the full history and stays connected to GitHub, so you can pull new changes
into the same folder later without redownloading everything.

### Where do the files actually end up on my computer?

If you downloaded a ZIP, wherever your browser saves downloads, usually a folder named Downloads, and
you need to extract it before it is usable. If Claude Code cloned it, wherever you were working when
you asked, and it will tell you the exact path. If you lose track of it, just ask: "Where did you put
the copy of [repository name] you cloned earlier?" Do not rely on memory for this, ask.

### How do I make a small edit through the browser?

Open the file on github.com, click the pencil icon (Edit file), make your change, scroll down and
write a commit message, choose whether to commit directly or start a pull request, click Commit
changes. If you do not have Write access to the repository, clicking Edit still works, but GitHub
makes you a personal copy (a fork) and proposes your change there instead, which is expected, not an
error.

### What is a commit, and what should I write in the message?

A commit is a saved snapshot of a change, permanent from the moment you make it. GitHub requires a
message but does not enforce a length or format, that part is up to you. Our recommendation, not a
GitHub rule: write it for the version of you, six months from now, with zero memory of today. "Fixed
it" tells that person nothing; "corrected Saturday opening hours" tells them everything they need.

### How do I get the newest changes down to my computer?

Depends how you got your copy. A ZIP has no ongoing connection, so there is no update step, only
downloading it again. A clone updates in place: ask Claude Code to "pull the latest changes." Commit
anything you have changed first, since pulling with uncommitted edits sitting around can get confused
about which version of a file to keep.

### Should I use the browser or Claude Code for a given task?

It depends on the task. Use the browser for a quick edit to a file you can already see and understand
on screen, or while you are still learning and want to see exactly what a click does. Use Claude Code
for getting a full connected copy of a repository, changing more than one file together, reviewing a
change before it is committed, or pulling down updates. Neither is more "correct," they produce the
same result; use whichever fits the moment.

### Do I need to know git commands to do any of this?

No. Everything on this page is either a browser click or a plain-English request to Claude Code.
Claude Code runs the underlying git commands for you; knowing their names is not required to use
them.

---

## Branches and pull requests

A branch is a private copy of a repository's contents you can change without touching what everyone
else sees. A pull request is a proposal to bring a branch's changes back into the main version, so
someone can look at the change before it lands.

### What is a branch, in plain terms?

Picture the main version of your project as a master document everyone relies on. Instead of
scribbling directly on it, you photocopy it, mark up the photocopy, and leave the original untouched
while you work. If the change turns out well, you swap it in later. If it does not, you bin the
photocopy and the original was never at risk. That photocopy is a branch.

### Why not just edit the main version directly?

Because mistakes on a branch cannot reach anyone else, and they are cheap to fix. GitHub's own
wording: "Your branch is a safe place to make changes. If you make a mistake, you can revert your
changes or push additional changes to fix the mistake." Nothing lands on the main version until you
take the deliberate step of merging it.

### How do I create a branch?

You need at least Write access to the repository. On the repository's main page, click the branch
dropdown, type a new name in the "Find or create a branch" field, click Create branch. Or through
Claude Code: "Make me a new branch called fix-homepage-typo, based on main." Name it after what it
does, in a few words with hyphens, `update-menu-prices` rather than `test` or `changes`, so a list of
ten branches still means something six months from now.

### How do I switch between branches?

Click the branch dropdown on the repository's main page and pick the one you want. No special access
needed beyond what you already have to view the repository. Through Claude Code, just ask: "Switch me
to the branch called update-menu-prices."

### What is a pull request?

GitHub's own words: "Pull requests are proposals to merge code changes into a project." It is
GitHub's key collaboration feature, letting people discuss and review a change before it lands in the
main version. You can also open one as a draft, which GitHub's own words describe plainly: "Draft
pull requests cannot be merged," useful for sharing work in progress before you are ready for a full
review.

### How do I open one?

On the repository's page, choose the branch with your commits from the branch menu, click "Compare &
pull request" in the yellow banner, pick the base branch you want to merge into, type a title and
description, click Create Pull Request. If you are proposing a change from your own fork of someone
else's repository, the extra step is clicking "compare across forks" so you can pick your fork as the
source.

### Who can merge it, and what are my options?

You need Write access on the target repository to merge, which is why proposing a change to a
repository you only have Read access on ends at "proposed and reviewed," someone with Write access
merges it, not you, and that is expected, not stuck. GitHub gives three merge methods: a merge
commit, which folds in every individual commit and is the method GitHub's own documentation names as
the default; a squash, which combines everything into one commit; and a rebase. This kit recommends
squash and merge for a small team's history, because it keeps one pull request as one clean line. That
is our recommendation, not GitHub's default, say so if you are teaching it to someone else.

### What's a merge conflict, and is it my fault?

It happens when you and someone else changed the same lines of the same file, and GitHub cannot tell
which version to keep automatically. It is normal and recoverable, not a sign anything broke and not
a personal failure.

### Can I fix a conflict myself in the browser?

Sometimes. GitHub's own words are exact about the limit: "You can resolve simple competing line change
conflicts on GitHub. For other conflicts, use the command line." Open the pull request, click Resolve
conflicts, pick the lines you actually want to keep and remove the conflict markers GitHub added
around them, click Mark as resolved for that file, then click Commit merge, that last click is the
step that actually finishes it. If the Resolve conflicts option is greyed out or the conflict is
bigger than a simple line change, that is not you doing something wrong, it is a documented limit.
Post which files are affected and ask someone with the command line for help rather than guessing your
way through it.

### What is a fork, and how is it different from a branch?

A branch is a copy inside the same repository, and anyone with access to that repository can see it.
A fork is a whole separate copy of the repository under your own account, typically used when you do
not have write access to the original at all. GitHub's own words: "Forks are repositories that start
as copies of another repository, called the upstream repository. A fork has its own settings and
permissions but stays connected to the upstream repository." Use a branch whenever you already have
write access to the repository you are working in; use a fork when you do not.

### How do I contribute to a repository I don't own?

Fork it (GitHub's own permission table places forking at the Read level, so ordinary access is
enough), branch and commit your change on your own fork, then open a pull request back to the
original repository, comparing your fork's branch to its base branch. GitHub's own description of
this whole loop: "If you want to contribute to someone else's project but don't have permission to
make changes directly, you can create your own copy of the project, make updates, and then suggest
those updates for inclusion in the main project." A maintainer of the original repository merges it,
not you, and waiting for that is normal, not stuck.

### What can I do with Read access versus Write access?

More than most people assume. GitHub's own role table places pulling a repository, forking it, and
sending a pull request from your fork all at the Read level. Write is what you need to push directly
to a repository, merge a pull request, or touch its Actions workflows and secrets. In plain terms:
Read is enough to propose a change to something you do not own; Write is what actually lands it.

### I deleted a branch by mistake. Can I get it back?

If that branch was the head branch of a pull request you had already closed or merged, yes: open that
pull request, click Restore branch near the bottom. If the branch never went through a pull request,
there is no documented way to bring it back through GitHub's interface. If you are unsure whether you
will want a branch again, the safer move is to leave it alone rather than delete it, an unused branch
sitting there costs nothing.

---

## When something goes wrong

### I did everything right and it still didn't work. What now?

Check what you actually see on screen against the step you were following, one step at a time, rather
than assuming the whole thing failed. GitHub's screens change, so if something does not match what a
guide describes, believe your own screen over the guide, and describe exactly what you see (the exact
words on a button or heading, not your interpretation of it) when you ask for help.

### GitHub refused to let me push or save my change. Is something broken?

Almost always no. It usually means you have Read access to that repository but not Write. That is
GitHub working correctly, not a bug. Check with whoever owns the repository about access, or, if you
are trying to contribute to a repository you were never meant to have write access to, use a fork and
a pull request instead, covered in the branches and pull requests section above.

### My invite never arrived.

Have them check spam and promotions folders first, that is the overwhelming majority of cases.
Invites expire automatically after seven days if not accepted. Past seven days, look under Failed
invitations on the organization's People tab and retry it, rather than assuming something is broken.

### I'm locked out of my account completely.

Work through it in order: your saved recovery codes, then any other method you already configured
such as a passkey, then formal account recovery if neither works. GitHub Support cannot troubleshoot
your 2FA methods by its own stated policy, so if both your device and your recovery codes are gone,
there is no support ticket that restores the original account. The only documented last resort is
unlinking your email so you can start a new account with it, which does not hand back your old
repositories or history.

### I made something public by mistake.

Flip it back to private from Settings, Danger Zone, Change visibility. Do that immediately, but treat
anything sensitive it held as seen: rotate any secret it contained in whatever service issued it,
since flipping visibility back does not undo who already saw or copied it while it was public.

### I hit a merge conflict I can't resolve in the browser.

That is a documented limit, not a mistake on your part. GitHub's own words: for anything beyond a
simple competing line change, "use the command line." Post which files are affected in your
community and get someone with a command line set up to help, rather than clicking around trying to
force it.

### I deleted something I need back.

It depends what you deleted. A branch tied to a closed pull request can be restored from that pull
request's page. A repository has a partial safety net, GitHub says "some" deleted repositories can be
restored within 90 days, not all, so act immediately and contact GitHub support rather than assuming
you have time. An organization's deletion is described as permanent, with no restore path documented.

### Can GitHub support fix a 2FA problem for me?

No, by its own stated policy: "For security reasons, GitHub Support cannot assist with troubleshooting
your 2FA methods, including SMS delivery." This is exactly why recovery codes matter so much, they
are the one thing that gets you back in when nobody else can.

### Who do I actually ask when I'm stuck?

For anything covered in this kit, ask in plain English, describing what you see on screen rather than
what you think went wrong. For a merge conflict too big for the browser, or anything genuinely
unusual, post it in the community with the specific detail (which file, which repository, the exact
wording of any error) rather than a general "it's not working," since the specific detail is what
lets someone actually help.

---

## Money and plans

### Does creating a GitHub account cost anything?

No. GitHub's own pricing page lists the Free plan at "$0 USD per month," described as free forever,
for personal accounts and for organizations.

### What does a free organization actually include?

Unlimited collaborators on unlimited public repositories with the full feature set, unlimited private
repositories with a limited feature set on those specifically, and 2,000 GitHub Actions minutes a
month, per GitHub's own account-types documentation. Required reviewers and some security tooling on
private repositories need a paid plan; the privacy of a private repository itself is not reduced on
Free.

### When would I actually need to pay for GitHub?

The concrete trigger is wanting a required check, a review that has to happen, before a change can
land on your main version of a private repository. GitHub's own confirmed wording: branch
restrictions work "in public repositories owned by a GitHub Free organization and in all repositories
owned by an organization using GitHub Team or GitHub Enterprise Cloud." In plain terms, that
protection is available on Free only for public repositories; a private repository needs Team or
above. Wanting more storage or more Actions minutes before you have actually run out is not a real
trigger, it is a guess.

### What does GitHub Team or Enterprise cost?

At the time this page was checked, GitHub's own pricing page lists GitHub Team at $4 USD per user per
month "for the first 12 months," and GitHub Enterprise Cloud starting at $21 USD per user per month,
also "for the first 12 months." Both figures carry that exact qualifier on GitHub's own page.

### Will the price go up later?

Possibly, and this page cannot confirm one way or the other. GitHub's own pricing page states both
Team and Enterprise Cloud prices as introductory, for the first 12 months, but does not publish what
the price becomes after that anywhere this page could find. Confirm the current renewal price on
GitHub's own pricing page before you commit to a paid plan, rather than assuming the introductory
number is the number you will pay in year two.

### Will I be charged automatically without warning?

The Free plan costs nothing and stays that way on its own, it is not something that turns into a
charge by itself. Moving to a paid plan (Team or Enterprise) is a deliberate action someone with
billing access takes from the organization's own settings, not something that happens passively while
you use the Free plan. What this page cannot confirm is the exact renewal behavior once an
introductory price period ends; check your organization's own billing settings for that rather than
assuming.

### What happens to a paid seat if I remove someone?

This page cannot confirm the exact seat-release behavior from GitHub's own documentation. Check your
organization's own billing settings page for the current answer before assuming a seat frees up
immediately.

### What happens if I stop paying?

It depends what "stop paying" means. If you let an organization's paid plan lapse rather than closing
the account entirely, this page cannot confirm the exact downgrade mechanics, check the
organization's own billing settings before assuming what happens to your data. If you cancel or delete
an account entirely, GitHub's own terms are specific: your profile and repository content are deleted
within 90 days of cancellation, described as unable to be recovered after that, though you can
request a copy of your own content within that same 90-day window. Content you contributed to someone
else's repository, or that someone else has forked, is not deleted along with your account.

---

## Privacy, security, and what I am exposing

### If my repository is private, is it really private?

For access, yes: nobody can see it except you, people you have explicitly given access to, and, for
an organization repository, certain organization members depending on that organization's own
settings. "Limited features" on the Free plan refers to things like required reviewers, not to
privacy itself being reduced. A private repository on Free is still private.

### Can GitHub's own staff see my private code?

Only in specific, stated circumstances, not routinely and not for browsing. GitHub's own Terms of
Service, Section E, name the circumstances plainly: for security purposes, for automated scanning or
manual review for known vulnerabilities or malware, to assist you with a support matter you raise, to
maintain the integrity of the service, or to comply with a legal obligation where there is reason to
believe the content violates the law. GitHub also states it will give notice about accessing private
content except where legal disclosure, a legal obligation, automated scanning, or an active security
threat prevents it.

### Does GitHub use my private code to train AI?

Only if you specifically use one of GitHub's own built-in AI features (this is about GitHub's own
tools, not about Claude Code, which is a separate product) and feed it your private repository content
as input. GitHub's Terms of Service state that input may then be used to "provide, develop, train, and
improve the Service, including AI Features," and that you retain an opt-out right under a separate
section of the same terms. If this matters to you, read that section of GitHub's own Terms of Service
directly before turning on any GitHub AI feature on a private repository.

### What happens to secrets I accidentally expose?

The danger closes the moment you rotate the secret in whatever service issued it, get a new key,
invalidate the old one, regardless of how many old commits still contain a copy of the leaked value.
Deleting the file in a new commit does not remove it from earlier history by itself. Full history
cleanup is a separate, harder job this kit deliberately does not walk you through solo, bring it to
the community rather than attempting a rewrite alone, since a mistake there can cause more damage than
the original leak.

### Who owns the code I put on GitHub?

You do, by default, whether or not the repository is public or private. GitHub's own documentation on
licensing states it plainly: "without a license, the default copyright laws apply, meaning that you
retain all rights to your source code and no one may reproduce, distribute, or create derivative
works from your work." Putting a license file in a repository is what changes that, by deliberately
granting other people specific permissions.

### Can someone just take my code if it's public?

They can see it and copy it onto their own machine, that is what "accessible to everyone on the
internet" means, and there is no way to undo someone having already looked at or downloaded it once a
repository has been public. What they are legally allowed to do with that copy is a separate question
from who can see it: without a license file, default copyright law means nobody may reproduce,
distribute, or build on your work without your permission, even if they can view it. If keeping people
from even seeing your files matters more than the visibility question, keep the repository private in
the first place rather than relying on copyright law after the fact.

### What does removing someone from my org actually stop, and not stop?

It stops their future access to your organization's repositories and settings on GitHub going
forward. It does not reach their own computer. GitHub's own words: "you are responsible for ensuring
that people who have lost access to a repository delete any confidential information or intellectual
property." If that matters for a specific removal, that is a conversation to have with the person
directly.

### What's the one setting that quietly gives everyone access to everything?

The organization's base permission, if set to Write. It applies to every current member and every
member you add in the future, on every repository the organization owns, current and future, with no
per-repository decision involved. Most small teams should leave this at Read or No permission and
grant Write only where it is specifically needed.

---

## Doing it through Claude Code

Every member of this kit has Claude Code on the Max plan. It already has git available, so it can
carry out the underlying steps for you from a plain-English request, but there are specific things it
should never be asked to do.

### What can Claude Code actually do for me on GitHub?

Getting a connected copy of a repository (a clone), pulling down the newest changes, creating and
switching between branches, and, if the GitHub CLI is already installed and signed in on your
machine, creating a new repository with an explicit public or private flag. It runs the underlying
git commands so you never have to know their names.

### What will Claude Code never do for me, on purpose?

Anything tied to your identity or your billing as a real person: turning on two-factor authentication,
saving your recovery codes, creating an organization, inviting or removing a member, transferring or
deleting a repository, changing billing. Every one of those needs GitHub to see you, specifically,
click the button or scan the code, and stays a browser-only, signed-in-as-yourself step in this kit on
purpose.

### How do I ask it to get me a copy of a repository?

Copy the repository's HTTPS link from its green Code button, then tell Claude Code, in plain English:
"Clone this repository for me," and paste the link. It runs the clone and tells you the folder path it
used, read that, do not skip past it. A public repository needs nothing else signed in; a private one
needs you (and Claude Code, acting as you) to already be signed in to GitHub on that machine.

### How do I ask it to make a branch?

Something like: "Make me a new branch called fix-homepage-typo, based on main." It creates the branch
and switches you onto it, then tells you what it did.

### How do I ask it to save my changes?

Describe the change and ask it to commit it, in plain English, and it will ask you (or you can tell
it upfront) what to put in the commit message. For anything touching more than one file at once, or
anything you want to review before it is saved, Claude Code is generally the better tool than the
browser, because it can show you exactly what changed before anything is committed.

### How do I ask it to get the newest updates?

Ask it to "pull the latest changes." Commit anything you have already changed first, so the update
does not get confused about which version of a file to keep.

### Does Claude Code need special access to create things for me?

Only for the `gh repo create` shortcut, and only in the sense that the GitHub CLI itself needs to
already be installed and signed in to your account before Claude Code can run it on your behalf. If
that is not already set up on your machine, use the browser path for creating a repository instead.

### I don't know where Claude Code put my files. What do I do?

Ask it directly: "Where did you clone [repository name] to?" It knows the exact path it used and will
tell you again, or open the folder for you. A habit worth building: pick one folder on your machine
for everything GitHub-related and always point Claude Code there, so you never lose track of where
things went.

---

## Questions people are embarrassed to ask

Nobody who has ever used GitHub started out knowing any of this. These are the questions people think
everyone else already understands. They usually don't.

### What actually is git, and how is it different from GitHub?

They are not the same thing, and it is a genuinely common mix-up. GitHub's own words: "Git is the
most popular distributed version control system," the underlying tool that tracks changes to files.
"GitHub hosts Git repositories and provides developers with tools to ship better code," on top of
that, things like pull requests, code review, and the website you actually click around on. In plain
terms: git is the engine, GitHub is the website and the team tools built around it. In this kit you
never have to touch git directly, Claude Code runs it for you, and the browser handles the rest.

### Do I need to know how to code to use any of this?

No, and this whole kit is built on that being true, not a comforting exaggeration. GitHub's own guide
above on the everyday workflow puts it plainly: "Do I need to actually know git to do any of this? No.
Everything on this page is either a browser click path or a plain-English request to Claude Code."
Creating a repository, making a branch, opening a pull request, none of it requires reading or writing
code yourself.

### Is it too late for me to learn this?

No. This kit assumes you have never used GitHub before and walks through the browser first every
time, precisely so you can see what each click actually does before you rely on it. There is no
point where the material assumes prior experience you have not been given here.

### Will this cost me money without warning?

The account itself, no, it is free and stays free unless you or someone with billing access
deliberately chooses a paid plan from the organization's own settings. See the money and plans section
above for exactly what is confirmed about pricing and what is not.

### Can someone steal my work?

If a repository is public, yes, anyone can see it and copy it, that is what public means on GitHub.
What they are legally allowed to do with that copy is a separate question governed by copyright, not
by GitHub's visibility setting: without a license file, GitHub's own documentation confirms default
copyright law means "no one may reproduce, distribute, or create derivative works from your work"
without your permission, even if they can see it. If you want to stop people from even seeing your
files, keep the repository private from the start.

### Is my code visible to GitHub staff?

Only in specific, documented circumstances, not for routine browsing, and this page covers exactly
which ones in the privacy and security section above, quoting GitHub's own Terms of Service directly.

### What happens if I stop paying?

See the full answer in the money and plans section above; it depends on whether you are letting a
paid organization plan lapse or cancelling an account entirely, and those have different, separately
confirmed answers.

### I'm scared I'll break something permanently. Can I?

Almost everything in this kit is designed so you cannot. A branch protects the main version while you
work, and can be deleted with no lasting effect if it never went through a pull request. Archiving a
repository can be undone at any time. Even deleting one has a partial 90-day restore window, though
not a guaranteed one, which is exactly why this kit's own guides recommend archiving over deleting
whenever you are not certain. The two genuinely irreversible actions in this whole kit are deleting a
repository past its restore window and deleting an organization entirely, and both require a typed
confirmation of the exact name before GitHub lets you proceed, specifically so you cannot do either by
accident.

---

## Sources

Every GitHub platform fact on this page traces to GitHub's own documentation, fetched or confirmed
between 17 and 18 August 2026. GitHub's screens and prices change, so treat anything time-sensitive
(prices, plan limits, exact button wording) as worth a fresh look on your own screen if real money or
a real decision rides on it.

- https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
- https://docs.github.com/en/account-and-profile/reference/email-addresses-reference
- https://docs.github.com/en/site-policy/other-site-policies/github-username-policy
- https://docs.github.com/en/account-and-profile/concepts/username-changes
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/countries-where-sms-authentication-is-supported
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/recovering-your-account-if-you-lose-your-2fa-credentials
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/troubleshooting-two-factor-authentication-issues
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/verifying-new-devices-when-signing-in
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/preventing-unauthorized-access
- https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts
- https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch
- https://docs.github.com/en/get-started/learning-about-github/githubs-plans
- https://docs.github.com/en/get-started/learning-about-github/githubs-products
- https://github.com/pricing
- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization
- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/maintaining-ownership-continuity-for-your-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization
- https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization
- https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository
- https://docs.github.com/en/account-and-profile/how-tos/organization-membership/removing-yourself-from-an-organization
- https://docs.github.com/en/organizations/managing-organization-settings/deleting-an-organization-account
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/setting-base-permissions-for-an-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/adding-outside-collaborators-to-repositories-in-your-organization
- https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/reinstating-a-former-member-of-your-organization
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks
- https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://cli.github.com/manual/gh_repo_create
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories
- https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository
- https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository
- https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- https://cli.github.com/manual/gh_repo_clone
- https://docs.github.com/en/get-started/using-git/about-git
- https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository
- https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files
- https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
- https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- https://cli.github.com/manual/gh_pr_create
