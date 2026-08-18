# The GitHub Strategy Pack

The other files in this kit teach you which button to click. This one teaches you what to decide.

Buttons are the same for everyone. Decisions are not. Whether you need an organization, how many
people should approve a change before it goes live, what to name your repositories, when a
contractor should get full access and when they should not: none of that has one right answer.
It depends on how many people are involved, what happens if something breaks, and how much
friction you are willing to put up with to prevent that.

This document is where you work that out. Read it once when you are setting up, and come back to
it every time your team changes size, because the right answer changes with it.

**A word you will see a lot below, defined once:** a repository is the project folder GitHub
tracks for you, the one that remembers every change ever made to it. If that word is new to you,
read `04-repositories-and-visibility.md` first. This document assumes you already know the basic
words this kit teaches (account, organization, repository, branch, commit) and builds judgement on
top of them. It does not re-teach the click paths.

## What is in this document

- [What order do I do things in?](#what-order-do-i-do-things-in)
- [Do I even need an organization?](#do-i-even-need-an-organization)
- [How does the work change at 2, 3, and 5+ people?](#how-does-the-work-change-at-2-3-and-5-people)
- [How much process is the right amount?](#how-much-process-is-the-right-amount)
- [What should I standardise?](#what-should-i-standardise)
- [What does good look like at one month, three months, a year?](#what-does-good-look-like-at-one-month-three-months-a-year)
- [The expensive mistakes, and how to avoid them by design](#the-expensive-mistakes-and-how-to-avoid-them-by-design)
- [When to stop and get help](#when-to-stop-and-get-help)
- [Three real setups, followed through end to end](#three-real-setups-followed-through-end-to-end)

---

## What order do I do things in?

The order depends on whether you are starting fresh or already have work scattered across a
laptop.

### Starting from nothing

1. **Create your account and lock it down.** Two-factor authentication, recovery codes saved
   somewhere that is not your phone. This is not optional and it takes about fifteen minutes.
   Covered in `01-accounts-and-security.md`.
2. **Decide if you need an organization yet.** Most people starting from nothing do not. See the
   next section. If you are genuinely solo with no second person on the horizon, skip straight to
   step 4.
3. **If you do need one, create the organization and add a second owner the same day**, not
   "eventually." This is the single most skipped step in this whole kit, and it is the one with
   the worst downside if you skip it. Covered in `02-organizations.md`.
4. **Create your first repository**, with a README and a `.gitignore` file, before you put a
   single real file in it. Covered in `04-repositories-and-visibility.md`.
5. **Add anyone else who needs access**, at the narrowest level that lets them do this week's job.
   Covered in `03-members-and-access.md`.
6. **Start working.** Solo, that means committing directly. With more than one person touching the
   same repository, that means branches and, once you are ready for it, pull requests.

### Work is already scattered across a laptop

If you already have files, folders, maybe a half-finished project, sitting on your own computer
with no GitHub involved yet, the order is different because you are retrofitting structure onto
something that already exists.

1. **Secure the account first**, same as above. This does not change regardless of what state your
   files are in.
2. **Pick one project to move first.** Not everything at once. Choose the project you are most
   likely to touch again this month.
3. **Create one repository for it**, and get that single project's files into GitHub before you
   think about organizations, teams, or anyone else. You are proving the workflow to yourself on
   one thing before you scale it.
4. **Only once that one project is comfortably living on GitHub, decide about an organization**,
   using the trigger in the next section. Do not create an organization "to be ready." Create it
   the day you actually need it.
5. **Move your other projects across one at a time**, each into its own repository, not all
   dumped into one. See "what to standardise" below for why one project should mean one
   repository.

The common mistake in this path is doing steps 2 through 5 for every project at once, in one long
session, and losing track of what moved where. Do one project, confirm it works, then move the
next.

---

## Do I even need an organization?

**Direct answer: probably not yet.**

A personal GitHub account already does everything a solo operator needs. Repositories, history,
everything else in this kit. An organization is a separate, shared account that sits above your
personal one, built specifically so more than one person can hold access to the same work over
time, even as who that person is changes (`02-organizations.md`).

**The one trigger that actually means you need one:** a second person needs push access to your
repositories on an ongoing basis, and you want that access to keep working even on a day you are
not around to grant it yourself. That is it. Not "it looks more professional." Not "I have a
registered business name." Specifically: recurring shared access to code, for more than one
person.

**What it costs you if you create one anyway, before you need it:**

- One more account that has to be kept secure, with nothing using it yet.
- A decision you now owe yourself: who is the second owner? An organization with only one owner is
  a real risk, not a theoretical one. GitHub's own guidance is that the owner role "should be
  limited, but to no less than two people," and separately warns that "if an organization only has
  one owner, the organization's projects can become inaccessible if the owner is unreachable"
  (`02-organizations.md:70-72`). If you create an organization for a future team that does not
  exist yet, you are the only owner in the meantime, sitting on that risk for nothing.

**What changes my mind:** the moment you actually bring someone else onto your code, on an
ongoing basis. Not a one-off contractor doing one job on one repository, that is a narrower case
covered below under outside collaborators. A real second person, joining the work.

If you are not sure yet, wait. Creating an organization later, once the need is real, costs you
nothing you have not already spent. Creating one early costs you a second-owner decision you were
not ready to make, sitting unresolved.

---

## How does the work change at 2, 3, and 5+ people?

Team size is the single biggest lever on how much structure is worth having. Below is what
actually changes at each size, grounded in what this kit's other files establish.

| Team size | Organization? | Base permission | Who gets what access | Review habit |
|---|---|---|---|---|
| Solo | No | Not applicable | Just you | None needed |
| 2 people | Yes, once the second person's access is ongoing | Read or No permission (`03-members-and-access.md:46-56`) | Both of you as owners is often reasonable at this size (see the second-owner rule above) | Optional; a quick look at each other's work before it goes live is enough |
| 3 people, one technical | Yes | Read or No permission | The technical person gets Write on the repositories they build; non-technical members get Read, or Write only on the specific things they edit (see standardising, below) | Informal: the technical person glances at anything customer-facing before it lands |
| 5 or more | Yes | Read or No permission, strictly | Use teams to group people by what they actually do, rather than granting access person by person (`03-members-and-access.md:108-124`) | Worth considering an enforced rule, not just a habit; see the process ladder below |

**Why base permission matters at every size above solo:** the base permission is the org-wide
default access every member gets to every repository, current and future. GitHub's own
documentation is direct that setting it to Write "so everyone can push without me having to add
each person to each repo" hands every current and future member push access to everything, with
no per-repository decision involved (`03-members-and-access.md:44-56`). This is the single most
common structural mistake in this entire document. It costs nothing to avoid: leave the default
low, grant Write per repository to the people who actually need it there.

**Why teams start earning their keep at five or more:** below that size, granting access person by
person is barely more work than setting up a team. Once you have distinct groups doing genuinely
different things (a design side and a build side, for instance), a team lets you grant access once
to the group and have it apply automatically to everyone in it, including people who join the team
later. GitHub's own description: teams give you "cascading access permissions," and nested teams
inherit their parent's access automatically (`03-members-and-access.md:108-118`). Below five
people, this is a solution looking for a problem; above it, it starts saving real time.

**Recurring, non-team access:** if someone is not becoming a real part of your team, just doing one
job on one repository, do not add them as a full organization member at all. Add them as an
outside collaborator instead, scoped to that one repository. This is covered in its own scenario
below, and in full in `03-members-and-access.md:83-106`.

---

## How much process is the right amount?

Every protection you add costs friction. The question is never "should we have protection," it is
"does what this specific protection buys outweigh what it costs us, at our current size." Here is
the ladder, in order, with the honest cost of each rung.

| Level | What it is | What it costs | What it buys | Add it when |
|---|---|---|---|---|
| **0. Nothing** | Direct commits, no organization, one person | Nothing | Nothing needed, because there is no one else to protect against | You are solo |
| **1. An organization with narrow default access** | Base permission at Read or No permission, access granted per repository | A little setup time; a second-owner decision you have to actually make | Access that survives people joining and leaving, without one setting quietly giving everyone push access to everything | A second person needs ongoing access |
| **2. Branches plus an informal review habit** | Changes happen on a branch first; someone glances at it before it lands, but nothing stops it if they do not | Some waiting; some coordination between people | A second pair of eyes catches mistakes before they become everyone's problem, without needing anyone's permission to skip it in a genuine hurry | More than one person touches the same repository regularly, especially anything a customer or client sees |
| **3. Enforced review, required by GitHub itself** | GitHub blocks a change from landing until someone else has actually approved it, on a private repository this needs GitHub Team, currently listed at $4 USD per user per month for the first twelve months (`02-organizations.md:34,38`; confirm the renewal price yourself on GitHub's own pricing page before committing, since what it becomes after year one is not stated there) | A real subscription cost in USD, plus real waiting time if a reviewer is slow or unavailable, and it cannot be skipped even when you genuinely need to | Nobody can skip the review by accident, on purpose, or in a rush; a permanent record of who approved what | Mistakes have started actually costing you money or reputation, or a client or compliance requirement demands proof that changes are reviewed |

**The trap to avoid in both directions.** Jumping straight to level 3 for a two-person shop buys
you almost nothing over level 2, because at that size the informal habit and the enforced rule
produce the same outcome nearly every time, and you are paying a subscription and absorbing real
delay for the difference. The opposite trap is staying at level 1 forever once mistakes are
genuinely expensive: an informal habit only works while everyone remembers to follow it, and the
first time someone is in a hurry, it will not stop them.

**How to tell you picked right:** if you are at level 2 or 3 and reviews are consistently a
rubber stamp nobody reads, you have over-invested; drop back a level. If you are at level 1 or 2
and a mistake has landed in something a customer saw because nobody happened to look at it first,
that is the signal to move up a level, not a one-off bad luck event to shrug off.

---

## What should I standardise?

Standardising a few habits early keeps a repository navigable a year from now, without needing a
rulebook.

**One project, one repository.** Do not put every project you own into a single giant repository,
and do not create a new repository for every small file. A repository should map to one thing you
would describe in a sentence: "the booking website," "the invoicing project," "the internal price
list." If you cannot say what one repository is for in a sentence, it is probably doing the job of
two.

**Repository names:** short, memorable, and describing what the thing is, not who asked for it or
when. `booking-site` beats `client-project-3` a year later, when you have forgotten which client
that was.

**Branch names:** GitHub's own guidance is that "a short, descriptive branch name enables your
collaborators to see ongoing work at a glance" (`06-branches.md:111-113`). Name it after what it
does, in a few words, hyphens instead of spaces: `update-menu-prices`, not `test` or your own name.
Ten branches all named after people tell nobody, including you in six months, what any of them
were actually for.

**Every repository gets a README and a `.gitignore` before the first real file goes in, not
after.** The README should say what the project is, and give you (or whoever inherits it) enough
to remember how it works six months from now, not a full manual (`04-repositories-and-visibility.md:148-152`).
The `.gitignore` should, at minimum, block `.env` files and anything else that holds a password or
a key, from the very first commit. This one habit is the difference between a secret that was
never a risk and a secret you have to rotate later. It only works before the first commit, not
after (`04-repositories-and-visibility.md:186-208`).

**What does not belong in a repository:** passwords, API keys, tokens, and anything that has
nothing to do with the project itself. If it should not be typed into a shared document, it should
not be typed into a file that gets committed either.

**Default new access to the least you can get away with, every time.** Start every new person at
the lowest role and the narrowest repository access that lets them do this week's job, not the
access you imagine they might need in six months. Widening someone's access later takes thirty
seconds. Discovering a year later that everyone has had push access to everything the entire time
is a much longer conversation (`03-members-and-access.md:120-124`).

---

## What does good look like at one month, three months, a year?

These are things you can check are actually true, not vibes.

**One month:**

- Two-factor authentication is on for every account that is active, with recovery codes saved
  somewhere that is not the same phone that generates the codes.
- If you created an organization, it has at least two owners. If it only has one, that is the
  first thing to fix, before anything else on this list.
- Every repository you actually use has a README and a `.gitignore` in it.
- Everyone on the team can tell you, in their own words, what a branch is for, even if nobody has
  used one yet.

**Three months:**

- At least one real change has gone through a branch, been looked at by someone else, and landed,
  for every person who regularly touches code or content.
- Nobody has made a repository public "so someone could see it." That should be a count of zero,
  permanently. If it has happened, it has been fixed and the reason discussed once, not repeated.
- The base permission on your organization is still at Read or No permission. If someone changed
  it to Write "temporarily" and it never got changed back, that is worth catching now.

**One year:**

- Offboarding has actually happened at least once, someone left or a contractor's engagement
  ended, access was pulled, and nothing broke because of it.
- You can name your organization's second owner without checking. If you cannot, that is the
  single most avoidable failure this whole document warns about, and it is worth fixing today, not
  after you finish reading.
- If a secret was ever accidentally committed, it happened once, was caught fast, was rotated
  immediately, and became a permanent `.gitignore` rule afterward, not a recurring incident.

---

## The expensive mistakes, and how to avoid them by design

Being careful does not scale, especially once more than one person is involved. These are the
mistakes worth preventing with a setting or a habit, not with vigilance.

| Mistake | Why it is expensive | Structural fix |
|---|---|---|
| Base permission set to Write "to save time" | Every current and future member gets push access to every current and future repository, silently (`03-members-and-access.md:46-56`) | Leave it at Read or No permission by default. Grant Write per repository, to the people who need it there. |
| A secret committed into a file | Once it is committed, it sits in every earlier version of that file, deleting the file later does not remove it from history (`04-repositories-and-visibility.md:192-208`) | Block `.env` and similar patterns in `.gitignore` before your very first commit, not after. |
| An organization with only one owner | If that one owner loses access for any reason, there is no documented way for anyone else to recover it (`02-organizations.md:70-72`) | Add a second owner the same day you create the organization. |
| Making a repository public "so someone can see it" | Public means every stranger on the internet, not "anyone with the link" (`04-repositories-and-visibility.md:59-70`) | Use a collaborator, or organization access, to share with the specific people who need to see it. |
| Recovery codes not saved anywhere | GitHub's own wording is direct: support "will not be able to restore access" if you lose both your two-factor device and your recovery codes (`01-accounts-and-security.md:134-140`) | Download the codes the day you turn on two-factor authentication, into a password manager, not a screenshot on the same phone. |
| Assuming removing someone deletes what they already copied | Removal stops future access. It does not reach onto their laptop (`03-members-and-access.md:134-138`) | If what they saw was sensitive, that is a direct conversation with the person, not something a GitHub setting handles for you. |

---

## When to stop and get help

Most of what this kit covers, a non-technical owner can do alone, in a browser, with Claude Code
alongside them for anything that needs a terminal. A few situations are genuinely not solo jobs.

**A real secret has already been committed, and you want it gone from the history, not just the
current version.** Rotate it yourself, immediately, in whatever service issued it, that is the
step that actually closes the hole. Cleaning it out of the repository's past commits is a separate,
real job that this kit deliberately does not walk you through solo, because a mishandled history
rewrite can do more damage than the leak itself did (`04-repositories-and-visibility.md:198-208`).
Bring this one to a developer or to GitHub's own community support.

**You are locked out, with no recovery codes and no other configured method.** Work through the
recovery steps in `01-accounts-and-security.md` first. If both your two-factor device and your
recovery codes are genuinely gone, GitHub's own documentation is blunt that support "cannot assist
with troubleshooting your 2FA methods" (`01-accounts-and-security.md:192-196`), and there is no
documented path back into that specific account. If the account held anything critical, this is
the moment to get advice on what is actually recoverable before assuming nothing is, rather than
guessing alone.

**A contractor's engagement is ending, and the work was sensitive.** GitHub can cut off their
future access with one click. It cannot reach their laptop. If what they built or saw matters
enough that their local copy is a real concern, that is a conversation, and possibly a written
agreement, to have directly with them, not a setting to configure and forget.

**You want something automated: tests that run by themselves, a site that deploys itself when code
changes.** That is real, useful, and outside what this kit teaches. It is a conversation with a
developer about what you actually need, not a browser click path to follow alone.

---

## Three real setups, followed through end to end

### A solo operator, everything on one laptop

She runs a small business alone, and has been keeping her price list, her booking notes, and a
half-built invoicing spreadsheet in a folder on her laptop. No GitHub yet.

**What she does, in order:** creates her account, turns on two-factor authentication with an
authenticator app, and saves her recovery codes to a password manager (`01-accounts-and-security.md`).
She skips the organization question entirely: nobody else needs ongoing access to her code, so it
does not meet the trigger. She creates one private repository for the invoicing project, with a
README describing what it does and a `.gitignore` that blocks `.env` files from day one. She works
directly, committing straight to her repository, no branches needed at this size.

**What she does not do:** create an organization "to look more professional." Set up a review
process for changes only she ever makes. Worry about teams, base permissions, or outside
collaborators, none of them apply while she is the only person touching her code.

**What would change this:** the day she brings on a bookkeeper or a virtual assistant who needs
ongoing access to her repository. That is the trigger from the organization section above. Until
then, everything on this page beyond account security is genuinely not for her yet.

### A team of three, one of them technical

A café owner runs an online ordering site. Her nephew built it and keeps it running. A staff member
updates the menu text and opening hours from time to time.

**What they do:** the owner creates the organization, since access needs to survive her nephew
being unavailable on any given day, and adds him as the second owner immediately, because he is
the one who will actually use the organization's admin tools day to day. Base permission is set to
Read. The nephew gets Write access on the ordering site's repository, since he builds it. The staff
member's menu edits live in their own smaller repository (a standardising decision: separating
content that changes often, edited by a non-technical person, from the code that runs the site),
and she gets Write there only, plus Read on the main site so she can see what it does.

**Their review habit:** informal, level 2 on the process ladder above. Before anything the staff
member changes goes live, the nephew glances at it, since he is the one who understands what a
mistake there would actually break. Nobody enforces this with a GitHub setting: at three people,
the habit does the job, and a $4 USD per seat per month enforced rule (`02-organizations.md:38`)
would buy them very little over what they already do.

**What would change this:** if a menu-text mistake actually cost them money or embarrassed them
publicly, that is the signal to move to enforced review, not a hunch that they probably should.

### A business bringing in a contractor for six weeks

A landscaping business hires a freelance developer to build a customer booking page. The
relationship is scoped, priced, and ends in six weeks. There is no plan to bring the developer onto
the team afterward.

**What they do:** the developer is added as an outside collaborator on the one repository the
booking page lives in, not as a full organization member, since there is no ongoing relationship to
justify that (`03-members-and-access.md:83-106`). They get Write access, since they are building,
not Admin, since Admin includes destructive actions like deleting the repository entirely, and this
contractor has no reason to need that (`03-members-and-access.md:34-42`). The business owner sets a
calendar reminder for the end of the six weeks, since GitHub does not do this automatically for
you.

**At the end of the engagement:** the owner removes the developer's access using the outside
collaborator removal steps in `03-members-and-access.md`, and has a direct conversation about what
the developer already has on their own laptop, since removal stops future access but does not
reach a machine that already has a local copy (`03-members-and-access.md:134-138`).

**What would change this:** if the "six week" engagement turns into an ongoing relationship, that
is the moment to reconsider outside-collaborator status and, if a second person now needs recurring
access, revisit the organization question from the top of this document.

---

## The one habit underneath everything above

Every recommendation in this document reduces to the same question, asked at every size and every
decision point: **what is the narrowest access, and the smallest amount of process, that gets this
week's job done safely?** Grant that. Not more, in case you need it later. Widening access later
takes thirty seconds. Finding out a year on that everyone has had more access than they ever needed
is the expensive version of this same question, answered wrong from the start.
