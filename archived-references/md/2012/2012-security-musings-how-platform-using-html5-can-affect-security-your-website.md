---
type: Article
title: How a Platform Using HTML5 Can Affect the Security of Your Website
description: "Caching application JavaScript in HTML5 localStorage turns any reflected XSS on the caching origin into a persistent, self-reloading compromise. The article documents a real case: the Apture widget cached 272KB of code and eval'd it, and a reflected XSS on cdn.apture.com let an attacker poison that cache. The payload then executed on every third-party site embedding Apture."
resource: "https://web.archive.org/web/20170903113359/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
tags: [article, webseclist-reference, en, security-musings, xss, javascript, cache, supply-chain, case-study, dom, novel-technique, owasp-a03-2021, owasp-a06-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-10T15:58:44+00:00"
status: deprecated
stale_after: 2027-08-10
sources:
  - id: original
    resource: "https://web.archive.org/web/20170903113359/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
    title: How a Platform Using HTML5 Can Affect the Security of Your Website
    author: Joey Tyson
    last_modified: 2012-02-01
  - id: canonical
    resource: "https://web.archive.org/web/20170611133815/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
  - id: capture
    resource: "https://web.archive.org/web/20170903113359/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
also_at: []
authors:
  - Joey Tyson
canonical_url: "https://web.archive.org/web/20170611133815/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
cited_by:
  - "2012.md:11"
commit: ""
content_sha256: 47cc4e69f21a77a689d9d13f6d6b75f6051925122ffae7d1fa76ed8b5d1c0767
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://web.archive.org/web/20170903113359/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
published: 2012-02-01
publisher: Security Musings
publisher_english: ""
raw_sha256: 5f85266fd57dba63788a5ff5c07501748808b942300644256d03927d2736d3af
retrieved_from: "https://web.archive.org/web/20170611133815/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website"
retrieved_kind: live
retrieved_utc: "2026-08-10T15:58:44+00:00"
slug: 2012-security-musings-how-platform-using-html5-can-affect-security-your-website
snapshot: 20170903113359
title_english: ""
translation_file: ""
translation_of: ""
---

# How a Platform Using HTML5 Can Affect the Security of Your Website

**How a Platform Using HTML5 Can Affect the Security of Your Website** - Joey Tyson, Security Musings.

- Published: 2012-02-01
- Original: <https://web.archive.org/web/20170903113359/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website>
- Current location: <https://web.archive.org/web/20170611133815/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website>
- Preserved from: https://web.archive.org/web/20170611133815/http://securitymusings.com/article/3159/how-a-platform-using-html5-can-affect-the-security-of-your-website (live) on 2026-08-10
- Capture timestamp: 20170903113359
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

### tl;dr Abstract

*To improve performance, particularly for mobile users, many websites have started caching app logic on client devices via HTML5 local storage. Unfortunately, this can make common injection vulnerabilities even more dangerous, as malicious code can invisibly persist in the cache. Real-world examples of this problem have now been discovered in third-party “widgets” embedded across many websites, creating security risks for the companies using such services – even if their sites are otherwise protected against attacks. Striking a balance between security and performance can be difficult, but certain precautions may help prevent an attacker from exploiting local storage caches.*

### Background

Throughout the history of web development, people have found ways to use and abuse various technologies beyond their intended purposes. Before CSS gained widespread support, many developers created complex layouts with HTML tables. Now that browsers provide far more presentation-layer tools, one can recreate complex images using only CSS. Such tricks can at times be very helpful in overcoming the limits of a browser-based environment, but they can also inadvertently create security issues.

One feature commonly classified as part of HTML5 is local storage, a method for saving content on a visitor’s device that offers more space and flexibility than previous options (such as cookies). While intended as a client-side analogue to database storage, local storage has increasingly served another purpose: code caching. If a web app routinely requires large blocks of JavaScript, it can avoid downloading those chunks every time a visitor returns to the app by saving a copy of them in local storage. This can provide a significant performance boost, particularly on mobile devices, where bandwidth and typical caches can be much more limited.

### Local Storage Attacks

However, this approach opens new possibilities for attacking the app. If the local storage can be compromised, an attacker could inject malicious code that persists in the client-side cache. This payload would then be executed by the web app each time a user opened the site – even if they’d previously closed the browser. In fact, eradicating such code can be quite difficult, and the victim website might not even be able to detect an ongoing attack. Artur Janc, a security engineer at Google, outlined these issues in [a talk last December](https://web.archive.org/web/20170611133815/http://events.ccc.de/congress/2011/Fahrplan/events/4811.en.html) ([video](https://web.archive.org/web/20170611133815/http://www.youtube.com/watch?v=ppFcSP2HWdE)) detailing many of the dangerous ramifications they present, but as Janc notes, such an attack was also previously described by [a paper from researchers at Berkeley](https://web.archive.org/web/20170611133815/http://www.cs.berkeley.edu/~dawnsong/papers/2010%20emperors%20new%20api.pdf) (PDF) in May 2010.

Given the restrictions on access to a site’s local storage, modifying code saved there would nearly always require another vulnerability in the app as an initial attack vector. However, just one entry point for injecting code in a page would be enough to change the cache, and such problems tend to be quite common across the web. Many of these vulnerabilities (described as cross-site scripting, or XSS) are “reflected”, in that they only change a particular request for content, but using local storage automatically makes them capable of launching persistent attacks. Essentially, caching code in HTML5 local storage actually makes any existing cross-site scripting vulnerabities more dangerous.

And as influential researcher Michal Zalewski [also noted a few months before](https://web.archive.org/web/20170611133815/http://lcamtuf.blogspot.com/2011/10/origin-is-forever.html) Janc’s presentation, “if content from the compromised origin is commonly embedded on third-party pages (think syndicated ‘like’ buttons or advertisements), with some luck, attacker’s JavaScript may become practically invincible”. In this age of mash-ups, data from a variety of sources are often mixed together, creating implicit trust relationships that may have significant effects on the security of an app. When a developer includes third-party JavaScript on his or her site, that code has the same capabilities as any other script on the page. Of course, modifying a static file on a remote server is generally not possible, even if cross-site scripting issues are present. But what if a third-party script from a site with XSS problems also stored code in local storage?

### Vulnerabilities in the Wild

As it turns out, this is no longer a hypothetical situation. Apture was a start-up that provided pop-up boxes for exploring content related to highlighted terms in a page. The service garnered praise from various tech media outlets, and the company was bought out by Google a few months ago. Just over a week ago, Google shut down the embedded search functionality, which was still in use by several sites after the acquisition. Apture is one example of a third-party “widget” service that used local storage code caching – and a page on the same domain as those scripts had a reflected XSS vulnerability which could be used to inject malicious code in the cache. This code would then be executed in the context of the site using Apture, meaning the problem with Apture’s service affected the security of many sites across the web.

And while Apture’s widgets are now offline, another service still operating on high-profile sites was recently found to have a similar issue (though in this case, scripts were not executed from the original site’s origin). This problem has been reported and is currently being addressed by the service’s engineers.

### Reducing Risk

Ultimately, there isn’t a simple way of avoiding this type of vulnerability while still getting the performance gains of client-side code caching. Another new HTML feature, application cache, is actually geared towards precisely this use case and would be harder to compromise, but it can create UI warnings in some browsers, such as Firefox. (Such warnings are a good practice, but may be unwanted for third-party widgets.) Ideally, any data in local storage should be treated as untrusted, even if it’s just content instead of code. But if local storage is used for scripts, it should be accessed from a domain that only serves static files. This will help reduce the likelihood of an XSS vulnerability that would have direct access to local storage, though the overall structure of an app should be taken into account to prevent indirect access as well. Newer browsers also support features such as sandboxed inline frames and Content Security Policy that could help limit the impact of embedded widgets if they became compromised.

I think it’s important to note that many smart people, including those behind Apture, have used local storage for caching app logic – even Google and Bing use a similar technique on their mobile sites – and that in theory, this method should not make a website less secure. And for many web developers, it may not be immediately obvious why local storage data should not be trusted. This is another case where a clever trick that serves its primary goal very well has unintended consequences when considered in a broader context. It’s also an example of possibly making trade-offs which balance usability with risk. Understanding these conflicts and connections is part of what information security is all about – and what we do at [Gemini](https://web.archive.org/web/20170611133815/http://geminisecurity.com/) every day. As browser features continue to expand and sites continue to integrate services from other domains, it’s likely we’ll see many more examples of security issues evolving in complexity – and organizations will need to adapt to such changes while still reducing risk.

*Special thanks to [@0x6D6172696F](https://web.archive.org/web/20170611133815/http://twitter.com/0x6D6172696F), [@lcamtuf](https://web.archive.org/web/20170611133815/http://twitter.com/lcamtuf), [@theKos](https://web.archive.org/web/20170611133815/http://twitter.com/thekos), and [@kkotowicz](https://web.archive.org/web/20170611133815/http://twitter.com/kkotowicz) for their help with this research!*

### Technical Details

For a site to use Apture widgets, the owner included a bit of JavaScript on their pages:

```
<script id="aptureScript">
(function (){var a=document.createElement("script");a.defer="true";
a.src="http://www.apture.com/js/apture.js?siteToken=XXXXXXX";
document.getElementsByTagName("head")[0].appendChild(a);})();
</script>
```

This dynamically loaded an external script hosted on apture.com with a site token specified. The external script included various parameters, such as title, logo, and search URLs that are associated with the account identified by the token. This code then loaded another script based on the user’s browser which actually began setting up the framework for Apture to integrate with the site’s content.

For browsers that support it, HTML5 cross-document messaging then came into play. The Apture script inserted an inline frame into the page that loaded a file from cdn.apture.com. A callback function allowed this iframe to pass messages back to the original window context where the script is running (the non-Apture site). This iframe then loaded the actual app logic and passed the code back to the original site via the cross-document messaging interface.

At this point, you’re probably wondering why Apture didn’t simply load the app logic as another script in the original page; in fact, that’s precisely what Apture did if the browser didn’t support newer HTML5 features. But Apture’s iframe setup allowed them to take advantage of another HTML5 innovation that made their service load much faster. Web storage functionality provides the localStorage object, a place to save key/value data on the client which allows for more space and flexibility than cookies. This storage is persistent across browser sessions, but is specific to each domain and access to it is restricted by a same-origin policy.

Apture used a localStorage object for cdn.apture.com not only to save data, such as an ID for tracking users, but to actually cache their app logic code. If the cdn.apture.com iframe detected that this cache already existed, it would simply load the code from localStorage rather than issue another HTTP request for the 272KB worth of JavaScript – saving time and bandwidth. Apture introduced this functionality in January 2011.

But how does one load code from localStorage? For Apture, with this line in the cross-domain callback function:

```
window.execScript ? window.execScript(f) : window.eval(f);
```

Seeing code such as this should immediately raise red flags in the mind of any web developer. Those familiar with browser security may have heard the adage that “eval is evil”, and it certainly applies here. The eval function (or the analogous execScript function also seen above) treats its input as valid JavaScript and simply executes it in the current window’s global context. If an attacker can send malicious code to the function, that code will also be executed – a class of vulnerabilities known as cross-site scripting (XSS).

In Apture’s case, though, the code came from the cdn.apture.com storage, so one might assume it can be trusted – in theory, only pages from cdn.apture.com can modify the localStorage cache. But once again, the power of cross-site scripting demonstrates that many seemingly trustworthy data sources are still potential avenues of attack. The presence of any XSS on a cdn.apture.com page, including reflected XSS, would allow an attacker to execute code in that domain’s context and thus modify the localStorage object.

As it turns out, Apture did have an exploitable XSS vulnerability. The cdn.apture.com domain actually mirrored www.apture.com, including a topic page that loaded a topic title from the URL path and a YouTube video ID from a GET parameter. Both of these values were included in the page without being escaped to prevent XSS. This example URL includes a script that appends “alert(document.cookie)” to the app logic in localStorage:

```
http://cdn.apture.com/search/xss?yt=%22%3E%3Cscript%3Eif%28
window.x%21%3D1%29%7BlocalStorage%5B%27app-49971756%27%5D
%3DlocalStorage%5B%27app-49971756%27%5D%2b%22alert%28
document.cookie%29%3B%22%7Dwindow.x%3D1%3C%2fscript%3E
```

The window.x logic ensures that the code only executes once, since the parameter appears in the topic page multiple times. In an actual attack, more code would likely be needed, as the specific localStorage key includes a version number that could change depending on the user. This does not stop the attack, however, as the correct version can be loaded by the script before making changes to localStorage.

Once this vulnerability is used to insert attack code into localStorage (e.g. if the above URL were loaded in an invisible iframe on an attacker’s site), visiting any site that had Apture’s widgets would cause the attack code to be loaded from the Apture iframe and executed in the context of the non-Apture site. And since this is essentially an example of DOM-based XSS (the code is loaded dynamically on the client side), requests sent to those sites’ servers would not include any XSS fingerprints, such as <script> in a GET or POST parameter. In summary, the localStorage code caching turned one reflected XSS vulnerability on Apture’s site into persistent, client-side XSS across all domains using their service.
