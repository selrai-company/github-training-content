# Notifications, and not drowning in them

The most common reason a person quietly stops using GitHub is not that it is too hard. It is that
it becomes noise: every day brings a pile of emails and a red dot they stop reading, and after a
few weeks they stop opening GitHub at all, which means the one or two things in that pile that
genuinely needed them get missed along with everything else. This file is about the opposite
outcome, an inbox that stays small enough to trust, so the alerts that arrive are ones worth
opening.

## What this gets you

Right now, if notifications feel like noise, you are probably choosing between two bad options:
read everything, which eats an hour a week you do not have, or ignore the pile, which means the
one message that actually needed a decision from you, someone asking you to check their work, or
someone asking you a direct question, is sitting unread next to a hundred updates that did not
need you at all. Once your notifications are set up properly, that stops being a choice. Routine
activity stays quiet in the background where you can check it when you choose to, and the two
things that genuinely need a response from you, being asked a direct question and being asked to
review someone's work, surface on their own. That is the entire value of this file: turning "I
have 400 unread things" into "I have two things to look at this morning," without missing
anything that actually mattered.

## Before you start

You need a GitHub account with access to at least one repository (a folder for one project, kept
online, where a record is saved every time anyone changes anything). Nothing else has to be set up
first, everything in this file is a setting on your own account.

You will get more out of this file if you have already read `05-daily-workflow.md` (so you know
what a comment and a commit are) and `07-pull-requests.md` (so "being requested for review," one
of the two reasons that actually need you, means something concrete). If you are not using pull
requests yet, the review-request part of this file will not come up for you, and you can skip
straight past it.

## The words you need

**A notification.** An update GitHub sends you because something happened that you are subscribed
to. GitHub's own description of what can trigger one: "a conversation in a specific issue, pull
request, or gist," "all activity in a repository," "CI activity, such as the status of workflows in
repositories set up with GitHub Actions," or a repository's "issues, pull requests, releases,
security alerts, or discussions."

**Watching a repository.** Manually subscribing to a repository so you hear about activity in it,
by clicking **Watch** on that repository's page.

**Participating.** Anytime you comment on something, or someone directly types your username with
an `@` in front of it (being "@mentioned"), you are participating in that conversation. GitHub
subscribes you to that specific conversation automatically the moment this happens, whether or not
you are watching the repository it is in.

**Ignoring a repository.** Turning off every notification from one repository, including the ones
that would otherwise reach you because you were mentioned or asked to review something. GitHub's
own caution about this: "we don't recommend ignoring repositories as you won't be notified if
you're @mentioned."

**The notifications inbox.** The page at `https://github.com/notifications` where every
notification you have not unsubscribed from or marked as handled shows up in one list.

**A reason label.** A small tag GitHub attaches to every notification in your inbox, telling you in
one or two words why you received it, for example `mention` or `review requested`. You can search
your inbox for one reason at a time.

**Being requested for review.** Someone has specifically asked you, by name, to look at a proposed
change (a pull request, covered in `07-pull-requests.md`) before it is accepted. This is one of the
two reasons in this file that genuinely need your attention, not just your awareness.

**Unsubscribing, as distinct from unwatching.** Unsubscribing stops one specific conversation from
notifying you again. Unwatching stops an entire repository from notifying you about general
activity, while still allowing conversations you are personally mentioned in or participating in to
reach you.

**Done.** Marking a single notification as handled, which removes it from your inbox. GitHub still
keeps a record of it for a while, covered below, in case you need to find it again.

**Saved.** Flagging a notification to come back to later. Unlike a notification you leave sitting
in your inbox, a saved one is kept indefinitely rather than being cleared out automatically.

**A custom filter.** A search you set up once inside your notifications inbox, so it shows only a
slice of your notifications, for example only the ones from one repository, whenever you click it.

**The subscriptions page.** A separate page, at `https://github.com/notifications/subscriptions`,
listing every conversation and repository you are currently subscribed to, including ones you have
already marked Done in your inbox. Useful for finding subscriptions you forgot you had, since your
inbox only shows what is still outstanding.

## How to do it

### What actually causes a notification

Two different things generate notifications, and it helps to keep them separate in your head.

The first is deliberate watching, covered in the next section, where you tell GitHub "keep me
posted on this repository."

The second is automatic, and GitHub's own documentation lists exactly when it subscribes you to a
conversation without you asking:

- You were assigned to an issue or pull request.
- You opened the issue or pull request.
- You commented on it.
- You clicked **Watch** or **Subscribe** on it directly.
- You were @mentioned by username.
- The state changed on something you are involved in, for example an issue you opened was closed,
  or a pull request you commented on was merged.
- A team you belong to was @mentioned.

GitHub also states plainly that, "in general," you are subscribed by default whenever you have
"not disabled automatic watching for repositories or teams you've joined," adding that "this
setting is enabled by default." In plain terms: the moment someone adds you to a repository or a
team, you start watching it, unless you have turned that behaviour off in your own notification
settings. You also automatically watch every repository you personally create.

### Watching, and the difference between watching everything, participating only, and ignoring

Open any repository you have access to and, near the top right of the page, find the **Watch**
button. Clicking its dropdown arrow gives you a small set of choices, and understanding what each
one actually does matters more than memorising the exact wording on the button, since GitHub does
occasionally reword its own interface. Confirm the exact label text on your own screen; what
follows is what each choice does, in GitHub's own words.

- **Watching everything.** You hear about all activity in that repository, described in GitHub's
  own words as "you will be notified of all conversations for that repository." This is the
  loudest setting, right for a repository small enough, or important enough, that you genuinely
  want to see everything happening in it.
- **Not watching, but still reachable.** This is the state you land in after choosing to stop
  watching a repository. GitHub's own description: "when you unwatch a repository, you unsubscribe
  from future updates from that repository unless you participate in a conversation or are
  @mentioned." This is the quiet middle setting, most repositories should sit here, you hear
  nothing routine, but a direct question to you still reaches you.
- **Custom.** Click **Custom** to pick specific kinds of update, issues, pull requests, releases,
  security alerts, or discussions, "in addition to participating and @mentions," in GitHub's own
  phrasing. Useful for a repository where you care about releases going out, say, but not about
  every individual issue.
- **Ignoring.** The loudest way to go quiet. GitHub's own words: "if you ignore a repository, you
  won't receive any notifications," and its own caution, worth repeating in full because it is easy
  to reach for this option without realising the cost: "we don't recommend ignoring repositories as
  you won't be notified if you're @mentioned." Reach for Ignore only for a repository you are
  certain you will never need to be pulled back into, for instance a very old, abandoned project. If
  there is any chance someone might need to reach you directly inside it, unwatch instead of
  ignore.

The direct address for a repository's watch settings follows this pattern (with your own
organisation and repository name in place of the capitalised placeholders), since the address
contains your own repository's name and cannot be given as a real link here:

`https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY`, then the **Watch** button near the top
right of that page.

You can also review and change these settings for every repository you watch in one place, rather
than opening each one individually. Open your [watched repositories
page](https://github.com/watching). You will know you are in the right place because it lists every
repository you currently watch, with an option next to each one to change or remove it.

### Where notifications arrive: the inbox, and email

Notifications reach you in two places, and GitHub treats them as connected but separately
switchable.

**The inbox.** Open your [notifications inbox](https://github.com/notifications). Every
notification you have not unsubscribed from or marked Done sits here as a list, newest first,
each one carrying its reason label.

**Email.** The same events can also land in your inbox as email, sent to a verified email address
on your account.

Whether each of these is switched on lives in one place, your [Notification
settings](https://github.com/settings/notifications). GitHub's own note on how the two interact:
"if you do not enable 'Notify me: On GitHub' for watching or participating notifications, then
your notifications inbox will not have any updates." In plain terms, if the inbox appears to be
receiving nothing at all, even though you know something happened, this is the first setting to
check, the "On GitHub" side may be switched off while email still is not, or the reverse.

### Turning email down without turning it off entirely

Getting every notification twice, once on GitHub and once in your inbox, is usually more than
anyone needs. GitHub lets you keep email for the things that genuinely need your attention and
drop it for routine background activity, rather than an all-or-nothing switch.

Open your [Notification settings](https://github.com/settings/notifications). You will know you
are in the right place because it lists separate rows for how you want to be notified about
different kinds of activity, including one row for updates in repositories you watch and
conversations you participate in.

- **To stop email for everything routine but keep it for what needs you:** deselect **email**
  next to watching, so a repository you are only half-watching stops filling your email, while
  leaving **email** selected next to participating, so a conversation you are directly involved in
  (commented on, or @mentioned in) still reaches your inbox that way too.
- **To narrow further, by the kind of update:** GitHub lets you choose which specific activities
  are sent to your default email address, among comments on issues and pull requests, pull request
  reviews, pull request pushes, and your own updates (things you personally opened, commented on,
  or closed).

Either way, turning email off completely does not turn GitHub off completely, the notifications
inbox keeps working on its own as long as "On GitHub" stays switched on, covered in the previous
section.

### The inbox: triaging, marking done, saving for later

Open your [notifications inbox](https://github.com/notifications). Next to each notification, or
across several selected at once, you have a small set of actions. GitHub's own description of
each:

| Action | What it does, in GitHub's own words |
| --- | --- |
| **Done** | "Marks a notification as completed and removes the notification from your inbox." Kept for five months afterward, in case you need to find it again. |
| **Save** | "Saves your notification for later review." Saved notifications stay flagged and are "kept indefinitely," unlike a notification you leave untouched. |
| **Unsubscribe** | "Automatically removes the notification from your inbox and unsubscribes you from the conversation until you are @mentioned, a team you're on is @mentioned, or you're requested for review." In plain terms, unsubscribing is not permanent if someone specifically pulls you back in later. |
| **Read / Unread** | Marks a notification as read, or puts it back as unread, without removing it from your inbox the way Done does. |

By default, your inbox shows both read and unread notifications together. If you only want to see
what you have not looked at yet, click **Unread**.

GitHub also builds a small set of filters into your inbox from the start, for the situations most
people actually need to check on: things you are assigned to, things you are participating in,
pull requests where you were asked to review, and anything where your username, or a team you
belong to, was directly @mentioned.

You can add up to fifteen of your own filters on top of these defaults, each one a saved search
you click to run again. GitHub's own example of the syntax: `repo:octocat/open-source-project-name
reason:participating`, which would show only notifications from that one repository, and only
where the reason was that you participated in the thread.

Notifications you never touch are not kept forever either way. GitHub's own retention rule:
notifications "that are not marked as Saved are kept for 5 months," after which they drop out of
your history. Saved ones are the exception, kept indefinitely.

### Being mentioned, and being requested for review, the two that actually need you

Almost everything else in your inbox is worth knowing about, but does not require a decision from
you today. These two do, because someone specifically chose to involve you.

**Being mentioned.** Someone typed your username with an `@` in front of it, inside an issue, a
pull request, or a comment, meaning they are speaking directly to you and likely expect a reply.
GitHub's inbox reason for this is labelled `mention`, and you can search for every mention across
everything you have access to with `reason:mention`.

**Being requested for review.** Someone has specifically asked you, by name, to review a pull
request before it is accepted, covered fully in `07-pull-requests.md`. GitHub's inbox reason for
this is labelled `review requested`, searchable with `reason:review-requested`. Both of these
reasons are already included in your inbox's default filters, so you do not need to build a filter
yourself to see them, but knowing the exact search is useful the moment your inbox gets busy enough
that scrolling stops being reliable.

Everything else, comments on threads you are only loosely involved in, state changes, activity
from a repository you are watching in full, is worth a glance but does not carry the same weight.
If your week only allows time for two things, make it these two.

## Strategy: how to actually use this

**If you personally hold access to a handful of repositories,** the whole system can run on
GitHub's defaults, with two small changes. Leave automatic watching switched on for anything you
create or are added to, it costs you nothing while the list stays short. Deselect email for
watching, but keep it selected for participating, so your inbox stays the single place you check,
rather than fighting your email client too. Do not bother building custom filters yet, the default
filters (assigned, participating, review requested, mentioned) already cover everything a solo
operator or a two or three person team actually needs, and a filter you built for a problem you do
not have yet is one more thing to maintain.

**If you are inside a busier organisation,** with people added and removed regularly and several
repositories generating steady activity, the defaults stop being enough on their own, mainly
because automatic watching means every repository or team you are added to starts talking to you
immediately, whether or not it turns out to matter to your role. The fix is not to turn automatic
watching off everywhere, it is to review what you are watching every so often, using your [watched
repositories page](https://github.com/watching), and move anything you do not need full activity
from down to the quiet setting (participating and mentions only) rather than leaving it on full
volume by accident. Build two or three custom filters around how your team actually splits work,
by repository, or by `reason:review-requested` if you are the person who reviews most pull
requests, so your inbox sorts itself instead of you sorting it by eye every morning.

**When to reach for Ignore, and when not to.** Ignore is the right tool for exactly one situation,
a repository you are certain has nothing left in it that will ever need you personally, most often
something old and closed out. It is close to never the right tool for a repository you are still a
genuine member of, because GitHub's own warning is accurate, you stop hearing about it even when
someone types your name directly into it. If in doubt, unwatch instead, it gets you the same
quiet, without the risk of a direct question to you going unanswered.

**What good looks like months later.** An inbox that sits close to empty most mornings, not because
nothing is happening, but because routine activity was never asked to reach you in the first place,
and because what does land there gets a Done, a Save, or an Unsubscribe within a minute of being
read, rather than accumulating. The two reasons that actually need you, being mentioned and being
requested for review, still reach you every time, because they were never the thing you were trying
to quiet down.

## A worked example

A landscaping business with two people using GitHub, the owner and the person who manages their
booking system, gets invited to join a client's organisation on GitHub so they can help maintain a
scheduling tool the client's own contractor originally built. Automatic watching, switched on by
default, immediately subscribes both of them to every repository in that organisation, six of them,
most completely unrelated to the one tool they were actually asked to help with.

Within a week, the owner's inbox has over 200 notifications, almost all of them routine commits and
comments on repositories she has never opened and never needs to. She stops checking it entirely,
which is exactly the failure this file exists to prevent, because a genuine question from the
client, asking her by name to review a change to the booking form before it goes live, sits unread
in the same pile for four days before she happens to notice it.

She opens her [watched repositories page](https://github.com/watching), reviews all six
repositories the invitation added her to, and unwatches five of them, leaving only the one
scheduling tool she actually works in. Unwatching does not cut her off from the other five
entirely, GitHub's own rule still applies, if anyone ever types her username directly into one of
them, that notification reaches her regardless. On the one repository she keeps, she leaves the
default "not watching, but still reachable" setting rather than watching everything, since she only
needs to know about direct questions to her, not every commit.

She also opens her [Notification settings](https://github.com/settings/notifications) and
deselects email for watching, keeping it only for participating, so her inbox becomes the one place
she checks rather than two. A week later, her inbox holds three or four items on a normal day,
every one of them either something she commented on herself or something someone specifically
asked her to look at.

## If it goes wrong

**I ignored a repository and missed something important.** This is the exact risk GitHub warns
about, ignoring blocks @mentions along with everything else. Open the repository, click the
**Watch** dropdown, and change it to the quieter "not watching" setting instead of Ignore. That
still keeps you out of the routine noise, while letting a direct mention find you again.

**I unsubscribed from something and it came back anyway.** This is expected, not a fault.
Unsubscribing only holds "until you are @mentioned, a team you're on is @mentioned, or you're
requested for review," in GitHub's own words. If someone pulls you back into the conversation on
purpose, you hear about it again on purpose.

**My inbox is already thousands deep and I do not know where to start.** Do not try to read
through it. Start with the [watched repositories page](https://github.com/watching) and unwatch
anything that no longer needs your full attention, GitHub even offers an **Unwatch all** option for
every repository owned by one user or organisation at once, though GitHub's own note is that "the
button to unwatch all repositories is only available if you are watching all activity or custom
notifications on over 10 repositories." On the [subscriptions page](https://github.com/notifications/subscriptions),
sort by "least recently subscribed" to find old subscriptions you likely forgot about. Remember
that anything you never touch clears out on its own after five months regardless, so an old
backlog is not a permanent weight, and a clean sweep now does not need to be perfect, it just needs
to get you back to a state where the default filters, assigned, participating, review requested,
mentioned, are doing the sorting for you again.

If you already have the GitHub CLI (`gh`) installed and signed in on your machine, Claude Code can
mark every current notification as read in one step, which is a genuinely faster starting point
than clicking through hundreds of them one at a time: `gh api notifications -X PUT -f read=true`.
This calls the same action GitHub's own documentation describes plainly: "marks all notifications
as 'read' for the current user." Two things worth knowing before you use it: this only marks
everything read, it does not mark anything Done or unsubscribe you from anything, so future
activity on those same threads will still notify you normally, and it is a one-way action, there is
no single command to put everything back to unread. Treat it as a way to get to a clean starting
line, not a substitute for actually reviewing what you are watching.

**I turned off email and now nothing is showing up anywhere.** Check whether "Notify me: On
GitHub" is switched on in your [Notification settings](https://github.com/settings/notifications).
GitHub's own words are direct on this: without it switched on for watching or participating
notifications, "your notifications inbox will not have any updates" either, so turning off email
without checking this setting can leave you with no notifications at all, rather than the quieter,
inbox-only setup you were probably aiming for.

**I do not understand why I got a particular notification.** Open it in your inbox and look at its
reason label, GitHub attaches one to every notification, and search `reason:mention`,
`reason:participating`, `reason:review-requested`, or any of the others to see everything sharing
that same reason at once.

## FAQ

**If I unwatch a repository, do I stop being told when someone asks me a direct question in it?**
No. GitHub's own rule is explicit, unwatching "unsubscribes you from future updates from that
repository unless you participate in a conversation or are @mentioned." Being mentioned, or being
requested for review, still reaches you either way. Only Ignore removes that.

**What is the actual difference between Unsubscribing and Unwatching?** Unsubscribing is scoped to
one specific conversation, an issue or a pull request, and stops just that one from notifying you
again, until someone pulls you back in. Unwatching is scoped to a whole repository, and turns off
its general, routine activity while still leaving direct mentions and review requests able to reach
you.

**Do saved notifications ever expire?** No. GitHub's own retention rule only applies to
notifications you leave untouched, kept for five months. A notification you have marked Saved is
"kept indefinitely," until you unsave it yourself.

**Does watching cost me anything if I end up watching a lot of repositories?** Not in any way this
file needs to warn you about, though GitHub does cap it: "you can watch a maximum of 10,000
repositories." Almost nobody reaches that limit, it is mentioned here only so you know it exists.

**If I turn off email entirely, do I lose anything permanently?** No. Turning off email only
changes where a notification is delivered, not whether GitHub keeps track of it. Everything still
appears in your notifications inbox as long as "Notify me: On GitHub" stays switched on, covered
above.

**Can I get notified by text message or through some other app instead of email or the website?**
This file could not confirm a way to do that, GitHub's own documentation for the settings covered
here only describes the notifications inbox and email as delivery options, alongside the separate
GitHub Mobile app, which is not covered in this file. If you need this, confirm on your own
Notification settings page whether any other option has since been added.

## Quick reference

```
Your inbox:                 https://github.com/notifications
Your watched repositories:  https://github.com/watching
Your subscriptions:         https://github.com/notifications/subscriptions
Your notification settings: https://github.com/settings/notifications

Watch dropdown, on any repository page, top right:
  Watching everything      -> notified of all activity in that repository
  Not watching (default)   -> quiet, except when you participate or are @mentioned
  Custom                   -> pick issues / pull requests / releases / security alerts / discussions
  Ignore                   -> silent even for @mentions, GitHub itself does not recommend this

Inbox triage:
  Done          removes it, kept 5 months in case you need it again
  Save          keeps it flagged, kept indefinitely
  Unsubscribe   quiets that one thread, until someone @mentions or requests review from you again
  Read / Unread just marks it, does not remove it

Default inbox filters:      assigned, participating, review requested, @mentioned
Search by reason:           reason:mention   reason:review-requested   reason:participating
                             reason:assign    reason:author             reason:comment
                             reason:state-change   reason:team-mention  reason:ci-activity

Inbox already too deep, quick reset via Claude Code (needs gh installed and signed in):
  gh api notifications -X PUT -f read=true      (marks everything read, not Done or unsubscribed)
```

## Sources

- https://docs.github.com/en/subscriptions-and-notifications/concepts/about-notifications
- https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications
- https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-subscriptions-for-activity-on-github/managing-your-subscriptions
- https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-subscriptions-for-activity-on-github/viewing-your-subscriptions
- https://docs.github.com/en/subscriptions-and-notifications/how-tos/viewing-and-triaging-notifications/managing-notifications-from-your-inbox
- https://docs.github.com/en/subscriptions-and-notifications/reference/inbox-filters
- https://docs.github.com/en/rest/activity/notifications
