## AIML 1.0 Compliance

This document describes the current state of PyAIML's compliance
to the AIML 1.0.1 standard.  The full AIML reference manual can be
found online at http://alicebot.org/TR/2001/WD-aiml.

The following tags are currently supported:

	<bot name="name"> (see notes)
	<condition>
	<date>
	<formal>
	<gender>
	<get>
	<id>
	<input>
	<learn>
	<li>
	<lowercase>
	<person>
	<person2>
	<random>
	<sentence>
	<set>
	<size>
	<sr>
	<srai>
	<star>
	<system>
	<that>
	<thatstar>
	<think>
	<topic>
	<topicstar>
	<uppercase>
	<version>

Support for the following tags should be implemented in the next version:

	None

The following tags are not supported:

	<gossip> (see notes)
	<if> / <else> (see notes)
	<javascript> (see notes)
	<secure> (see notes)

------------------------------------------------------------------

NOTES ON SPECIFIC TAGS:

<bot name="name">
To set the bot's name, use Kernel.setBotName("NewName").  Note that the
name *MUST* be a single word!  Use Kernel.getBotName() to query the bot's
name in your code.

<gossip>
The AIML 1.0.1 specification lets engine authors implement the the behavior
of the <gossip> tag however they wish.  I haven't yet decided what I'd like
to do with it, so right now it doesn't do anything at all.

<if> / <else>
These elements appear to have been dropped between AIML 1.0 and AIML 1.0.1.
They may someday be added as a part of an AIML 1.0 backwards-compatibility
mode, but in the meantime, use <condition> instead.

<javascript>
Support for the JavaScript tag is not anticipated; one of the design
goals of PyAIML is to remain 100% pure standard Python.  So until
somebody writes a JavaScript interpreter in Python, PyAIML won't
support the <javascript> tag.  On the bright side, it is possible
to simulate the effects of the <javascript> tag (i.e. dynamically-
generated tag contents) using the <system mode="sync"> tag.  This
solution has the added advantage of allowing *any* programming
language to be used, not just JavaScript.
UPDATE: The python-spidermonkey project provides a bridge between Python
and the open-source SpiderMonkey JavaScript library.  I am currently
investigating the possibility of adding support for the <javascript>
tag ON A PURELY OPTIONAL BASIS.

<secure>
Some AIML implementations support a non-standard <secure> tag, intended to
wrap parts of a template which should only be processed if the user is
"secure", or trusted.  After implementing support for this tag, I realized
that it wasn't doing anything that you can't do with the <condition> tag.
Therefore, I've decided to drop support for the <secure> tag.  You can
easily duplicate its effects; simply replace this:
	<secure error="you're not allowed">you are allowed</secure>
with this:
	<condition name="secure">
		<li value="yes">you are allowed</li>
		<li>you are not allowed</li>
	</condition>
Then, use the Kernel.setPredicate() call to set the "secure" predicate to
"yes" for any session that you wish to be secure.

## AIML 2.0 Compliance

- [ ] Zero+ wildcards: new wildcards that match 0 or more words.
- [ ] Highest priority matching: select certain words to have top matching priority.
- [ ] Migrating from attributes to tags: more dynamic control of attribute values.
- [ ] AIML Sets: match inputs with sets of words and phrases.
- [ ] AIML Maps: map set elements to members of other sets.
- [ ] Loops: Iterations.
- [ ] Local variables: variables with scope limited to one category.
- [ ] Sraix: access external web services and other Pandorabots.
- [ ] Denormalization: the (approximate) inverse of normalization.
- [ ] Pandorabots extensions:
	- [x] date: formatted date and time.
	- [ ] request: access previous input request history.
	- [ ] response: access previous bot response history.
	- [ ] unbound predicates: check if a predicate has been set or not
	- [x] learn: learn new AIML categories.
	- [ ] learnf: learn new AIML categories and save in a file.
	- [ ] explode: split words and phrases into individual character.
- [ ] OOB (Out of Band) Tags: AIML extension for mobile device control.


## AIML 2.1 Compliance 

- [ ] Rich Media Extensions
