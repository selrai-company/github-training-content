# Your GitHub account, and locking it down

This is the first topic in the kit on purpose. Everything else, your code, your organization, your
team's access, sits on top of this one account. Get this part wrong (a weak password, no recovery
codes, a phishing email you click without thinking) and everything built on top of it is at risk too.
Get it right once, in about fifteen minutes, and you mostly never have to think about it again.

Every step in this file happens in your browser, signed in to github.com as yourself. None of it runs
through Claude Code, and that's deliberate: these are identity and security actions tied to you as a
real person. GitHub needs to see you click the button, scan the code, or type the number yourself. A
terminal assistant cannot do that part for you, and it shouldn't be able to.

## Creating your account

1. Go to [github.com/signup](https://github.com/signup).
2. Enter your details and follow the prompts. You can also sign up with **Continue with Google** as a
   shortcut instead of filling in the form by hand.
3. Verify your email address when GitHub asks. This step is not optional: GitHub's own documentation
   states plainly, "Without a verified email address, you won't be able to complete some basic GitHub
   tasks, such as creating a repository." Skipping it just means you hit a wall later.

**Screenshot placeholder:** the github.com/signup screen, showing the fields it currently asks for, so
a reader can match what they see to this step.

## Choosing an email you won't regret

Use an email address you expect to control for years, not one tied to a job or a phone number you
might lose. If your business changes email providers later, you can always add a new address to the
same account, but the account you're creating today should start with an address that's genuinely
yours long-term.

GitHub also gives you a way to keep your real email address out of public view when you commit code
through the browser. Turn on **Keep my email addresses private** in your email settings, and GitHub
generates a private stand-in address for you in the exact form `ID+USERNAME@users.noreply.github.com`.
Anything committed through the GitHub website uses that address instead of your real one. This matters
more once you're publishing public repositories; for a private repository it's a smaller concern, but
there's no reason not to turn it on now.

## Choosing a username you won't regret

Your username becomes part of every profile link and every repository URL you own, so it's worth
thirty seconds of thought before you lock it in.

Two things to know before you pick one:

**It's first-come, first-served, and GitHub does not hold names for you.** GitHub's own username
policy says it directly: "GitHub account names are available on a first-come, first-served basis, and
are intended for immediate and active use." Squatting on a name you're not using is against the rules,
and if the name you want is already taken, GitHub is blunt about your options: "Valid trademark-related
complaints are the only requests we review for possible release of a username that is already claimed."
In plain terms, if someone else already holds the name you wanted, you are very unlikely to get it back
from them, even if it matches your business name. If your exact business name is available, it may be
worth grabbing now for that reason alone.

**You can change it later, but it isn't free of consequences.** GitHub's own documentation on username
changes is specific about what happens:

- "After changing your username, your old username becomes available for anyone else to claim." If
  someone else grabs it and creates a repository with the same name yours had, that overrides your old
  redirect and it stops working.
- "Most references to your repositories under the old username automatically change to the new
  username," but not everything follows automatically.
- "After changing your username, the URLs to any public or secret gists will also change and previous
  links to these will return a 404 error." The same applies to your old profile page link.
- Any CODEOWNERS file that names your old username has to be updated by hand; it does not update
  itself.
- GitHub's own recommendation: "We recommend you update all existing remote repository URLs after
  changing your username," because of the redirect risk above.

None of this means never change it. It means: pick something you're reasonably happy to keep, because
changing it later is possible but has real cleanup attached, not just a cosmetic swap.

## Two-factor authentication: turn it on today

Two-factor authentication (2FA) means signing in needs your password **and** a second proof that it's
really you, usually a six-digit code from your phone. GitHub's own framing: it's "an extra layer of
security that can help keep your account secure." Do this before anything else on this list.

**Methods GitHub currently supports**, per GitHub's own documentation:

- A **TOTP authenticator app** (a phone or desktop app that generates a fresh six-digit code every 30
  seconds).
- **SMS text message** to your phone.
- A physical **security key** (a FIDO2/WebAuthn hardware key, or your device's built-in option like
  Touch ID or Windows Hello).
- A **passkey**, which GitHub says "satisfy both password and 2FA requirements" on its own.
- **GitHub Mobile**, once you've already set up a TOTP app or SMS as your first method.

**Use an authenticator app, not SMS, if you have a choice.** GitHub says so directly: "We strongly
recommend using a TOTP application for two-factor authentication instead of SMS, and using security
keys as backup methods instead of SMS." Their stated reasons: SMS "is susceptible to interception, does
not provide resistance against phishing attacks, has unreliable deliverability, and is not supported in
all countries." A free authenticator app (on the phone you already carry) takes about the same effort
to set up as SMS and doesn't have any of those weaknesses.

**If you do use SMS, know it's not available everywhere.** GitHub's own wording: "Because of delivery
success rates, GitHub only supports two-factor authentication via SMS for certain countries." This is a
maintained list that changes, not a fixed rule, so **confirm your own country is currently on it on
your own screen** before you plan around SMS as your method. At the time this page was written,
Australia was on that list, but check it yourself at the moment you set this up rather than trust that
this stays true.

**How to turn it on:**

1. Click your **profile picture** (top right) → **Settings**.
2. In the **Access** section of the sidebar, click **Password and authentication**.
3. Under "Two-factor authentication," click **Enable two-factor authentication**.
4. Pick your method:
   - **TOTP app:** scan the QR code with your authenticator app (or type in the setup key by hand),
     then enter the six-digit code it shows you under "Verify the code from the app."
   - **SMS:** complete the CAPTCHA, enter your phone number, and enter the code you're texted under
     "Verify the code sent to your phone."
5. Click **Download** to save your recovery codes (see the next section before you do this).
6. Click **I have saved my recovery codes** to finish.

**Screenshot placeholder:** the "Password and authentication" settings page, with the "Two-factor
authentication" section visible, so a reader can find it without hunting.

## Recovery codes: this is the part people skip, and shouldn't

When you turn on 2FA, GitHub gives you a set of one-time backup codes. Each one works exactly once:
"Each code is single-use only: once it has been used to authenticate, it cannot be used again." They
exist for one job: getting you back into your account if you lose your phone, your authenticator app,
or your SMS number.

**Where to get them (any time, not just at setup):** profile picture → **Settings** → **Password and
authentication** → **Recovery codes** → **View**.

**Where to keep them:** GitHub's own advice: "We recommend saving them with a secure password manager."
Not a screenshot on the same phone that holds your authenticator app. Not a note stuck to your monitor.
A password manager, or printed and kept somewhere physically safe, separate from the device that
generates your 2FA codes.

**This is the sentence that makes this whole section matter.** GitHub states it exactly like this, and
it's worth reading twice: **"GitHub Support will not be able to restore access to accounts with
two-factor authentication enabled if you lose your two-factor authentication credentials or lose access
to your account recovery methods."** Not "it's difficult." Not "contact us and we'll sort it out."
GitHub Support itself cannot get you back in. Your recovery codes, or another configured recovery method
(a passkey, a security key, a second device you've already verified), are the only way back in if your
main 2FA device is gone. Download them the day you turn on 2FA, not the day you need them.

## GitHub's mandatory 2FA program

GitHub does not leave 2FA fully optional for every account forever. Since March 2023, GitHub has
required 2FA for accounts that take certain actions that mark them as contributors. Per GitHub's own
documentation, you become eligible for mandatory enrollment if you are:

- Publishing an app or action for others to use.
- Creating a release for your repository.
- Contributing to specific high-importance repositories.
- An administrator or a contributor of a high-importance repository.
- An organization owner.
- An enterprise administrator.

If your account is selected, GitHub notifies you by email and shows on-site banners. That notification
starts a **45-day 2FA enrollment period**. After that window closes, GitHub gives you a further
**7-day grace period** on top of it. If 2FA still isn't enabled once both windows have passed, GitHub's
own wording is direct: **"You will not be able to access GitHub.com until you enable 2FA."** Accounts in
this state also cannot authorize new third-party apps or create new personal access tokens until 2FA is
turned on, though tokens created earlier keep working in the meantime.

The practical read: the moment you create an organization or publish a release (both covered elsewhere
in this kit), you're very likely to land in one of the qualifying groups above. Turning 2FA on now,
voluntarily, means you never see that 45-day clock start at all.

## Signing in on a new device

If 2FA is off, or even sometimes when it's on, GitHub may still ask you to verify a sign-in from a
device or browser it doesn't recognize, a new computer, a new phone, a new browser, or a fresh browser
profile.

- The verification code goes out by email: "The verification code is sent to all primary and backup
  email addresses associated with your account," and it's "valid for one hour."
- If you have the GitHub Mobile app installed, GitHub skips the email and sends a push instead: "GitHub
  sends a verification request to your mobile device, instead of sending an email. Enter the code
  displayed in your browser into the GitHub Mobile app to verify your sign-in."
- Once you've verified a device, GitHub says "you will only need to verify a new device once." It only
  asks again on that same device if you clear your cookies or switch to a different browser on it.

**One warning worth remembering:** if a verification code shows up in your inbox and you didn't just try
to sign in anywhere, GitHub is telling you plainly what that means: "your GitHub password may have been
compromised." Change your password immediately if that happens; don't dismiss the email.

## What to do if you're locked out

Work through these in order:

1. **Try your recovery codes**, if you saved them (login screen → "More options" → 2FA recovery code).
2. **Try another method you've already configured**, if you have one, GitHub's own guidance lists
   "authenticating with another method, such as a passkey, GitHub Mobile, or a security key, if
   pre-configured on the account."
3. **If none of that works, you're into formal account recovery.** GitHub's own troubleshooting page is
   direct about the limit here: "For security reasons, GitHub Support cannot assist with troubleshooting
   your 2FA methods, including SMS delivery." Combined with the line quoted above, if both your 2FA
   device and your recovery codes are gone, there is no support ticket that gets your original account
   back.
4. **The last resort GitHub documents is not account recovery, it's an email release.** If every
   recovery option is genuinely exhausted, GitHub's documentation describes only this: "you can unlink
   an email address tied to the locked account. The unlinked email address can then be linked to a new
   or existing account." Read that carefully: this does not hand your old account, its repositories, or
   its history back to you. It frees your email address so you can use it to start again. This is the
   entire reason recovery codes are step one in this file, not an afterthought.

## Protecting the access you now hold

Once your account is real and secured, it becomes a target worth attacking. Three patterns to know:

**An email asking you to "sign in" from a link inside the email itself.** GitHub's own security alert
about a phishing campaign against its users spells out the check: before you type a password anywhere,
"confirm that the URL in the address bar is 'https://github.com/login' and that the site's TLS
certificate is issued to GitHub, Inc." The safer habit is simpler than checking a certificate under
pressure: never click a sign-in link from an email at all. Open a new browser tab and type github.com
in yourself, every time.

**Anyone asking you for your codes.** Nobody legitimate ever needs your 2FA code, your recovery codes,
or your password read aloud to them, not a client, not "GitHub verification," not a support agent. You
already know from the section above that GitHub Support itself "cannot assist with troubleshooting your
2FA methods." If a message asks you to hand over a code to "verify" or "unlock" your account, that
request is the attack, not a fix for one.

**An app asking for access to your whole account or every repository when it only needs one.** When you
authorize a third-party app on GitHub, the authorization screen lets you choose which repositories it
can see: GitHub's own documentation confirms "you also specify which repositories the app can access."
Read that screen before you click Authorize. If a tool only needs to work with one repository, grant it
that one repository, not "all repositories." You can review and pull access from anything you've
already authorized at profile picture → **Settings** → **Applications**, where each entry has its own
**Revoke** button (or **Revoke all** to clear everything at once).

**Screenshot placeholder:** the Settings → Applications page, showing an authorized app's repository
access, so a reader can see what this screen looks like before they hit it live.

---

## If it goes wrong

**I enabled 2FA and now I can't get the setup screen to accept my code.** Double-check the time on your
phone or computer is correct and set automatically; TOTP codes are time-based, and a clock that's even a
minute or two off will generate the wrong code. If SMS codes aren't arriving, confirm your country is
still on GitHub's supported list before assuming it's a typo in your number.

**I lost my phone and I don't have my recovery codes.** Work through the "What to do if you're locked
out" section above in order. If you truly have no recovery codes and no other configured method, the
honest answer is that GitHub Support cannot get your old account back for you; the only documented path
is unlinking your email and starting fresh. This is exactly why this file puts recovery codes before
almost anything else.

**I got a "verify this device" email or code and I wasn't the one signing in.** Change your password
immediately. That's GitHub's own guidance for an unrequested verification code, and it applies whether
or not the sign-in attempt actually succeeded.

---

## Questions people ask here

**Do I really need 2FA if I'm just one person, working alone, with no releases yet?** Turn it on anyway.
It takes about two minutes, and the moment you create an organization or publish anything (both covered
elsewhere in this kit), GitHub is very likely to require it regardless. Doing it now on your own terms
beats a 45-day countdown you didn't choose.

**Can Claude Code set up 2FA or save my recovery codes for me?** No, and this isn't a limitation worth
working around. GitHub's whole point with 2FA is proving a human is physically present with the phone
or the security key. A terminal assistant has no way to scan your QR code or hold your device, and it
shouldn't be trusted with your recovery codes even if it could.

**Is it fine to reuse a password I already use somewhere else?** Confirm GitHub's current password
requirements on your own screen at sign-up, since this page doesn't repeat a rules list that GitHub
could change. As a habit regardless of the minimum rule: don't reuse a password across sites. If one
site the password was used on ever leaks, every account sharing that password becomes exposed with it,
GitHub included.

**What if the username or organization name I want is already gone?** For a personal username, see the
policy quoted above: trademark disputes are the only path GitHub reviews to release a taken name, so
plan on a variation rather than waiting the original owner out.

**I set up SMS 2FA and now I'm travelling somewhere it doesn't work. What now?** Add a TOTP authenticator
app as an additional method before you travel, from the same Password and authentication settings page.
You can have more than one 2FA method configured at once, so this doesn't require dropping SMS, just not
depending on it as your only option.

---

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
