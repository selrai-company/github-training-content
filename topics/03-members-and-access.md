# Adding people, and giving them the right access

This page covers everything about letting other people into your GitHub organization: what role to give them, how to invite them, the difference between a full member and someone who just needs access to one repository, how teams work, and what actually happens when you remove someone.

By the end, you'll be able to invite the right person with the right access, avoid the one setting that quietly gives everyone push access to everything, and offboard someone correctly, including knowing what removal does and does not undo.

This whole page assumes you already have an organization. If you don't, read the previous page in this kit first.

Every click path below is browser-only, on github.com. There is no GitHub CLI command for inviting people, managing roles, or managing teams. Checking the GitHub CLI's own command list confirms this: the `org` command only has a `list` subcommand, and there's no `team` command at all. These are identity, permission, and (on paid plans) billing actions, so do them yourself, signed in as you, in your browser. Nothing on this page needs Claude Code or a terminal.

## The two layers of access: organization role and repository role

GitHub separates "what can this person do across the whole organization" from "what can this person do in this one repository." You'll set both, and they're easy to confuse because people use words like "admin" loosely for both.

### Organization-level roles

These control what someone can do to the organization itself (its billing, its settings, its member list), not any one repository. GitHub's own one-line definition of each, from its roles-in-an-organization page:

- **Organization owner:** "Organization owners have complete administrative access to your organization." This includes billing, every repository, and every other member's access.
- **Organization member:** "The default, non-administrative role for people in an organization is the organization member." This is what everyone gets unless you pick something else on the invite screen.
- **Moderator:** "Moderators are organization members who, in addition to their permissions as members, are allowed to block and unblock non-member contributors, set interaction limits, and hide comments in public repositories owned by the organization." Mostly relevant if your organization has public repositories with open discussion; a small private-repo team usually doesn't need this role.
- **Billing manager:** "Billing managers are users who can manage the billing settings for your organization, such as payment information." They cannot see or touch code.
- **Security manager:** "The security manager role is an organization-level role that organization owners can assign to any member or team in the organization," giving read access to every repository plus security-alert visibility, without full owner control.
- **GitHub App manager:** by default, "only organization owners can manage the settings of GitHub App registrations owned by an organization"; this role is how an owner delegates just that one slice of control to someone else.

For a small business, you will mostly be choosing between **owner** and **member**. The other three roles exist for larger setups with dedicated billing or security people.

**Screenshot placeholder:** the organization's People tab, with the role dropdown next to a member's name open, showing the full list of roles above.

### Repository-level roles

These control what someone can do inside one specific repository, from least to most permissive. GitHub's own recommendation for who each role fits, from its repository-roles page:

| Role | GitHub's own description |
|---|---|
| **Read** | "Recommended for non-code contributors who want to view or discuss your project" |
| **Triage** | "Recommended for contributors who need to proactively manage issues, discussions, and pull requests without write access" |
| **Write** | "Recommended for contributors who actively push to your project" |
| **Maintain** | "Recommended for project managers who need to manage the repository without access to sensitive or destructive actions" |
| **Admin** | "Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository" |

**One thing worth saying plainly:** organization owners get admin access to every repository the organization owns automatically, regardless of any role you set for them individually, per GitHub's own repository-roles page. You cannot lock an owner out of a repository by giving them a lower repository role.

## Base permissions, and the trap of setting them too high

Base permissions are the org-wide default. GitHub's own words: they're the permissions "that apply to all members of an organization when accessing any of the organization's repositories." There are four levels: **No permission**, **Read**, **Write**, and **Admin**.

**Where to set it:** profile picture (top right) → **Organizations** → your organization → **Settings** → **Access** section of the sidebar → **Member privileges** → under "Base permissions," pick a level from the dropdown → confirm.

**The trap, stated plainly:** if you set the base permission to Write "so everyone can push without me having to add each person to each repo," you have just given every current member, and every member you add in the future, push access to every repository the organization owns, current and future, with no per-repo decision involved. It's a single setting that quietly overrides the entire point of having repository roles. Most small teams should leave this at **Read** or **No permission**, and grant Write (or a narrower role) per repository, or per team, to the specific people who actually need it there.

Three details worth knowing before you touch this setting, all from GitHub's own documentation:

- **Base permissions do not apply to outside collaborators.** An outside collaborator always needs to be granted access to a repository directly, no matter what the base permission says. (More on outside collaborators below.)
- **A higher permission explicitly granted on one repository wins.** If someone's base permission is Read but you've separately given them Write on one specific repository, they keep that Write access on that repository; the base permission doesn't pull it back down.
- **Changing the base permission doesn't retroactively touch private forks.** If a member already has a private fork of one of your repositories, lowering the base permission afterward doesn't automatically change that fork's permissions.

## Inviting someone into the organization

This is the click path for bringing someone in as a full organization member, per GitHub's own inviting-users documentation:

1. Profile picture (top right) → **Organizations**.
2. Click your organization's name.
3. Click the **People** tab.
4. Click **Invite member**.
5. Type their username or email address, then click **Invite**.
6. Pick their organization role (owner, member, or one of the others above), and optionally add them to a team right away.
7. Click **Send invitation**.

**What happens next:** GitHub's own words: "The invited person will receive an email inviting them to the organization. They will need to accept the invitation before becoming a member of the organization." Exactly how that email is worded and formatted isn't published on the docs page itself, so confirm on your own screen what it looks like when you send your first one.

**Screenshot placeholder:** the invite email itself, as received in an inbox, so a reader recognizes it and doesn't mistake it for spam.

**The invite expires after seven days.** This is confirmed on two separate GitHub sources: the inviting-users page states "if an invitee does not accept the invitation within seven days, the pending invitation expires automatically," and GitHub's own changelog states the same rule applies to both organization invites and repository-collaborator invites: "Invitations to join an organization or become a collaborator on a repository will expire seven days after they are created."

**If it doesn't arrive:**
- Ask them to check spam or promotions folders first; this is by far the most common cause.
- You can cancel or resend it any time before they accept, from the same People tab.
- If it's genuinely been more than seven days, it has already auto-expired. Look under **Failed invitations** on the People tab, then click **Retry invitation** (or **Cancel invitation** if you've changed your mind), rather than assuming something is broken.

**One billing detail if you're on a paid plan:** on GitHub Team or Enterprise (not Free), GitHub's own documentation is direct: "if your organization has a paid per-user subscription, an unused license must be available before you can invite a new member." On Free this never blocks you.

## Outside collaborators versus members

Sometimes the person you're adding isn't going to be part of your organization at all, just someone who needs access to one or two repositories. That's what an **outside collaborator** is. GitHub's own definition: "An outside collaborator is a person who is not a member of your organization, but has access to one or more of your organization's repositories."

Two facts about outside collaborators that change how you should use them:

**They cannot be added to a team.** GitHub's own wording is direct: "Outside collaborators cannot be added to a team, team membership is restricted to members of the organization." If you want someone inside a team's cascading permissions (see below), they have to be a full member, not an outside collaborator, full stop. There's no workaround for this from the outside-collaborator side.

**They still cost a paid seat on a paid plan.** A common assumption is that adding someone as an outside collaborator, instead of a full member, avoids using up a paid license. That's false once you're off the Free plan. GitHub's own wording: "Unless you are on a free plan, adding an outside collaborator to a private repository will use one of your paid licenses." On GitHub Free, this isn't a concern either way.

**Adding someone as an outside collaborator (per-repository, not per-organization):**

1. Open the specific repository → **Settings**.
2. In the "Access" section of the sidebar, click **Collaborators & teams**.
3. Click **Add people**.
4. Search for and select their name.
5. Under "Choose a role," pick the repository role to give them (see the role table above).
6. Click **Add [their name] to [the repository]**.

They'll get an invite the same way an organization invite works, and it expires under the same seven-day rule described above.

**Where to see and manage your outside collaborators as a group:** People tab → in the "Organization permissions" sidebar, click **Outside collaborators**. From there you can remove someone from a single repository, remove them from every repository they have access to at once, or convert them into a full organization member if their role has grown.

**When to use which:** a contractor doing one job on one repository, with no ongoing relationship to the rest of your organization, is a textbook outside collaborator. Someone who's becoming a regular part of the team, who should be inside your team structure and see your organization's shared context, should be a full member instead.

## Teams, and how permissions cascade

A team is GitHub's way of granting the same access to a group of people at once, instead of person by person. GitHub's own definition: "Teams are groups of organization members that reflect your company or group's structure with cascading access permissions and mentions."

Only organization members can be on a team. The teams documentation repeats the same restriction stated above from the other direction: "Teams can only be made up of members of your organization, outside collaborators are unable to be on a team."

**Nested (parent and child) teams** let you build a structure once and have access flow down it. GitHub's own wording: "Child teams inherit the parent's access permissions, simplifying permissions management for large groups." Practically, that means if you give a parent team Write access to a repository, every child team nested underneath it also gets that Write access automatically, without you granting it again on each child team. Add a new child team under that parent later, and it inherits the same access immediately.

This also cascades for @mentions: "Members of child teams also receive notifications when the parent team is @mentioned, simplifying communication with multiple groups of people." So mentioning the top-level team notifies everyone underneath it too, not just the people directly on that top team.

For most small businesses, one or two teams (say, "Everyone" for broad Read access, and a smaller team with Write access to the repositories that team actually works in) covers it. Nesting matters once you have distinct sub-groups (a design team and a build team, say) that should each get their own narrower access on top of a shared baseline.

## The principle: give what's needed today, not everything just in case

Everything above adds up to one habit worth building early: start every new person at the lowest role and the narrowest repository access that lets them actually do their job this week, not the access you imagine they might need in six months.

In practice that means: default new members to Read or No permission at the base-permission level, and grant Write (or Maintain, or Admin) only on the specific repositories where it's actually needed. Use an outside collaborator, not a full member, for a one-off contractor. Add someone to a team for the access that team gives, rather than granting them broad access individually "to save a step." It's far easier to widen someone's access later, in thirty seconds, than to discover after the fact that everyone in your organization has had push access to everything for the last year because the base permission was set to Write on day one.

## Offboarding: what removing someone actually does, and doesn't do

**Click path to remove a full member:** profile picture → **Organizations** → your organization → **People** tab → tick the checkbox next to the person → open the **"X members selected..."** dropdown → **Remove from organization** → confirm **Remove members**.

**Click path to remove an outside collaborator** (from one repository, or from all of them at once): People tab → **Outside collaborators** in the sidebar → select them → either open their settings to remove access to a single repository, or use the **"X collaborators selected"** dropdown → **Remove from all repositories** → confirm.

Now the part owners most often get wrong, stated plainly, all sourced from GitHub's own removal documentation:

**Removal stops future access. It does not claw back what they already copied to their own machine.** GitHub's own words: "Removed members will lose access to private forks of your organization's private repositories, but they may still have local copies. However, they cannot sync local copies with your organization's repositories." In other words: if they had already cloned a repository to their laptop before you removed them, that clone stays on their laptop exactly as it was. Removal cuts off future pulls, pushes, and any view of your repositories on GitHub going forward. It does not reach onto their computer and delete anything. GitHub is direct about whose problem that is afterward: "you are responsible for ensuring that people who have lost access to a repository delete any confidential information or intellectual property." If that matters for what you're removing them from, that's a conversation to have with the person, not a button GitHub provides.

**Their own private fork gets deleted, but a fork living in a different organization can survive.** If the person had personally forked one of your private repositories, GitHub's own forks documentation states: "If you remove a person's access to a private repository, any of their forks of that private repository are deleted. Local clones of the private repository are retained." So their personal copy on GitHub itself goes away (their local clone, again, does not). But there's a real exception worth knowing: "When private repositories are forked to other organizations, those organizations are able to control access to the fork network. This means users may retain access to the forks even after losing access to the original organization because they will still have explicit access via a fork." If your private repository was forked into a separate organization at some point, that other organization now controls who can see that fork, independently of what you do in yours. Removing someone from your organization does not automatically cut their access to a fork living somewhere else.

**There's a three-month window to undo a removal.** GitHub's own words: "When you remove a user from your organization, their membership data is saved for three months. You can restore their data, or any private forks they owned of your organization's repositories, if you invite the user to rejoin the organization within that time frame." Past that window, their old role, access, and forks are gone for good and you'd be setting them up from scratch.

**To reinstate someone within that window:**

1. People tab → **Invite member**.
2. Type their username, click **Invite**.
3. Choose to restore their previous privileges, or start fresh with new ones, then click **Invite and reinstate** or **Invite and start fresh**.
4. If you started fresh, pick their new role and teams, then **Send invitation**.
5. They'll get the same invite email as any new member, and need to accept it.

**One 2FA catch on reinstating:** if your organization requires two-factor authentication and the person was removed for not having it enabled, GitHub's own wording is: "you can send an invitation to reinstate a user's privileges and access to the organization before they have enabled two-factor authentication, but they must enable 2FA before they can accept your invitation to rejoin the organization." You can start the process before they've set up 2FA; they just can't finish accepting until they have.

---

## If it goes wrong

**I set the base permission to Write months ago, and I just realized everyone can push to everything.** Go to Settings → Access → Member privileges and drop the base permission down to Read or No permission. Then check whether anyone was also explicitly granted a higher role directly on a specific repository, since that explicit grant survives a base-permission change and won't be undone by this step alone.

**I invited someone and they say the email never arrived.** Have them check spam and promotions folders first; this is the overwhelming majority of cases. If more than seven days have passed, the invite has already auto-expired on its own, and you'll find it under **Failed invitations** on the People tab to retry.

**I need to add a contractor to a team, but the option isn't there.** They're an outside collaborator, and outside collaborators cannot be added to teams under any circumstance. Either bring them in as a full member (they'll then count toward a paid seat the same as any member on a paid plan), or grant them access to the specific repositories they need one at a time instead of through a team.

**I removed someone and now regret it, or removed the wrong person.** You have three months from the removal date to reinstate them with their old role, access, and forks intact, using the "Invite and reinstate" option above. After that window, you're rebuilding their access from scratch.

---

## Questions people ask here

**What's the actual difference between an organization Owner and a repository Admin?** Owner is organization-wide: billing, every repository, every member's access. Admin is scoped to one repository only: that repo's settings, its collaborators, and the ability to delete that one repo. An owner automatically has admin-level access to every repository anyway, but an admin on one repository has no organization-wide power at all.

**If I remove someone, does it delete their personal GitHub account too?** No. Your organization is a separate account they belong to, not their whole GitHub identity. Removing them from your organization only removes their access to your organization's repositories and settings; their own personal GitHub account, and anything under it that has nothing to do with your organization, is untouched.

**Can I make someone a member without giving them access to any code yet?** Yes. Invite them as a member, leave the base permission at No permission (or Read), and don't add them to a repository or a team. They'll show up as a member of the organization with no repository access until you deliberately grant it.

**Does an outside collaborator show up in my People tab the same way a member does?** They're kept separate. Full members appear on the main People list; outside collaborators have their own view, under People → **Outside collaborators** in the sidebar. Confirm exactly how that's laid out on your own screen, since the visual layout of that page isn't something GitHub's written documentation spells out in detail.

**What happens to a member's paid seat if I remove them?** That's a billing-settings detail that sits outside what this page covers. Confirm the current behavior on your organization's own billing settings page before assuming it frees up the seat immediately.

---

## Sources

- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/setting-base-permissions-for-an-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/adding-outside-collaborators-to-repositories-in-your-organization
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/removing-an-outside-collaborator-from-an-organization-repository
- https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/reinstating-a-former-member-of-your-organization
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks
- https://github.blog/changelog/2020-02-05-self-expiring-repository-and-organization-invitations/
- https://docs.github.com/en/get-started/learning-about-github/githubs-plans
- https://cli.github.com/manual/
