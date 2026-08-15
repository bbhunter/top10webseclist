---
type: Article
title: How to Create a GIFAR
resource: "http://riosec.com/how-to-create-a-gifar"
tags: [article, webseclist-reference, en, riosec-com]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T10:26:15+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "http://riosec.com/how-to-create-a-gifar"
    title: How to Create a GIFAR
    author: Christopher
  - id: capture
    resource: "https://web.archive.org/web/20081225132058/http://riosec.com/how-to-create-a-gifar"
also_at: []
authors:
  - Christopher
canonical_url: ""
cited_by:
  - "2008.md:5"
commit: ""
content_sha256: 54e2f7b6ddf70a9de938961332fe0ccd1dde0a53319e8012e763efe4e4cd330c
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "http://riosec.com/how-to-create-a-gifar"
published: ""
publisher: riosec.com
publisher_english: ""
raw_sha256: acccdbaa413e2f6349f6534ea1e0aed6b558753f1c7f8970fb747beb76c1d1c0
retrieved_from: "http://riosec.com/how-to-create-a-gifar"
retrieved_kind: stored
retrieved_utc: "2026-08-09T10:26:15+00:00"
slug: chromewebdata-how-create-gifar
snapshot: 20081225132058
title_english: ""
translation_file: ""
translation_of: ""
---

# How to Create a GIFAR

**How to Create a GIFAR** - Christopher, riosec.com.

- Published: date not stated
- Original: <http://riosec.com/how-to-create-a-gifar>
- Preserved from: http://riosec.com/how-to-create-a-gifar (stored) on 2026-08-09
- Capture timestamp: 20081225132058
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

How to Create a GIFAR | RioSec

 How to Create a GIFAR

Search

 Search this site:

Interesting Reading

- [Traffic for Revoked TLSv1 Certificate](http://taosecurity.blogspot.com/2008/12/traffic-for-revoked-tlsv1-certificate.html)
- [Perfect MITM Attacks With No-Check SSL Certs](http://rss.slashdot.org/~r/slashdot/eqWf/~3/iMN2-r5jzY8/article.pl)
- [Physical Security Lessons for Digital Security](http://taosecurity.blogspot.com/2008/12/physical-security-lessons-for-digital.html)
- [Structuring for Strategic Cyber Defense: State of the Nation and What We Can Do](http://www.cigital.com/justiceleague/2008/12/22/structuring-for-strategic-cyber-defense-state-of-the-nation-and-what-we-can-do/)
- [Bypass Network Blocks with Remote Desktop [Tip Testers]](http://feeds.gawker.com:80/~r/lifehacker/full/~3/VPAp6sTanxg/bypass-network-blocks-with-remote-desktop)

[more](http://riosec.com/aggregator/sources/6)

SANS ISC

- [Infocon: green](http://isc.sans.org/diary.php?rss)
- [Merry Christmas, and beware of digital hitchhikers!, (Thu, Dec 25th)](http://isc.sans.org/diary.php?storyid=5554&rss)
- [Farewell to CastleCops, (Wed, Dec 24th)](http://isc.sans.org/diary.php?storyid=5551&rss)

[more](http://riosec.com/aggregator/sources/1)

Linux Security

- [PandaLabs' 2009 Predictions: Malware Will Increase In 2009](http://www.linuxsecurity.com/content/view/146347?rdf)
- [5 Known Linux Anti-virus Software for Paranoid Users](http://www.linuxsecurity.com/content/view/146346?rdf)
- [Nipper - The Network Infrastructure Parser](http://www.linuxsecurity.com/content/view/146052?rdf)
- [5 Best Linux/BSD Firewall Tools](http://www.linuxsecurity.com/content/view/145952?rdf)
- [Firefox Issues Eight Patches for Web Browser](http://www.linuxsecurity.com/content/view/145951?rdf)

[more](http://riosec.com/aggregator/sources/5)

SecurityFocus

- [Oliver Day: Time to Exclude Bad ISPs](http://www.securityfocus.com/columnists/487?ref=rss)
- [Infocus: Responding to a Brute Force SSH Attack](http://www.securityfocus.com/infocus/1903?ref=rss)
- [Chris Wysopal: Standing on Other's Shoulders](http://www.securityfocus.com/columnists/486?ref=rss)
- [Mark Rasch: Just EnCase It's Not a Search](http://www.securityfocus.com/columnists/485?ref=rss)
- [Oliver Day: Microsoft's Stance on Piracy Affects Us All](http://www.securityfocus.com/columnists/484?ref=rss)

[more](http://riosec.com/aggregator/sources/2)

Syndicate

[![Syndicate content](http://riosec.com/themes/sky/images/feed.png)](http://riosec.com/node/feed)

# How to Create a GIFAR

Posted 2008-08-12 17:05 by Christopher

At BlackHat, security researchers Billy Rios and Nathan McFeters presented "The Internet is Broken" which contained information on GIFARs, a term meaning GIF image files combined with Java ARchives (JAR). These files could be uploaded to sites that allow image uploading (such as many site's member photos), to run code in the context of that site - getting around the "same origin policy" that browsers impose. This works because GIF images (along with many other file types) store their header in the beginning of the file, and ZIP archives (which is what JAR files are made of) store their data at the tail.

The folowing video demonstrates this technique.
