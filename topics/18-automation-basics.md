# Automation, what GitHub can do while you sleep

## What this gets you

GitHub can carry out instructions for you automatically, the moment something specific happens in
your repository. Not "you remember to run a check every Friday." Something happens, GitHub notices,
and it does the thing, whether anyone is at a computer or not. GitHub's own name for this feature is
**GitHub Actions**, described in its own documentation as "a continuous integration and continuous
delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline."
(See Sources.)

In plain terms, that means things like: every time someone proposes a change to your website's
code, a check runs before anyone approves it, catching an obvious mistake before it goes live, not
after a customer notices. Or something runs every night on a fixed schedule, without anyone needing
to remember to start it. Or something happens automatically the moment a new issue is raised, rather
than waiting for a person to notice it.

For a small business, the value is the same shape every time: a repetitive check that a person would
otherwise have to remember to do by hand, done instead by the repository itself, consistently, on
time, whether or not anyone is watching.

**Be honest with yourself about this one:** most people using this kit will never write one of these
from scratch. That is a job that leans technical, and it is genuinely fine to leave it to a technical
teammate, or to a tool that sets one up for you as part of something else you installed. What you do
need is to recognise one when you see it, read it well enough to have a rough idea what it does, know
whether it passed or failed, and know how to turn it off if it is doing something you do not want. That
is what this file teaches.

## Before you start

**You need a repository**, ideally one where a technical teammate, or a tool you installed, has
already set at least one of these up. If nothing has, the practice repository at
`https://github.com/selrai-company/github-training-content` is a safe place to look at a real one
without any risk to your own work.

**You need at least Read access to the repository** to see what is running. GitHub's own
documentation on viewing this describes it as something anyone with "read access to the repository"
can do. `03-members-and-access.md` covers checking your own access level if you are not sure what
you have.

**You do not need to already understand branches or pull requests**, but the most common place
you will actually see this in daily use is on a pull request, where a pass or fail shows up before
anyone approves the change. `07-pull-requests.md` covers pull requests from the ground up if you
have not met them yet.

**This file does not teach you to write one.** Writing a workflow file from scratch, deciding what
it should check, and getting the wording right is a task for a technical teammate, or for asking
Claude Code to do it for you as a specific, deliberate project, not something covered step by step
here. What follows is about recognising, reading, and controlling what already exists.

## The words you need

**GitHub Actions.** The name of the whole feature: instructions GitHub carries out for you
automatically. GitHub's own wording, quoted above: "a continuous integration and continuous
delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline."

**Workflow.** One specific set of automated instructions. GitHub's own description: "A workflow is
a configurable automated process that will run one or more jobs. Workflows are defined by a YAML
file checked in to your repository and will run when triggered by an event." A repository can have
several workflows, each doing something different.

**Workflow file.** The actual text file a workflow is written in. GitHub's own wording for where it
lives: "Workflows are defined in the `.github/workflows` directory in a repository." That is a
folder named `.github`, containing a folder named `workflows`, sitting alongside your other files.
It is a differently formatted kind of text file than the Markdown this kit covers in
`14-markdown-and-writing.md`, so what that file taught about formatting text does not carry over
directly, though reading one is still mostly reading plain English once you know what each part
means, covered below.

**Trigger, also called an event.** What starts a workflow running. GitHub's own wording: "An event
is a specific activity in a repository that triggers a workflow run. For example, an activity can
originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a
repository." A workflow can also be set to trigger on a schedule, or to be started by hand, both
covered below.

**Job.** One task inside a workflow. GitHub's own wording: "A job is a set of steps in a workflow
that is executed on the same runner." A workflow can have one job or several.

**Step.** One instruction inside a job, run in order. GitHub's own wording: "Each step is either a
shell script that will be executed, or an action that will be run."

**Action.** A ready-made, packaged step someone else has already written, that a workflow can reuse
instead of writing the instruction out by hand. This is confusing because the whole feature is also
called "GitHub Actions." Read "an action" as one reusable ingredient, and "GitHub Actions" as the
kitchen the ingredient gets used in. Actions are published in a catalogue GitHub calls the
**Marketplace**, and this distinction matters directly for the security point later in this file.

**Runner.** The computer that actually carries out a workflow's instructions, provided by GitHub
unless someone has deliberately set up their own. GitHub's own wording: "A runner is a server that
runs your workflows when they're triggered. Each runner can run a single job at a time." Most small
business workflows run on GitHub's own standard Linux runner, which is also the cheapest option,
covered under cost below.

**Workflow run, or just a run.** One specific time a workflow actually executed, with its own record
of what happened, when, and whether it succeeded.

**Secret.** A password, key, or other sensitive value stored on the repository so a workflow can use
it without that value ever appearing in the workflow file itself, where anyone with Read access
could otherwise see it. Secrets matter directly to the security point later in this file, because a
workflow that uses one is a workflow with real access to something private.

**Check.** The pass or fail result a workflow leaves behind, most visibly the one shown directly on
a pull request before anyone approves it. `10-protecting-your-work.md` covers making a check
required before a change can merge at all; this file covers where a check actually comes from.

## How to do it

### Seeing what automation already exists on a repository

**The landmark and path.** On the repository's main page, along the top, in the row of tabs that
starts with **Code** and **Issues**, look for a tab labelled **Actions**, marked with a play-style
icon. Click it.

**The confirmation.** You will see a left-hand list of every workflow set up on this repository, each
named individually, with a history of its runs on the right, each one showing whether it succeeded or
failed.

**The fallback.** If you cannot see an **Actions** tab, or the list is empty, that usually means
either you only have limited access to this repository, or nobody has set any automation up on it
yet. Neither is a fault.

### Reading a workflow file well enough to know what it does

You do not need to understand every line. You need to be able to answer three questions: what starts
it, what does it do, and where does it run. Every workflow file answers those in roughly the same
shape, GitHub's own quickstart example, reproduced here, shows the pattern clearly:

```yaml
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "This job was automatically triggered by a push event."
      - name: Check out repository code
        uses: actions/checkout@v6
      - run: echo "The workflow is now ready to test your code on the runner."
```

Read it top to bottom, and it decodes like this:

- **`name:`** is the label you see in the Actions tab's list. This one is called "GitHub Actions
  Demo."
- **`on:`** is the trigger. This one runs `on: [push]`, meaning every time someone pushes a commit.
  Other common triggers you will see: `pull_request` (runs when a change is proposed),
  `schedule` (runs at a set time, GitHub's own wording: "The `schedule` event allows you to trigger
  a workflow at a scheduled time"), `issues` (runs when an issue is opened or changed, relevant if
  you are also using `13-issues-and-tracking-work.md`), and `workflow_dispatch` (adds a manual **Run
  workflow** button so a person can start it on demand instead of waiting for a trigger).
- **`jobs:`** lists what actually happens, one or more tasks, each with its own name.
- **`runs-on:`** says which kind of computer carries it out. `ubuntu-latest` is GitHub's standard,
  cheapest option, and what most small business workflows use, covered under cost below.
- **`steps:`** is the ordered list of instructions inside that job. A line starting with `run:` is a
  plain command. A line starting with `uses:` is pulling in someone else's packaged action rather
  than writing the instruction from scratch, in this example, `actions/checkout@v6`, an action
  published by GitHub itself that fetches your repository's files onto the runner so later steps
  can work with them.

**Where to find one on your own repository.** Click **Code**, the first tab along the top, then
open the `.github` folder, then the `workflows` folder inside it, then click any file ending in
`.yml` to read it.

**Through Claude Code**, if you would rather have it explained in plain English than decode the file
yourself:

```
Read the workflow file at .github/workflows/check.yml and explain in plain English what it does and
what triggers it.
```

Claude Code can also read one straight from GitHub without you needing to find the file first, the
equivalent of GitHub's own `gh workflow view --yaml` command, described in GitHub's own documentation
as a way to "view the workflow yaml file."

### Telling whether a run passed or failed

On the **Actions** tab, each run in the list shows as failed, marked with a red cross, or succeeded,
marked with a green tick. Click any run to open it. GitHub's own description of what you land on:
a summary showing "status for each job and step in a workflow," so you can see exactly which part, if
any, did not succeed.

The same pass or fail also shows up directly on a pull request, usually before the option to approve
and merge it, which is the version of this most people using this kit will actually see day to day.
Do not approve or merge a pull request showing a failed check without asking whoever set the
automation up what it means, the same way you would not wave through an inspection you knew had
failed.

### Turning off one specific automation

**The path.** Open the **Actions** tab, click the workflow you want to stop in the left-hand list, then
look for a small menu, GitHub's own name for it is "Show workflow options," shown as three dots.
Click it, then click **Disable workflow**.

**The confirmation.** The workflow stops appearing in the default list, and stops running when its
trigger happens. It is not deleted, its file is untouched, and you can bring it back the same way,
the menu option becomes **Enable workflow** once it is off.

**The access this needs.** GitHub's own permissions table groups editing, running, and disabling
workflows together with Write access and above. If the option is not there for you to click, that is
the likely reason; `03-members-and-access.md` covers checking or requesting a higher access level.

**Through Claude Code**, once `gh` is set up as covered in `11-github-with-claude-code.md`:

```
Disable the workflow called "Check the website builds" in this repository.
```

which runs the equivalent of `gh workflow disable`, GitHub's own description: "Disable a workflow,
preventing it from running or showing up when listing workflows." To see everything, including ones
already turned off:

```
List every workflow in this repository, including any that are disabled.
```

which runs the equivalent of `gh workflow list --all`, since GitHub's own documentation notes this
command normally hides disabled workflows unless you ask for all of them.

### Turning off automation for the whole repository

This is a different, larger switch than disabling one workflow: it stops every workflow in the
repository from running at all, and it belongs to the same category as the settings covered in
`10-protecting-your-work.md`, an admin-only, signed-in-as-you change made in the browser, not
something to hand to Claude Code.

**The path.** Open the repository's **Settings** tab. In the left sidebar, click **Actions**, then
**General**. Under **Actions permissions**, choose **Disable all**.

**The confirmation.** GitHub's own wording for the effect: with this selected, "no workflows run in
your repository." Nothing is deleted, the workflow files stay exactly where they were, they stop
being run and nothing more.

**The fallback.** If you cannot see a **Settings** tab at all, you are not an administrator of that
repository, covered under `NAVIGATION-STYLE.md`'s general rule for this. If the options under
**Actions permissions** are greyed out or will not change, an organization or enterprise policy above
this repository may be fixing that setting for every repository underneath it, and only whoever
administers that level can change it.

### Checking what it has cost you so far

**The path.** Open your own account settings and look for the billing area, `github.com/settings`
then a **Billing** section, GitHub's own documentation points here as "viewing your usage of metered
products and licenses." The exact layout of this page can differ depending on your plan, so confirm
on your own screen what it shows once you are there; look for a section naming GitHub Actions minutes
used this month.

This is a billing action tied to your own identity, in the same category as the other browser-only,
signed-in-as-you actions this kit keeps out of Claude Code's hands, `01-accounts-and-security.md` and
`11-github-with-claude-code.md` cover why.

## Strategy: how to actually use this

**A solo operator with no technical teammate** will mostly encounter this file's territory as a
passenger, not a driver: a website builder, a template, or a kit you installed may have set an
automation up on your behalf, and your job is limited to recognising the pass or fail marker and not
approving a change that failed one. The decision rule worth having, stated plainly: do not go looking
for automations to add from the internet yourself. If you want one, ask a technical teammate, or ask
Claude Code to build a specific one for you as a deliberate task, and then treat the reading, checking,
and turning-off skills in this file as the part that stays yours.

**A team with one technical person** (this kit's recurring example is the café and its ordering
site, run day to day by a technical nephew) gets the most out of this the moment a proposed change to
something customer-facing, the ordering site, a price list feeding into it, needs a check before it
goes live. The technical person sets the workflow up once. The owner's ongoing job is small and
concrete: glance at the pass or fail marker on a pull request before approving it, and know which
menu turns a misbehaving automation off if one starts failing repeatedly or something looks wrong.

**What good looks like months later:** a short list of named workflows on the **Actions** tab, each
one you, or whoever runs the repository day to day, could describe in one sentence without opening
the file. Not a long list of automations nobody remembers adding. Not zero, if there is real
repetitive checking this could be doing instead. A monthly minutes total, checked occasionally on the
billing page, that roughly matches what you would expect from what is actually running.

**When it is not worth bothering with at all:** a repository that is really just documents, price
lists, or notes, with nobody proposing changes that need catching before they go live. Automation
earns its keep on repetitive checking a person would otherwise have to remember to do by hand.
Nothing here needs a workflow just because the feature exists.

## A worked example

The café's ordering site has one workflow set up by the nephew, named "Check the site still builds,"
triggered `on: pull_request`, meaning it runs automatically every time anyone proposes a change to
the site's code. It does one job: attempt to build the website exactly the way it would be built for
real customers, and report whether that succeeded.

A few months in, the owner wants a small wording change on the delivery page. She does not write the
code herself, but she does open the pull request the nephew made for the change, and before clicking
approve, she looks at the check underneath it. It shows a green tick next to "Check the site still
builds." She knows, without reading a line of code, that the site still works with this change in it,
and approves it.

A different week, the nephew proposes a bigger change, and the same check comes back with a red
cross. The owner does not try to diagnose why. She recognises the failure, does not approve the
change, and messages the nephew that the check failed, which is exactly the outcome this kind of
automation exists to produce: a mistake caught before it reached a customer, by someone who does not
read code at all.

## If it goes wrong

**A run shows as failed and I do not know why.** That is expected to be outside what you diagnose
yourself. Your job is to recognise the failure and not proceed past it, then hand the specific run
to whoever set the automation up, or to Claude Code, to look into. Clicking into the failed run does
show more detail, GitHub's own wording is that it breaks down "status for each job and step," but
reading that detail productively is a technical task.

**Actions stopped running partway through the month, or a bill turned up unexpectedly.** GitHub's
own documentation is direct about what happens once your account's free monthly minutes are used up:
"If your account does not have a valid payment method on file, usage is blocked once you use up your
quota." If a payment method is on file, GitHub begins charging automatically for minutes beyond the
free allowance instead of blocking anything. Either way, GitHub's own wording confirms the free
allowance resets on a fixed cycle: "At the start of each month, the minutes used by the account are
reset to zero." Check the billing page above to see which situation you are actually in.

**A scheduled automation that used to run seems to have quietly stopped.** In a public repository,
GitHub automatically turns off a schedule-triggered workflow after a period with no other activity
on the repository, GitHub's own wording: "In a public repository, scheduled workflows are
automatically disabled when no repository activity has occurred in 60 days." Re-enable it the same
way covered above under turning off one specific automation, in reverse.

**I cannot find the Actions tab at all, or every option under it is greyed out.** Either the whole
repository has Actions turned off under **Settings**, covered above, or an organization or
enterprise-level policy above this repository is enforcing that for every repository underneath it.
Whoever administers that higher level is the person who can change it, not you at the repository
level.

**Something is running that I do not recognise and did not knowingly add.** Treat this the same way
you would treat unfamiliar software you found installed on a computer you are responsible for: do not
assume it is fine because nothing has visibly gone wrong yet. Open it, read what it does using the
guide above, check who added it and when on the file's own history, and if you cannot account for it,
disable it while you find out, covered above under turning off one specific automation.

## FAQ

**Do I have to learn to write one of these?** No. Most people using this kit never will, and this
file deliberately does not teach it. What you need is the ability to recognise, read, and turn off
automation that already exists, which is everything covered above.

**Is this the same thing as the required checks covered in `10-protecting-your-work.md`?** Related,
not the same. A workflow is where a check actually comes from, the thing that runs and decides pass
or fail. `10-protecting-your-work.md` covers a separate decision: whether a check is allowed to be
ignored, or must pass before a change can merge at all. You can have workflows without ever making
any of them required, and you can only make one required once it exists.

**What is the actual difference between "GitHub Actions" and "an action"?** GitHub Actions is the
whole feature, the platform that runs your automated instructions. An action is one specific,
reusable, packaged instruction someone has already written, that a workflow can pull in with a
`uses:` line instead of writing the step out by hand. GitHub's own naming genuinely overlaps here;
it is not a case of you having misunderstood something.

**Can adding someone else's action from the Marketplace be a real risk?** Yes, and this is the one
security point in this file worth taking seriously. GitHub's own security guidance states it
plainly: "a compromise of a single action within a workflow can be very significant, as that
compromised action would have access to all secrets configured on your repository, and may be able
to use the `GITHUB_TOKEN` to write to the repository." In plain terms, an automation someone else
wrote runs with real access to your repository, including anything you have stored as a secret.
GitHub's own recommendation, where you are choosing to use one at all, is to "be sure that you trust
the action's creators" rather than adding one because it happened to appear in a search. Adding an
automation written by someone else is a decision, not a routine step, the same category of decision
as installing software from an unfamiliar source. If you are not confident judging that yourself,
that judgement is exactly what a technical teammate is for.

**Will turning off Actions for the whole repository break anything else, like pull requests?** No.
Pull requests, branches, and everything else this kit covers keep working exactly the same. What
stops is only the automated checks and tasks that used to run on top of them, any check built with a
workflow will no longer report anything.

**Does disabling a workflow delete it?** No. GitHub's own wording for what disabling does:
"preventing it from running or showing up when listing workflows" by default. The file itself is
untouched, and re-enabling it brings it straight back.

## Quick reference

- **See what is set up:** repository page, **Actions** tab
- **Read what one does:** **Code** tab, `.github` folder, `workflows` folder, open the `.yml` file;
  check its `name:`, `on:`, `jobs:`, and `steps:`
- **Check pass or fail:** **Actions** tab for the full history, or directly on a pull request before
  approving it
- **Turn one off:** **Actions** tab, pick the workflow, **Show workflow options** (three dots),
  **Disable workflow**
- **Turn off everything on a repository:** repository **Settings**, **Actions**, **General**,
  **Actions permissions**, **Disable all**
- **Check the bill:** your own account **Settings**, **Billing**
- **Free allowance:** resets at the start of each month; a private repository draws down a monthly
  minutes quota depending on your plan; a public repository's standard runners are free
- **Through Claude Code:** "Explain what this workflow file does", "Disable the workflow called X",
  "List every workflow, including disabled ones"
- **The one judgement call that matters:** adding someone else's action gives it real access to your
  repository and its secrets. Treat it as a decision, not a routine step.

## Sources

- https://docs.github.com/en/actions/get-started/understanding-github-actions
- https://docs.github.com/en/actions/writing-workflows/quickstart
- https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows
- https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history
- https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows
- https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization
- https://docs.github.com/en/billing/concepts/product-billing/github-actions
- https://docs.github.com/en/billing/how-tos/products/view-productlicense-use
- https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions
- https://cli.github.com/manual/gh_workflow_list
- https://cli.github.com/manual/gh_workflow_disable
- https://cli.github.com/manual/gh_workflow_view
- https://cli.github.com/manual/gh_run_list
