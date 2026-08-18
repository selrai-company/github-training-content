# When it goes wrong, and how to get unstuck

Every other file in this kit teaches you how to do something. This one is for the moment it
hasn't gone the way that file described, and you don't know what to click next.

## What this gets you

Ten real situations are covered below, each in the same shape: what actually happened, what to do
about it right now, and the point at which you should stop digging and ask someone rather than
keep guessing. None of these mean you broke something. GitHub is built so that almost nothing you
can do by clicking around is instantly, silently permanent. The two genuinely hard-to-undo actions,
deleting a repository outright and rewriting history to remove something, are both flagged clearly
below, and this kit steers you away from doing either one alone.

The business value is time and nerve. Without this page, a stuck moment turns into an afternoon of
guessing, or worse, a guess that makes the original mistake bigger. With it, you find your
situation below, take the one safe step, and get back to work. Bookmark this page.

## Before you start

- You do not need to have read every other file in this kit to use this one. Each situation below
  names the file that covers it in full, where one exists.
- You need to be signed in to GitHub in your browser for most of what's below. A handful of items
  are about not being able to sign in at all, those are covered first.
- Every member of this kit has Claude Code on the Max plan. Where it's genuinely the safer or
  easier path, this page says so and shows you what to type. Where the problem is tied to you as a
  real person, signing in, two-factor authentication, account recovery, it stays in your browser,
  and this page says that plainly too. That's the same rule this whole kit follows.
- Work out which of the ten situations below you're actually in before you try anything. "I can't
  sign in" and "I lost my phone with two-factor authentication on it" read like the same problem
  and are not, and the fix for one won't touch the other.

## The words you need

**Two-factor authentication (2FA).** A second proof of identity, on top of your password, usually a
code from an app or a physical key, that GitHub asks for when you sign in. It matters because it's
also the thing that can lock you out hardest if you lose access to it, there is no simple support
override for it, covered below.

**Recovery codes.** A one-time-use list of backup codes you're given when you turn on two-factor
authentication, meant to be saved somewhere that is not the phone your 2FA normally runs on. They
are the fastest way back in if you lose your usual 2FA method, and the only fully self-service one.

**Revert.** Adding a brand new commit that does the exact opposite of an earlier one, so a file or a
whole set of changes ends up back the way it was. The mistaken commit stays in the project's
history, sitting right next to the one that cancels it out. Nothing about the past is erased. Think
of it as crossing something out rather than tearing the page.

**Force-push.** Pushing a rewritten history up to GitHub, overwriting what was there before instead
of adding to it. This kit does not teach it as a routine fix, and it's one of the specific actions
Claude Code treats as needing you directly and deliberately involved, covered in
`11-github-with-claude-code.md`.

**Secret.** Any value that grants access on its own if someone else gets hold of it, a password, an
API key, a token. The danger with a secret isn't that it exists in a file, it's that once it's been
seen, only changing the value itself, not deleting the file, actually closes the risk.

**Rotate.** Getting a new value for a secret from whatever service issued it, and invalidating the
old one there at the same time. This is the actual fix for a leaked secret, not deleting the file
that contained it.

**Rewriting history.** Editing or removing an entry from a repository's commit history itself,
rather than adding a new commit that cancels it out. This kit doesn't teach how to do this. Where it
would be the answer, this page says so and tells you to bring it to someone else, a mistake made
while rewriting history can do more damage than the thing you were trying to fix.

**Restore branch.** A button GitHub shows on a closed or merged pull request, that brings back the
branch that pull request was made from if it's since been deleted.

**Default branch.** The branch a repository shows first, and the one most connected features (like
automatically closing a linked issue) are built around. Usually called `main`.

**ZIP snapshot.** A one-time downloaded copy of a repository's files, with no connection back to
GitHub and no history attached. It never updates itself, unlike a clone, which stays linked to the
repository it came from.

**Danger Zone.** The section at the bottom of a repository's **Settings** page where the genuinely
serious, hard-to-reverse actions live: changing visibility, transferring ownership, and deleting
the repository outright. It's laid out separately from everything else on purpose.

**Fork.** A full copy of someone else's repository, made under your own account, that stays linked
back to the original.

## How to do it

### I cannot sign in

"I can't sign in" is actually several different problems wearing the same sentence. Work out which
one you're in before you try anything, because the fix is different for each.

**You typed the wrong password, or genuinely can't remember it.** Go to
[github.com/password_reset](https://github.com/password_reset). GitHub's own documentation
describes exactly what happens next: "Enter the email address associated with your account," then
"click **Send password reset email**." One detail worth knowing before you go looking for the
email: "Only primary and backup email addresses can be used to request a new password," so if you
try an address that isn't one of those, nothing will arrive. Once the email lands, you need to act
on it: GitHub's own wording is that you must click the reset link "within 3 hours of receiving the
email," after that you'd need to request a fresh one.

**You can't remember your username, or which email you signed up with.** If you still have a
working local copy of a repository on your machine, or GitHub Desktop installed, GitHub's own
documentation gives a few ways to recover it from there: in GitHub Desktop, your username is under
**Preferences then Accounts** (Mac) or **Options then Accounts** (Windows) in the app's own menu, and
your email is in the matching **Git** section. If you're working from a clone through Claude Code
instead, ask it directly: "What GitHub username or email is this repository set up under?" and it
can check your git configuration for you. If you have neither a local copy nor GitHub Desktop and
genuinely can't recall any detail of the account at all, that's a case for GitHub's own support form,
covered below.

**You're being asked for a two-factor code you can't supply.** That's not a sign-in problem on its
own, it's the next section, go there.

**You see a message about a payment, or the word "locked," rather than a plain sign-in failure.**
That's a narrower, different thing: it means your account's *paid* features are locked, not that
you can't sign in at all. GitHub's own wording: "Your account's paid features are locked if your
payment is past due because of billing problems." The fix is to update your payment method. In the
top right corner of any GitHub page, click your profile picture, then **Settings** in the menu that
opens. In the left-hand list of settings, find **Billing & Licensing**, then **Payment information**
underneath it. You'll know you're in the right place because the page shows your current payment
method and a way to add a new one. GitHub's own documentation says "the account will automatically
unlock when a payment has been successfully processed," though it also notes payments "may take up
to 24 hours to process."

**None of the above, and you still can't get in.** GitHub has a dedicated support page for exactly
this situation, at
[support.github.com/contact/cannot_sign_in](https://support.github.com/contact/cannot_sign_in).
This page's own research couldn't confirm what happens after you submit that form, since GitHub
doesn't publish those internal steps, so **confirm on your own screen** what it asks for once you're
there, and follow it.

**Stop and ask if:** you've tried a password reset and the username-recovery steps above and you're
still locked out, or if any message you see mentions your account being suspended or restricted for
a policy reason rather than a simple lockout. Don't create a second GitHub account to work around
this without checking with your team first, your business's repositories are almost certainly tied
to the original account, and a second account won't see them.

### I lost my phone with two-factor authentication on it

This is covered in full, with every step, in `01-accounts-and-security.md`. The short version, in
order:

1. **Try your recovery codes**, if you saved them, at the sign-in screen's "More options" then 2FA
   recovery code.
2. **Try any other method you already had configured**, a passkey, a security key, or GitHub Mobile
   on a second device.
3. **If neither works, you're into GitHub's formal account recovery process.** Its own account
   recovery policy states plainly: "GitHub Support will not restore access to accounts with
   two-factor authentication enabled if you lose your two-factor authentication credentials or lose
   access to your account recovery methods." There is no support ticket that skips this.
4. **If every one of those is genuinely exhausted**, the only documented path left is unlinking the
   email address from the locked account so you can start fresh with it. This does not hand back
   your old repositories, your history, or the account itself, it only frees the email address.

**Stop and ask if:** you don't have recovery codes and don't recognise any other configured method.
At that point there is nothing left to try alone, and repeatedly guessing at codes doesn't help.
Go straight to the recovery steps in `01-accounts-and-security.md`, and treat the community as moral
support here, not a technical fix, nobody else can complete this step for you.

### My invite never arrived

Covered in full in `03-members-and-access.md`. The checklist:

1. **Check spam and promotions folders first.** This is, by a wide margin, the most common cause.
2. **Confirm which email address the invite actually went to**, and that it's one you check. If it
   went to an address you don't use day to day, it's sitting there, not lost.
3. **Check whether more than seven days have passed.** GitHub's own wording is direct: "if an
   invitee does not accept the invitation within seven days, the pending invitation expires
   automatically," and this applies the same way to an invite to join an organization and an invite
   to be a collaborator on one specific repository.
4. **If it's expired**, whoever invited you can find it under **Failed invitations** on the
   organization's People tab (or the repository's Collaborators screen) and click **Retry
   invitation**, rather than either of you assuming something is broken. Confirm on that screen
   that the invitation's status changes from failed back to pending after retrying.

**Stop and ask if:** it's genuinely under seven days, it isn't in spam, and the person who invited
you confirms, by looking at their own screen, that the invite is still shown as pending. At that
point, stop guessing and have them cancel it and send a fresh one to a confirmed correct address
instead.

### I pushed to the wrong place

**What happened, most often:** a change landed on the wrong branch inside a repository you meant to
be working in, usually a direct commit to your main branch when you meant to be on a working branch.
Less often, it landed in the wrong repository entirely.

**What to do now:**

1. **Work out exactly where it landed.** Open the repository on github.com and look at its recent
   commits, or ask Claude Code directly: "What did we just push, and where did it go?" It can tell
   you the repository, the branch, and the exact commit.
2. **If it's your own repository (or one you have Write access to), and it just landed on the wrong
   branch, the safe fix is to revert the commit, not force it back out.** A revert creates a brand
   new commit that undoes exactly what the mistaken one did. GitHub's own engineering blog describes
   why this is the safe move: "`git revert` will create a new commit that's the opposite (or
   inverse) of the given SHA... This is Git's safest, most basic 'undo' scenario, because it doesn't
   alter history." Nothing about your project's past is erased or rewritten, a new commit is added
   that cancels the mistaken one out.
   - **If the mistaken change went through a pull request that's already merged**, open that pull
     request on github.com and, near the bottom, click **Revert**. GitHub's own documentation
     describes what this does: "Reverting a merged pull request creates a new pull request that
     reverts the original merge commit." Merge that new pull request the normal way to finish
     undoing it.
   - **If it was a direct commit with no pull request involved**, ask Claude Code plainly: "Revert
     the commit we just pushed to [branch name], the one about [what it changed]." It will find that
     commit and push the inverse of it for you.
3. **Never ask for a force-push as the fix here.** A force-push overwrites history, not just adds to
   it, and it's one of the specific actions Claude Code treats as needing you directly and
   deliberately involved rather than something it does on its own, covered in
   `11-github-with-claude-code.md`. Reverting is the safe direction for this situation. Force-pushing
   is not, and this kit doesn't teach it as a routine fix.
4. **If it landed in a repository that genuinely isn't yours**, stop there. Don't try to revert or
   delete anything in someone else's repository yourself, you may not have the access to do it
   safely, and guessing can make it worse. Tell the repository's owner exactly what happened and let
   them decide what to do next.

**Stop and ask if:** you're not certain which repository or branch it actually landed on, or if what
you pushed contained something sensitive, that's the next section, and rotating the secret comes
before tidying up the commit.

### I committed a file with a password or an API key in it

**What happened:** a real secret, a password, an API key, a token, ended up inside a file that got
committed and pushed.

**What to do right now, in this order:**

1. **Rotate the secret first, before anything else.** Get a new key or password from whatever
   service issued the leaked one, and invalidate the old one there. GitHub's own guidance is direct
   about this being the first step: "if the sensitive data you need to remove is a secret (e.g.
   password/token/credential)... as a first step you need to revoke and/or rotate that secret." This
   single step is what actually closes the danger, the moment the old value stops working anywhere,
   it doesn't matter how many old commits still contain a copy of it.
2. **Add it to your `.gitignore` so it can't happen the same way again.**
   `04-repositories-and-visibility.md` has a ready-to-paste starting file, the three lines covering
   `.env` files matter most.
3. **Do not just delete the file in a new commit and consider it handled.** GitHub is specific about
   this not being enough on its own: the value "is already checked in," and deleting it going
   forward "does not" remove it from every earlier commit that already held it.
4. **Do not try to rewrite your repository's history yourself to scrub it out.** This kit
   deliberately does not teach that as something to attempt alone: a mistake made while rewriting
   history can do more damage than the original leak did. Cleaning history is a real job, but it's
   one to bring to the community, not a solo fix on a call with an AI assistant.

**Stop and ask if:** the moment you realise a real secret is committed, full stop, don't spend time
deciding whether it's "bad enough" to rotate. Rotating takes minutes and closes the actual danger.
The history cleanup afterwards is not urgent, and it's exactly the point at which to bring in the
community rather than dig further alone.

### I deleted something

What you can get back, and how, depends entirely on what was deleted.

**A whole repository.** GitHub's own wording is careful here, and worth reading exactly as written:
"some deleted repositories can be restored within 90 days of deletion." Not every one. If you think
you deleted a repository by mistake, act immediately and contact
[GitHub support](https://support.github.com/) rather than assuming the 90 days definitely covers
your case.

**A branch.** If that branch was the head branch of a pull request you'd already closed or merged,
you can get it back: open that pull request, and near the bottom click **Restore branch**. Check
back on the repository's branch list afterward, if the branch you deleted is there again, the
restore worked. If the branch never went through a pull request at all, there's no documented way to
bring it back through GitHub's interface. If you're ever unsure whether you'll want a branch's work
again, the safer habit is to leave it alone rather than delete it, an unused branch costs nothing
just sitting there.

**A file.** This uses the same revert mechanism as the previous "pushed to the wrong place" section,
because deleting a file is itself just a commit, and the opposite of a commit that removes a file is
a commit that adds it back. If the deletion went through a merged pull request, open it and click
**Revert**. If it was a direct commit, ask Claude Code to revert that specific commit. Either way,
you get the file back exactly as it was, without touching anything else that's happened since.

**Stop and ask if:** it was a whole repository, don't wait to see if you really need it back, act
immediately, minutes matter more than certainty for the 90-day window above. For a branch or file
outside of a pull request with no documented restore path, ask before trying any git command you
don't already know from this kit, guessing at commands beyond a revert can make recovery harder, not
easier.

### I cannot see a repository someone says they shared with me

Work through this in order, most people find the answer in the first three steps.

1. **Confirm you're signed in to the correct GitHub account.** In the top right corner of any
   GitHub page, click your profile picture. A menu opens showing your username, check it matches
   what you told the person who shared it with you. Having more than one GitHub account (a personal
   one and a work one, say) and being signed into the wrong one in your browser is a genuinely
   common, easy-to-miss cause. If a different account's name is showing, sign out and back in as the
   right one before anything else.
2. **Confirm you actually accepted the invite, not just received it.** An invitation to join an
   organization, or to be a collaborator on one specific repository, needs to be accepted before it
   grants you anything, GitHub's own wording: "They will need to accept the invitation before
   becoming a member." Check your email for it, and check it hasn't already expired, covered above.
3. **Work out exactly what kind of access they meant to give you.** Full organization membership, a
   team, and a single-repository collaborator invite are three different things that get checked in
   three different places, all covered in `03-members-and-access.md`.
4. **Check the organizations you actually belong to.** Open
   [your organization settings](https://github.com/settings/organizations). If the organization the
   repository belongs to isn't listed there, you're not a member of it yet, regardless of what
   anyone intended to do.
5. **Double check the exact repository address with whoever shared it.** A private repository is
   only visible to people explicitly granted access, GitHub's own definition: "Private repositories
   are only accessible to you, people you explicitly share access with, and, for organization
   repositories, certain organization members." Being sent the link on its own grants you nothing,
   if a link was all you were given, the actual access step, covered in `03-members-and-access.md`
   or `04-repositories-and-visibility.md`, may not have happened yet.
6. **If all of that checks out and you still can't see it**, ask the person who shared it to open
   that repository's own **Settings then Collaborators & teams** (or the organization's **People**
   tab) and confirm your exact username is listed there, not just that they remember adding you.

**Stop and ask if:** you've confirmed your account, confirmed the invite was genuinely accepted, and
it still doesn't show. That's not something to keep guessing at alone, get the person who shared it
to look at their own screen with you at the same time, one of you is very likely seeing something
the other one isn't.

### My change is not showing up

Work through this in order, it's almost always one of the first four.

1. **Did you actually commit it?** An edit sitting in an open file, whether in the browser or on
   your machine, isn't tracked by git at all until it's committed.
2. **If you're working through a clone, did you push it?** A commit made on your machine stays only
   on your machine until it's pushed. Ask Claude Code: "Did we push that commit?" if you're not
   sure.
3. **Are you looking at the right branch on github.com?** If your change went to a working branch
   rather than your default branch, the page everyone else sees won't show it until it's merged.
4. **If it went through a pull request, has that pull request actually been merged, not just
   opened?** An open, unmerged pull request doesn't change anything anyone else sees yet.
5. **Hard refresh your browser** (Ctrl+F5 on Windows, Cmd+Shift+R on Mac) or open the page in a
   private or incognito window before assuming GitHub itself is behind.
6. **If you're working from a downloaded ZIP rather than a clone, remember what a ZIP actually is.**
   GitHub's own documentation is direct: "snapshots don't contain the entire repository history," it
   is a one-time copy that never updates itself. If you edited a file inside an old ZIP folder, you
   may be looking at an outdated copy, not a real problem with your change. Download it again.

**Stop and ask if:** you've confirmed it's committed, pushed, on the branch you're checking, merged
if it needed to be, and refreshed the page, and it's still nowhere to be seen. Bring the exact commit
or pull request link with you when you ask, rather than describing it from memory, see "Asking for
help well" below for why that matters.

### I have a conflict I do not understand

A merge conflict is git asking you a question it can't answer by itself, not an error you caused and
not a sign anything is broken. This is covered start to finish, including what the marker lines
mean, the exact browser steps to resolve a simple one, and precisely where the browser's tool stops
and Claude Code takes over, in `08-merge-conflicts.md`. This page won't repeat it here.

**Stop and ask if:** the **Resolve conflicts** button isn't there or won't click, or what's inside
the marker lines doesn't look like something you'd normally read or write. `08-merge-conflicts.md`
covers exactly how to recognise that moment and what to do next, don't force the browser tool past
that point.

### The repository is public and should not be

**What happened:** at some point the repository's visibility was set to public, whether when it was
first created or changed afterwards, on purpose or by mistake.

**What to do right now, in this order:**

1. **Flip it back to private immediately.** Open the repository's front page, and along the top, in
   the row of tabs that starts with **Code** and **Issues**, look toward the right-hand end for a
   tab labelled **Settings**. On that page, scroll to the bottom to the **Danger Zone**. You'll know
   you're in the right section because it groups the repository's most serious actions together:
   changing visibility, transferring ownership, and deleting the repository. Click **Change
   visibility**, select **Private**, confirm you've read the warnings, and click through to finish.
   If you don't see a **Settings** tab at all, you're not an administrator of that repository, and
   whoever is will need to make this change, or grant you that access first
   (`03-members-and-access.md` covers access levels). Full click-by-click detail is in
   `04-repositories-and-visibility.md`.
2. **At the same time, assume anything sensitive it held has already been seen or copied.** Being
   public even briefly doesn't undo itself when you flip the switch back.
   `04-repositories-and-visibility.md` states this plainly: "assume it may already have been seen or
   copied, and flipping back to private does not undo that."
3. **If it held a real secret, that's the previous section on this page, act on it now, not after
   you've finished tidying up visibility.** Rotate the secret first, in whatever service issued it.
4. **Know what flipping it back changes on its own, so you're not surprised afterward.** Existing
   forks of the repository stay public and get detached rather than turning private with you, and any
   GitHub Pages site published from it gets unpublished, both per GitHub's own documentation, covered
   in full in `04-repositories-and-visibility.md`.

**Stop and ask if:** you're not certain whether anything sensitive was actually in it, or you don't
have the admin access to change the visibility yourself. Don't wait to find out which before acting,
flag it in the community immediately and get someone with access to flip it while you work out what
it held. Minutes matter more here than being sure first.

### Asking for help well

The single biggest difference between a question that gets answered in five minutes and one that
sits unanswered is what you include the first time you ask.

Bring these five things, every time:

```
What I was trying to do:
[one sentence]

The exact link (repository, pull request, or branch):
[paste it]

What I actually see (the exact wording of any error, or a screenshot):
[paste or describe it, word for word, not your interpretation of it]

What I expected to happen instead:
[one sentence]

What I've already tried:
[so nobody repeats a step that didn't work]
```

Describe what's on your screen, not what you think went wrong. "It says Error 403" gets a much
faster, more accurate answer than "it's broken." GitHub's interface changes over time, so if
something you see doesn't match what a guide (including this one) describes, trust your own screen
over the guide, and say so when you ask, that mismatch is itself useful information for whoever
helps you.

## Strategy: how to actually use this

**One rule outranks everything else on this page: if a secret is involved, rotate it first, no
matter what else is going on.** If you pushed to the wrong place and the commit also contained an
API key, don't sequence it as "fix the branch, then think about the key." Rotate the key first,
every time, then come back and sort out where the commit landed. A misplaced commit costs you tidy-up
time. A live secret sitting in a public or semi-public place costs you the thing it protects.

**Not every wrong turn belongs on this page.** If something looks different from what you expected
but nothing is broken and nothing is urgent, that's often just a refresh or a wrong-branch moment,
covered under "My change is not showing up" above. Reach for this page when you're genuinely stuck
or genuinely worried, not for every small surprise, or you'll start treating routine friction as an
emergency.

**A solo operator working alone has to be more cautious with Claude Code's suggestions, not less.**
There's nobody looking over your shoulder to catch a bad guess before it's pushed. The trade-off:
stick strictly to the fixes shown on this page and in the files it points to, and treat any command
Claude Code proposes that isn't shown here as a "stop and ask" moment by default, even if it sounds
confident. The community is your second pair of eyes when you don't have a teammate for that.

**A team of four should agree, once, on who holds the "stop and ask" line.** Not every situation
needs a formal decision-maker, but the ones flagged "stop and ask" above genuinely benefit from one
person who's allowed to say "we wait" while someone checks, rather than whoever is online first
guessing at a fix under pressure. Decide this before you need it, not during the incident.

**The decision rule that covers almost everything here:** if the fix is a documented click shown on
this page, do it yourself. If the fix would need a git command not shown anywhere in this kit,
that's the line, stop and ask, regardless of how confident anyone (including Claude Code) sounds
about it. Confidence isn't the same as safety when the action can't be easily undone.

**What good looks like months later:** a team that's never once needed the "rewriting history"
warning on this page, because the `.gitignore` habits and rotation discipline from day one meant a
secret never had to be scrubbed out of history in the first place. That's this page working, not
this page being unnecessary.

**What would change my mind about a "one-off" mistake:** the same mistake happening twice on the
same repository. A single accidental push to the default branch is a Tuesday. A second one, from the
same person, on the same repository, within a few months, isn't bad luck anymore, it's a sign the
underlying setup needs a guardrail, most often branch protection, covered in
`10-protecting-your-work.md`, so the mistake becomes structurally harder to repeat rather than
something you keep reverting by hand.

## A worked example

The café's ordering site is run by the same small team described in the strategy pack for this kit:
an owner, a nephew who built and maintains the site, and a staff member who updates menu text and
hours.

The staff member has started making small text changes herself, using Claude Code, on a working
branch, the way `05-daily-workflow.md` describes. One afternoon, in a hurry before a delivery
deadline, she commits and pushes a change directly, without checking which branch she's on, and it
lands straight on the site's default branch. Worse, the file she edited also contained a test API
key for the payment provider, sitting in a `.env` file that was never added to `.gitignore`.

She notices the mistake within the hour and messages the nephew rather than trying to fix it herself.
He reads this page and follows the priority rule at the top of the strategy section above: the
secret comes first, regardless of the branch problem sitting next to it. He logs into the payment
provider's dashboard, generates a new test key, and revokes the old one immediately, before he does
anything else. That single step means the leaked key is now worthless to anyone who might have seen
it, whether or not the repository was ever public.

Only once that's done does he turn to the branch. He asks Claude Code: "What did we just push, and
where did it go?" It confirms the commit landed directly on the default branch. Since there's no
pull request involved, he asks it to revert that specific commit, and it pushes the inverse change,
restoring the file to how it was before, without touching anything else. He does not attempt a
force-push, and he does not try to remove the old key from the repository's history himself, that
value is already dead now that it's rotated, so there's no urgency left in the history itself.

Last, he adds `.env` to the repository's `.gitignore` file, using the starting file in
`04-repositories-and-visibility.md`, so the same file can't be committed by accident again. The
whole incident, start to finish, costs him about fifteen minutes, almost all of it the rotation
step, because he followed the order this page recommends instead of tidying the branch first and
getting to the key second.

## If it goes wrong

**Your exact situation isn't one of the ten above.** Re-read the "what happened" line of the closest
match rather than assuming yours is unique, most real problems are a variation of one of these.

**You tried the fix here and it didn't work.** Stop before trying a second thing on top of the
first, especially anything involving git commands not shown in this kit. Go back to the "stop and
ask" line for that section and follow it, rather than layering guesses.

**Nothing in this whole kit covers it.** Say that plainly to whoever you ask, rather than presenting
a guess as a fact. "I've checked this kit's troubleshooting page and it isn't in there" is a
genuinely useful thing to tell someone helping you, it saves them from re-explaining something you
already ruled out. Use the "Asking for help well" template above when you do.

## FAQ

**Did I permanently break something?** Almost certainly not. Nearly everything covered on this page
has a documented way back, or a safe forward-only fix like a revert. The two genuinely hard-to-undo
actions on GitHub are deleting a repository outright and rewriting history to remove a secret, and
this kit deliberately steers you away from attempting either alone.

**Can Claude Code fix any of this for me automatically?** It can do the git side of several of
these: reverting a commit, checking exactly where a push landed, pulling the latest changes. It
cannot do anything tied to your identity as a real person, signing in, two-factor authentication,
accepting an invite, recovering an account, or changing a repository's visibility. Those stay in
your browser, signed in as yourself, on purpose, the same rule `01-accounts-and-security.md` and
`11-github-with-claude-code.md` both apply.

**Is it ever OK to just start over with a new repository or account instead of fixing this?** For a
very young repository with almost no history, sometimes, that's a genuine judgement call. It's never
the right move as a way around an account lockout tied to a business's existing repositories, and
it's never the right move to avoid rotating a leaked secret, that danger follows the secret, not the
repository or account it happened to leak from.

**Why does this page keep saying "stop and ask" instead of just giving me one more thing to try?**
Because the fixes this kit teaches are the ones that are genuinely safe for someone without a
technical background to do alone. Past that point, the honest answer is that guessing at git
commands this kit hasn't shown you can turn a small, recoverable mistake into a bigger one. Asking
costs you a few minutes. A bad guess can cost a lot more.

**I'm not sure which of the ten situations I'm even in, where do I start?** Read the "what happened"
line at the top of each section, not the full section, until one matches what's on your screen.
Most people find their situation in under a minute this way. If genuinely nothing matches, that's
the "Nothing in this whole kit covers it" line above.

## Quick reference

- **Can't sign in (forgot password):** [github.com/password_reset](https://github.com/password_reset)
- **Can't sign in (paid features locked):** update payment method under profile picture, then
  **Settings**, then **Billing & Licensing**, then **Payment information**
- **Can't sign in (nothing above worked):**
  [support.github.com/contact/cannot_sign_in](https://support.github.com/contact/cannot_sign_in)
- **Lost 2FA device:** try recovery codes, then any other configured method, then
  `01-accounts-and-security.md`
- **Invite never arrived:** check spam, check the email address, check the seven-day expiry,
  `03-members-and-access.md`
- **Pushed to the wrong branch:** revert the commit, ask Claude Code, never force-push
- **Committed a secret:** rotate it first, always, before touching the commit or the branch
- **Deleted a repository:** contact [GitHub support](https://support.github.com/) immediately, 90-day
  window at best
- **Deleted a branch:** open the pull request it came from, click **Restore branch**, if it had one
- **Deleted a file:** revert the commit or pull request that removed it
- **Can't see a shared repository:** check the account you're signed in as, then the invite, then
  `03-members-and-access.md`
- **Change not showing up:** check committed, pushed, right branch, merged, then hard refresh
- **Merge conflict:** `08-merge-conflicts.md`
- **Repository is public by mistake:** Settings, then Danger Zone, then Change visibility, then
  Private, then assume it was already seen
- **Asking for help:** what you tried to do, the exact link, the exact error, what you expected,
  what you've already tried

## Sources

- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/updating-your-github-access-credentials
- https://docs.github.com/en/account-and-profile/how-tos/email-preferences/remembering-your-github-username-or-email
- https://docs.github.com/en/billing/using-the-billing-platform/unlocking-a-locked-account
- https://support.github.com/contact/cannot_sign_in
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/recovering-your-account-if-you-lose-your-2fa-credentials
- https://docs.github.com/en/site-policy/other-site-policies/github-account-recovery-policy
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization
- https://github.blog/changelog/2020-02-05-self-expiring-repository-and-organization-invitations/
- https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request
- https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
- https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives
