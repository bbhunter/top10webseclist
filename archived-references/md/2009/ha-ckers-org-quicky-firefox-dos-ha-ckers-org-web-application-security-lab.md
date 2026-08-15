---
type: Article
title: Quicky Firefox DoS ha.ckers.org web application security lab
description: "A four-line script hangs Firefox indefinitely: a loop to 65536 that appends one character at a time and calls document.write on the whole growing string each pass. The author expected the slow-script prompt and instead had to kill the process after ten minutes. The cost is quadratic rather than linear, as the comment thread works out."
resource: "http://ha.ckers.org/blog/20090727/quicky-firefox-dos/"
tags: [article, webseclist-reference, ha-ckers-org, dos, javascript, algorithmic-complexity, dom, owasp-a04-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T05:08:14+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "http://ha.ckers.org/blog/20090727/quicky-firefox-dos/"
    title: Quicky Firefox DoS ha.ckers.org web application security lab
  - id: capture
    resource: "https://web.archive.org/web/20090731121001/http://ha.ckers.org/blog/20090727/quicky-firefox-dos/"
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2009.md:25"
commit: ""
content_sha256: 0630658a86f5752ca38278b0abf8dd3eeef485e93049b45cb7bbf29d36f42da4
depth: full
depth_reason: default
kind: article
language: ""
licence: unknown
original_url: "http://ha.ckers.org/blog/20090727/quicky-firefox-dos/"
published: ""
publisher: ha.ckers.org
publisher_english: ""
raw_sha256: 69e42fd9f79a698e986ac85b9168f4f8e47227a5320aa0f41fcabfa40f0b6af3
retrieved_from: "http://ha.ckers.org/blog/20090727/quicky-firefox-dos/"
retrieved_kind: stored
retrieved_utc: "2026-08-09T05:08:14+00:00"
slug: ha-ckers-org-quicky-firefox-dos-ha-ckers-org-web-application-security-lab
snapshot: 20090731121001
title_english: ""
translation_file: ""
translation_of: ""
---

# Quicky Firefox DoS ha.ckers.org web application security lab

**Quicky Firefox DoS ha.ckers.org web application security lab** - Author not stated, ha.ckers.org.

- Published: date not stated
- Original: <http://ha.ckers.org/blog/20090727/quicky-firefox-dos/>
- Preserved from: http://ha.ckers.org/blog/20090727/quicky-firefox-dos/ (stored) on 2026-08-09
- Capture timestamp: 20090731121001
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Quicky Firefox DoS ha.ckers.org web application security lab

[![](http://ha.ckers.org/images/nto_top.jpg)](http://ha.ckers.org/blog/20071014/web-application-scanning-depth-statistics/)
 Paid Advertising
 [![web application security lab](http://ha.ckers.org/images/84844372/rsnake/hackers.jpg)](http://ha.ckers.org/)

## [Quicky Firefox DoS](http://ha.ckers.org/blog/20090727/quicky-firefox-dos/)

Well, it turns out I am speaking at Blackhat after all - plus I have an OWASP preso to do tomorrow. That makes five presos in 6 days. Shoot me now. Anyway, I was playing around with Firefox today and accidentally found a super tiny DoS for Firefox that reminded me of my childhood. Remember that math puzzle where you put one penny on one square and then two on the next and four on the next and so on? Clearly that would amount to more money than you could realistically have when you really think through it, but kids have a hard time wrapping their heads around it. This is sort of similar, except it’s not geometric, it’s linear, which was surprising that it caused Firefox so much pain. I had just assumed the JS engine in Firefox would have said that it’s running too tight of a loop and throw the “running too slow” prompt at worst - or just finish at best since it doesn’t look all that complicated:

> var a;
 for(i=0;i<65536;i++){
 document.write(a+=String.fromCharCode(i));
 }

I let this run for 10 minutes on a decent sized test machine and it never finished - I had to kill the process. Yeah, I know there are a million ways to DoS browsers, this one was just surprising because I honestly didn’t think it could. Anyway, if I don’t post before then, see you in Vegas!
