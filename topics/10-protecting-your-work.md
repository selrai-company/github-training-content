# Protecting the main copy, and what it costs

This file covers why you would stop people pushing straight to your default branch, the two ways
GitHub lets you enforce that (rulesets and the older branch protection rules, and which one this
kit reaches for today), requiring a review before a change can merge, what that actually costs a
small team versus what it buys, why a solo operator usually should not turn this on the way a team
does, and what push protection for secrets does and does not do.

## What this gets you

Protecting your main branch means GitHub itself stops a change from landing on the copy your
website, your ordering system, or your business actually runs on, until whatever rule you set has
been satisfied, rather than relying on everyone remembering to be careful. Without it, anyone with
Write access can push straight to that branch, on purpose or by accident, and the next visitor to
your site sees the result immediately. GitHub's own reasoning for keeping a main branch separate
from everyone's working copies in the first place: "Rather than modifying the default branch
directly, you create a separate branch to develop features or test ideas. This prevents your
experimental or incomplete work from affecting the main codebase that others depend on." The rules
in this file are what make that actually enforced, instead of just a habit people are trusted to
remember.

## Before you start

**You need to already know what a branch and a pull request are.** If you have not read
`06-branches.md` and `07-pull-requests.md` yet, read those first. This file assumes you already
know both.

**You need administrator access to the repository.** Every setting this file covers is a
signed-in-as-you action on GitHub's own settings screens, the same category as creating an
organization or inviting a member. It is not something to hand to Claude Code, the same way this
kit never hands it two-factor authentication or billing.

**None of this matters yet if you are the only person with Write access to the repository.**
Nobody else can push to your main copy in that case, so there is nothing yet to enforce. This
starts mattering the moment a second person gets Write access to a repository your business
depends on. The Strategy section below walks through exactly when to bother and when not to.

## The words you need

**Default branch.** The branch GitHub treats as the main copy of your repository, the one people
see first when they open it, and the one a new branch copies from unless told otherwise. New
repositories name it `main`. Every rule in this file is about protecting this one branch.

**Branch protection rule.** GitHub's older mechanism for enforcing rules on a specific branch,
such as requiring a pull request and a review before a change can land. Only one branch protection
rule can apply to a given branch at a time.

**Ruleset.** GitHub's newer mechanism for the same job. More than one ruleset can apply to the same
branch at once, you can switch a ruleset off without deleting it, and anyone with Read access to
the repository can see which rulesets are active, not just administrators. This kit's
recommendation for the one to reach for today, covered below.

**Enforcement status.** Whether a ruleset is actually switched on. A brand-new ruleset starts set
to **Disabled** and enforces nothing at all until you change it to **Active**. This is the single
most common reason a new ruleset looks like it is not working, it was never switched on.

**Bypass list.** The people, teams, or roles allowed to skip a rule that would otherwise block
them. A ruleset does not exempt anyone automatically, whoever should be able to skip its rules has
to be added to the list on purpose.

**Administrator.** Someone with full admin-level access to a repository, including the ability to
change its settings. As the owner of your own repository, you are an administrator of it.

**Required approval.** A reviewer's sign-off on a pull request that GitHub can be set to require
before that pull request is allowed to merge. Without this turned on, an approval or a "Request
changes" is a strong signal, not something that actually stops a merge.

**CODEOWNERS file.** A file you can add to a repository naming specific people as responsible for
specific files or folders, so GitHub can automatically ask them to review a pull request that
touches those paths. Most small repositories in this kit's audience will not have set one up.

**Force push.** A push that rewrites a branch's history instead of adding to it. It can silently
overwrite work other people are relying on, which is why blocking it is one of the defaults this
file covers below.

**Push protection.** A feature that looks at what you are about to push and blocks it before it
reaches GitHub if it looks like a password, key, or token. It has a real bypass: anyone with Write
access can push past it anyway by giving a reason.

**Secret scanning.** The broader feature family push protection belongs to. It looks for
credentials already sitting in a repository, not just ones about to be pushed.

## How to do it

### Choosing rulesets or branch protection rules

GitHub has two separate features that do this job. Both are real, both are documented, and as of
when this kit was checked, GitHub's own words are that they "work alongside each other, and all
applicable rules are enforced" if a repository has both. You will not usually run both at once, but
neither one replaces the other automatically.

**Branch protection rules** are the older mechanism. GitHub's own definition: "You can protect
important branches by setting branch protection rules, which define whether collaborators can
delete or force push to the branch and set requirements for any pushes to the branch, such as
passing status checks or a linear commit history." One real limitation GitHub states plainly: "only
a single branch protection rule can apply at a time," which can get confusing once you have more
than one rule that might match the same branch.

**Rulesets** are the newer mechanism, and GitHub's own page on branch protection rules points
toward them directly: "For information about an alternative to branch protection rules, see About
rulesets." A ruleset does the same underlying job, plus a few things branch protection rules
cannot: multiple rulesets can apply to the same branch at once (GitHub's own wording: "Multiple
rulesets can apply to the same branch at the same time, while only one branch protection rule
applies"), you can switch a ruleset off without deleting it and losing your setup, and anyone with
read access to the repository can see which rulesets are active, not just administrators.

**This kit recommends rulesets as the one to reach for today.** That is our recommendation, the
same way squash and merge is our recommendation in `07-pull-requests.md`, not GitHub declaring one
mechanism obsolete. Branch protection rules still work and are still documented. Rulesets are just
the more flexible option if you ever need a second rule, a temporary exception, or want to turn a
rule off for a week without rebuilding it from scratch.

**The tier claim, and it carries a real qualifier.** Both mechanisms are gated by plan the same
way, and the split is by whether the repository is public or private, not by whether you are on an
organization at all. GitHub's own wording for rulesets: "Rulesets are available in public
repositories with GitHub Free and GitHub Free for organizations, and in public and private
repositories with GitHub Pro, GitHub Team, and GitHub Enterprise Cloud." GitHub's own wording for
branch protection rules, stating the identical split: "Protected branches are available in public
repositories with GitHub Free and GitHub Free for organizations. Protected branches are also
available in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud,
and GitHub Enterprise Server." In plain terms: on a public repository, either mechanism is free, on
any plan. **On private repositories**, you need at least GitHub Pro (the paid personal plan) or,
for an organization-owned repository, GitHub Team or above. If your repository is private and you
are on a Free plan, confirm on your own screen whether the option to add a rule or ruleset even
appears before you plan around it, that is the fastest way to know where you actually stand.

### Setting up a ruleset that protects your default branch

Open the front page of your repository, then, along the top, in the row of tabs that begins with
**Code** and **Issues**, look toward the right-hand end for a tab labelled **Settings**, with a
small gear beside it. The direct address, if you would rather go straight there, follows the
pattern `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings`. You will know you are in
the right place because a long list of setting groups appears down the left-hand side, starting
with General. If you cannot see a **Settings** tab at all, you are not an administrator of that
repository, and that is the thing to have fixed first; `03-members-and-access.md` covers who can
grant it to you.

1. In the left sidebar, under the group labelled **Code and automation**, click **Rules**, then
   click **Rulesets**. You will know it worked because the page heading changes to Rulesets, with
   a **New ruleset** button near the top right.
2. Click **New ruleset**, then click **New branch ruleset**. (There is a separate **New tag
   ruleset** next to it, for tags instead of branches, not what you want here.)
3. Under **Ruleset name**, type a name for it, something like `protect-main`.
4. Look for the enforcement status control near the top of the page. **A brand-new ruleset starts
   set to Disabled**, GitHub's own default, and a disabled ruleset enforces nothing at all. Click
   it and change it to **Active** once you are ready for the rule to actually apply.
5. In the **Target branches** section, click **Add a target**, then choose the option for your
   default branch specifically (this kit found it described in GitHub's own words as including
   "the default branch," worded close to **Include default branch** when this was last checked;
   if the exact wording on your screen differs slightly, pick whichever option clearly names your
   default branch rather than a text pattern).
6. Tick **Require a pull request before merging** (covered in more detail below), and any of the
   other rules you want, then click **Create** near the bottom of the page.

**Confirmation:** the ruleset now appears in your Rulesets list, marked Active, and if you try to
push straight to your default branch from the command line (or ask Claude Code to do it for you),
the push is rejected with a message naming the ruleset that blocked it.

**Screenshot placeholder:** the ruleset creation page, showing the "Ruleset name" field, the
enforcement status control near the top, and the "Target branches" section with an "Add a target"
button, so a reader can match each field to the steps above before creating one.

### The older way: a branch protection rule

Starting from the same repository Settings page covered just above, in the left sidebar, under
**Code and automation**, click **Branches**. You will know it worked because the page heading
changes to Branches, with a **Branch protection rules** section beneath it.

1. Under **Branch protection rules**, click **Add rule**.
2. Under **Branch name pattern**, type your default branch's name, usually `main`.
3. Under **Protect matching branches**, tick **Require a pull request before merging**, and any
   other rules you want.
4. Click **Create** near the bottom of the page.

**Confirmation:** the rule appears listed under **Branch protection rules** on that same Settings
page, naming the branch pattern it covers.

Nothing is wrong with picking this over a ruleset. It is a smaller page with fewer moving parts,
and for a single rule on a single branch, that simplicity is a real advantage, not a compromise.

### Requiring a review before a change can merge

This is the single most consequential rule either mechanism offers, and it is the one that answers
what `07-pull-requests.md` already flagged: without it, "Request changes" on a pull request is
"purely informational and will not prevent merging." With it turned on, that stops being true.

**What ticking it actually does.** GitHub's own wording: "You can require that all changes to the
target branch be associated with a pull request," and once you also require approvals, "Repository
administrators or custom roles with the 'edit repository rules' permission can require that all
pull requests receive a specific number of approving reviews before someone merges the pull request
into a protected branch." In the click paths above, that is the **Require approvals** option, with
a **Required number of approvals before merging** dropdown where you pick how many.

Two options worth knowing sit right alongside it, both optional: **Dismiss stale pull request
approvals when new commits are pushed** (GitHub's own wording: dismisses an existing approval "when
commits are pushed that affect the diff in the pull request," so an approval cannot quietly cover a
change made after it was given), and **Require review from Code Owners**, which only does anything
if your repository has a CODEOWNERS file naming specific people for specific paths, most small
repositories in this kit's audience will not have set one up.

### Other rules worth knowing about while you are on this page

Both mechanisms offer more than required reviews. Two are worth naming here because they are
directly about protecting the branch itself, and, under rulesets, both come switched on by default:

- **Block force pushes.** GitHub's own wording: "You can prevent users from force pushing to the
  targeted branches or tags. This rule is enabled by default." A force push can silently overwrite
  history other people are relying on, so leaving this on is rarely the wrong call.
- **Restrict deletions.** GitHub's own wording: "If selected, only users with bypass permissions
  can delete branches or tags whose name matches the pattern you specify. This rule is selected by
  default." This is what stops your default branch itself from being deleted by mistake.

There are others (required status checks, a linear history requirement, signed commits, and more)
that go beyond what a small business typically needs on day one. This file is not walking through
every one of them, turn on what solves a problem you actually have, and revisit the list on your
own screen if a specific need comes up later.

### Adding yourself to a ruleset's bypass list

This matters if you ever set up a ruleset with required reviews and do not want to risk locking
yourself out of your own solo work (the Strategy section below explains when this applies to you).
On the ruleset's page, in the **Bypass list** area, click **Add bypass**, search for the role,
team, or app you want, select it, and click **Add Selected**. You will know it worked because that
role now appears listed under Bypass list on the ruleset's page.

### Push protection for secrets, and its real limits

This is a different feature from everything above. It is not about who can merge, it is about
stopping a password or an API key from ever reaching GitHub in the first place. It is worth
knowing about, because push protection does less than people assume.

**What it is.** GitHub's own wording: "Push protection is a secret scanning feature designed to
prevent hardcoded credentials, such as secrets or tokens, from ever being pushed to your
repository." GitHub's own list of where it steps in: "Push protection blocks secrets detected in:
Pushes from the command line, Commits made in the GitHub UI, File uploads to a repository on
GitHub, Requests to the REST API, Interactions with the GitHub MCP server (public repositories
only)." When it catches something, GitHub's own wording is direct: "it will block the push and
provide a detailed message explaining the reason for the block."

**It has a bypass, and that is real, not a bug.** GitHub's own wording: "For push protection for
repositories, by default, anyone with write access to the repository can bypass push protection by
specifying a bypass reason." So push protection is a prompt to stop and check, not an absolute
wall, someone in a hurry who is confident the flagged text is not really a secret can push past it.

**Where it applies by default, and this is the same public-versus-private split as everything else
in this file.** GitHub's own wording, on public repositories: "Secret scanning runs automatically
for free." On an organization-owned private or internal repository, it is a paid feature you have
to turn on: "Available with GitHub Secret Protection enabled on GitHub Team or GitHub Enterprise
Cloud." There is also a separate, personal setting on your own GitHub account, covering pushes you
make to public repositories specifically, and GitHub's own wording for that one is: "Push
protection for users is on by default for public repositories." Confirm your own setting under
your account's [**Security settings**](https://github.com/settings/security). You will know you
are looking at the right thing because the page lists security-related toggles for your account;
this kit could not pin down the precise wording of this specific toggle from GitHub's own
documentation text, so read what your own screen actually says.

**What it does not do, and this is the part worth remembering.** Push protection only looks at
what you are pushing right now. It does nothing about a secret that is already sitting in your
repository's history from before it was turned on, or one that got through because someone
bypassed it. If a secret is already out, the fix is not push protection and it is not rewriting
history yourself either, rotate the key in whatever service issued it first, that closes the actual
danger regardless of how many old commits still mention the leaked value. Cleaning up the history
afterwards is a separate, harder job this kit deliberately does not walk you through solo, treat
push protection as a useful check, not a substitute for never typing a real password or key into a
file that gets committed in the first place.

### Doing this through Claude Code

You will not. Creating a ruleset or a branch protection rule, and turning on push protection, are
all signed-in-as-you actions on GitHub's own settings screens, the same category as creating an
organization or inviting a member. Claude Code can run git commands on your behalf, but it cannot
click a settings toggle that needs GitHub to see you specifically. If you ask it to "protect my
main branch," the right answer from it should be to walk you to this page, not to attempt the
setting itself.

What Claude Code *can* usefully do here: if a push it just tried to make on your behalf gets
rejected by a rule or by push protection, it will see GitHub's own rejection message and can
explain it back to you in plain English, including which rule or which detected secret caused it.
That is a genuinely good use of it, reading an error is exactly the kind of thing worth handing
over.

## Strategy: how to actually use this

**Who this actually matters for.** If you are the only person with Write access to a repository,
nobody else can push to your main copy anyway, so there is nothing yet to enforce. This starts
mattering the moment a second person gets Write access, and it matters more the more that
repository is something a customer, a client, or your whole business depends on.

**Where enforced review sits on the ladder.** `STRATEGY-PACK.md`'s process ladder walks through
this same decision in rungs, from nothing, for a solo operator, up through an organization with
narrow default access, then branches plus an informal review habit, then enforced review required
by GitHub itself, the level the "Requiring a review before a change can merge" section above sets
up (`STRATEGY-PACK.md:161`). Jumping straight to enforced review for a two- or three-person shop
usually buys almost nothing over the informal habit, because at that size the two produce the same
outcome nearly every time, and you pay a real subscription cost and absorb real waiting time for
the difference (`STRATEGY-PACK.md:166`).

**A solo operator** should skip everything in this file except, eventually, confirming the push
protection account setting mentioned above. There is no second person to protect your main branch
against yet, and turning on required reviews without adding yourself to a bypass list is how you
lock yourself out of your own work for no benefit.

**A team of two or three** usually does better with the informal habit: someone glances at a
change before it lands, and nobody enforces it with a GitHub setting. Move to an enforced ruleset
only once a mistake would actually cost money, embarrass you publicly, or a client genuinely
demands proof that changes get reviewed, not because you feel like you are overdue for it.

**A team of four or more, or anyone whose main branch runs something a customer depends on
directly,** is where enforced review starts earning its cost. Set up a ruleset, require at least
one approval, and add yourself, or the admin role, to its bypass list so a genuine emergency fix is
still possible without switching the rule off first.

**What would change this.** The signal to move up a level is a mistake that actually landed and
actually cost you something, not a hunch that you are probably due for more process. The signal to
move back down a level is reviews that have become a rubber stamp nobody actually reads, at that
point the rule is costing you waiting time and buying you nothing.

**What good looks like months later.** Nobody remembers switching the rule on, because it has
quietly stopped being something anyone thinks about. Changes go through a pull request, get a
genuine look before they land, and nobody has ever been locked out of their own repository by an
enforcement they forgot they had set up.

## A worked example

This is the same three-person team described in the strategy pack: a café owner, her nephew who
built and keeps running the online ordering site, and a staff member who updates the menu text and
opening hours (`STRATEGY-PACK.md:327-328`).

For the first year, their review habit is informal. The nephew glances at anything the staff
member changes before it goes live, and nobody has needed an enforced rule (`STRATEGY-PACK.md:338`).

Then, over a long weekend, the staff member pushes a menu update straight to the main branch of
the smaller repository her edits live in, without asking the nephew to look first, since nothing
stops her, she has Write access there. The update has a wrong price in it, and it sits live on the
ordering site for two days before anyone notices, over the café's busiest weekend of the year. That
is exactly the trigger the strategy pack names for moving up a level: a mistake that actually cost
them money and embarrassment, not a hunch (`STRATEGY-PACK.md:344`).

The nephew decides an enforced rule is worth it now. He opens that repository's Settings, creates
a ruleset named `protect-main`, sets its enforcement status to **Active**, targets the default
branch, and ticks **Require a pull request before merging** with one required approval. Because he
is the one who will occasionally need to push an urgent fix himself, he adds the **Repository
admin** role to the ruleset's bypass list before saving it, so he is not locked out of his own
emergency fixes.

From that point on, the staff member's menu edits go through a pull request instead of a direct
push. The nephew still glances at each one, the same habit as before, except now GitHub actually
enforces that a pull request happens, instead of relying on either of them to remember.

## If it goes wrong

**I created a ruleset and it does not seem to be doing anything.** Check its enforcement status
first. A brand-new ruleset starts **Disabled**, and a disabled ruleset enforces nothing at all,
this is the single most common reason a rule looks like it is not working. Open the ruleset and
switch it to **Active**.

**I am the repository owner and I cannot merge my own pull request anymore.** If you are using a
ruleset with required reviews and you did not add yourself or the repository admin role to its
bypass list, this is expected, not a bug, rulesets do not exempt anyone automatically. Open the
ruleset, add **Repository admin** to the bypass list (or get a second approval if you would rather
keep the review requirement genuinely enforced on yourself too), or, if you are using a branch
protection rule instead, this should not happen at all unless you deliberately ticked **Do not
allow bypassing the above settings**, check whether that is ticked.

**A push got rejected and I do not understand the message.** GitHub's rejection message names what
blocked it, either the rule (if it is a branch protection or ruleset issue) or the specific secret
pattern it detected (if it is push protection). Read the exact wording back, or paste it to Claude
Code and ask it to explain what it means, that is a genuinely good use of it, see the Claude Code
section above.

**I do not see the option to create a ruleset or a branch protection rule at all.** Confirm on
your own screen whether your repository is private and your plan is Free. Both mechanisms are free
on public repositories on any plan, but a private repository needs at least GitHub Pro, or GitHub
Team and above for an organization-owned repository, before the option appears.

## FAQ

**Do I need to protect my main branch if it is just me working alone?** Not really, and this kit
would not recommend it by default. Nobody else can push to your repository without Write access,
so there is nothing to enforce yet. It starts being worth considering the moment a second person
gets Write access to something that matters.

**Can I require a review and still merge my own work without one, on purpose?** Yes, and this is
normal, not a workaround. Branch protection rules exempt administrators automatically unless you
turn that off. Rulesets need you to deliberately add yourself, or the admin role, to the bypass
list. Either way, this is a documented, intended option, not a loophole you are not supposed to
use.

**Does turning on push protection mean my code is now scanned for every kind of secret?** No.
Push protection catches patterns GitHub recognizes as likely credentials at the moment you push.
It is not a guarantee nothing sensitive ever gets through, especially anything bypassed on purpose
or anything that does not match a recognized pattern. Treat it as a useful check, not a substitute
for never typing a real password or key into a file that gets committed in the first place.

**If I already accidentally pushed a secret, does deleting the file fix it?** No. `06-branches.md`
and this file both point the same way here: rotate the actual key or password in whatever service
issued it first, that is what actually closes the danger. Deleting the file in a new commit leaves
the old value sitting in your history regardless. Cleaning history is a separate job this kit does
not walk you through solo, bring it to the community if you get to that point.

**Can I use rulesets and branch protection rules on the same repository at the same time?** Yes,
GitHub's own wording is that they "work alongside each other, and all applicable rules are
enforced." It is simpler to pick one and stick with it for a given branch, but nothing breaks if
you end up with both.

**Does GitHub charge extra for rulesets or branch protection rules on their own?** Not on a public
repository, both are free on every plan there. On a private repository, you need at least GitHub
Pro for a personal account, or GitHub Team and above for an organization-owned repository, before
either one is available.

## Quick reference

- **Create a ruleset:** repository **Settings** > **Rules** > **Rulesets** > **New ruleset** >
  **New branch ruleset** > name it > set enforcement to **Active** > target your default branch >
  tick the rules you want > **Create**
- **Create a branch protection rule:** repository **Settings** > **Branches** > **Add rule** >
  branch name pattern (usually `main`) > tick the rules you want > **Create**
- **Require review before merge:** tick **Require a pull request before merging** plus **Require
  approvals**, then set how many
- **Add yourself to a ruleset's bypass list:** ruleset page > **Bypass list** > **Add bypass** >
  pick **Repository admin** > **Add Selected**
- **Block force pushes / restrict deletions:** both on by default in a new ruleset
- **Push protection:** on by default for public repositories; a paid feature to turn on for an
  organization's private repositories; check your own account setting at
  [**Security settings**](https://github.com/settings/security)
- **If a secret already leaked:** rotate the key at the service that issued it first, do not just
  delete the file
- **Through Claude Code:** it cannot set any of this up for you, but it can read a rejected push's
  error message and explain it

## Sources

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
- https://docs.github.com/en/code-security/concepts/secret-security/push-protection
- https://docs.github.com/en/code-security/secret-scanning/push-protection-for-users
- https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning
