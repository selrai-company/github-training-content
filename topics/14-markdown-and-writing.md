# Markdown, and writing things people can actually read

The first thing you ever type on GitHub, a comment, a README, an issue, a pull request description,
gets written in Markdown. This file covers what Markdown actually is, the marks that turn plain text
into formatting, what GitHub adds on top of standard Markdown, and how to write a README someone can
actually use. Everything below works the same wherever you type it on GitHub: a comment box, an issue,
a pull request, or a file that ends in `.md`.

## What this gets you

Right now, if you write a plain paragraph in a GitHub comment or a README, it reads as one dense block
of text, no matter how important some of it is. Markdown fixes that. A few characters typed around
your words turn into headings, bold text, checklists, and tables the moment GitHub displays them, so a
teammate can scan a pull request description in ten seconds instead of reading every word, a new hire
can find the one command they need in a README without hunting through paragraphs, and a bug report
with a checklist actually gets worked through instead of half-forgotten. None of this needs a course.
It is a handful of marks you will use constantly from your very first week on GitHub.

## Before you start

You do not need anything set up to read this file or try the examples below. Any text box on GitHub,
a comment, an issue, a README, accepts Markdown the same way.

You will get more out of this file if you have already read `04-repositories-and-visibility.md` (so
you know what a repository and a README are) and `05-daily-workflow.md` (so you know how to open and
edit a file). If you have not, that is fine, come back to this file once you have somewhere to try
these examples for real.

## The words you need

**Markdown.** Plain text with a small set of marks around it, like `**this**` or `# this`, that
GitHub turns into formatting (bold text, a heading) when it displays your writing. You always type
the plain marks; GitHub does the turning-into-formatting part.

**Rendering, or rendered.** The formatted version GitHub shows you, after it has read your Markdown
marks and turned them into headings, bold text, lists, and so on. "Raw" means what you actually typed,
marks and all, before GitHub renders it.

**GitHub Flavored Markdown.** GitHub's own name for the version of Markdown it supports. It is
standard Markdown plus a handful of extra, GitHub-specific features layered on top, covered later in
this file: mentioning a person with `@`, and linking straight to an issue or pull request by typing
its number.

**Heading.** A line marked to stand out as a title for the section under it, made with one or more `#`
characters at the start of the line.

**Fenced code block.** A block of text set off from the rest of your writing by a line of three
backticks (`` ` ``) above it and another line of three backticks below it, so GitHub displays it
exactly as typed, in a fixed-width font, instead of trying to format it.

**Inline code.** A short piece of code or an exact word wrapped in single backticks in the middle of a
sentence, so it stands out from the surrounding prose.

**Task list.** A line that starts with `- [ ]` or `- [x]`, which GitHub turns into a real, clickable
checkbox instead of plain text.

**Blockquote.** A line or paragraph marked with a `>` at the start, so GitHub displays it as a quoted
passage, set apart from your own writing.

**README.** A file named `README`, almost always written in Markdown as `README.md`, that GitHub shows
automatically on a repository's front page, so anyone who opens the repository sees it first.

**Mention.** Typing `@` followed by someone's username inside a comment, which notifies that person and
links straight to their profile.

**Autolink, or reference.** Typing something GitHub recognizes, like `#12` for issue or pull request
number 12, or a full web address on its own, and having GitHub turn it into a clickable link
automatically, without you writing out the link syntax yourself.

## How to do it

### Headings

Put one to six `#` characters at the start of a line, then a space, then your heading text. GitHub's
own words: "To create a heading, add one to six `#` symbols before your heading text. The number of
`#` you use will determine the hierarchy level and typeface size."

```
# A big heading
## A smaller heading
### Smaller again
```

Use headings to break a long README or a long comment into sections someone can jump between. Do not
bother with a heading in a two-sentence comment, there is nothing to break up yet.

### Bold, italic, and a line through

```
**This is bold**
*This is italic*
~~This has a line through it~~
```

Bold pulls the eye to the one word or phrase that matters most in a sentence, "the deadline is
**Friday**, not Monday." Do not bold whole paragraphs, once everything is bold, nothing stands out
anymore.

### Lists

```
- First item
- Second item
- Third item
```

```
1. First step
2. Second step
3. Third step
```

Use a plain list (with `-`) when order does not matter. Use a numbered list when it does, like steps
someone has to follow in sequence. One thing worth knowing before it confuses you: GitHub renumbers a
numbered list for you when it renders it, so typing `1.` on every line still produces a correctly
numbered list, 1, 2, 3, on screen.

### Task lists, the checkbox kind

```
- [ ] Update the opening hours
- [ ] Fix the broken image on the menu page
- [x] Reply to the supplier email
```

The hyphen and a space come first, then square brackets: a space inside them for an unchecked task, a
lowercase `x` for a checked one. GitHub's own description: "A tasklist is a set of tasks that each
render on a separate line with a clickable checkbox." You can use one in any comment on GitHub, which
covers issues, pull requests, and discussions. One real limit worth knowing: GitHub's own
documentation notes "you cannot create tasklist items within closed issues or issues with linked pull
requests," so if your checkboxes are not turning into real boxes, check whether the issue you are
writing in is already closed.

One older feature is worth a note so you are not confused if you read about it elsewhere. GitHub used
to offer an enhanced version of task lists inside issue bodies specifically, called tasklist blocks,
with extra tracking features layered on top. GitHub's own documentation says plainly that "tasklist
blocks are retired" and points people toward sub-issues instead for that specific tracking job. That
retirement is about the enhanced version only. The plain checkbox syntax above still works everywhere,
exactly as described.

### Links and images

```
[SelrAI's practice repository](https://github.com/selrai-company/github-training-content)
```

```
![A screenshot of the ordering page](image-url-here)
```

GitHub's own words: "You can create an inline link by wrapping link text in brackets `[ ]`, and then
wrapping the URL in parentheses `( )`," and an image works the same way with a `!` in front of it. You
do not need to write the link syntax at all for a plain web address on its own line, GitHub turns a
bare address like `https://github.com` into a clickable link automatically.

### Quoting someone

```
> The site went down again this morning, right after the update.
```

A `>` at the start of a line turns that line into a quoted passage, set visually apart from your own
writing, which is worth using whenever you are responding directly to a specific line someone else
wrote, so nobody has to guess what you are replying to.

There is also a shortcut for quoting something someone already wrote, so you never have to retype it.
While reading a conversation on GitHub, highlight the text you want to quote with your mouse, then
press the **R** key on your keyboard. GitHub inserts that exact text into your own comment box,
already formatted as a quote with the `>` mark in front of it, ready for you to reply underneath.

### Tables

```
| Item          | Price   |
| -------------- | ------- |
| Coffee         | $4.50   |
| Toasted sandwich | $9.00 |
```

The pipe character (`|`) separates columns, and the row of hyphens under the header tells GitHub where
the header row ends and the data begins. Two rules GitHub actually enforces: "You must include a blank
line before your table in order for it to correctly render," and "there must be at least three hyphens
in each column of the header row." Miss either one and the table shows up as a jumbled line of pipe
characters instead of a table. The pipes on the far left and right edges are optional, and your columns
do not need to line up neatly in the raw text, only the pipes and the hyphen row actually matter.

Tables earn their place when you are comparing more than two things side by side, a price list, a
comparison of options. For two items, a short list usually reads faster than a table.

### Code blocks, and why they matter

Wrap anything you want shown exactly as typed, a command, an error message, a piece of code, in a line
of three backticks above it and three below.

````
```
Error: could not connect to the ordering service
```
````

Add a word straight after the opening three backticks to turn on colour-coded highlighting for that
language, for instance ` ```html ` for a snippet of HTML.

A code block matters because it is the one piece of Markdown that protects your text from being
touched. GitHub will not turn straight quotes into curly ones inside it, will not collapse extra
spaces, and will not try to make a line starting with a number look like a numbered list. If you are
ever pasting something a reader needs to copy back out exactly, an error message, a command, a link
that must not be auto-formatted, a code block is the way to guarantee it survives untouched. GitHub's
own recommendation: "place a blank line before and after code blocks to make the raw formatting
easier to read." If your code block itself needs to show three backticks inside it (rare, but it
happens if you are demonstrating Markdown itself, as this file does above), wrap the whole thing in
four backticks instead of three, GitHub's own documentation is explicit that this is how you nest one
inside the other.

### What GitHub adds beyond standard Markdown

**Mentioning a person.** Type `@` followed by their username, `@janesmith`, anywhere in a comment.
GitHub's own words: "You can mention a person or team on GitHub by typing `@` plus their username or
team name. This will trigger a notification and bring their attention to the conversation." One real
limit worth knowing before you assume a mention silently failed: GitHub's own documentation states "a
person will only be notified about a mention if the person has read access to the repository and, if
the repository is owned by an organization, the person is a member of the organization." If you mention
someone and they never seem to notice, check whether they actually have access to that repository
(`03-members-and-access.md` covers granting it).

**Referencing an issue or pull request by number.** Type `#` followed by the number, `#12`, and GitHub
turns it into a link to that issue or pull request, right inside your text. To point at one in a
different repository, add the owner and repository name in front: `selrai-company/github-training-content#12`.

**Closing an issue automatically from a pull request.** A small extension of the same idea: typing a
keyword like `Fixes #12` or `Closes #12` in a pull request's description links the two and closes the
issue the moment the pull request merges. `07-pull-requests.md` covers this in full, including GitHub's
own complete list of keywords that trigger it.

### Previewing before you post

Every comment box on GitHub has two tabs above where you type: **Write**, where you type your Markdown,
and **Preview**, where you can see exactly how it will render before anyone else does. Type your
comment in the **Write** tab, then click the **Preview** tab above it, in the same box, to check your
headings, lists, and links turned into what you meant before you post it. GitHub's own documentation
across its writing guides consistently tells you to "click the Preview tab" to check your formatting.

GitHub's own words describe what sits alongside those two tabs: "Every comment field on GitHub contains
a text formatting toolbar," letting you apply bold, italics, headings, links, and lists by clicking a
button instead of typing the marks yourself, plus GitHub-specific buttons for mentions and task lists.
If you would rather click than remember syntax, that toolbar sits directly above the text box, and it
produces the exact same Markdown as typing it by hand.

**Through Claude Code:** if you ask Claude Code to write or update a README, an issue description, or
any other Markdown file for you, it edits the file's raw text directly, the same characters described
in this file. Claude Code does not show you a rendered preview the way GitHub's Preview tab does, so
open the file in your browser afterward and check it looks the way you meant, especially the first
time you try something new like a table.

### Where Markdown shows up across GitHub

Anywhere you can leave a comment, an issue, a pull request, a discussion, applies. GitHub's own words
confirm this broadly: "Every comment field on GitHub contains a text formatting toolbar," which only
exists because every one of those fields accepts Markdown. Any file in your repository ending in `.md`
is rendered the same way when you view it on github.com, plain formatting instead of raw symbols, which
is exactly what makes a README readable rather than a wall of hash signs and asterisks.

### Writing a README someone can actually use

GitHub's own description of the point of a README: "communicate important information about your
project" to anyone who opens it. GitHub's own list of what it should cover: "What the project does, Why
the project is useful, How users can get started with the project, Where users can get help with your
project, Who maintains and contributes to the project." That is also a reasonable order to write them
in, what it is, and how to get started, near the top, before anything else.

A copy-and-pasteable starting skeleton for a small project's README:

```
# Ordering Site

What this project is: the website customers use to order from the counter online.

## Getting started

1. Open this repository in your browser or clone it with Claude Code.
2. Menu prices live in `menu.json`. Edit that file to change a price.
3. Opening hours live in `hours.json`.

## Where to get help

Post in the community, or ask whoever set this repository up.

## Who maintains this

Set up by [name], [date]. Ask before changing anything under the `site/` folder directly.
```

For GitHub to show your README automatically on the repository's front page, it needs to be named
`README` (almost always saved as `README.md`) and sit in one of three places. GitHub's own words: "If
you put your README file in your repository's hidden `.github`, root, or `docs` directory, GitHub will
recognize and automatically surface your README to repository visitors." The plain root of your
repository, the same place your other top-level files live, is the right choice for almost every small
project. If more than one exists in different places, GitHub picks between them using that same order,
`.github` first, then root, then `docs`.

## Strategy: how to actually use this

**Bother with formatting when a reader has to find something inside your writing. Skip it when they
just have to read it.** A one-line comment ("done, pushed to main") does not need a heading. A README,
a pull request description with three separate changes in it, or a bug report someone will scan under
pressure, does. The test is whether formatting saves the reader time. If it does not, plain sentences
are faster to write and just as easy to read.

**Solo, your README is a note to future-you.** Keep it short: what the project is, and enough to
remember how it works when you come back to it in six months with no memory of today. You do not need
a "Where to get help" section if there is nobody but you to ask.

**A team of three or four, your README is the difference between someone asking you a question and
finding the answer themselves.** The "Where users can get help" and "Who maintains and contributes"
sections stop being optional at this size, they are what stops a new person from interrupting you for
something already written down. Add a short "How this repository is organized" note once the project
has more than a couple of folders, so nobody has to guess what `site/` versus `assets/` means.

**Use task lists in a pull request description or an issue once a change has more than one real step**,
so a reviewer can see what is done and what is left at a glance, and so the change does not quietly get
half-finished. For a one-line fix, a task list is overhead, just say what you changed.

**Use a code block whenever something must be copied exactly.** An error message, a command, a price,
a URL you do not want auto-formatted. This is the one rule worth turning into a habit rather than a
judgement call: if a reader might copy and paste it, wrap it in a code block, every time, without
having to think about whether this particular instance deserves one.

**What good looks like months later:** your README still describes what the project actually does
today, not what it did when you first wrote it. The habit that keeps that true is small and specific,
whenever you change something the README describes (a command, a file's purpose, how to get started),
update the README in the same sitting, not "later." A README that quietly went stale is worse than no
README, because a reader trusts it and gets it wrong.

## A worked example

A café owner runs an online ordering site with two other people: her nephew, who built it, and a staff
member who updates the menu and hours. The site's Saturday hours are wrong.

She opens an issue on the repository. She writes a short heading-free description, since it is short
enough not to need one, then adds one line in a code block showing exactly what is currently on the
site:

```
Saturday: 8am - 3pm
```

and one line below it, in plain text, saying what it should say instead: "Saturday: 8am to 1pm, we
changed this two weeks ago and the site was never updated." She clicks **Preview** to check the code
block rendered as a fixed block, not a numbered list (the "8" at the start briefly worried her), confirms
it looks right, and posts the issue.

Her nephew picks it up. He fixes the file, then opens a pull request. In the description, he writes:

```
Fixes #12

Updated Saturday hours in `hours.json` to match what's posted outside the shop.

- [x] Checked the file matches the sign outside
- [x] Confirmed it displays correctly on the live preview
```

Typing `Fixes #12` links his pull request straight to her issue, and means it will close automatically
the moment this merges, so nobody has to remember to close it by hand afterward. He mentions her
directly underneath with `@` and her username, asking her to have a look before he merges it, since she
is the one who knows the actual hours.

She opens the pull request, clicks the **Files changed** tab, and sees the one line that changed. She
had one question, so she highlights the original wrong line in the conversation, presses **R** to quote
it, and asks underneath it whether Sunday needs the same fix. He replies that Sunday is already correct,
she approves, and he merges it.

A new casual staff member joins the following month. Instead of asking anyone where the hours live, she
opens the repository, reads the README's "Getting started" section, sees "opening hours live in
`hours.json`," and finds it herself in under a minute.

## If it goes wrong

**My heading looks like plain text with hash signs in front of it, not an actual heading.** You are
missing the space between the `#` and your text. `#Like this` stays plain text; `# Like this`, with a
space, becomes a heading.

**My list, table, or code block is not rendering, it just shows the raw symbols.** The most common
cause is a missing blank line directly above it. GitHub needs that blank line to know where your
regular paragraph ends and the list, table, or code block begins.

**My table shows up as a jumbled line of pipe characters instead of columns.** Check two things: a
blank line sits above the table, and the row of hyphens under your header has at least three hyphens
in every column. Two hyphens is not enough, GitHub will not treat it as a table's header separator.

**I mentioned someone with @ and nothing happened, no notification, no highlighted link.** Check that
the username is typed exactly right, and that the person actually has access to the repository you
mentioned them in. GitHub's own rule is direct: no access means no notification, even if the mention
itself renders as a link.

**My checkboxes are not turning into real, clickable boxes.** Check the exact spacing: a hyphen, a
space, an open bracket, a space or an `x`, a close bracket, then another space before your text,
`- [ ] Like this`. A missing space anywhere in that pattern is the usual cause. If the spacing is right
and it still is not working, check whether the issue you are writing inside is already closed, GitHub
will not create new task list items there.

**A code block I pasted broke the formatting around it.** If the thing you are showing inside your code
block itself contains three backticks (you are demonstrating Markdown itself, for instance), wrap the
whole block in four backticks instead of three, so GitHub knows where your outer block actually ends.

## FAQ

**Do I need to memorize any of this before I start using GitHub?** No. Every comment box has a
formatting toolbar above it that does bold, italic, headings, links, and lists for you with a click,
and a **Preview** tab so you can check the result before you post. Typing the marks by hand gets faster
with use, it is never required.

**Does the same Markdown work in a comment and in a README file?** Yes. GitHub renders GitHub Flavored
Markdown the same way everywhere it applies, a comment, an issue, a pull request description, or a
`.md` file in your repository.

**If I paste a plain web address, does it automatically become a clickable link?** Yes, GitHub turns a
standard URL into a link on its own, no brackets or parentheses needed for that specific case.

**Can I edit a README or write Markdown through Claude Code instead of the browser?** Yes. Ask it, in
plain English, to write or update the file, and it edits the raw text directly. Because Claude Code
does not show you a rendered preview the way GitHub's own Preview tab does, open the file in your
browser afterward to check it rendered the way you intended, particularly the first time you try
something like a table.

**Can I use Markdown in a commit message?** This kit could not confirm a documented answer either way
from GitHub's own pages, so confirm this on your own screen before relying on it, and keep commit
messages as plain, short sentences regardless (`05-daily-workflow.md` covers what actually belongs in
one).

**Why did my numbered list not start at the number I typed?** GitHub renumbers an ordered list for you
when it renders it, so it is not a mistake if you type `1.` on every line and it still comes out 1, 2,
3 on screen.

## Quick reference

```
# Heading
**bold**   *italic*   ~~strikethrough~~
- plain list item
1. numbered list item
- [ ] unchecked task     - [x] checked task
> a quote
[link text](https://example.com)
![image alt text](image-url)
`inline code`
```code block```  (three backticks above and below)
| Column | Column |
| ------ | ------ |
| cell   | cell   |
@username         (mentions someone, if they have access)
#12                (links to issue or pull request 12)
Fixes #12          (closes issue 12 automatically when this pull request merges)
```

Preview before you post: click the **Preview** tab, above the box, next to **Write**.

## Sources

- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- https://github.blog/changelog/2025-02-18-github-issues-projects-february-18th-update/
