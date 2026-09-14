---
type: Article
title: TweetDeck Taken Down in Wake of XSS Attacks
description: "TweetDeck rendered tweet content as live markup, so a script tag inside a tweet executed in every reader's client. The published payload used the client's own retweet control to repost itself, producing a self-spreading worm that also allowed account takeover, and Twitter pulled the service to patch it."
resource: "https://web.archive.org/web/20160403035045/http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
tags: [article, webseclist-reference, en-US, threatpost-english-global-threatpost-com, xss, sanitizer-bypass, javascript, dom, browser-extension, case-study, owasp-a03-2021, owasp-a05-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T11:25:45+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://web.archive.org/web/20160403035045/http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
    title: TweetDeck Taken Down in Wake of XSS Attacks
    author: Michael Mimoso
    last_modified: 2014-06-11
  - id: canonical
    resource: "http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
  - id: capture
    resource: "https://web.archive.org/web/20141024063136/http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
also_at: []
authors:
  - Michael Mimoso
canonical_url: "http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
cited_by:
  - "2014.md:18"
commit: ""
content_sha256: c6b286b8e3f60d2c7efe4149bd796b4864b9f92033208bb8c125921c1d2e0eb8
depth: full
depth_reason: default
kind: article
language: en-US
licence: unknown
original_url: "https://web.archive.org/web/20160403035045/http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
published: 2014-06-11
publisher: Threatpost - English - Global - threatpost.com
publisher_english: ""
raw_sha256: 08027eac63b3c57efb50366bdb90bde5119c98727053633f1c0e55cca0bd4c34
retrieved_from: "https://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks"
retrieved_kind: stored
retrieved_utc: "2026-08-06T15:39:23+00:00"
slug: threatpost-com-tweetdeck-taken-down-wake-xss-attacks-threatpost
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# TweetDeck Taken Down in Wake of XSS Attacks

**TweetDeck Taken Down in Wake of XSS Attacks** - Michael Mimoso, Threatpost - English - Global - threatpost.com.

- Published: 2014-06-11
- Original: <https://web.archive.org/web/20160403035045/http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks>
- Current location: <http://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks>
- Preserved from: https://threatpost.com/tweetdeck-taken-down-in-wake-of-xss-attacks (stored) on 2026-08-06
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so
it remains readable if the page goes offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

TweetDeck services have been disabled for the time being as Twitter tries to get a handle on a cross-site scripting vulnerability that caused mountains of consternation on the social networking platform this morning.

>

We've temporarily taken TweetDeck services down to assess today's earlier security issue. We'll update when services are back up.

— TweetDeck (@TweetDeck) [June 11, 2014](https://twitter.com/TweetDeck/statuses/476770732987252736)

Initially users were told log out of the real-time Twitter monitoring tool in order for a fix to take effect. But the repairs, however, didn’t take for some who reported seeing a pop-up dialog box indicative of a benign XSS exploit.

Users could be at risk for more serious attacks. Cross-site scripting occurs when attackers are able to inject code into webpages or web-based services that can automatically be executed by a user’s browser. Hackers successfully executing a cross-site scripting attack can remotely inject code client-side, leading to data loss or service interruption.

>

<script class="xss">$('.xss').parents().eq(1).find('a').eq(1).click();$('[data-action=retweet]').click();alert('XSS in Tweetdeck')</script>♥

— Someone actually (@Dani___Alves) [June 11, 2014](https://twitter.com/Dani___Alves/statuses/476765438991679488)

In the case of the TweetDeck exploit, an attacker could take over a user’s account, post or delete tweets or deface the account. Exploit code was tweeted throughout the morning, and automatically retweeted tens of thousands of times.

“This vulnerability very specifically renders a tweet as code in the browser, allowing various cross site scripting (XSS) attacks to be run by simply viewing a tweet,” said Trey Ford, global security strategist at Rapid7. “The current attack we’re seeing is a ‘worm’ that self-replicates by creating malicious tweets. It looks like this primarily affects users of the Tweetdeck plugin for Google Chrome.”

Ford compared it to the Samy Worm that hit MySpace eight years ago, but points out that the TweetDeck worm does not force an account to follow the attacker.

Twitter acquired TweetDeck in 2011 for upwards of $50 million. TweetDeck provides users with a dashboard view of multiple accounts. Tweet timelines, notifications and direct messages appear in customizable streaming columns.

## Recovery notes

Source evidence recovered on 2026-09-14. The earlier source capture (SHA-256 `a12f8179194b4b7fbebddfcad0da4ca7641f10f50350e775c6c6923c5113b525`) is no longer available. This publication uses a separately preserved capture of the same document recorded on 2026-08-06 (SHA-256 `08027eac63b3c57efb50366bdb90bde5119c98727053633f1c0e55cca0bd4c34`). The existing article text is retained. The archive journal ties this replacement source to the same extracted content; differences in the published copy are documented formatting and footer cleanup. The missing earlier capture remains documented in the archive history.
