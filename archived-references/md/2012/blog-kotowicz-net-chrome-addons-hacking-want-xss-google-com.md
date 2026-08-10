---
type: Article
title: "Chrome addons hacking: want XSS on google.com?"
resource: "https://web.archive.org/web/20170903113359/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
tags: [article, webseclist-reference, blog-kotowicz-net]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T01:05:11+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://web.archive.org/web/20170903113359/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
    title: "Chrome addons hacking: want XSS on google.com?"
  - id: canonical
    resource: "https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
  - id: capture
    resource: "https://web.archive.org/web/20170903113359/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
also_at: []
authors: []
canonical_url: "https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
cited_by:
  - "2012.md:7"
commit: ""
content_sha256: 1650b24d09d0b1794517f5d90b93e7d554fe8403dab3c68a225471af7c4beeb9
depth: full
depth_reason: default
kind: article
language: ""
licence: unknown
original_url: "https://web.archive.org/web/20170903113359/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
published: ""
publisher: blog.kotowicz.net
publisher_english: ""
raw_sha256: ad9d39fa33929b8b72243050e737a2e3d33eaf41bb09e21b27a8b7a4b18c6c37
retrieved_from: "https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html"
retrieved_kind: live
retrieved_utc: "2026-08-09T01:05:11+00:00"
slug: blog-kotowicz-net-chrome-addons-hacking-want-xss-google-com
snapshot: 20170903113359
title_english: ""
translation_file: ""
translation_of: ""
---

# Chrome addons hacking: want XSS on google.com?

**Chrome addons hacking: want XSS on google.com?** - Author not stated, blog.kotowicz.net.

- Published: date not stated
- Original: <https://web.archive.org/web/20170903113359/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html>
- Current location: <https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html>
- Preserved from: https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2012/02/chrome-addons-hacking-want-xss-on.html (live) on 2026-08-09
- Capture timestamp: 20170903113359
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

For a few days now I'm checking various Chrome extensions code looking for vulnerabilities (see also [the first post of the series](https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2012/02/intro-to-chrome-addons-hacking.html)). There are many. Most of them due to lazy programming (ignoring even the [Google docs](https://web.archive.org/web/20171003023224/http://code.google.com/chrome/extensions/content_scripts.html#security-considerations) on the subject), some are more subtle, coming from poor design decisions.

 As for the risk impact though, there are **catastrophic** vulnerabilities. This is just a sample of what code is committed to [Chrome Web Store](https://web.archive.org/web/20171003023224/https://chrome.google.com/webstore/) and can be downloaded as a Google Chrome extension.

##  How would you like an XSS on google.com?

 Chrome extensions can alter the contents of a webpage you're navigating (if they have the permission for the URL). In web security, what is the worst thing you might do when altering HTML document on-the-fly? Of course, [XSS](https://web.archive.org/web/20171003023224/http://en.wikipedia.org/wiki/Cross-site_scripting). Even if the page itself is totally safe from XSS, an addon might introduce it (it's similar to just entering javascript:code()in address bar) and the page cannot possibly defend from it ([more or less](https://web.archive.org/web/20171003023224/http://blog.kotowicz.net/2011/10/sad-state-of-dom-security-or-how-we-all.html)).

 Google documentation about Chrome extensions [warns about this](https://web.archive.org/web/20171003023224/http://code.google.com/chrome/extensions/content_scripts.html#security-considerations) exact threat. But, as it turns out, seeing is believing, so there you go. Let me tell you about some minor extension (196 users as of now, which is the only reason why I'm 0daying now) that allowed me to XSS Google.
 

##  Meet Linkify

 [Linkify Code Review URLs for Google Reader](https://web.archive.org/web/20171003023224/https://chrome.google.com/webstore/detail/lddlkekpgalmadkfkhfnckdgdmolknig) is just what it says on the cover:

>  *If you follow Chromium Code Reviews inside Google Reader, you do want the ability to click on a link. This extension is there for that. And just that.*

 It upgrades link-like texts for a certain domain in Google Reader site to <a>nchors. How does it do it?

```
// manifest.json
{
"update_url":"http://clients2.google.com/service/update2/crx",
   "name": "Linkify Code Review URLs for Google Reader™",
   "version": "1.0.0",
   "description": "Does what it says",
   "content_scripts": [ {
      "all_frames": true,
      "js": [ "ba-linkify.min.js", "jquery-1.6.2.min.js", "content.js" ],
      "matches": [ "https://www.google.com/reader/*" ],
      "run_at": "document_start"
   } ]
}

```

 It attaches 3 JS files from extension code into any document from https://www.google.com/reader . The main logic in those files is:

```
window.addEventListener('DOMNodeInserted', handleEvent, false);

function browseAndLinkify(node) {
  if (!node) {
    return;
  }
  if (node.children && node.children.length > 0) {
    $.each(node.children, function(index, element) {
      browseAndLinkify(element);
    });
  } else {
      if (node.innerHTML.indexOf('http://codereview.chromium.org/') > -1) {
        node.innerHTML = linkify(node.innerHTML);
     }
  }
}

function handleEvent(event) {
  browseAndLinkify(event.target);
}

```

 So every node in the document, when its HTML contains 'http://codereview.chromium.org/', gets linkified (linkifying is converting http://anything to <a href="http://anything">anything</a>)and reinserted it into the DOM using innerHTML. Which smells like XSS.

##  Exploitation

 Manipulating any node in Google Reader to start with http://codereview.chromium.org and having the XSS payload bypassing linkify engine is very simple. In Google Reader search box just start searching for:

 http://codereview.chromium.org/"onmouseover="if(!window.a){alert(document.domain);window.a=1}//" ddd

 and mouseover. Or, even better, visit this handy URL (of course, with the extension installed):

 [https://www.google.com/reader/view/#search/http%3A%2F%2Fcodereview.chromium.org%2F%22onmouseover%3D%22if(!window.a)%7Balert(document.domain)%3Bwindow.a%3D1%7D%2F%2F%22%20ddd/](https://web.archive.org/web/20171003023224/https://www.google.com/reader/view/#search/http%3A%2F%2Fcodereview.chromium.org%2F%22onmouseover%3D%22if(!window.a)%7Balert(document.domain)%3Bwindow.a%3D1%7D%2F%2F%22%20ddd/)

| [![](https://web.archive.org/web/20171003023224im_/http://3.bp.blogspot.com/--vAvbaYevXc/T0Px2xgOF4I/AAAAAAAAE6U/tegnHkPmhlU/s320/linkify.png)](https://web.archive.org/web/20171003023224/http://3.bp.blogspot.com/--vAvbaYevXc/T0Px2xgOF4I/AAAAAAAAE6U/tegnHkPmhlU/s1600/linkify.png) |  |
| Voila! XSS on www.google.com |  |

##  Lessons to take

 **Google Extension authors** - don't use innerHTML with anything outside your control. Really!
 **Users** - pay attention to what you're installing.
