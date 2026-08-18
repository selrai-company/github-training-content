# Organizations, and when you actually need one

## What an organization actually is

Your normal GitHub account (the one with your name and your face on it) is a **personal account**. Only you can sign in to it. Anything you do with it (a commit, a comment, a repository you create) is attributed to you.

An **organization** is a separate, shared account that sits above your personal account. Nobody signs in to an organization directly. Instead, people sign in with their own personal accounts and are given access to the organization. GitHub's own words for this: organizations are "shared accounts where a large number of people can collaborate across many projects at once" (see Sources).

Think of it like the difference between your own personal email address and a shared company inbox. The company inbox isn't a person. People with the right permission can open it, but it doesn't belong to any one of them, and it doesn't disappear if one person leaves.

**Screenshot placeholder:** a browser tab open on github.com, with the profile picture menu open showing "Your organizations" and a personal account name side by side, so a reader can see the visual difference between the two.

## Do you actually need one yet?

Honestly: probably not, if you're working alone.

If it's just you, a personal account already does everything you need. You get repositories, you get history, you get everything covered in the rest of this kit. Creating an organization on top of that adds nothing for a solo operator except one more thing to keep secure.

**The one signal that means you now need one:** a second person needs to push code into your repositories, on an ongoing basis, and you want that access to survive even if you're not around to grant it repo by repo.

That's the real trigger. Not "I want this to look more professional," not "I have a business name." It's specifically about sharing access to code with other people in a way that keeps working when people join, leave, or change roles. A solo owner with no plans to bring anyone else onto the code doesn't need this step. Skip it until the day you actually have a second person to add.

## What a new organization plan lands on

A brand new organization is created on **GitHub Free**, automatically, at no cost. GitHub's own account-types page states it plainly: "You can use organizations for free, with GitHub Free, which includes limited features on private repositories." (See Sources.)

On GitHub Free, an organization gets, per GitHub's own plans comparison page:

- Unlimited collaborators on unlimited public repositories, with the full feature set.
- Unlimited private repositories too, but with a **limited** feature set on those private repos.
- 2,000 GitHub Actions minutes a month.
- Community support (meaning: GitHub's public forums and documentation, not a private support ticket line).

To get the full feature set on private repositories, plus things like required pull request reviewers and a security overview, you'd upgrade to **GitHub Team**. Team also raises the Actions minutes to 3,000 a month and adds email support. Above that sits **GitHub Enterprise Cloud**, aimed at much larger companies, with single sign-on, centrally managed policy across multiple organizations, and far higher usage limits.

For a small business with a private repo and a small team, the practical read is: start on Free, and only look at Team the day you specifically want a checkpoint (a required review) before someone's change lands on the main branch. That's a real, concrete reason to upgrade. Wanting more storage or more Actions minutes before you've actually run out is not.

**A note on price, stated carefully:** at the time of writing, GitHub's pricing page lists GitHub Team at $4 USD per user per month **for the first 12 months**, and GitHub Enterprise Cloud starting at $21 USD per user per month **for the first 12 months**. Both prices carry an asterisk on GitHub's own pricing page pointing to an introductory-rate footnote. What the price becomes after those first 12 months is not stated anywhere on that page. Confirm the current renewal price on GitHub's own pricing page before you commit to a paid plan; do not assume the introductory number is the number you'll pay in year two.

## Creating an organization: the exact click path

This is a browser-only step. There is no GitHub CLI command and no Claude Code shortcut for creating an organization, because this is an account and billing action tied to your own identity. Do this yourself, signed in as you, in your browser.

1. On any github.com page, click your **profile picture** in the top right corner.
2. Click **Settings**.
3. In the **Access** section of the left sidebar, click **Organizations**.
4. Next to the "Organizations" heading, click **New organization**.
5. Follow the on-screen prompts to finish setup.

GitHub's own step-by-step for this is at the URL in Sources below, and it stops exactly there: it tells you to "follow the prompts," but doesn't publish the exact list of fields on the page (organization name, contact email, personal-or-business option, and so on). That's normal. It means the screen you land on is the authority, not this page. **Confirm on your own screen** what fields it actually asks for at the moment you create yours, and fill them in with your own real details.

**Screenshot placeholder:** the "New organization" screen from GitHub, whatever fields it currently asks for, so a reader can match what they see to this step.

**What if I already answered a plan question during setup?** GitHub's plans page for organizations exists specifically so you can compare options before or during that step. Whatever you pick, you can change your plan later from the organization's own settings; picking Free to start is not a one-way door.

## Naming your organization

GitHub doesn't publish a specific naming-rules page for organization names on the page that walks through creation. Pick a name your team will recognize (often the business name, with no spaces, since GitHub account names generally don't allow spaces). If the exact name you want is taken, you'll be told so on screen, and you'll need a variation. Confirm the exact rules and any error message on your own screen when you get there, since that page is the authority, not this one.

You can rename an organization later. Only organization owners can do it. From the organization's **Settings**, scroll to the **Danger zone**, click **Rename organization**, click **I understand, let's rename my organization** to confirm, then type the new name and click **Change organization's name**. Three things to know before you do:

- Most links to your existing repositories keep working. GitHub automatically redirects them to the new name.
- Your **old organization's profile page** (the one people bookmark or share) stops working and shows a 404 once the rename goes through.
- The old name becomes available for someone else to claim once you've moved off it, so don't rename and expect to "come back to" the old name later.

## Adding a second owner (do this early, not eventually)

An organization **owner** has complete administrative control: billing, every repository, every member's access, the works. When you create an organization, you are automatically its first owner.

GitHub's own guidance is specific and worth repeating word for word: the owner role "should be limited, but to no less than two people, in your organization." A separate GitHub page on keeping ownership continuous is blunter about why: "If an organization only has one owner, the organization's projects can become inaccessible if the owner is unreachable."

Read that plainly. If you are the only owner and something happens to your access (you lose your two-factor device, your password reset email goes to an inbox you no longer check, your account gets locked for any reason), there is nobody left with the authority to fix it, recover it, or even grant someone else access. GitHub's published documentation does not describe an emergency override for this situation. Treat "add a second owner" as a day-one task, not a someday task.

**To promote an existing organization member to owner:**

1. Profile picture (top right) → **Settings** → **Organizations** → click your organization's name.
2. Click the **People** tab.
3. Tick the checkbox next to the person you want to promote.
4. Above the member list, open the **"X members selected..."** dropdown and click **Change role**.
5. Choose the new role, then click **Change role** again to confirm.

**If that second person isn't in the organization yet, invite them first:**

1. Organization page → **People** tab → **Invite member**.
2. Enter their username, full name, or email address, then click **Invite**.
3. Pick their organization role on the invite screen itself (you can invite them straight in as an owner, or as a member and promote them later using the steps above).
4. Click **Send invitation**.

They'll get an emailed invite link. If they don't accept it within seven days, the invite expires automatically and you'll need to send a new one.

**One billing note if you're on a paid plan (Team or Enterprise, not Free):** GitHub's own docs state that "if your organization has a paid per-user subscription, an unused license must be available before you can invite a new member." On Free this isn't a concern; on a paid plan, adding your second owner may need a paid seat the same as adding anyone else.

## Transferring an existing repository into your organization

If you already have a repository sitting under your personal account and you want it living inside your new organization instead, you move it with a **transfer**, not by re-creating it from scratch. History, issues, pull requests, the wiki, stars, and watchers all move with it.

This is also a browser-only step: there is no GitHub CLI (`gh`) command for transferring repository ownership. It's a web-interface-only action.

1. Requirements first: you need **administrator access** to the repository you're moving, and permission to create a repository inside the target organization.
2. Open the repository's main page, then click its **Settings** tab.
3. Scroll to the bottom, to the **Danger Zone**.
4. Click **Transfer**.
5. Under "New owner," choose **Select one of my organizations** and pick your organization from the dropdown.
6. Optionally give the repository a new name at the same time (only available if you're an owner of the destination organization).
7. Type the repository's name to confirm, then click **I understand, transfer this repository**.

A few things that survive the move automatically, straight from GitHub's own documentation: webhooks, services, secrets, and deploy keys all stay attached after the transfer completes. Links to the old location redirect to the new one. One detail worth knowing about issues specifically: if you're moving from a personal account into an organization, any issue assigned to someone who's a member of that organization keeps its assignee; every other issue assignment gets cleared, because that person may not have access to the repository's new home.

**Screenshot placeholder:** the "Danger Zone" section of a repository's Settings page, with the "Transfer" button visible, so the reader can see exactly where this lives.

## Leaving an organization

If you're a member (or an outside collaborator) and you want out, you can leave at any time, without asking anyone's permission.

1. Profile picture (top right) → **Settings**.
2. **Access** section of the sidebar → **Organizations**.
3. Next to the organization, click **Leave**.

**One important gap to know about before you do this:** if you're the person currently responsible for paying for the organization, leaving does **not** hand billing off to anyone else. GitHub's own wording is direct: leaving "does not update the billing information on file for the organization," and if you're currently responsible for billing, "you must have another owner or billing manager for the organization update the organization's payment method" first. Sort out who's paying before you click Leave, not after.

## Deleting an organization entirely

This is different from leaving. Deleting removes the organization for everyone, permanently.

GitHub is explicit that this is irreversible: deleting "permanently removes all repositories, forks of private repositories, wikis, issues, pull requests, and project or organization pages." Billing for the organization ends. Once deleted, the organization's name is locked for 90 days before it becomes available for anyone (including you) to claim again.

Back up anything you want to keep before you start. GitHub's own advice is the same: make sure you have a copy of every repository, wiki, issue, and project first.

1. Profile picture (top right) → **Organizations** → select the organization.
2. Open its **Settings** (or via the **More** dropdown if you don't see a direct tab).
3. Scroll to the **Danger zone**.
4. Click **Delete this organization**.
5. Type the organization's name to confirm, then click **Cancel plan and delete the organization**.

Confirm on your own screen exactly who is allowed to see and click this button before you rely on it as a safeguard; the fetched documentation walks through the steps but doesn't spell out the permission requirement on that specific page. In practice, treat it as an owner-only action and don't hand owner access to anyone you wouldn't trust with this button.

---

## If it goes wrong

**"New organization" isn't there, or I can't create one.** Confirm you're signed in with your own personal account first (check for your profile picture in the top right). Organization creation is tied to your personal account, so a fresh or half-finished sign-up can hide this option until your account itself is fully verified. If it's still missing after that, GitHub's own account-status pages (under Settings) will tell you if anything about your account needs attention first.

**I created the organization alone and I'm worried about being locked out.** Add a second owner today, using the steps above, before you do anything else with the organization. This is the single most avoidable failure on this page: GitHub's own guidance says never run an organization with only one owner, and there's no documented emergency recovery path if that one owner loses access.

**I invited someone and nothing happened.** Ask them to check their spam or promotions folder; invitation emails land there often. If it's genuinely been more than seven days, the invite has expired automatically and you just need to send it again from the People tab.

---

## Questions people ask here

**Does creating an organization make me its owner automatically?** When you create it through the flow above, you are the one setting it up, and organization owners have full administrative control. Rather than assume, check your own role on the organization's People page once it's created: your role is listed right next to your name.

**Can I turn my personal account into an organization, or the other way around?** This page only covers creating a brand new organization and moving individual repositories into one. Converting an existing personal account into an organization, or an organization back into a personal account, is a different, more involved process. Confirm directly on GitHub's own documentation before attempting anything like that; it isn't covered here.

**If I'm on GitHub Free, is my private code actually private?** Yes. "Limited features" on Free means things like required reviewers and advanced security tooling aren't available, not that privacy itself is reduced. A private repository on Free is still private.

**What happens to my organization's paid seats if I remove someone?** That question sits outside what this page covers (it's a billing and member-management detail, not an organization-level setup step). Confirm current seat behavior on your own billing settings page before assuming either way.

**Do I need to install anything to do any of this?** No. Every step on this page happens in your browser, signed in to github.com. Nothing here uses Claude Code or the terminal, because these are account and billing actions tied to your own identity, and GitHub doesn't offer a command-line shortcut for most of them anyway (transferring a repository, for example, has no `gh` CLI command at all).

---

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
