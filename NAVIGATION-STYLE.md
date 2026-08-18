# How we point someone at something on screen

House rule for every page in this kit. It exists because the most common way training fails is not a
bad explanation. It is a reader who cannot find the button, gives up, and concludes the fault is theirs.

A link on its own is not enough. A link takes them to a page. It does not take them to the control, it
breaks when they are signed out, and it tells them nothing about what they are looking for.

## The formula

Five parts, in this order. Not every part is needed every time, but the order never changes.

**1. Landmark.** Start from something they are certainly looking at already. "On the front page of your
repository" or "From the page you are on now". Never start from nowhere.

**2. Path.** Where to go from that landmark, described by position and grouping rather than by pixel.
"Along the top of the page, in the row of tabs that starts with Code" is findable. "In the top right" on
its own is not, because there are usually four things there.

**3. Label, in bold, spelled exactly as it appears.** Bold it so the eye catches it while scanning, and
match the capitalisation on screen. **Settings**, not "the settings option".

**4. Confirmation.** What changes when they get it right. This is the part almost everybody leaves out,
and it is the part that lets a reader know they are on track rather than lost. "A list of settings
appears down the left-hand side."

**5. Fallback.** What it means if it is not there. Usually one of three things: they lack the access, the
page has changed since this was written, or they are in the wrong place. Say which, and say what to do.

## Link the label itself, where a link can actually work

Put the link on the bold label so the thing they are hunting for is the thing they can click. This is
the fastest possible route for a reader, and it costs nothing to add.

There are two cases and they must not be mixed up.

### Case one: pages that are the same for everyone. Make these real links.

Anything about the reader's own account has an address that is identical for every reader, so it can be
a working link on the page. Use them.

| Where you are sending them | The address |
| --- | --- |
| Their profile and account settings | `https://github.com/settings/profile` |
| Security, including two-factor and recovery codes | `https://github.com/settings/security` |
| Their email addresses | `https://github.com/settings/emails` |
| The organizations they belong to | `https://github.com/settings/organizations` |
| Repository access they have granted | `https://github.com/settings/repositories` |
| Their notification inbox | `https://github.com/notifications` |
| Creating a new repository | `https://github.com/new` |
| Their security log, which shows recent account activity | `https://github.com/settings/security-log` |
| People they have blocked | `https://github.com/settings/blocked_users` |

Written out, a link on the label reads like this:

> Open your [**Security settings**](https://github.com/settings/security). You will know you are in the
> right place because the page lists Two-factor authentication with an option to enable or manage it.

**How these were checked, and the limit of that check.** Each address above was requested on
2026-08-18 and returned a success response, against a deliberately nonsense address that returned a not
found, so the check could tell the difference. What that proves is that the paths are real. It does not
prove what each page shows once a reader is signed in, because the check was not signed in. So still
write the confirmation line telling them what they should see.

### Case two: pages inside a repository or organization. Never link these.

A repository address contains the reader's own names, so any link we write goes to our repository or to
nothing. Give the pattern instead, in capitals so it is obvious it needs changing:

`https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings`

Then describe the path properly, because the pattern is a template rather than a shortcut. A link that
takes a reader somewhere unexpected is worse than no link, because they will trust it.

### Both cases still get the prose

The link is the shortcut. The description is what works when the reader is signed out, lacks the access,
is on a phone, or GitHub has moved something. Never let a link replace the five-part formula above.

## What this looks like in practice

**Too thin, and this is the version we keep writing by accident:**

> Go to Settings and turn on branch protection.

**Hardened:**

> Open the front page of your repository. Along the top, in the row of tabs that begins with **Code**
> and **Issues**, look toward the right-hand end for a tab labelled **Settings**. It has a small gear
> beside it.
>
> The direct address is `https://github.com/YOUR-ORGANISATION/YOUR-REPOSITORY/settings` if you would
> rather go straight there.
>
> You will know you are in the right place because a long list of setting groups appears down the
> left-hand side, starting with General.
>
> If you cannot see a **Settings** tab at all, you are not an administrator of that repository. That is
> the thing to fix first, and the page on access levels explains who can grant it to you.

Longer, and it is the difference between a reader who finishes and a reader who stops.

## Rules that come out of this

**Never rely on colour alone.** "The green button" stops working the day GitHub restyles it, and it
excludes anyone who does not see colour the way you do. Say the label. Colour can be a secondary hint:
"the button labelled **Code**, which is currently green".

**Never rely on position alone.** "Top right" is four different things. Combine position with the label
and, where it helps, with what sits next to it.

**Bold every on-screen label**, every time, including in the middle of a sentence. It turns a paragraph
into something scannable by someone hunting.

**Use the reader's placeholder, not ours.** `YOUR-ORGANISATION` and `YOUR-REPOSITORY` in capitals, so it
is obvious they are meant to change it. Never leave a real example address they might follow by mistake.

**Give the confirmation every time.** If you cannot say what changes when they succeed, you have not
finished writing the instruction.

**Where you are not certain, say so.** GitHub moves things. "If the buttons do not match what is
described here, read what they actually say and use the one that offers to make you a copy" is an honest
instruction that still works after a redesign. A confident wrong path is worse than an admission.

**Screenshots do not replace this.** A screenshot goes stale silently and nobody notices. Written
navigation degrades gracefully. Where a screenshot helps, add it to good prose rather than instead of
it.

## The one-line test

Read the instruction back and ask: could someone follow this with the page open, without already knowing
where the thing is, and would they know whether they got it right?

If not, it is not finished.
