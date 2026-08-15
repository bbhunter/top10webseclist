---
type: Article
title: Chrome and Safari users open to stealth HTML5 AppCache attack
description: "Chrome and Safari let any site create an HTML5 Application Cache without prompting, and unlike ordinary cache it can hold a site's root resource. On a hostile Wi-Fi an attacker frames http://mail.google.com/mail/ and caches a fake Gmail login for it, so credentials are stolen later on a trusted network. Pointing the manifest at an existing file keeps the poisoned entry alive."
resource: "http://blog.andlabs.org/2010/06/chrome-and-safari-users-open-to-stealth.html"
tags: [article, webseclist-reference, en, blog-andlabs-org, cache-poisoning, cache, https, tls, iframe, auth-bypass, info-leak, owasp-a01-2021, owasp-a02-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-10T15:04:01+00:00"
status: stable
stale_after: 2027-08-10
sources:
  - id: original
    resource: "http://blog.andlabs.org/2010/06/chrome-and-safari-users-open-to-stealth.html"
    title: Chrome and Safari users open to stealth HTML5 AppCache attack
    author: lava
also_at: []
authors:
  - lava
canonical_url: ""
cited_by:
  - "2010.md:34"
commit: ""
content_sha256: 46fd3fdf7591b619f84e070ce50618564eb7ae5bbc49f7e967d016b9a1860bb0
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "http://blog.andlabs.org/2010/06/chrome-and-safari-users-open-to-stealth.html"
published: ""
publisher: blog.andlabs.org
publisher_english: ""
raw_sha256: 70b4ce831e90d00f8d20033a0783692cc2e5ea30b0b2b2d1da6a8c8fe8de1bf4
retrieved_from: "http://blog.andlabs.org/2010/06/chrome-and-safari-users-open-to-stealth.html"
retrieved_kind: live
retrieved_utc: "2026-08-10T15:04:01+00:00"
slug: blog-andlabs-org-chrome-safari-users-open-stealth-html5-appcache-attack
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Chrome and Safari users open to stealth HTML5 AppCache attack

**Chrome and Safari users open to stealth HTML5 AppCache attack** - lava, blog.andlabs.org.

- Published: date not stated
- Original: <http://blog.andlabs.org/2010/06/chrome-and-safari-users-open-to-stealth.html>
- Preserved from: http://blog.andlabs.org/2010/06/chrome-and-safari-users-open-to-stealth.html (live) on 2026-08-10
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Google Chrome, Safari, Firefox and Opera(Beta) have implemented the [HTML5 Offline Application Cache](http://www.w3.org/TR/html5/offline.html#appcache) feature. Using this feature a website can have greater control over the caching process to enable Offline access of websites.

When a website is trying to create an Offline Application Cache, Firefox and Opera ask for user permission and only after the user permitting, the site is able to create this cache. With Google Chrome and Safari this step is skipped, any website can create an Application Cache without the user even knowing about it.

The thing with caches is that they can be [poisoned very easily](http://www.networkworld.com/news/2010/020310-black-hat-wi-fi-attackers.html) the moment you connect to an unsecured network, like open Wi-Fi. By poisoning a cached JavaScript file of Facebook or Twitter an attacker can eventually take control of your account. But with normal cache, HTTP content can be easily poisoned, but it is difficult to poison a page that is only served over HTTPS. So none of Gmail’s files can be poisoned, they are all over HTTPS.

Now enter HTML5 Application Cache. Unlike a traditional cache, with Application Cache any file can be cached. For example, the root file ‘/’ of a site can be cached. Let’s say an application cache is created for ‘/’ of www.facebook.com. Then every time the user types in www.facebook.com in their browser this cached page would be fetched. If this was done with normal cache then when the user requests this page the browser would send a request to the server for this resource and only if the server responds with a 304 Not Modified response, would the cache be served. But for '/’ all sites would respond back with a 200 OK with the index page’s content and that is what would be loaded and not the cache

The point is that with Application Cache, root files can be cached, this cannot be done with a normal cache. An attacker could then create a malicious cache for the index page of every HTTP site as soon as the victim connects to an unsecured WiFi. For example for Facebook, if the index page is controlled by the attacker then he can capture the username and password of the victim. Facebook being a HTTP site (post authentication) can anyway be compromised by poisoning the normal cache. But Gmail?

Almost all users open Gmail by typing in gmail.com in the address bar and this means its http://gmail.com (remember SSLstrip??). The server responds to this with a redirect to http://mail.google.com/mail/. And when requested for http://mail.google.com/mail/ the server responds with https://www.google.com/accounts/ServiceLogin?service=mail&blahblah... There are two HTTP requests before the server redirects the user to an HTTPS page. Either of those can be cached using Application Cache, http://gmail.com/ or http://mail.google.com/mail/.

This is how the entire attack works:

Step1: The victim connects to an unsecured network controlled by the attacker.

Step2: The victim browses to any random website, even opening the browser would do as it would send a request for the home page.

Step3: The attacker responds to this request with a page which contains an hidden iframe pointing to http://mail.google.com/mail/ .

Step4: The victim’s browser sends a request for http://mail.google.com/mail/.

Step5: The attacker responds to this with his own copy of the Gmail login page that would look exactly like the actual login page but would include a backdoor to steal the victim’s credentials when entered. This page also includes the manifest attribute in the HTML element so that the page is cached.

Step6: Victim goes back to secured network (home/office) and types in gmail.com, gets redirected by Google server to http://mail.google.com/mail/

Step7: The browser would load the fake login page.

Step8: User enters his Gmail credentials in to it, the credentials are sent over to the attacker.

By poisoning or creating a malicious Application Cache, the victim’s credentials to all HTTPS-only websites can be stolen by an attacker.

I have made a [POC](http://www.andlabs.org/tools/imposter/imposter_poc.zip) for this attack using [Imposter](http://www.andlabs.org/tools.html#imposter). The POC comes with a config file loaded with the payloads for [Facebook](http://www.andlabs.org/hacks/fb.html) and [Gmail](http://www.andlabs.org/hacks/gmail.html). The cached pages would load fake login pages from www.andlabs.org through an iframe. Once the victim enters his username and password these are stored locally in the victim’s browser in the LocalStorage of www.andlabs.org and the credentials are passed on to the parent frame using HTML5 PostMessage API. The parent frame logs the user in using these credentials. The entered credentials can be viewed by visiting, [http://www.andlabs.org/hacks/viewcreds.html](http://www.andlabs.org/hacks/viewcreds.html). The credentials are not sent to the AnD Labs server so it’s safe to try out the POC.

There is a video of the entire attack using the POC [here](http://www.youtube.com/watch?v=00sKMMyXJsI). POC can be downloaded [here](http://www.andlabs.org/tools/imposter/imposter_poc.zip).

One point of interest is the Manifest file. Everytime a cached file is requested for, the browser would request the server for the Manifest file and if the server responds with a 404 then the cache would be removed. Picking an existing file on the server as the Manifest file would solve this issue as the server would return a 200. This would not result in a update of the cache because the server would not include “text/cache-manifest” in the Content-Type header. Even without this the cache would be served the first time but would be removed after that, using this technique can keep the cached file alive till it is deleted by the user.

Coming back to Chrome and Safari, when I first realized that they were not prompting for user permission I thought it was a serious oversight. I even contacted both the security teams, however they didn’t consider this to be a security issue. But on closer look their stance made sense, it is because they treat Application Cache the same way as normal cache. When you delete cache in these browsers all Application Cache is also deleted. But in Firefox they are handled separately. Deleting normal cache does not delete Application Cache, it has to be deleted explicitly. It is difficult to say which approach is better but the idea of user permission prompt is more reassuring to me. Till then browsing in private/incognito mode should keep user’s safe.

Update:
Chris Evans pointed out on FD that root resources can been cached even by using the normal cache mechanism, so using Application Cache for that reason alone might not gives an edge to the attacker.
However, using Application Cache does have a major advantage over normal cache.
When a root resource is cached using normal cache, it is removed the moment the user hits refresh on that page, but Application Cache stays. This can give an attacker continued access to the victim's browser until the user explicitly clears the cache. In Firefox this has to be done explicitly for Offline Website data.
