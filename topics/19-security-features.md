# The security features that watch your back

## What this gets you

Two of the most common ways a small business gets broken into online are a password or an API key
that ended up somewhere public by accident, and a piece of software the business relies on that
turns out to have a known hole in it. GitHub has features that watch for both of these, some of them
running automatically without you doing anything, some of them you have to switch on yourself.

None of this replaces good judgement, and this file says plainly where each feature stops working,
not just where it helps. A team that believes GitHub is "handling security" for them, when in fact
half of what they need is switched off or does not apply to their plan, is worse off than a team who
knows exactly what is and is not being watched. That is the actual point of this file.

## Before you start

**You need a repository.** If you have not created one yet, `04-repositories-and-visibility.md`
covers that first.

**You need to know your access level to it.** Seeing a security alert on a repository needs Write
access or higher. GitHub's own wording: "Security alerts for a repository are visible to people with
write, maintain, or admin access to the repository and, when the repository is owned by an
organization, organization owners." If you only have Read access, none of the alerts described below
will show up for you, and that is expected, not a fault. `03-members-and-access.md` covers checking
or changing your access level.

**You do not need to already understand branches or pull requests.** Everything in this file lives on
its own settings pages and its own tab. If Dependabot opens a pull request to fix something, though,
`07-pull-requests.md` covers what to do with it once it appears.

## The words you need

**Secret scanning.** A GitHub feature that automatically reads what gets pushed to a repository,
looking for things that look like passwords, API keys, or tokens, and raises an alert if it finds
one.

**Push protection.** A stricter version of secret scanning that acts before a secret ever lands in
your repository at all, by refusing the push in the first place.

**Bypass.** An option, present by default, to push a flagged change anyway, after giving a reason.
Covered in detail below, because it is the part most worth understanding correctly.

**Alert.** GitHub's word for the notice it raises when one of these features finds something. Every
alert described in this file lands in the same place, your repository's **Security and quality** tab,
covered below.

**Dependency.** A piece of software your project uses that someone else wrote and maintains, not code
you wrote yourself. A website built with a shopping-cart library, a script that uses a PDF-generating
package, both are relying on dependencies.

**Dependency graph.** GitHub's internal map of every dependency your repository uses, and every
dependency those dependencies use in turn. This is what the next two features are built on top of.

**Dependabot alert.** A notice that one of your dependencies has a known security problem. GitHub's
own wording: "Dependabot alerts notify you about vulnerable dependencies so you can upgrade to secure
versions and protect your project."

**Dependabot security update.** A separate, optional feature that goes one step further than an
alert: instead of just telling you about a problem, it opens a pull request that fixes it for you.
GitHub's own wording: "Dependabot will automatically try to open pull requests to resolve every open
Dependabot alert that has an available patch."

**GitHub Advisory Database.** GitHub's own running list of known security problems in publicly
available software packages, reviewed by GitHub staff before they count as confirmed. This is where
Dependabot alerts come from. GitHub's own wording: "If you enable Dependabot alerts for your
repositories, you are automatically notified when a new GitHub-reviewed advisory reports a
vulnerability for a package you depend on."

**Repository security advisory.** A separate, optional tool for privately discussing and fixing a
vulnerability in your own project before telling the world about it. GitHub's own wording:
"Repository security advisories allow maintainers of public repositories to privately discuss and fix
a security vulnerability in a project." Covered briefly below, mainly so you recognise it if you ever
see it, most readers of this kit will not need to use it themselves.

**Security and quality tab.** The one place on a repository where every alert from every feature in
this file collects, so you never need to remember five different places to check.

## How to do it

### What happens automatically, and what does not

Not every feature in this file behaves the same way, and the difference matters enough to state
plainly before anything else.

**On a public repository**, secret scanning and push protection for it are already running, for
free, without you doing anything. GitHub's own wording: "Secret scanning runs automatically for
free" on public repositories.

**On a private repository owned by an individual account, not an organization**, secret scanning is
not available at all short of GitHub's largest enterprise plans. GitHub's own wording, for
user-owned repositories specifically: "Available on GitHub Enterprise Cloud with Enterprise Managed
Users. Available on GitHub Enterprise Server when the enterprise has GitHub Secret Protection
enabled." In plain terms: if you are a solo operator with a private repository under your own
personal account, not an organization, this kit could not find a paid tier that turns secret scanning
on for you. **This is exactly the gap `10-protecting-your-work.md` and this kit's rule against
committing secrets exist to cover.** If you are in this situation, the discipline of never typing a
real password or key into a file that gets committed is not a backup plan, it is your actual defence.

**On a private repository owned by an organization**, secret scanning becomes available as a paid
add-on. GitHub's own wording: "Available with GitHub Secret Protection enabled on GitHub Team or
GitHub Enterprise Cloud." Because push protection is described in GitHub's own words as "a secret
scanning feature," the same split applies to it: automatic and free on public repositories, a paid
organization feature on private ones.

**Dependabot alerts sit apart from all of that.** GitHub lists "Dependabot alerts" as a plain GitHub
Free feature, not something gated behind a paid tier, and its own configuration page describes
turning it on as something you do yourself: "Repository administrators and organization owners can
enable Dependabot alerts for their repositories and organizations. When enabled, GitHub immediately
generates the dependency graph and creates alerts for any vulnerable dependencies it identifies."
This kit could not confirm from GitHub's own pages whether a brand-new repository already has this
switched on by the time you first look, or whether it is always an extra step. Check your own
repository's settings, covered next, rather than assuming either way.

### Turning on Dependabot alerts

1. From the main page of your repository, click **Settings**.
2. In the left sidebar, click **Advanced Security**.
3. Find **Dependabot alerts** in the list, and click **Enable** next to it.

**Confirmation:** the button next to Dependabot alerts now reads **Disable** instead of **Enable**,
and GitHub's own wording is that it "immediately generates the dependency graph and creates alerts
for any vulnerable dependencies it identifies," so if your project has an existing problem, you
should see it appear on the Security and quality tab within a short time, not after a wait.

**Fallback:** if you do not see an **Enable** button, or the whole **Advanced Security** page looks
different from this description, GitHub may have moved the page since this was checked, or you may
not have administrator access to this repository. Confirm your access level in
`03-members-and-access.md` before assuming the page itself is broken.

### Turning on secret scanning, on a private organization repository

This only applies if your repository is owned by an organization on GitHub Team or GitHub Enterprise
Cloud, and the organization has purchased GitHub Secret Protection. If either of those is not true,
this option will not appear, and that is expected, not a fault, see above.

1. From the main page of your repository, click **Settings**.
2. In the left sidebar, click **Advanced Security**.
3. If **Secret scanning** appears in the list, click **Enable** next to it.

**Confirmation:** the button changes to **Disable**, and any secret already sitting in your
repository's history at the time you turn this on gets scanned and, if something is found, an alert
appears on the Security and quality tab.

**Screenshot placeholder:** the Advanced Security settings page, showing the Dependabot alerts and
Secret scanning rows side by side with their Enable and Disable buttons, so a reader can see exactly
which row is which before clicking either one.

### Finding the Security and quality tab

On the main page of your repository, along the row of tabs across the top, alongside **Code**,
**Issues**, **Pull requests**, and **Projects**, look for a tab labelled **Security and quality**.

**Confirmation:** the page that opens is headed **Security**, and lists sections including a
security policy status and any published security advisories, with every open alert from secret
scanning, push protection, and Dependabot collected in one place underneath.

**Fallback:** if you do not see this tab at all, you most likely have Read access rather than Write
access to this repository, since GitHub's own wording restricts who can see security alerts to
people with "write, maintain, or admin access." Check your access level in
`03-members-and-access.md`.

### Reading a Dependabot alert once you have one

From the Security and quality tab, click the **Dependabot** dropdown menu, then click
**Vulnerabilities**. GitHub's own wording for what an individual alert shows: "A link to the affected
file, Details about the vulnerability and its severity, Information about a fixed version (when
available)."

In plain terms, an alert is answering three questions for you: which piece of software has the
problem, how serious GitHub considers it, and whether a fixed version already exists that would make
the problem go away. That third answer is the one that decides what you actually do next, covered
under Strategy below.

If you decide an alert does not need action right now, you can dismiss it, and GitHub asks you to
choose a reason first. If you later change your mind and it has not already been fixed, GitHub's own
wording confirms you can reopen it: "Alerts that have already been fixed cannot be reopened," which
means anything still open remains reversible.

### When Dependabot fixes it for you

Dependabot security updates are a separate switch from Dependabot alerts, and GitHub's own wording is
plain about the relationship: this feature "is available for repositories where you have enabled the
dependency graph and Dependabot alerts." Once it is on, Dependabot does not just tell you a fix
exists, it opens a pull request containing that fix, ready for someone to review.

**Treat that pull request exactly like any other pull request, not as something to merge on sight.**
`07-pull-requests.md` covers reviewing one properly. A dependency update can occasionally change how
something behaves, not just patch a security hole, so the same "does this still work" check you would
give any other change still applies, it is simply Dependabot that wrote the change instead of a
person.

### Repository security advisories, briefly

This one is worth knowing exists, even though most readers of this kit will not use it directly.
GitHub's own wording restricts it to public repositories: "Repository security advisories allow
maintainers of public repositories to privately discuss and fix a security vulnerability in a
project." If you ever publish something on a public repository and someone finds a security problem
in it, this is the tool that lets you fix it quietly first, in a temporary private space, before
telling anyone the problem existed at all. If your work stays on private repositories, as most of
this kit's audience's does, you are unlikely to ever need this one.

### What to do when an alert appears and you do not understand it

This is the realistic case, and there is nothing wrong with it. Nobody reading this kit is expected
to already know what a given vulnerability means.

1. **Read what the alert actually says first**, not just its title. GitHub's own alert format
   already gives you the affected file, the severity, and whether a fixed version exists, which is
   most of what a decision needs.
2. **If a fixed version is listed, that is usually the whole answer.** Updating to it, either by
   hand or by merging Dependabot's own pull request if it opened one, closes the alert.
3. **If you genuinely cannot follow what the alert is describing, paste its text to Claude Code and
   ask it to explain what the problem actually is, in plain English, and what updating would
   involve.** This is a genuinely good use of it: reading and explaining a technical notice, not
   deciding your security posture for you.
4. **If nobody involved, including Claude Code, can tell you with confidence what a fix would break,
   that is a signal to bring in someone technical before merging anything**, not a reason to ignore
   the alert. `12-when-things-go-wrong.md` covers getting unstuck more generally.

### Doing this through Claude Code

You will not turn any of these features on through Claude Code. Enabling Dependabot alerts, enabling
secret scanning, and reading the Security and quality tab are all signed-in-as-you actions on GitHub's
own settings screens, the same category as creating an organization or protecting a branch. Claude
Code cannot click a toggle that needs GitHub to see you specifically.

What Claude Code *can* usefully do here: explain an alert's plain meaning if you paste it in,
explain a push protection rejection message if a push it made on your behalf gets blocked, and help
you update a flagged dependency to the version GitHub names as fixed, once you tell it which one.
Reading a technical message back to you in plain English is exactly the kind of thing worth handing
over.

## Strategy: how to actually use this

**Turn on Dependabot alerts even if you are working alone.** It costs nothing, GitHub lists it as a
GitHub Free feature, and it answers a question you cannot easily answer yourself: whether any piece
of software your project depends on has since been found to have a known problem. There is close to
no cost to having it on and simply not acting on every alert the moment it appears.

**Do not assume secret scanning is protecting you if you are solo on a private, personal-account
repository.** As covered above, this kit could not find a paid tier that turns it on for that
specific situation. If that describes your setup, the actual defence is the habit `10-protecting-your-
work.md` already covers: never type a real password or key into a file that gets committed, and if
one ever does slip through, rotate it in the service that issued it immediately, do not wait for a
scanner to catch it, because for you, nothing is watching.

**A solo operator's realistic routine** is to glance at the Security and quality tab occasionally,
not on a schedule, and act on anything that shows a fixed version already exists, since that is
close to zero-effort. Anything more involved than that is usually not worth a solo operator's time
unless the alert is marked as high severity.

**A team with someone technical in it** gets more value from turning on Dependabot security updates
as well, so fixes arrive as ready-to-review pull requests instead of alerts someone has to act on by
hand. The technical person becomes the one who reviews and merges those pull requests, the same way
they would review any other change.

**What good looks like months later** is not a Security and quality tab with zero alerts ever shown,
new vulnerabilities get discovered in existing software constantly, that is a normal, ongoing fact of
using anyone else's code. What good looks like is a tab where nothing sits open for months
unexplained, and where a dismissed alert has an actual reason attached to it, not silence.

## A worked example

The café's ordering site, built and maintained by the owner's nephew, has Dependabot alerts turned
on. One morning, a new alert appears: a JavaScript package the site's checkout page depends on has a
newly discovered vulnerability, marked high severity, with a fixed version already available.

The nephew does not fully understand the vulnerability's description on sight. He copies the alert's
text into Claude Code and asks what it means in plain English. Claude Code explains that the flaw
could, in principle, let an attacker read data they should not be able to see, and that updating to
the fixed version resolves it with no other changes needed on the nephew's part. Because Dependabot
security updates are also switched on, a pull request titled with the fix is already sitting open,
waiting for review. The nephew checks that the ordering site still works correctly with the update
applied, following `07-pull-requests.md`'s review steps, then merges it. The alert closes itself
automatically once the fix lands.

Separately, the café owner is working on a private repository she made herself, not through the
organization, to store a spreadsheet of supplier contacts. She has no reason to expect secret
scanning to be watching that repository, because it is a personal private repository, not an
organization one, and this kit could not confirm any tier that covers that case. She never types
anything as sensitive as a password into it anyway, which is the actual reason it stays safe, not a
GitHub feature working quietly in the background.

## If it goes wrong

**An alert appeared and I have no idea what it means.** Read the alert's own text first, it names
the affected file, the severity, and whether a fixed version exists. If it still does not make
sense, paste it to Claude Code and ask for a plain-English explanation, that is a genuinely good use
of it.

**Dependabot opened a pull request and I am nervous about merging it.** That caution is reasonable,
not excessive. Review it the same way you would review any pull request, following
`07-pull-requests.md`, and confirm the thing it changes still works before merging. A dependency
update fixing a security hole can occasionally change other behaviour too.

**I do not see a Security and quality tab, or an Enable button, at all.** This almost always means
you have Read access to the repository rather than Write. GitHub's own wording restricts visibility
of security alerts to people with "write, maintain, or admin access." Check `03-members-and-access.md`
or ask whoever administers the repository to raise your access.

**I got a push protection rejection and I am confident it is a false alarm, not a real secret.**
Push protection has a bypass for exactly this situation, GitHub's own wording confirms "anyone with
write access to the repository can bypass push protection by specifying a bypass reason." Use it
honestly. If you are wrong and it genuinely was a real secret, rotate it in whatever service issued
it immediately, `10-protecting-your-work.md` covers this in full.

**I turned on Dependabot alerts and nothing appeared, even though I expected a problem.** That is a
genuinely good result, not a sign the feature is broken, it means no vulnerability in GitHub's
Advisory Database currently matches anything your repository depends on. New advisories get added
constantly, so this can change later without you doing anything differently.

## FAQ

**Does turning these features on slow anything down?** No. None of the features in this file change
how your repository behaves day to day. Secret scanning and push protection act at the moment
something is pushed, not while you are working. Dependabot alerts run in the background and simply
add to a list you check when you choose to.

**Do I have to fix every alert the moment it appears?** No. An alert is information, not a deadline.
Fixing the ones with an available patch is usually close to effortless, so there is rarely a reason
to leave those sitting, but nothing about the feature forces immediate action, and dismissing an
alert with a genuine reason is a normal, supported option.

**What if nobody on my team is technical enough to understand an alert?** Paste the alert's text into
Claude Code and ask what it means, that is exactly the kind of explaining it is good at. If the fix
itself turns out to need judgement Claude Code cannot confidently give you, that is the point to
bring in someone technical, not to ignore the alert.

**Does any of this mean my business is now protected from being hacked?** No, and this is the most
important thing in this file. These features catch two specific things: a secret accidentally pushed
into your repository, and a dependency with a publicly known problem. They say nothing about weak
passwords on your other accounts, phishing emails your staff might click, a secret stored somewhere
other than a repository, like a spreadsheet or a chat message, or a mistake in logic you wrote
yourself that has nothing to do with a leaked credential or an outdated package. Treat this file as
one part of staying safe, not the whole of it.

**Does secret scanning catch a password I paste into an issue or a comment, not a file?** This kit
could not confirm that from GitHub's own pages one way or the other. Treat anything you type into
GitHub, in a file, a comment, an issue, or anywhere else, as something you would not mind a stranger
reading, and you will not need the answer to matter.

**If my private repository is not covered by secret scanning at all, is there anything else I can
do?** Yes, the same thing this kit recommends regardless of which tier you are on: never type a real
password, key, or token into a file that gets committed in the first place. That habit works
identically whether or not a scanner is watching, and for a solo operator on a personal private
repository, it is genuinely the only defence this file can point you to.

## Quick reference

- **Secret scanning, public repos:** automatic, free, already on
- **Secret scanning, private repos:** organization-owned only, paid, GitHub Team or Enterprise Cloud
  with GitHub Secret Protection; not available for a personal account's private repository outside
  Enterprise
- **Push protection:** same coverage as secret scanning above; has a bypass anyone with write access
  can use by giving a reason
- **Dependabot alerts:** GitHub Free feature, turn on at Settings, **Advanced Security**, **Enable**
  next to Dependabot alerts
- **Dependabot security updates:** separate switch, needs alerts already on, opens a pull request
  with the fix instead of just an alert
- **Where every alert collects:** the **Security and quality** tab on the repository's main page
- **Who can see alerts:** Write, Maintain, or Admin access, or organization owners
- **Confused by an alert:** paste its text to Claude Code and ask what it means
- **What this does not cover:** weak passwords elsewhere, phishing, secrets stored outside a
  repository, mistakes in your own logic

## Sources

- https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning
- https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
- https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts
- https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts
- https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates
- https://docs.github.com/en/code-security/security-advisories/repository-security-advisories/about-repository-security-advisories
- https://docs.github.com/en/code-security/security-advisories/global-security-advisories/about-the-github-advisory-database
- https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository
- https://docs.github.com/en/get-started/learning-about-github/githubs-products
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository
- https://github.com/selrai-company/github-training-content/security (live check against the kit's own
  practice repository, confirming the tab's current label and position)
