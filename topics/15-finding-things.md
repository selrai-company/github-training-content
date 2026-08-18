# Finding things again, without hunting

Once you have been on GitHub for a few months, you stop having one repository and start having a
handful: the website, the ordering system, the internal documents, a project a contractor set up for
you. Inside each one you have issues, pull requests, and files, and none of it stays small. This file
covers finding things again once that has happened: searching inside one repository, searching across
everything you personally have access to, the handful of search filters actually worth learning, finding
a file by name without clicking through folders, working out who changed something and why, browsing a
repository without hunting, saving the things you use constantly so you stop navigating to them from
scratch, and the small number of keyboard shortcuts worth learning by heart.

Most of this happens in your browser, so you can see the results as they appear. Wherever Claude Code
is genuinely faster (mainly once you have a copy of a repository on your own machine already), this file
says so and shows exactly what to type.

## What this gets you

Right now, finding something you know exists somewhere in your work probably means clicking into a
repository, scrolling, giving up, and asking whoever set it up. That costs you minutes every time, and
it costs your team more, because every one of those questions interrupts someone else's afternoon.
Once you know how to search properly, that same question takes seconds: every open task assigned to
you, across every project you have access to, in one line typed into one box. Knowing who changed a
price, a policy, or a piece of text, and being able to see their reasoning next to the change, turns
"who did this and why" from a slow, awkward conversation into something you can answer yourself in
under a minute. None of this needs a course. It is a small number of habits that pay for themselves the
first week you have more than one or two repositories.

## Before you start

You do not need anything specially set up to search or browse GitHub, any account with access to at
least one repository can do everything in this file.

You will get more out of this file if you have already read `04-repositories-and-visibility.md` (so you
know what a repository is and what public and private mean for it) and `05-daily-workflow.md` (so you
know what a commit and a commit message actually are, since a lot of this file is about finding and
reading them). If your team uses issues and pull requests, this file also assumes you have looked at
`07-pull-requests.md` at least once, since several of the search filters below are built specifically for
those.

## The words you need

**A search qualifier.** A short piece of text you add to a search, like `is:issue` or `author:janesmith`,
that tells GitHub to only show results matching that one condition. You can combine several qualifiers
in the same search box, one after another, separated by spaces.

**Searching globally, or "all of GitHub."** Searching across every repository you personally have access
to, rather than just the one you happen to be looking at. GitHub's own description of how you reach it:
"type what you're looking for into the search field at the top of any page, and choose 'Search all of
GitHub.'"

**A repository-scoped search.** A search that only looks inside the one repository you are currently
in, rather than everywhere you have access to. You get this by searching from inside that repository
instead of from the general search field.

**A commit,** as a quick reminder from `05-daily-workflow.md`: a saved snapshot of a change, with its
own ID, a timestamp, and the name of whoever made it. Almost everything in the "who changed this and
why" part of this file is really about finding and reading commits.

**The file finder.** A small search box, specifically for jumping straight to one file in a repository
by typing its name, instead of clicking through folders to find it.

**The Blame view.** A way of looking at a file where, instead of seeing the current text on its own,
you see which commit last changed every single line, right next to that line.

**A file's history.** The list of every commit that has changed one specific file over time, in order,
newest first. Different from Blame, which shows you line by line; a file's history shows you commit by
commit.

**A permalink.** A link to a file that points at one exact, permanent version of it, the version it was
at the moment you copied the link, rather than "whatever the file currently says."

**A breadcrumb trail.** The row of clickable folder names across the top of a repository page, showing
you the path to where you currently are, so you can jump back up several folders in one click instead
of clicking Back repeatedly.

**Starring a repository.** Marking a repository as one you want to find again easily, similar in spirit
to bookmarking a page in a browser.

**Pinning.** Choosing a small number of repositories (or gists, a related feature this kit does not
cover) to display prominently on your own GitHub profile, so anyone visiting it, including you, sees
them first.

**A saved search.** A search you have typed once, given a short name, and stored, so you can run it
again later by clicking its name instead of retyping the whole query.

**The Command Palette.** A single search box, opened with a keyboard shortcut from anywhere on GitHub,
that lets you jump to a repository, a file, or an issue, or run an action, without navigating any menu
first.

## How to do it

### Searching everywhere you have access to

Click the search field at the top of any GitHub page and type what you are looking for. If you want
results from every repository you can see rather than just the one you are currently viewing, choose
**Search all of GitHub**, GitHub's own wording for this option, from what appears as you type. This is
the search to reach for when you are not sure which repository something is in, or when you want to
see something across all of them at once, every open task assigned to you, for instance, regardless of
which project it belongs to.

**One real limit worth knowing before you rely on it:** GitHub's own documentation states plainly,
"Currently our search doesn't support exact matching." Putting a phrase in quotation marks (covered
below) narrows your results toward that phrase, but it is not a guarantee of a literal, word-for-word
match the way it might be in some other search box you have used. If a search comes back with something
close but not quite what you typed, that is expected, not a mistake on your part.

### Searching inside one repository

Open the repository first, then type your query into the search field on that repository's own pages
and press Enter. GitHub's own description of the difference: you can search "globally across all of
GitHub, or scope your search to a particular repository or organization" by searching from inside it.
Use this whenever you already know which project something lives in, it is faster because GitHub is not
sorting through every repository you can see, only the one you are standing inside.

You can also reach the same result from the general search field by adding a `repo:` qualifier, typing
the repository's full name (`repo:YOUR-ORGANISATION/YOUR-REPOSITORY`) as part of a global search. This
is worth knowing because it lets you search one specific repository even while your eyes are on a
completely different page.

### The search filters worth knowing

Search qualifiers exist for almost every part of GitHub, but a small handful cover most of what a small
business actually needs. Type these straight into any search field, combined with plain words or with
each other.

| Qualifier | What it does | A working example |
| --- | --- | --- |
| `is:issue` / `is:pr` | Only issues, or only pull requests | `is:pr is:open` finds every open pull request |
| `is:open` / `is:closed` | Only things still open, or only things already closed | `is:issue is:open label:bug` |
| `author:` | Only things a specific person created | `is:pr author:janesmith` |
| `assignee:` | Only things assigned to a specific person | `is:issue assignee:@me` finds issues assigned to you |
| `mentions:` | Only things where a specific person was `@` mentioned | `mentions:janesmith` |
| `label:` | Only things with a specific label | `label:"help wanted" is:open` (quote a label that has a space in it) |
| `in:title` / `in:body` | Only match your words inside the title, or inside the description, rather than anywhere | `menu in:title` finds "menu" only where it appears in a title |

**One shortcut worth learning on its own: `@me`.** GitHub's own syntax documentation confirms you can
use `@me` in place of your own username in any of these qualifiers, so `assignee:@me` always means "
assigned to whoever is currently signed in," without you having to type or remember your own username.

**Quoting a phrase.** Put multi-word searches in quotation marks, GitHub's own documentation gives the
example `cats NOT "hello world"`, which finds results mentioning "cats" while excluding the exact phrase
"hello world." Remember the limit above, quoting narrows your results toward that phrase, it is not a
guaranteed exact match.

**Excluding something.** Put a hyphen directly in front of any qualifier to exclude it instead of
requiring it. GitHub's own example: `cats stars:>10 -language:javascript` finds repositories about cats
with more than 10 stars, excluding any written in JavaScript.

**Searching inside your files, not just titles and descriptions.** This is a separate kind of search,
code search, aimed at finding a word or phrase somewhere inside your actual files rather than in an
issue or a repository name. Two qualifiers worth knowing: `filename:` finds a file by its exact name
(GitHub's own example, "`filename:linguist` matches files named linguist"), and `extension:` narrows to
files of one type (GitHub's own example, "`extension:css`"). A few real limits, in GitHub's own words:
"Only the default branch is indexed for code search," "Only files smaller than 384 KB are searchable,"
and "you must always include at least one search term when searching source code," except when you are
searching by filename alone. Signing in matters here too, GitHub's own wording: "you must be signed
into a personal account on GitHub to search for code across all public repositories." For your own
private repositories specifically, GitHub's own documentation adds one more limit worth knowing: "Up to
4,000 private repositories are searchable," the most recently updated 4,000 out of the first 10,000
private repositories you personally have access to. Almost no small business will hit that ceiling, it
is here so you are not confused if you ever manage a very large number of repositories and something
does not turn up.

### Finding a file by name

Instead of clicking through folders to find one file, use the file finder. On any repository's main
page, look for a **Go to file** search field (it sits above the file list). Click it, then type the
name of the file or folder you want. GitHub's own instructions: "type the name of the file or directory
you'd like to find," then click the one you want from the results underneath.

**The fast way, once you know it exists:** press the **t** key on your keyboard while viewing any part
of a repository. GitHub's own wording: this key "activates the file finder" directly, no clicking
required first.

**One thing worth knowing so a missing file does not confuse you:** the file finder skips certain
folders by default, GitHub's own list is `.git`, `.hg`, `.sass-cache`, `.svn`, `build`, `dot_git`, `log`,
`tmp`, and `vendor`. If a file genuinely exists but will not show up in the file finder, one of those
folder names is the most likely reason, browse to it directly using the regular file list instead.

**Through Claude Code:** if you already have a copy of the repository on your own machine, ask it in
plain English:

```
Find the file that has the menu prices in it.
```

Claude Code searches your local copy directly and tells you where the file is, which is often faster
than opening the browser at all once you are mid-conversation with it about something else.

### Who changed this, and why

Two different views answer two different versions of this question, and knowing which one you actually
want saves you time.

**Use the file's history when your question is "what has happened to this file over time."** Open the
file, then look for **History**, which sits near the commit information above the file's content and
links to the full list of commits that changed that file, newest first. GitHub's own framing of the
difference between this and the wider repository history: "a file's history shows commits that affected
that file, while the repository history shows the broader branch history." Click any entry in that list
to see exactly what changed in that one commit, and who made it.

**Use Blame when your question is "who wrote this specific line, and when."** Open the file, then click
**Blame**, above the file's content, next to the **Raw** and **Copy path** options. GitHub's own
description: "This view gives you a line-by-line revision history, with the code in a file separated by
commit. Each commit lists the author, commit description, and commit date." Click the commit message
next to any line for the full detail on that change, including the reasoning if whoever made it wrote
one.

**One thing worth knowing before Blame confuses you:** if a whole file was reformatted or tidied up in
one big commit, every line can end up crediting that tidy-up commit rather than the change that actually
put the words there originally. If a lot of lines all point at the same commit with a generic message
like "reformatting" or "cleanup," that is usually what happened, click through to that commit's own
description, and if it does not explain the actual content, work backward from there through the file's
history instead.

**How this was checked, and the limit of that check.** GitHub's documentation for viewing a file
describes the Blame view in full, but does not spell out the exact click path to the History link in
the same words. This kit confirmed the History link exists, and where it sits, by opening a real file on
github.com directly during research for this file. Screens change, so if you cannot find it exactly
where described here, look near the commit message shown just above a file's content, that is where it
lives.

**Through Claude Code:** GitHub's own documentation confirms the command-line equivalent of Blame:
"On the command line, you can also use `git blame` to view the revision history of lines within a
file." If you already have a copy of the repository on your machine, you do not need to remember that
command yourself, ask Claude Code in plain English:

```
Show me who last changed the Saturday opening hours in hours.json, and why.
```

Claude Code runs the right git command against your local copy and reads you back the answer, including
the commit message, which is often the fastest route to "why" specifically, since it does not require
you to open a browser tab at all.

### Browsing a repository without hunting

A repository's file list shows folders and files together on its main page, same as any folder on your
own computer. Two things make moving around it faster than clicking one folder at a time:

**The breadcrumb trail.** As you open folders, GitHub adds each one to a row of clickable names across
the top of the page, so opening `docs`, then `content` inside it, leaves you a trail reading `docs /
content`, and each part of that trail is its own link. Click an earlier part of the trail to jump back
several levels in one click, instead of clicking Back repeatedly.

**The collapsible file tree.** Many repository pages also show a **Files** panel down the left-hand
side, which you can expand or collapse, listing the whole folder structure at once so you can see where
something sits without opening each folder in turn. This kit confirmed this panel by opening a real
repository directly during research for this file, GitHub's own documentation was not specific about it
by name, so treat it as something to look for on your own screen rather than something guaranteed to
appear identically everywhere.

**Getting a permanent link to what you are looking at.** If you want to share a link to a file that
will always show exactly the version it shows right now, even after someone else changes it later,
press the **y** key while viewing that file. GitHub's own wording: this key "expands a URL to its
canonical form," which turns the address in your browser into one tied to that exact commit rather than
to "whichever version is current." This matters whenever you are pointing a teammate at something and
you need them looking at what you were actually looking at.

### Saving what you use constantly

**Starring a repository** marks it as one you want to find again quickly. GitHub's own description of
the point of it: "Starring makes it easy to find a repository or topic again later," and it also "shows
appreciation to the repository maintainer for their work." On any repository's main page, click **Star**
in the top-right corner. To find your starred repositories again, click your profile picture, then
**Your stars**, or go directly to your [stars page](https://github.com/stars). GitHub's own note on
using it: "The search bar only searches based on the name of a repository or topic, and not on any other
qualifiers," and you can also sort that list by **Recently starred**, **Recently active**, or **Most
stars**. To remove one, open the repository and click **Starred** (the button relabels itself once you
have already starred something) to unstar it.

**Pinning** puts a small number of repositories front and centre on your own GitHub profile, for anyone
who visits it, including you. Click your profile picture, then **Your profile**, then, at the top of the
"Popular repositories" or "Pinned" section, click **Customize your pins**. Choose which repositories to
include, then click **Save pins**. GitHub's own limit: "Select up to six repositories and gists,
combined." Reorder your pins by dragging them with the grabber icon that appears next to each one while
customizing.

**Saved searches** let you store a query you run often under a short name, so you can run it again with
one click instead of retyping it. Click the search field at the top of any page and type `saved:` to see
your existing saved searches under a "Saved queries" section, along with a **Manage saved searches**
option for creating, editing, or deleting one. GitHub's own description of the point of it: it helps you
"quickly find what you're looking for, often without having to fully type a query or view the search
results page." This is worth setting up for the two or three searches you would otherwise type out from
memory every single week, an open-issues-assigned-to-you search is the obvious first one for most small
teams.

### The keyboard shortcuts worth learning

GitHub documents a long list of keyboard shortcuts. Most of them you will never touch. These few are
worth learning by heart, because they replace something you would otherwise do constantly with your
mouse:

- **`s`** or **`/`**, focuses the search bar from wherever you are on the page.
- **`t`**, opens the file finder, so you can jump straight to a file by typing its name.
- **`l`**, jumps to a specific line number while viewing a file's content.
- **`b`**, opens the Blame view for the file you are currently looking at.
- **`w`**, opens the branch or tag switcher.
- **`y`**, turns the current page's address into a permanent link tied to the exact version you are
  looking at.
- **Ctrl+K** (Windows and Linux) or **Cmd+K** (Mac), opens the Command Palette, GitHub's own single
  search box for jumping to a repository, a file, or an issue, or running an action, without navigating
  any menu first. GitHub's own description of how it decides what to search: it "displays your location
  at the top left and uses it as the scope for suggestions," so it searches more narrowly while you are
  already inside a repository, and more broadly from GitHub's front page.

None of these need memorising all at once. Learn `t` and `/` first, they cover the two things you will
do most, and pick up the rest only once you notice yourself reaching for the mouse to do the same thing
over and over.

## Strategy: how to actually use this

**Search is not worth the habit until you actually have something to lose track of.** With one
repository and a handful of files, scrolling to find something is faster than typing a search query.
The moment you cross roughly a dozen files, or you have more than one repository, or issues start
piling up faster than you close them, that flips, and a well-aimed search beats scrolling every time.
Do not force the habit early, let the pain of hunting teach you when to reach for it.

**Solo, star what you personally use every week, and skip the rest.** Pinning matters much less to you
than to a team, your own profile is not something you are navigating past strangers to reach, you
already know where your own work is most of the time. The one search worth setting up as a saved search
even solo is `is:issue is:open assignee:@me`, so on a Monday morning you can see everything you told
yourself you would get to, across every project, in one click.

**A team of three or four, pinning and saved searches stop being personal convenience and start being
onboarding.** A new person's first ten minutes go faster if your organization's most-used repositories
are pinned somewhere visible, and if there is a shared, agreed convention for labels (`bug`, `waiting on
client`, `this-week`) that makes `label:` searches actually useful across everyone's issues, not just
your own. Agree the label names once, in writing, before anyone starts using them, a `label:bug` search
is only useful if everyone spells "bug" the same way every time.

**Blame and file history earn their keep specifically when something looks wrong and nobody remembers
changing it.** This is the actual, recurring, real use case for a small business: a price is off, a
policy line reads strangely, a setting has clearly changed. Open Blame on that exact line before you ask
around the team, half the time the commit message already answers "why," and you save everyone a Slack
message.

**What good looks like months later:** commit messages that actually say why something changed (covered
in `05-daily-workflow.md`), so that Blame and file history are worth opening at all, because a Blame
view full of messages that just say "update" or "fix" gives you the "who" but not the "why," and "why"
is almost always the half of the question you actually needed answered. A team that writes decent commit
messages from day one gets months of free troubleshooting time out of a habit that costs nothing extra
to build.

## A worked example

A small accounting practice runs four repositories on GitHub: their client portal, their internal
document templates, their website, and a repository a contractor set up for a one-off automation project
last year. Three staff use GitHub day to day.

One Monday, a client calls to say a fee listed on the portal looks wrong. The office manager who took
the call is not the one who built the portal, and has no idea which of the four repositories the fee
even lives in.

She clicks the search field at the top of any GitHub page, types `fee schedule`, and chooses **Search
all of GitHub** rather than guessing which repository to open first. One result comes back from the
client portal repository, a file called `fees.json`. She opens it, clicks **Blame** above the file's
content, and finds the line with the wrong fee. Next to it is a commit from six weeks ago, made by the
practice's junior accountant, with the message "updated fee schedule for FY26, confirmed with Sarah."

Instead of guessing, she now has an actual answer: the fee was changed on purpose six weeks ago, by a
named person, with a stated reason. She checks with Sarah, finds the number typed into the file does not
match what Sarah actually confirmed, a genuine typo rather than a mystery, and fixes it the same
afternoon.

Afterward, she sets up a saved search, `is:issue is:open label:client-facing`, across all four
repositories, so any open issue tagged as something a client might notice surfaces automatically the
next time this happens, rather than relying on a phone call to catch it. She also pins the client portal
and the website to her own profile, the two repositories she opens almost every day, so she stops
navigating to them through the organization's full repository list each time.

## If it goes wrong

**I searched for something I know exists and got nothing back.** Check three things in order: whether
you searched inside one repository when the thing you want is actually in another (try **Search all of
GitHub** instead), whether you are signed in (code search across public repositories specifically
requires it), and whether you actually have access to the repository it lives in, GitHub only shows you
results from repositories you can already open.

**My search for an exact phrase returned things that do not contain that exact phrase.** This is
expected, not a fault in your search. GitHub's own documentation states plainly that its search "doesn't
support exact matching." Quoting a phrase narrows your results toward it, it does not guarantee a
literal match.

**Blame keeps pointing every line at the same commit, even lines I know are old.** A whole-file
reformatting or tidy-up commit can end up "owning" every line in Blame's eyes, since it was the last
commit to touch each one. Open that commit's own description first, if it does not explain the actual
content, use the file's history to work backward to the change that came before it.

**The file finder will not find a file I know exists.** GitHub's file finder skips a small, fixed list of
folder names by default: `.git`, `.hg`, `.sass-cache`, `.svn`, `build`, `dot_git`, `log`, `tmp`, and
`vendor`. If your file sits inside one of those, browse to it directly using the ordinary file list
instead of the file finder.

**I starred or pinned something and now cannot find it again.** Starred repositories live on your
[stars page](https://github.com/stars), reachable from your profile picture, then **Your stars**. Pinned
repositories show on your own profile page itself, under "Pinned." They are two different features with
two different homes, starring is your own private bookmark list, pinning is what shows publicly on your
profile.

**I pressed a keyboard shortcut and nothing happened.** Most of these shortcuts only work while your
cursor is on the page itself, not inside a text box (typing `t` while you are actually typing in a
comment just types the letter t). Click somewhere on the page that is not a text field, then try the
shortcut again.

## FAQ

**Does search show me things from repositories I do not have access to?** No. You only ever see results
from repositories you can already open. GitHub's own documentation confirms this specifically for code
search in private repositories, and nothing in GitHub's documentation suggests general search works any
differently, but if you want to confirm this on your own screen, search for something you know exists in
a private repository you are not a member of, and you should get nothing back.

**What is the actual difference between Blame and a file's history?** Blame answers "who last touched
this exact line, and when." A file's history answers "what is the full list of commits that ever touched
this file, in order." Use Blame when you have found the wrong line already and want to know who put it
there. Use the file's history when you are trying to trace how a whole file got to where it is now.

**Can I search for something inside a Word document, PDF, or image I uploaded to a repository?** GitHub's
own documentation for code search only describes searching the actual text content of files, this kit
could not confirm whether that extends to documents or images, so treat that as something to confirm on
your own screen, and rely on the filename search (`filename:`) as the safer bet for anything that is not
plain text or code.

**Do saved searches update automatically, or do I have to run them again?** A saved search is a stored
query, not a live feed, you still click it (or type `saved:` and pick it) to run it, and it returns
whatever currently matches at the moment you run it.

**Is pinning the same as starring?** No. Starring is a private list you build for yourself, of anything
you want to find again. Pinning is a small, curated, public selection, up to six items, that shows on
your own profile page for anyone who visits it. You can, and often should, do both for the same
repository.

## Quick reference

```
Search all of GitHub:      click the search field at the top of any page, choose "Search all of GitHub"
Search one repository:     open it first, search from inside it, or add repo:OWNER/REPO to a global search
is:issue / is:pr           is:open / is:closed
author:USERNAME            assignee:USERNAME (or assignee:@me for yourself)
mentions:USERNAME          label:"label name"
in:title / in:body         "exact phrase" (narrows, does not guarantee an exact match)
filename:NAME               extension:TYPE   (searching inside file contents)

Find a file by name:       press t, or click "Go to file" above a repository's file list
File's history:            open the file, click History (near the commit info above the content)
Who wrote this line:       open the file, click Blame, or press b
Permanent link to now:     press y while viewing a file

Star a repository:         open it, click Star, top right    -> find again: github.com/stars
Pin a repository:          your profile -> Customize your pins -> up to 6, combined with gists
Saved search:               type saved: in any search field -> Manage saved searches

s or /   focus search        t   file finder        l   jump to a line
b   open Blame                w   switch branch/tag  y   permanent link
Ctrl+K (Windows/Linux) or Cmd+K (Mac)   Command Palette
```

## Sources

- https://docs.github.com/en/search-github/getting-started-with-searching-on-github/about-searching-on-github
- https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax
- https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests
- https://docs.github.com/en/search-github/searching-on-github/searching-code
- https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories
- https://docs.github.com/en/search-github/getting-started-with-searching-on-github/sorting-search-results
- https://docs.github.com/en/search-github/searching-on-github/finding-files-on-github
- https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file
- https://docs.github.com/en/pull-requests/committing-changes-to-your-project/viewing-and-comparing-commits/differences-between-commit-views
- https://docs.github.com/en/get-started/accessibility/keyboard-shortcuts
- https://docs.github.com/en/get-started/accessibility/github-command-palette
- https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars
- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile
- https://docs.github.com/en/search-github/github-code-search/using-github-code-search
