# Gaps: what to check on your own screen before you record

Every file in this kit is built from GitHub's own published documentation, with every source
recorded at the bottom of the file. But GitHub does not publish everything. Sometimes a page
describes the general rule and leaves the exact button wording unstated. Sometimes a screen has
no documentation page at all, and the only way to know what is on it is to look.

This page collects every one of those moments in one place. Nothing here is wrong. Each line is
a place where the honest answer was "confirm this on your own screen" instead of a quoted fact,
and each topic file already says so at the point it comes up. This page exists so you do not
have to hunt through seventeen files to find them all before you sit down to film, teach, or
answer a question live.

If you confirm one of these on your own screen and it now matches what's written here, that's
good news, it just means GitHub hasn't moved that particular piece yet. If it doesn't match,
trust your own screen over this kit, every time, and say so out loud if you're teaching someone
else in the moment.

## 01-accounts-and-security.md

- **Which countries currently support SMS two-factor.** Australia was on GitHub's list at the
  time this was written, but GitHub calls this a maintained list that changes. Check it
  yourself, on GitHub's own SMS-countries page, at the moment you or a member sets this up.
- **GitHub's current password requirements at sign-up.** Not repeated in this kit because it
  can change; read it straight off the sign-up screen.

## 02-organizations.md

- **The exact fields on the "New organization" creation screen.** GitHub's own walkthrough
  says "follow the prompts" without listing them. Confirm what your screen actually asks for.
- **Any naming rules or the exact error message for a taken organisation name.** Not published
  on the page that covers creation. Read it off the screen if the name you want is rejected.
- **Who is allowed to see and click "Delete this organization."** This kit treats it as an
  owner-only action in practice, but GitHub's own page for that specific step doesn't spell out
  the permission requirement. Confirm before relying on it as a safeguard.
- **What happens to a member's paid seat when you remove them.** A billing-settings detail,
  confirm on your organisation's own billing page.

## 03-members-and-access.md

- **The exact wording and layout of the organisation invite email.** Confirm what it looks
  like the first time you send one, so you recognise it and don't mistake it for spam.
- **The exact layout of the "Outside collaborators" view on the People tab.** GitHub's written
  docs don't describe the visual layout in detail.
- **What happens to a member's paid seat when you remove them.** Same gap as above, confirm on
  your billing settings page.

## 04-repositories-and-visibility.md

- **Which option (public or private) is pre-selected on the repository creation form.**
  GitHub's own documentation does not state a default anywhere this kit could find. Do not
  click through this step on autopilot; read your own screen and choose deliberately every
  time.
- **Whether a private repository is ever visible to any human being under any circumstance
  beyond GitHub's stated access rules.** This kit can confirm GitHub's own access-boundary
  wording (you, people you've explicitly shared with, and certain organisation members), but a
  broader question about GitHub's own trust and support practices wasn't confirmed one way or
  the other, so it isn't asserted either way.

## 05-daily-workflow.md

No unconfirmed items on this file specifically; it defers to the gaps already listed for
repository creation and the GitHub CLI setup covered under `11-github-with-claude-code.md`
below.

## 06-branches.md

- **How long the "Restore branch" button stays available after a pull request closes.** GitHub
  confirms the button exists but not how long it lasts. Don't sit on it if you change your
  mind about a deleted branch.

## 07-pull-requests.md

- **The exact label of the "start a new pull request" button when the yellow banner isn't
  showing.** Confirm the wording on your own screen.
- **The exact click to edit a pull request's title or description after it's created.** The
  option is real; the precise control wasn't pinned down word for word.
- **The exact click to change a pull request's base branch.** Same as above, the option is
  real, confirm the exact wording when you get there.
- **Whether a documented "reopen" button exists for a closed pull request.** Not confirmed from
  GitHub's own pages. Look near the bottom of the closed pull request before assuming there
  isn't one.
- **Whether GitHub notifies someone when you've reviewed their pull request.** Depends on their
  own notification settings; not part of what this kit checked.
- **Which merge methods (merge commit, squash, rebase) are ticked on a brand-new repository by
  default.** Confirm on your own screen rather than assuming; this kit did not confirm the
  out-of-the-box default.

## 08-merge-conflicts.md

- **Where exactly "simple" stops and "complex" begins for the browser's conflict resolver.**
  GitHub does not publish a rulebook (no line count, no fixed cutoff). This kit gives you signs
  to recognise it yourself (an unclickable button, unfamiliar syntax, markers scattered across
  a file) rather than a hard number, because GitHub itself doesn't give a hard number either.

## 09-forks-and-contributing.md

- **Whether a private repository owned by a personal account (not an organisation) has its own
  "allow forking" toggle.** GitHub's documentation spells this out for organisation-owned
  private repositories in detail, but not for a personal account's private repository. Have
  the repository's owner check their own Settings → Features section directly.
- **Whether forking uses up a seat or costs anything on a paid plan.** Not stated either way in
  what this kit found. Confirm on your own account's billing or usage page.
- **Whether deleting a fork automatically closes any pull requests opened from it.** Not
  confirmed. Close or merge an open pull request from a fork before deleting that fork, rather
  than assuming it's handled for you.

## 10-protecting-your-work.md

- **The exact current wording of the "include default branch" option when targeting a
  ruleset.** This kit found it worded close to "Include default branch" at the time of
  writing; if your screen differs, pick whichever option clearly names your default branch.
- **The exact sidebar wording and location for your own personal account's push-protection
  setting on public repositories.** Confirmed that the setting exists and is on by default;
  the precise menu wording wasn't pinned down.

## 11-github-with-claude-code.md

No unconfirmed GitHub facts beyond what's already listed for the files it cross-references
(repository creation, pull requests, forks). Its claims about Claude Code itself are sourced
directly from Anthropic's own documentation, quoted in the file.

## 12-when-things-go-wrong.md

- **What actually happens after you submit GitHub's "I cannot sign in" support form.** GitHub
  doesn't publish its internal handling of that form. Confirm on your own screen what it asks
  for once you're there.

## 13-issues-and-tracking-work.md

- **The exact field name for a milestone's due date on the creation screen**, as opposed to
  only appearing once you go back in to edit the milestone. Confirm on your own screen which
  screen actually offers it.
- **Whether a documented "reopen" button exists for a closed issue.** Same gap pattern as
  closed pull requests above; not confirmed, look near the bottom of the page before assuming.
- **Whether there's a documented, direct way to convert an issue into a pull request, or the
  reverse.** Not confirmed. Treat them as two separate, related things instead.
- **Whether Issues carries any plan-based feature restriction.** No restriction found in what
  this kit checked, but confirm on GitHub's own pricing page if you want certainty.
- **Whether a deleted issue's number gets reused for the next new issue.** Not confirmed either
  way.

## 14-markdown-and-writing.md

- **Whether Markdown formatting works inside a commit message itself**, as opposed to comments,
  issues, pull requests, and `.md` files, where it definitely does. Not confirmed either way.
  Keep commit messages as plain, short sentences regardless.

## 15-finding-things.md

- **The exact click path to a file's "History" link.** Confirmed by this kit opening a real
  file directly during research, not from GitHub's written documentation text describing that
  specific control by name. Look near the commit info just above a file's content if it's not
  exactly where described.
- **Whether the collapsible file-tree panel on the left of a repository page appears
  identically on every repository.** Confirmed by hands-on look during research, not named
  specifically in GitHub's own documentation. Treat it as something to look for, not something
  guaranteed.
- **Whether general search (not code search specifically) ever shows results from a repository
  you don't have access to.** Confirmed for code search directly from GitHub's own wording.
  For general search, this kit reasoned by extension rather than finding a direct statement; if
  you want certainty, test it yourself against a private repository you're not a member of.
- **Whether you can search inside the text of an uploaded Word document, PDF, or image.** Not
  confirmed. Rely on filename search as the safer bet for anything that isn't plain text or
  code.

## 16-notifications.md

- **The exact current wording of the Watch dropdown's options** (Watching everything, Not
  watching, Custom, Ignore). GitHub reworks its own interface text over time; confirm the exact
  labels on your own screen.
- **Whether GitHub offers notification delivery by text message or any app besides email and
  the website**, beyond the separate GitHub Mobile app. Not confirmed either way in what this
  kit checked.

## 17-releases-and-versions.md

- **Whether a deleted release can be restored.** Not confirmed from GitHub's own pages. Treat
  deleting a release as final, and leave one published if you're not certain you're done with
  it.
- **Whether "release immutability" is switched on for a specific repository.** This is a
  repository setting an administrator can check directly; not something to assume either way.

## STRATEGY-PACK.md

- **What the price becomes for GitHub Team or GitHub Enterprise Cloud after the first twelve
  months.** GitHub's own pricing page states both figures as introductory rates for the first
  year and does not publish the renewal price anywhere this kit could find. Confirm the current
  renewal price on GitHub's own pricing page before committing to a paid plan on the strength
  of the year-one number.

## FAQ-PACK.md

- **The exact renewal or downgrade mechanics if an organisation's paid plan lapses without the
  account being cancelled outright.** Not confirmed. Check the organisation's own billing
  settings page.
- **The exact seat-release behaviour when a member is removed from a paid organisation.** Same
  gap as listed under `02-organizations.md` and `03-members-and-access.md` above, restated
  here because it's asked directly as an FAQ.
- **How a specific community currently delivers "this week's build."** This varies by
  community and isn't a single fixed GitHub answer. Check the most recent pinned instructions
  in your own community rather than assuming a fixed mechanism.

## 20-licences-and-ownership.md

- **Which of GitHub's two Terms of Service, standard or Corporate, actually covers a given paid
  organization account**, and specifically whether its content-licence grant to GitHub includes AI
  training. This file quotes both versions accurately but could not confirm a rule for which one
  applies to a specific account from GitHub's own published pages alone. Confirm directly with
  GitHub, or whoever set up the organization's billing, rather than assuming.
- **Whether removing or replacing a repository's `LICENSE` file cancels permission already granted
  to someone who copied the work under the old licence.** This file states the general shape (it
  does not cancel it) as reasoned from how licences generally work, not as a fact found stated word
  for word on GitHub's own pages for this exact scenario. Confirm with a lawyer if real stakes ride
  on a specific case.
- **Whether GitHub itself ever polices or enforces a broken licence condition between two users.**
  This file infers "no" from GitHub's own disclaimer that it displays licence information and is
  "not lawyers", not from a direct statement that GitHub never intervenes. Treat licence enforcement
  as a matter between the parties, and a lawyer, rather than a GitHub support matter, unless you
  confirm otherwise.

## One structural item worth checking before you rely on this kit as written

`SKILL.md`, in this same folder, routes every question to a file path written as
`topics/<filename>.md` (for example `topics/01-accounts-and-security.md`), and separately
points unknown-word questions at `topics/GLOSSARY.md`. As this kit currently sits on disk, the
numbered topic files live directly in this folder, not inside a `topics` subfolder, and no
`GLOSSARY.md` file exists anywhere in this kit yet. If `SKILL.md` is used to route lookups as
written, every one of those file paths will fail to resolve. This is worth fixing (or the
routing table worth correcting to match where the files actually live) before `SKILL.md` is
relied on to answer a live question, rather than something to route around case by case.

## CODEOWNERS, checked and still unverified, 2026-08-18

The glossary defines CODEOWNERS but hedges on two specifics: the exact filename and which folders
GitHub searches for it. That hedge was checked rather than left assumed.

GitHub's documented page for it, at the path the kit expected, returned **HTTP 404 Not Found** on
2026-08-18. The page has been moved or retired, so the specifics could not be confirmed from GitHub's
own documentation.

What this means in practice:
- The glossary's CODEOWNERS entry stays hedged. Do not tighten it into a stated rule.
- Anyone recording or teaching this must read the current GitHub page on screen and quote what it says.
- Two topic files reference CODEOWNERS in passing. Neither states a filename or folder rule, so neither
  is wrong. They just rely on the glossary, which is now honest about its limit.

This is recorded as a dead documentation URL rather than as a fact, because "we looked and the page was
gone" is a different thing from "we did not look".
