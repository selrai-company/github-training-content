# Your GitHub account, and locking it down

## What this gets you

Your GitHub account is the one thing everything else in this kit sits on top of: your code,
your organization, your team's access, all of it. A weak password, no recovery codes, or one
phishing email clicked without thinking puts everything built on top of that account at risk
too, not just the account itself. Fifteen minutes spent now, done properly once, means you
mostly never have to think about account security again, and it means that if your phone is
lost or stolen, you have a documented way back in instead of a locked-out business.

## Before you start

**Every person on your team needs their own account, not a shared login.** This file is
something each person does for themselves. If you run this business with a partner or staff,
send them this file too rather than doing it once on their behalf.

**You need an email address you control, and access to your phone.** The phone is for either
a free authenticator app or a text message, covered below. Have both open before you start.

**Set fifteen minutes aside, uninterrupted.** Part of this involves GitHub showing you a set
of recovery codes exactly once at setup time. Doing this in a rush, halfway through something
else, is how people skip the step that matters most.

**Have somewhere ready to store recovery codes before you get to that step.** A password
manager is what GitHub itself recommends. If you do not have one yet, decide where those codes
are going before you reach that part of this file, not while the download is sitting in your
downloads folder.

**None of this runs through Claude Code, and that is deliberate.** Every step below happens in
your browser, signed in to github.com as yourself. These are identity and security actions
tied to you as a real person: GitHub needs to see you click the button, scan the code, or type
the number yourself. A terminal assistant cannot do that part for you, and it should not be
trusted to.

**If you already have a GitHub account,** skip account creation below and go straight to
two-factor authentication. That section matters for you even if your account is years old.

## The words you need

**GitHub account.** Your sign-in identity on GitHub. Every repository, every organization, and
every permission in this kit's other files sits on top of this one thing.

**Verified email address.** An email address GitHub has confirmed belongs to you, by sending a
link you clicked. GitHub blocks some basic actions, including creating a repository, until this
is done.

**Username.** Your public handle on GitHub. It becomes part of every profile link and every
repository address you own, so it is worth a little thought before you settle on one.

**Two-factor authentication (2FA).** Signing in with your password **and** a second proof that
it is really you. The idea is that a stolen password alone is not enough to get in. Think of it
like a house key plus an alarm code: someone copying your key still cannot get past the alarm.

**Authenticator app (TOTP).** A phone or desktop app that generates a fresh six-digit code every
30 seconds, used as your second proof. TOTP stands for "time-based one-time password," which is
just a technical name for "a code that changes every half minute."

**SMS code.** A six-digit code sent to your phone by text message, used as an alternative second
proof. Weaker than an authenticator app, and covered in more detail below.

**Security key.** A physical device, or your device's own built-in option like Touch ID or
Windows Hello, that proves it is you by a hardware check rather than a typed code.

**Passkey.** A credential stored on your device that can stand in for both your password and
your second proof at once, in a single step.

**Recovery codes.** A set of one-time backup codes GitHub gives you when you turn on 2FA. Each
one works exactly once, and they exist for one job: getting you back into your account if your
phone, authenticator app, or SMS number is ever unavailable.

**Verification code (new-device check).** A different, separate code GitHub can ask for when you
sign in from a browser or device it does not recognize. This is not the same thing as your 2FA
code, and it can happen even with 2FA turned off.

**Phishing.** A message built to trick you into typing your password, your 2FA code, or your
recovery codes into a fake page or handing them to a fake support agent. It works by looking
exactly like the real thing.

**Third-party app authorization.** Permission you have granted to an outside tool to access some
or all of your GitHub account, usually by clicking "Authorize" on a screen GitHub shows you.

## How to do it

### Creating your account

1. Go to [github.com/signup](https://github.com/signup).
2. Enter your details and follow the prompts. You can also sign up with **Continue with
   Google** as a shortcut instead of filling in the form by hand.
3. Verify your email address when GitHub asks. This step is not optional: GitHub's own
   documentation states plainly, "Without a verified email address, you won't be able to
   complete some basic GitHub tasks, such as creating a repository." Skipping it just means you
   hit a wall later, at a moment that is less convenient than right now.

**Screenshot placeholder:** the github.com/signup screen, showing the fields it currently asks
for, so a reader can match what they see to this step.

### Choosing an email you won't regret

Use an email address you expect to control for years, not one tied to a job or a phone number
you might lose. If your business changes email providers later, you can always add a new
address to the same account, but the address you start with today should be genuinely yours
long-term.

GitHub also gives you a way to keep your real email address out of public view when you commit
code through the browser.

Open your [**Emails settings**](https://github.com/settings/emails), a page that is the same
address for every GitHub user. On it, turn on **Keep my email addresses private**. You will know
it worked because GitHub generates a private stand-in address for you, in the exact form
`ID+USERNAME@users.noreply.github.com`, and shows it to you on that same page. Anything you
commit through the GitHub website then uses that stand-in address instead of your real one.
This matters more once you're publishing public repositories; for a private repository it is a
smaller concern, but there is no reason not to turn it on now.

### Choosing a username you won't regret

Your username becomes part of every profile link and every repository URL you own, so it is
worth thirty seconds of thought before you lock it in.

Two things to know before you pick one:

**It's first-come, first-served, and GitHub does not hold names for you.** GitHub's own
username policy says it directly: "GitHub account names are available on a first-come,
first-served basis, and are intended for immediate and active use." Squatting on a name you're
not using is against the rules, and if the name you want is already taken, GitHub is blunt
about your options: "Valid trademark-related complaints are the only requests we review for
possible release of a username that is already claimed." In plain terms, if someone else already
holds the name you wanted, you are very unlikely to get it back from them, even if it matches
your business name. If your exact business name is available, it may be worth grabbing now for
that reason alone.

**You can change it later, but it isn't free of consequences.** GitHub's own documentation on
username changes is specific about what happens:

- "After changing your username, your old username becomes available for anyone else to
  claim." If someone else grabs it and creates a repository with the same name yours had, that
  overrides your old redirect and it stops working.
- "Most references to your repositories under the old username automatically change to the new
  username," but not everything follows automatically.
- "After changing your username, the URLs to any public or secret gists will also change and
  previous links to these will return a 404 error." The same applies to your old profile page
  link.
- Any CODEOWNERS file that names your old username has to be updated by hand; it does not
  update itself.
- GitHub's own recommendation: "We recommend you update all existing remote repository URLs
  after changing your username," because of the redirect risk above.

None of this means never change it. It means: pick something you're reasonably happy to keep,
because changing it later is possible but has real cleanup attached, not just a cosmetic swap.
When you're ready to change it, the setting lives on your [**profile and account
settings**](https://github.com/settings/profile) page, the same address for every GitHub user.

### Turning on two-factor authentication

Do this before anything else on this list, even if you plan to skip every other optional step
in this file.

**Methods GitHub currently supports**, per GitHub's own documentation:

- A **TOTP authenticator app**.
- **SMS text message** to your phone.
- A physical **security key**, or your device's built-in option like Touch ID or Windows Hello.
- A **passkey**, which GitHub says "satisfy both password and 2FA requirements" on its own.
- **GitHub Mobile**, once you've already set up a TOTP app or SMS as your first method.

**Use an authenticator app, not SMS, if you have a choice.** GitHub says so directly: "We
strongly recommend using a TOTP application for two-factor authentication instead of SMS, and
using security keys as backup methods instead of SMS." Their stated reasons: SMS "is susceptible
to interception, does not provide resistance against phishing attacks, has unreliable
deliverability, and is not supported in all countries." A free authenticator app, on the phone
you already carry, takes about the same effort to set up as SMS and does not have any of those
weaknesses.

**If you do use SMS, know it is not available everywhere.** GitHub's own wording: "Because of
delivery success rates, GitHub only supports two-factor authentication via SMS for certain
countries." This is a maintained list that changes, not a fixed rule, so **confirm your own
country is currently on it, on your own screen**, before you plan around SMS as your method.
This kit cannot confirm which countries are on that list today on your behalf; check it
yourself at the moment you set this up rather than assume.

**Turning it on, step by step.** From any page on github.com, once you are signed in, click
your **profile picture** in the top right corner of the page, then click **Settings** in the
menu that opens. You will know you are in the right place because the page's address becomes
`github.com/settings/profile`, and a list of setting groups appears down the left-hand side.

In the **Access** section of that left-hand sidebar, click **Password and authentication**.
You will know you are on the right page because it lists **Two-factor authentication** with an
option to enable or manage it. The direct address, the same for every GitHub user, is
[**Security settings**](https://github.com/settings/security) if you would rather go straight
there. If your sidebar looks different from this description, you may be looking at an
organization's settings rather than your own personal ones; use the direct address above, or
click your profile picture again and confirm you chose **Settings** for yourself.

From there:

1. Under "Two-factor authentication," click **Enable two-factor authentication**.
2. Pick your method:
   - **TOTP app:** scan the QR code with your authenticator app, or type in the setup key by
     hand, then enter the six-digit code it shows you under "Verify the code from the app."
   - **SMS:** complete the CAPTCHA, enter your phone number, and enter the code you're texted
     under "Verify the code sent to your phone."
3. Click **Download** to save your recovery codes. Read the next section before you click this,
   so you know where you're saving them to.
4. Click **I have saved my recovery codes** to finish.

**Screenshot placeholder:** the "Password and authentication" settings page, with the
"Two-factor authentication" section visible, so a reader can find it without hunting.

### Saving your recovery codes

When you turn on 2FA, GitHub gives you a set of one-time backup codes. Each one works exactly
once: "Each code is single-use only: once it has been used to authenticate, it cannot be used
again." They exist for one job: getting you back into your account if you lose your phone, your
authenticator app, or your SMS number.

**Where to get them, any time, not just at setup:** click your **profile picture**, then
**Settings**, then **Password and authentication** in the Access section of the sidebar (or go
straight to the [**Security settings**](https://github.com/settings/security) page). Under
Two-factor authentication, find the **Recovery codes** row and click **View**. You will know it
worked because GitHub shows you your current set of codes on screen.

**Where to keep them:** GitHub's own advice: "We recommend saving them with a secure password
manager." Not a screenshot on the same phone that holds your authenticator app. Not a note stuck
to your monitor. A password manager, or printed and kept somewhere physically safe, separate
from the device that generates your 2FA codes.

**This is the sentence that makes this whole section matter.** GitHub states it exactly like
this: **"GitHub Support will not be able to restore access to accounts with two-factor
authentication enabled if you lose your two-factor authentication credentials or lose access to
your account recovery methods."** Not "it's difficult." Not "contact us and we'll sort it out."
GitHub Support itself cannot get you back in. Your recovery codes, or another configured
recovery method, are the only way back in if your main 2FA device is gone. Download them the
day you turn on 2FA, not the day you need them.

### Recognizing a new-device sign-in check

If 2FA is off, or even sometimes when it is on, GitHub may still ask you to verify a sign-in
from a device or browser it does not recognize: a new computer, a new phone, a new browser, or
a fresh browser profile.

- The verification code goes out by email: "The verification code is sent to all primary and
  backup email addresses associated with your account," and it's "valid for one hour."
- If you have the GitHub Mobile app installed, GitHub skips the email and sends a push instead:
  "GitHub sends a verification request to your mobile device, instead of sending an email. Enter
  the code displayed in your browser into the GitHub Mobile app to verify your sign-in."
- Once you've verified a device, GitHub says "you will only need to verify a new device once."
  It only asks again on that same device if you clear your cookies or switch to a different
  browser on it.

**One warning worth remembering:** if a verification code shows up in your inbox and you did not
just try to sign in anywhere, GitHub is telling you plainly what that means: "your GitHub
password may have been compromised." Change your password immediately if that happens; do not
dismiss the email.

### Reviewing what you've given access to

Every so often, check what third-party tools can see inside your GitHub account, and remove
anything you no longer use.

Open your account settings (**profile picture** then **Settings**), and look down the left-hand
sidebar for **Applications**. The direct address, the same for every GitHub user, is
[**github.com/settings/applications**](https://github.com/settings/applications). You will know
you are in the right place because it lists each outside tool you have authorized, one row per
tool. Each entry has its own **Revoke** button, and a **Revoke all** option at the top clears
everything at once.

When you originally authorize a tool, GitHub shows you which repositories it will be able to
see: GitHub's own documentation confirms "you also specify which repositories the app can
access." Read that screen before you click **Authorize**. If a tool only needs to work with one
repository, grant it that one repository, not "all repositories."

**Screenshot placeholder:** the Settings then Applications page, showing an authorized app's
repository access, so a reader can see what this screen looks like before they hit it live.

## Strategy: how to actually use this

**Do the whole thing in one sitting, not spread over a week.** Account creation, 2FA, and
recovery codes are one connected task. Doing 2FA today and telling yourself you'll download
recovery codes "later" is exactly how a recovery code never gets downloaded at all.

**A solo operator needs this more than anyone, not less.** With no one else in the business,
there is nobody to notice your account behaving strangely, and nobody who can get you back in
if you lose your phone and your codes at the same time. Treat the fifteen minutes here as
non-negotiable specifically because you are the only safety net your business has.

**A team of two to four people should treat this as a per-person checklist, not an owner-only
task.** Every person who touches the repository has their own account, their own 2FA, and their
own recovery codes. One person having strong account security while a teammate reuses a
five-year-old password is still a hole in the business, because either account can reach the
same repository.

**Default to an authenticator app over SMS, every time you have the choice.** GitHub's own
guidance already says this, and it costs you nothing extra: the same phone, roughly the same
effort. Reach for SMS only as a fallback method alongside a real authenticator app, never as
your only method, and never because it felt like the path of least resistance at setup time.

**Turn 2FA on voluntarily, before GitHub makes you.** Publishing a release, creating an
organization, or becoming an administrator on a repository that matters, all covered elsewhere
in this kit, are exactly the kinds of actions that put an account into GitHub's mandatory 2FA
enrollment. Once that happens, a 45-day enrollment window opens, followed by a further 7-day
grace period, and GitHub is direct about what happens if both pass with 2FA still off: "You will
not be able to access GitHub.com until you enable 2FA." Doing this now, on your own schedule,
means you never see that clock start.

**Review your authorized third-party apps on a schedule, not only when something feels wrong.**
Once a quarter is a reasonable habit for a small business. A code editor plugin, an old
deployment tool, a service you tried once and stopped paying for: each one that still holds
access to your repositories is a door you forgot was unlocked. Revoking access you're not using
costs a few clicks and removes a real risk for free.

**Treat every unexpected sign-in request as suspicious by default, not as an inconvenience to
click past.** A verification code you did not request, or an email asking you to "sign in"
through a link, is not routine account noise. The safer habit is not learning to check a
certificate under pressure, it is never clicking a sign-in link from an email at all: open a new
browser tab and type github.com in yourself, every time. Nobody legitimate, not a client, not
"GitHub verification," not a real support agent, ever needs your 2FA code, your recovery codes,
or your password read aloud to them.

**What good looks like months later:** every person on the team has 2FA on, their recovery codes
live somewhere durable that is not the same device as their authenticator app, and the
Applications list only contains tools currently in active use. Nobody can tell you the last time
they checked any of it, because there was never a scare that forced the question.

**What would change my mind about any of this being optional:** nothing here is optional for a
business account holding real client work. The only genuine judgment call is authenticator app
versus security key versus passkey, and that comes down to what device you already carry, not
whether to bother with a second factor at all.

## A worked example

A café owner is setting up GitHub for the first time, for the online ordering site her nephew
is about to build for her. Her nephew already has an account from earlier freelance work, and a
staff member will need occasional access to update menu text.

The owner goes to github.com/signup, creates an account using her business email address, and
verifies it from the confirmation link GitHub sends. She turns on **Keep my email addresses
private** from her Emails settings before she does anything else, since she knows her commits
will otherwise show her real address in public later. She picks a username close to her
business name while it is still available.

Next, she opens her Password and authentication settings and turns on two-factor
authentication, choosing a free authenticator app on her phone rather than SMS, since that's
what GitHub itself recommends. When GitHub offers her the recovery codes, she downloads them
straight into the password manager she already uses for the business's banking logins, not onto
her phone's photo gallery.

Her nephew, whose account is a few years old, uses this same file as a prompt to check his own
account rather than assume it's already covered. He opens his Applications settings and finds a
code-hosting plugin from a freelance job that ended over a year ago, still showing full
repository access. He clicks **Revoke** on it.

Three months later, the staff member gets an email asking her to "verify her GitHub sign-in" by
clicking a link. She remembers this file's advice, opens a new tab, and types github.com in
herself instead of following the link. Nothing in her actual account settings mentions a pending
sign-in. She reports the email to the owner rather than clicking it, and nothing happens to the
account.

## If it goes wrong

**I lost my phone, my authenticator app, or my SMS number, and I need to get back in.** Work
through this in order:

1. **Try your recovery codes**, if you saved them (login screen then "More options" then 2FA recovery
   code).
2. **Try another method you've already configured**, if you have one. GitHub's own guidance
   lists "authenticating with another method, such as a passkey, GitHub Mobile, or a security
   key, if pre-configured on the account."
3. **If none of that works, you're into formal account recovery**, and GitHub's own
   troubleshooting page is direct about the limit here: "For security reasons, GitHub Support
   cannot assist with troubleshooting your 2FA methods, including SMS delivery." Combined with
   the recovery-code warning above, if both your 2FA device and your recovery codes are gone,
   there is no support ticket that gets your original account back.
4. **The last resort GitHub documents is not account recovery, it's an email release.** If every
   recovery option is genuinely exhausted, GitHub's documentation describes only this: "you can
   unlink an email address tied to the locked account. The unlinked email address can then be
   linked to a new or existing account." Read that carefully: this does not hand your old
   account, its repositories, or its history back to you. It frees your email address so you can
   use it to start again. This is the entire reason recovery codes are step one above, not an
   afterthought.

**I enabled 2FA and now I can't get the setup screen to accept my code.** Double-check the time
on your phone or computer is correct and set automatically; TOTP codes are time-based, and a
clock that's even a minute or two off will generate the wrong code. If SMS codes aren't
arriving, confirm your country is still on GitHub's supported list before assuming it's a typo
in your number.

**I got a "verify this device" email or code and I wasn't the one signing in.** Change your
password immediately. That's GitHub's own guidance for an unrequested verification code, and it
applies whether or not the sign-in attempt actually succeeded.

**I authorized a tool a while ago and I'm not sure what it can still see.** Open your
Applications settings (the direct address is above), find it in the list, and either check its
access or click **Revoke**. Revoking is not destructive to your repositories; it only removes
that tool's ability to reach them, and you can always re-authorize it later if you decide you
need it again.

## FAQ

**Do I really need 2FA if I'm just one person, working alone, with no releases yet?** Turn it on
anyway. It takes about two minutes, and the moment you create an organization or publish
anything, both covered elsewhere in this kit, GitHub is very likely to require it regardless.
Doing it now on your own terms beats a 45-day countdown you did not choose.

**Can Claude Code set up 2FA or save my recovery codes for me?** No, and this isn't a limitation
worth working around. GitHub's whole point with 2FA is proving a human is physically present
with the phone or the security key. A terminal assistant has no way to scan your QR code or
hold your device, and it shouldn't be trusted with your recovery codes even if it could.

**Is it fine to reuse a password I already use somewhere else?** Confirm GitHub's current
password requirements on your own screen at sign-up, since this page does not repeat a rules
list that GitHub could change. As a habit regardless of the minimum rule: don't reuse a password
across sites. If one site the password was used on ever leaks, every account sharing that
password becomes exposed with it, GitHub included.

**What if the username or organization name I want is already gone?** For a personal username,
see the policy quoted above: trademark disputes are the only path GitHub reviews to release a
taken name, so plan on a variation rather than waiting the original owner out.

**I set up SMS 2FA and now I'm travelling somewhere it doesn't work. What now?** Add a TOTP
authenticator app as an additional method before you travel, from the same Password and
authentication settings page. You can have more than one 2FA method configured at once, so this
doesn't require dropping SMS, just not depending on it as your only option.

**Does 2FA or storing recovery codes cost anything extra?** This kit did not find a stated cost
for either in the GitHub documentation reviewed for this file. Confirm your own plan's feature
list on GitHub's own pricing page if you want certainty before relying on it.

## Quick reference

- **Create an account:** [github.com/signup](https://github.com/signup), then verify your email
- **Hide your real email in commits:** [Emails settings](https://github.com/settings/emails),
  **Keep my email addresses private**
- **Turn on 2FA:** profile picture then **Settings** then **Password and authentication** (or go
  straight to [Security settings](https://github.com/settings/security)) then **Enable two-factor
  authentication**
- **Get your recovery codes:** same page then **Recovery codes** then **View**, save in a password
  manager
- **Review authorized apps:** profile picture then **Settings**  then 
  [**Applications**](https://github.com/settings/applications) then **Revoke**
- **Locked out:** recovery codes first, then another configured method, then GitHub Support
  only if both are gone (Support cannot restore 2FA access itself)
- **Suspicious email:** never click a sign-in link inside one, type github.com into a new tab
  yourself
- **Through Claude Code:** none of the above. These are identity actions and need you, not the
  terminal.

## Sources

- https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
- https://docs.github.com/en/account-and-profile/reference/email-addresses-reference
- https://docs.github.com/en/site-policy/other-site-policies/github-username-policy
- https://docs.github.com/en/account-and-profile/concepts/username-changes
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/countries-where-sms-authentication-is-supported
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/recovering-your-account-if-you-lose-your-2fa-credentials
- https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/troubleshooting-two-factor-authentication-issues
- https://docs.github.com/en/site-policy/other-site-policies/github-account-recovery-policy
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/verifying-new-devices-when-signing-in
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/preventing-unauthorized-access
- https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps
- https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps
- https://github.blog/news-insights/company-news/security-alert-new-phishing-campaign-targets-github-users/
