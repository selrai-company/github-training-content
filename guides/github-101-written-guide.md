# GitHub 101: Set Up Your Organization, Add Your Team, Get to Work

This is the written, step by step version of the GitHub 101 video. You do not need to have watched
the video to follow this page. Everything you need is here, and it works with just a browser, no
install and no code.

By the end of this page you will have a GitHub account that is properly protected, your own
organization, a second owner added to it, your first teammate invited with the right level of
access, and your team's first shared repository created on purpose, not by accident.

Work through the steps in order. Each one only takes a couple of minutes.

---

## Before you start

**What you need:** a browser, and an email address you check.

**What you do not need:** anything installed, any code, GitHub Desktop, or a command line. This
whole guide happens in your browser.

If you have not set up your Claude Code build system yet, that is a separate guide, and it does
not need to happen before this one: `[LINK: your separate build-system setup guide]`.

---

## Step 1: Make a GitHub account (skip this if you already have one)

Go to `github.com` and sign up. Use an email you check regularly, and one you will still have in
six months. Follow GitHub's own sign-up page, it takes about a minute.

Come back to this page once you are signed in and can see your own profile picture in the top
right corner of the screen.

---

## Step 2: Protect your account before it holds a business

Do this before you create an organization. In a moment this account is going to be responsible for
a business's shared work, not just your own, so lock it down first.

1. Go to your account **Settings**, then **Password and authentication**. Look for **two-factor
   authentication**, sometimes shown as **2FA**.
2. If it already shows as enabled, you are most of the way there, skip to the recovery codes step
   below.
3. If it is off, click enable and follow GitHub's own steps on screen. An authenticator app on
   your phone works everywhere. A text message works only in certain countries, and GitHub itself
   recommends the app over a text message. If you are setting this up fresh, choose the app.
4. Once it is on, find **Save your recovery codes** and click **Download**. Save that file
   somewhere that is not your phone, for example a password manager, or a printed page kept
   somewhere safe. If your phone is ever lost, stolen, or just dies, these codes are what gets you
   back in.

**Why this matters, in GitHub's own words:** if you ever lose your two-factor device and have no
recovery codes saved, "you have permanently lost access to your account." Even GitHub's own support
team "will not be able to restore access" in that situation. Two minutes now avoids that
permanently.

**Why now, before you create an organization:** owning an organization that has repositories or
people in it is one of the things that puts your account on GitHub's required list for two-factor
authentication. GitHub gives you a 45-day window to turn it on, plus a 7-day grace period after
that. If both run out, you are locked out of GitHub entirely until you enable it. Doing this now,
before that clock even starts, means it never becomes a problem later.

---

## Step 3: Create your organization

1. Click your profile picture in the top right corner, then click **Settings**.
2. In the sidebar, under **Access**, click **Organizations**.
3. Next to the "Organizations" header, click **New organization**, and follow GitHub's own prompts
   from there. That is every click, start to finish.

New organizations run on GitHub's free plan unless you choose to upgrade, so there is nothing to
pay to get this far.

Once it exists, open the organization's **People** page and look at what it shows next to your own
name. On GitHub, **Owner** means complete administrative access. No official source confirms that
creating an organization automatically makes you its Owner, so check your own role on the People
page rather than assuming it, GitHub shows you directly.

---

## Step 4: Add a second owner, first

Do this before you configure anything else in your new organization.

GitHub itself recommends that **at least two people** hold the owner role in every organization,
because "the organization's projects can become inaccessible if the owner is unreachable" when
there is only one.

1. If the person you want as a second owner is not already listed as a member, invite them first.
   The exact invite screen is worth reading directly off your own page when you get there, since
   its wording can change.
2. Once they are listed on the **People** page: tick their name, open the "X members selected..."
   dropdown, click **Change role**, select **Owner**, then click **Change role** again to confirm.

That is your second owner, done. If you do not have anyone ready to invite yet, you can invite
yourself on a second email address for now, or come back to this step once you have a real second
person, either is a normal path.

---

## Step 5: Invite your first teammate

Go back to the **People** page and invite whoever needs access next.

Pick the narrowest access level that actually does their job, not the widest one out of
convenience. You can always add more access later; you cannot always take back what was already
used.

**One thing to know the moment you add someone, not after:** if you ever remove that person from
your organization, GitHub is specific about what that does and does not do.

- It stops what they can do **from that point forward**.
- It does **not** undo what they already have. GitHub's own words: a removed member "may still
  have local copies," they just "cannot sync local copies with your organization's repositories."
- Two more things worth knowing: if a private repository was ever forked somewhere else, that
  person may keep access to that fork even after losing access to your organization. And if you
  remove someone by mistake, GitHub keeps their membership data for three months, so re-inviting
  them within that window restores it.

The rule this points to: give people what they need today, not everything just in case. Less
handed out is less that walks out the door later.

---

## Step 6: Create your team's first shared repository

Create the repository your team will actually use. When you reach the visibility choice, look
carefully, in GitHub's own words:

- **Public** repositories are "accessible to everyone on the internet."
- **Private** repositories are "only accessible to you, people you explicitly share access with,
  and, for organization repositories, certain organization members."

Nowhere does GitHub state which option the new-repository form starts on. So when you get to that
screen, look at whichever option is already selected, and choose the one you actually want on
purpose. Do not assume it is set to the safe option already.

**The rule for a leaked secret.** If a password, a key, or a login ever ends up in a file you
commit to this repository, even by accident, even if you delete it a minute later, treat it as
burned. GitHub's own stated first step is to go straight to wherever that key came from and get a
new one. Deleting the file does not undo it: the old version can still be reached through clones,
forks, or GitHub's own cached views of your repository. If this ever happens to you, ask in the
community before trying to clean up the history yourself. That part is not a solo job.

---

## Step 7: Now that you own an organization, three things are always a scam

This is our own guidance, based on common sense about what an organization owner becomes a target
for, not something GitHub itself publishes as a warning.

1. An email asking you to sign in, using a link inside that email.
2. Anyone at all asking for your two-factor code or your recovery codes.
3. Any app or any person asking for access to your **whole organization**, when they only need one
   repository.

If you ever see one of these, stop. Do not click anything. Ask in the community first.

---

## Step 8: Get this week's build

There are two ways teams in this community get their weekly build. Use whichever one your team
actually uses.

**If your build lands in a shared repository:** once you are a member of your organization, you
already have access to it. Go to the repository page, click the green **Code** button above the
file list, then click the download option shown there (it downloads GitHub's docs describe as
"Download ZIP", but read the exact wording on your own screen, the label can change). That pulls
the week's files down as one folder, no extra software needed. Note where your browser saves
downloads, that is exactly where it lands every time.

**If your build is posted in the community instead:** look for the pinned post in your community
channel, click the link inside it, and it downloads straight to your machine, the same place your
browser always saves downloads to. Nothing to open in GitHub for this part.

Either way, the result is the same: this week's build is somewhere on your machine you can find
again.

---

## Step 9: Confirm it worked, and post it

Go to your organization's **People** page. You should see your teammate and your second owner both
listed there.

Take a screenshot of exactly that page, showing the person you just added, and post it in the
community: `[LINK: where members post their proof]`.

That one screenshot is what shows you actually finished, not just watched.

---

## Quick reference: organization role names

You do not need to memorize this. Come back to it any time a role name shows up on screen.

| Role | What it means, in GitHub's own words |
|---|---|
| **Owner** | "Complete administrative access to your organization." |
| **Member** | "The default, non-administrative role for people in an organization." |
| **Billing manager** | "Can manage the billing settings for your organization, such as payment information." |
| **Moderator** | "Allowed to block and unblock non-member contributors, set interaction limits, and hide comments in public repositories owned by the organization," in addition to their permissions as a member. |
| **Security manager** | "Gives permission to view security alerts and manage settings for security features across your organization, as well as read permission for all repositories in the organization." |

---

## If something goes wrong

- **Can't sign back in the following week?** Make sure you know which email and password you used
  for GitHub, and keep that written down somewhere you will find again.
- **Invite email never arrives?** Check the spam folder first. If it is still not there, send the
  invite again from the People page.
- **Not sure what a role actually lets someone do?** Use the reference table above rather than
  guessing.
- **Anything about a screen does not match what this page says?** Trust your own screen. GitHub's
  interface changes over time, and this page is written to be accurate as of when it was published.
  Ask in the community if something looks different.
