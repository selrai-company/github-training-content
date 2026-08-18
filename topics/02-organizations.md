# Organizations, and when you actually need one

## What this gets you

An organization moves your repositories off your own personal account and onto a shared
account your business controls together. The practical payoff: when a second person needs
ongoing access to your code, granting and revoking that access lives in one place, and it
keeps working even on the day you are unreachable, on leave, locked out, or gone. Without an
organization, every repository's access sits with whichever personal account created it, and
that one person becomes a single point of failure for the whole business. Most solo owners do
not need this yet. The moment a second person needs standing access, this page is what fixes
that.

## Before you start

**You need a personal GitHub account already set up and signed in.** An organization sits on
top of your personal account, not instead of it. `01-accounts-and-security.md` covers creating
one and turning on two-factor authentication, which you should already have done.

**You do not need a repository yet.** An organization can be created with nothing in it. If you
already have a repository under your personal account that you plan to move in later, note
which one, the section on transferring a repository below covers moving it across once your
organization exists.

**Decide, honestly, whether you have actually hit the trigger for this at all.** The short
version: a second person needs ongoing, standing access to your code. If that is not true yet,
skip this page and come back the day it is. The full reasoning, including what a solo operator
should do instead, is under Strategy below.

**Nothing here needs Claude Code or a terminal to complete.** Creating, naming, and deleting an
organization are account and billing actions tied to your own identity, and they only happen in
your browser, signed in as yourself. A couple of the read-only checks further down do have a
faster path through Claude Code, and those are called out where they apply.

## The words you need

**Personal account.** Your own GitHub account, the one with your name and your face on it. Only
you can sign in to it, and anything you do with it, a commit, a comment, a repository you
create, is attributed to you.

**Organization.** A separate, shared account that sits above personal accounts. Nobody signs in
to an organization directly. People sign in with their own personal accounts and are given
access to it. GitHub's own words for this: organizations are "shared accounts where a large
number of people can collaborate across many projects at once" (see Sources). Think of it like
the difference between your own personal email address and a shared company inbox. The company
inbox is not a person. People with the right permission can open it, but it does not belong to
any one of them, and it does not disappear if one person leaves.

**Repository.** The project itself, your code, files, and their full history, always living
inside exactly one account, either a personal account or an organization, never floating free.
`04-repositories-and-visibility.md` covers creating and configuring one in full. What matters
here is only that a repository has to live somewhere, and moving it between a personal account
and an organization is the "transfer" covered further down this page.

**Owner.** The role with complete administrative control over an organization: billing, every
repository, every member's access, the works. Every organization needs at least one owner from
the moment it exists.

**Member.** Someone who belongs to the organization itself, with a role and a level of access
GitHub tracks for them individually. Being a member is different from having access to just one
repository, covered next.

**Outside collaborator.** Someone given access to one or more of an organization's specific
repositories without being made a full member of the organization itself. `03-members-and-access.md`
covers the difference in full and how to add one. The short version worth knowing here: an
outside collaborator cannot use the "leave an organization" flow described below, because they
were never inside it to begin with. Removing their own access means removing themselves from
the specific repository, not from an organization.

**Plan.** The tier an organization is billed on: **GitHub Free**, **GitHub Team**, or **GitHub
Enterprise Cloud**, each unlocking more features and support than the last. Every organization
starts on Free automatically. What each tier actually includes is covered below.

**Seat, sometimes called a license.** A paid slot for one person, on a paid plan. On GitHub Free
this never comes up. On Team or Enterprise, GitHub's own wording is direct: "an unused license
must be available before you can invite a new member."

**Billing manager.** A role GitHub offers, separate from being an organization owner, for
someone who manages payment on the organization's behalf. This page does not walk through
setting one up. Confirm the option on your own organization's billing settings if you plan to
use it.

**Transfer.** Moving an existing repository from one account into another, personal account to
organization or the other way around, while keeping its full history, issues, and pull requests
intact. It is a specific, named action on GitHub, not the same as deleting the old copy and
creating a fresh one.

## How to do it

### Creating an organization: the exact click path

This is a browser-only step. There is no GitHub CLI command for creating an organization
(confirmed by running `gh org --help`, which lists exactly one subcommand, `list`, nothing for
creating one) and no Claude Code shortcut, because this is an account and billing action tied to
your own identity. Do this yourself, signed in as you, in your browser.

1. **Landmark:** start from any page on github.com while signed in.
   **Path:** in the top right corner, click your **profile picture**.
   **Confirmation:** a dropdown menu opens, your username at the top and a list of links below
   it.
2. **Path:** near the bottom of that dropdown, click **Settings**.
   **Confirmation:** you land on your own account Settings page, with a list of setting groups
   running down the left-hand side.
3. **Path:** in that left sidebar, under the **Access** heading, click **Organizations**.
   **Confirmation:** the page shows a heading that reads "Organizations," listing any you
   already belong to, empty if you belong to none yet.
   **Direct address**, since this exact page looks the same for every signed-in reader:
   `https://github.com/settings/organizations`. Going there skips steps 1 through 3.
4. **Path:** next to the "Organizations" heading, click **New organization**.
   **Confirmation:** GitHub shows you a plan-comparison screen, Free, Team, and Enterprise
   Cloud, before it asks for any setup details.
5. Follow the on-screen prompts to finish setup.

GitHub's own step-by-step for this stops exactly there: it tells you to "follow the prompts,"
but does not publish the exact list of fields on the page (organization name, contact email,
personal-or-business option, and so on). That is normal. It means the screen in front of you is
the authority, not this page. **Confirm on your own screen** what fields it actually asks for at
the moment you create yours, and fill them in with your own real details.

**Screenshot placeholder:** the "New organization" screen from GitHub, whatever fields it
currently asks for, so a reader can match what they see to this step.

**Fallback, if "New organization" is not there at all:** confirm you are signed in with your own
personal account (look for your profile picture in the top right). A fresh or half-finished
account sign-up can hide this option until your account itself is fully verified. If it is still
missing after that, your account status pages, under Settings, will say if anything needs
attention first.

**What if I already answered a plan question during setup?** GitHub's plans page for
organizations exists specifically so you can compare options before or during that step.
Whatever you pick, you can change it later from the organization's own settings. Picking Free to
start is not a one-way door.

### Checking which organizations you belong to, and your role in each

**In the browser:** the `https://github.com/settings/organizations` page above lists every
organization tied to your signed-in account. Open any one of them, then its **People** tab, and
your own role is listed right next to your name.

**Through Claude Code, if you already have the GitHub CLI (`gh`) installed and signed in** (the
same one-time setup covered in `04-repositories-and-visibility.md` and `05-daily-workflow.md`):

```
gh org list
```

This lists every organization on your account, one per line, without opening a browser tab.
Tested this session against a real signed-in account: it returned exactly what the equivalent
browser page showed.

To check your own role inside one specific organization:

```
gh api orgs/YOUR-ORGANISATION/memberships/YOUR-GITHUB-USERNAME
```

The reply is a block of raw technical data (JSON) with a `role` field in it. Read that field for
your own standing. This kit's own test run of that command returned `"role":"member"` for a
non-owner account; what value appears there for an owner is worth confirming once against what
the People tab shows you, rather than guessing from this page.

### Which plan you land on

A brand new organization is created on **GitHub Free**, automatically, at no cost. GitHub's own
account-types page states it plainly: "You can use organizations for free, with GitHub Free,
which includes limited features on private repositories."

On GitHub Free, per GitHub's own plans comparison page, an organization gets:

- Unlimited collaborators on unlimited public repositories, with the full feature set.
- Unlimited private repositories too, but with a **limited** feature set on those private repos.
- 2,000 GitHub Actions minutes a month.
- Community support (GitHub's public forums and documentation, not a private support ticket
  line).

To get the full feature set on private repositories, plus things like required pull request
reviewers and a security overview, you would upgrade to **GitHub Team**. Team also raises the
Actions minutes to 3,000 a month and adds email support. Above that sits **GitHub Enterprise
Cloud**, aimed at much larger companies, with single sign-on, centrally managed policy across
multiple organizations, and far higher usage limits.

**A note on price, stated carefully:** at the time of writing, GitHub's pricing page lists
GitHub Team at $4 USD per user per month **for the first 12 months**, and GitHub Enterprise
Cloud starting at $21 USD per user per month **for the first 12 months**. Both prices carry an
asterisk on GitHub's own pricing page pointing to an introductory-rate footnote. What the price
becomes after those first 12 months is not stated anywhere on that page. Confirm the current
renewal price on GitHub's own pricing page before you commit to a paid plan. Do not assume the
introductory number is the number you will pay in year two.

### Naming your organization

GitHub does not publish a specific naming-rules page for organization names on the screen that
walks through creation. Pick a name your team will recognize, often the business name, with no
spaces, since GitHub account names generally do not allow spaces. If the exact name you want is
taken, you will be told so on screen, and you will need a variation. **Confirm the exact rules
and any error message on your own screen** when you get there. That page is the authority, not
this one.

**You can rename an organization later.** Only organization owners can do it.

1. **Landmark:** from your organization's own page.
   **Path:** click **Settings**.
   **Confirmation:** the organization's own settings page opens, a list of setting groups down
   the left-hand side, similar in shape to your personal Settings page but scoped to the
   organization.
2. **Path:** scroll to the bottom, to the **Danger zone**.
3. **Path:** click **Rename organization**.
4. **Path:** click **I understand, let's rename my organization** to confirm.
5. **Path:** type the new name, then click **Change organization's name**.

Three things to know before you do this:

- Most links to your existing repositories keep working. GitHub automatically redirects them to
  the new name.
- Your **old organization's profile page** (the one people bookmark or share) stops working and
  shows a 404 once the rename goes through. That is expected, not a sign anything else broke.
- The old name becomes available for someone else to claim once you have moved off it, so do not
  rename and expect to "come back to" the old name later.

### Adding a second owner (do this early, not eventually)

GitHub's own guidance is specific and worth repeating word for word: the owner role "should be
limited, but to no less than two people, in your organization." A separate GitHub page on
keeping ownership continuous is blunter about why: "If an organization only has one owner, the
organization's projects can become inaccessible if the owner is unreachable."

Read that plainly. If you are the only owner and something happens to your access, you lose
your two-factor device, your password reset email goes to an inbox you no longer check, your
account gets locked for any reason, there is nobody left with the authority to fix it, recover
it, or even grant someone else access. GitHub's published documentation does not describe an
emergency override for this situation. Treat "add a second owner" as a day-one task, not a
someday task.

**Whoever runs the setup screen above ends up holding owner-level control once the organization
exists.** This page could not find a single sentence in GitHub's own documentation stating that
outright as a guarantee, so treat it as something to confirm rather than something to assume.
The moment your organization exists, check: open its **People** tab, and your role is listed
right next to your name (or use the `gh api` check in the section above).

**To promote an existing organization member to owner:**

1. **Landmark:** any github.com page, signed in.
   **Path:** click your **profile picture** (top right), then **Settings**, then, in the
   **Access** section of the sidebar, **Organizations**. (Or go straight to
   `https://github.com/settings/organizations`.)
2. **Path:** click your organization's name.
3. **Path:** click the **People** tab.
   **Confirmation:** a list of everyone with access to the organization appears, with their
   current role shown next to each name.
4. **Path:** tick the checkbox next to the person you want to promote.
5. **Path:** above the member list, open the **"X members selected..."** dropdown and click
   **Change role**.
6. **Path:** choose the new role, then click **Change role** again to confirm.
   **Confirmation:** their role next to their name updates immediately.

**If that second person is not in the organization yet, invite them first:**

1. Organization page, **People** tab, **Invite member**.
2. Enter their username, full name, or email address, then click **Invite**.
3. Pick their organization role on the invite screen itself. You can invite them straight in as
   an owner, or as a member and promote them later using the steps above.
4. Click **Send invitation**.

They will get an emailed invite link. If they do not accept it within seven days, the invite
expires automatically and you will need to send a new one.

**One billing note if you are on a paid plan (Team or Enterprise, not Free):** GitHub's own docs
state that "if your organization has a paid per-user subscription, an unused license must be
available before you can invite a new member." On Free this is never a concern. On a paid plan,
adding your second owner may need a paid seat, the same as adding anyone else.

### Transferring an existing repository into your organization

If you already have a repository sitting under your personal account and you want it living
inside your new organization instead, you move it with a **transfer**, not by re-creating it
from scratch. History, issues, pull requests, the wiki, stars, and watchers all move with it.

This is also a browser-only step. There is no GitHub CLI (`gh`) command for transferring
repository ownership. Confirmed this session: neither the general `gh repo --help` command list
nor the `gh org --help` command list includes anything named "transfer." It is a web-interface-
only action.

1. **Before you start this one:** you need **administrator access** to the repository you are
   moving, and permission to create a repository inside the target organization.
2. **Landmark:** open the repository's main page.
   **Path:** click its **Settings** tab.
   **Confirmation:** the repository's own settings page opens.
   For any repository you administer, the direct pattern is
   `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings` (use your own personal
   username in place of YOUR-ORGANISATION if the repository still sits under your personal
   account at this point). Replace both placeholders with your own names, this address is never
   a working link as written.
3. **Path:** scroll to the bottom, to the **Danger Zone**.
4. **Path:** click **Transfer**.
   **Confirmation:** a form appears asking for the new owner.
5. **Path:** under "New owner," choose **Select one of my organizations** and pick your
   organization from the dropdown.
6. Optionally give the repository a new name at the same time. This option only appears if you
   are an owner of the destination organization.
7. **Path:** type the repository's name to confirm, then click **I understand, transfer this
   repository**.
   **Confirmation:** the repository's page reloads under its new address, showing your
   organization's name where your personal account name used to be.

A few things that survive the move automatically, straight from GitHub's own documentation:
webhooks, services, secrets, and deploy keys all stay attached after the transfer completes.
Links to the old location redirect to the new one. One detail worth knowing about issues
specifically: if you are moving from a personal account into an organization, any issue assigned
to someone who is a member of that organization keeps its assignee. Every other issue assignment
gets cleared, because that person may not have access to the repository's new home.

**Screenshot placeholder:** the "Danger Zone" section of a repository's Settings page, with the
"Transfer" button visible, so the reader can see exactly where this lives.

### Leaving an organization

This section is for organization **members**. If you are an outside collaborator on one of an
organization's repositories rather than a full member, this flow does not apply to you, remove
your own access from the specific repository instead, or ask whoever manages it to do so
(`03-members-and-access.md` covers that).

If you are a member and you want out, you can leave at any time, without asking anyone's
permission.

1. **Landmark:** click your **profile picture** (top right), then **Settings**.
2. **Path:** in the **Access** section of the sidebar, click **Organizations**. (Or go straight
   to `https://github.com/settings/organizations`.)
3. **Path:** next to the organization, click **Leave**.
   **Confirmation:** the organization no longer appears in your list on that page.

**One important gap to know about before you do this:** if you are the person currently
responsible for paying for the organization, leaving does **not** hand billing off to anyone
else. GitHub's own wording is direct: leaving "does not update the billing information on file
for the organization," and if you are currently responsible for billing, "you must have another
owner or billing manager for the organization update the organization's payment method" first.
Sort out who is paying before you click Leave, not after.

### Deleting an organization entirely

This is different from leaving. Deleting removes the organization for everyone, permanently.

GitHub is explicit that this is irreversible: deleting "permanently removes all repositories,
forks of private repositories, wikis, issues, pull requests, and project or organization pages."
Billing for the organization ends. Once deleted, the organization's name is locked for 90 days
before it becomes available for anyone, including you, to claim again.

**Back up anything you want to keep before you start.** GitHub's own advice is the same: make
sure you have a copy of every repository, wiki, issue, and project first.

1. **Landmark:** click your **profile picture** (top right), then **Organizations**, then select
   the organization.
2. **Path:** open its **Settings** (or via the **More** dropdown if you do not see a direct
   tab).
3. **Path:** scroll to the **Danger zone**.
4. **Path:** click **Delete this organization**.
5. **Path:** type the organization's name to confirm, then click **Cancel plan and delete the
   organization**.
   **Confirmation:** you are returned to your account's organization list, and this organization
   no longer appears in it.

**Confirm on your own screen exactly who is allowed to see and click this button** before you
rely on it as a safeguard. The fetched documentation walks through the steps but does not spell
out the permission requirement on that specific page. In practice, treat it as an owner-only
action, and do not hand owner access to anyone you would not trust with this button.

## Strategy: how to actually use this

**Do you actually need one yet? Honestly, probably not, if you are working alone.** A personal
account already does everything covered in the rest of this kit: repositories, history, access
control on individual repos. Creating an organization on top of that adds nothing for a solo
operator except one more thing to keep secure.

**The one signal that means you now need one:** a second person needs to push code into your
repositories, on an ongoing basis, and you want that access to survive even if you are not
around to grant it repo by repo. That is the real trigger. Not "I want this to look more
professional." Not "I have a business name." It is specifically about sharing access to code
with other people in a way that keeps working when people join, leave, or change roles.

**A solo operator with no plans to bring anyone else onto the code should skip this page
entirely, for now.** Create your repositories under your personal account, and revisit this the
day you actually have a second person to add. Nothing here needs deciding in advance.

**Two or three people, one of them the technical one, is where this earns its keep
immediately.** Create the organization as soon as a second person's access needs to outlast any
single day you might be unreachable, and add that second owner the same session you create it,
not later once you remember to. At this size, an informal review habit, someone glancing at a
change before it goes live, usually does the job. A paid plan's enforced review rule buys a team
this small very little over what they already do by habit.

**Once you are past three or four people, individual per-repository access starts costing real
upkeep.** That is the point where teams, GitHub's way of granting the same access to a group at
once instead of person by person, become worth setting up. `03-members-and-access.md` covers
teams in full. It is also the point worth reviewing your organization's base permission setting
(also covered there), since a default that made sense for three people can quietly over-grant
access once you are past six or eight.

**Do not reach for a paid plan because of headcount.** The concrete reason to move from Free to
Team is wanting a required check, a mandatory reviewer, before a change lands on your main
version. That is a real decision with a real trigger. "We might grow" or "more storage, just in
case" is not a reason, it is a subscription you have not used yet.

**What would change my mind about staying on Free:** the day someone other than the person who
wrote a change is the only thing standing between a mistake and it going live for customers.
That is the moment an enforced reviewer earns its monthly cost. Before that day, it is a rule
enforcing a habit you already have.

**What good looks like months later:** two or more current owners, not one who meant to add a
second and never got to it. No member sitting on a paid seat nobody remembers assigning. A
People tab you could hand to a new hire and have them understand who does what without asking.
None of that happens by default, it happens because someone checked it once a quarter, roughly
the same discipline as reviewing who has a key to the office.

## A worked example

A café owner runs an online ordering site. Her nephew built it, under his own personal account,
and keeps it running. A staff member updates the menu text and opening hours from time to time.
This is the same team of three described in the strategy pack for this kit.

The ordering site starts to matter enough that the owner does not want its future tied to one
person's personal account, her nephew's, especially since he travels for weeks at a time and is
not always reachable. She creates an organization for the business, following the click path
above. Straight after, on the same visit, she adds her nephew as the second owner, since he is
the one who will actually use the organization's admin tools day to day, and GitHub's own
guidance against a lone owner is exactly the risk she is trying to avoid.

Her nephew then transfers the ordering site's existing repository, the one he originally built
under his own personal account, into the new organization, using the Transfer steps above. He
needed administrator access to that repository to do it, which he already had, since he built
it. The repository's history, every commit, every past issue, moves with it. Its address changes
from his personal account's name to the organization's name, and GitHub keeps the old address
redirecting so nothing that already linked to it breaks.

The staff member is not made an organization member at all, since her only job is editing menu
text, not administering anything. She is added directly to the specific repository that holds
the menu content, with Write access there and Read on the main site so she can see what it does,
a decision covered in full in `03-members-and-access.md`.

Three months later, the nephew is travelling and unreachable for a week when the site needs an
urgent fix. Because the owner is also a full owner of the organization, not just a member, she
can grant a contractor temporary access herself, on the spot, without waiting for him. That is
the entire reason the organization exists.

## If it goes wrong

**"New organization" is not there, or I cannot create one.** Confirm you are signed in with your
own personal account first (check for your profile picture in the top right). Organization
creation is tied to your personal account, so a fresh or half-finished sign-up can hide this
option until your account itself is fully verified. If it is still missing after that, GitHub's
own account-status pages (under Settings) will tell you if anything about your account needs
attention first.

**I created the organization alone and I am worried about being locked out.** Add a second owner
today, using the steps above, before you do anything else with the organization. This is the
single most avoidable failure on this page: GitHub's own guidance says never run an organization
with only one owner, and there is no documented emergency recovery path if that one owner loses
access.

**I invited someone and nothing happened.** Ask them to check their spam or promotions folder,
invitation emails land there often. If it has genuinely been more than seven days, the invite has
expired automatically and you just need to send it again from the People tab.

**I renamed my organization, and now a bookmark to its old page shows a 404.** That is expected,
not a fault. GitHub redirects links to your repositories automatically after a rename, but the
organization's own old profile page is not one of them. Update any bookmark you were relying on
to the new name.

**I am the one who currently handles billing, and I want to leave.** Sort this out before you
click Leave, not after. Leaving does not transfer billing responsibility to anyone else
automatically. Either hand billing to another owner or a billing manager first, or confirm on
your organization's own billing settings page what happens if you do not.

## FAQ

**Does creating an organization make me its owner automatically?** Confirm this on your own
screen rather than assuming it from this page. Whoever runs the setup flow above does end up
with owner-level control in practice, but this kit could not find a single sentence in GitHub's
own documentation guaranteeing it outright. Check your own role on the organization's People page
once it is created, right next to your name, or use the `gh api` check earlier on this page.

**Can I turn my personal account into an organization, or the other way around?** This page only
covers creating a brand new organization and moving individual repositories into one. Converting
an existing personal account into an organization, or an organization back into a personal
account, is a different, more involved process. Confirm directly on GitHub's own documentation
before attempting anything like that. It is not covered here.

**If I am on GitHub Free, is my private code actually private?** Yes. "Limited features" on Free
means things like required reviewers and advanced security tooling are not available, not that
privacy itself is reduced. A private repository on Free is still private.

**What happens to my organization's paid seats if I remove someone?** That question sits outside
what this page covers, it is a billing and member-management detail, not an organization-level
setup step. Confirm current seat behavior on your own billing settings page before assuming
either way.

**Can I belong to more than one organization, and to my own personal account, at the same time?**
Yes. Nothing about how GitHub accounts work ties you to just one. The `gh org list` command
earlier on this page will show you every organization tied to your account, one per line, if
there is more than one.

**What is the difference between leaving an organization and being removed from one?** This page
only covers leaving voluntarily, of your own choice, at any time. Being removed by an owner is a
different action they take, covered in `03-members-and-access.md`, not something you trigger from
here.

**Do I need to install anything to do any of this?** No. Every step on this page happens in your
browser, signed in to github.com. Creating, naming, and deleting an organization use no terminal
and no Claude Code, because these are account and billing actions tied to your own identity, and
GitHub does not offer a command-line shortcut for most of them anyway. Transferring a repository,
for example, has no `gh` CLI command at all, confirmed this session.

## Quick reference

- **Check your organizations:** `https://github.com/settings/organizations`, or `gh org list`
  through Claude Code
- **Create one:** profile picture, **Settings**, **Organizations**, **New organization**, follow
  the prompts (browser only)
- **Check your role:** organization's **People** tab, or `gh api orgs/YOUR-ORGANISATION/memberships/YOUR-GITHUB-USERNAME`
- **Rename:** organization **Settings**, **Danger zone**, **Rename organization**
- **Add a second owner:** organization **People** tab, tick their name, **Change role**, choose
  owner
- **Invite someone new:** organization **People** tab, **Invite member**
- **Transfer a repository in:** repository **Settings**, **Danger Zone**, **Transfer**, pick the
  organization
- **Leave:** `https://github.com/settings/organizations`, **Leave** next to the organization
  (members only, sort out billing first if that is you)
- **Delete entirely:** organization **Settings**, **Danger zone**, **Delete this organization**,
  type the name to confirm (irreversible, back up first)

## Sources

- https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts
- https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch
- https://docs.github.com/en/get-started/learning-about-github/githubs-plans
- https://github.com/pricing
- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization
- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/maintaining-ownership-continuity-for-your-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization
- https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization
- https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository
- https://docs.github.com/en/account-and-profile/how-tos/organization-membership/removing-yourself-from-an-organization
- https://docs.github.com/en/organizations/managing-organization-settings/deleting-an-organization-account
