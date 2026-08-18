# Backups, exports, and never being locked in

## What this gets you

A question worth asking before you put real work on any platform: what happens to it if that
platform disappears, changes its terms, or you decide to leave? This file answers that for
GitHub, in plain terms, and the honest short answer is better than most people expect. Because of
how the underlying tool (git, covered below) actually works, every full copy you or a teammate has
ever made of a repository already holds the entire history of that project, not just today's
files. You are less dependent on any one company than you might think, as long as you know where
your copies actually are.

That still leaves real gaps worth closing. A copy of your code is not a copy of the conversation
that happened around it, the issues, the pull request discussion, the back-and-forth that explains
why a change was made. That part lives only on GitHub's own servers unless you deliberately pull
it out. This file covers getting a full copy of your work, exporting the parts of your account
that GitHub tracks separately, backing up the conversation history before you need it rather than
after, a backup routine sized for a small business rather than a data centre, what actually moves
if you leave for another provider, what is destroyed if you delete an account or an organization,
and what GitHub itself formally commits to about staying up and running.

## Before you start

**You need at least one repository with something in it worth protecting.**
`04-repositories-and-visibility.md` covers creating one, and `21-moving-your-work-in.md` covers
bringing existing work in from a folder on your computer, if you have not done either yet.

**You need at least Read access to a repository to copy it.** GitHub's own requirement, in its
own words, covers exactly this: "you have permission to access the repository you want to clone."
`03-members-and-access.md` covers checking or requesting your access level if you are not sure
what you currently have.

**You do not need to already know git, or the command line.** Everything in this file can be done
from the browser, or by describing what you want to Claude Code in plain English. Where the
underlying mechanics are worth understanding, this file explains them in words, not commands you
need to type yourself.

**Nothing in this file needs organization-owner status, unless you are specifically deleting an
organization**, covered near the end. Exporting your own account's data and getting a copy of a
repository you can already see are both things any member can do for themselves.

## The words you need

**Clone.** A full copy of a repository, downloaded to your own computer, that includes the
project's entire history, not only its current files. GitHub's own wording: "Cloning a repository
pulls down a full copy of all the repository data that GitHub.com has at that point in time,
including all versions of every file and folder for the project." This is the thing that makes the
sovereignty question in this file's title less frightening than it sounds: a clone is already a
real backup, sitting on a machine GitHub does not control.

**Source code archive.** A ZIP or tarball file GitHub generates on request, containing a snapshot
of a repository's files exactly as they stand right now. GitHub's own wording draws the line
plainly: "Snapshots don't contain the entire repository history. If you want the entire history,
you can clone the repository." A ZIP is a photograph. A clone is the whole album.

**Personal account data archive.** A separate export, covering your account itself rather than one
repository, that you request from your own account settings. GitHub's own description of its
contents: "GitHub stores repository and profile metadata from your personal account's activity."
This is metadata about your account, not a copy of your repositories' actual code and history,
which is what cloning is for. Do not mistake one for the other.

**Migration archive.** A fuller, more technical export, available through GitHub's own data
interface rather than a settings button, that can bundle a repository's git data together with its
issues, its pull requests, and the comments on both. Covered in detail below, for the moment
backing up the conversation genuinely matters to you.

**Bare clone, and mirror-push.** The two-step technique GitHub itself documents for creating a
full duplicate of a repository elsewhere: first make a clone with nothing extra attached (a "bare"
clone), then push everything in it, including every branch and tag, to a new destination in one go
(a "mirror" push). This is the mechanism behind moving your work to another provider, covered
below.

**Vendor lock-in.** A general, plain-English term, not one GitHub itself uses, for a situation
where switching away from a service you use is difficult or costly, because too much of what you
depend on only exists inside that one service. This file's real subject is checking how much of
that risk actually applies to you, and closing the gaps that do.

## How to do it

### Where your work actually lives, and why a copy on any machine is already a backup

GitHub hosts your repositories, but it does not uniquely hold them. The moment anyone, you, a
teammate, the nephew who built the ordering site, clones a repository rather than only viewing it
in a browser, GitHub's own description of what that action does applies in full: it pulls down
"a full copy of all the repository data GitHub.com has at that point in time, including all
versions of every file and folder for the project." Every version. Not the current state dressed
up as a backup, the actual, complete history, on a machine sitting on someone's desk.

This is the single most important idea in this file. If your business has even one laptop with a
current clone of its important repositories, you already have a real, working backup of that
project's entire history, independent of GitHub, right now, without doing anything new. The
practical work left is making sure that is actually true (a stale clone from a year ago is not the
same as a current one), and closing the gap this file covers next: a clone is a backup of your
code's history, it is not a backup of the conversation that happened on GitHub's own site around
that code.

### Downloading a repository: a ZIP or a clone, and why the difference matters here

You have two genuinely different ways to get a copy of a repository, and only one of them is a
backup in the full sense this file means.

**A ZIP file, GitHub's own three routes to one:** above the file list on a repository's main page,
click **Code**, then **Download ZIP**; from a release, in the **Assets** section, click
**Source code (zip)**; or from the **Tags** page, click the zip link next to any tag. All three
generate the same kind of thing: a snapshot of the files exactly as they stand at that point,
nothing more. GitHub's own wording is direct about the limit: "Snapshots don't contain the entire
repository history."

**A clone, through Claude Code, keeps the whole history and stays connected.**
`05-daily-workflow.md` covers this step by step; the short version is copying the repository's
**HTTPS** link from the same green **Code** button, then telling Claude Code, in plain English,
"Clone this repository for me:" followed by the link. Claude Code runs the underlying `git clone`
command for you and reports back exactly where it put the folder.

**For a genuine backup, prefer the clone.** A ZIP is fine for a one-off look at a project you will
not come back to. It is not fine as the only copy of something your business depends on, because
the moment you need to know what a file looked like six months ago, or who changed what and why,
a ZIP has none of that, and a clone has all of it.

One more detail worth knowing, because it affects whether a ZIP link is something you can rely on
sitting still: GitHub's own wording for how these files are produced is "generated on request,
cached for a while, and then deleted." A ZIP link is not a permanent file waiting on GitHub's
servers for you. It is regenerated when asked for. If you want a permanent copy, downloading it
and actually keeping the file is the step that makes it permanent, the link itself is not that.

**Screenshot placeholder:** the **Code** button's dropdown panel, showing the **HTTPS** clone link
and the **Download ZIP** option in the same view, so a reader can see both routes sitting next to
each other before choosing.

### Exporting your account data

Separately from any one repository, GitHub keeps metadata about your account itself, and lets you
export it directly.

1. In the upper-right corner of any page, click your profile picture, then click **Settings**.
2. In the left sidebar, click **Account**.
3. Find the **Export account data** section and click **Start export** (or **New export**, if
   this is not your first one).

GitHub packages the result into a `tar.gz` file (a compressed archive; if your computer cannot
open it directly, a free extraction tool will) and emails a download link to your primary email
address. **That link expires after seven days by default.** GitHub also lets you disable the link
yourself, from the same **Account** settings page, any time before it expires, if you decide you
no longer want it live.

**Be clear about what this is and is not.** GitHub's own description of the contents is
"repository and profile metadata from your personal account's activity." This is a record about
your account, useful for knowing what GitHub itself holds on you. It is not a substitute for
cloning your repositories, and it does not, on its own, hand you back the conversation inside your
issues and pull requests. That is covered next.

### Backing up issues and pull request discussion, the part people forget

Here is the gap a clone does not close. `13-issues-and-tracking-work.md` and `07-pull-requests.md`
cover issues and pull requests as living, working tools, but neither one lives inside your
repository's git history the way a commit does. They are records kept on GitHub's own servers,
separately, and a plain `git clone` does not bring them down with it. If the discussion attached to
an issue or a pull request is genuinely part of your business's record, deciding it works this
way, agreeing on that price, explaining why a change was made, it is worth pulling out
deliberately, not assuming it travels with everything else.

**For a quick, occasional export, ask Claude Code.** GitHub's own command-line tool can list every
issue or pull request in a repository as structured data, including its comments, and Claude Code
can run this for you and save the result as a plain file. From inside your project folder:

```
Export every issue in this repository, with its comments, to a file called issues-backup.json.
```

Underneath, this runs the equivalent of `gh issue list --json` naming the fields you want, and
GitHub's own documentation for that command confirms `comments` is one of the fields available,
alongside `title`, `body`, `author`, `labels`, `state`, and several others. The same works for
pull requests with `gh pr list`. One thing worth knowing before you rely on this for something
important: GitHub's own default is to fetch "the most recent 30 open items" unless you ask for
more, so for a full backup, tell Claude Code you want everything, open and closed, not just what's
currently outstanding, and it can add the flags that ask for that.

**For a thorough, one-time export of everything together, GitHub has a fuller tool, and it is more
technical.** GitHub's own data-migration system can bundle a repository's git data with its
issues, pull requests, and every comment on both, into a single downloadable archive. GitHub's own
list of what that archive can contain includes, among other things, `issues`, `issue_comments`,
`pull_requests`, `review_comments`, and `repositories`. This is genuinely the most complete option
available, and it is also the one this kit found stated plainly as available only "via the REST
API," not as a button anywhere in the browser. If you want this, the practical route is asking
Claude Code to start and download this export for you, describing what you want in plain English,
rather than looking for it as a settings page, because there isn't one. Confirm on your own screen
what the finished file actually contains once you have it; GitHub's own note is that a generated
archive stays available to download for seven days before it is deleted, so download it somewhere
permanent as soon as it is ready.

### Setting up a realistic backup routine for a small business

None of the above is useful unless it happens on a schedule you will actually keep, and the right
amount of effort here is genuinely small for most of this kit's audience. A few honest rules of
thumb:

- **If a repository matters to your business, at least one machine should hold a current clone of
  it, not just a memory of having downloaded it once.** Refresh that clone (pull the latest
  changes, covered in `05-daily-workflow.md`) whenever you sit down to work in it. You do not need
  a separate "backup step," using it correctly already keeps it current.
- **If two people, or two machines, both hold a current clone, you already have redundancy without
  a special backup tool.** One laptop being lost, stolen, or destroyed does not take the project's
  history with it, as long as a second clone exists somewhere else.
- **Export the conversation, issues and pull request comments, on a schedule that matches how much
  you would actually miss it.** For most small repositories, this is a quarterly or half-yearly
  habit, not a weekly one. For a repository where the discussion genuinely is the business record
  (agreed pricing, a client's specific requirements, a decision explained in a comment thread), do
  it more often, and definitely do it before deleting anything.
- **Do not build a backup system for a repository nobody would notice losing.** A test project, a
  throwaway experiment, a folder you cloned once and never opened again, none of that needs a
  routine. Spend the effort where losing it would actually cost you something.

### Moving to another provider

Your code, and its entire history, is not actually GitHub's to hold onto. It is git's, the
underlying tool GitHub is built on top of, and git itself does not care which company is hosting
it. That is the whole reason a clone already counts as a backup, covered above, and it is also why
moving your code elsewhere is genuinely possible, not a hypothetical.

The technique GitHub itself documents for duplicating a repository is two commands: first, a
**bare clone** (a clone with nothing extra attached, made purely to move on):

```
git clone --bare https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY.git
```

then a **mirror push**, sending everything in it, every branch and every tag, to a new address:

```
git push --mirror https://NEW-HOST/YOUR-ORGANISATION/YOUR-REPOSITORY.git
```

**A genuine hedge worth stating plainly.** GitHub's own documented page for this exact technique
is written for moving between two GitHub repositories, and it explicitly points anyone moving from
a different git-based host in the other direction, into GitHub, at a separate importer tool. This
kit did not find a GitHub-published page walking through pointing the second command at a
non-GitHub destination end to end. The two commands themselves are ordinary git, not something
GitHub built specifically, so there is nothing GitHub-specific stopping the second address from
being a different company's service instead. Confirm the exact address format your new provider
expects on their own page, and consider asking Claude Code to run this for you once you have it,
rather than typing it by hand.

**What genuinely does not travel with a mirror push, and why.** Your code and its full history
move cleanly, because that is what git itself tracks. Anything that only ever lived inside GitHub's
own systems, issues, pull request discussion, the run history of any GitHub Actions workflows, who
is currently a collaborator, does not move with it, for the same reason a ZIP download does not
include it either: none of that was ever part of the git history in the first place. If any of it
matters to you, back it out first, using the steps above, before you consider the move complete.

### Deleting your own account, and what is destroyed

You can delete your personal GitHub account at any time, and GitHub is direct about the one thing
that matters most before you do: "Once your personal account has been deleted, GitHub cannot
restore your content." There is no support ticket that undoes this afterwards. Back up anything
you would miss first, using the steps above, not after.

**A real prerequisite if you belong to any organizations.** GitHub's own wording: "If you're the
only owner in the organization, you must transfer ownership to another person or delete your
organization" first. "If there are other organization owners in the organization, you must remove
yourself from the organization" first. Your personal account cannot be deleted while it is the only
thing keeping an organization administratively alive.

**What gets deleted, in GitHub's own words:** "All repositories, forks of private forks, wikis,
issues, pull requests and GitHub Pages sites owned by your account will be deleted." Your billing
ends immediately. Your username becomes available for anyone else to claim after 90 days.

**One detail worth knowing, hedged honestly.** An older version of GitHub's own documentation
states plainly that "issues and pull requests you've created and comments you've made in
repositories owned by other users will not be deleted." That is, your own contributions to
someone else's project are expected to stay put even after your account is gone. The current
GitHub.com page this kit checked does not repeat that exact line, so treat it as very likely still
true, this is not the kind of behaviour GitHub would be expected to have quietly reversed, but
confirm it directly with GitHub if a real, specific case depends on it.

**The click path:**

1. Profile picture (upper-right corner), then **Settings**.
2. Left sidebar, **Account**.
3. Scroll to the bottom, under **Delete account**, click **Delete your account**.
4. In the confirmation dialog, type your username or email in the first field, then type the exact
   phrase the dialog shows you in the second field.

### Deleting an organization, and what is destroyed

Deleting an organization is a separate, larger action than deleting a single repository, and it is
just as permanent. GitHub's own wording: "GitHub cannot restore your content" once it is done.

**What gets permanently deleted:** "All repositories, forks of private repositories, wikis,
issues, pull requests, and project or organization pages." If the organization's name is attached
to any packages or container images in a GitHub Packages registry, those are deleted too, and
GitHub's own warning is specific: "you may break projects that depend on these packages and
images" elsewhere. The organization's name itself becomes available for anyone to claim again
after 90 days.

**If your actual goal is just to stop paying, not to destroy everything, you do not need this
step.** Downgrading the organization to GitHub Free keeps its repositories and content in place;
it only removes whichever paid features do not exist on the free tier. Deleting the organization
is for when you genuinely want the content gone, not as a routine way to cancel a subscription.

**Who is actually allowed to click this, hedged.** This kit treats deleting an organization as an
owner-only action in practice, the same way `02-organizations.md` treats it, but GitHub's own page
for this specific step does not spell out the permission requirement in so many words. Confirm on
your own screen, or with whoever administers your organization, before relying on that as a
safeguard against an accidental click by someone with less access than you'd expect.

**The click path:**

1. Profile picture (upper-right corner), then **Your organizations**.
2. Click the organization's name.
3. Click **Settings**.
4. Scroll to the **Danger zone** at the bottom of the page and click **Delete this organization**.
5. Type the organization's name to confirm, then click through to cancel any plan and complete the
   deletion.

**Screenshot placeholder:** the organization Settings page scrolled to the Danger Zone, showing
Delete this organization sitting below the other, less permanent options on that same page, so a
reader recognises the visual weight GitHub gives this one before they get there themselves.

### What GitHub commits to about availability

GitHub does make a formal, written commitment about staying up and running, but it is worth
reading exactly who it covers before leaning on it. GitHub's own customer agreement for its paid
Enterprise Cloud product states: "GitHub commits to maintain at least 99.9% Uptime for the
applicable GitHub service," and names three specific services this covers: GitHub Actions, GitHub
Enterprise Cloud, and GitHub Packages. If GitHub misses that figure in a given quarter, the
remedy is a service credit toward your bill, not compensation for anything you lost, and you have
to ask for it in writing within thirty days of the quarter ending.

**Read that scope carefully. This kit did not find GitHub Free, GitHub Pro, or GitHub Team named
in that same commitment.** If your business is on one of those plans rather than a paid Enterprise
Cloud agreement, the practical, honest position is that you are relying on GitHub's own operational
track record and its live public status page, not a contractual promise with a remedy attached to
it. GitHub does publish that status live, at `githubstatus.com`, including current incidents and a
rolling history. Check it yourself for the current picture rather than trusting any specific number
repeated here, because it updates by the day and a figure quoted today will already be out of date
by the time you read this.

**The real point of this section is not the percentage.** An uptime commitment, however GitHub
words it, is a promise about keeping the lights on, not a promise that the company exists in ten
years on the same terms, or that its policies never change. Nothing in this file argues GitHub is
about to disappear. The reason a current clone on your own machine matters is that it does not
depend on any commitment at all, from GitHub or anyone else, which is a stronger position to be in
than trusting a number on a page.

## Strategy: how to actually use this

**A solo operator working alone** gets almost all of the real protection here from one habit: keep
a current clone on the machine you actually work from, and refresh it by using it normally.
Exporting issues and pull request discussion barely matters if you are the only person who was ever
in that conversation, you already remember it, or it is sitting in your email anyway. The moment
worth treating differently is right before you would delete an account or an organization, back
up first, always, no exceptions, because that step alone is the one GitHub is explicit cannot be
undone afterwards.

**A team of three or four** gets real value from two extra habits a solo operator does not need.
First, more than one person's machine should hold a current clone, so the business is not one
laptop away from losing a project's history, this happens naturally once more than one person is
actively working in a repository, but is worth checking rather than assuming. Second, if issues and
pull requests are where real decisions get explained, pricing agreed, requirements written down,
that record is worth exporting on the quarterly-or-so schedule covered above, because losing it is
a genuinely different kind of loss than losing code, it is losing the reasoning behind the code.

**When this is overkill.** A single repository nobody else has ever opened, a personal experiment,
a template nobody would notice going away, none of it needs a backup routine at all. The judgement
call throughout this file is the same one this kit repeats elsewhere: match the effort to what
losing the thing would actually cost you, not to what is technically possible to protect.

**What good looks like months later.** At least one current, recently-refreshed clone of every
repository the business actually depends on, sitting on more than one machine if more than one
person works in it. A recent export of issue and pull request discussion for anything where that
conversation is part of the real record, not a scramble to grab it the day someone decides to
leave, delete an account, or move providers. Nobody discovering, at the worst possible moment, that
the only copy of something was a browser tab.

## A worked example

The café's ordering site, this kit's recurring example, is cloned onto two machines: the nephew's
laptop, where he does the actual work, and, since a conversation earlier in this kit, the
front-counter desktop the owner occasionally checks it from. Neither of them thinks of this as "a
backup." It is just how they both already work. But it means that if either machine failed
tomorrow, the entire project, every version of every file, all the way back to the first commit,
would still exist on the other one, without either of them having set up anything special for
that.

What they had never thought about was the issue thread where the owner first described exactly how
delivery charges should work, the conversation the March fix (covered in
`17-releases-and-versions.md`) was actually built from. None of that lived in the code itself, only
in GitHub's own record of the issue. Prompted by a question from a business mentor, "what happens
to all that if you two ever stopped using GitHub", the owner asks Claude Code to export every issue
in the repository, with its comments, to a file, and saves it in the same folder where she keeps
the café's other business records. It takes a few minutes, costs nothing, and closes the one real
gap the two clones on their laptops never covered.

Separately, the nephew, thinking ahead to a possible future where he takes the ordering site's
underlying framework and reuses it for a different client on a different platform, tries the bare
clone and mirror push technique on a personal side project first, pointing the second command at a
different host's address rather than another GitHub repository, to confirm for himself, on his own
screen, that his understanding of how the addresses work is correct before he would ever consider
doing it with something the café actually depends on.

## If it goes wrong

**I downloaded a ZIP thinking it was a full backup, and now I need something from three months
ago.** A ZIP never had that history to begin with, GitHub's own wording is explicit that snapshots
"don't contain the entire repository history." If a clone exists anywhere, current or not, check
that first: even an older clone holds real history up to the point it was last updated, which a
ZIP never has at all. Going forward, prefer a clone over a ZIP for anything you might need to look
back on.

**I exported my account data and expected my repositories' code to be inside it.** It was never
going to be. GitHub's own description of that export is "repository and profile metadata," not the
repositories themselves. Cloning is the separate step that gets you the actual code and its
history, covered above.

**The download link for my account export, or my migration archive, expired before I downloaded
it.** Both are time-limited by GitHub's own design, seven days for each, by default. Nothing is
lost permanently, start the export again from the same settings page or the same process, and
download it promptly this time rather than leaving the email sitting unread.

**I deleted an organization and only afterwards remembered a repository inside it that mattered.**
GitHub's own wording here is unambiguous: "GitHub cannot restore your content." There is no
recovery path documented for this. This is precisely why this file's advice is to back up first,
always, before any deletion, not to treat deletion as safely reversible because most other actions
on GitHub are.

**I moved my code to another provider with a mirror push, and now issues and pull requests I
expected to see over there are missing.** They were never going to move. A mirror push carries git
data, your code and its history, and nothing else, because issues and pull requests were never part
of git's own history in the first place, they live only inside GitHub's own systems. If you needed
that record on the new provider, it has to be exported and re-entered separately; there is no
GitHub feature that carries it across automatically.

**I am the sole owner of an organization and tried to delete my personal account, and GitHub would
not let me.** This is expected, not a fault. GitHub's own rule is plain: as the only owner, you
must first transfer ownership to someone else, or delete the organization outright, before your
personal account deletion is allowed to go through.

## FAQ

**If GitHub shut down tomorrow, would I lose my business's code?** Only the parts that only ever
existed on GitHub's own servers and were never cloned anywhere. Anything with a current clone on a
machine you control already exists independently of GitHub, in full, including its history, right
now. The genuinely vulnerable part is anything that lives only in GitHub's own systems and was
never exported, issues, pull request discussion, and the like, covered throughout this file.

**Is a clone the same thing as "my code is safe forever"?** No, a clone is only as safe as the
machine it sits on. A single laptop with the only current clone is a single point of failure, the
same way a single physical filing cabinet would be. The fix is the same one this file gives
throughout: more than one current copy, on more than one machine.

**Do I need to export my issues and pull requests if I'm never planning to leave GitHub or delete
anything?** Mostly no, for casual use. The value of exporting them shows up specifically when
something is about to change, deleting an account or an organization, moving to another provider,
or wanting a durable written record of a decision that currently only exists as a comment
thread. If none of those are on the horizon, the conversation stays perfectly safe sitting where it
is.

**Does making a private repository public change any of this?** No, this file's whole subject is
independent of that choice. `04-repositories-and-visibility.md` covers what public actually exposes;
backups and exports work the same way, and matter for the same reasons, whichever one you have
chosen.

**Can I get my data back if I already deleted my account or my organization?** No. Every source
this file checked from GitHub's own documentation says the same thing, in the same words: "GitHub
cannot restore your content." Treat that sentence as final, and back up before deleting, not after.

**Is there a single "back up everything" button?** No, and this file is honest about that rather
than pretending there is one. There are separate pieces, cloning your repositories, exporting your
account data, and separately exporting issues and pull request discussion, and putting the right
ones together, on a schedule that matches how much you would actually miss each part, is the real
answer.

## Quick reference

- **A clone already is a real backup**, full history included: GitHub's own wording, "a full copy
  of all the repository data... including all versions of every file and folder."
- **A ZIP download is a snapshot only**, no history. Fine for a one-off look, not a backup on its
  own.
- **Export your account data:** profile picture, **Settings**, **Account**, **Export account
  data**, **Start export**. Emailed link, expires in 7 days by default.
- **Back up issues and pull requests with their comments:** ask Claude Code, for example "Export
  every issue in this repository, with its comments, to a file."
- **The fullest export (repository plus issues plus comments together):** GitHub's migration
  archive, API-only, ask Claude Code to run it for you; downloadable for 7 days once ready.
- **Moving to another provider:** `git clone --bare` then `git push --mirror` to the new address.
  Code and history move. Issues, pull requests, and Actions run history do not.
- **Deleting your personal account:** Settings, Account, **Delete your account**, at the bottom.
  Permanent. Must resolve sole organization ownership first.
- **Deleting an organization:** organization's Settings, **Danger zone**, **Delete this
  organization**. Permanent. Just want to stop paying? Downgrade to Free instead.
- **GitHub's written uptime commitment** covers GitHub Actions, GitHub Enterprise Cloud, and
  GitHub Packages, under a paid Enterprise Cloud agreement, at 99.9% per quarter. Check
  `githubstatus.com` for the current live picture rather than trusting any fixed number.
- **Back up before you delete anything.** Every relevant GitHub source says the same thing:
  content cannot be restored afterwards.

## Sources

- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives
- https://docs.github.com/en/get-started/archiving-your-github-personal-account-and-public-repositories/requesting-an-archive-of-your-personal-accounts-data
- https://docs.github.com/en/rest/migrations/users
- https://cli.github.com/manual/gh_issue_list
- https://cli.github.com/manual/gh_issue_view
- https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository
- https://docs.github.com/en/account-and-profile/how-tos/account-management/deleting-your-personal-account
- https://docs.github.com/en/account-and-profile/reference/personal-account-reference
- https://docs.github.com/en/enterprise-server@3.6/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/deleting-your-personal-account
- https://docs.github.com/en/organizations/managing-organization-settings/deleting-an-organization-account
- https://docs.github.com/en/billing/managing-the-plan-for-your-github-account/downgrading-your-accounts-plan
- https://github.com/customer-terms/github-online-services-sla
- https://www.githubstatus.com/
- https://github.com/selrai-company/github-training-content
