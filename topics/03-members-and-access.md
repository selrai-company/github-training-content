# Adding people, and giving them the right access

## What this gets you

Adding someone to your GitHub organization is how a bookkeeper, a virtual assistant, a business
partner, or the nephew who built your website gets to do real work on your repositories, without
you ever handing over your own password. You choose exactly what each person can see and change,
on which repository, and you can take that access back the same day they leave. Get this page
right and you also avoid the single most common, most expensive mistake covered anywhere in this
kit: one setting, ticked once and forgotten, that quietly gives every current and future member of
your organization push access to everything you own.

## Before you start

**You need an organization already.** Everything on this page is about adding people to an
organization account, not your own personal account. If you have not created one yet,
`02-organizations.md` covers that first, including the one signal that tells you whether you
actually need an organization at all.

**Know your own role before you start changing anyone else's.** Most of what follows needs you to
be an organization owner. If you are not sure what your own role currently is, the organization's
own **People** tab lists it right next to your name; check there rather than assuming.

**Every action on this page happens in your browser, signed in as yourself.** There is no GitHub
CLI (`gh`) command for inviting someone, changing anyone's role, or managing a team. Checking the
GitHub CLI's own command list confirms this directly: the `org` command has only a `list`
subcommand, and there is no `team` command at all. These are identity, permission, and, on a paid
plan, billing actions tied to your own sign-in, so do them yourself, in your browser, rather than
through Claude Code or a terminal. Nothing on this page needs a terminal.

## The words you need

**Organization role.** What a person can do to the organization itself: its billing, its overall
settings, and its member list. This is a different question from what that same person can do
inside any one repository, and the two get confused constantly because people use the word "admin"
loosely for both. Keep them separate in your head: organization role is about the whole business,
repository role, below, is about one project inside it.

**Organization owner.** GitHub's own one-line definition: "Organization owners have complete
administrative access to your organization." That includes billing, every repository, and every
other member's access, whether or not you have separately set them a lower role on any specific
repository.

**Organization member.** GitHub's own words: "The default, non-administrative role for people in an
organization is the organization member." This is what someone gets automatically unless you
deliberately pick something else for them on the invite screen.

**Moderator, billing manager, security manager, and GitHub App manager.** Four narrower
organization roles that most small businesses will never need. A **moderator** can, in addition to
the normal member permissions, "block and unblock non-member contributors, set interaction limits,
and hide comments in public repositories owned by the organization," which only matters if your
organization has public repositories with open discussion. A **billing manager** "can manage the
billing settings for your organization, such as payment information," and nothing else; they cannot
see or touch any code. A **security manager** gets read access to every repository plus visibility
of security alerts, without full owner control. A **GitHub App manager** is how an owner delegates
just the management of GitHub App registrations to someone else, instead of keeping that with the
owners only. For a small business, you will almost always be choosing between owner and member;
treat these four as options that exist for larger setups with dedicated billing or security people.

**Repository role.** What a person can do inside one specific repository. This is a completely
separate setting from their organization role, and it is set per repository, from **Read** (look
and comment only) up to **Admin** (full control of that one repository, including deleting it).
GitHub's own recommendation for who fits each one:

| Role | GitHub's own description |
|---|---|
| **Read** | "Recommended for non-code contributors who want to view or discuss your project" |
| **Triage** | "Recommended for contributors who need to proactively manage issues, discussions, and pull requests without write access" |
| **Write** | "Recommended for contributors who actively push to your project" |
| **Maintain** | "Recommended for project managers who need to manage the repository without access to sensitive or destructive actions" |
| **Admin** | "Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository" |

One thing worth knowing before you set any of these: an organization owner has Admin-level access
to every repository the organization owns automatically, no matter what repository role you set for
them individually. You cannot lock an owner out of one repository by giving them a lower role
there.

**Base permissions.** The organization-wide default repository access every member gets, to every
repository the organization owns, current and future, unless you separately give someone a higher
role on a specific repository. There are four levels: **No permission**, **Read**, **Write**, and
**Admin**. This is the setting behind the most expensive mistake on this page, covered in full
below.

**Outside collaborator.** GitHub's own definition: "An outside collaborator is a person who is not
a member of your organization, but has access to one or more of your organization's repositories."
Think of it as a side door: it gives someone a key to one specific room, not a set of keys to the
whole building.

**Team.** GitHub's own definition: "Teams are groups of organization members that reflect your
company or group's structure with cascading access permissions and mentions." Instead of granting a
repository role to five people one at a time, you grant it once to a team, and everyone on that team
gets it, including anyone who joins the team later.

**Nested team, a parent team and a child team.** A structure where one team sits underneath
another. GitHub's own wording: "Child teams inherit the parent's access permissions, simplifying
permissions management for large groups." Give the parent team Write access to a repository, and
every child team nested under it gets that same Write access automatically, without you granting it
again.

**Invitation.** The email GitHub sends someone after you add them, whether as a full member or an
outside collaborator, which they must accept before the access actually takes effect. It expires
automatically after seven days if nobody accepts it.

**Seat, also called a licence.** On a paid organization plan (GitHub Team or GitHub Enterprise, not
Free), each person taking up a place, whether a full member or an outside collaborator with access
to a private repository, uses one of a limited number of paid seats. On GitHub Free, this does not
apply.

**Two-factor authentication, usually shortened to 2FA.** A second proof of identity, beyond a
password, required to sign in. It comes up on this page only because of one specific rule around
bringing someone back after you remove them; `01-accounts-and-security.md` covers setting it up in
full.

**Private fork.** A person's own personal copy of one of your private repositories, made inside
their own account. It comes up on this page because of what happens to it when you remove that
person, covered under offboarding below.

## How to do it

### Setting your organization's base permission, before you invite anyone

Do this first, since it decides what a brand-new member gets automatically the moment they accept
an invitation.

From any github.com page, click your **profile picture** in the top right corner, then click
**Organizations**. The direct address, if you would rather go straight there, is
[github.com/settings/organizations](https://github.com/settings/organizations). You will know you
are in the right place because it lists every organization you belong to, with your role listed
next to each one.

Click your organization's name. Along the top of the organization's own page, click its
**Settings** tab. In the sidebar, under the **Access** heading, click **Member privileges**. Scroll
down to the section titled **Base permissions**, and pick a level from the dropdown: **No
permission**, **Read**, **Write**, or **Admin**.

You will know it saved because the dropdown shows your new choice the next time you load the page.

If you do not see an **Access** heading in that sidebar at all, you are not signed in as an
organization owner. Only owners can normally reach this screen; ask whoever holds that role in
your organization to make the change, or add yourself as a second owner first (`02-organizations.md`
covers why you want a second owner regardless).

**The trap, stated plainly.** If you set this to Write "so everyone can push without me having to
add each person to each repository," you have just given every current member, and every member
you add in the future, push access to every repository the organization owns, current and future,
with no per-repository decision involved on your part ever again. It is a single setting that
quietly overrides the entire point of having repository roles at all. Leave it at **Read** or **No
permission**, and grant Write, or a narrower role, per repository, or per team, to the specific
people who actually need it there.

Three details worth knowing before you touch this setting, all from GitHub's own documentation:

- **Base permissions do not apply to outside collaborators.** An outside collaborator always needs
  to be granted access to a repository directly, no matter what the base permission says.
- **A higher permission explicitly granted on one repository wins.** If someone's base permission is
  Read but you have separately given them Write on one specific repository, they keep that Write
  access there; the base permission does not pull it back down.
- **Changing the base permission does not retroactively touch a private fork someone already
  made.** Lowering it afterward does not automatically change an existing fork's permissions.

### Inviting someone into the organization

1. From your **Organizations** list (the page you reached above), click your organization's name,
   then click the **People** tab.
2. Click **Invite member**.
3. Type their username or email address, then click **Invite**.
4. Pick their organization role (owner, member, or one of the narrower roles above), and,
   optionally, add them to a team right away.
5. Click **Send invitation**.

You will know it worked because they appear on the **People** tab immediately, marked as pending,
and disappear from that pending state once they accept.

**What they receive:** GitHub's own wording: "The invited person will receive an email inviting
them to the organization. They will need to accept the invitation before becoming a member of the
organization." Exactly how that email is worded and formatted is not published on GitHub's own
documentation page, so confirm on your own screen what it looks like the first time you send one,
so you recognise it later and do not mistake it for spam.

**The invite expires after seven days.** Confirmed on two separate GitHub sources: the
inviting-users page states "if an invitee does not accept the invitation within seven days, the
pending invitation expires automatically," and GitHub's own changelog states the same rule applies
to both organization invites and repository-collaborator invites.

**If it does not arrive:** ask them to check spam or promotions folders first, by far the most
common cause. You can cancel or resend it any time before they accept, from the same **People**
tab. If more than seven days have genuinely passed, it has already auto-expired; look under
**Failed invitations** on the **People** tab, then click **Retry invitation**, or **Cancel
invitation** if you have changed your mind, rather than assuming something is broken.

**One billing detail on a paid plan.** On GitHub Team or Enterprise, not Free, GitHub's own
documentation is direct: "if your organization has a paid per-user subscription, an unused licence
must be available before you can invite a new member." On Free, this never blocks you.

### Outside collaborators, for someone who is not really joining the team

Use this instead of a full invitation when the person only needs access to one or two repositories,
with no ongoing relationship to the rest of your organization.

Two facts change how you should use this option:

**They cannot be added to a team.** GitHub's own wording is direct: "Outside collaborators cannot
be added to a team, team membership is restricted to members of the organization." If you want
someone inside a team's cascading permissions, covered below, they have to be a full member. There
is no workaround from the outside-collaborator side.

**They still cost a paid seat on a paid plan.** A common assumption is that adding someone as an
outside collaborator, instead of a full member, avoids using up a paid licence. That is false once
you are off the Free plan. GitHub's own wording: "Unless you are on a free plan, adding an outside
collaborator to a private repository will use one of your paid licenses." On GitHub Free, this is
not a concern either way.

**Adding one, per repository, not per organization:**

1. Open the specific repository, then click its **Settings** tab.
2. In the **Access** section of the sidebar, click **Collaborators & teams**.
3. Click **Add people**.
4. Search for and select their name.
5. Under "Choose a role," pick the repository role to give them, from the table above.
6. Click **Add [their name] to [the repository]**.

You will know it worked because their name appears on that repository's **Collaborators & teams**
page, marked as pending until they accept, under the same seven-day expiry rule described above.

**Where to see and manage all of them at once:** the organization's **People** tab, then, in the
sidebar, click **Outside collaborators**. From there you can remove someone from a single
repository, remove them from every repository they have access to at once, or convert them into a
full organization member if their role in your business has grown. GitHub's own written
documentation does not describe the exact visual layout of that page in detail, so confirm on your
own screen what it actually looks like once you are there.

**When to use which:** a contractor doing one job on one repository, with no ongoing relationship
to the rest of your organization, is a textbook outside collaborator. Someone becoming a regular
part of the team, who should see your organization's shared context, should be a full member
instead.

### Teams, and giving a team access to a repository

Set this up once you have more than a couple of people who should share the same access, so you
grant it once to the group instead of person by person.

**Creating a team:**

1. From your organization's own page, click the **Teams** tab (it sits next to **People**, with a
   small people icon beside it).
2. Click **New team**.
3. Type a name for the team, and, if you want one, a short description.
4. If this team should sit underneath another one, pick the parent team from the dropdown.
5. Choose the team's visibility, and its notification preference.
6. Click **Create team**.

You will know it worked because the team's own page opens, with a **Members** tab and a
**Repositories** tab across the top. This kit could not confirm, from GitHub's own documentation,
exactly which organization roles besides owner are permitted to create a team; if the **New team**
button is missing for you, that is the first thing to check with whoever holds the owner role.

**Giving that team access to a repository:**

1. Open the repository, then click its **Settings** tab.
2. In the **Access** section of the sidebar, click **Collaborators & teams**.
3. Next to "Manage access," click **Add teams**.
4. Search for and select the team.
5. Under "Choose a role," pick the repository role to give the whole team, from the table above.
6. Click **Add [team name] to [the repository]**.

Every current member of that team gets the role you just picked, immediately, and so does anyone
who joins the team later, without you doing this again.

**Nesting teams:** GitHub's own wording: "Child teams inherit the parent's access permissions,
simplifying permissions management for large groups." Give a parent team Write access to a
repository, and every child team nested underneath it gets that same Write access automatically.
This also cascades for @mentions: mentioning the parent team notifies everyone in every child team
underneath it, not just the people directly on that top team.

For most small businesses, one or two teams, an "Everyone" team with broad Read access, and a
smaller team with Write access to the repositories it actually works in, covers it. Nesting starts
to matter once you have distinct sub-groups, a design side and a build side, say, that should each
get their own narrower access on top of a shared baseline.

### Removing someone (offboarding)

**Removing a full member:**

1. **Profile picture** (top right), then **Organizations**, then your organization's name.
2. Click the **People** tab.
3. Tick the checkbox next to the person's name.
4. Above the member list, open the dropdown that reads **"X members selected..."**, and click
   **Remove from organization**.
5. Click **Remove members** to confirm.

**Removing an outside collaborator**, from one repository or from all of them at once:

1. **People** tab, then **Outside collaborators** in the sidebar.
2. Select them.
3. Either open their settings to remove access to a single repository, or open the **"X
   collaborators selected"** dropdown and click **Remove from all repositories**, then confirm.

You will know either removal worked because the person disappears from that list. What it does, and
does not, undo is the part most owners get wrong, all sourced from GitHub's own removal
documentation:

**Removal stops future access. It does not claw back what they already copied to their own
machine.** GitHub's own words: "Removed members will lose access to private forks of your
organization's private repositories, but they may still have local copies. However, they cannot
sync local copies with your organization's repositories." If they had already cloned a repository
to their laptop before you removed them, that clone stays there exactly as it was. Removal cuts off
future pulls, pushes, and any view of your repositories on GitHub going forward; it does not reach
onto their computer and delete anything. GitHub is direct about whose problem that is afterward:
"you are responsible for ensuring that people who have lost access to a repository delete any
confidential information or intellectual property." If that matters for what you are removing them
from, that is a direct conversation with the person, not a button GitHub provides.

**Their own private fork is deleted, but a fork living in a different organization can survive.** If
they had personally forked one of your private repositories, GitHub's own forks documentation
states: "If you remove a person's access to a private repository, any of their forks of that
private repository are deleted. Local clones of the private repository are retained." Their personal
copy on GitHub itself goes away; their local clone, again, does not. One real exception worth
knowing: "When private repositories are forked to other organizations, those organizations are able
to control access to the fork network. This means users may retain access to the forks even after
losing access to the original organization because they will still have explicit access via a
fork." If your private repository was forked into a separate organization at some point, that other
organization now controls who can see that fork, independently of what you do in yours.

### Reinstating someone you removed by mistake

**There is a three-month window.** GitHub's own words: "When you remove a user from your
organization, their membership data is saved for three months. You can restore their data, or any
private forks they owned of your organization's repositories, if you invite the user to rejoin the
organization within that time frame." Past that window, their old role, access, and forks are gone
for good, and you would be setting them up from scratch.

1. **People** tab, then **Invite member**.
2. Type their username, then click **Invite**.
3. Choose to restore their previous privileges, or start fresh with new ones, then click **Invite
   and reinstate** or **Invite and start fresh**.
4. If you started fresh, pick their new role and teams, then **Send invitation**.
5. They receive the same invite email as any new member, and need to accept it.

**One two-factor authentication catch.** If your organization requires two-factor authentication and
the person was removed for not having it enabled, GitHub's own wording is: "you can send an
invitation to reinstate a user's privileges and access to the organization before they have enabled
two-factor authentication, but they must enable 2FA before they can accept your invitation to
rejoin the organization." You can start the process before they have set up 2FA; they cannot
finish accepting until they have.

## Strategy: how to actually use this

**The one habit underneath everything above: give what is needed today, not everything just in
case.** Start every new person at the lowest organization role and the narrowest repository access
that lets them do this week's job, not the access you imagine they might need in six months.
Widening someone's access later takes thirty seconds. Discovering a year from now that everyone in
your organization has had push access to everything, because the base permission was set to Write
on day one, is a much longer conversation.

**A solo operator does not need most of this page.** If it is genuinely just you, none of
organization roles, base permissions, outside collaborators, or teams apply yet; a personal account
already does everything you need. The trigger that means you have outgrown this is specific: a
second person needs push access to your repositories on an ongoing basis, and you want that access
to keep working even on a day you are not around to grant it yourself. Not "it looks more
professional." Not "I have a registered business name."

**A two or three-person business, one of them technical:** set the base permission to Read or No
permission from day one. Give the technical person Write on whatever they actually build. Give
everyone else Read by default, and Write only on the specific repository, or the specific content
inside it, that they personally edit. Skip teams entirely at this size; adding one person to a
group is not faster than adding them directly, and a team you set up "to be organised" is a layer
of indirection nobody needed yet.

**A team of four or more, with distinct groups doing genuinely different things:** this is where
teams start earning their keep. GitHub's own description is that a team gives you "cascading access
permissions." Once you have, say, a build side and a content side, create a team for each, grant
the repository access once to the group, and stop granting it person by person. Add someone new to
the group, and they inherit the same access automatically, the day they join. Below four or five
people, this is a solution looking for a problem; above it, it starts saving real time every time
someone joins.

**Outside collaborator versus full member is a relationship question, not an access-level
question.** A contractor doing one scoped job on one repository, with a defined end date and no
plan to keep working with you afterward, is a textbook outside collaborator, whatever role you give
them while they are there. Someone becoming a genuine, ongoing part of how your business runs
should be a full member, even if their access starts narrow, because a member can join a team and
see your organization's shared context in a way an outside collaborator structurally cannot.

**What would change this:** if reviewing who has access to what has become a genuine chore because
you have dozens of people and repositories to track by hand, that is the point at which teams stop
being optional and become the only sane way to manage it, regardless of your headcount. And if a
mistake made by someone with more access than they needed has actually cost you money, embarrassed
you publicly, or exposed something sensitive, that is the moment to audit every role and base
permission you have set, not a hunch to shrug off.

**What good looks like months later.** You can name every person with Write access or higher on
each of your repositories without opening GitHub to check. Your base permission is still at Read or
No permission, unless you deliberately raised it and remember exactly why. Nobody who left, or
whose contract ended, still shows up with active access, and the one time you did remove someone by
mistake, you knew about the three-month reinstatement window and used it instead of rebuilding
their access from scratch. That is the actual return on the small amount of setup this page asks
for.

## A worked example

A two-partner physiotherapy clinic runs its booking website and its client-intake forms out of one
organization. The two partners are its only members, and both are organization owners, so neither
of them is ever the single point of failure the rest of this kit warns about.

They take on a part-time bookkeeper to handle invoicing, for a few hours a week, with no plan for
the relationship to grow beyond that. They add her as an **outside collaborator** on the invoicing
repository only, with **Write** access, since she needs to push updated invoice templates but has
no reason to touch the booking website or delete anything. She never becomes an organization
member, and never appears on any team.

A few months later, they hire a receptionist to manage bookings day to day, and expect her to be
part of the business for years, not weeks. They invite her as a full **organization member**, with
the base permission already sitting at **Read**, and separately grant her **Write** on the booking
repository only, since that is the one thing she actually edits.

When a second receptionist joins six months after that, doing the exact same job, the partners
realise they are about to grant the same **Write** access a second time by hand, and decide it is
worth a **team** instead. They create a "Bookings" team, add both receptionists to it, and give the
team **Write** access to the booking repository once. The next person hired into that same role
gets added to the team on day one, and the partners never touch a repository-role dropdown for a
bookings hire again.

When the bookkeeper's engagement eventually ends, one partner removes her using the
outside-collaborator removal steps above, and has a short, direct conversation with her about the
invoice templates already saved on her own laptop, since removing her access on GitHub does not
reach that machine.

## If it goes wrong

**I set the base permission to Write months ago, and I have just realised everyone can push to
everything.** Go to your organization's **Settings**, then **Access**, then **Member privileges**,
and drop the base permission down to **Read** or **No permission**. Then check whether anyone was
also explicitly granted a higher role directly on a specific repository, since that explicit grant
survives a base-permission change and will not be undone by this step alone.

**I invited someone and they say the email never arrived.** Have them check spam and promotions
folders first; this is the overwhelming majority of cases. If more than seven days have passed, the
invite has already auto-expired on its own, and you will find it under **Failed invitations** on
the **People** tab to retry.

**I need to add a contractor to a team, but the option is not there.** They are an outside
collaborator, and outside collaborators cannot be added to a team under any circumstance. Either
bring them in as a full member, in which case they count toward a paid seat the same as any other
member on a paid plan, or grant them access to the specific repositories they need one at a time,
without a team.

**I removed someone and now regret it, or removed the wrong person.** You have three months from
the removal date to reinstate them with their old role, access, and forks intact, using the "Invite
and reinstate" option above. After that window, you are rebuilding their access from scratch.

**I cannot find a New team button anywhere.** Confirm you are looking at your organization's own
**Teams** tab, not a repository's. If it is still missing, you are most likely not an organization
owner; this kit could not confirm from GitHub's own documentation exactly which roles besides owner
are permitted to create one, so check with whoever holds that role in your organization.

**I typed someone's username into an issue's assignee box and nothing appeared.** That is not this
page, it is `13-issues-and-tracking-work.md`, but the underlying cause is usually the same one:
they have not been added to the repository yet. Add them here first, then try again there.

## FAQ

**What is the actual difference between an organization owner and a repository admin?** Owner is
organization-wide: billing, every repository, every member's access. Admin is scoped to one
repository only: that repository's settings, its collaborators, and the ability to delete that one
repository. An owner automatically has admin-level access to every repository anyway, but an admin
on one repository has no organization-wide power at all.

**If I remove someone, does it delete their personal GitHub account too?** No. Your organization is
a separate account they belong to, not their whole GitHub identity. Removing them from your
organization only removes their access to your organization's repositories and settings; their own
personal account, and anything under it that has nothing to do with your organization, is
untouched.

**Can I make someone a member without giving them access to any code yet?** Yes. Invite them as a
member, leave the base permission at **No permission** or **Read**, and do not add them to a
repository or a team. They show up as a member of the organization with no repository access until
you deliberately grant it.

**Does an outside collaborator show up in my People tab the same way a member does?** They are kept
separate. Full members appear on the main **People** list; outside collaborators have their own
view, under **People**, then **Outside collaborators** in the sidebar. Confirm exactly how that
page is laid out on your own screen, since GitHub's written documentation does not spell out the
visual layout in detail.

**What happens to a member's paid seat if I remove them?** That sits outside what this page can
confirm from GitHub's own documentation. Confirm the current behaviour on your organization's own
billing settings page before assuming it frees up the seat immediately.

**Can a team have more than one parent?** Not confirmed from GitHub's own documentation for this
page. Treat team nesting as a single line running from one parent down to its children, not a shape
where a team reports to two parents at once, and confirm on your own screen if you attempt anything
more complex.

**Do I need to remove someone from every team individually before removing them from the
organization?** No. Removing someone from the organization entirely, using the steps above, removes
their access everywhere at once, including every team and every repository, in one action. You only
manage team membership separately if you want to narrow their access while keeping them in the
organization.

## Quick reference

- **Set base permission:** Organizations, org name, Settings, Access, Member privileges, Base
  permissions dropdown
- **Invite a member:** Organizations, org name, People, Invite member, pick role, Send invitation
- **Add an outside collaborator:** repository Settings, Access, Collaborators & teams, Add people,
  pick role
- **Create a team:** org page, Teams, New team, name it, Create team
- **Give a team repository access:** repository Settings, Access, Collaborators & teams, Add teams,
  pick role
- **Remove a member:** People tab, tick their name, "X members selected...", Remove from
  organization
- **Remove an outside collaborator:** People tab, Outside collaborators, select, Remove from all
  repositories
- **Reinstate someone (within 3 months):** People tab, Invite member, username, Invite and
  reinstate
- **Check your own role:** organization's People tab, listed next to your name
- **Through Claude Code:** none of this page has a `gh` CLI equivalent; do it in the browser

## Sources

- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/setting-base-permissions-for-an-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/adding-outside-collaborators-to-repositories-in-your-organization
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/removing-an-outside-collaborator-from-an-organization-repository
- https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams
- https://docs.github.com/en/organizations/organizing-members-into-teams/creating-a-team
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization
- https://docs.github.com/en/organizations/managing-membership-in-your-organization/reinstating-a-former-member-of-your-organization
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks
- https://github.blog/changelog/2020-02-05-self-expiring-repository-and-organization-invitations/
- https://docs.github.com/en/get-started/learning-about-github/githubs-plans
- https://cli.github.com/manual/
