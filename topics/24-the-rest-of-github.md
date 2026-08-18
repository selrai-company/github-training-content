# The rest of GitHub, and what is worth your time

## What this gets you

GitHub has more tabs and buttons on it than this kit has covered so far. Most of them will never
come up for a small business, and a few are genuinely useful once you know they exist. The problem
with not knowing what a button does is not that you will break something by clicking it, it is that
you will either ignore something that could have saved you real time, or spend an afternoon setting
up something your business never needed.

This file is a tour of everything left: GitHub Pages, wikis, Discussions, gists, Projects, template
repositories, the mobile app, starring, watching, following, and your profile page. For each one, you
get one plain sentence on what it does, who it actually fits, and a straight answer on whether it is
worth your time. Several of these get a genuine "skip this" from this kit, not because they are
badly built, but because a small business almost always already has a better tool for the same job.

## Before you start

**You need a GitHub account**, and it helps to already have at least one repository, since most of
this file is easier to follow with a real one open in another tab. `04-repositories-and-visibility.md`
covers creating one if you have not yet.

**Knowing branches, pull requests, and issues is not required, but it helps.** A few of the features
in this file, Projects especially, exist to organise the issues and pull requests covered in
`06-branches.md`, `07-pull-requests.md`, and `13-issues-and-tracking-work.md`. If those words are
still unfamiliar, this file will still make sense, you will just get more out of the Projects and
Discussions sections after reading those first.

**Several of these features live behind your repository's Settings tab**, which on most repositories
only opens for someone with Admin access, or Maintain access and above for the specific settings this
file names as needing it. `03-members-and-access.md` covers checking or changing your own access
level. Where a specific access level is confirmed below, this file states it plainly rather than
assuming Admin for everything.

## The words you need

**GitHub Pages.** A GitHub feature that turns the files in a repository into a website, publishing
whatever it finds directly onto the internet. GitHub's own wording: "GitHub Pages is a static site
hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub,
optionally runs the files through a build process, and publishes a website."

**Static site.** A website made of plain files that look the same for every visitor, rather than one
built by a program that assembles a different page for each person on the fly. GitHub Pages only
publishes this simpler kind of site.

**Wiki.** A separate, editable documentation space attached to a repository, for writing longer than
what belongs on the front page. GitHub's own wording for what it is for: to "share long-form content
about your project, such as how to use it, how you designed it, or its core principles."

**Discussions.** A forum attached to a repository, for open-ended conversation that is not a specific
task and is not attached to a piece of code. GitHub's own wording: "a collaborative communication
forum" for conversations that "do not need to be tracked on a project and are not related to code."

**Discussion category.** A label a discussion is filed under when it is opened, chosen by whoever
created it, such as "Ideas" or "Q&A." GitHub's own wording: "Discussions are opened in user-defined
categories."

**Gist.** A small, separate GitHub feature for sharing a short piece of text or code on its own, without
needing a full repository around it. GitHub's own wording: "a simple way to share code snippets with
others." Every gist is its own tiny repository underneath, with its own history.

**Secret gist.** A gist that does not show up in GitHub's public listing of gists and is not
searchable, but is not truly private either. GitHub's own wording: "if you send the URL of a secret
gist to a friend, they'll be able to see it." Anyone with the direct link can open it.

**GitHub Projects.** A planning board that sits above your issues and pull requests, letting you view
and organise them as a table, a board of cards you drag between columns like "To do" and "Done," or a
timeline. GitHub's own wording: "an adaptable table, board, and roadmap that integrates with your
issues and pull requests."

**Custom field.** A piece of information you add to a Project yourself, beyond what an issue or pull
request already carries, such as a priority level or a due date, so you can sort and group by it.

**Template repository.** A repository marked so that anyone with access to it can generate a brand
new repository copying its structure, files, and settings, instead of starting from an empty folder.
GitHub's own wording: creating from one gives you "a new repository based on the template with the
same directory structure, branches, and files."

**GitHub Mobile.** GitHub's own phone app, for Android and iOS, for reading and responding to
GitHub activity away from a computer.

**Star / Starring.** Marking a repository as one you want to find again easily, similar in spirit to
bookmarking a page in a browser. Covered briefly in `15-finding-things.md`; covered in full here.

**Watching.** Subscribing to a repository so GitHub notifies you about its activity. Already covered
in full in `16-notifications.md`; mentioned here only so this file's tour is complete.

**Following.** Subscribing to a specific person, or an organisation, so their public activity shows on
your own GitHub dashboard.

**Profile README.** A short piece of writing that appears at the top of your own GitHub profile page,
written by you, in the same Markdown covered in `14-markdown-and-writing.md`.

**Pinning.** Choosing up to six repositories or gists, combined, to display prominently at the top of
your own profile page. GitHub's own wording on the limit: "Select up to six repositories and gists,
combined."

## How to do it

### GitHub Pages: turning a repository into a website

**What it is.** A free way to publish a simple website straight from a repository's files, with no
separate hosting account to set up.

**Who it is for.** Someone who already has files sitting in a GitHub repository, project documentation,
a portfolio, a one-page announcement, and wants them visible on the web with nothing extra to pay for
or maintain.

**The plan detail worth knowing before you start.** GitHub's own products page states plainly that
GitHub Free includes "GitHub Pages in public repositories" only. GitHub Pro and GitHub Team both list
GitHub Pages too, but with this exact note attached: "To publish a GitHub Pages site privately, you
need to have an organization account. Additionally, your organization must use GitHub Enterprise
Cloud." In plain terms: for almost every small business on this kit, a GitHub Pages site is
effectively a public website, whatever the repository's own visibility is set to. Do not put anything
on a Pages site you would not want a stranger to see.

**Other real limits, confirmed from GitHub's own published numbers.** A published site "may be no
larger than 1 GB." Bandwidth carries "a soft bandwidth limit of 100 GB per month." Builds carry "a
soft limit of 10 builds per hour," though that limit does not apply if you deploy through a custom
GitHub Actions workflow instead of GitHub's automatic build.

**A first look, in the browser.**

**Landmark:** open a repository's Settings page (the same tab covered in
`04-repositories-and-visibility.md`).
**Path:** in the left sidebar, under **Code and automation**, click **Pages**.
**Confirmation:** a page titled **GitHub Pages** appears, with a **Source** setting you can point at a
branch and folder.

Marking a source and saving publishes the repository's chosen files at a GitHub-given address, built
from your account or organisation name. GitHub's own repository-roles table confirms configuring a
Pages publishing source needs **Maintain** access or above; Read and Write alone are not enough on an
organisation-owned repository.

**This kit's verdict: skip it, for most small businesses.** If you already have a website through a
normal website builder, GitHub Pages adds a second, separate site to keep straight, for no real
benefit over what you already have. It earns its keep in one specific case: a small, simple,
public-facing page, like project documentation, a one-page price list, or a portfolio, from someone
already comfortable working inside a repository. If that is not your situation, do not set this up
just because it exists.

### Wikis: an editable space beside your repository, and why a plain file usually beats it

**What it is.** A separate area attached to a repository for writing that goes beyond a normal file,
edited straight in the browser, in the same Markdown covered in `14-markdown-and-writing.md`.

**Who it is for.** A project with genuinely long documentation, spread across many separate pages,
that does not fit comfortably inside one README.

**A first look, in the browser.**

**Landmark:** a repository's main page.
**Path:** along the top, in the row of tabs that starts with **Code**, look for a tab labelled
**Wiki**. If it is not there, it has not been turned on for this repository yet, covered next.
**Confirmation:** clicking it opens a page inviting you to create the first wiki page.

**Turning it on, if it is not already.** This is the same **Features** toggle list mentioned in
`04-repositories-and-visibility.md`: open the repository's Settings, find **Features** on the General
page, and tick **Wikis**. GitHub's own repository-roles table confirms enabling wikis, and choosing
who is allowed to edit them, needs **Maintain** access or above.

**The setting worth checking before you rely on a wiki, especially on a public repository.** By
default, GitHub's own wording is that "only repository collaborators can edit a public repository's
wiki." But every repository also carries a separate setting, in the wiki's own sidebar, called
**Restrict editing to collaborators only**. GitHub's own description of what turning that setting off
does: it "allows anyone with a GitHub.com account to edit the wiki, rather than limiting edits to
repository collaborators." On a private repository, editing already requires Write access regardless
of this setting; GitHub's own repository-roles table shows editing a private repository's wiki starts
at Write. But on a public repository, if that box has ever been unticked, anyone signed in to GitHub
at all, not just people you gave access to, can rewrite your wiki. Check it before you trust anything
written there.

**This kit's verdict: skip it, and use a plain Markdown file instead.** A README, or a second file
sitting in a `docs` folder, already does almost everything a wiki does: it renders Markdown, it holds
long writing, and it sits inside your repository. What a plain file does better: every change to it
goes through the same commit history as the rest of your project, and if you want it, the same pull
request review covered in `07-pull-requests.md`, before it changes. A wiki page, by contrast, is
edited and saved directly, with no review step built in, only the access-level check above. For a
small business, the extra tab a wiki adds is rarely worth the loss of that review step. Reach for a
wiki only if the amount of documentation has genuinely grown too large for a handful of files to hold
comfortably, which is uncommon for the audience this kit is written for.

### Discussions: a forum for conversation that is not a task

**What it is.** A comment-based forum attached to a repository, for conversation that does not belong
on a specific issue or pull request.

**Who it is for.** A project with a real community around it asking open-ended questions, sharing
ideas, or discussing direction, separate from tracking a specific piece of work.

**How Discussions differs from Issues, in GitHub's own words.** Discussions are for conversations that
"do not need to be tracked on a project and are not related to code." An issue, by contrast, is
specifically for tracking something that needs doing, covered in `13-issues-and-tracking-work.md`.
GitHub does let you move a conversation between the two in one direction: its own description lists
the ability to "convert open-ended issues into discussions" as a management tool. This kit could not
confirm from GitHub's own pages whether the reverse, turning a discussion into an issue, is a
documented feature, so do not assume it exists; treat the direction as one-way until you confirm
otherwise on your own screen.

**A first look, in the browser.**

**Landmark:** a repository's main page.
**Path:** along the top, in the row of tabs, look for **Discussions**. If it is not there, it has not
been turned on yet.
**Confirmation:** clicking it shows a list of discussions filed under categories, with a button to
start a new one.

**Turning it on, if it is not already.** Open the repository's Settings, find **Features** on the
General page, and tick **Discussions**, then follow the short setup screen that appears. GitHub's own
wording on who can do this: "Repository owners and people with write access can enable GitHub
Discussions," on public and private repositories alike, a genuinely lower bar than the Maintain level
that Pages and wikis need.

**This kit's verdict: skip it, for a small private team.** Discussions exist to give a large, mostly
public audience a place to talk that is not cluttering the issue list. A café owner, her nephew, and
one staff member do not need a forum, they can talk directly, and anything worth keeping a record of
belongs in an issue instead. Turn this on only if your repository is public and genuinely draws
outside questions or ideas worth a dedicated space.

### Gists: sharing one small thing without a whole repository

**What it is.** A quick way to share a short piece of text or code on its own, without setting up a
full repository for it.

**Who it is for.** Anyone who wants to hand someone a small snippet, a script, a configuration file,
a short note, and does not want to build a repository around one file.

**A first look, in the browser.**

**Landmark:** any GitHub page, once signed in.
**Path:** click your profile picture in the top right corner, then, in the menu, look for **Your
gists**, or go directly to `https://gist.github.com`.
**Confirmation:** a page appears listing any gists you have already made, with a way to start a new
one.

1. Click the **+** to start a new gist, or the equivalent button on the gist page.
2. Add an optional description of what the file is.
3. Type a filename, including its extension, for example `notes.txt` or `config.json`.
4. Paste or type the content.
5. Choose **Create secret gist** or **Create public gist**.

**Public versus secret, and the trap in the name.** A public gist shows up in GitHub's own Discover
listing and is searchable by anyone. A secret gist does not appear there and is not searchable, but
GitHub is direct about what that does and does not mean: "if you send the URL of a secret gist to a
friend, they'll be able to see it." A secret gist is unlisted, not private. If real confidentiality
matters, GitHub's own recommendation is a private repository instead, covered in
`04-repositories-and-visibility.md`. One more detail worth knowing: a secret gist can be switched to
public later, but GitHub does not offer the reverse, so nothing you have ever made public through a
gist can be pulled back to secret afterward.

**This kit's verdict: worth knowing about, not worth building a habit around.** For the one moment
you want to hand someone a single file or a short snippet without any of the setup a repository asks
for, a gist is the right-sized tool. It is not a replacement for a repository once there is more than
one file involved, or once the content needs real privacy rather than an unlisted link.

### Projects: a board view across your issues and pull requests

**What it is.** A visual way to plan and track work, sitting on top of the issues and pull requests
you already have, viewable as a table, a board of cards you drag between columns, or a timeline.

**Who it is for.** Anyone coordinating more than a handful of issues at once, especially across more
than one repository, who wants to see the whole picture in one place rather than reading a plain list.

**How it connects to issues and pull requests.** Adding one to a Project does not copy it, it links
the two. GitHub's own wording: information "is synced automatically to your project as you make
changes," and changing something inside the project view, like its status, updates the real issue or
pull request behind it, not a separate copy.

**A first look, in the browser.**

**Landmark:** either your own profile page, or an organisation's page, or a specific repository's main
page.
**Path:** along the top row of tabs, look for **Projects**. From your own profile or an organisation
page, this lists every Project you have access to; from a repository, click it, then **New project** to
start one scoped to that repository.
**Confirmation:** a blank board or table appears, ready to have issues and pull requests added to it.

**What you get once it is set up.** GitHub's own description covers custom fields, up to 50 in total,
several different views of the same underlying items, and templates you can reuse the next time you
start a new one. This kit could not confirm the current limit on the total number of items a single
Project can hold from GitHub's own documentation this session; treat it as a genuinely large number
that a small business is very unlikely to reach, rather than a figure to plan around.

**This kit's verdict: worth it, once there is enough work to actually need a picture of it.** A solo
operator with three open issues gets nothing from a board that a plain issues list does not already
show. The value shows up once there are enough moving pieces, several jobs in progress across more
than one repository, a small team each holding a different piece, that a visual board genuinely
answers "what is everyone working on right now" faster than reading through separate lists.

### Templates: making sure a new repository starts set up correctly

**What it is.** A repository marked so that starting a new one from it copies its structure straight
away: the same folders, the same starter files, the same settings, instead of a new empty repository
every time.

**Not to be confused with an issue template**, the pre-written starting form covered in
`13-issues-and-tracking-work.md`, which sets up one issue, not a whole new repository. Also not to be
confused with the `.gitignore` template offered on the repository creation form, covered in
`04-repositories-and-visibility.md`, which fills in one file, not the rest of a project's structure.
This section is specifically about copying an entire repository as a starting point.

**Who it is for.** Anyone who creates a similar kind of repository more than once: a consultant who
starts a fresh repository for every new client, a business that spins up a matching setup for every
new location or product line, a technical person tired of re-adding the same starter files by hand
each time.

**Marking a repository as a template.**

**Landmark:** the repository you want to use as the starting point in future.
**Path:** open its Settings, then, on the General page, look for a checkbox labelled **Template
repository**.
**Confirmation:** once ticked, the repository's own main page shows a green **Use this template**
button where **Code** normally sits alone.
**Fallback:** if the checkbox is not there, or does nothing, this kit could not confirm the exact
access level required directly from GitHub's own repository-roles table, since it does not name this
specific action. Given that every other Settings-page action this kit has confirmed needs at least
Maintain access, treat that as the level to check first, and confirm your own access in
`03-members-and-access.md` before assuming something else is wrong.

**Starting a new repository from a template.**

**Landmark:** a repository already marked as a template.
**Path:** on its main page, click **Use this template**, then **Create a new repository**.
**Confirmation:** a familiar repository-creation form appears, pre-filled from the template, asking
you to name the new one and choose whether to copy every branch or just the default one.

**One real limit worth knowing.** GitHub's own wording: "your template repository cannot include
files stored using Git LFS," a separate system for very large files this kit does not otherwise cover.
If your starter files include anything large enough to need that, it will not carry across.

**This kit's verdict: genuinely worth it, if you repeat this pattern at all.** This is one of the
few features in this file this kit recommends without much hesitation, for the specific business that
needs it. If you only ever have one project, it does nothing for you. If you start a similar new
repository more than once a year, it turns "remember everything we usually set up" into one button.

### The mobile app: doing small things without a laptop

**What it is.** GitHub's own phone app. GitHub's own wording: "GitHub Mobile gives you a way to do
high-impact work on GitHub quickly and from anywhere," described as "a safe and secure way to access
your data through a trusted, first-party client application."

**Who it is for.** Anyone who wants to check notifications, read or comment on an issue or pull
request, or approve something small, without opening a laptop.

**What it can actually do**, confirmed from GitHub's own page: manage and clear notifications, read,
review, and collaborate on issues and pull requests, edit files inside a pull request, search across
users, repositories, and organisations, receive a push notification when you are mentioned, search
code, turn on two-factor authentication, and use GitHub Copilot Chat to ask coding-related questions.

**Getting it.** GitHub's own instruction is short: visit `https://github.com/mobile` on the phone you
want to install it on, which detects your device and sends you to the right app store listing for
Android or iOS.

**This kit's verdict: a genuine convenience, not a requirement.** Nothing in this kit assumes you have
it installed, and nothing about running a small business on GitHub requires a phone app. Install it if
being able to glance at a notification or approve something small away from a computer sounds useful
to how you actually work. Skip it if everything you do on GitHub already happens at a desk.

### Stars, watching, and following

**Starring a repository.** GitHub's own description of what it is for: to "keep track of projects you
find interesting," and, separately, "starring a repository also shows appreciation to the repository
maintainer for their work." Click **Star** on any repository's main page. Find everything you have
starred again at `https://github.com/stars`, where GitHub's own wording confirms you can "search, sort,
and filter your starred repositories and topics."

**Watching a repository** is covered in full in `16-notifications.md`; it is the setting that decides
which activity on a repository actually reaches your notifications. This file mentions it only so the
full set of "keep track of" features sits in one place: starring bookmarks something for yourself,
watching subscribes you to hear about it.

**Following a person, or an organisation.** GitHub's own wording on what it does: "you'll see their
public activity on your personal dashboard." Open the profile page of the person or organisation, and
click **Follow**, underneath their profile picture. One detail worth flagging: GitHub's own
documentation currently marks following an organisation specifically as "in public preview and subject
to change," so treat that particular option as newer and less settled than following an individual
person.

**This kit's verdict.** Starring costs nothing and genuinely helps you find something again later,
use it freely, including on your own repositories. Following is a social feature built for browsing
other people's open-source work; it does nothing for running your own business, and this kit sees no
reason for a small business account to bother with it. Watching is the one of the three that actually
matters day to day, and it already has its own full file.

### Your profile page

**What it is.** The page at `https://github.com/<your-username>`, showing your public activity, your
bio, and anything you have chosen to pin, to anyone who looks you up.

**Who it is for.** Anyone whose GitHub account might reasonably be looked up by someone outside your
own team: a technical person people find through their public work, a consultant whose profile is
part of how a prospective client sizes them up, an owner whose account link ends up on a business card
or an email signature.

**What shows there**, confirmed from GitHub's own description: "your work, contributions, and
information you choose to share publicly," including your profile picture, name, bio, a visualisation
of your contribution activity, pinned repositories, a status, and achievement badges.

**A profile README, the short introduction at the top of the page.**

1. Click the **+** in the top right corner, then **New repository**.
2. Name the repository exactly your own GitHub username. GitHub's own wording: "type a repository
   name that matches your GitHub username. For example, if your username is 'octocat,' the repository
   name must be 'octocat.'" This exact match is what tells GitHub to treat it specially.
3. Set it to **Public**.
4. Turn on **Add a README file**.
5. Click **Create repository**.
6. On the new repository's page, click **Edit README**, and write what you want to appear at the top
   of your profile. It supports the same Markdown covered in `14-markdown-and-writing.md`, including
   images and emoji.

**Pinning up to six repositories or gists.** Open your own profile, click **Customize your pins**,
choose up to six, in whatever order you like, and save. GitHub's own wording on the limit: "Select up
to six repositories and gists, combined."

**Controlling what is visible.** You can make your whole profile private, which GitHub's own wording
confirms hides your achievements, your activity feed, your contribution graph, your follower count,
and your organisation memberships, while your README, bio, and profile picture stay visible regardless.
You can also turn off individual pieces one at a time instead of hiding everything at once.

**This kit's verdict.** If nobody outside your own team is ever likely to look at your GitHub profile,
this is genuinely low priority, spend your time elsewhere in this kit first. If your account is even
occasionally public-facing, a short, honest profile README and a handful of pinned repositories are a
worthwhile fifteen minutes: it is the difference between someone landing on a blank page and someone
landing on a page that tells them who you are and what you have actually built.

## Strategy: how to actually use this

**The right amount of this file to actually use is usually small.** Read the whole tour once so
nothing on GitHub is a mystery the day it appears in front of you. Then, in practice, most small
businesses using this kit will genuinely set up two or three of these ten features, not all of them.

**A solo operator working alone** gets the least out of almost everything in this file. Discussions,
Projects, and a wiki all exist to coordinate more than one person, or to organise more work than one
person can hold in their head. The two exceptions worth a solo operator's time: a template repository,
if the same kind of project gets started more than once, and a polished profile page, if clients or
collaborators are likely to look the account up.

**A small team, one of them technical** (the café and its ordering site, covered throughout this kit)
gets real value from a Project board once there is more than one job in flight at a time, and from a
template repository the moment a second, similar site or repository gets built. Discussions and a wiki
still rarely earn their keep for a team this size; a private team talks directly, and documentation
short enough to fit in a README does not need a second space to live in.

**A public-facing open-source-style project** is the one situation where this file flips: Discussions,
a wiki, and GitHub Pages genuinely start earning their place, because the audience they are built for,
a large, mostly anonymous group of people who are not on your team, is exactly who is now involved.
Almost nobody using this kit is running a project shaped like that, so treat this as the exception, not
the target you are building toward.

**What good looks like months later.** A repository using only the features it actually needs: no
half-set-up wiki nobody writes in, no Discussions tab sitting empty, a Project board only where there
is enough work to justify glancing at it, and a template in place the moment the same kind of project
gets started for a second time.

## A worked example

The café's nephew, from earlier in this kit, starts building websites for two more small businesses
nearby: a bakery and a florist. Before starting the second one, he notices how much of the first
site's setup he is about to retype by hand, the same `.gitignore`, the same starter folder structure,
the same first few files. He opens the café's original repository, goes to its Settings, and ticks
**Template repository**. The next time a new client signs on, he clicks **Use this template** on that
repository instead of starting empty, and has a working starting point in under a minute.

He considers a wiki for writing up how each site is put together, but decides against it once he
checks how wiki editing permissions actually work: a plain `SETUP.md` file, sitting inside each
repository, does the same job and goes through the same commit history as everything else he tracks.
He adds one to the template, so every new site starts with that file already in place.

As the number of client sites grows to four, keeping track of "which site needs what done this week"
in his head stops working. He opens a Project, adds the open issues from all four repositories to it,
and switches to the board view so he can see, at a glance, what is in progress and what is waiting on
him. He does not turn on Discussions or GitHub Pages for any of the client repositories, none of them
have an outside audience that would use either.

A prospective client finds his GitHub profile through a mutual contact. It currently shows nothing but
his username and a wall of green activity squares. He writes a short profile README explaining what he
builds and for whom, and pins the café's ordering site and one other project he is proud of. The next
time someone looks him up before a first phone call, the page actually tells them something.

## If it goes wrong

**I turned on a wiki or Discussions tab and now regret it.** Both can be switched off the same way
they were switched on: the repository's Settings, **Features**, untick the box. Turning either off
does not delete anything already written there; it just stops showing the tab.

**I published a repository to GitHub Pages, thinking it would stay private, because the repository
itself is private.** Check the plan detail above directly: on GitHub Free, GitHub Pro, and GitHub
Team, GitHub's own wording ties truly private publishing to an organisation account on GitHub
Enterprise Cloud specifically. If that does not describe your setup, treat anything you have published
through Pages as public, and remove it if it should not be.

**I unticked "Restrict editing to collaborators only" on a public repository's wiki, and now I am not
sure who has changed it.** Check the wiki's own history first, the same idea as a file's history
covered in `15-finding-things.md`, to see what changed and when. Re-tick the setting if you did not
mean to leave it open, and treat anything written while it was open as something to review rather than
trust outright.

**I made a gist public by mistake, or shared a secret gist's link somewhere I now regret.** GitHub
does not offer a way to turn a public gist back to secret. If the content itself is sensitive, treat
it the same way you would a leaked password: assume it has been seen, and change or replace whatever
it contained rather than relying on hiding it again.

**I cannot find the "Template repository" checkbox, or ticking it does nothing.** This kit could not
confirm the exact access level this specific action requires from GitHub's own repository-roles table.
Confirm your own access level in `03-members-and-access.md`; every comparable Settings-page action this
kit has confirmed needs at least Maintain access, so treat that as the first thing to check.

**Issues added to a Project do not seem to update when I change something on the issue itself.** Open
the actual issue, not just the card inside the Project, and confirm the change was saved there.
GitHub's own wording is explicit that the two stay in sync automatically, so a mismatch usually means
the change was made somewhere other than expected, rather than a genuine sync failure.

## FAQ

**Do I need to use any of these features to use GitHub properly?** No. Nothing in this file is
required. A repository, branches, pull requests, and issues, all covered earlier in this kit, are a
complete way to run a small business on GitHub without touching a single feature in this file.

**Is a wiki safer than just editing a file, since it needs write access to change?** Not necessarily,
and it depends entirely on one setting. On a private repository, wiki editing does require Write access,
the same as editing any file. On a public repository, unless "Restrict editing to collaborators only"
is switched on and left on, anyone signed in to GitHub at all can edit it. A plain file always goes
through the same access rules as the rest of your repository, with no separate setting to accidentally
leave open.

**Can I turn Discussions or a wiki back off after using them for a while?** Yes, the same Settings
toggle that turns them on turns them off, and nothing already written is deleted by switching the
tab off.

**What actually happens to a secret gist if I make it public later?** It becomes visible in GitHub's
public Discover listing and becomes searchable, same as anything made public from the start. This can
be done from the gist's own settings. GitHub does not offer the reverse.

**Does a GitHub Project cost anything extra?** This kit's research this session did not find any
plan-based restriction stated on GitHub's own plan comparison page for Projects, unlike the specific
restrictions it states for private GitHub Pages sites and for Wikis under GitHub Pro and Team. Confirm
current availability on GitHub's own pricing page if you want certainty before relying on it.

**Is GitHub Copilot Chat only available through the mobile app?** No. This kit could not confirm that
from GitHub's own pages, and it would be surprising if true, since Copilot Chat is a broader GitHub
feature. What GitHub's own page for the app confirms is only that the app includes it as one of its
features, not that the app is the only place it lives. Confirm on your own screen where else you can
already reach it before assuming the app is your only option.

**Can I follow my own business's repositories to keep an eye on them?** That is what watching is for,
not following, which is aimed at people and organisations. `16-notifications.md` covers watching in
full.

## Quick reference

- **GitHub Pages:** repository Settings, **Pages**, pick a source. Free plan publishes public
  repositories only; genuinely private publishing needs an organisation on GitHub Enterprise Cloud.
- **Wiki:** repository Settings, **Features**, tick **Wikis**. Check **Restrict editing to
  collaborators only** on any public repository's wiki before trusting what is written there.
- **Discussions:** repository Settings, **Features**, tick **Discussions**. Needs Write access or
  above to turn on.
- **Gist:** `https://gist.github.com`, click **+**, choose **secret** (unlisted, not private) or
  **public**.
- **Projects:** repository or organisation page, **Projects** tab, **New project**. Worth it once
  there is enough work to need a picture of it.
- **Template repository:** repository Settings, tick **Template repository**. Reuse it with **Use
  this template** on its main page.
- **Mobile app:** visit `https://github.com/mobile` on your phone.
- **Star a repository:** click **Star** on its main page; view them all at
  `https://github.com/stars`.
- **Follow someone:** their profile page, click **Follow**. Following an organisation is currently a
  public preview feature.
- **Profile README:** new public repository named exactly your username, README turned on, then
  **Edit README**.
- **Pin items to your profile:** your profile, **Customize your pins**, up to six repositories and
  gists combined.

## Sources

- https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://docs.github.com/en/get-started/learning-about-github/githubs-products
- https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis
- https://docs.github.com/en/communities/documenting-your-project-with-wikis/changing-access-permissions-for-wikis
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization
- https://docs.github.com/en/discussions/quickstart
- https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions
- https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository
- https://docs.github.com/en/get-started/using-github/github-mobile
- https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars
- https://docs.github.com/en/get-started/exploring-projects-on-github/following-people
- https://docs.github.com/en/get-started/exploring-projects-on-github/following-organizations
- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile
- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile
