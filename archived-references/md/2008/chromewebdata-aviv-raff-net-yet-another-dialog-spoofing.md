---
type: Article
title: Aviv Raff On .NET - Yet another Dialog Spoofing
description: Firefox 2.0.0.11 renders the WWW-Authenticate Basic realm value in its authentication dialog and stops at the last double quote, but does not sanitise single quotes or spaces. A crafted realm therefore makes the prompt appear to come from a trusted site. Delivery vectors include a script-redirected popup and an img tag in webmail, RSS or forum posts.
resource: "https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx"
tags: [article, webseclist-reference, aviv-raffon-net, phishing, url-spoofing, http, filter-bypass, auth-bypass, owasp-a01-2021, owasp-a04-2021, owasp-a05-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-10T15:02:48+00:00"
status: stable
stale_after: 2027-08-10
sources:
  - id: original
    resource: "https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx"
    title: Aviv Raff On .NET - Yet another Dialog Spoofing
    author: Aviv Raff
  - id: capture
    resource: "https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx"
also_at: []
authors:
  - Aviv Raff
canonical_url: ""
cited_by:
  - "2008.md:57"
commit: ""
content_sha256: c10c8a8cffe9f45bda839b31cfd4c187b7f93129424e3335e92e8ac6ccd0bc99
depth: full
depth_reason: default
kind: article
language: ""
licence: unknown
original_url: "https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx"
published: ""
publisher: aviv.raffon.net
publisher_english: ""
raw_sha256: 536ca2ff5b3def9ce5f0a3bead1626ffdc6543cb29a10c90b0f8e6fde985b025
retrieved_from: "https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx"
retrieved_kind: live
retrieved_utc: "2026-08-10T15:02:48+00:00"
slug: chromewebdata-aviv-raff-net-yet-another-dialog-spoofing
snapshot: 20080106144155
title_english: ""
translation_file: ""
translation_of: ""
---

# Aviv Raff On .NET - Yet another Dialog Spoofing

**Aviv Raff On .NET - Yet another Dialog Spoofing** - Aviv Raff, aviv.raffon.net.

- Published: date not stated
- Original: <https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx>
- Preserved from: https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx (live) on 2026-08-10
- Capture timestamp: 20080106144155
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Aviv Raff On .NET - Yet another Dialog Spoofing - Firefox Basic Authentication

The Wayback Machine - https://web.archive.org/web/20080106144155/http://aviv.raffon.net:80/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx

|    |
|

|    |   |
|

|

Wednesday, 02 January 2008

 |  |
|

|   |

|

[Yet another Dialog Spoofing - Firefox Basic Authentication](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx)

 |  |
|

**Summary**

Mozilla Firefox allows spoofing the information presented in the basic authentication dialog box. This can allow an attacker to conduct phishing attacks, by tricking the user to believe that the authentication dialog box is from a trusted website.

****

**Affected versions**

Mozilla Firefox v2.0.0.11.
Prior versions and other Mozilla products may also be affected.

**Technical details**

Mozilla Firefox displays an authentication dialog, whenever the visited web server returns 401 status code, and the "WWW-Authenticate" header. In order to specify [basic authentication](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/ct.ashx?id=d7ac10b1-2fe9-43f3-a445-48b6ea890747&url=http%3a%2f%2fwww.faqs.org%2frfcs%2frfc2617.html), the "WWW-Authenticate" header should have the value [Basic realm="XXX"] (without the brackets). The Realm value, which in this case is XXX, will be displayed in the authentication dialog window.

While Firefox does not display the characters in the "WWW-Authenticate" header Realm value after the last double-quotes ("), it fails to sanitize single-quotes (') and spaces. This makes it possible for an attacker to create a specially crafted Realm value which will look as if the authentication dialog came from a trusted web site.

[![image](https://web.archive.org/web/20080106144155im_/http://aviv.raffon.net/content/binary/WindowsLiveWriter/91bd20013c07_14012/image_thumb.png)](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/ct.ashx?id=d7ac10b1-2fe9-43f3-a445-48b6ea890747&url=http%3a%2f%2faviv.raffon.net%2fcontent%2fbinary%2fWindowsLiveWriter%2f91bd20013c07_14012%2fimage_2.png)

There are at-least two possible attack vectors:

- An attacker creates a web page with a link to a trusted website (e.g. Bank, PayPal, Webmail, etc.). When the victim clicks on the link, the trusted web page will be opened in a new window, and a script will be executed to redirect the new opened window to the attacker's web server, which will then return the specially crafted basic authentication response.
- An attacker embeds an image (pointing to the attacker's web server, which will return the specially crafted basic authentication response) to:

- A mail which will be sent to a webmail user.
- RSS feed which will be consumed by a web RSS reader.
- A forum/blog/social network page.

A video which demonstrates the first attack vector can be found [on YouTube](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/ct.ashx?id=d7ac10b1-2fe9-43f3-a445-48b6ea890747&url=http%3a%2f%2fwww.youtube.com%2fwatch%3fv%3dNaCPw1s3GFw). A better quality video can be download [from here](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/ct.ashx?id=d7ac10b1-2fe9-43f3-a445-48b6ea890747&url=http%3a%2f%2fwww.raffon.net%2fvideos%2fffauth.wmv).

A video of a real live attack on a forum, which used basic authentication but without exploiting the vulnerability, can be found on [Zull's weblog](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/ct.ashx?id=d7ac10b1-2fe9-43f3-a445-48b6ea890747&url=http%3a%2f%2fwww.hacking.org.il%2f642) (Hebrew).

**Suggestion / Workaround**

Until Mozilla fixes this vulnerability, I recommend not to provide username and password to web sites which show this dialog.

[UPDATE:] Due to some questions, I've put a [list of frequently asked questions](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/ct.ashx?id=d7ac10b1-2fe9-43f3-a445-48b6ea890747&url=http%3a%2f%2faviv.raffon.net%2f2008%2f01%2f05%2fFirefoxDialogSpoofingFAQ.aspx).

 |  |
|

 Wednesday, 02 January 2008 22:15:57 UTC |  | [Security](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/CategoryView,category,Security.aspx)[![#](https://web.archive.org/web/20080106144155im_/http://aviv.raffon.net/images/itemLink.gif)](https://web.archive.org/web/20080106144155/http://aviv.raffon.net/2008/01/02/YetAnotherDialogSpoofingFirefoxBasicAuthentication.aspx)

 |  |

  |   |   |

 |  |

  |   |
|    |

  |

|   |
