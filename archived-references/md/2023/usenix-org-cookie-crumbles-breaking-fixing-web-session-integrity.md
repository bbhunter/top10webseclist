---
type: Article
title: "Cookie Crumbles: Breaking and Fixing Web Session Integrity"
resource: "https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina"
tags: [article, webseclist-reference, en, usenix-org]
generated:
  by: webseclist-refs/1
  at: "2026-08-19T16:22:36+00:00"
status: stable
stale_after: 2027-08-19
sources:
  - id: original
    resource: "https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina"
    title: "Cookie Crumbles: Breaking and Fixing Web Session Integrity"
    author: Marco Squarcina, Pedro Adão, Lorenzo Veronese, Matteo Maffei
also_at:
  - "https://www.usenix.org/system/files/usenixsecurity23-squarcina.pdf"
  - "https://www.usenix.org/system/files/usenixsecurity23-appendix-squarcina.pdf"
  - "https://www.usenix.org/system/files/sec23_slides_squarcina-marco.pdf"
authors:
  - Marco Squarcina
  - Pedro Adão
  - Lorenzo Veronese
  - Matteo Maffei
canonical_url: ""
cited_by:
  - "2023.md:13"
commit: ""
content_sha256: 68d257dc26780e55835c508a6a873b72fb42e08c3f61dc6948ae1e700571d9f4
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina"
published: ""
publisher: usenix.org
publisher_english: ""
raw_sha256: 16dbdbebba2d794b992fbe243902345112c96ca2926076df20834869e769d17e
retrieved_from: "https://www.usenix.org/system/files/usenixsecurity23-squarcina.pdf"
retrieved_kind: live
retrieved_utc: "2026-08-19T16:22:36+00:00"
slug: usenix-org-cookie-crumbles-breaking-fixing-web-session-integrity
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Cookie Crumbles: Breaking and Fixing Web Session Integrity

**Cookie Crumbles: Breaking and Fixing Web Session Integrity** - Marco Squarcina, Pedro Adão, Lorenzo Veronese, Matteo Maffei, usenix.org.

- Published: date not stated
- Original: <https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina>
- Also published at: <https://www.usenix.org/system/files/usenixsecurity23-squarcina.pdf>
- Also published at: <https://www.usenix.org/system/files/usenixsecurity23-appendix-squarcina.pdf>
- Also published at: <https://www.usenix.org/system/files/sec23_slides_squarcina-marco.pdf>
- Preserved from: https://www.usenix.org/system/files/usenixsecurity23-squarcina.pdf (live) on 2026-08-19
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Cookie Crumbles: Breaking and Fixing
                Web Session Integrity
  Marco Squarcina, TU Wien; Pedro Adão, Instituto Superior Técnico, ULisboa,
Instituto de Telecomunicações; Lorenzo Veronese and Matteo Maffei, TU Wien
     https://www.usenix.org/conference/usenixsecurity23/presentation/squarcina




       This paper is included in the Proceedings of the
             32nd USENIX Security Symposium.
                   August 9–11, 2023 • Anaheim, CA, USA
                                978-1-939133-37-3




                                        Open access to the Proceedings of the
                                         32nd USENIX Security Symposium
                                              is sponsored by USENIX.
                 Cookie Crumbles: Breaking and Fixing Web Session Integrity

    Marco Squarcina                         Pedro Adão                           Lorenzo Veronese             Matteo Maffei
       TU Wien                 Instituto Superior Técnico, ULisboa                   TU Wien                    TU Wien
                                  Instituto de Telecomunicações



                          Abstract                                  a session cookie (e.g., via cross-site scripting) and use it to
                                                                    obtain unauthorized access to a website [72]. Session fixation
Cookies have a long history of vulnerabilities targeting
                                                                    attacks involve compromising cookie integrity to force an
their confidentiality and integrity. To address these issues,
                                                                    attacker-controlled cookie in the victim’s browser, and then
new mechanisms have been proposed and implemented in
                                                                    impersonate the victim on the target website [61]. Cross-site
browsers and server-side applications. Notably, improvements
                                                                    request forgery (CSRF) attacks, instead, are a typical session
to the Secure attribute and cookie prefixes aim to strengthen
                                                                    integrity violation problem where the attacker issues cross-
cookie integrity against network and same-site attackers,
                                                                    site requests from the victim’s browser to execute unwanted
whereas SameSite cookies have been touted as the solution
                                                                    actions on a website in which the victim is authenticated [41].
to CSRF. On the server, token-based protections are consid-
ered an effective defense for CSRF in the synchronizer token           In response to these attacks, new mechanisms have been
pattern variant. In this paper, we question the effectiveness of    proposed on both the client and the server side. On the client
these protections and study the real-world security implica-        side, major browsers now support the updated cookie standard
tions of cookie integrity issues, showing how security mecha-       RFC6265bis [50] which includes extended security features
nisms previously considered robust can be bypassed, exposing        compared to the original RFC from 2011 [39]. A notable
Web applications to session integrity attacks such as session       example is the SameSite attribute, which has been touted
fixation and cross-origin request forgery (CORF). These flaws       as a robust solution against CSRF attacks [58, 59]. Other
are not only implementation-specific bugs but are also caused       changes focused on strengthening cookie integrity against
by compositionality issues of security mechanisms or vul-           same-site and network attackers, with improvements to the
nerabilities in the standard. Our research contributed to 12        Secure flag and the introduction of __Host- and __Secure-
CVEs, 27 vulnerability disclosures, and updates to the cookie       cookie name prefixes [69]. On the server side, traditional pro-
standard. It comprises (i) a thorough cross-browser evaluation      tections against CSRF attacks include the usage of a secret
of cookie integrity issues, that results in new attacks originat-   token shared between browsers and servers [41]. This ap-
ing from implementation or specification inconsistencies, and       proach has been widely adopted by popular Web frameworks
(ii) a security analysis of the top 13 Web frameworks, expos-       and considered an effective defense in the synchronizer token
ing session integrity vulnerabilities in 9 of them. We discuss      pattern variant [62, 71].
our responsible disclosure and propose practical mitigations.          In this paper, we question the effectiveness of existing pro-
                                                                    tections and study the real-world security implications of
                                                                    cookie integrity issues. In particular, we focus on network
1    Introduction                                                   and same-site attackers [44], a class of attackers increasingly
                                                                    becoming a significant threat to Web application security [78].
HTTP cookies are the oldest and most widely used mecha-             We show how security mechanisms considered to be robust
nism for state sharing between Web clients and servers. They        against these threat models can be bypassed, exposing Web ap-
are a cornerstone of Web sessions and play a crucial role in        plications to session integrity attacks such as session fixation
the authentication and authorization of users. Despite their        and cross-origin request forgery (CORF). We suggest that
prominence in Web applications, cookies have a long history         these vulnerabilities are due to compositionality challenges
of vulnerabilities and several known pitfalls [41,44,64,76,89].     between Web standards, browsers, and servers, and we pro-
   Entire classes of attacks revolve around compromising ei-        pose a set of countermeasures to reconcile these issues. Over-
ther the confidentiality or the integrity of cookies [48]. For      all, our research contributed to 12 CVEs, 27 vulnerability dis-
instance, session hijacking attacks aim to leak the value of        closures, and updates to the RFC of the cookie standard [50].



USENIX Association                                                                    32nd USENIX Security Symposium          5539
We identified novel attack vectors that bypass modern cookie         2.1    Origins and Sites
protections and precisely characterize a class of attacks called
CORF token fixation that highlights weaknesses in current            The same-origin policy (SOP) [40] defines the traditional
CSRF protections. We performed a systematic security analy-          Web security boundary between websites. The SOP is based
sis of the top 13 Web frameworks, exposing session integrity         on the notion of origin, defined as a tuple of scheme, host,
vulnerabilities in 9 of them. We showed that these vulnerabil-       and port. For instance, the origin of https://example.com:443
ities are not only implementation-specific bugs but are caused       is <https, example.com, 443>. The SOP prevents an origin
by compositionality issues of security mechanisms or flaws in        from reading or modifying the contents of a different origin.
the standard. We also discussed the response of developers to        However, some components of the Web platform have a differ-
our responsible disclosure and proposed mitigation strategies        ent scope. Cookies, for instance, are scoped to the registrable
to improve the security of the Web ecosystem.                        domain of the website that set them. A registrable domain is a
                                                                     domain name with one label on the left side of an effective top-
Contributions. Our contributions are summarized as follows:          level domain, as defined by the Public Suffix List (PSL) [66].
                                                                     Hosts sharing the same registrable domain are considered
    • We extend the work of Squarcina et al. [78] to propose a
                                                                     to be same-site, e.g., example.com, auth.example.com, and
      taxonomy of threat models that describes network and
                                                                     api.staging.example.com all belong to the same site exam-
      same-site attackers in terms of their capabilities and
                                                                     ple.com. Same-site hosts are also called sibling domains.
      goals (Sec. 3).
                                                                        In recent years, the definition of same-site evolved to in-
    • We perform a thorough cross-browser evaluation of              clude the URL scheme [84]. Hence, sibling domains with
      known cookie integrity attacks and introduce new at-           different schemes are considered same-site, but not schemeful
      tacks classified along 4 different categories: serialization   same-site. To avoid ambiguities, we maintain both terminolo-
      collisions due to nameless cookies, server-side parsing        gies and refer to same-site only when the scheme is irrelevant.
      vulnerabilities, cookie jar desynchronization issues, and
      broken composition of (compliant) parsers. We present          2.2    Cookies
      our methodology and discuss the result of a measurement
      study on nameless and prefixed cookies (Sec. 4).               Cookies are the main state management mechanism of the
                                                                     Web, allowing servers to maintain a stateful session over the
    • In Sec. 5, we precisely define the class of CORF to-           stateless HTTP protocol [50]. Servers can set a cookie in the
      ken fixation attacks which captures known and novel            browser through the Set-Cookie header. This cookie is then
      bypasses of real-world CSRF protections, including the         automatically attached by the browser to all following HTTP
      synchronizer token pattern which is considered robust          requests to the server via the Cookie header. Additionally,
      against same-site and network attackers.                       JavaScript code running in Web pages can access and set
                                                                     the value of cookies using the traditional Document.cookie
    • Sec. 6 presents a systematic security analysis of the top
                                                                     property or the new Cookie Store API [68].
      13 Web frameworks, exposing CORF and session fixa-
      tion vulnerabilities in 9 of them. We discuss the response     Attributes. Cookies can be configured with attributes, or
      of developers to our responsible disclosure and propose        flags, which specify additional properties or constraints. The
      a set of practical countermeasures to prevent our attacks.     Path attribute allows to limit the cookie to a set of URL paths,
                                                                     i.e., the browser will include the cookie in HTTP requests if
    • We formally verify the correctness of our proposed             the path of the request URL matches or is a subdirectory of
      mitigation to the synchronizer token pattern using the         the Path attribute. The Domain attribute broadens the scope of
      ProVerif protocol verifier [42] (Sec. 7).                      a cookie. The value of this attribute can be assigned to any of
                                                                     the parent domains of the origin that sets the cookie, up to the
We publish all artifacts developed during this research, includ-     registrable domain. For instance, a server at foo.example.com
ing the browser test suite (Sec. 4.3), the dataset and processing    can set a cookie with Domain=example.com to specify that the
code of our measurement (Sec. 4.4), the ProVerif models and          cookie should be attached to all subdomains of example.com.
scripts (Sec. 7), as well as the reproducible proof-of-concept       If the attribute is omitted, the browser will send the cookie
attacks against Web frameworks (Sec. 6) [77].                        only to the host that set it. HttpOnly prevents the cookie from
                                                                     being accessed by JavaScript, e.g., via the Document.cookie
2    Background                                                      property. The Secure attribute limits the scope of the cookie
                                                                     to secure connections. Browsers must reject the insertion of
In the following, we provide an overview of cookie attributes,       a cookie from a non-secure origin if the cookie jar already
including existing mechanisms for cookie integrity, and CSRF         contains a secure cookie with the same name and scope.
protections. We first revise standard notions such as origins        Same-Site Cookies. The SameSite attribute has been intro-
and sites being instrumental to the rest of the paper.               duced in 2016 as a defense in depth protection against CSRF



5540    32nd USENIX Security Symposium                                                                        USENIX Association
attacks by confining cookies to same-site requests [86]. In par-     Web frameworks [62], and – as shown in Sec. 7 – can offer
ticular, the standard defines three same-site policies: Strict,      robust protection if correctly implemented. The main idea is
cookies are attached to same-site requests only, i.e., no cookie     to send an unguessable parameter t, commonly named CSRF
is attached to cross-site requests; Lax, cookies are attached to     token, with every state-changing request, typically as a hidden
same-site requests and cross-site top-level navigations, e.g.,       input field in a form. By ensuring that t remains secret to the
clicking on a link, using the GET request method; None, cook-        attacker, cross-origin forged requests will be discarded by the
ies are attached to all requests, cross-site included. According     target website, as the token t is missing. Below, we discuss
to the standard, SameSite cookies follow the schemeful same-         the two most popular token-based protection patterns [62, 71].
site definition to determine whether a request is cross-site.        Synchronizer Token Pattern (STP). In STP, the server gen-
This is in contrast to Domain cookies which do not consider          erates CSRF tokens and inserts them in every webpage that
the URL scheme, unless used in combination with the Secure           may lead to a state-changing operation, e.g., as a hidden field
attribute. SameSite cookies also represent one of the most           in a form for transferring funds. This token is then bound
effective protection against XS-Leaks, an emerging class of          to the user’s session and the server validates newly received
attacks that exploits gaps in the same-origin policy (SOP)           tokens by verifying the correctness of this binding. Multiple
to infer information such as PII and the authentication sta-         implementations (see Sec. 6) generate a fixed CSRF secret
tus of a user from a cross-site position [55, 73, 79, 81]. The       s per session, and use it to derive CSRF tokens t(s). Other
SameSite attribute restricts the ability to initiate authenticated   implementations generate a fresh CSRF secret s per request,
requests to same-site attackers, thus preventing traditional         and derive CSRF tokens t(s) similarly to the previous case.
Web attackers from leaking the user’s state on a website.            In this pattern, secrets are always linked to the user session,
Cookie Prefixes. Cookie prefixes, originally introduced in           irrespective of whether it is stateful or stateless. In the former
2015 [85], enable additional security constraints on cookies         case, secrets are stored in the server session, whereas in the
based on their name. The specification defines two prefixes:         latter, client-side storage mechanisms, e.g., cookies, are used
when a cookie name begins with __Secure-, the cookie must            to synchronize the secret between the server and the browser.
be set with the Secure attribute and from a page served over         Double Submit Pattern (DSP). In this pattern, the CSRF
HTTPS; when the name of a cookie starts with __Host-, in             token is a random value stored in a cookie other than the
addition to all restrictions of the __Secure- attribute, the Path    session cookie. The server typically renders the CSRF token
attribute must be explicitly set to /, and it must not contain       in the HTML page as a hidden input field, and the browser
the Domain attribute, locking the scope of the cookie to the         sends it back to the server as part of the authenticated request.
host that created it. These additional constraints guarantee the     The server then verifies the validity of the request by checking
integrity of __Host- cookies against same-site attackers, as         the equivalence between the cookie value and the CSRF token.
such cookies are unaffected by shadowing attacks performed           This makes DSP more suitable for stateless sessions, as it
from a same-site position (see Sec. 4).                              does not require the server to store the CSRF secrets or tokens
                                                                     in the session. Notice that CSRF cookies can be encrypted
2.3    CSRF Protections                                              or signed with a fixed key or secret stored on the server. In
                                                                     this case, the server-side validation should account for an
CSRF attacks are a well-known class of attacks where the             additional decryption or validation step before performing the
adversary executes unauthorized state-changing actions under         comparison. Additionally, servers could store a CSRF secret
the victim’s authenticated session. A CSRF attack is always          in a cookie and use it to derive the CSRF token: whenever the
preceded by a setup phase where the attacker prepares a mali-        CSRF secret or token is not cryptographically bound to the
cious website that silently performs a cross-site request to the     current session identifier, we still refer to this pattern as DSP.
target website to execute the unauthorized action, e.g., via an
automatic form submission or the fetch API.
   Over the years, many types of CSRF defenses have been             3   Threat Model
proposed in the literature, including (i) origin/referrer checks,
(ii) token-based mechanisms to ensure request unguessability,        In this paper, we aim to investigate the security risks that arise
(iii) the SameSite cookie attribute, and (iv) explicit user in-      from the interaction between a website and a victim’s browser
teraction such as CAPTCHAs [41, 62]. All these protections           when a network or a same-site attacker can forge cookies
have some limitations and drawbacks. For instance, Same-             scoped to the target website. As shown in recent works, these
Site cookies are not effective against attacks performed from        two threat models are still relevant today. According to Zheng
a same-site position. To avoid ambiguity, we use the term            et al. [90], only 0.13% of the top 1M websites in 2015 were
Cross-Origin Request Forgery (CORF) in the rest of the paper,        protected from network attackers thanks to full HSTS de-
as it includes the attack scenario of a network or same-site         ployment. The situation improved in 2022, although 90% of
attacker. We focus our analysis on token-based protection            websites remain vulnerable [46]. Large-scale studies on sub-
techniques as they are the most common defense adopted by            domain takeover vulnerabilities demonstrated the impact of



USENIX Association                                                                      32nd USENIX Security Symposium           5541
 Capability      Description                                                                    SS-HOST-S
                                                                                         { https , js , headers }
  headers        Control arbitrary HTTP response headers at wa .
  js             Execute arbitrary JavaScript on a page at wa .
                                                                                     SS-XSS-S           NET, SS-HOST-I
  https          The scheme of wa is https.
                                                                                   { https , js }       { headers , js }
Table 1: Capabilities required to set cookies in the victim’s
                                                                                                SS-XSS-I
browser from a sibling domain of the target (wa ).
                                                                                                 { js }

same-site attackers. In 2016, Liu et al. [63] identified 227 of       Figure 1: Taxonomy of threat models for cookie integrity
the Alexa top-10K sites affected by vulnerable subdomains.            violations.
Borgolte et al. [43] studied deprovisioned cloud instances,
finding 700K vulnerable domains. Squarcina et al. [78] es-
timated 13K potentially vulnerable domains due to deprovi-            SS-XSS-I is an attacker with an XSS vulnerability on a sib-
sioned cloud instances and discovered 887 sites with other            ling domain served over an insecure connection. The only
subdomain takeover vulnerabilities among the top 50K sites            available capability is js .
in the Tranco list. They also discussed the dangers posed             NET maps to a standard network attacker who can fully con-
by corporate networks, roaming services, and dynamic DNS              trol cleartext traffic generated by the victim’s browser. This at-
providers, which put users in a same-site position without            tacker is able to intercept, modify, and inject network traffic of
carrying out attacks.                                                 any sibling domain of the target domain, including the target
   We consider a range of threat models corresponding to              domain itself. These capabilities translate into the headers
different levels of control and visibility that an attacker may       and js , similarly to the SS-HOST-I attacker. Notice that net-
have over the network and sibling domains of the website.             work attackers cannot manipulate cleartext network traffic if
To exclude trivially vulnerable scenarios, we assume that the         the domain enforces a strict HSTS policy that includes the
victim accesses the target website over a correctly-configured        includeSubDomains directive [90].
secure channel. We do not discuss specific attack vectors
                                                                         We also formulate a precise definition of cookie integrity
that can be exploited to acquire a certain position since they
                                                                      violations, taking into account the cookie’s intended recipient.
have been extensively covered in the past [43, 53, 63, 78]. We
                                                                      We assume that the attacker aims to compromise a cookie
focus, instead, on the capabilities of standard threat models
                                                                      c = ⟨n, v⟩ with name n and value v, stored in the victim’s
that are relevant to violations of cookie integrity. To do so, we
                                                                      browser B for the origin o. In a server-side integrity violation,
build on the framework introduced by Squarcina et al. [78].
                                                                      the attacker implants a cookie c′ = ⟨n′ , v′ ⟩ in the victim’s
Table 1 outlines the capabilities that are relevant to set cookies,
                                                                      browser B with the goal of forcing the browser B to send
assuming a target website w, the set of its sibling domains Sw ,
                                                                      c′ to o. The server at o parses the Cookie header obtaining
a website controlled by an attacker wa ∈ Sw , and the victim’s
                                                                      a cookie with name n but tampered value v′ ̸= v. We refer
browser B. Different combinations of these capabilities enable
                                                                      to a client-side integrity violation when the attacker causes
precise characterization of the threat models considered in
                                                                      the JavaScript Document.cookie property on o to return a
this work, as shown in Fig. 1.
                                                                      key=value pair where the key corresponds to n and the value
                                                                      is chosen by the attacker. Additionally, we consider cookie
SS-HOST-S maps to a same-site attacker, also called related-
                                                                      eviction attacks as integrity violations, i.e., attacks that evict
domain attacker, with full control over a sibling domain of the
                                                                      the cookie c from requests to o or remove the cookie from the
target with a valid TLS certificate. This attacker can render
                                                                      key=value pairs returned by the Document.cookie API on o.
arbitrary content over a secure channel, having the full set of
capabilities https , js , and headers .
SS-HOST-I is similar to SS-HOST-S, excluding the ability to           4    Violationg Cookie Integrity
host pages over a secure channel. This threat model captures
the case where an attacker controls a sibling domain of the           In this section, we show how attacker capabilities, and there-
target but cannot obtain a valid TLS certificate, e.g., due to        fore the standard threat models discussed in Sec. 3, map to
the presence of a CAA DNS record defining a strict allow-list         concrete attacks. First, we systematize known cookie integrity
of permitted CAs [78]. The capabilities are js and headers .          pitfalls and evaluate them on the top 3 Web browsers. Then,
SS-XSS-S is a same-site attacker obtaining indirect control           we introduce a range of novel attacks along 4 attack classes
over a sibling domain via a script injection vulnerability (XSS)      enabled by inconsistencies between servers, browsers, and
on a page served via HTTPS. Since the attacker is not in              the cookie specification. We show that these attacks are pos-
control of the response headers returned by the page, the             sible in practice and can be used to break cookie integrity
capabilities are https and js .                                       in unprecedented ways. Finally, we discuss the methodology



5542    32nd USENIX Security Symposium                                                                           USENIX Association
                                          RFC           Browsers               Browser                 Application                 Attacker
                                                                                Victim                 site.tld                 atk.site.tld
  Attack                                  
                                                                                            GET /
  Tossing (creation date, latest first)          Ë          Ë
  Tossing (insecure over secure cookie)          Ë          Ë                    Set-Cookie: sid=good; Path=/

  Eviction (cookie jar overflow)                                   Ë
                                                                                                          GET /
  Eviction (__Host- via secure cookies)                            Ë
  Serialization collision (=a=b→a=b)       ≥04                     Ë                Set-Cookie: sid=evil; Path=/login; Domain=site.tld

  Serialization collision (__Host-)        ≥11   <104       <105   Ë
                                                                                   POST /login/index.php
  Cookie jar desynchronization                   Ë                 Ë              Cookie: sid=evil; sid=good
  Server-side parsing issues                     −          −      −                                            !
  Parser-chaining                                −          −      −
                                                                                         Figure 2: Cookie tossing attack.
Table 2: Evaluation of cookie integrity attacks against the
cookie standard RFC6265bis-11 and browsers: Chrome
(v109), Firefox (v109), and Safari (v16.0). compliant,
                                                                       same-site position. Furthermore, the standard specifies that se-
violation, Ë unaffected, vulnerable, − does not apply.
                                                                       cure cookies have strong integrity against non-secure origins.
                                                                       To summarize, cookie tossing requires the https capability
adopted to discover these issues and report on a measurement           only for cookies with the Secure flag. Otherwise, either the
study performed using the HTTP Archive dataset [37].                   headers or the js capability is needed.


4.1     Weak Integrity
Due to their legacy design, cookies have a long history of in-         4.1.2    Eviction Techniques
tegrity issues, as documented in the cookie specification [50].
A comparison of the top 3 browsers on the integrity pitfalls           Cookies are evicted from the browser’s storage when the stor-
discussed below is included in Table 2 together with the new           age limit is reached. The eviction policy and precise limits are
attacks introduced in this section.                                    not specified by the standard, and are left to browser vendors
                                                                       to decide. In practice, recent versions of Firefox and Chrome
4.1.1      Cookie Tossing                                              limit the size of the cookie jar to 180 cookies per scheme-
                                                                       ful site, while Safari does not enforce any limit. In addition,
Cookies scoped for a target origin o are sorted by standard-           browsers evict cookies in a least-recently-used (LRU) fashion,
compliant browsers by the most-specific matching Path at-              i.e., the oldest cookies are evicted first. This is problematic
tribute, meaning that cookies set with Path=/foo are sent be-          because it allows attackers to control the eviction of cookies
fore cookies with Path=/. When Path attributes are equal,              by overflowing the cookie jar, and then use cookie tossing to
cookies are sorted by creation time, i.e., cookies set first are       replace the evicted cookies with their own. It is worth mention-
sent before cookies that are set later. Although the standard          ing that the HttpOnly flag does not provide integrity against
states that servers should not rely on the order of cookies sent       an attacker with the js capability. Indeed, while HttpOnly
by browsers, most implementations only consider the first              cookies cannot be read via JavaScript, they can be evicted by
occurrence of a cookie name in the Cookie header field [90].           any of the threat models considered in this paper. On the other
Since attributes are not sent along with cookies, duplicated           hand, the Secure flag does provide integrity against attackers
cookies with the same name but different Path attributes are           without the https capability, since modern browsers partition
indistinguishable to the server [50, §5.7.3].                          cookies by scheme.
   Attackers can exploit this behavior to violate cookie
integrity. For example, consider a Web application at
https://site.tld/login/index.php that sets a cookie via the re-
sponse header Set-Cookie: sid=good; Path=/. Assume also
an attacker in control of http://atk.site.tld/. The attacker can       4.2     Novel Attacks
set a domain cookie for site.tld with name sid and value evil.
By setting a more specific path in the new cookie, the attacker        The cookie standard evolved in recent years to provide
can cause the victim’s browser to send the attacker’s con-             stronger integrity guarantees. In particular, the __Host- prefix
trolled cookie first, as in Fig. 2. This specific attack is called     was proposed in 2015 [85] to prevent cookie tossing attacks.
cookie tossing, or shadowing.                                          In the following, we present a range of novel cookie integrity
   As mentioned in Sec. 2, __Host- prefixed cookies are                attacks that exploit issues in the cookie standard, server and
considered to be unaffected by shadowing attacks from a                client implementation problems, and the combination of both.



USENIX Association                                                                          32nd USENIX Security Symposium                    5543
        Browser                 Application                 Attacker     Working Group on the cookie standard [31] and jointly dis-
         Victim                 site.tld                atk.site.tld
                                                                         closed the __Host- cookie bypass to the Chrome [29] and Fire-
                     GET /                                               fox [34] security teams who issued CVE-2022-2860 and CVE-
   Set-Cookie: __Host-sid=good; Secure; Path=/                           2022-40958, respectively.2 Chrome fixed the issue in version
                                                                         104 and Firefox in version 105. Safari is not affected by this
                                   GET /
                                                                         vulnerability because it deviates from the standard since it
         Set-Cookie: =__Host-sid=evil; Path=/login; Domain=site.tld
                                                                         serializes nameless cookies by prefixing the value with =. Our
             POST /login/index.php                                       contributions and extensive discussion with browser maintain-
    Cookie: __Host-sid=evil; __Host-sid=good                             ers [30] led to updates to the cookie standard [50, §5.6, point
                                               !                         22] that now mandates browsers to reject nameless cookies
                                                                         with a value starting with a case-insensitive match for __Host-
  Figure 3: __Host- cookie bypass via nameless cookies.                  or __Secure-.

4.2.1   Nameless Cookies and Serialization Collisions                    4.2.2    Server-Side Parsing Issues
In 2020, a change to the cookie standard1 added support                  The cookie standard [50, §5.5] describes a set of parsing rules
to nameless cookies, i.e., cookies set with empty name and               for the Set-Cookie header that user agents must follow. Un-
non-empty value. This change was motivated by some servers               fortunately, the standard does not clearly specify how servers
setting cookies with empty names, and the cookie standard did            should parse cookies received via the Cookie header. This
not specify how to parse them. As a result, the standard now             discrepancy causes server-side cookie integrity violations
mandates browsers to parse the Set-Cookie: token header                  whenever servers parse two distinct cookies as the same one.
as a nameless cookie with value token. This cookie must be                  Although the problem is not new per se [90], we discov-
serialized as Cookie: token, without any = character.                    ered a new vulnerability that bypasses __Host- cookies in
   We found that this design introduces a novel attack vec-              PHP [35], the server-side language used by 78% of web-
tor that can bypass even the __Host- prefix. Consider, for               sites [83]. Due to the legacy design derived from regis-
instance, a page at site.tld that sets a named cookie sid=good.          ter_globals [18], PHP replaces spaces, dots, and open square
A same-site attacker can set a nameless cookie scoped to                 brackets with the underscore symbol _ in the keys of $_POST
site.tld with value sid=evil. This can be done via either                and $_GET superglobal arrays. The same string transformation
the Document.cookie property or the HTTP response header                 applies to the keys of the $_COOKIE superglobal array. As a
Set-Cookie: =sid=evil; Domain=site.tld, which is a valid                 result, an attacker can fixate a cookie in the victim’s browser
header. According to the standard, the attacker-controlled               via Set-Cookie: ..Host-sid=evil; Domain=site.tld, that
cookie is serialized as Cookie: sid=evil, resulting indis-               is parsed by PHP as Cookie: __Host-sid=evil. This vulner-
tinguishable to the server, or to frontends using the Docu-              ability extends integrity concerns to all cookies that contain
ment.cookie getter, from a cookie named sid.                             the underscore symbol, e.g., non-secure origins can use this
   This attack is particularly dangerous because it can vio-             bug to shadow secure cookies. Similarly, the HTTP server
late the integrity guarantees enforced by __Host- cookies.               component of the ReactPHP library incorrectly parses the
Indeed, any attacker in our taxonomy can shadow a cookie                 Cookie header by url-decoding cookie names [51]. This vul-
__Host-<name>=<value> by forcing in the victim’s browser a               nerability can be exploited to bypass __Host- cookies using
nameless cookie via Set-Cookie: =__Host-<name>=<value>;                  percentage-encoded names, e.g., a cookie set via Set-Cookie:
Domain=<domain>. An example of the attack flow is in Fig. 3.             %5F%5FHost-sid=evil; Domain=site.tld is parsed by React-
   The same attack vector can shadow arbitrary secure cook-              PHP as Cookie: __Host-sid=evil.
ies from an insecure origin. As explained in Sec. 2, browsers               We also discovered a vulnerability in the Werkzeug li-
must reject a cookie set from a non-secure origin if the cookie          brary, the HTTP middleware used by the popular Flask frame-
jar contains a secure cookie matching the name of the new                work [52]. The Cookie header is incorrectly parsed by strip-
cookie scoped to the same site. Since secure cookies are parti-          ping all leading = symbols. To exemplify, a nameless cookie
tioned differently from insecure ones, the https capability is           set via Set-Cookie: ==__Host-sid=evil; Domain=site.tld
typically required to perform an eviction or a cookie tossing            is parsed by Werkzeug as a name-value pair corresponding to
attack against a secure cookie. This attack, however, lowers             (__Host-sid, evil).
the preconditions for the integrity violation of secure cookies,
                                                                            All threat models discussed in Sec. 3 can mount these
requiring only the headers or the js capability.
                                                                         attacks that exploit server-side parsing issues, meaning that
Disclosure. The attacks above are representative of a larger
                                                                            2 The __Host- bypass vulnerability was reported 3 weeks earlier as an
class of serialization issues that we reported to the IETF HTTP
                                                                         independent effort by Axel Chong who is credited on both CVEs. Our issues
  1 RFC6265bis,Accept nameless cookies:            https://github.com/   were merged into the previous vulnerability reports to jointly discuss the
httpwg/http-extensions/commit/0178223                                    mitigation and additional edge cases.




5544    32nd USENIX Security Symposium                                                                                   USENIX Association
 1   / / Assume an empty c o o k i e j a r t h e n s e t 181 c o o k i e s               ment.cookie to read cookies. However, the security impact of
 2   f o r ( l e t i = 1 ; i <=181 ; i ++)                                               this second desynchronization issue is limited since it only
 3           document . c o o k i e = ’ a ’ + i + ’ =_ ’ ;
 4   / / Count t h e number o f c o o k i e s                                            affects insecure origins that are trivially vulnerable to cookie
 5   document . c o o k i e . s p l i t ( " ; " ) . l e n g t h                          integrity attacks.
 6   > 181 / / H i g h e r t h a n t h e l i m i t o f 180 c o o k i e s p e r s i t e
                                                                                         Disclosure. We reported both issues to the Firefox security
Listing 1: Cookie jar overflow desynchronization in Firefox.                             team in June 2022. According to Firefox developers, the root
                                                                                         cause of these problems is the composition of cookies’ access
only the headers or js capabilities are required.                                        control policies with Firefox’s implementation of Site Isola-
Disclosure. The PHP vulnerability was assigned CVE-2022-                                 tion, project Fission [67]. The second issue has been fixed in
31629 and fixed in PHP 7.4.31, 8.0.24, and 8.1.11. ReactPHP                              Firefox 112 and obtained CVE-2023-29547, whereas the first
issued CVE-2022-36032 after our report and fixed the vulner-                             one is still under active investigation as of May 2023.
ability in version 1.7.0. The Werkzeug vulnerability obtained
CVE-2023-23934 and has been patched in version 2.2.3.                                    4.2.4   Parser Chaining Vulnerabilities
                                                                                         The serialization collision previously discussed introduces
4.2.3     Cookie Jar Desynchronization                                                   a new attack vector against chains of cookie parsers. We in-
We identified two vulnerabilities in Firefox that cause a desyn-                         vestigated the presence of this configuration in real-world
chronization between the cookies listed by Document.cookie                               applications by studying the AWS API Gateway, a service
and the actual content of the cookie jar. We experimentally                              that acts as a frontend for other AWS services. The AWS
discovered that a cookie jar overflow operated via JavaScript                            Lambda proxy integration for HTTP APIs enables develop-
sets more cookies than the maximum number of cookies al-                                 ers to bridge an API route with a Lambda function, passing
lowed on a single site. Surprisingly, these cookies can only be                          request payloads to the Lambda function using a JSON mes-
retrieved via the Document.cookie API and are not effectively                            sage exchange format. According to the documentation [75]:
set in the cookie jar, i.e., they are not attached to subsequent                         “Format 2.0 includes a new cookies field. All cookie head-
HTTP requests [32].                                                                      ers in the request are combined with commas and added to
    The issue can be easily reproduced using the JavaScript                              the cookies field. In the response to the client, each cookie
code snippet in Listing 1. This example stores 181 cookies                               becomes a set-cookie header.”
(a1 to a181) in Document.cookie, however, manual inspection                                 From our tests, this proxy introduces an additional parser
of the cookie jar reveals that only 151 cookies are set (a31 to                          that serializes the cookies in the request payload. As a re-
a181). Attempts to clear the cookie jar via the Firefox storage                          sult, a cookie attached to a request, such as Cookie: =__Host-
inspector, setting an expiration date in the past via the Set-                           sid=evil corresponding to a nameless cookie with value
Cookie header, or using the Clear-Site-Data header [82], fail                            =__Host-sid=evil, is serialized by the AWS Lambda proxy as
to remove the first 30 cookies (a1 to a31). This set of cookies                          {"cookies": ["__Host-sid=evil"], ...}, resulting indistin-
survives page reloads and schemeful-same-site navigations.                               guishable from a legitimate cookie named __Host-sid. Notice
It is also preserved in new schemeful-same-site windows                                  that this specific attack is not prevented by recent Chrome and
created via the Window.open method. The only way to remove                               Firefox mitigations against __Host- cookie collisions, since
them is to set a past expiration date via JavaScript, or by                              the cookie value starts with the = symbol.
closing the browser tab.                                                                 Disclosure. We reported the issue to the AWS security team
    The described issue can be exploited to violate client-side                          in October 2022 that deployed a fix in November 2022. The
cookie integrity and requires the js capability, with the op-                            mitigation consists of discarding key-value cookie entries
tional https capability if the target website is on a secure                             starting with the = symbol followed by a case-insensitive
origin. Notice also that this inconsistent state could intro-                            match for __Host- or __Secure-. This approach, combined
duce vulnerabilities in applications trusting cookies read from                          with modern browsers that adhere to the latest draft of the
Document.cookie, providing a novel avenue for attacks. For                               cookie standard [50], effectively protects against the threat
instance, frontends often set custom HTTP headers using the                              described in this section.
values of specific cookies read via the Document.cookie prop-
erty. Notable examples are ASP.NET [65] and Angular [36].                                4.3     Discovering Cookie Integrity Issues
    The second desynchronization issue happens when there is
a secure cookie set by a domain, and a page on a same-site                               The methodology used to discover these attacks consisted of
non-secure origin tries to set another cookie with the same                              three main stages.
name using Document.cookie [33]. We discovered that the                                  Browser Testing. We performed a comprehensive evalu-
insecure cookie is not stored as required by the standard, but                           ation of known cookie integrity attacks across the top-3
it is listed by the Document.cookie property. This inconsis-                             browsers (Chrome, Firefox, and Safari). Inspired by the WPT
tency can create confusion on frontends that rely on Docu-                               project [25], we developed a suite of test cases that simulated



USENIX Association                                                                                         32nd USENIX Security Symposium          5545
various types of attacks and evaluated the behavior of the         Archive dataset [37] and performed all queries against the
browsers. The test cases were designed to cover all possible       database provided by the Web Almanac initiative [46]. We
combinations of secure and insecure origins between the vic-       considered the website popularity rank in the Chrome User
tim and a same-site attacker. We also tested different ways        Experience Report (CrUX) [56], which distinguishes the pop-
to set cookies, i.e., via the Set-Cookie header or using the       ularity of origins by orders of magnitude (top 1K, 10K, 100K,
JavaScript Document.cookie property. The test cases were           etc.). CrUX introduced the rank metric in February 2021 [60],
run on the latest browser versions, and the results were ana-      thus we restricted the measurement to the last 2 years to avoid
lyzed to identify any inconsistencies between the browsers.        any bias due to mixing different ranking metrics. We also
Additionally, we used BrowserStack3 to test all releases from      excluded third-party cookies from our analysis and focused
January 2021 to January 2023 of the three major browsers           instead on first-party cookies to avoid popular CDNs and
against our test suite and identify any changes in the behavior    analytics services from affecting the results.
over time. This phase was crucial to uncover little-known
discrepancies between the browsers. For instance, Safari sorts        Table 3 reports the outcome of our measurement performed
cookies by placing the most recent one first, while Firefox        on the dataset from June 2022. The table shows the number of
and Chrome serialize cookies starting from the oldest one,         origins that use the Secure attribute, the __Host- and __Secure-
as mandated by the specification. We also verified that Sa-        prefix, and nameless cookies. Fig. 4 provides a direct com-
fari does not prevent cookie tossing of secure cookies from        parison between July 2021 and June 2022 of the adoption
non-secure cookies, which is a violation of the standard [50].     of cookies on the top 100K origins. As expected, prominent
Additionally, we experimentally verified that Safari does not      websites are more inclined towards well-established security
enforce limits on the maximum number of cookies stored             features such as the Secure attribute. We found that more than
for a single site. Finally, the test suite enabled the automatic   70% origins in the top 1K range are using secure cookies,
discovery of the cookie jar desynchronization issue in Firefox,    while the percentage decreases to 60% in the top 100K range.
which was previously unknown to the security community.            Interestingly, while the adoption of secure cookies remained
                                                                   overall stable in the last 2 years for the top 1K websites, lower-
Reviewing the Cookie Standard. Whenever a discrepancy              ranked origins are increasingly adopting the Secure attribute.
was found between the browsers, we manually reviewed the           This trend becomes even more evident by focusing on the
cookie standard [50] to determine what was the expected be-        adoption of the __Host- prefix. Despite numbers being still
havior. During this phase, we learned that the standard intro-     low, the popularity of __Host- prefix is growing rapidly in
duced support to nameless cookies in 2020 and we discovered        the top 10K and top 100K ranges. Overall, 77 origins used
the serialization collision issues. We engaged with the IETF       the __Host- prefix in 2021, in contrast to the 133 origins that
HTTP Working Group and browser vendors to address the              used it in 2022, which corresponds to a 72% increase in one
problems as we found them.                                         year. On the other hand, the distribution of nameless cookies
Testing Server-Side Parsers. As a third stage of the anal-         is more stable over time and does not show a clear correlation
ysis, we investigated the presence of inconsistencies in the       with the website rank.
cookie parsers of the server-side languages and core HTTP
handling libraries used by the frameworks discussed in Sec. 6.        Table 4 provides a characterization of __Host- and name-
For each target considered in our analysis, we developed a         less cookies, showing the most common names and values, re-
small reflector program that parses the Cookie header and          spectively, across the top 100K origins. Intuitively, the names
returns pairs of cookie names and values. Then, we wrote a         adopted by __Host- cookies suggest that they are used to
simple fuzzer to generate variations of the Cookie request         store sensitive data such as session identifiers or CSRF to-
header and automatically assessed how the header was parsed        kens. Nameless cookies, instead, are likely to be the result of
by our programs. We acknowledge that this approach does            misconfigurations on the server side, since the most common
not constitute a systematic evaluation of server-side parsing      values match cookie attribute identifiers. A manual analysis
inconsistencies. However, our initial analysis provided strong     of the full collection of nameless cookies did not reveal any
evidence of the pervasiveness of the issue. We leave such          clear intended usage. To the best of our knowledge, our study
comprehensive study as future work.                                is the first to measure the prevalence of nameless cookies
                                                                   in the wild. The results suggest that nameless cookies are a
                                                                   byproduct of misconfigurations and are not actively used by
4.4 Measurement of Cookie Name Prefixes and                        websites. For these reasons, we advocate for the removal of
    Nameless Cookies                                               nameless cookies from the cookie standard and browsers to
                                                                   eradicate this source of confusion and the serialization col-
We present the results of our measurement of the prevalence
                                                                   lision vulnerabilities discussed in Sec. 4.2. Conversely, we
of cookie name prefixes and nameless cookies in the top
                                                                   believe that the increasing adoption of __Host- cookies is a
100K websites. We based our evaluation on the public HTTP
                                                                   positive trend that should be further promoted among Web
  3 https://www.browserstack.com/                                  developers and security practitioners.



5546    32nd USENIX Security Symposium                                                                        USENIX Association
    Rank    Origins         Secure      __Host-    __Secure-    Nameless      __Host- cookie names                                #       Nameless cookie values                                              #
      1K       732      537 (73.4%)     6 (0.8%)     1 (0.1%)    1 (0.1%)
                                                                              __Host-next-auth.csrf-token                       26        HttpOnly                                                           50
     10K      5952     4005 (67.3%)    14 (0.2%)    19 (0.3%)    6 (0.1%)
    100K     58068    35098 (60.4%)   113 (0.2%)   109 (0.2%)   86 (0.1%)     __Host-GAPS                                       23        <empty string>                                                     16
                                                                              __Host-csrf-token                                 13        Secure                                                              6
Table 3: Number of origins from the 2022-06-01 dataset set-                   __Host-PHPSESSID                                  10        =                                                                   5
ting cookies, and the percentage of origins using the Secure                  __Host-SESSION_LEGACY                              5        ACookieAvailableCrossSite                                           4
                                                                              __Host-SESSION                                     5        =0                                                                  3
attribute, cookie prefixes, and nameless cookies.
                                                                              __Host-sess                                        4        secure                                                              1
                                                                              __Host-SWAFS                                       3        *                                                                   1
                                                                              __Host-session                                     3        ˆ(.*)$ $1                                                           1
                                                                              __Host-js_csrf                                     3        =1                                                                  1

                                                                            Table 4: Top-10 __Host- cookie names and nameless cookie
                                                                            values from 2022-06-01.

                                                                                             Browser                        Application                     Attacker
                                                                                              Victim                        site.tld                      atk.site.tld
                                                                                                                                          1 GET /login

                                                                                                                                   Set-Cookie: sess[⊥, s]




                                                                                                                                                                                      pre-session fixation
                                                                                                                                           form( t(s) )


                                                                                                                             GET /foo

                                                                                                   2 Set-Cookie: sess[⊥,token] ; Domain=site.tld

                                                                                                       GET /login
                                                                                                  Cookie: sess[⊥,token]

                                                                                                          form( t ′ (s) )




                                                                                                                                                                       token replay
 Figure 4: Deployment of cookies between 2021 and 2022.
                                                                               user login




                                                                                                         POST /login
                                                                                                       Cookie: sess[⊥, s]
                                                                                                        user, pwd, t ′ (s)
5     CORF Token Fixation
                                                                                                 3 Set-Cookie: sess′ [⊤, s]

We present a class of attacks that we call CORF Token Fix-
ation that undermine implementations of the synchronizer                                            4 POST /action
token pattern in the presence of network or same-site attack-                                      Cookie: sess′ [⊤, s]
                                                                                                              t(s)
ers. The synchronizer token pattern is considered a robust                                                                            !
CSRF protection against the same-site threat model [71] and
is widely used in Web applications [62]. However, as we show
                                                                                            Figure 5: CORF token fixation attack (pre-login).
in Sec. 6, common implementations are vulnerable to CORF
attacks. The term CSRF Token Fixation has been used in the
past to refer to a vulnerability affecting the Devise authenti-             in the first case, typically referred to as stateful, the cookie
cation library [80]. Although this vulnerability is an instance             includes only the session identifier; in the latter, known as
of our attack class, we provide for the first time a precise                stateless, the content of the session is used as the cookie value,
characterization of the attack flow and discuss a more general              possibly after being encoded and signed. The attack flow is
instance of the problem. Moreover, by factorizing the attacks               identical in both scenarios.
into fixation and replay phases, we show how known bypasses                    The attack has the following preconditions: (i) the target
to the double submit pattern can be framed in this class.                   application uses the synchronizer token pattern, storing the
                                                                            CSRF secret in the session; (ii) the application constructs
5.1        Token Fixation Attacks                                           a pre-session for guest users (i.e., not logged-in) and has at
                                                                            least one CSRF token-protected form visible to guests. Al-
Fig. 5 shows an instance of a token fixation attack (pre-                   ternatively, the CSRF token can be derived from information
login) that performs a state-changing request to a token-                   present in the pre-session. In the diagram, t(s) represents the
protected endpoint (/action). User sessions are represented as              token that is attached to forms and derived (e.g., hashed or
sess[loggedin-status, csrf-secret], where sess is the identifier            encoded) from the CSRF secret s; (iii) the CSRF secret is
for a session containing the loggedin-status and the csrf-secret            shared unchanged between the pre-session and the session.
value. Sessions can be stored on the server or the client side:                When these preconditions are satisfied, the attack is per-



USENIX Association                                                                                           32nd USENIX Security Symposium                                           5547
formed as follows: 1 the attacker visits the target application      application at example.com, requires setting domain cookies.
and obtains the value of the pre-session cookie and the CSRF         Token Secret Refresh for STP. A robust mitigation for token
token that is bound to that pre-session; 2 the attacker per-         fixation attacks for websites that implement the synchronizer
forms a pre-session fixation attack [61], setting the victim         token pattern consists in refreshing the value of the CSRF
pre-session cookie to the value previously obtained by the           secret in the user session upon login. This update has the
attacker; 3 by logging into the application, the user has an au-     effect of using different secrets in the pre-session and in the
thenticated session sess′ which shares the CSRF secret s with        authenticated session, so that precondition (iii) of the pre-
the attacker-known pre-session sess; 4 the attacker causes           login attack is no longer satisfied. This leads to the rejection
the victim’s browser to execute a crafted request towards the        of pre-session tokens in authenticated sessions and prevents
/action endpoint, attaching the value of the token t(s) ob-          the attacker from executing step 4 of Fig. 5, since the token
tained in the first step. Given precondition (iii), the secret was   obtained at step 1 is not valid for the new user session.
preserved during the login process, so a valid token for the
                                                                     Mitigating Attacks Against DSP. In 2012, Wilander [87]
pre-session is accepted as a valid token for the authenticated
                                                                     proposed a variation of the double submit pattern named triple
session. This allows the attacker to perform a CORF attack
                                                                     submit cookies to address a specific version of the attack. The
that bypasses the CSRF token protection.
                                                                     mechanism employ random identifiers for both the name and
   Note that the encoding/serialization mechanism used to
                                                                     value of the cookie, attaching only the random value to forms,
derive a token from the secret s may generate different tokens
                                                                     and leveraging HttpOnly cookies to not disclose the random
(t(s) and t ′ (s) in the figure) for different requests, e.g., by
                                                                     name with client-side scripts. The server-side validation of
including an expiration date. In such cases, a server could
                                                                     the submitted token may require storing the random name in
disallow expired tokens or only accept the last token that was
                                                                     the user session (stateful triple submit), or enforcing that the
generated. Still, an attacker could bypass this protection by
                                                                     request contains only a single cookie with a random name,
executing again step 1 before constructing the request 4 to
                                                                     discarding the request otherwise (stateless). The stateful vari-
obtain a valid token. Furthermore, the attack can be performed
                                                                     ant is equivalent to a synchronizer token pattern, where the
even if the victim has an already established authenticated
                                                                     random name acts as the CSRF secret and is stored in the
session with the website. Besides setting a more specific
                                                                     user session. The stateless variant relies on the assumption
path in the injected cookie, as described in Sec. 4.1.1, the
                                                                     that cookies cannot be erased since, otherwise, the attacker
attacker can forcibly logout the victim from the website using
                                                                     can forge a request with a single random-name cookie [64].
a cookie eviction technique (see Sec. 4.1.2) before fixating
                                                                     This assumption is only valid for Safari (see Sec. 4.1.2), thus
the pre-session cookie.
                                                                     the stateless triple submit is not effective in the general case.
Post-Login Variant. The double submit pattern typically              Consequently, the post-login attack can only be mitigated by
stores the CSRF secret in a separate cookie from the session.        (i) using __Host- prefix cookies, which are subject to com-
Hence, overwriting/shadowing this cookie (fixation phase) is         patibility issues, or (ii) switching to the synchronizer token
sufficient to perform the attack, assuming that the attacker         pattern and refreshing the secret upon login.
subsequently crafts a request to the protected endpoint with a
CSRF token that matches the value of the overwritten cookie
(replay phase). Notice that this attack variant does not require     6   Systematic Evaluation of Web Frameworks
fixating the pre-session, thus lowering the set of preconditions
compared to the STP bypass. Additionally, the post-login             We perform a study of Web development frameworks aimed
attack can be commonly performed without prior knowledge             at detecting session integrity vulnerabilities that may derive
of a valid CSRF token. Still, whenever the server performs           from the composition of security libraries, focusing on session
additional validation checks, an attacker can obtain a valid         management and CSRF protection components. In particular,
cookie for the application and its related CSRF token and use        we apply the threat models defined in Sec. 3 and leverage the
them to carry out the attack.                                        techniques described in Sec. 4 to conduct the CORF token
                                                                     fixation attacks presented in Sec. 5. Albeit developers are
                                                                     ultimately responsible for securing their Web applications,
5.2    Mitigations                                                   we believe security abstractions should provide defaults that
Token fixation attacks are enabled by cookie integrity viola-        ensure safe composition. Hence we conducted the study on
tions from network and same-site attackers. Hence, prevent-          the default settings enabled by each framework. Moreover,
ing cookie tossing from sibling domains, i.e., via the __Host-       we discuss relevant opt-in options that are listed in the docu-
cookie prefix, would trivially prevent the attacker from exe-        mentation and assess how they affect security. As part of our
cuting the fixation phase (step 2 ). However, __Host- cookies        work, we responsibly performed a coordinated disclosure of
may introduce compatibility issues on applications that use          all the identified issues.
multiple origins. For instance, sharing the same session at ac-      Selection Criteria. The selection criteria for the analyzed
counts.example.com, where users log in, with the rest of the         Web development frameworks follow the approach adopted



5548    32nd USENIX Security Symposium                                                                         USENIX Association
by Likaj et al. in their comprehensive study [62]. First, we     6.2     Synchronizer Token Pattern Bypasses
considered the top 5 languages used for Web development in
2022 according to [54], i.e., JS, Python, Java, C#, and PHP,     In the following, we present the security analysis of vulnerable
and then selected the most used frameworks from this pool.       real-world implementations of the synchronizer token pattern.
For this purpose, we used the GitHub metrics watch, fork,        All vulnerable frameworks, excluding CodeIgniter 4, failed to
and stars, collected on April 8, 2022. We then picked the        refresh the CSRF secret after a successful login, thus allowing
top 10 of each category. This selection resulted in a total of   an attacker to perform a CORF token fixation (pre-login)
13 frameworks. We refer the reader to Appendix A for the         by reusing the CSRF token issued for the attacker’s session
complete framework list and the associated GitHub metrics.       following the steps described in Fig. 5.



6.1    Frameworks Analysis Methodology                           6.2.1   Passport-Based: Express, Koa, Fastify

We conducted a manual security analysis to expose Web ses-       Several frameworks based on Node.js integrate with the Pass-
sion integrity vulnerabilities in the selected frameworks. For   port authentication middleware to support authenticated user
each framework, we followed the official documentation to        sessions. Express natively integrates with Passport, Koa re-
develop a toy application that includes a login form and a       quires an additional Passport middleware (koa-passport), and
state-changing endpoint protected by a token-based CSRF          Fastify provides its own port of Passport (fastify-passport).
mechanism. The login and CSRF functionalities were imple-        The CSRF protection is implemented by the csurf CSRF token
mented using the official libraries provided by the framework.   middleware in Express, while Koa uses a different middleware
When official libraries were not available, we used external     called koa-csrf; Fastify, instead, provides CSRF protection via
libraries that are widely used by the community, thus be-        the csrf-protection plugin. All implementations support the
ing considered the de facto standards. In two cases, we had      synchronizer token pattern with the CSRF secret being stored
to implement the session management functionality at the         in the session object. The login and user validation functions
application level following the instructions provided in the     are performed by the authenticate function of Passport (and
documentation since no standard libraries were available. For    fastify-passport). We discovered that this function does not
each framework, we also developed an automated routine to        clear, nor reinitializes, the attributes in the session object other
simulate the attacker’s website and to mechanize the CORF        than those specific to Passport, e.g., the passport attribute.
token fixation attacks.                                          Hence, the session attribute csrfSecret (secret in Fastify)
   We performed a coordinated disclosure of the identified       is not renewed upon successful authentication, satisfying the
vulnerabilities, and assisted framework developers to under-     condition (iii) of our attack. Consequently, CSRF tokens is-
stand the threat model and to implement appropriate solutions    sued to the attacker during the pre-session fixation step can
that would improve the baseline security of their frameworks.    be used to forge CORF requests after the victim authenticates
We focused our disclosure on unsafe defaults, avoiding re-       on applications developed using these frameworks.
ports that would have been perceived by developers as poten-     Disclosure. We reported this issue to the Passport developer,
tially deceptive. For instance, we reported vulnerabilities on   who promptly fixed it in version 0.6.0 by clearing all attributes
the double submit pattern only when this CSRF protection         from the session object after login, effectively solving the vul-
mechanism was set as default or it was the only one available.   nerability on Express. However, for backward compatibility,
Double submit is indeed known to be vulnerable against same-     Passport 0.6.0 supports the keepSessionInfo option that en-
site attackers, although it provides some protection against     ables Web developers to opt out from the new safe behavior,
standard Web attackers.                                          and preserve the session attributes between pre-sessions and
   Table 5 summarizes the results of our analysis categorizing   authenticated sessions. This option is set to false by default.
each framework by language and including the selection of        CVE-2022-25896 was issued for this vulnerability. Fastify de-
the libraries used to implement the login and CSRF functional-   velopers promptly fixed the vulnerability in version 2.3.0 by
ities, as well as the adopted CSRF protection mechanisms and     clearing all attributes from the session object after login and
the tested versions. The table also shows the outcome of our     assigned CVE-2023-29020 to this vulnerability. The release
disclosure, denoted with an arrow symbol. Out of the 13 ana-     also introduced support to the clearSessionIgnoreFields op-
lyzed frameworks, we identified 12 supporting the synchro-       tion that enables Web developers to define a set of session
nizer token pattern, among which 7 were found vulnerable         attributes to be preserved between pre-sessions and authen-
to CORF token fixation attacks (pre-login). Furthermore, 6       ticated sessions. On the other hand, the new version of Koa
frameworks implemented the double submit pattern, resulting      middleware (6.0.0, published on February 2023) does not
vulnerable to the post-login attack variant. We also discov-     benefit from the best practices implemented in Passport 0.6.0
ered 3 frameworks vulnerable to session fixation attacks, thus   and remains vulnerable. We are currently in touch with the
allowing an attacker to fully compromise the victim’s account.   developers to identify an effective mitigation.



USENIX Association                                                                  32nd USENIX Security Symposium            5549
                                                                                                    CSRF Protection     CORF Token Fixation   Session
 Framework                   Lang.    Auth. Library                   CSRF Library
                                                                                                        STP   DSP        Pre-L      Post-L    Fixation
 Express (4.18.1) [5]        JS       passport (0.5.3) [57]           csurf (1.11.0) [6]                                       Ë                    Ë
 Koa (2.13.4) [14]           JS       koa-passport (4.1.3) [16]       csrf (3.0.8) [15]                         −                     −         Ë
 Sails (1.5.3) [20]          JS       in cookies as in docs           csurf (1.10.0) [6]                        −                     −

 Fastify (4.13.0) [8]        JS       fastify/passport (2.2.0) [10]   csrf-protection (6.1.0) [9]                              Ë          Ë         Ë
 Django (3.2.13) [4]         Python   built-in                        built-in                                            Ë                     Ë
 Flask (2.1.2) [11]          Python   flask-login (0.6.1) [12]        flask-wtf (1.0.1) [13]                    −                     −         Ë
 Tornado (6.2.0) [26]        Python   in cookies as in docs           built-in                           −                 −                    Ë
 Laravel (9.1.5) [17]        PHP      built-in                        built-in                                  −         Ë           −         Ë
 Symfony (5.4.19) [23]       PHP      built-in                        security-csrf (5.4.19) [24]               −              Ë      −         Ë
 CodeIgniter 4 (4.2.1) [2]   PHP      shield (1.0.0-beta) [3]         built-in                                      −          Ë          −     Ë
 Yii2 (2.0.45) [28]          PHP      built-in                        built-in                                            Ë                     Ë
 ASP.NET Core (6.0.4) [1]    C#       built-in                        built-in                                  −         Ë           −         Ë
 Spring (5.3.19) [21]        Java     Spring Security (5.6.3) [22]    Spring Security (5.6.3)                   −         Ë           −         Ë


Table 5: Analyzed Web frameworks, and their respective authentication and CSRF libraries. default, available, Ë unaffected,
  vulnerable, − not implemented. Ë safe (insecure options available),     vulnerable (secure options available).


6.2.2    Symfony                                                                    user-management logic is hard-coded at the application level
                                                                                    and that the session object is not refreshed upon login, any
Symfony provides user management natively and relies on the
                                                                                    token generated before authentication is still valid after the
official library security-csrf for CSRF protection. Symfony
                                                                                    user authenticates, thus satisfying the precondition (iii) of the
supports three different ways to handle session identifiers and
                                                                                    attack. We expect Web developers to build their applications
session content while authenticating users, called strategies.
                                                                                    starting from the generated template application. For this rea-
The default strategy (MIGRATE) regenerates the session identi-
                                                                                    son, we consider this unsafe code pattern to be likely inherited
fier upon login, but preserves the remaining session attributes.
                                                                                    by real-world websites.
As the CSRF secret is not refreshed, the framework is vul-
nerable to the pre-login CORF token fixation attack. One                           Disclosure. The unsafe code pattern was reported to the Sails
specificity of Symfony is that the granularity of the CSRF                         development team. As a result, a new version of the generator
mechanism can be configured to support distinct CSRF se-                           was released (2.0.7) with support for __Host- cookie prefixes
crets depending on the endpoint. In this case, the pre-login                       in production mode (non-default). Using a __Host- cookie
attack still succeeds against all endpoints where it is possible                   for the session addresses the vulnerability, although Web de-
to obtain a valid CSRF token under a pre-login session. The                        velopers must be aware of cookie scope restrictions that may
attacker simply needs to execute step 1 towards all these                          hamper the deployment of the protection, as discussed in
endpoints to populate a pre-session with the corresponding                         Sec. 5.2.
CSRF secrets before executing step 2 .
Disclosure. This vulnerability was reported to the Symfony                          6.2.4       Flask
developers who updated the MIGRATE strategy to clear the
                                                                                    Flask-based applications supporting user authentication often
CSRF storage in new versions of the library (v4.4.50, v5.4.20,
                                                                                    rely on the Flask-Login library for session management and
v6.0.20, v6.1.12, v6.2.6). We stress that the two other strate-
                                                                                    Flask-WTF to provide CSRF protection using WTForms [27].
gies are either insecure or could introduce compatibility prob-
                                                                                    Login and user validation are performed by the login_user
lems on websites based on Symfony: NONE preserves the same
                                                                                    function that, similarly to Passport, does not clear nor reini-
session after authentication, leading to session-fixation at-
                                                                                    tialize the attributes in the session object other than those
tacks, whereas INVALIDATE regenerates the session identifier
                                                                                    specific for Flask-Login, thus satisfying precondition (iii) of
and deletes all other attributes in the session. CVE-2022-
                                                                                    the attack.
24895 was issued after our disclosure.
                                                                                    Disclosure. This vulnerability was disclosed to the develop-
                                                                                    ers of Flask and Flask-login, proposing a fix that would allow
6.2.3    Sails
                                                                                    developers to define a set of opt-in attributes to be preserved
Sails does not implement a login handler function, however it                       upon login and to clear all others. Given that the two libraries
ships with a generator [19] that bootstraps a template applica-                     operate separately, developers proposed instead to clear all
tion providing a user-management service based on express-                          attributes from the session and let application developers ex-
session [7]. Sails can be configured to enable CSRF pro-                            plicitly copy the attributes that should be preserved. A pull
tection out of the box via the csurf library. Given that the                        request for this issue is still open.



5550     32nd USENIX Security Symposium                                                                                            USENIX Association
6.2.5   CodeIgniter 4                                                 vent cookie tossing. CVE-2023-27495 was issued for this
                                                                      vulnerability. The CodeIgniter 4 Shield library disallowed the
CodeIgniter 4 provides user management via the (official)             combination with the double submit pattern, relying now only
library Shield [3], while CSRF protection is included natively        on the synchronizer token pattern as a more robust CSRF
and can be easily enabled. CodeIgniter 4 offers the synchro-          protection. Tornado added optional support for the __Host-
nizer token pattern and double submit as CSRF protections,            prefix to the CSRF cookie in version 6.3.0 4 . Yii2 develop-
with the latter being the default option. For both mechanisms,        ers initially replied to our disclosure but, to the best of our
the framework supports the option to regenerate the CSRF se-          knowledge, did not follow up on the issue.
cret upon each CSRF-protected action (default), or to preserve
the secret per session, via the option security.regenerate =
true and false respectively. Similarly to the previous cases,         6.4     Session Fixation Vulnerabilities
CodeIgniter 4 is vulnerable to the CORF token fixation (pre-
login) attack when the CSRF secret is not refreshed at login.         We also found 3 frameworks vulnerable to session fixation
However, we discovered that CodeIgniter 4 is also vulner-             attacks. Session fixation attacks happen when pre-session
able when the CSRF secret is regenerated at login via the             cookies are preserved after authentication, thus allowing an
security.regenerate = true setting.                                   attacker to hijack the session of an authenticated user violating
   CodeIgniter 4 sessions objects are stored on the server and        its confidentiality and integrity [61]. The attack flow is the
contain CSRF secrets as attributes called csrf_test_name.             following: (i) the attacker obtains an unauthenticated session
When a user accesses the application, a session object sess           cookie session_cookie=S by visiting https://example.com;
is created with secret s, and upon login, a new session sess′         (ii) the victim is lured into visiting https://atk.example.com
is created with secret s′ . However, while creating sess′ , the       that sets a domain cookie for https://example.com/ in the
attribute csrf_test_name of sess is also updated to s′ . Thus,        victim’s browser, such that session_cookie=S; (iii) the victim
the attack illustrated in Fig. 5 is still possible as the attacker,   authenticates on https://example.com/; (iv) the attacker uses
knowing sess, can perform an additional request between               the session cookie session_cookie=S to hijack the victim’s
steps 3 and 4 to, e.g., /login, and obtain a fresh token t ′ (s′ )    session at https://example.com/. Notice that regenerating the
that is valid for both the pre-session sess and the authenticated     session cookie prevents session fixation, but it is not enough
session sess′ .                                                       to mitigate CORF token fixation attacks if CSRF secret values
Disclosure. This vulnerability was communicated to the de-            still propagate unchanged to the authenticated session.
velopers of Shield, who released a new fixed version of the li-
brary (1.0.0-beta.2) that (i) always refreshes the CSRF secrets
                                                                      6.4.1   Passport
at login, (ii) deletes pre-sessions upon login, and (iii) discon-
tinues the double submit pattern in combination with Shield.          We identified a session fixation vulnerability in Passport stem-
CVE-2022-35943 was issued for this vulnerability.                     ming from the fact that the session attribute sessionId of the
                                                                      pre-session was not cleared nor reinitialized upon login, but
6.3     Double Submit Pattern Issues                                  rather preserved after user authentication.
                                                                      Disclosure. This vulnerability was disclosed to the devel-
All analyzed frameworks implementing the double submit
                                                                      opers of the Passport library and was fixed in version 0.6.0
pattern were vulnerable to CORF token fixation attacks (post-
                                                                      using the Session.regenerate method of the express-session
login). Although this pattern is known to enable same-site
                                                                      module to generate a new sessionId after a successful login.
attackers to bypass CSRF protections, our study aimed at
                                                                      CVE-2022-25896 was issued for this vulnerability.
identifying if any of the frameworks was applying mitigations
such as the __Host- cookie prefix. We concluded that none
of the frameworks applied the above mitigation. Fastify tried         6.4.2   Fastify
to mitigate this attack by including information related to the
logged-in user in the CSRF token in order to prevent cookie           A session fixation attack similar to the one in Passport was
tossing. It turns out that the attack was still possible if the       also identified in Fastify when using the fastify/session plugin
userInfo associated with the target was predictable.                  as the underlying session management mechanism (stateful).
Disclosure. As discussed in Sec. 6.1, we did not contact              Disclosure. This vulnerability was disclosed to the develop-
developers of frameworks that were already applying safe              ers of fastify-passport and was fixed in version 2.3.0 using the
defaults (Express) or were already aware of the risks asso-           session.regenerate method of fastify/session to generate a
ciated with the double submit pattern (Django). The other             new sessionId after a successful login. CVE-2022-29019
vulnerabilities were communicated to the developers of the            was issued for this vulnerability.
4 remaining frameworks. Fastify addressed the vulnerability
by performing an HMAC of the userInfo in order to pre-                   4 https://www.tornadoweb.org/en/stable/releases.html




USENIX Association                                                                       32nd USENIX Security Symposium          5551
6.4.3   Sails                                                       app-action-begin, that happens when the honest user submits
                                                                    the form that contains the CSRF token.
A session fixation attack similar to the one in Passport was
also identified in Sails. We recall that, although Sails does           ∀(c : Cookie)(b : Browser)(token : CSRFToken).
not implement a native login interface, it provides an applica-          event(app-action-successful(c,token)) ⇒ event(app-action-begin(b,token))

tion template that bootstraps a project. Consequently, unsafe
                                                                    Intuitively, the correspondence requires that every instance of
code patterns embedded in the application template could be
                                                                    the app-action-successful event must be preceded by the app-
inherited by real-world websites.
                                                                    action-begin event. This property explicitly forbids execution
Disclosure. This unsafe code pattern was disclosed to the           traces where the attacker successfully executes the protected
Sails team. No particular action was taken to mitigate this         action without the honest user submitting the form.
unsafe pattern in the template application, although the ad-           ProVerif confirms that the property does not hold on any of
dition of the optional __Host-sails.sid in production mode          the four models, producing counterexamples that closely re-
described before mitigates the impact of this attack.               semble the token fixation attack of Fig. 5. We then update the
                                                                    models to include the token refresh mitigation, i.e., generate a
                                                                    new CSRF secret upon user login (Sec. 5.2). Additionally, we
7   Formal Verification of Web Frameworks                           refresh the session identifier on the model for Sails, Express,
                                                                    and Fastify (see session fixation attacks, Sec. 6.4). With these
We complement the analysis of the top Web frameworks
                                                                    modifications, we obtain four fixed models for which ProVerif
(Sec. 6) with the formalization of their session management
                                                                    proves that our correspondence property is valid. Notice that
mechanism and CSRF protections. The goal of our formaliza-
                                                                    in the presence of a session fixation attack, refreshing the
tion is to verify the correctness of the mitigation to vulnerable
                                                                    CSRF secret is not enough for the property to hold, as the at-
synchronizer token patterns, i.e., the CSRF secret refresh dis-
                                                                    tacker can perform a full session hijacking attack and execute
cussed in Sec. 5.2. To this end, we use the WebSpi [38] library
                                                                    the token-protected action.
for the ProVerif [42] protocol verifier, which enables auto-
                                                                       This analysis shows that refreshing the CSRF secret upon
mated security proofs for Web applications.
                                                                    login makes the synchronizer token pattern a robust mitigation
   Our formalization focuses on the 7 frameworks that are           for CORF attacks, even in presence of same-site or network
vulnerable to the pre-login token fixation attack and resulted      attackers who can fully compromise cookie integrity. We
in 4 different framework models that differ depending on            refer the reader to the extended version of our paper [77] for
whether the session is stored on the client or the server side,     additional details on the formalization of Web frameworks.
and on implementation details of the synchronizer token pat-
tern adopted by the framework. This is the case since most
JavaScript frameworks share the user management mecha-              8     Related Work
nism based on the Passport library, and, for instance, Express
and Sails implement CSRF protection with the csurf library.         Several studies have focused on cookie integrity issues, with a
The framework models implement a common API used by a               particular emphasis on session integrity [44, 45, 47, 49, 70, 90].
generic application model to implement login and protected          In their seminal work, Bortz et al. [44] introduce the related-
form elements. The application is run in parallel with a power-     domain attacker model and propose a mechanism, named ori-
ful same-site attacker that can overwrite any cookie on its sib-    gin cookies, to bind cookies to specific origins. The __Host-
ling domains, independently from path or flags/prefixes. This       prefix builds on this proposal and has been integrated into
attacker model over-approximates the threat models in Sec. 3,       modern browsers [50]. Other studies suggest browser exten-
essentially considering cookies with no integrity and resulting     sion, e.g., to transparently strip session (cookie) identifiers
more powerful than SS-HOST-S. This over-approximation               from network requests to avoid session hijacking [45, 70];
ensures stronger security proofs, which are valid irrespectively    Calzavara et al. [47] focus on the server-side by proposing
of integrity assumptions on cookies.                                a type system for verifying session integrity of PHP code
   A CSRF attack results from an unauthorized authenticated         against a variety of attackers, including network and related
request to a protected endpoint performed by the attacker,          domain attackers. These works, except for [90], do not assess
thus we define our expected security property as follows.           the implications of the lack of cookie integrity for real world
                                                                    application. Zheng et al. [90] present an empirical assessment
Invariant. Every action executed by a token-protected end-          of cookie injection attacks on the Web, taking into account
point must be explicitly initiated by an honest user by per-        both browser-side and server-side cookie handling inconsis-
forming a request containing the token.                             tencies, and discovering attacks on popular Web sites (e.g.,
We encode the invariant as a correspondence assertion [88]          Google, Amazon). Similarly to our work, the authors discover
between the two events (i) app-action-successful, that happens      browser implementation differences in storage limits for cook-
when the server successfully validates the CSRF token and           ies and cookie ordering in requests, and inconsistencies in
performs the token-protected state-changing action, and (ii)        server-side languages such as the automatic percent decoding



5552    32nd USENIX Security Symposium                                                                                   USENIX Association
of cookie names in PHP. Our findings uncover that, even after      Acknowledgments
seven years, these types of cross-browser/language incon-
sistencies are still relevant and also affect newly introduced     We thank the anonymous reviewers for their helpful sug-
security mechanisms such as __Host- prefix cookies.                gestions. We also thank Bernhard Kralofsky for perform-
   Recently, Squarcina et al. [78] measured and quantified         ing an initial investigation of Web frameworks as part of
the threats posed by same-site attackers to Web application        his bachelor thesis at TU Wien in 2021 and Leonardo
security. In their study of cookies, they discovered that the      Nodari, who suggested studying the AWS Lambda proxy
majority of the cookies on sites vulnerable to subdomain           and prepared a testing environment for us. This work has
takeover has no integrity against related domain attackers.        been partially supported by the European Research Coun-
The authors highlight that the __Host- prefix was used only        cil (ERC) under the European Union’s Horizon 2020 re-
once in their dataset. Our measurement (Sec. 4.4) confirms         search (grant agreement 771527-BROWSEC); by the Vi-
the infrequent usage of the prefix in the wild, but shows a        enna Science and Technology Fund (WWTF) and the City
promising positive trend on its adoption in the last 2 years,      of Vienna [Grant ID: 10.47379/ICT22060]; by the Austrian
especially on lower-ranked websites. Sanchez-Rola et al. [74]      Research Promotion Agency (FFG) through the COMET
performed a large-scale measurement to characterize cookie-        K1 SBA; by the Fundação para a Ciência e a Tecnologia
based Web tracking. The study shows that third-party script        (UIDB/50008/2020, Instituto de Telecomunicações), project
inclusion enables cookie sharing in the context of first-party     DIVINA (CMU/TIC/0053/2021), and the European Commis-
cookies, thus enabling third parties to set cookies on behalf      sion under grant agreement 830892 (SPARTA).
of the visited website. Additionally, the authors report on
instances of cookie collisions, where scripts from different       References
actors in the same website access cookies created with the
same name but different semantics. This setting matches our         [1] ASP.NET. https://dot.net.
SS-XSS-S threat model (Sec. 3), where different parties gain
control of a domain on a page served via HTTPS. However,            [2] CodeIgniter 4. https://codeigniter.com/user_
unlike the study of Sanchez-Rola et al., which does not con-            guide/index.html.
sider domain cookies, we focus on cookie integrity violations
                                                                    [3] CodeIgniter Shield. https://codeigniter4.github.
from attacker-controlled subdomains.
                                                                        io/shield/.
   Concerning the analysis of Web frameworks, Likaj et
al. [62] evaluated the mechanisms implemented by major              [4] Django Framework. https://www.djangoproject.
Web frameworks, quantifying their exposure to CSRF attacks              com/.
as a result of implementation mistakes, cryptography-related
flaws, cookie integrity violations, or leakage of CSRF tokens.      [5] Express. https://expressjs.com/.
The authors discover that 37 out of 44 frameworks are affected
                                                                    [6] Express csurf: CSRF token middleware. https://
by such issues. Our analysis of Web frameworks (Sec. 6)
                                                                        github.com/expressjs/csurf.
shows that further implementation issues in the synchronizer
token pattern (deemed secure in [62]), originating from the         [7] Express Session. https://github.com/expressjs/
composition of different libraries, lead to a bypass of the pro-        session.
tection in the presence of same-site attackers. For instance,
the CORF token fixation attack sidesteps the Flask framework        [8] Fastify. https://www.fastify.io/.
protection, which was considered secure in previous work.
                                                                    [9] Fastify csrf-protection. https://github.com/
                                                                        fastify/csrf-protection.
9   Conclusion
                                                                   [10] Fastify Passport. https://github.com/fastify/
This study is a modern look at cookie integrity issues and their        fastify-passport.
impact on Web application security. Our research showed that       [11] Flask. https://flask.palletsprojects.com/.
integrity vulnerabilities are not limited to implementation
bugs, but are a pervasive threat across the Web due to com-        [12] Flask Login. https://flask-login.readthedocs.
positionality problems at multiple levels. We engaged with              io/.
browser vendors, the IETF HTTP Working Group, and Web
framework developers to address the discovered issues, which       [13] Flask WTF.      https://flask-wtf.readthedocs.
resulted in several high-impact updates, e.g., Chrome and               io/.
Firefox, PHP (the server-side language powering 78% of all         [14] Koa. https://koajs.com.
websites), major authentication libraries such as Passport (2M
weekly downloads), and the cookie standard [50].                   [15] Koa CSRF. https://github.com/koajs/csrf.



USENIX Association                                                                 32nd USENIX Security Symposium     5553
[16] Koa Passport.         https://github.com/rkusa/          [34] Mozilla Bugzilla. Issue 1783982: Cookie pre-
     koa-passport.                                                 fixes bypass via nameless cookies (rfc6265bis).
                                                                   https://bugzilla.mozilla.org/show_bug.cgi?
[17] Laravel Framework. https://laravel.com/.                      id=1783982, 2022.
[18] PHP Manual: Using Register Globals. https://web.
                                                              [35] PHP Bug Tracker. Issue 81727: cookie integrity vul-
     archive.org/web/20201205183413/https://www.
                                                                   nerabilities. https://bugs.php.net/bug.php?id=
     php.net/manual/en/security.globals.php.
                                                                   81727, 2022.
[19] Sails   Generate.           https://sailsjs.
                                                              [36] Angular.    HTTP: Security - XSRF Protec-
     com/documentation/reference/
                                                                   tion.        https://angular.io/guide/http#
     command-line-interface/sails-generate.
                                                                   security-xsrf-protection, 2022.
[20] Sails.js. https://sailsjs.com/.
                                                              [37] HTTP Archive. The HTTP Archive.               https://
[21] Spring. https://spring.io/.                                   httparchive.org/.
[22] Spring Security. https://spring.io/projects/             [38] C. Bansal, K. Bhargavan, and S. Maffeis. Discovering
     spring-security.                                              Concrete Attacks on Website Authorization by Formal
                                                                   Analysis. In CSF. IEEE, 2012.
[23] Symfony. https://symfony.com/.
                                                              [39] A. Barth. HTTP State Management Mechanism. RFC
[24] Symfony CSRF.       https://github.com/symfony/
                                                                   6265, IETF, 2011.
     security-csrf.
[25] The Web Platform Tests Project.            https://      [40] A. Barth. The Web Origin Concept. RFC 6454, IETF,
     web-platform-tests.org/.                                      12 2011.

[26] Tornado Web Server.      https://www.tornadoweb.         [41] A. Barth, C. Jackson, and J. C. Mitchell. Robust De-
     org/.                                                         fenses for Cross-Site Request Forgery. In CCS. ACM,
                                                                   2008.
[27] WTForms. https://wtforms.readthedocs.io/.
                                                              [42] B. Blanchet. An efficient cryptographic protocol verifier
[28] Yii PHP framework. https://www.yiiframework.                  based on Prolog rules. In WCSF. IEEE, 2001.
     com/.
                                                              [43] K. Borgolte, T. Fiebig, S. Hao, C. Kruegel, and G. Vigna.
[29] Chromium Bugs. Issue 1351601: Cookie pre-                     Cloud Strife: Mitigating the Security Risks of Domain-
     fixes bypass via nameless cookies (rfc6265bis).               Validated Certificates. In NDSS, 2018.
     https://bugs.chromium.org/p/chromium/
     issues/detail?id=1351601, 2022.                          [44] A. Bortz, A. Barth, and A. Czeskis. Origin Cookies:
                                                                   Session Integrity for Web Applications. In W2SP, 2011.
[30] Chromium Bugs. Issue 1354090: post-CVE-2022-
     2860 security limitations of cookie prefixes and         [45] M. Bugliesi, S. Calzavara, R. Focardi, and W. Khan.
     nameless cookies. https://bugs.chromium.org/p/                CookiExt: Patching the browser against session hijack-
     chromium/issues/detail?id=1354090, 2022.                      ing attacks. Journal of Computer Security, 2015.
[31] IETF HTTP Working Group, HTTP Extensions. Issue          [46] Web Almanac by HTTP Archive. Http archive’s
     2229: [rfc6265bis] nameless cookies, client/server in-        annual state of the web report. https://almanac.
     consistencies #2229. https://github.com/httpwg/               httparchive.org/, 2022.
     http-extensions/issues/2229, 2022.
                                                              [47] S. Calzavara, R. Focardi, N. Grimm, M. Maffei, and
[32] Mozilla Bugzilla. Issue 1782561. document.cookie              M. Tempesta. Language-Based Web Session Integrity.
     desynchronization    after cookie jar overflow.               In CSF. IEEE, 2020.
     https://bugzilla.mozilla.org/show_bug.cgi?
     id=1782561, 2022.                                        [48] S. Calzavara, R. Focardi, M. Squarcina, and M. Tem-
                                                                   pesta. Surviving the Web: A Journey into Web Session
[33] Mozilla Bugzilla. Issue 1783536. document.cookie in           Security. CSUR, 50(1):13:1–13:34, 2017.
     an insecure origin process allows setting an insecure
     cookie in that process that has the same name as a se-   [49] S. Calzavara, A. Rabitti, and M. Bugliesi. Sub-Session
     cure one. https://bugzilla.mozilla.org/show_                  Hijacking on the Web: Root Causes and Prevention.
     bug.cgi?id=1783536, 2022.                                     Journal of Computer Security, 2019.



5554   32nd USENIX Security Symposium                                                                 USENIX Association
[50] L. Chen, S. Englehardt, M. West, and J. Wilander. Cook-   [64] R. Lundeen. The Deputies are Still Confused. https://
     ies: HTTP State Management Mechanism (IETF Draft).             media.blackhat.com/eu-13/briefings/Lundeen/
     RFC 6265bis, IETF, 2022.                                       bh-eu-13-deputies-still-confused-lundeen-wp.
                                                                    pdf, 2013.
[51] GitHub Advisory Database. ReactPHP’s HTTP server
     parses encoded cookie names so malicious __Host- and      [65] Microsoft.  Prevent Cross-Site Request Forgery
     __Secure- cookies can be sent. https://github.com/             (XSRF/CSRF)    attacks  in    ASP.NET    Core.
     advisories/GHSA-w3w9-vrf5-8mx8, 2022.                          https://learn.microsoft.com/en-us/aspnet/
                                                                    core/security/anti-request-forgery, 2022.
[52] GitHub Advisory Database. Incorrect parsing of
     nameless cookies leads to __Host- cookies by-             [66] Mozilla. Public Suffix List. https://publicsuffix.
     pass.   https://github.com/pallets/werkzeug/                   org/.
     security/advisories/GHSA-px8h-6qxv-m22q,
     2023.                                                     [67] Mozilla. Project Fission. https://wiki.mozilla.
                                                                    org/Project_Fission, 2022.
[53] Detectify.     Hostile subdomain takeover us-
                                                               [68] Mozilla Developer Network. Cookie Store API.
     ing heroku/github/desk + more.         https:
                                                                    https://developer.mozilla.org/en-US/docs/
     //labs.detectify.com/2014/10/21/
                                                                    Web/API/Cookie_Store_API.
     hostile-subdomain/, 2014.
                                                               [69] Mozilla Developer Network.        Set-Cookie.
[54] GitHub.        Top programming languages.                      https://developer.mozilla.org/en-US/docs/
     https://octoverse.github.com/2022/                             Web/HTTP/Headers/Set-Cookie.
     top-programming-languages, 2022.
                                                               [70] N. Nikiforakis, W. Meert, Y. Younan, M. Johns, and
[55] T. Van Goethem, C. Pöpper, W. Joosen, and M. Vanhoef.          W. Joosen. SessionShield: Lightweight Protection
     Timeless Timing Attacks: Exploiting Concurrency to             against Session Hijacking. In Engineering Secure Soft-
     Leak Secrets over Remote Connections. In USENIX                ware and Systems. Springer Berlin Heidelberg, 2011.
     Security, 2020.
                                                               [71] OWASP. Cross-site request forgery prevention cheat
[56] Google. Chrome UX Report. https://developer.                   sheet.  https://cheatsheetseries.owasp.org/
     chrome.com/docs/crux/.                                         cheatsheets/Cross-Site_Request_Forgery_
                                                                    Prevention_Cheat_Sheet.html.
[57] J. Hanson. Passport – Simple, unobtrusive authentica-
     tion for Node.js. https://www.passportjs.org/.            [72] OWASP.     Session hijacking attack.  https:
                                                                    //owasp.org/www-community/attacks/Session_
[58] S. Helme. Cross-Site Request Forgery is dead! https:           hijacking_attack.
     //scotthelme.co.uk/csrf-is-dead/, 2017.
                                                               [73] I. Sanchez-Rola, D. Balzarotti, and I. Santos. Baking-
[59] S. Helme.   CSRF is (really) dead. https://                    Timer: Privacy Analysis of Server-Side Request Process-
     scotthelme.co.uk/csrf-is-really-dead/, 2019.                   ing Time. In ACSAC. ACM, 2019.

[60] J. Henkel and B. Pollard. Adding Rank Magnitude to        [74] I. Sanchez-Rola, M. Dell’Amico, D. Balzarotti,
     the CrUX Report in BigQuery. https://developer.                P. Vervier, and L. Bilge. Journey to the Center of the
     chrome.com/blog/crux-rank-magnitude/, 2021.                    Cookie Ecosystem: Unraveling Actors’ Roles and
                                                                    Relationships. In S&P. IEEE, 2021.
[61] M. Kolšek. Session fixation vulnerability in web-
     based applications. https://acrossecurity.com/            [75] Amazon Web Services.          Working with
     papers/session_fixation.pdf, 2002.                             AWS Lambda proxy integrations for HTTP
                                                                    APIs.          https://docs.aws.amazon.com/
[62] X. Likaj, S. Khodayari, and G. Pellegrino. Where We            apigateway/latest/developerguide/
     Stand (or Fall): An Analysis of CSRF Defenses in Web           http-api-develop-integrations-lambda.html,
     Frameworks. In RAID. ACM, 2021.                                2022.

[63] D. Liu, S. Hao, and H. Wang. All Your DNS Records         [76] K. Singh, A. Moshchuk, H. J. Wang, and W. Lee. On the
     Point to Us: Understanding the Security Threats of Dan-        Incoherencies in Web Browser Access Control Policies.
     gling DNS Records. In CCS. ACM, 2016.                          In S&P. IEEE, 2010.



USENIX Association                                                              32nd USENIX Security Symposium       5555
[77] M. Squarcina, P. Adão, L. Veronese, and M. Maffei.      A    Web Framework Analysis
     Cookie Crumbles: Breaking and Fixing Web Session
     Integrity – source code, artifacts, and extended ver-   Table 6 lists the entire pool of Web frameworks considered
     sion of the paper. https://github.com/SecPriv/          for this study. We restricted the analysis to the top 10 frame-
     cookiecrumbles, 2023.                                   works according to the GitHub metrics watch, fork, and stars,
                                                             obtaining the final set of 13 frameworks.
[78] M. Squarcina, M. Tempesta, L. Veronese, S. Calzavara,
     and M. Maffei. Can I Take Your Subdomain? Exploring      Framework        Language   GH Watch     GH Fork    GH Star
     Same-Site Attacks in the Modern Web. In USENIX           ASP.NET MVC         C#              75        329        739
     Security, 2021.                                          ASP.NET Core        C#            1.4k       7.7k      27.8k
                                                              Service Stack       C#             515       1.6k         5k
                                                              Nancy               C#             438       1.5k       7.2k
[79] A. Sudhodanan, S. Khodayari, and J. Caballero. Cross-
     Origin State Inference (COSI) Attacks: Leaking Web       Spring             Java           3.4k      33.3k      47.1k
                                                              Play               Java            683         4k      12.1k
     Site States through XS-Leaks. In NDSS, 2020.             Spark              Java            413       1.6k       9.3k
                                                              Vert.x-web         Java             79        470        955
[80] J. Valim. CSRF token fixation attacks in Devise.         Vaadin             Java             53         59        361
     https://blog.plataformatec.com.br/2013/                  Dropwizard         Java            398       3.4k       8.2k
     08/csrf-token-fixation-attacks-in-devise/,               Blade              Java            302       1.1k       5.6k
                                                              ZK                 Java             46        169        350
     2013.                                                    Apache Struts      Java            124        737       1.1k
                                                              Apache Wicket      Java             61        354        616
[81] T. Van Goethem, G. Franken, I. Sanchez-Rola,             Express             JS            1.8k       9.6k      56.6k
     D. Dworken, and W. Joosen. SoK: Exploring Current        Meteor              JS            1.6k       5.2k      42.9k
     and Future Research Directions on XS-Leaks through       Koa                 JS             847       3.2k      32.5k
     an Extended Formal Model. In ASIA CCS. ACM, 2022.        Hapi                JS             422       1.4k      13.8k
                                                              Sails               JS             667         2k      22.2k
                                                              Fastify             JS             281       1.7k      22.7k
[82] W3C. Working Draft: Clear Site Data. https://www.        ThinkJS             JS             268        643       5.3k
     w3.org/TR/clear-site-data/, 2017.                        Total.js            JS             218        459       4.1k
                                                              AdonisJS            JS             229        579      12.3k
[83] W3Techs. Usage statistics of PHP for websites. https:    Laravel            PHP            4.6k      22.4k      69.3k
     //w3techs.com/technologies/details/pl-php,               Symfony            PHP            1.2k       8.6k      26.7k
     2023.                                                    Slim               PHP             525       1.9k      11.3k
                                                              CakePHP            PHP             573       3.5k       8.5k
                                                              Zend/Laminas       PHP              18         56       1.4k
[84] web.dev. Schemeful Same-Site. https://web.dev/           CodeIgniter        PHP            1.6k       7.8k      18.2k
     schemeful-samesite/.                                     FuelPHP            PHP             107        287       1.4k
                                                              Yii2               PHP            1.1k         7k      13.9k
[85] M. West. Cookie Prefixes. https://tools.ietf.            Phalcon            PHP             658       1.9k      10.6k
     org/html/draft-west-cookie-prefixes-05.                  Li3                PHP              91        247       1.2k
                                                              CodeIgniter4       PHP             278       1.6k       4.2k

[86] M. West and M. Goodwin. RFC6265: Same-site Cook-         Flask             Python          2.2k       15k       58.5k
                                                              Django            Python          2.3k      26.9k      63.3k
     ies draft-west-first-party-cookies-07, 2016.             Tornado           Python            1k       5.4k      20.5k
                                                              Bottle            Python           320       1.4k       7.6k
[87] J. Wilander. Advanced CSRF and Stateless Anti-           Pyramid           Python           160        878       3.7k
     CSRF.     https://owasp.org/www-pdf-archive/             Falcon            Python           273        872       8.7k
     /AppSecEU2012_Wilander.pdf, 2012.                        Zope              Python            91         99        288
                                                              Masonite          Python            57        104       1.7k
                                                              TurboGears2       Python            32         76        777
[88] T. Y. C. Woo and S. S. Lam. A semantic model for         Web2py            Python           220        866         2k
     authentication protocols. In S&P. IEEE, 1993.
                                                             Table 6: Web development frameworks from [62] ranked
[89] M. Zalewski. The tangled web: A guide to securing       according to GitHub metrics as of April 8, 2022.
     modern web applications. No Starch Press, 2011.

[90] X. Zheng, J. Jiang, J. Liang, Haixin Duan, S. Chen,
     T. Wan, and N. Weaver. Cookies lack integrity: Real-
     world implications. In USENIX Security, 2015.



5556   32nd USENIX Security Symposium                                                                  USENIX Association
