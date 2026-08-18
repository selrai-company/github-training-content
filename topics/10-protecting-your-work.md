# Protecting the main copy, and what it costs

This file covers why you would stop people pushing straight to your default branch, the two ways
GitHub lets you enforce that (rulesets and the older branch protection rules, and which one this
kit reaches for today), requiring a review before a change can merge, what that actually costs a
small team versus what it buys, why a solo operator usually should not turn this on the way a team
does, and what push protection for secrets does and does not do.

If you haven't read `06-branches.md` and `07-pull-requests.md` yet, read those first. This file
assumes you already know what a branch and a pull request are.

Everything below happens in your browser. Setting these rules is an admin-only, signed-in-as-you
action, the same category as creating an organization or inviting a member, so it is not something
to hand to Claude Code, the same way this kit never hands it two-factor authentication or billing.

## Why you would stop people pushing straight to main

`06-branches.md` already covers the core idea: a branch is a photocopy, and the main copy stays
safe while people work on their own copies. GitHub's own reasoning for why that matters: "Rather
than modifying the default branch directly, you create a separate branch to develop features or
test ideas. This prevents your experimental or incomplete work from affecting the main codebase
that others depend on."

But a branch only protects your main copy if people actually use one. Nothing stops a collaborator
with Write access from committing straight to your default branch instead, by habit, by accident,
or because it's faster in the moment. The rules this file covers are how you make that impossible
rather than just discouraged: GitHub itself enforces the habit, instead of everyone having to
remember it.

**Who this actually matters for:** if you are the only person with Write access to a repository,
nobody else can push to your main copy anyway, so there is nothing to enforce yet. This starts
mattering the moment a second person gets Write access, and it matters more the more that
repository is something a customer, a client, or your whole business depends on.

## Two ways to enforce it: rulesets and branch protection rules

GitHub has two separate features that do this job. Both are real, both are documented, and as of
when this kit was checked, GitHub's own words are that they "work alongside each other, and all
applicable rules are enforced" if a repository has both. You won't usually run both at once, but
it's worth knowing neither one replaces the other automatically.

**Branch protection rules** are the older mechanism. GitHub's own definition: "You can protect
important branches by setting branch protection rules, which define whether collaborators can
delete or force push to the branch and set requirements for any pushes to the branch, such as
passing status checks or a linear commit history." One real limitation GitHub states plainly: "only
a single branch protection rule can apply at a time," which can get confusing once you have more
than one rule that might match the same branch.

**Rulesets** are the newer mechanism, and GitHub's own page on branch protection rules points
toward them directly: "For information about an alternative to branch protection rules, see About
rulesets." A ruleset does the same underlying job, plus a few things branch protection rules can't:
multiple rulesets can apply to the same branch at once (GitHub's own wording: "Multiple rulesets
can apply to the same branch at the same time, while only one branch protection rule applies"),
you can switch a ruleset off without deleting it and losing your setup, and anyone with read access
to the repository can see which rulesets are active, not just administrators.

**This kit recommends rulesets as the one to reach for today.** That's our recommendation, the same
way squash and merge is our recommendation in `07-pull-requests.md`, not GitHub declaring one
mechanism obsolete. Branch protection rules still work and are still documented. Rulesets are just
the more flexible option if you ever need a second rule, a temporary exception, or want to turn a
rule off for a week without rebuilding it from scratch.

**The tier claim, and it carries a real qualifier.** Both mechanisms are gated by plan the same
way, and the split is by whether the repository is public or private, not by whether you're on an
organization at all. GitHub's own wording for rulesets: "Rulesets are available in public
repositories with GitHub Free and GitHub Free for organizations, and in public and private
repositories with GitHub Pro, GitHub Team, and GitHub Enterprise Cloud." GitHub's own wording for
branch protection rules, stating the identical split: "Protected branches are available in public
repositories with GitHub Free and GitHub Free for organizations. Protected branches are also
available in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud,
and GitHub Enterprise Server." In plain terms: on a public repository, either mechanism is free, on
any plan. On a private repository, you need at least GitHub Pro (the paid personal plan) or, for an
organization-owned repository, GitHub Team or above. If your repository is private and you're on a
Free plan, confirm on your own screen whether the option to add a rule or ruleset even appears
before you plan around it, that's the fastest way to know where you actually stand.

## Setting up a ruleset that protects your default branch

**The click path:**

1. On the repository's main page, click **Settings**.
2. In the left sidebar, under "Code and automation," click **Rules**, then click **Rulesets**.
3. Click **New ruleset**.
4. Click **New branch ruleset**. (There's a separate **New tag ruleset** next to it, for tags
   instead of branches, not what you want here.)
5. Under "Ruleset name," type a name for it, something like `protect-main`.
6. Look for the enforcement status control near the top of the page. **A brand-new ruleset starts
   set to Disabled**, GitHub's own default, and a disabled ruleset enforces nothing at all. Click
   it and change it to **Active** once you're ready for the rule to actually apply, this is the
   single most common way a ruleset "doesn't work," it was never switched on.
7. In the "Target branches" section, click **Add a target**, then choose the option for your
   default branch specifically (this kit found it described in GitHub's own words as including
   "the default branch," worded close to **Include default branch** when this was last checked;
   if the exact wording on your screen differs slightly, pick whichever option clearly names your
   default branch rather than a text pattern).
8. Tick **Require a pull request before merging** (covered in more detail below), and any of the
   other rules you want, then click **Create** near the bottom of the page.

**Confirmation:** the ruleset now appears in your Rulesets list, marked Active, and if you try to
push straight to your default branch from the command line (or ask Claude Code to do it for you),
the push is rejected with a message naming the ruleset that blocked it.

**Screenshot placeholder:** the ruleset creation page, showing the "Ruleset name" field, the
enforcement status control near the top, and the "Target branches" section with an "Add a target"
button, so a reader can match each field to the steps above before creating one.

## The older way, if you'd rather use it

**The click path for a branch protection rule:**

1. On the repository's main page, click **Settings**.
2. In the left sidebar, under "Code and automation," click **Branches**.
3. Under "Branch protection rules," click **Add rule**.
4. Under "Branch name pattern," type your default branch's name (usually `main`).
5. Under "Protect matching branches," tick **Require a pull request before merging**, and any
   other rules you want.
6. Click **Create** near the bottom of the page.

**Confirmation:** the rule appears under "Branch protection rules" on that same Settings page,
listing the branch pattern it covers.

Nothing is wrong with picking this over a ruleset. It's a smaller page with fewer moving parts, and
for a single rule on a single branch, that simplicity is a real advantage, not a compromise.

## Requiring a review before a change can merge

This is the single most consequential rule either mechanism offers, and it's the one that answers
what `07-pull-requests.md` already flagged: without it, "Request changes" on a pull request is
"purely informational and will not prevent merging." With it turned on, that stops being true.

**What ticking it actually does.** GitHub's own wording: "You can require that all changes to the
target branch be associated with a pull request," and once you also require approvals, "Repository
administrators or custom roles with the 'edit repository rules' permission can require that all
pull requests receive a specific number of approving reviews before someone merges the pull request
into a protected branch." In the click path above, that's the **Require approvals** option, with a
**Required number of approvals before merging** dropdown where you pick how many.

Two options worth knowing sit right alongside it, both optional: **Dismiss stale pull request
approvals when new commits are pushed** (GitHub's own wording: dismisses an existing approval "when
commits are pushed that affect the diff in the pull request," so an approval can't quietly cover a
change made after it was given), and **Require review from Code Owners**, which only does anything
if your repository has a CODEOWNERS file naming specific people for specific paths, most small
repositories in this kit's audience won't have set one up.

**What this costs, in plain terms.** Every change now has to wait for someone else to look at it
before it can land. If that someone is slow, on leave, or asleep in a different timezone, your
change waits too. There's no "just this once" override once the rule is on, unless you've deliberately
built one in (covered next), and that's the entire point of turning it on in the first place.

**When it's worth that cost, and when it isn't.** It's worth it the moment a mistake landing in
your main copy would actually cost you money, a client relationship, or hours of cleanup, and more
than one person can push to that repository. It is very often not worth it for a two-person shop
where an informal "glance at it before you merge" habit produces the same outcome nearly every
time, without the subscription cost or the waiting. `STRATEGY-PACK.md`'s section on how much
process is the right amount walks through this trade-off in full, with a size-by-size ladder, if
you want to think it through properly before deciding.

**Do not oversell this to yourself if you're a solo operator.** If you are the only person who will
ever push to a given repository, requiring a review before merge doesn't add safety, it adds a step
where you'd otherwise need a second person, or yourself, to approve your own change before it can
land. Whether that locks you out of your own work depends on which mechanism you used, and this is
worth getting right before you turn either one on:

- **Branch protection rules exempt administrators by default.** GitHub's own wording: "By default,
  the restrictions of a branch protection rule don't apply to people with admin permissions to the
  repository or custom roles with the 'bypass branch protections' permission." As the owner of your
  own repository, you're an administrator, so a required review under this mechanism won't actually
  block you unless you separately tick **Do not allow bypassing the above settings**, which exists
  specifically for someone who wants to hold themselves to the same rule as everyone else.
- **Rulesets do not exempt anyone automatically.** GitHub's own wording: "When you create a ruleset,
  you can allow certain users to bypass the rules in the ruleset," meaning nobody bypasses unless
  you deliberately add them. If you create a ruleset requiring a review and don't add yourself (or
  the repository admin role) to its bypass list, you genuinely can lock yourself out of merging your
  own solo work. If you want a ruleset with required reviews but don't want that risk, add
  **Repository admin** as a bypass actor when you create it: in the "Bypass list" area of the
  ruleset page, click **Add bypass**, search for the role, team, or app you want, select it, and
  click **Add Selected**.

## Other rules worth knowing about while you're on this page

Both mechanisms offer more than just required reviews. Two are worth naming because they're
directly about protecting the branch itself, and, under rulesets, both come switched on by default:

- **Block force pushes.** GitHub's own wording: "You can prevent users from force pushing to the
  targeted branches or tags. This rule is enabled by default." A force push can silently overwrite
  history other people are relying on, so leaving this on is rarely the wrong call.
- **Restrict deletions.** GitHub's own wording: "If selected, only users with bypass permissions
  can delete branches or tags whose name matches the pattern you specify. This rule is selected by
  default." This is what stops your default branch itself from being deleted by mistake.

There are others (required status checks, a linear history requirement, signed commits, and more)
that go beyond what a small business typically needs on day one. This kit isn't walking through
every one of them here, that would be exactly the kind of theory-first detour this kit's own
members have already said not to do. Turn on what solves a problem you actually have, and revisit
the list on your own screen if a specific need comes up later.

## Push protection for secrets, and its real limits

This is a different feature from everything above, it isn't about who can merge, it's about
stopping a password or an API key from ever reaching GitHub in the first place. It's worth knowing
briefly, because it's easy to assume it does more than it does.

**What it is.** GitHub's own wording: "Push protection is a secret scanning feature designed to
prevent hardcoded credentials, such as secrets or tokens, from ever being pushed to your
repository." GitHub's own list of where it steps in: "Push protection blocks secrets detected in:
Pushes from the command line, Commits made in the GitHub UI, File uploads to a repository on
GitHub, Requests to the REST API, Interactions with the GitHub MCP server (public repositories
only)." When it catches something, GitHub's own wording is direct: "it will block the push and
provide a detailed message explaining the reason for the block."

**It has a bypass, and that's real, not a bug.** GitHub's own wording: "For push protection for
repositories, by default, anyone with write access to the repository can bypass push protection by
specifying a bypass reason." So push protection is a prompt to stop and check, not an absolute
wall, someone in a hurry who's confident the flagged text isn't really a secret can push past it.

**Where it applies by default, and this is the same public-versus-private split as everything
else in this file.** GitHub's own wording, on public repositories: "Secret scanning runs
automatically for free." On an organization-owned private or internal repository, it's a paid
feature you have to turn on: "Available with GitHub Secret Protection enabled on GitHub Team or
GitHub Enterprise Cloud." There's also a separate, personal setting on your own GitHub account,
covering pushes you make to public repositories specifically, and GitHub's own wording for that one
is: "Push protection for users is on by default for public repositories." Confirm your own account's
setting under your account's security settings if you want to know exactly where you stand, this
kit couldn't pin down the precise sidebar wording for that specific toggle.

**What it does not do, and this is the part worth remembering.** Push protection only looks at what
you're pushing right now. It does nothing about a secret that's already sitting in your repository's
history from before it was turned on, or one that got through because someone bypassed it. If a
secret is already out, the fix isn't push protection and it isn't rewriting history yourself either,
rotate the key in whatever service issued it first, that closes the actual danger regardless of how
many old commits still mention the leaked value. Cleaning up the history afterwards is a separate,
harder job this kit deliberately doesn't walk you through solo.

## Doing this through Claude Code

You won't. Creating a ruleset or a branch protection rule, and turning on push protection, are all
signed-in-as-you actions on GitHub's own settings screens, the same category as creating an
organization or inviting a member. Claude Code can run git commands on your behalf, but it can't
click a settings toggle that needs GitHub to see you specifically. If you ask it to "protect my main
branch," the right answer from it should be to walk you to this page, not to attempt the setting
itself.

What Claude Code *can* usefully do here: if a push it just tried to make on your behalf gets
rejected by a rule or by push protection, it will see GitHub's own rejection message and can explain
it back to you in plain English, including which rule or which detected secret caused it. That's a
genuinely good use of it, reading an error is exactly the kind of thing worth handing over.

---

## If it goes wrong

**I created a ruleset and it doesn't seem to be doing anything.** Check its enforcement status
first. A brand-new ruleset starts **Disabled**, and a disabled ruleset enforces nothing at all,
this is the single most common reason a rule looks like it isn't working. Open the ruleset and
switch it to **Active**.

**I'm the repository owner and I can't merge my own pull request anymore.** If you're using a
ruleset with required reviews and you didn't add yourself or the repository admin role to its
bypass list, this is expected, not a bug, rulesets don't exempt anyone automatically. Open the
ruleset, add **Repository admin** to the bypass list (or get a second approval if you'd rather keep
the review requirement genuinely enforced on yourself too), or, if you're using a branch protection
rule instead, this shouldn't happen at all unless you deliberately ticked **Do not allow bypassing
the above settings**, check whether that's ticked.

**A push got rejected and I don't understand the message.** GitHub's rejection message names what
blocked it, either the rule (if it's a branch protection or ruleset issue) or the specific secret
pattern it detected (if it's push protection). Read the exact wording back, or paste it to Claude
Code and ask it to explain what it means, that's a genuinely good use of it, see above.

## Questions people ask here

**Do I need to protect my main branch if it's just me working alone?** Not really, and this kit
wouldn't recommend it by default. Nobody else can push to your repository without Write access, so
there's nothing to enforce yet. It starts being worth considering the moment a second person gets
Write access to something that matters.

**Can I require a review and still merge my own work without one, on purpose?** Yes, and this is
normal, not a workaround. Branch protection rules exempt administrators automatically unless you
turn that off. Rulesets need you to deliberately add yourself (or the admin role) to the bypass
list. Either way, this is a documented, intended option, not a loophole you're not supposed to use.

**Does turning on push protection mean my code is now scanned for every kind of secret?** No.
Push protection catches patterns GitHub recognizes as likely credentials at the moment you push.
It's not a guarantee nothing sensitive ever gets through, especially anything bypassed on purpose
or anything that doesn't match a recognized pattern. Treat it as a useful check, not a substitute
for simply not typing a real password or key into a file that gets committed in the first place.

**If I already accidentally pushed a secret, does deleting the file fix it?** No. `06-branches.md`
and this file both point the same way here: rotate the actual key or password in whatever service
issued it first, that's what actually closes the danger. Deleting the file in a new commit leaves
the old value sitting in your history regardless. Cleaning history is a separate job this kit
doesn't walk you through solo, bring it to the community if you get to that point.

**Can I use rulesets and branch protection rules on the same repository at the same time?** Yes,
GitHub's own wording is that they "work alongside each other, and all applicable rules are
enforced." It's simpler to pick one and stick with it for a given branch, but nothing breaks if you
end up with both.

---

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
