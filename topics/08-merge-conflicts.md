# Merge conflicts, and what to do when git asks you a question

A merge conflict is the moment git can't decide something on its own and stops to ask you. This file
covers what a conflict actually is, what the marker lines you'll see mean, the exact click path for
fixing a simple one in your browser (including the step people miss and get stuck without), where the
browser's help genuinely stops and how to recognise that moment yourself, what GitHub itself says to do
when the browser can't help, how to have fewer conflicts in the first place, and where to practise all
of it on a repository that holds nothing real.

Nothing in this file requires the command line. Where the honest answer is "this needs more than the
browser can do," the path this kit teaches is Claude Code, not a terminal command you type yourself.

## What a conflict actually is

Picture two people editing the same paragraph of the same document at the same time, each saving their
own version. Whoever looks at both afterwards can't just mash them together, someone has to read both
and decide what the paragraph should actually say. That's a merge conflict. It happens when git tries to
combine two branches and finds the same part of the same file changed two different ways.

GitHub's own description of when this happens: "Merge conflicts often happen when people make different
changes to the same line of the same file, or when one person edits a file and another person deletes
the same file." Most of the time git doesn't need you at all. Its own framing of the normal case: "Git
can often resolve differences between branches and merge them automatically. Usually, changes are on
different lines or in different files, so Git can merge them without help. Sometimes, competing changes
need your help."

That's the important part to hold onto: **a conflict is git asking a question, not git reporting an
error you caused.** GitHub's own reasoning for why it stops instead of guessing: "Merge conflicts block
merging because Git cannot safely choose which version of the conflicting content to keep." Two people
each did something reasonable. Git just can't tell which one you meant to keep, so it hands the decision
back to a person instead of picking wrong silently. This kit's own practice repository puts it exactly
right, in its glossary of the words you'll meet there: "It is not an error and you have not broken
anything. It is the system asking you a question it cannot answer on its own."

**In practice, for a small business:** this happens most often when two people edit the same document,
template, or page around the same time, on different branches, then both try to bring their branch back
into the main copy. Neither person did anything wrong. It's just two answers to the same question,
arriving at once.

## What the conflict markers mean, shown literally

When git can't decide, it doesn't pick a version and hide the other one. It puts both versions in the
file, wrapped in three lines that mark where the disagreement starts, where one version ends and the
other begins, and where it stops. GitHub's own instruction for dealing with them: "Delete the conflict
markers `<<<<<<<`, `=======`, `>>>>>>>` and make the changes you want in the final merge."

Here's a real one, live in this kit's own practice repository as this file is written. Two branches each
changed the same line of a file to something different: one says the cafe opens Saturday morning, the
other says it's closed. Laid out with the marker lines around them, a conflict like that looks like this:

```
<<<<<<< saturday-closed
Saturday: closed
=======
Saturday: 8am to 12pm
>>>>>>> saturday-morning
```

Everything between the top marker and the middle `=======` line is one version. Everything between
`=======` and the bottom marker is the other. The word after each outer marker is usually the name of the
branch that version came from, so you can tell which is which, read that part straight off your own
screen since it names your actual branches, not the ones shown here.

To resolve it, you delete all three marker lines and decide what the file should actually say: pick one
version, pick the other, rewrite it as something new entirely, or keep both if that's genuinely correct
("Saturday: closed over winter, 8am to 12pm the rest of the year" is a perfectly valid way to resolve
this exact conflict). GitHub's instruction is exactly that open-ended: delete the markers, "make the
changes you want in the final merge." There's no wrong answer as far as git is concerned, only a
decision only a person can make.

**Screenshot placeholder:** a pull request's conflicting file open in GitHub's editor, showing the three
marker lines with a competing line of text on each side, so a reader can match the raw text above to
what actually appears on screen.

## Resolving a simple conflict in the browser

This is the path GitHub documents for handling a conflict without leaving your browser. It works for
what GitHub calls "simple competing line change conflicts", more on that ceiling in the next section.

1. Open the pull request that has the conflict. GitHub tells you on the pull request page when one
   exists.
2. Near the bottom of the pull request, click **Resolve conflicts**.
3. For each conflicting file, GitHub shows you the marker lines described above. Delete the three marker
   lines and edit the file to what you actually want it to say, exactly as covered above.
4. If the same file has more than one conflicting section, repeat step 3 for each one.
5. Once a file is done, click **Mark as resolved**.
6. If more than one file conflicts, GitHub lists them on the left under "conflicting files". Click the
   next one and repeat steps 3 to 5.
7. **This is the step people miss and get stuck on.** Marking every file as resolved is not the last
   step. Once every file shows as resolved, click **Commit merge**. Nothing is actually saved into your
   branch until you click this. GitHub's own wording for what it does: "After you've resolved all your
   merge conflicts, click **Commit merge**. This merges the entire base branch into your head branch." If
   you close the tab after marking files resolved but before this click, you have not finished, and
   whatever you typed in the editor may not be there when you come back. Do this step in one sitting.
8. Finish the pull request the normal way: click **Merge pull request**. Resolving the conflict doesn't
   merge the pull request by itself, it just clears the thing that was stopping the merge.

One warning worth knowing before you start, in GitHub's own words: "Resolving conflicts on GitHub merges
the entire base branch into the head branch. If the head branch is the default or protected branch, you
may be prompted to create a new head branch." For almost everything this kit's audience does, the head
branch is a regular working branch, not the default one, so this won't come up. If GitHub does ask you to
create a new branch partway through, that's it protecting your default branch, not something you did
wrong, follow the prompt.

You might also see a button offering to fix the conflict automatically with Copilot. That only appears
if your repository has that specific feature turned on, and it's a separate Copilot feature this file
doesn't cover. The steps above are the path that works on every repository, with or without it.

**Screenshot placeholder:** the **Resolve conflicts** button near the bottom of a pull request page, and
separately, the **Commit merge** button that appears once every conflicting file is marked resolved, so
a reader can see both are genuinely two different clicks, not one.

## The line the browser resolver doesn't cross

GitHub is direct about the limit of this tool. Its own wording: "You can resolve simple competing line
change conflicts on GitHub. For other conflicts, use the command line." Its overview of resolving
conflicts in general puts the same line differently: "Simple line conflicts can often be resolved on
GitHub," while "more complex conflicts must be resolved in a local clone and pushed back to the pull
request branch."

GitHub doesn't publish an exact list of what counts as "simple" versus "complex", there's no rulebook
that says "under five lines is fine, over five isn't." So rather than a checklist to compare your
conflict against, here's how to recognise for yourself that you've gone past what the browser can help
with, and the moment to stop:

- **The `Resolve conflicts` button isn't there, or it's there but greyed out and won't click.** That's
  GitHub telling you directly, don't try to force it.
- **You open the editor and what's on screen doesn't look like something you'd normally read or write.**
  Plain sentences in a document you understand are fine to resolve yourself, whichever version you pick.
  Code, configuration, or anything with brackets, symbols, or syntax you don't recognise is a different
  situation, stop there even if the button is technically clickable.
- **There are conflict markers scattered through a big chunk of the file, not one clear block.** A tidy
  swap of one line for another is what this tool is built for. A file that's marked up in several
  separate places, especially if changing one spot seems to depend on what you decide in another, is past
  it.

One thing that is **not** a reason to stop: not being sure which version is correct. That's a
business decision, not a technical one, pick the one you actually want, ask whoever wrote the other
version if you're unsure, or combine them. The stopping point is about whether you understand what
you're looking at and can safely edit it, not about which answer is right.

## When "Resolve conflicts" isn't there for you to click

Two different situations look the same on screen, an absent or disabled button, so it's worth telling
them apart.

**If the conflict itself is too complex for the browser**, GitHub's own guidance is direct: "If Resolve
conflicts is deactivated, resolve the conflict using another Git client or the command line," and
separately, "more complex conflicts must be resolved in a local clone and pushed back to the pull request
branch." This kit doesn't teach the command line to its members. Instead, this is exactly the situation
Claude Code is for: it already has git available, so it can act as that "another Git client" for you
without you typing a single git command yourself. Tell it plainly what's going on, something like:

```
I've got a merge conflict in <file name> on pull request <link or number>. Can you get a local copy,
show me what's actually different between the two versions, and help me decide what it should say?
Once I tell you, push the result back up.
```

Claude Code pulls both versions down, shows you the same two competing pieces of content the marker
lines represent, but in plain language, asks what you want to keep, then commits and pushes the result
back to the pull request branch for you. You're making the same decision either way, in the browser
you're just doing it with your own two hands and the raw marker text.

If you'd rather have a person look at it, especially the first few times, that's a completely reasonable
call too. Ask whoever's technical on your team, or bring it to the community and say plainly what the
screen showed.

**If the button is missing because you don't have the access to finish the job, not because the
conflict is complex,** that's a different fix entirely. Completing a pull request on GitHub, including
resolving its conflicts and merging it, needs Write access to that repository or higher. GitHub's own
permissions table confirms this for "Merge a pull request": only the Write, Maintain, and Admin roles
have it, Read and Triage don't. If you're only able to read a repository someone else owns, you'll be
able to look at a conflict but not finish resolving it there. If that pull request is genuinely meant to
be yours to complete, that's a conversation about your access level, covered in this kit's members and
access file, not something to work around.

## Avoiding conflicts in the first place

None of this is about eliminating conflicts entirely, sometimes two people genuinely do need to decide
the same thing differently, and that's fine. But a few habits mean you hit conflicts less often, and the
ones you do hit stay small and simple.

**Keep each branch to one thing.** GitHub's own guidance on this: "Make a separate branch for each set
of unrelated changes," and within a branch, "each commit contains an isolated, complete change." A
branch that only touches the one page, template, or document it's meant to change stays small, and a
small branch overlaps with far less of what everyone else is doing than a branch that's grown to cover
several unrelated jobs at once.

**Land your branch quickly, rather than letting it sit open.** This is this kit's own practical advice,
not a rule GitHub states, but it follows directly from how conflicts happen. The longer a branch stays
open and unmerged, the further the main copy drifts from where your branch started, and the more likely
it is that someone else has since touched the same lines you're touching. A branch opened and merged the
same day rarely conflicts with anything. One left open for weeks, on a file other people keep changing,
is where conflicts pile up.

**Keep your branch up to date with main while you're still working on it**, rather than only finding out
about a conflict right when you try to merge. GitHub's own reasoning for this: "Before merging, update
your pull request branch with changes from the base branch to catch conflicts or test failures early."
This kit's branches file covers the exact click path for this, the **Update branch** button on a pull
request, in full, this file won't repeat the mechanics. The point here is why it's worth doing before
you're forced to: a conflict caught early, while it's still one or two lines, is the simple kind this
file's browser steps handle easily. One that's built up silently for weeks, across many changes on both
sides, is far more likely to be the kind that needs more than the browser.

**If you know someone else is about to work on the same file or the same part of it, say so out loud
before either of you starts.** Not a GitHub feature, just the plainest way to avoid a conflict rather
than having to resolve one afterwards.

## Practising this safely

This kit has a practice repository built for exactly this, so the first conflict you ever deal with
doesn't have to be a real one. It's public, holds nothing that matters to any real business, and lives
at `https://github.com/selrai-company/github-training-content`.

Inside it, the [practice folder](https://github.com/selrai-company/github-training-content/tree/main/practice)
walks you through four things to try, in order, on your own fork (your own personal copy of the
repository, which this kit's branches file touches on and its forks file covers in full). The fourth one
is a conflict you build yourself, on purpose: change one line of a practice file to one thing on one
branch, change the exact same line to something else on a second branch, then open a pull request between
them. Both branches will have changed the same line two different ways, so GitHub will tell you there's a
conflict, and you resolve it using the exact steps in this file, on a fork where you have everything you
need to actually click every button, including **Commit merge**.

**If you'd rather look at a conflict before making one, there's a real one sitting there permanently.**
Pull request 1 on that same repository is two branches genuinely disagreeing about the same line, on
purpose. The practice folder's own description of it: "It is two branches disagreeing about the Saturday
line, left open on purpose so there is always an example to look at. It is not waiting on anyone and it
is not going to be fixed." Open it, read the conflicting file, and match what you see against what this
file describes above before you build your own.

One thing worth knowing before you go looking at that pull request: you won't be able to click **Resolve
conflicts** on it yourself, even if it's visible. It belongs to this kit, not to you, and finishing a
pull request needs Write access or higher, covered above. That pull request is there to look at, not to
fix. Actually resolving one, safely, with every button available to you, is exactly what the fourth step
in the practice folder is for.

---

## If it goes wrong

**I marked every file as resolved but the pull request still won't let me merge.** You've almost
certainly missed the **Commit merge** click covered above, marking files resolved and committing the
merge are two separate steps. Open the pull request again and check whether "conflicting files" still
lists anything, and whether you see a **Commit merge** button waiting for you.

**There's no `Resolve conflicts` button on a pull request I need to fix.** Work out which situation
you're in first: if it's your own branch and you genuinely have Write access to that repository, the
conflict is likely past what the browser handles, see the recognition signs above and hand it to Claude
Code or a technical teammate. If it's someone else's repository and you only have Read access, that's an
access problem, not a conflict problem, see this kit's members and access file.

**I resolved a conflict and merged it, but my own copy (or a teammate's) still looks wrong.** Resolving
and merging changes the copy on GitHub. Nobody's local copy updates on its own. Everyone who has their
own copy, including you, needs to pull the latest main again, covered in this kit's daily workflow file.

## Questions people ask here

**Did I do something wrong to cause this?** No. A conflict means two people made two reasonable changes
to the same spot, not that either change was a mistake. See the framing at the top of this file.

**Can I lose work by resolving a conflict wrong?** Not by clicking the wrong thing. Nothing changes on
either original branch until you click **Commit merge**, and even then, both branches' original commits
are still there in the repository's history, resolving a conflict doesn't erase anyone's earlier work.
What you can lose is unsaved typing in the browser editor if you navigate away before clicking Commit
merge, which is exactly why that step matters, covered above.

**What if I genuinely want to keep both versions, not just pick one?** That's allowed. Delete the three
marker lines and write the file however you actually want it to read, including both pieces of content
if that's the correct answer. GitHub's own instruction is exactly that open, "make the changes you want
in the final merge," it doesn't have to be a straight choice between the two.

**Is this the same thing as the "Update branch" button covered in the branches file?** Related, not
identical. Updating your branch is how you catch a conflict early, before you're forced to deal with it.
This file is what to do once a conflict has actually shown up, whether you found it through Update
branch or by trying to merge a pull request outright. If updating your branch itself hits a conflict,
the steps in this file are exactly what resolves it.

**Does anything merge automatically while a conflict exists?** No. GitHub's own reasoning for stopping
rather than guessing: "Merge conflicts block merging because Git cannot safely choose which version of
the conflicting content to keep." Nothing merges, on purpose, until a person resolves it.

---

## Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
- https://docs.github.com/en/get-started/using-github/github-flow
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization
