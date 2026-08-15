---
type: Article
title: OpenSecurityResearch/clipcaptcha
description: Repository page for clipcaptcha, a Python tool built on the sslstrip codebase that impersonates CAPTCHA providers on an intercepted HTTP validation channel. Signatures identify reCAPTCHA, OpenCAPTCHA and Captchator traffic, and the README documents monitor, avalanche, stealth, denial-of-service and random modes plus private-key logging.
resource: "https://web.archive.org/web/20170903113359/https://github.com/OpenSecurityResearch/clipcaptcha"
tags: [article, webseclist-reference, en, github, tooling, python, auth-bypass, https, info-leak, owasp-a01-2021, owasp-a02-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T01:12:52+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://web.archive.org/web/20170903113359/https://github.com/OpenSecurityResearch/clipcaptcha"
    title: OpenSecurityResearch/clipcaptcha
    author: Gursev Singh Kalra
  - id: canonical
    resource: "https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha"
  - id: capture
    resource: "https://web.archive.org/web/20150110195825/https://github.com/OpenSecurityResearch/clipcaptcha"
also_at: []
authors:
  - Gursev Singh Kalra
canonical_url: "https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha"
cited_by:
  - "2012.md:58"
commit: ""
content_sha256: 518c98ea453b2efd73c76675a02f127e959c37dbe426b4d7637c1b6da78778eb
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://web.archive.org/web/20170903113359/https://github.com/OpenSecurityResearch/clipcaptcha"
published: ""
publisher: GitHub
publisher_english: ""
raw_sha256: 2b632562aa316f8c68c7e32e7bae88cb68498613cc38c10ee97ac1b036ed49e5
retrieved_from: "https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha"
retrieved_kind: live
retrieved_utc: "2026-08-09T01:12:52+00:00"
slug: github-opensecurityresearch-clipcaptcha
snapshot: 20150110195825
title_english: ""
translation_file: ""
translation_of: ""
---

# OpenSecurityResearch/clipcaptcha

**OpenSecurityResearch/clipcaptcha** - Gursev Singh Kalra, GitHub.

- Published: date not stated
- Original: <https://web.archive.org/web/20170903113359/https://github.com/OpenSecurityResearch/clipcaptcha>
- Current location: <https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha>
- Preserved from: https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha (live) on 2026-08-09
- Capture timestamp: 20150110195825
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

A Tool for Impersonating CAPTCHA Providers

-  [  2  commits ](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/commits/master)
-  [  1  branch ](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/branches)
-  [  0  releases ](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/releases)
-   [  Fetching contributors ](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/graphs/contributors)
-  [ GPL-3.0 ](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/blob/master/COPYING)

-  [  Python 100.0% ](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/search?l=python)

 Python

 ![](https://web.archive.org/web/20180611034231im_/https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif) Fetching latest commit…

 Cannot retrieve the latest commit at this time.

   [Permalink](https://web.archive.org/web/20180611034231/https://github.com/OpenSecurityResearch/clipcaptcha/tree/e42859349a0662ff8331fbdf87c07402f49288c0)

###  README.md

# clipcaptcha

A Tool for Impersonating CAPTCHA Providers

**Author**: Gursev Singh Kalra ([gursev.kalra@foundstone.com](https://web.archive.org/web/20180611034231/mailto:gursev.kalra@foundstone.com) - McAfee, Foundstone)

**clipcaptcha** is an extensible and signature based CAPTCHA Provider impersonation tool based off Moxie Marlinspike's sslstrip codebase. For additional information please visit: [http://www.foundstone.com](https://web.archive.org/web/20180611034231/http://www.foundstone.com/) and [http://blog.opensecurityresearch.com](https://web.archive.org/web/20180611034231/http://blog.opensecurityresearch.com/)

It requires Python 2.5 or newer, along with the 'twisted' python module.

**Running clipcaptcha**:

```
Run 'python clipcaptcha.py -h' for help.

The four steps to getting this working on Linux are:

1. Enable forwarding mode on your machine
	echo "1" > /proc/sys/net/ipv4/ip_forward

2. Setup iptables to redirect HTTP traffic to clipcaptcha.
	iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port <listeningPort>

3. Run arpspoof to redirect the traffic to your machine.
	arpspoof -i <interface> -t <targetIP> <gatewayIP>

4. Run clipcaptcha in one of its mode of operation.
	clipcaptcha.py <mode> -p <listeningPort>

	clipcaptcha can be run in one of the following five operational modes and selecting
	more than one operation mode is an error:
	a. Monitor Mode: Signature based CAPTCHA provider detection is performed
	   and all CAPTCHA validation requests are logged to a local file. The CAPTCHA
	   validation requests and corresponding responses are allowed to complete without
	   any modifications.
	b. Avalanche Mode: Success response is returned on the matching CAPTCHA provider
	   for all validation requests. It is recommended to not run clipcaptcha in this
	   mode as a surge in successful account creation or registrations may be detected.
	c. Stealth Mode: Stealth is the recommended mode for running clipcaptcha. This
	   mode relies on the fact that all CAPTCHA validation API.s need to send user
	   supplied CAPTCHA solution to the CAPTCHA providers for validation.
	   clipcaptcha banks on this behavior to operate stealthily and return Success
	   status only for the requests that contain a secret string. In its current
	   implementation, clipcaptcha parses the entire CAPTCHA validation request
	   (initial line, headers and body) and returns success if the secret string is
	   found or allows the request to complete without any modifications.
	d. DoS Mode: Failure response is returned for all CAPTCHA validation requests.
	   This leads to a Denial of Service condition on the target web application
	   for all forms that require CAPTCHA validation.
	e. Random Mode: Random Success and Failure responses are returned as per the
	   matching CAPTCHA provider for all validation requests and exits only
	   as a teaser mode.

Once clipcaptcha instance starts running, all CAPTCHA validation requests will be
administered by clipcaptcha.

```

**Signature based CAPTCHA provider detection**:

All CAPTCHA providers are basically HTTP based custom web services. These services accept CAPTCHA validation requests in a particular format and respond with finite set of responses that allow the clients to make Boolean choices to allow or disallow the request. clipcaptcha takes advantage of this finite and predictable request and response data set to implement signature based request detection and response system. For additional details please refer clipcaptcha whitepaper. The default configuration contains signatures for reCAPTCHA, opencaptcha and captchator.

```
Example runs:
clipcaptcha.py -m -p 7777 	# Run clipcaptcha in monitor mode listening on port 7777.

clipcaptcha.py -a -p 8888 	# Run clipcaptcha in avalanche mode and approve all CAPTCHAs
				# for which signatures are available)

clipcaptcha.py -s clipcaptcha 	# Run clipcaptcha in stealth mode and approve all CAPTCHA
				# requests which contain the secret string "clipcaptcha"

```
