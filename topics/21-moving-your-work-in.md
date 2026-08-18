# Moving work you already have into GitHub

## What this gets you

Right now your work lives in one folder, on one laptop, reachable by one person: you. If that
laptop is lost, stolen, or spills coffee on itself, the work goes with it. If a bookkeeper, a
virtual assistant, or a business partner needs to see the latest price list or the half-built
booking page, you email a file, or a ZIP, and from that moment there are two versions of the
truth and no way to know which one is current.

Moving that folder into GitHub fixes both problems at once. The work now lives somewhere that
does not depend on one laptop surviving, and anyone you choose to give access to sees the same,
current version you do, without you sending anything by hand. This page walks through doing
that move once, safely, for one project. It also covers the one step that matters more than any
other on this page: checking what is actually in that folder before any of it leaves your
laptop.

## Before you start

**You need a GitHub account.** If you have not made one yet, `01-accounts-and-security.md`
covers that, including turning on two-factor authentication, which this kit recommends doing
before you put any real work anywhere near GitHub.

**Know roughly what is in the folder you are about to move**, even if you have not opened some of
these files in months. You do not need a complete inventory, but you should be able to say, in
one sentence, what the project is and roughly what kinds of files are in it (documents,
spreadsheets, images, code, a mix). The next section is where that pays off.

**Decide whether this repository will be public or private before you start**, and if you are
not sure, start private. `04-repositories-and-visibility.md` covers the exact difference; the
short version is that public means every stranger on the internet can see it, and there is no
"just my team" setting other than private plus adding the specific people you choose. Almost
everything a small business moves in from a laptop belongs in a private repository.

**This page assumes you already know what a repository is: a folder GitHub tracks for you, where
every change is kept.** If that is new, read the first section of `04-repositories-and-visibility.md`
before this one. This page does not re-teach repository creation from scratch; it teaches getting
existing work into one.

## The words you need

**Upload.** Sending a copy of files from your computer up to a repository on GitHub, through the
browser, by choosing them or dragging them in.

**Push.** The equivalent action done through git, the tool underneath GitHub, usually with Claude
Code running it for you. Same outcome as an upload, different route: an upload is one click-based
action in the browser, a push is a short sequence of commands that also carries any history you
have already built up. For a folder that has never been tracked by git before, described below,
there is no history yet either way, so the two routes end up in almost the same place.

**Commit.** A saved snapshot of a change, with a short message describing what it was.
`05-daily-workflow.md` covers this in full if you have not met it yet.

**.gitignore.** A file you put in a repository that tells GitHub which files to never track, so
things like passwords never get the chance to be uploaded in the first place. Covered in depth in
`04-repositories-and-visibility.md`, and used again below.

**Secret.** A password, an API key, a token, or any credential that proves who you are to some
other service. The word covers anything that would let someone impersonate you or your business
if they got hold of it.

**Git LFS (Git Large File Storage).** A separate system for handling files too big for GitHub to
track normally, videos, large design files, that kind of thing. Covered below, in the very large
files section.

**Collaborator, and organization member.** The two ways to give someone else access to a
repository: a collaborator is added to one specific repository under your personal account, an
organization member belongs to a shared organization account and gets access according to that
organization's own settings. `03-members-and-access.md` and the collaborator section of
`04-repositories-and-visibility.md` cover both in full; this page only covers telling your team
once access is sorted, not setting the access up.

## How to do it

### Stop: check what is in the folder before anything leaves your laptop

Read this section before you touch the "Upload" or "Clone" buttons anywhere else on this page.
**Once a file has left your laptop and reached GitHub, even for a moment, even in a private
repository you delete five minutes later, treat it as seen.** Deleting a file in a later commit
does not erase it from the repository's history, `04-repositories-and-visibility.md` covers
exactly why in its `.gitignore` section, and even a repository you delete outright has, in
GitHub's own words, only "some" chance of being restored within 90 days, not a guarantee either
way. The safe moment to catch a problem is before the first upload, not after.

Go through the folder you are about to move and look specifically for:

- **A password, key, or token typed directly into a file.** Common places this hides: a file
  literally named something like `passwords.txt` or `login-info.docx`, a `.env` file, a
  configuration file for software you use, or a note you jotted a password into once and forgot
  about.
- **Client or customer data**, a spreadsheet of contact details, payment information, or anything
  a client gave you that they would not expect to see sitting in a shared folder. This is not a
  GitHub rule, it is your own judgement about what your clients would reasonably expect, and it
  matters just as much in a private repository as a public one, because a private repository is
  still shared the moment you add a second person to it.
- **Anything you would not want a stranger to read**, even if it is not technically a secret or
  client data. If you are unsure whether something belongs, leave it out for now. Moving it in
  later takes thirty seconds. Getting it back out of a repository's history does not.

**A genuinely good use of Claude Code here, and a safe one:** ask it, in plain English, something
like "Look through this folder and tell me if you see anything that looks like a password, an API
key, a token, or a file of customer or client information, before I upload any of it to GitHub."
This is reading files already sitting on your own machine, nothing leaves your computer to do it,
and a second look at exactly this one question is worth the short wait.

**Do not rely on GitHub's own push protection to catch this instead of checking yourself.**
`10-protecting-your-work.md` covers push protection in full; the short version is that it only
looks at what is being pushed at that exact moment, it needs a paid plan turned on to run at all
on an organization-owned private repository, and even where it is on, anyone with Write access can
bypass it by typing a reason. It is a genuinely useful backstop. It is not a substitute for
looking through your own folder first.

### Assessing what you actually have

Once the secrets check above is done, look at the folder itself with two questions in mind.

**Is this one project, or several projects living in the same folder?** GitHub works best when one
repository maps to one thing you could describe in a sentence, "the invoicing project," "the
booking page." If your folder is actually three different projects that happened to end up in the
same place over time, decide that now, before you upload anything, because splitting them apart
afterward is real, avoidable work. `STRATEGY-PACK.md`'s section on what to standardise covers this
choice in more depth if you want it.

**Roughly how big is this folder, and does it contain anything unusually large?** A folder of
documents and spreadsheets is rarely a problem. A folder with videos, exported design files, or
years of accumulated photos might run into the file size limits covered later on this page. You do
not need an exact number yet, just a sense of whether anything in there is a large media file, so
you are not surprised by a size warning partway through the next step.

### Uploading an existing folder through the browser

This is the more visible of the two routes, and the better one the first time you do this, since
you can see exactly what lands where.

1. If you have not created the repository yet, do that now, following `04-repositories-and-visibility.md`'s
   creation steps: choose private if you are at all unsure, turn on **Add a README file**, and add
   a `.gitignore` (that same file's `.gitignore` section has a starting template that blocks `.env`
   files by default, worth using even if nothing in your folder is called that).
2. On the repository's main page, click the **Add file** dropdown, then click **Upload files**.
3. Drag the files (or the folder) from your computer into the upload area, or click **choose your
   files** and select them that way. GitHub's own instructions describe this step as being able to
   "drag and drop the file or folder."
4. Wait for everything to finish uploading, then look at the file list GitHub shows you before you
   commit anything. **Confirm your folder structure landed the way you expected.** GitHub's own
   documentation does not spell out exactly how nested folders behave in every case, so this is a
   moment to check your own screen rather than assume: if everything landed one folder level
   deeper than you intended, that is fixable (delete the extra layer and re-upload), not a
   disaster.
5. Scroll down, write a commit message describing what this upload is (something like "Add
   existing invoicing project files"), and choose whether to commit directly to your main branch
   or start a pull request instead. For a first upload into your own new repository, direct is
   normal.
6. Click **Commit changes** (the button reads **Propose changes** instead if you chose the branch
   option).

**Two limits worth knowing before you start dragging files in.** GitHub's own stated limits: files
uploaded through the browser are "limited to 25 MiB per file," and you can "upload up to 100 files
to GitHub at the same time." A folder bigger than that is not a problem, you upload it in more
than one batch, but knowing the limit up front means a stalled upload does not look like something
broke.

**One thing the browser upload quietly skips.** GitHub's own documentation states plainly that
"Uploading a file through the GitHub web interface will ignore `.gitattributes`," a more advanced
file some projects use to control things like line-ending conversion. Most small-business folders
will never have one of these and this will never matter, but if you know your project has a
`.gitattributes` file, the Claude Code route below respects it and the browser upload does not.

**Screenshot placeholder:** the Upload files screen mid-drag, showing files listed underneath the
drop area with their individual sizes, and the commit message box at the bottom, so a reader
recognises this screen and the two limits above before they hit them.

### Doing the same thing through Claude Code

This route is faster once your folder is genuinely large, and it is the one that carries a
`.gitattributes` file correctly if you have one. It also has one requirement the browser route
does not: **the new repository needs to start completely empty**, no README, no `.gitignore`, no
license file ticked on during creation, because those are added by pushing your own commit into
it, and a repository that already has files from two separate starting points can produce an error
when you try to connect them.

1. If you have not already created the repository, either ask Claude Code to create one for you:
   "Create a new private GitHub repository called [name] for me, empty, no README." This needs the
   GitHub CLI already installed and signed in on your machine, covered in
   `11-github-with-claude-code.md`. Or create one yourself in the browser and leave **Add a README
   file** switched off.
2. Tell Claude Code, in plain English: "Turn this folder into that GitHub repository and push
   everything up." Point it at the folder if it is not already the one it is working in.
3. Claude Code checks whether the folder is already tracked by git, sets it up if not, saves
   everything as a first commit, connects it to the repository you created, and pushes it up. It
   will tell you when it has finished, and what it did.
4. Open the repository on github.com afterward and check the file list matches what you expected,
   the same confirmation step as the browser route.

**Why this needs an empty repository, stated plainly.** GitHub's own guidance for exactly this
situation is direct: "Create a new repository on GitHub. To avoid errors, do not initialize the
new repository with README, license, or gitignore files." If you already created one with a
README switched on, that is not a lost cause, either delete it and create an empty one instead (a
fresh repository costs you nothing at this stage), or ask Claude Code to work around it, and read
what it proposes before agreeing, the same habit `11-github-with-claude-code.md` covers for
everything else you hand it.

**GitHub's own reminder is worth repeating here, not just at the checklist above.** Its own
documentation states it directly, for this exact step: "Never git add, commit, or push sensitive
information, for example passwords or API keys, to a remote repository." That is the same warning
as the checklist section above, from GitHub's own side of the process.

### What to leave behind

Not everything in the folder needs to make the trip. Three categories worth deciding on
deliberately rather than uploading everything by default:

- **Anything caught by the secrets check above.** Do not upload it at all, in either route, until
  you have decided what to do with it, covered in that section.
- **Files that have nothing to do with the project itself**, random downloads, an old draft folder
  you meant to delete, a screenshot you took to remind yourself of something unrelated. Not a
  GitHub rule, just the same hygiene point `04-repositories-and-visibility.md` makes: a repository
  is easier to understand, for you and anyone you share it with, when everything in it is actually
  part of the project.
- **Very large files you do not need version history for**, covered in its own section next, since
  it has real mechanics behind it rather than being purely a judgement call.

### Keeping the folder structure sensible

Whatever folder structure your files already sit in on your laptop is generally fine to bring
across as-is, subfolders and all, since GitHub tracks folders the same way your computer already
does. Two things worth deciding before you upload rather than after:

**One project should mean one repository**, covered above in the assessment step. If your laptop
folder is genuinely several unrelated projects that grew together over time, split them into
separate repositories now, at move time, rather than moving the tangle across intact and sorting
it out later inside GitHub.

**A README and a `.gitignore` belong at the top level, added once, not per subfolder.** If you
followed the browser route above, you already have both from repository creation. If you followed
the Claude Code route, ask it to add both once the push is done, the same README guidance from
`04-repositories-and-visibility.md` applies: a couple of lines on what the project is, and enough
for you or whoever inherits it to remember how it works six months from now.

### Very large files

If your assessment step above turned up anything genuinely large, a video, a big exported design
file, a large data export, check it against GitHub's own stated limits before you try to bring it
across the normal way.

GitHub's own numbers: "GitHub blocks files larger than 100 MiB," a push that includes something
over 50 MiB "will receive a warning" but still goes through, and a browser upload specifically is
capped lower still, at 25 MiB per file. Beyond the hard limits, GitHub's own guidance on overall
repository size is to keep it "ideally less than 1 GB, and less than 5 GB is strongly
recommended," because a smaller repository stays fast to work with.

**For a file over 100 MiB, or a repository that is starting to feel large because of a handful of
big files, GitHub's own recommendation is Git Large File Storage (Git LFS).** Its own description
of what it does: "Git LFS handles large files by storing references to the file in the repository,
but not the actual file itself," so the repository itself stays small while still tracking the
file's changes over time. Setting it up is a short, genuinely good job to hand to Claude Code, ask
it to "Set up Git Large File Storage for the [file type] files in this project" rather than
clicking through it yourself the first time, and it is worth confirming your own account's storage
and bandwidth allowance for it on GitHub's own billing pages before you rely on it for a lot of
large files, since this page did not find a fixed free quota stated plainly enough to repeat here.

**For a large file you want to hand out rather than track changes to** (a finished export, a video
you are distributing rather than editing), GitHub's own suggestion is a GitHub Release instead of
a normal commit, covered fully in `17-releases-and-versions.md`.

**The option that is often simplest and needs nothing new learned:** if a large file rarely changes
and does not need GitHub's version history, it does not have to go into the repository at all.
Keep it in whatever cloud storage you already use, and link to it from your README instead. Not
every file benefits from being tracked; only put something through Git LFS if you genuinely expect
to update it and want the history GitHub keeps for everything else.

### Bringing across work that is already in another system

Sometimes what you are moving is not sitting in a folder on a laptop at all, it is already inside
some other online system: another Git-based host, an old company GitHub organization you are
leaving, or an older version-control system from years back.

**If it is already on another Git-based host** (GitLab, Bitbucket, an old GitHub account you are
consolidating out of), GitHub has a dedicated tool for exactly this. GitHub's own click path: the
**+** icon, top right of any github.com page, then **Import repository**. It asks for the URL of
the remote repository, credentials if the source is private, and the owner and name for the new
repository it creates on GitHub. This is a genuinely good shortcut when both sides speak git;
GitHub is doing the transfer for you rather than you downloading and re-uploading anything.

**If it is in an older system that is not Git at all**, Mercurial, Subversion, or Team Foundation
Version Control, be aware GitHub Importer no longer supports these. GitHub's own changelog states
plainly that, "effective" from 17 April 2024, it "ended support for" importing from those three
systems. If that describes what you are moving from, there is no direct import path left; get the
current, latest version of the files out of that old system in whatever way it offers (usually an
export or a checkout), and follow the ordinary folder steps earlier on this page instead, treating
it exactly like work that has been sitting on a laptop.

**Either way, the secrets and client-data check at the top of this page still applies.** An import
tool moving files for you does not look at what those files contain any more carefully than you
uploading them yourself would; it is still your job to know what is in there first.

### Telling your team where it now lives, and what changes for them

Once the files are up, the work is not quite done: whoever needs access still needs to actually be
given it, and told what changes for them.

**Give them access first.** For one or two specific people on a repository under your own personal
account, add them as a collaborator, the exact steps are in the "Access then Collaborators" part of
`04-repositories-and-visibility.md`. If you already have an organization and this is going to be
one of several repositories a real team shares on an ongoing basis, add them as an organization
member instead, covered fully in `03-members-and-access.md`. Give them the narrowest access that
lets them do the job in front of them; both of those files cover exactly what each access level
actually allows.

**Then tell them, in outcome terms, not mechanics.** They do not need to hear "the repository has
been created and you have been added as a collaborator." They need to hear something like: "The
invoicing project now lives on GitHub instead of my laptop. Here is the link. You can open it and
see everything, and once you have GitHub set up on your end, you can make changes there too instead
of me emailing you the file." Send them the repository's URL directly, and if this is their first
time on GitHub at all, point them at this kit's own starting point rather than assuming they will
find their footing alone.

**Say plainly what stops.** From this point on, the laptop folder is not where the current version
lives, the repository is. If you keep both updated by habit for a while during the handover, say so
out loud to your team so nobody is quietly working from the stale copy without realising it.

### What to do with the old copy on the laptop

GitHub does not do anything about this for you, moving files in does not remove or lock the
originals, so this is your own decision, not a setting to configure.

**Do not delete it immediately.** Keep it exactly where it is for a while after the move, as a
backup you are not actively using rather than your working copy. This costs you nothing but a
little disk space, and it is the difference between "the upload went slightly wrong and I can just
check the original" and having no fallback at all.

**Stop treating it as current the moment the upload finishes.** The trap this kit's daily workflow
guide already names is two folders that look identical with no way to tell which is newer. If you
or your team keep editing the laptop copy out of habit, you have quietly recreated the exact
problem GitHub was meant to solve. Decide, and say out loud to anyone else involved, that the
repository is now the one true copy, starting today.

**Delete it, eventually, once you trust the move.** There is no fixed timeline GitHub recommends
here, this is a business judgement, not a platform fact. A reasonable habit: once your team has
been working from the repository for a few weeks without anything going missing or looking wrong,
the laptop copy has done its job as a safety net and can go, or move to a proper backup location
if you keep backups that way regardless.

## Strategy: how to actually use this

**Move one project first, not everything you own.** `STRATEGY-PACK.md` makes this same point for
setting GitHub up from nothing, and it matters even more here, when you already have real work
sitting somewhere: pick the project you are most likely to touch again this month, move it,
confirm the whole loop works end to end, upload, access, your team actually using it, before you
repeat the process for anything else. Moving five projects in one long session and losing track of
what went where is the single most common way this goes wrong for a first-timer.

**A solo operator moving one folder in has almost no decisions left to make once the secrets check
is done.** Private repository, upload or push the whole thing, done, no organization needed,
covered in `STRATEGY-PACK.md`'s own solo example. The judgement calls in this page start mattering
once a second person is involved.

**A team of three or four bringing several projects across at once should still move them one at a
time, just faster.** Assign one project per person if it helps, but keep each project's move as its
own complete pass, secrets checked, uploaded, access given, team told, rather than everyone
uploading in parallel with nobody quite sure what has and has not landed yet.

**What good looks like a few months later:** every project that actually gets used regularly has
made the move, the laptop copies of those specific projects are gone or clearly labelled as old
backups nobody works from, and nobody on the team can remember the last time someone emailed a
file back and forth because "that's just where the current version lives." If you are still
finding secrets in a folder you meant to move six months ago, that folder has not actually been
checked yet, not moved, treat it the same as day one.

## A worked example

A physiotherapy clinic owner keeps everything for her new online booking page, a half-built
booking form, her price list, a folder of client intake templates, and (she discovers when she
looks properly) an old spreadsheet with a handful of real client phone numbers and emails from a
trial run last year, in one folder on her laptop called "Website work." She has just hired a
freelance web designer for six weeks to finish the booking page, and emailing files back and forth
with him for six weeks sounds worse than the alternative.

**She checks first.** She asks Claude Code to look through the folder for anything that looks like
a password, a key, or client information, and it flags the old client spreadsheet immediately.
She pulls that one file out of the folder entirely and keeps it where it already was, since it has
nothing to do with the booking page project and was never meant to leave her laptop in the first
place. Nothing else in the folder concerns her; the intake templates are blank, unused forms, not
actual client records.

**She creates the repository.** Private, since there is no reason for a stranger to see her price
list or an unfinished booking page. She turns on the README and picks a `.gitignore` for the type
of project her designer told her it is.

**She uploads through the browser**, since the folder is small and she wants to watch it happen the
first time. Everything is well under the size limits. She checks the file list afterward and
everything landed where she expected.

**She adds her designer as a collaborator** on that one repository, with Write access since he is
building the page, not Admin, since he has no reason to delete her repository or change its
settings. She sends him the link with one line: "The booking page project now lives here instead
of in email attachments, you'll have edit access as of today."

**She keeps the laptop folder for now**, minus the spreadsheet she already moved elsewhere, and
plans to check back in six weeks, once the engagement with her designer ends, on whether she still
needs it sitting there at all.

## If it goes wrong

**I uploaded a file and then realised it had a password or client information in it.** Do not just
delete the file in a new commit, `04-repositories-and-visibility.md` covers exactly why that does
not remove it from the repository's history. Rotate the actual password or key first, immediately,
in whatever service issued it, that is the step that genuinely closes the danger. If it was client
data rather than a credential you can rotate, that is a direct conversation with the client about
what happened, not something a GitHub setting fixes for you.

**My upload through the browser landed my files one folder level deeper than I expected.** This is
recoverable, not a disaster: delete the extra layer of folders inside the repository (or delete the
files and re-upload, dragging the folder's contents in rather than the folder itself, or the other
way around, whichever you did not try the first time) and check the result again before you commit
to it being right.

**Claude Code said it could not push because the repository already had a README or other files in
it.** This is the empty-repository requirement covered in the Claude Code section above. Either
delete that repository and create a fresh, empty one, or ask Claude Code to work around the
conflict, reading exactly what it proposes to do before you say yes.

**A file was too large to upload.** Check which limit you hit, GitHub's own numbers are 25 MiB
through the browser, 50 MiB before a warning appears through git, and 100 MiB as a hard block
either way. Under 100 MiB but over the browser's 25 MiB, switch to the Claude Code / push route
instead of the browser. Over 100 MiB, that file needs Git LFS or needs to stay out of the
repository entirely, covered in the very large files section above.

**I moved the project across and now I am not sure which copy, the laptop or GitHub, is the real
one.** Decide, today, and say so to anyone else involved. GitHub is not automatically the source of
truth just because a copy exists there, it becomes the source of truth the moment everyone agrees
to treat it that way and stops editing the old copy out of habit.

## FAQ

**Do I have to remove anything from my laptop to move it into GitHub?** No. Uploading or pushing a
copy of your files does not touch or delete the originals. What to do with the old copy afterward
is a separate decision, covered above, not something GitHub requires either way.

**Is it safe to upload client information if the repository is private?** Private means only you
and the people you explicitly give access to can see it, not the whole internet, but "private" is
not the same question as "should this specific client's information be sitting in a shared
repository at all." That is your own judgement call, covered in the checklist at the top of this
page, and it does not go away just because the visibility setting is private.

**What if I don't notice a secret was uploaded until weeks later?** The same fix applies regardless
of how long it has been sitting there: rotate it, immediately, in whatever service issued it. The
danger comes from the credential still working, not from how recently it was uploaded, so acting
now closes it exactly as effectively as acting on day one would have.

**Can I move a project in and decide later whether to make it public?** Yes. Start private,
covered in `04-repositories-and-visibility.md`'s section on changing visibility later. The one
thing worth remembering: once something has been public, even briefly, treat it as seen by
whoever might have looked, flipping back to private does not undo that.

**Do I need to know git to do any of this?** No. The browser route is entirely clicking and
dragging. The Claude Code route is a plain-English request; Claude Code runs the underlying git
commands, you do not need to know their names, the same as everywhere else this kit covers Claude
Code doing git work for you.

**What if my project already had version history somewhere else, like an old git setup on my own
computer that I never pushed anywhere?** If it is genuinely already a git repository on your
machine, just not yet connected to GitHub, the Claude Code route above still works and carries that
history across intact rather than starting fresh, since it checks whether the folder is already
tracked before doing anything. Ask Claude Code directly if you are not sure whether your folder
already has that history: "Is this folder already tracked by git?"

**Should I move everything I own into GitHub at once?** No. `STRATEGY-PACK.md` and the strategy
section above both say the same thing: move one project, confirm the whole loop actually works for
you and your team, then move the next one. Doing several at once is the most common way people lose
track of what has and has not actually landed.

## Quick reference

**Before you upload anything:**
1. Check the folder for passwords, keys, tokens, and client or customer data. Pull anything you
   find out before you continue, do not upload it "for now."
2. Decide: is this one project, or several? Split them now if needed.
3. Decide: public or private. If unsure, private.

**Browser route (small folder, first time, want to watch it happen):**
1. Create the repository (README and `.gitignore` on).
2. Add file then Upload files then drag your files or folder in.
3. Check the file list landed correctly.
4. Write a commit message, click Commit changes.

**Claude Code route (larger folder, or you have a `.gitattributes` file):**
1. Create an empty repository (no README, no license, no gitignore).
2. Ask Claude Code: "Turn this folder into that GitHub repository and push everything up."
3. Check the file list landed correctly.

**Very large files:** under 100 MiB, use the Claude Code / push route instead of the browser if it
is over 25 MiB. Over 100 MiB, use Git LFS, a GitHub Release, or keep it out of the repository
entirely.

**Already in another Git host:** use the **+** icon then **Import repository** instead of downloading
and re-uploading by hand.

**After it lands:** give your team access (collaborator or organization member), tell them plainly
what changed, keep the old laptop folder as a backup rather than deleting it right away, and agree
out loud on which copy is now the real one.

## Sources

- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- https://docs.github.com/en/migrations/importing-source-code/using-github-importer/importing-a-repository-with-github-importer
- https://github.blog/changelog/2024-04-17-updates-to-github-importer-and-the-deprecation-of-the-source-import-rest-api-endpoint/
- https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
- https://cli.github.com/manual/gh_repo_create
- https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- https://docs.github.com/en/code-security/concepts/secret-security/push-protection
