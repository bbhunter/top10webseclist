---
type: Article
title: New Adobe Flash Zero-Day Used in Pawn Storm Campaign Targeting Foreign Affairs Ministries
description: Vendor report that the Pawn Storm espionage group spear phished foreign affairs ministries with news themed links delivering a then unpatched Adobe Flash exploit, later assigned CVE-2015-7645 and affecting Flash 19.0.0.185 and 19.0.0.207. It lists SHA1 hashes for the exploit and payload files and the vendor detection rule.
resource: "http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/"
tags: [article, webseclist-reference, en-US, blog-trendmicro-com, flash, cve, vendor-advisory, rce, case-study, detection, owasp-a09-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T21:29:34+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/"
    title: New Adobe Flash Zero-Day Used in Pawn Storm Campaign Targeting Foreign Affairs Ministries
    author: Brooks Li, Feike Hacquebord, Peter Pi
  - id: capture
    resource: "https://web.archive.org/web/20151228211219/http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/"
also_at: []
authors:
  - Brooks Li
  - Feike Hacquebord
  - Peter Pi
canonical_url: ""
cited_by:
  - "2015.md:20"
commit: ""
content_sha256: 98ef2bf8455ee988d8a9296546fe689aed106f097cae8e14f9241c390c1a9120
depth: full
depth_reason: default
kind: article
language: en-US
licence: unknown
original_url: "http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/"
published: ""
publisher: blog.trendmicro.com
publisher_english: ""
raw_sha256: fc8a4a22e0975a32dfcd29d56f3731763c0ea8bd3024c06375bb279092fc85bf
retrieved_from: "http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/"
retrieved_kind: stored
retrieved_utc: "2026-08-14T21:29:34+00:00"
slug: blog-trendmicro-com-new-adobe-flash-zero-day-used-pawn-storm-ministries
snapshot: 20151228211219
title_english: ""
translation_file: ""
translation_of: ""
---

# New Adobe Flash Zero-Day Used in Pawn Storm Campaign Targeting Foreign Affairs Ministries

**New Adobe Flash Zero-Day Used in Pawn Storm Campaign Targeting Foreign Affairs Ministries** - Brooks Li, Feike Hacquebord, Peter Pi, blog.trendmicro.com.

- Published: date not stated
- Original: <http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/>
- Preserved from: http://blog.trendmicro.com/trendlabs-security-intelligence/new-adobe-flash-zero-day-used-in-pawn-storm-campaign/ (stored) on 2026-08-14
- Capture timestamp: 20151228211219
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

New Adobe Flash Zero-Day Used in Pawn Storm Campaign Targeting Foreign Affairs Ministries

# New Adobe Flash Zero-Day Used in Pawn Storm Campaign Targeting Foreign Affairs Ministries

-

 Posted on:[October 13, 2015](http://blog.trendmicro.com/trendlabs-security-intelligence/2015/10/) at 11:57 am

-

 Posted in:[Exploits](http://blog.trendmicro.com/trendlabs-security-intelligence/category/exploits/), [Targeted Attacks](http://blog.trendmicro.com/trendlabs-security-intelligence/category/targeted_attacks/), [Vulnerabilities](http://blog.trendmicro.com/trendlabs-security-intelligence/category/vulnerabilities/)

-

 Author:

 [Trend Micro](http://blog.trendmicro.com/trendlabs-security-intelligence/author/trend-micro/)

***Analysis by Brooks Li, Feike Hacquebord, and Peter Pi***

![pawnstorm](http://blog.trendmicro.com/trendlabs-security-intelligence/files/2015/10/pawnstorm-300x140.jpg)Trend Micro researchers have discovered that the attackers behind [Pawn Storm](http://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-pawn-storm-fast-facts) are using a new Adobe Flash zero-day exploit in their latest campaign. Pawn Storm is a long-running cyber-espionage campaign known for its [high-profile targets](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storms-domestic-spying-campaign-revealed-ukraine-and-us-top-global-targets/) and usage of the [first Java zero-day we’ve seen](http://blog.trendmicro.com/trendlabs-security-intelligence/analyzing-the-pawn-storm-java-zero-day-old-techniques-reused/) in the last couple of years.

We coordinated with Adobe in processing this finding. They have since released a security advisory and assigned it with the identifier [CVE-2015-7645](https://helpx.adobe.com/security/products/flash-player/apsa15-05.html). Adobe has since released the bulletin [APSB15-27](https://helpx.adobe.com/security/products/flash-player/apsb15-27.html) to address this vulnerability

In this most recent campaign, Pawn Storm targeted several foreign affairs ministries from around the globe. The targets received spear phishing e-mails that contained links leading to the exploit. The emails and URLs were crafted to appear like they lead to information about current events, with the email subjects containing the following topics:

*“Suicide car bomb targets NATO troop convoy Kabul”*

*“Syrian troops make gains as Putin defends air strikes”*

*“Israel launches airstrikes on targets in Gaza”*

*“Russia warns of response to reported US nuke buildup in Turkey, Europe”*

*“US military reports 75 US-trained rebels return Syria”*

It’s worth noting that the URLs hosting the new Flash zero-day exploit are similar to the URLs seen in [attacks that targeted North Atlantic Treaty Organization (NATO) members and the White House](http://blog.trendmicro.com/trendlabs-security-intelligence/operation-pawn-storm-ramps-up-its-activities-targets-nato-white-house/) in April this year.

Foreign affairs ministries have become a particular focus of interest for Pawn Storm recently. Aside from malware attacks, fake Outlook Web Access (OWA) servers were also set up for various ministries. These are used for simple, but extremely effective, [credential phishing attacks](http://blog.trendmicro.com/trendlabs-security-intelligence/operation-pawn-storm-putting-outlook-web-access-users-at-risk/). One Ministry of Foreign Affairs got its DNS settings for incoming mail compromised. This means that Pawn Storm has been intercepting incoming e-mail to this organization for an extended period of time in 2015.

Based on our analysis, the Flash zero-day affects at least Adobe Flash Player versions 19.0.0.185 and 19.0.0.207.

![](http://blog.trendmicro.com/trendlabs-security-intelligence/files/2015/10/Pawn-Storm-Flash-ZeroDay3.png)
 *Figure 1. Affected Adobe versions*

Defense against threats that involve zero-day exploits require proactive multi-layered solutions. Zero-day vulnerabilities in applications like Adobe Flash have proven to be difficult to manage since they are commonly targeted and at the same time very widely used. [Trend Micro technologies protects users from zero-day exploits ](http://www.trendmicro.com/us/security-intelligence/adobe-flash-zero-day/index.html) by offering protections for all the different layers within an infrastructure.

More specifically, the existing Sandbox with Script Analyzer engine, which is part of [Trend Micro™ Deep Discovery](http://www.trendmicro.com/us/enterprise/security-risk-management/deep-discovery/#network-protection), can be used to detect this threat by its behavior without any engine or pattern updates.

Trend Micro Deep Security and Vulnerability Protection, on the other hand, protect user systems from threats that may leverage this Adobe Flash zero-day with the DPI rule **1007119 – Identified Malicious Adobe Flash SWF File**.

We have notified Adobe about our discovery and are working with them to address this security concern.

You may read about the technical details of this vulnerability in our blog entry, *[Latest Flash Exploit Used in Pawn Storm Circumvents Mitigation Techniques](http://blog.trendmicro.com/trendlabs-security-intelligence/latest-flash-exploit-used-in-pawn-storm-circumvents-mitigation-techniques/)*.

The SHA1 hashes of files related to this threat are:

- 2DF498F32D8BAD89D0D6D30275C19127763D5568 – detected as SWF_OLOLO.A
- 20F5A9C0E1D2AEF36D15CA149FE71AC6B2A9AF1E – detected as TROJ_SEDNIT.D
- A5FCA59A2FAE0A12512336CA1B78F857AFC06445 – detected as TSPY_SEDNIT.D

*Updated on October 13, 2015 9:50 P.M. PDT (UTC-7) to add more details on past Pawn Storm campaigns and details on provided Trend Micro protection.*

*Updated on October 14, 2015 8:34 A.M. PDT (UTC-7) to include the CVE designation of the zero-day vulnerability.*

*Updated on October 14, 2015 5:45 P.M. PDT (UTC-7) to update the Trend Micro protections.*

*Updated on October 15, 2015 2:50 A.M. PDT (UTC-7) to add target patch date announced by Adobe.*

*Updated on October 15, 2015 8:50 P.M. PDT (UTC-7) to change patch date from week of October 19 to as early as October 16, as stated by Adobe.*

*Updated on October 16, 2015 9:50 A.M. PDT (UTC-7) to include links to the patch and to a related blog entry.*

*Updated on October 17, *2015* 7:29 P.M. PDT (UTC-7) to add the SHA1 hashes related to this latest Flash exploit.*
