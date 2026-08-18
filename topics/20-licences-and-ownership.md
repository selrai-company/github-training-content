# Who owns what you put on GitHub, and how licences work

## What this gets you

Everyone learns to click the buttons. Almost nobody is ever told the business question sitting
underneath them: once your work is on GitHub, who actually owns it, and what is anyone else allowed
to do with it? Get this wrong in one direction and you can hand away something that took real money
to build. Get it wrong in the other direction and you can spend a lawyer's afternoon chasing someone
who never actually broke a rule.

This file settles four things in plain terms: what GitHub itself says about who owns the content you
upload, what a licence actually is and what it decides, what happens by default when you never add
one (which surprises almost everyone the first time they learn it), and why the ownership question
for an employee or a contractor is never settled by anything you click on GitHub, only by the
agreement you had them sign.

**Say this plainly, once, at the start: nothing in this file is legal advice.** It is GitHub's own
published wording, quoted directly, plus the general shape of how ownership and licensing work. The
moment real money, a real dispute, or a contract with someone else's business is involved, that is
the point to pay a lawyer for an hour rather than rely on this page. This file tells you exactly
where that point is as it comes up.

**One spelling note before you read on.** GitHub's own documentation always spells this word the
American way, "license", including in every quotation in this file. This file's own sentences use
the Australian spelling, "licence" as a thing you have, "license" as a thing you do to something.
If you see both in the same paragraph, that is why, not a typo.

## Before you start

**You need at least one repository**, public or private. `04-repositories-and-visibility.md` covers
creating one and the public-versus-private choice, which matters directly to this file, read it
first if you have not already.

**You do not need to already understand branches or pull requests.** Adding a licence to an existing
repository is a single new file, covered below, not a change that needs either.

**You need at least Write access to a repository to add a file to it**, the same access level
needed for any other change. `03-members-and-access.md` covers checking or requesting that. If a
repository is not yours, adding a licence to it is a decision for whoever owns it, not something to
do on someone else's behalf.

## The words you need

**Copyright.** The legal right, that exists automatically the moment you create something, to
control who can copy, share, or build on it. You do not have to write the word "copyright" anywhere,
register anything, or ask for it. It is the default background rule everything else in this file sits
on top of.

**Content, or "Your Content".** GitHub's own term for anything you upload, push, or create on the
service, including "your modifications to Content you have forked or cloned", GitHub's exact
wording. The words "owning" and "licensing" in this file are both about Content in this sense.

**Licence.** A legal document that tells other people exactly what they are, and are not, allowed to
do with something you made. GitHub's own plain description: "A software license tells others what
they can and can't do with your source code." A licence does not change who owns the work. It changes
what other people are permitted to do with it.

**Licence file, or LICENSE.** The actual text file a licence lives in inside a repository, almost
always named `LICENSE`, `LICENSE.txt`, or `LICENSE.md`, sitting in the repository's root, GitHub's
own guidance: "Most people place their license text in a file named LICENSE.txt (or LICENSE.md or
LICENSE.rst) in the root of the repository."

**Open source licence.** A licence written to let other people use, change, and share your work
freely, usually with a small number of conditions attached (covered under attribution below), rather
than a licence written to restrict or sell access to it.

**Permissions, conditions, and limitations.** The three things every licence actually decides, in
plain terms. Permissions are what someone is allowed to do (use it commercially, change it,
redistribute it). Conditions are what they have to do in return if they want those permissions
(usually, keep your name on it). Limitations are what the licence explicitly does not promise them
(that the code works, that you are liable if it doesn't). Every licence on GitHub's own licence
comparison site is broken down into exactly these three columns, covered under attribution below.

**Public domain.** A separate thing from an open source licence: work with no copyright restrictions
left on it at all, that anyone can do anything with, no attribution required. Choosing "no licence"
is not the same as public domain, and the difference is covered below because it is a genuinely
common mix-up.

**Attribution.** Keeping the original creator's name, and usually a copy of the licence text itself,
attached to a piece of work when you reuse it. Whether attribution is required, and exactly what form
it has to take, is decided by the specific licence, not by GitHub or by general politeness.

**Administrative control.** A separate idea from ownership, specific to GitHub's own account system:
who can manage settings, access, and billing for an account or an organization. GitHub's own wording
distinguishes it plainly from Content ownership, covered in the next section.

## How to do it

### What GitHub itself says about who owns what you upload

GitHub's own Terms of Service state this directly, in a section headed "Ownership and License
Grants": "You own Your Content. If you post Content you did not create, you are responsible for
ensuring you have the right to post it and for complying with any applicable licenses." That is the
whole rule, in GitHub's own words. Whoever's account created or uploaded the work owns it, full stop,
as far as GitHub's own agreement with you is concerned.

**Do not confuse that with "administrative control", which is a separate thing.** GitHub's Terms
spell the two apart. For a personal account: "you retain ultimate administrative control over your
Personal Account and the Content within it." For an organization: "The 'owner' of an Organization...
has ultimate administrative control over that Organization and the Content within it." Administrative
control is about who can manage settings, membership, and access on GitHub itself. It is not GitHub
deciding who legally owns the copyright in what was typed. Those are two different questions, and
GitHub's own wording keeps them separate on purpose.

**A genuinely important detail if your business pays for a GitHub plan under a signed agreement with
GitHub**, rather than a personal card on a personal account: a different, business-specific version
of these terms, GitHub's Corporate Terms of Service, may cover your organization instead of the
standard one quoted above, and it is worded differently in a way that actually matters. Its ownership
clause reads: "Customer retains ownership of Customer Content that Customer creates or owns." Broadly
the same idea, ownership stays with whoever created it, but the licence your business grants back to
GitHub under this version is narrower than the standard one, covered in the very next point. Which of
these two agreements actually covers your account depends on how it was set up. Confirm this directly
with GitHub, or with whoever set up your organization's billing, rather than assuming.

### What you're actually agreeing GitHub can do with it

Owning your content does not mean GitHub has no rights to it at all, you did agree to something by
using the service. Under the standard Terms, the licence you grant back to GitHub is worded broadly:
"You grant GitHub and our Affiliates the right to store, host, archive, parse, display, and make
copies of Your Content as necessary to provide, develop, and improve the Service, **including by
training AI Features**, and for the purpose of training, developing, and improving artificial
intelligence and machine learning models and technologies of our Affiliates." Read that a second
time. It explicitly includes using your content to train GitHub's own AI features.

**The Corporate Terms of Service version, covered above, is narrower on this specific point.** Its
equivalent clause limits the licence to storing, archiving, parsing, and displaying content "only as
necessary to provide the Service, including improving the Service over time", and states plainly:
"This license does not grant GitHub the right to sell Customer Content. It also does not grant GitHub
the right to otherwise distribute or use Customer Content outside of our provision of the Service." No
AI-training language appears in the version this file could find. If whether GitHub can use your
business's code to train its AI features is something you care about, this is exactly the kind of
detail worth confirming for your specific account, in writing, rather than assuming either version
applies.

**None of this changes what a public repository exposes.** GitHub's own Terms are direct about
public repositories specifically: "By setting your repositories to be viewed publicly, you agree to
allow others to view and 'fork' your repositories... By making a repository public, you grant other
Users a nonexclusive, worldwide license to use, display, perform and reproduce (by forking) Your
Content through the Service as permitted by GitHub's functionality." That right to view and copy a
public repository exists the moment you make it public, whether or not you have added a licence file
at all. `04-repositories-and-visibility.md` covers exactly what "public" exposes and why flipping
back to private afterwards doesn't undo it.

### What happens if you never add a licence, and why it surprises people

This is the single most common thing people get wrong about this topic, so it is worth stating
plainly, in GitHub's own words: "You're under no obligation to choose a license. However, without a
license, the default copyright laws apply, meaning that you retain all rights to your source code and
no one may reproduce, distribute, or create derivative works from your work."

Read that carefully. **No licence does not mean "up for grabs."** It means the exact opposite: full
copyright, all rights reserved, by default, automatically, whether you meant it that way or not.
GitHub's own licence guidance says it even more bluntly for the reader on the other side of this: "if
you find software that doesn't have a license, that generally means you have no permission from the
creators of the software to use, modify, or share the software." Being able to see a public
repository, or even copy it, is not the same as being allowed to use it. Covered in full under "using
someone else's code" below.

**For a private repository, this is nothing to think about at all.** Access to a private repository
is already controlled by who you've explicitly shared it with, covered in
`03-members-and-access.md`, and licensing is a question about what strangers are allowed to do with
something they can see. If nobody outside your business can see it, there is no licensing decision to
make yet. Most repositories a small business creates should stay in exactly this state: private, no
licence, nothing more to do.

### Adding a licence, and where it actually lives

**When you're creating a brand new repository**, GitHub offers a licence picker directly on the
creation screen, covered in `04-repositories-and-visibility.md`'s repository-creation steps. GitHub's
own note on this: "The license picker is only available when you create a new project on GitHub."

**For a repository that already exists**, add one through the browser:

1. On the repository's main page, above the file list, click the **Add file** dropdown, then click
   **Create new file**.
2. In the file name field, type `LICENSE` (in capitals, exactly as GitHub's own instructions word
   it) or `LICENSE.md`.
3. Underneath the file name field, click **Choose a license template**.
4. On the left side of the page that opens, review the list of available licences and select one.
5. Click **Review and submit**.
6. Click **Commit changes...**, add a short message describing what you did, and click **Commit
   changes** or **Propose changes**, whichever is offered.

**The confirmation.** GitHub's own wording for what happens once this is done: "people who visit your
repository will see it at the top of the repository page." GitHub detects the licence automatically
by comparing your `LICENSE` file against a list of known licences, so an unusual or heavily edited
licence file may not be recognised and shown, even though the file is genuinely there.

**Screenshot placeholder:** the "Choose a license template" screen, showing the list of licences down
the left and a preview of the selected one on the right, so a reader can see what this actually looks
like before they click through it themselves.

### Choosing a licence, when you actually want to give something away

GitHub built its own tool specifically for this decision, at `choosealicense.com`, GitHub's own
words: "We created choosealicense.com, to help you understand how to license your code." It is
GitHub's own site, not a third party, and it offers a short, plain-English decision path rather than a
legal document to read cold:

- **Fitting into an existing community or project.** "Use the license preferred by the community
  you're contributing to or depending on. Your project will fit right in."
- **Wanting it simple and permissive.** "The MIT License is short and to the point. It lets people do
  almost anything they want with your project, like making and distributing closed source versions."
- **Caring about your improvements staying open.** "The GNU GPLv3 also lets people do almost anything
  they want with your project, except distributing closed source versions", meaning anyone who builds
  on your GPLv3 work has to share their own version openly too, they cannot fold it into a closed,
  paid product.

As a concrete example, here is exactly what the MIT licence, the most common permissive choice,
actually decides, taken straight from GitHub's own comparison table for it: permitted uses are
commercial use, distribution, modification, and private use, all allowed. The one condition is
"License and copyright notice", meaning your name and the licence text have to stay attached to any
copy. The explicit limitations are that you are not liable if it breaks, and you give no warranty
that it works.

**The honest advice this kit will give you, that is not a GitHub rule, it is judgement:** a licence
is for something you have deliberately decided to give away or share, not for something you're trying
to protect. If what's in the repository is commercially sensitive, the right move is never "pick a
restrictive licence." It's keeping the repository private in the first place, covered in
`04-repositories-and-visibility.md`. Adding any licence at all, restrictive or not, to something
public is already a decision to let people reuse it under those terms. If you are not sure you want
that yet, the repository staying private and licence-free is the safer default until you are.

**GitHub says this plainly about itself too, and it's worth repeating rather than paraphrasing:**
"we're not lawyers and that we make mistakes like everyone else... If you have any questions
regarding the right license for your code or any other legal issues relating to it, it's always best
to consult with a professional." If real money is riding on the choice, that is the point to pay for
an hour of a lawyer's time, not the point to guess from a comparison table, GitHub's own or this
kit's.

### Using someone else's code in your business, and checking you're allowed to

Flip the same rule around, and this is the version most small businesses actually run into: someone
finds a useful piece of code, a script, a library, a template, on GitHub, and wants to build it into
something the business sells or relies on.

**The default rule, again in GitHub's own words, is the same one from above, read from the other
side:** "if you find software that doesn't have a license, that generally means you have no
permission from the creators of the software to use, modify, or share the software. Although a code
host such as GitHub may allow you to view and fork the code, this does not imply that you are
permitted to use, modify, or share the software for any purpose." Being able to see it and copy it on
GitHub is a platform feature, not a legal permission.

If you find code with no licence attached at all, GitHub's own recommended options are exactly two:
"Ask the maintainers nicely to add a license", or "Don't use the software. Find or create an
alternative that is under an open source license." There isn't a third option where you use it anyway
and hope nobody notices.

**If the code does have a licence, read what it actually says before you build on it, particularly
for anything you plan to sell.** The permissions-conditions-limitations breakdown covered above
applies here just as much: an MIT-style licence generally lets you fold the code into a closed, paid
product as long as you keep the attribution notice. A GPL-family licence generally does not, it can
require that anything you build using it, and distribute to customers, be shared under the same open
terms, which is a serious constraint on a product you intend to sell as closed software. This is
exactly the kind of decision worth a lawyer's hour before you build a real product on top of someone
else's licensed code, not something to eyeball from the licence's name alone.

**GitHub also lets you search specifically by licence.** You can filter repositories using a
`license:` qualifier and the licence's exact keyword, for example `license:mit`, when you're
deliberately looking for something you know you'll be allowed to reuse, rather than finding something
useful first and checking afterwards.

### Employees and contractors: why this is a contract question, not a GitHub setting

This is the point in this file worth reading twice if your business pays anyone, staff or
contractors, to write code, documents, or anything else that ends up on GitHub.

**GitHub's "you own Your Content" rule, quoted at the start of this file, tells you who owns
something as between that person's account and GitHub. It does not tell you who owns it as between
an employer and an employee, or between a business and a contractor, once someone was paid to make
it.** That second question is a matter of the agreement between the business and the person doing the
work, an employment contract, a contractor or consulting agreement, or, absent any written agreement
at all, whatever the general copyright rules for that situation happen to default to, which vary and
are exactly the kind of thing worth a lawyer confirming rather than assuming.

**Nothing on GitHub settles this.** There is no setting, checkbox, repository permission, or
organization role anywhere on GitHub that transfers copyright ownership from one person or business
to another. Having Write access to push code, being listed as the commit author, or even being the
person who physically typed it, none of that is the same as owning it once money and a contract are
involved. GitHub's account and access system, covered in `03-members-and-access.md`, controls who can
do what on the platform. It has nothing to do with who owns the work underneath it.

**The practical habit worth adopting, not a legal rule, judgement:** get the ownership assignment
written into the contract before the work starts, not worked out afterwards from who has push access
to the repository. A one-line clause in an employment or contractor agreement, stating plainly that
anything created for the business in the course of the work belongs to the business, is a small,
one-time cost. Sorting out an ownership dispute after the fact, with nothing written down, is not.
This is squarely a "pay the lawyer" moment, specifically for getting that clause worded correctly for
your situation, before anyone starts pushing code.

## Strategy: how to actually use this

**A solo operator working alone** barely needs to think about any of this. Keep repositories private
by default, add nothing licence-related unless you deliberately decide to share something with the
world. The only real trigger to come back to this file is the day you either bring on your first
contractor or employee, or decide to give something away publicly.

**The moment you bring on your first contractor.** Before they push a single line, have the
ownership clause in their agreement. Do not treat this as something to sort out later once there's a
repository to argue about. This is the single highest-value five minutes in this entire file for a
growing small business.

**If you want to give something away** (a free tool, a template, a checklist, something built for
goodwill or reputation rather than revenue), work through the choosealicense.com decision guide
above. MIT is the sensible permissive default unless you have a specific reason to force people to
share their improvements back, in which case GPLv3 is GitHub's own suggested alternative.

**If you're not sure whether something is "giving away" or "commercially sensitive"**, treat it as
sensitive until you decide otherwise. Default private, no licence. You can make something public and
licensed later at any time. You cannot undo who already copied it once it was public, covered in
`04-repositories-and-visibility.md`, so the safer direction to be wrong in is starting closed.

**What good looks like months later:** every repository holding something the business actually
depends on is private, with no licensing question left open because there's nothing there to license
out. Anything public and intentionally shared has a licence file that matches what you actually meant
to allow, chosen deliberately rather than left as whatever the creation screen defaulted to. Every
contractor and employee agreement already states, in writing, who owns what they build, settled
before they started, not argued about after they left.

## A worked example

The café's ordering site, this kit's recurring example, is built by the owner's technical nephew,
paid per project as a contractor. The repository is private from the start, nothing public, and it
stays that way. No licence file exists in it, and that is entirely correct, not a gap to fix, because
nobody outside the business has access to it in the first place.

Before the nephew wrote a single line for this project, the owner had him sign a short agreement
stating plainly that anything he builds for the café's business belongs to the café, once he's paid
for it, not to him personally. That single clause is what actually decides who owns the ordering
site's code. It has nothing to do with GitHub, and nothing on the repository's settings page could
have achieved the same thing.

Some months later, the nephew wants to reuse a small, genuinely generic "print a receipt neatly"
script he originally wrote for the café, in a different, unrelated project for someone else. Whether
that's allowed depends entirely on what his agreement with the café actually says, not on which
repository the script currently happens to live in, and not on the fact that he was the one who
typed it.

Separately, the owner puts together a short, genuinely useful checklist for other café owners in her
local business network, something with no commercial value to her business specifically, and decides
to share it properly rather than just emailing a document around. She creates a new public
repository for it, and, using the click path above, adds an MIT licence. Now anyone in her network,
or anyone else who finds it, can use her checklist however they like, including inside their own
paid materials, as long as they keep her name on it, which is exactly the one condition the MIT
licence attaches.

## If it goes wrong

**I found code with no licence and want to use it in something the business sells.** Don't, not as
it stands. GitHub's own guidance gives exactly two honest options: ask the person who made it to add
a licence, or find a different piece of code that already has one. Using it anyway and hoping nobody
notices is not a third option worth risking a real product on.

**A contractor who's left now claims code they wrote for the business is theirs.** Whatever the
signed agreement between the business and that contractor actually says is what decides this, not
GitHub, and not who has push access today. If there was no written agreement covering it, this is
exactly the situation to take to a lawyer rather than try to settle it by changing repository access
or arguing about commit history.

**I made a repository holding real client or business content public, and it had no licence
attached.** No licence being attached does not undo what public exposure already did. GitHub's own
Terms confirm that once a repository is public, others already have the right to view and fork it,
whether or not a licence file exists. Follow `04-repositories-and-visibility.md`'s steps to make it
private again immediately, and treat anything sensitive it held as potentially already seen or
copied, the same way that file treats a leaked secret.

**I added a licence and now think it was the wrong one, or want it gone.** You can change or remove
a `LICENSE` file the same way you added it, as a normal commit. Be honest with yourself about what
that does and does not undo: it changes what the repository currently offers going forward. It does
not reach back and cancel whatever permission the old licence already gave someone for a copy they
took while it was in place. That's the general shape of how licences work, not a specific point this
kit found stated word for word on GitHub's own pages for this exact scenario, so if real stakes ride
on it, confirm with a lawyer rather than assume.

## FAQ

**Does making my repository private already protect my code the way a licence would?** They do two
different jobs. Private controls who can see the repository at all. A licence controls what someone
who already has permission to see it is allowed to do with it. If nobody outside your business needs
to see something, private with no licence is the simpler, and safer, combination. You don't need a
licence to protect something nobody else can reach.

**I'm the only person doing the work in my business. Do I need to do anything about ownership?**
Generally not. GitHub's own rule is that you own what you post yourself. The contractor and employee
question in this file matters once someone else is being paid to build something for the business,
not before.

**Does GitHub use my private code to train its own AI features?** It depends which version of
GitHub's terms actually covers your account, and the two versions this file found say genuinely
different things, covered in full above. The standard personal terms explicitly include training AI
features as part of what you license back to GitHub. The business-specific Corporate Terms of Service
this file found is narrower and does not include that wording. Confirm directly which one applies to
your account if this matters to you, rather than assuming either way.

**What's the actual difference between "no licence" and "public domain"?** They sound similar and
are not. No licence, GitHub's own default, means full copyright, all rights reserved, nobody may
reuse it without your permission. Public domain is the opposite: you've deliberately given up those
rights so anyone can do anything with it, no permission or attribution needed. GitHub's own licence
guidance flags this mix-up directly: "Disallowing use of your code might not be what you intend by
'no license'... If your goal is to completely opt-out of copyright restrictions, try a public domain
dedication instead." If you actually want to give something away with no strings at all, a licence
choice like CC0 does that; not adding a licence does the opposite.

**Someone is using my public, licensed work and ignoring the licence's conditions, for example
stripping out the attribution an MIT licence requires. Will GitHub step in?** GitHub's own disclaimer
about its licensing tools is direct: it displays licence information to help you make an informed
choice, states plainly "we're not lawyers", and takes no responsibility for enforcing what a licence
says. Enforcing a licence someone has broken is a legal question between you and them, worth a
lawyer's involvement once it's a real problem, not a GitHub support request.

**Do I have to add a licence to every repository I create?** No. GitHub's own wording is explicit:
"You're under no obligation to choose a license." Most repositories a small business creates, the
private, working ones, should have none at all. A licence only becomes a real decision the moment
you're sharing something publicly and mean for other people to actually use it.

## Quick reference

- **No licence, private repository:** normal, nothing to do, this describes most repositories a
  small business will ever create.
- **No licence, public repository:** full copyright, all rights reserved, by default. Others can
  still view and fork it under GitHub's own Terms, that is not the same as having permission to use
  it.
- **Add a licence when creating a repository:** the licence picker on the creation screen, see
  `04-repositories-and-visibility.md`.
- **Add a licence to an existing repository:** **Add file** > **Create new file** > name it `LICENSE`
  > **Choose a license template** > pick one > **Review and submit** > commit.
- **Giving something away, simple and permissive:** MIT. **Want improvements shared back:** GPLv3.
  **Joining an existing project:** match its own licence. Full guide at `choosealicense.com`, GitHub's
  own site.
- **Found code with no licence?** Assume you don't have permission to use it. Ask the creator to add
  one, or don't use it.
- **Employee or contractor ownership:** a contract question, never a GitHub setting. Get it written
  into the agreement before the work starts.
- **Commercially sensitive work:** keep it private. A licence is for what you deliberately give away,
  not for what you're protecting.
- **Not legal advice.** Pay a lawyer for: the ownership clause in an employment or contractor
  agreement, choosing a licence with real money riding on it, and enforcing a licence someone has
  broken.

## Sources

- https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- https://docs.github.com/en/site-policy/github-terms/github-corporate-terms-of-service
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
- https://choosealicense.com/
- https://choosealicense.com/licenses/mit/
- https://choosealicense.com/no-permission/
