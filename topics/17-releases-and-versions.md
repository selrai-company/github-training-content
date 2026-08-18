# Releases and versions, marking what you shipped

## What this gets you

A release is how you point at your repository and say "this exact state, right here, is what went
out." Not the current state, which keeps changing as people keep working. One specific moment,
permanently labelled, that you can come back to on any later date.

For a small business, this answers a question that otherwise has no good answer: "what exactly was
live in March?" Without a release, that question sends someone digging through months of individual
changes trying to reconstruct what the website, the document, or the build actually looked like on a
given day. With a release, you open the list, find the one dated around then, and you are looking at
the real answer in seconds, not a guess pieced together from memory.

It is also how you hand someone something finished. A customer downloading a template, a client
downloading a report, a teammate installing the version you actually tested, rather than whatever
happens to be sitting in the repository at the moment they look. A release is a fixed point you can
safely point other people at.

## Before you start

**You need a repository**, and something in it worth marking a version of. If you have not created
one yet, `04-repositories-and-visibility.md` covers that first.

**You need Write access to that repository.** GitHub's own wording: "Only people with write
permissions to a repository can manage releases." GitHub's own permissions table for a repository
role in an organization confirms the same thing at the Write role and above, and separately shows
that creating a release and viewing a release that is still a draft both start at Write, not at
Triage. If you only have Read access, you can look at a repository's published releases, but you
cannot create one yourself. `03-members-and-access.md` covers checking or changing your access
level.

**You do not need to already understand branches or pull requests.** A release can be made straight
from your default branch with nothing else going on. If your work does involve branches and pull
requests, `06-branches.md` and `07-pull-requests.md` cover getting a change into your default branch
first, which is usually the point at which a release is worth making.

## The words you need

**Tag.** A permanent label attached to one specific point in your repository's history. GitHub's own
wording: "Releases are based on Git tags, which mark a specific point in your repository's history."
Once a tag exists, it always points at that same point, even after you keep working and everything
else moves on.

**Release.** A tag with a title, a description, and, optionally, files attached, all wrapped up
together on its own page. GitHub's own description: "Releases are deployable software iterations you
can package and make available for a wider audience to download and use."

**Release notes.** The written description on a release's page, explaining what changed and why it
matters. You can write this by hand, or have GitHub write a first draft of it for you (covered
below).

**Asset.** A file attached to a release. GitHub's own phrase for the box you drop them into is "the
binaries box." GitHub also automatically adds two files to every release without you doing anything:
a zip file and a tarball, both containing the full contents of your repository exactly as it stood
at that tag.

**Source code archive.** The zip file and tarball GitHub adds automatically, described above. This is
different from an asset you upload yourself, GitHub always includes these two, on top of whatever you
attach.

**Draft.** A release you have started but not published yet. Nobody with only Read access to your
repository can see a draft, so it is safe to leave one half-finished while you gather the rest of what
belongs in it.

**Pre-release.** A release you have published, but marked as not ready for everyday use. GitHub's own
wording for what this is for: "to notify users that the release is not ready for production and may
be unstable."

**Latest release.** A label GitHub shows next to one release in your list, marking it as the current
one. You can set this yourself, or let GitHub work it out for you, covered below.

**Version number.** The label you give the tag itself, like `v1.0` or `v2`. GitHub does not force any
particular format on you. A simple scheme worth adopting is covered under Strategy below.

## How to do it

### Creating a release in the browser

1. On the repository's main page, to the right of the file list, click **Releases**.
2. At the top of the page, click **Draft a new release**.
3. Click the **Choose a tag** dropdown. To reuse a tag that already exists, click it. To make a new
   one, type a version number and click **Create new tag**.
4. If you made a new tag, click the **Target** dropdown and choose the branch you are releasing from,
   usually your default branch.
5. Optionally, click the **Previous tag** dropdown and choose the tag your last release used. GitHub
   uses this to work out what changed between the two, covered under release notes below.
6. In the **Release title** field, type a short title.
7. In the **Describe this release** field, write your release notes, or click **Generate release
   notes** to have GitHub draft a starting point for you (covered below).
8. Optionally, drag files into the binaries box, or click to choose them, if you have anything for
   people to download alongside the source code.
9. Optionally, select **This is a pre-release** if the release is not ready for everyday use yet.
10. Optionally, select **Set as latest release**. If you leave this unticked, GitHub decides which
    release counts as "latest" for you, based on version numbering, covered under Strategy below.
11. Optionally, select **Create a discussion for this release** and pick a category, if your
    repository has Discussions turned on and you want people to be able to comment on this release
    as a group. This kit does not otherwise cover Discussions; leave this unticked if you are not
    sure what it does, nothing else on the form depends on it.
12. Click **Publish release** to make it live, or **Save draft** to keep working on it later without
    anyone else seeing it yet.

You will know it worked because the release now has its own page, listed at the top of your
repository's Releases tab if it is the latest one, with your title, your notes, and, if you added
any, your files, all sitting underneath it.

**Screenshot placeholder:** the release creation form after "Choose a tag" has been clicked, showing
the "Create new tag" option beneath a typed-in version number, so a reader can see what that step
looks like before committing to it.

### Writing release notes a non-technical person can read

The habit worth having: write the release notes for the person who will read them later with no
memory of today, not for yourself right now. "Fixed the ordering form so GST calculates correctly on
delivery orders" tells a future reader everything. "Bug fixes" does not, and a list of releases that
all say "bug fixes" is no more useful than no release notes at all.

**A short, readable release note usually has three things:** what changed, in plain words, not code
terms. Why it mattered, in one line, if it is not obvious. And, if the change fixed something someone
reported, a mention of what was reported, so a future reader can match a complaint to its fix.

**GitHub will draft a starting point for you.** Click **Generate release notes** on the creation
form, and GitHub fills in the description box automatically. GitHub's own description of what this
produces: "a list of merged pull requests, a list of contributors to the release, and a link to a
full changelog." This is genuinely useful as a technical record of exactly what changed, but it is
written in GitHub's terms, pull request titles and usernames, not necessarily in terms a customer or
a non-technical teammate would find useful on its own. Treat it as a first draft: keep it if your
audience is technical, or add two or three plain-English lines above it if the people reading this
release are not.

### Version numbering, without the dogma

GitHub does not require any particular format for a version number. It is free text on the tag. That
said, GitHub's own behaviour gives you a reason to pick a sensible scheme anyway: if you do not
manually select **Set as latest release**, GitHub's own wording is that "the latest release label
will automatically be assigned based on semantic versioning." If your tags do not look like version
numbers at all, that automatic ordering has nothing to work from, so it is worth either using a
version-numbering scheme or ticking **Set as latest release** yourself every time.

**A simple scheme worth adopting, if you do not already have one:** three numbers, separated by
dots, in the form `MAJOR.MINOR.PATCH`. This is the shape GitHub's own wording refers to as "semantic
versioning," and it is worth adopting because everyone who has ever used software already
half-understands it.

- The first number, **MAJOR**, goes up for a big change, especially one that changes how something
  works for the people using it.
- The second number, **MINOR**, goes up for something new added, without changing what already
  existed.
- The third number, **PATCH**, goes up for a fix, a correction, or a small tidy-up.

A first release is usually `1.0.0`. A small fix after that is `1.0.1`. Adding something new,
without breaking what was there, is `1.1.0`. A significant redesign is `2.0.0`. Most people
write a `v` in front when typing the tag itself, `v1.0.0`, which is a habit, not a rule.

**For a small business that is not shipping software at all,** a document set, a set of templates, a
snapshot of a website, three numbers is often more precision than you need. A single number that goes
up by one every time, `v1`, `v2`, `v3`, works fine, and is easier for a non-technical team to agree
on without a conversation about what counts as "major." Pick one scheme and stay with it. Changing
schemes partway through a project is the thing that actually causes confusion, not which scheme you
picked.

### Attaching files people download

Anything you drag into the binaries box on the creation form becomes downloadable from that
release's page alongside the automatic source code archive. GitHub's own limits on this: "Each file
included in a release must be under 2 GiB," "up to 1000 release assets may be associated with a
single release," and "there is no limit on the total size of a release, nor bandwidth usage." A GiB,
short for gibibyte, is close enough to a gigabyte for everyday purposes, so treat the 2 GiB limit as
roughly 2,000 megabytes, larger than almost anything a small business attaches to a release.

**If you forgot a file, or need to add one after the release is already published**, you do not need
to start over. Through Claude Code, from inside your project folder:

```
Upload the file report-march.pdf to the v1.2.0 release.
```

Claude Code runs the equivalent of `gh release upload v1.2.0 report-march.pdf` for you. If a file
with that name is already attached and you want to replace it, say so, GitHub's CLI needs an explicit
instruction to overwrite rather than doing it by default.

### Pre-releases and drafts

Use a **draft** while you are still assembling a release and are not ready for anyone else to see it.
GitHub keeps it hidden from anyone without Write access to the repository until you publish it,
GitHub's own permissions table shows viewing a draft release requires the same Write role as creating
one. Nothing about a draft is visible on your repository's main Releases list to a Read-only
teammate or an outside visitor.

Use a **pre-release** once you are ready to publish, but the contents are not something you would put
in front of a customer yet, an early look, a version still being tested, something you want a specific
person to check before it becomes the version everyone gets pointed at. Tick **This is a pre-release**
on the creation form. GitHub's own wording for the purpose: it is there "to notify users that the
release is not ready for production and may be unstable."

Neither of these needs any special access beyond the Write access already required to make any
release at all.

### Getting a past release through Claude Code

Once you have releases to look back on, Claude Code can pull one up for you without you touching the
browser. From inside your project folder:

```
Show me the release notes for v1.2.0.
```

or, to list everything so far:

```
List every release in this repository, newest first.
```

Claude Code runs `gh release view v1.2.0` or `gh release list` for you and reads the result back in
plain English. To download the actual files from a specific release rather than just read about it:

```
Download the files attached to release v1.2.0 into my Downloads folder.
```

which runs the equivalent of `gh release download v1.2.0`.

## Strategy: how to actually use this

**A release earns its keep the moment someone, including future you, needs to point at a fixed
version of something rather than "whatever it currently looks like."** If nobody has ever asked, or
would ever plausibly ask, "what did this look like on a given date," or "can I get the version from
before that change," releases are not doing anything for you yet, and that is fine.

**A solo operator working alone** gets real value out of releases the moment they are shipping
something to someone else, a document, a template, a build, even occasionally. It buys almost nothing
while everything stays on the laptop and nobody downloads anything, the current state of the
repository already is the answer to "what does this look like right now." Start using releases the
day you first hand something to someone outside your own head.

**A team of three, one of them technical** (the café and its ordering site, covered throughout this
kit) gets the most practical use out of releases around exactly the question this file opened with:
"what was live on a given date." The technical person tags a release each time a real change goes
live on the ordering site, not for every small edit, but for anything that changes how the site
behaves for a customer. The other two never need to touch the Releases tab themselves; it exists so
that when a question comes up later, there is a real answer waiting instead of a guess.

**When it is overkill:** a repository of documents that only ever matters in its current form, a
shared price list nobody looks back on, a set of notes edited in place, does not need releases at
all. Making one for every small edit to a file like that adds a step that returns nothing, since
nobody is ever going to ask what the price list looked like on a Tuesday in June. Reach for a release
when the answer to "would someone want this exact version again" is genuinely yes, not as a habit
applied to everything in a repository.

**What good looks like months later:** a short, readable list of releases, each with a title that
tells you what changed without opening it, roughly matching the moments the business actually cared
about, a launch, a fix, a season's menu. Not a release for every single change, and not zero releases
either. Somewhere in between, driven by "would I want to come back to this specific point," is the
right amount for almost every small business using this kit.

## A worked example

The café's ordering site, run by the nephew with Write access, has been stable for a few months. In
early March, he makes a real change: he fixes how the checkout page calculates delivery charges. He
tags this state `v1.3.0`, with the release title "Delivery charge fix" and a short note: "Delivery
orders under $30 were being charged the pickup rate. Corrected so delivery orders now charge the
delivery rate." He does not attach any files, this release exists purely as a marker and a written
record, not something anyone downloads.

Two months later, a regular customer emails the café owner insisting she was charged the wrong
delivery fee back in early March, before the fix. The owner does not know the code and cannot check
this herself, but she does not need to. She opens the repository's Releases tab, scrolls to the
release dated around when the customer placed the order, and reads its title: "Delivery charge fix,"
dated after the customer's order. That confirms the bug was still live when the customer ordered, and
the owner can refund her with confidence instead of guessing.

The nephew, separately, wants to preview a redesigned homepage before the owner sees the finished
version. He publishes it as a release tagged `v1.4.0-preview`, with **This is a pre-release** ticked,
and sends the owner the link directly. She can see it and comment, but it never shows as the site's
"latest release," and a casual visitor to the repository would not stumble onto it by accident.

## If it goes wrong

**I don't see a Releases link on a repository where I expect one.** Check you are looking to the
right of the file list on the repository's main page, that is where GitHub places it. If it is
genuinely not there, confirm on your own screen whether the repository has any releases published
yet; a brand-new repository with none can still show the same link, so an absent link is worth a
second look rather than an assumption.

**I clicked Draft a new release, or tried to publish one, and nothing happened.** This almost always
means you have Read access to the repository rather than Write. GitHub's own wording is that "only
people with write permissions to a repository can manage releases." Check your access level in
`03-members-and-access.md`, or ask whoever administers the repository to raise it.

**A teammate says they can't see a draft release I made.** That is expected, not a fault. Draft
releases are only visible to people with Write access or higher, the same level required to create
one. If they need to see it, either publish it, or confirm they actually have Write access rather
than Read.

**I uploaded a file over 2 GiB and it failed.** GitHub's own stated limit is that "each file included
in a release must be under 2 GiB." Split the file, compress it further, or host it somewhere designed
for large files and link to it from the release notes instead.

**I deleted a release and I'm not sure the tag is gone too.** It is not, by default. GitHub's own
command-line tool documents a separate flag, `--cleanup-tag`, described as "delete the specified tag
in addition to its release," which only makes sense if the plain delete leaves the tag behind. Check
your repository's Tags tab (next to Releases, at the top of the Releases page) to see whether the tag
is still there.

**I deleted a release outright and want it back.** This kit could not confirm a documented way to
restore a deleted release from GitHub's own pages, so treat deleting one as final. If you are not
sure yet whether you will want it again, leaving it published, even a slightly out-of-date one, costs
you nothing, deleting is the step you cannot undo.

**I can't edit an old release's files or notes anymore.** Some repositories have a setting called
release immutability turned on, which locks a release's contents once it is published. GitHub's own
wording for what it does is prevent changes to a release after the fact, as a security measure. If
you hit this, whoever administers your repository can confirm on their own screen whether that
setting is on, under the repository's Settings, in the Releases section.

## FAQ

**What's the actual difference between a tag and a release?** A tag is the permanent label on a
point in your history, and it can exist entirely on its own with no title, no notes, and nothing
attached. A release is a tag wrapped with a title, a description, and, optionally, files, all
gathered onto one readable page. Every release has a tag underneath it; not every tag has a release
built on top of it.

**Do I have to use version numbers like `v1.2.3`?** No. GitHub does not enforce a format on the tag
name. It is worth adopting a consistent scheme anyway, covered under Strategy above, mainly so
GitHub's automatic "latest release" labelling and your own future self both have something sensible
to compare.

**Does deleting a release also delete the tag?** No, not automatically. GitHub's own command-line
tool offers a separate `--cleanup-tag` flag specifically for also removing the tag, which would not
need to exist if deleting a release already removed it.

**Can two releases share the same tag?** No. GitHub bases a release on one specific tag, and each tag
points at one specific point in your history. If you need to correct a release, edit the existing one
rather than making a second release on the same tag.

**Do I need to know git or the command line to make a release?** No. Everything in this file's "How
to do it" section can be done from the browser, start to finish. The command-line examples are there
for the moments Claude Code does the typing for you, not because the browser path is missing
anything.

**Is a pre-release visible to everyone who can see the repository?** Yes, once published, a
pre-release is visible the same way any published release is, to anyone with at least Read access.
Marking it as a pre-release changes how it is labelled and whether it counts as "latest," not who can
see it. If you need something hidden from most people entirely, that is what a draft is for instead,
covered above.

## Quick reference

- **Create a release:** repository page, **Releases**, **Draft a new release**, choose or create a
  tag, fill in title and notes, **Publish release**
- **Save without publishing:** same form, click **Save draft** instead
- **Auto-draft notes:** on the creation form, click **Generate release notes**
- **Attach a file:** drag it into the binaries box on the creation form
- **Mark not-ready-yet:** tick **This is a pre-release**
- **Force a specific release to show as latest:** tick **Set as latest release**
- **A simple version scheme:** `MAJOR.MINOR.PATCH`, e.g. `v1.0.0`, or just `v1`, `v2`, `v3` if three
  numbers is more than you need
- **File size limit per asset:** under 2 GiB, up to 1000 assets per release
- **Through Claude Code:** "Show me the release notes for v1.2.0", "List every release", "Download the
  files from v1.2.0", "Upload report.pdf to v1.2.0"

## Sources

- https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
- https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases
- https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags
- https://docs.github.com/en/desktop/managing-commits/managing-tags-in-github-desktop
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization
- https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes
- https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository
- https://cli.github.com/manual/gh_release_create
- https://cli.github.com/manual/gh_release_list
- https://cli.github.com/manual/gh_release_view
- https://cli.github.com/manual/gh_release_download
- https://cli.github.com/manual/gh_release_upload
- https://cli.github.com/manual/gh_release_delete
