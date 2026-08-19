---
type: Article
title: "Dancer in the Dark: Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting"
resource: "https://www.usenix.org/conference/usenixsecurity24/presentation/kirchner"
tags: [article, webseclist-reference, en, usenix-org]
generated:
  by: webseclist-refs/1
  at: "2026-08-19T16:20:43+00:00"
status: stable
stale_after: 2027-08-19
sources:
  - id: original
    resource: "https://www.usenix.org/conference/usenixsecurity24/presentation/kirchner"
    title: "Dancer in the Dark: Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting"
    author: Robin Kirchner, Jonas Möller, Marius Musch, David Klein, Konrad Rieck, Martin Johns
also_at:
  - "https://www.usenix.org/system/files/usenixsecurity24-kirchner.pdf"
  - "https://www.usenix.org/system/files/usenixsecurity24-appendix-kirchner.pdf"
  - "https://www.usenix.org/system/files/sec23winter-prepub-226-kirchner-rev.pdf"
  - "https://www.usenix.org/system/files/usenixsecurity24_slides-kirchner.pdf"
authors:
  - Robin Kirchner
  - Jonas Möller
  - Marius Musch
  - David Klein
  - Konrad Rieck
  - Martin Johns
canonical_url: ""
cited_by:
  - "2024.md:112"
commit: ""
content_sha256: 9478b6cc4e0fa5892a86550d96539636aee6c99e902496949224b56ce7747449
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://www.usenix.org/conference/usenixsecurity24/presentation/kirchner"
published: ""
publisher: usenix.org
publisher_english: ""
raw_sha256: 77c6eff0cb65a30d5648c36416f94a8311c92bbdb272e72ff2382c3b1b10c63a
retrieved_from: "https://www.usenix.org/system/files/usenixsecurity24-kirchner.pdf"
retrieved_kind: live
retrieved_utc: "2026-08-19T16:20:43+00:00"
slug: usenix-org-dancer-dark-synthesizing-evaluating-polyglots-blind-cross-scripting
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Dancer in the Dark: Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting

**Dancer in the Dark: Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting** - Robin Kirchner, Jonas Möller, Marius Musch, David Klein, Konrad Rieck, Martin Johns, usenix.org.

- Published: date not stated
- Original: <https://www.usenix.org/conference/usenixsecurity24/presentation/kirchner>
- Also published at: <https://www.usenix.org/system/files/usenixsecurity24-kirchner.pdf>
- Also published at: <https://www.usenix.org/system/files/usenixsecurity24-appendix-kirchner.pdf>
- Also published at: <https://www.usenix.org/system/files/sec23winter-prepub-226-kirchner-rev.pdf>
- Also published at: <https://www.usenix.org/system/files/usenixsecurity24_slides-kirchner.pdf>
- Preserved from: https://www.usenix.org/system/files/usenixsecurity24-kirchner.pdf (live) on 2026-08-19
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Dancer in the Dark: Synthesizing and Evaluating
    Polyglots for Blind Cross-Site Scripting
Robin Kirchner, Technische Universität Braunschweig; Jonas Möller, Technische
  Universität Berlin; Marius Musch and David Klein, Technische Universität
  Braunschweig; Konrad Rieck, Technische Universität Berlin; Martin Johns,
                      Technische Universität Braunschweig
      https://www.usenix.org/conference/usenixsecurity24/presentation/kirchner




       This paper is included in the Proceedings of the
              33rd USENIX Security Symposium.
                 August 14–16, 2024 • Philadelphia, PA, USA
                                 978-1-939133-44-1




                                        Open access to the Proceedings of the
                                          33rd USENIX Security Symposium
                                              is sponsored by USENIX.
                                    Dancer in the Dark:
             Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting

       Robin Kirchner∗† , Jonas Möller ‡ , Marius Musch† , David Klein† , Konrad Rieck ‡ , Martin Johns†
                                      † Technische Universität Braunschweig, Germany
                                          ‡ Technische Universität Berlin, Germany

                             {robin.kirchner, m.musch, david.klein, m.johns}@tu-braunschweig.de
                                              {jonas.moeller.1, rieck}@tu-berlin.de

                               Abstract                              re-identification of an input string in the application’s HTML,
Cross-Site Scripting (XSS) is a prevalent and well known             in the case of manual bug hunting, and as sophisticated as
security problem in web applications. Numerous methods to            fully automatic taint analysis.
automatically analyze and detect these vulnerabilities exist.           This poses a problem for an often overlooked component of
However, all of these methods require that either code or feed-      large web applications: the backend. Similar to the use of web
back from the application is available to guide the detection        technologies in its public frontend, the same application often
process. In larger web applications, inputs can propagate from       employs web interfaces for its internal backends. These inter-
a frontend to an internal backend that provides no feedback to       faces, inaccessible from the public internet behind a firewall,
the outside. None of the previous approaches are applicable          serve various internal application functions, including admin-
in this scenario, known as blind XSS (BXSS). In this paper,          istration of the application, usage analysis, and back-office
we address this problem and present the first comprehensive          tasks such as supply chain management and accounting.
study on BXSS. As no feedback channel exists, we verify the             Not different from public web applications, internal web
presence of vulnerabilities through blind code execution. For        tools are also susceptible to security problems in general and
this purpose, we develop a method for synthesizing polyglots,        XSS in particular. As these backend systems process data
small XSS payloads that execute in all common injection con-         generated by the application’s public counterpart, there is a
texts. Seven of these polyglots are already sufficient to cover      high likelihood of data from potentially malicious, attacker-
a state-of-the-art XSS testbed. In a validation on real-world        supplied inputs flowing into the backend’s web code. This
client-side vulnerabilities, we show that their XSS detection        situation opens the door for XSS attacks on internal applica-
rate is on par with existing taint tracking approaches. Based        tion components. However, current XSS detection techniques
on these polyglots, we conduct a study of BXSS vulnerabil-           fall short in finding such flaws, as no evidence of problematic
ities on the Tranco Top 100,000 websites. We discover 20             data flows can be obtained. All effects of the public-to-internal
vulnerabilities in 18 web-based backend systems. These find-         flows remain within the constraints of the internal systems.
ings demonstrate the efficacy of our detection approach and          Testing tools operating from the outside are literally “blind”
point at a largely unexplored attack surface in web security.        to any side effects caused by injection attempts.
                                                                        In this paper, we present the first comprehensive study on
                                                                     Blind Cross-Site Scripting (BXSS) vulnerabilities. As by defi-
1     Introduction                                                   nition no direct channels from the affected system-under-test
                                                                     and the testing approach exist, the only option to verify the
Web applications are ubiquitous—so are their security prob-
                                                                     presence of a BXSS vulnerability is the injection and execu-
lems. In particular, the vulnerability class of Cross-Site Script-
                                                                     tion of JavaScript code. To this end, we present a method for
ing (XSS) remains one of the major security issues on the
                                                                     synthesizing polyglots: XSS payloads specifically designed
Web. Over the past decade, XSS has been studied extensively,
                                                                     for a multitude of injection contexts. More specifically, we
with a focus on approaches to detect these flaws in exist-
                                                                     use Monte Carlo tree search (MCTS) to synthesize a small
ing applications. This detection relies on the identification
                                                                     set of seven polyglots, capable of executing code in all test
of insecure data flows from attacker-controlled inputs into
                                                                     cases of a state-of-the-art XSS testbed (see Section 3).
security-sensitive sinks. The actual techniques to pursue this
                                                                        However, good performance on an artificial testbed does
goal vary, but they all rely on the availability of observable
                                                                     not necessarily result in similar properties in real-world set-
evidence of such data flows. This can be as simple as the
                                                                     tings. For this reason, we validate the generated polyglots on
    ∗ Corresponding author                                           a set of recently uncovered client-side XSS vulnerabilities



USENIX Association                                                                      33rd USENIX Security Symposium          6723
found in the Tranco Top 10,000 websites. To do so, we com-             language defines its own syntactic and semantic rules, an at-
pare the polyglots’ capability to uncover vulnerabilities with         tack payload has to be tailored to the exact location where
the currently established state-of-the-art method of precise           it is inserted in the document. In the following, we refer to
payload generation [4, 19, 22, 26, 42, 43]. In this experiment         this location as the injection context. Similarly, protection
our blind polyglots prove to be highly competitive with pre-           mechanisms need to be context aware to correctly assess what
cise exploit generation, through triggering 147 vulnerabilities        constitutes dangerous input for a specific injection context.
compared to 145 found by the precise payload generation.               This makes it challenging to defend against XSS [37, 48].
Furthermore, the generated polyglots vastly outperform the                 To illustrate the role of the injection context, let us consider
well-known, manually crafted “Ultimate Polyglot” [11] (see             the running example in Figure 1. The code snippet contains
Section 4 for details).                                                three lines, each highlighting a different injection context:
   Finally, we present the—to the best of our knowledge—first          inside of an HTML a tag ❶, as a URI in the src attribute in
study on BXSS in the wild. We conduct a large-scale analysis           the iframe element ❷, and as a double-quoted string inside a
of the Tranco Top 100,000 websites using our generated poly-           JavaScript code context ❸. Input injected at each of these three
glots as testing payloads, uncovering 20 instances of BXSS             points is processed by a different parser, namely the HTML,
problems in internal systems. This study demonstrates that             the URI and the JavaScript parser, respectively. Consequently,
our testing approach is well suited to detect BXSS vulnerabil-         each of these injection contexts and their many variations
ities in real-world websites, as well as, the existence of this        require substantially different attack payloads tailored for the
vulnerability class (see Section 5) on popular websites.               syntactic and semantic rules of said parser and context.
                                                                           In order to successfully achieve code execution within one
Contribution. In summary, we make the following contri-                of these injection contexts, one needs to craft a payload that
butions in this paper:                                                 either directly calls a JavaScript function or moves into a
                                                                       parsing state where this is possible. Especially the URI case
    • We propose a method for automatically synthesizing               highlights how not only the current parser state, but also the
      a small set of XSS polyglots using Monte Carlo tree              directly preceding ones are relevant for success. For example,
      search, covering all currently known injection contexts.         the src attribute of the iframe at ❷ is directly exploitable
    • We show that the polyglots synthesized by our method             with a JavaScript URI, unlike the src of an img tag. Instead,
      achieve comparable performance to state-of-the-art vul-          we would have to move to a different parsing state first by
      nerability detection for client-side XSS.                        trying to break out of the surrounding quotes.
    • We design a methodology to detect backend XSS auto-
      matically and use it to conduct a large-scale evaluation     1     <a href="..."> ❶ </a>
                                                                   2     <iframe src='❷'></iframe>
      on the 100,000 most popular websites, finding 20 BXSS        3     <script>if (x == "❸") { ... }</script>
      vulnerabilities in 18 backend systems.

2    Blind Cross-Site Scripting                                        Figure 1: Code segments depicting injections in three different
                                                                       contexts: In HTML ❶, in a URI ❷, and in JavaScript code ❸.
Cross-Site Scripting (XSS) is a notorious class of vulnera-
bilities, consistently earning a place in the OWASP Top 10                Therefore, to craft an XSS payload an attacker has to de-
as one of the most critical web security risks [29–31]. These          duce the injection context first. This is usually done by either
vulnerabilities are rooted in the representation of web content,       manual testing, where the tester analyzes the website’s code,
which only loosely separates data from markup and enables              or automatic payload generation in the presence of perfect in-
an attacker to manipulate a website or even execute code               formation. The latter, in particular, received a lot of attention
through malicious inputs deliberately breaking this separa-            from researchers applying taint tracking techniques to un-
tion. Therefore, special care has to be taken when inserting           cover these vulnerabilities [19, 22, 26, 41, 42]. In short, these
user-controlled data into web content.                                 approaches use a modified browser to mark all data entered
   This problem of XSS is further exacerbated by the wealth of         via user-controlled sources as tainted. This taint information
representations available for describing web content. For ex-          is then propagated through the browser until it enters a sink
ample, HTML documents can be interspersed with resources               functionality, which potentially results in code execution.
spanning various languages, such as Cascading Style Sheets                While the detection of reflected XSS vulnerabilities has
(CSS), JavaScript code, Scalable Vector Graphics (SVG) and             been thoroughly studied, the server-side stored XSS variant,
even mathematical expressions (MathML). As a result, XSS               i.e., when the payload is not directly executed and instead first
vulnerabilities can arise in any of these formats if user-             stored on the server, is still a hard-to-detect XSS type [13].
controlled data is inserted without sanitization.                      The main challenge with this variant is that it requires rea-
   However, this mishmash of languages also imposes require-           soning about intra-page dependencies: The page where the
ments on any attack exploiting XSS vulnerabilities. As each            payload is inserted to be subsequently stored somewhere,



6724    33rd USENIX Security Symposium                                                                             USENIX Association
                                                                   unsuccessful attack attempts provide no information to an
          Web Application            Web App          Backend
                                                                   attacker who is totally in dark about in which context the
                                                ?                  malicious payloads is injected, whether it has been adapted,
              Database                                             or if simply nobody visited the backend system to trigger it.
                                                                      Figure 2 further illustrates this crucial difference: As Fig-
                                                                   ure 2a shows, the attacker can access the vulnerable page,
                                                                   learn about the injection context and adapt their payload ac-
                                                                   cordingly in the stored XSS case. However, they have no way
                                     Attacker          Victim
   Attacker                 Victim                                 of inspecting the admin panel in the backend in the blind XSS
                (a)                             (b)                case depicted in Figure 2b. Due to these challenges and to the
                                                                   best of our knowledge, blind XSS has not yet been system-
Figure 2: Attack flows of stored XSS (a) and blind XSS (b)         atically studied and no automated approach to uncover these
vulnerabilities. Only the stored XSS scenario allows the at-       vulnerabilities exists, so far.
tacker to inspect the injection context to adapt their exploit.
                                                                   Threat model. We consider the following threat model:
                                                                   The attacker interacts with a publicly accessible website that
might only be indirectly related to the page where the ex-         might or might not be indirectly connected to an internal web-
ploit actually triggers after it is read from storage. However,    site via a storage mechanism, such as a database, log file or
as long as these two sides are publicly accessible, a manual       internal web service. The attacker has no knowledge about
tester or automated system can still incrementally adjust the      any internal webpages, the used storage technology, or data
stored attack payloads to explore the server-side processing       transformations steps in between. There is no feedback unless
and finally derive a working exploit.                              the attack is successful. The attacker’s goal is to achieve code
   One particularly challenging variation of stored XSS is the     execution via XSS in the context of an internal web applica-
so-called blind XSS (BXSS) vulnerability, where even this          tion of the website’s backend, once visited by a person with
context information is no longer available.                        access or an automated system with a full browser. All other
                                                                   payload entry points besides publicly accessible websites,
2.1     The BXSS Attack Scenario                                   such as phishing emails, are out of scope for this work.

As part of the deployment of larger web applications, there
are often further web-based backends involved beyond what          2.2    XSS Polyglots
is accessible for visitors from the Internet. Typical use cases    Ideally, we would overcome this challenge of not having a
for such intranet web applications are administration, mon-        feedback by creating a universal XSS payload that triggers
itoring, visitor statistics, and back office tasks. While these    in all contexts. As previously described, we need to consider
applications are usually protected by a firewall from direct       several different parsers for this, as our payload could end up
outside attacks, they can still be susceptible to XSS attacks      inside any of them. A construct that is valid input in multiple
if malicious inputs reach these internal sites. For example, a     formats and/or languages is a so-called polyglot [23]. For
monitoring system might read web server access logs from the       example, GIFAR is a technique to create a file that is both a
public part of the website and display all Referer headers on      valid GIF image and a valid Java Archive (JAR) [5].
an internal webpage, allowing insights into visitor behavior.         In the context of this paper, polyglot refers to an XSS ex-
However, if these attacker-controlled header values are not        ploit that is able to execute in multiple injection contexts, such
properly sanitized, they could result in XSS on that internal      as HTML and JavaScript code. Moreover, payload refers to
page. Due to their purpose, the consequences of successful         the part of the exploit that is actually executed, e.g., alert()
attacks on these internal pages can be especially high, as these   or import(). Coming back to our example in Figure 1 and
pages are only visited by privileged users and might allow ad-     assuming we want to execute the payload alert() for demon-
ministrative actions. Moreover, these backend systems might        stration, the three different injection contexts require different
not be part of the application’s threat model and therefore        conditions for the payload to be executed.
might have received less security attention.                          For the HTML context inside the anchor tag in injec-
   The main challenge in this scenario from the attacker’s per-    tion ❶, we first need to close that tag and then need
spective is that they have no information where their payloads     to insert an element that executes code, e.g., like this:
might end up, hence the name blind XSS. Without any feed-          </a><script>alert()</script>.1 On the other hand, the
back that allows them to identify the injection context in the     second injection context expects a URL ❷. While we could try
backend’s markup, dedicated XSS payload creation through           to break out of the surrounding quotation marks, this might not
means such as taint tracking is impossible. Even worse, only       be possible due to sanitization. One solution is to instead use
a successful attack provides information on the vulnerability
and allows to exfiltrate information about the backend. All           1 The dangling </a> will be ignored by the browser.




USENIX Association                                                                      33rd USENIX Security Symposium         6725
    a JavaScript URI, e.g., by supplying javascript:alert().            covering the entire state-of-the-art testbed. From a tester’s
    Finally, the injection context in JS code ❸ requires us to break    perspective, this results in less required tests and less system
    out of the quotes and close all expected parentheses to make        log noise. From a researcher’s view, it means less submissions
    sure that the code does not break, e.g., "){}alert();//. The        and thus less noise and reduced load for systems-under-test.
    two trailing slashes are important to comment out the rest of
    the line to avoid a syntax error.
                                                                        2.3    Research Questions
       For this simple example, we can still come up with
    a polyglot by carefully combining all three exploits                Constructing a set of powerful polyglots is key to the analysis
    by hand: javascript:alert()//"){}alert();//</a>                     of blind XSS, as it makes it possible to successfully trigger
    <script>alert()</script>. For case ❶, this just puts a              vulnerabilities without feedback. While previous work has
    lot of “garbage text” into the anchor text before closing the       focused on manually engineering polyglots [11, 27, 45], we
    tag and executing the script. For case ❷, this is interpreted as    argue that an automated process is inevitable here to han-
    a URI with valid JavaScript code and a long trailing comment.       dle the amount of injection contexts. This leads us to the
    Finally, for injection ❸, this puts the URI in the string, closes   following research questions that structure our work:
    the if-branch and executes our payload, while ignoring the
    rest due to the second // comment.                                  RQ1: Is it possible to automatically create a set of XSS poly-
       However, this polyglot just covers three contexts and there           glots that are capable of covering all common injection
    are a lot of variations where it would not work properly. For            contexts in combination?
    example, injection ❶ could also happen in the href attribute,       RQ2: Do these synthesized polyglots scale up to real-world
    with either single or double quotes, or might be inserted via            settings and how do they compare with existing XSS
    innerHTML where the script tags do not execute but event                 detection approaches?
    handlers do [49]. As another example, ❸ would result in a           RQ3: Can these polyglots be employed to perform a large-
    syntax error when the code has an else branch, as our inserted           scale analysis of blind XSS and indicate vulnerabilities
    alert would break the if-else construct. Covering all these              in web application backends?
    common variations of all contexts results in an explosion of
    possible combinations, making manual polyglot construction             To address these research questions, we conduct a series
    extremely tedious, if not impossible.                               of experiments: In Section 3, we introduce a method for syn-
                                                                        thesizing polyglots using concepts from game theory (RQ1).
1     //Read from a stored object without injection into the source     In Section 4, we assess the real-world performance of these
2     document.location = someObj.redirectLocation;                     polyglots, comparing them to traditional approaches (RQ2).
3     //Directly injected into the source code of a .js file
4     var foo = ❹;                                                      Finally, in Section 5, we perform a large-scale study to detect
                                                                        BXSS vulnerabilities in the wild (RQ3).

    Figure 3: Two injection contexts that are mutually exclusive,       3     Synthesizing Polyglots
    i.e., can not be solved by the same XSS polyglot.
                                                                        The generation of a polyglot is a challenging task. Unlike
       As an additional complication, some injection contexts are       attack payloads designed for a single environment, we are
    mutually exclusive. Figure 3 shows one example of such a            faced with multiple programming languages and contexts.
    case: The first injection context is only possible to solve by      Although a polyglot is basically just a string of characters,
    exploits starting with javascript: as such a JavaScript URI         conceptually it is a chimera made up of terminal symbols
    does not trigger an actual navigation, but instead executes         from different grammars. Some of these characters are even
    the subsequent code in the context of the current document.         ambiguous and only parsed correctly when the respective
    Starting with anything else will either fail, as escaping from      injection context is known. To cope with this complexity and
    the statement is impossible without a direct reflection into        ambiguity, we develop an automated approach that phrases
    the source code, or cause a navigation away from the website        the synthesis of a polyglot as a discrete optimization problem.
    that was the target of the attack. On the other hand, there         The objective is to find a string that maximizes the number of
    are also injection contexts that do not allow javascript:           exploitable injection contexts on a given testbed, regardless
    at the very beginning, e.g., the injection context in Figure 3      of the underlying languages and grammars.
    at position ❹, as the colon produces a syntax error on the             This optimization has several constraints: First, evaluating
    right side of the variable assignment. Illustrated by these two     a polyglot on the testbed involves running an entire browser,
    examples, mutually exclusive injection contexts thwart efforts      including HTML parser and JavaScript engine. Second, dur-
    to construct one universal XSS polyglot. On the other hand,         ing the polyglot evaluation, we receive only binary feedback
    full coverage could be achieved with one payload per context.       indicating success or failure, making gradient-based optimiza-
    However, we aim at creating a small set of polyglots while still    tion unfeasible. Lastly, as discussed in Section 2.2, some test



    6726    33rd USENIX Security Symposium                                                                        USENIX Association
cases are mutually exclusive. Therefore, we must identify a         of this reduction, MCTS omits moves that are impossible to
set of polyglots that collectively solve the testbed.               yield reasonable polyglots. The resulting token set consists
                                                                    of HTML literals, HTML tag names, HTML event handler
                                                                    content attribute, and other HTML tokens. The complete list
3.1    Monte Carlo Tree Search
                                                                    including the rules can be found in our companion repository.
Interestingly, the described optimization problem can be cast          Starting from an empty string, MCTS iteratively appends
into a game in which a player iteratively modifies a polyglot       tokens to it to expand the game tree and measure the poly-
to exploit as many contexts as possible. In this game, moves        glot’s reward. Unlike conventional games, however, this game
correspond to changes of the polyglot, while its reward is          has no clear end state, since polyglots can be arbitrary long.
determined by the number of exploited contexts. Different           We therefore set a fixed limit of 400 characters, after which
algorithms exist for solving such games, ranging from simple        we stop appending tokens to the polyglot. Since this fixed
search strategies to reinforcement learning [35].                   length condition might lead to superfluous tokens, we employ
   For our analysis, we focus on the concept of Monte Carlo         a minimization strategy afterwards (see Section 3.4).
tree search (MCTS) [6] that is known to find strong moves in           To evaluate a polyglot during search, we implement a fast,
round-based games, such as Chess and Go [38]. The genera-           manually created testbed covering 27 common XSS injec-
tion of polyglots, however, is agnostic to this algorithm and       tion contexts using Puppeteer (13.1.3) based on Chromium
thus we present a comparison of MCTS with other strategies          (98.0.4758.0). The complete testbed is included in our com-
for solving the underlying game in Appendix C.                      panion repository. In the regular MCTS backpropagation,
   Technically, MCTS simulates multiple games to conclusion         each polyglot would be assigned a score used to update the
to gather knowledge about promising game states. To keep            win counters on its path. Since we evaluate the polyglot on
track of the performance, MCTS constructs a game tree in            multiple test cases simultaneously, however, we receive a list
which each node corresponds to a polyglot and contains two          of scores on each playout. Instead of saving only one score,
attributes: a visit and a win counter. The algorithm explores a     we thus save the entire list and sum it up, once we need the
path in this tree using four steps:                                 total score wi for a particular node in the tree. As a result, we
                                                                    can keep track of the individual tests solved by a particular
  1. Selection: Starting from the root node of the game tree,       polyglot during construction. This gives us more flexibility:
     an unexplored child or the most-promising child node is        When some test cases have already been covered, we can
     selected until a leaf node is reached.                         exclude them from the score calculation in later runs.
  2. Expansion: If the selected leaf node is non-terminal, the         The final synthesis of one polyglot is shown in Algorithm 1:
     game tree is expanded by generating the child nodes of         Starting from the root node, we use MCTS to explore the
     the leaf node.                                                 game tree for N rounds until we fix the first move, i.e., select
  3. Playout: Starting from the leaf node, random nodes are         the first token of the polyglot. With the first token in place,
     explored until a terminal node is reached. This is equiva-     we repeat the process N times and select the second token.
     lent to performing random moves until the game ends.           We continuously start the game from a deeper root node until
  4. Backpropagation: On the path back to the root, the visit       the depth limit D is reached. At the end, the polyglot with the
     counter is incremented by one and the win counter is           highest score is returned.
     updated according to the result of the simulated game.
                                                                       Input: root, start node for generation
   During the selection phase, MCTS balances exploitation              Input: D, maximum depth of the root node
(selecting moves that were successful in the past) and explo-          Input: N, iterations until a move is chosen
                                                                       Output: polyglot string
ration (gathering knowledge about unexplored areas). √   To rank
                                                                     1 bestPolyglot, bestScore ← null, 0
each child i, we use the upper confidence bound wn i + 2 lnn Ni      2 for i ← 1 to D do
                                                                             for j ← 1 to N do
                                                      i        i
                                                                     3
where wi is the number of wins, ni is the number of visits and
                                                                     4            leaf ← select(root)
Ni is the number of visits of the parent node. If a child has not    5            expand(leaf)
been explored before, i.e., ni = 0, it takes precedence.             6            polyglot, score ← playout(leaf)
                                                                     7            backpropagate(leaf, score)
                                                                     8            if score > bestScore then
3.2    Synthesizing Polyglots with MCTS                              9                 bestScore, bestPolyglot ← score, polyglot
                                                                    10            end
To reduce the extensive search space, we incorporate expert         11       end
knowledge into the construction of the game tree: Instead           12       root ← choose_best(root)
                                                                    13 end
of operating on all characters, we generate polyglots only
                                                                    14 return bestPolyglot
from a set of tokens, such as < and script. We refine these
tokens with simple rules that prevent invalid combinations
                                                                                 Algorithm 1: Generating a polyglot
form appearing, such as svg appended to iframe. As a result



USENIX Association                                                                        33rd USENIX Security Symposium           6727
            D
            7                                                                                                                      46/111
            6                                                                                                                      31/111
 Polyglot




            5                                                                                                                      55/111
            4                                                                                                                      82/111
            3                                                                                                                      38/111
            2                                                                                                                      65/111
            1                                                                                                                      89/111
            *                                                                                                                      88/111

                1      10      20       30       40        50           60         70        80         90         100       110
                                                                Test cases

Figure 4: Composition of our minimal polyglot set solving all 111 test cases of our testbed. Squares (∎) indicates solved tests.
The top row (D) visualizes the overall difficulty of each test case, calculated from the total ratio of polyglots we generated that
solve this test i.e., difficult tests with fewer solutions are red (∎), while the color of more frequently solved tests gradually shifts
to yellow (∎). The numbered rows show the performance of our polyglot set. Diamonds (⧫) are placed instead of squares, where
only one polyglot in the set solves a test. For comparison, the bottom row (*) shows the performance of the Ultimate polyglot.


   At best, our approach would generate a single polyglot to             to select a minimal subset that solves all GFR test cases. We
“rule them all”, that is, solve all provided test cases. How-            build this minimal set by adding the polyglot to the set that
ever, our analysis reveals that depending on the test cases,             solves the most tests yet unsolved by the set, until no addi-
this might not be possible. For example, as discussed in Sec-            tional solutions can be added. Our final set of polyglots that
tion 2.2, some injection contexts are mutually exclusive and             is used in our study consists of 7 instances. Thus, we answer
a polyglot providing proper execution of JavaScript code in              RQ1 and show that it is possible to automatically create a
both cannot exist. As a remedy, we develop a strategy for                set of XSS polyglots that cover common injection contexts.
combining multiple polyglots into a set.                                 To compare the efficacy of our final polyglot set with a pub-
   In particular, after one polyglot is created, we remove the           licly available polyglot, we chose the best polyglot from the
test cases it solves and start over the search process of MCTS.          blog posts mentioned in Section 2.3—the Ultimate XSS Poly-
As result, by design, we seek a complementing polyglot that              glot [11]—as our reference. Now, to display the composition
focuses only on those cases the previous one cannot solve. We            of our polyglot set, Figure 4 visualizes our evaluation results
continue generating new polyglots using Algorithm 1, until               for each polyglot on the 111 test cases. We give an indication
all tests have been covered or a maximum number of tries is              of the difficulty of synthesizing a solution for each test by
reached. Finally, we obtain a set of polyglots that solves the           assigning a color to each of them. The number of polyglots
entire testbed of the synthesis process.                                 from our full set that successfully solve a test, determines
                                                                         its difficulty. Tests for which we synthesized fewer solutions
                                                                         tend to be more challenging and are depicted in red. In con-
3.3             Selecting a Final Polyglot Set                           trast, the color of easier tests, i.e., those with more solutions,
While we synthesize polyglots on a fast testbed, we use a                gradually shifts to yellow. The numbered rows below corre-
larger testbed to determine the quality of the generated poly-           spond to each polyglot of our final set, while the bottom row
glots. For this purpose, we set up a local instance of the               displays the Ultimate polyglot’s score. Indicated by diamond
Google Firing Range (GFR) [15], which is a state-of-the-                 symbols in the corresponding rows, each polyglot in the final
art XSS testbed [3]. We manually choose a subset of GFR                  set contributes at least one unique solution, e.g., polyglot 4
tests for our scope, based on the following criteria: First, we          is the only in the set solving test 36. The plot shows that
exclude non XSS-related test cases. Second, in cooperation               our polyglots cover all test cases, ranging from 31 to 89 tests
with Google, we obtain a list of GFR tests that have a known             covered by each individual polyglot. The Ultimate polyglot
solution which we manually confirm. We further exclude                   works surprisingly well and manages to cover 88 tests. How-
tests exceeding our scope, namely exploits relying on specific           ever, our automatic polyglot set creation outperforms manual
frameworks and those requiring a specific encoding. Tests that           engineering, as our generation process can target gaps left by
aggressively block special characters with an error page, e.g.,          previously synthesized polyglots.
any request that contains < or >, are also excluded. While solu-
tions for these tests exist, their solution needs to be so narrow        3.4    Minimizing Polyglots
that they are no longer a polyglot and thus also out-of-scope.
We confirmed all solutions and verified that an applicable solu-         Since our generation uses a termination criterion that sets a
tion exists for our requirements. A detailed list of the excluded        fixed minimum length for a polyglot, it is possible that some
tests and the specific reasons can be found in Appendix D.               tokens in the polyglot are superfluous. In general, this would
   After generating 4000 polyglots over multiple runs from               not constitute a problem, but some websites have length con-
different seeds, we utilize a greedy min-set cover approach              straints to the inputs in their backend. To make sure that



6728            33rd USENIX Security Symposium                                                                      USENIX Association
such obstacles do not obstruct our polyglots, we minimize          1     let d = document.getElementById("..");
                                                                   2     let href = decodeURIComponent(window.location.href);
the lengths of our final polyglots. The objective is to find       3     d.innerHTML = '<a href="' + href + '">';
the smallest polyglot with equivalent test results on the GFR
testbed. The minimization is done automatically and at token
level, i.e., we first deconstruct each polyglot into its tokens.             Figure 5: A typical Client-Side XSS vulnerability.
Since each token could be removed independently, there are
2N minimization candidates where N is the number of tokens
in the polyglot. Instead of testing all 2N options, we build our       potentially susceptible to CXSS it has the following informa-
minimization strategy on a single assumption: If removing              tion available: The source (here location.href), the sink
a token changes the test results, then all minimizations in            (here .innerHTML), what characters from the source ended
which that token is removed are invalid. Although there might          up in the sink, as well as the whole string entering the sink.
be edge cases, where this does not hold true, this drastically            With this information, the exploit generation strategy works
reduces the search space as we can first test each token sep-          as follows: The first step is to generate the so called break-
arately. Our polyglot minimization then involves iteratively           Out sequence, which aims to close the current context (here
removing combinations of tokens until no more tokens can               the double quoted href attribute) and put the parser into a
be removed without altering the evaluation result. Overall,            state where we can insert a XSS payload. Several HTML
in every polyglot (except for one), some unnecessary tokens            tags, such as iframe or textarea prevent code execution of
have been identified and removed. For the other polyglots we           their children. So the breakOut will close those tags as well.
achieve a reduction between 6% and 24%.                                Next, a context specific payload is generated, this is based on
                                                                       the sink function, as innerHTML requires a different payload
                                                                       than, e.g., eval(). The payload generated by the exploit gen-
4     Validation on Real-World Websites                                erator for innerHTML is <img src=x onerror=f()>. If this
                                                                       report function is called, we know that the generated exploit
While our test bed and the Google Firing Range cover a wide            was successful. However, with remaining markup from the
range of XSS vectors, they can only serve as an artificial eval-       original <a> tag, we must first create a breakIn sequence. Its
uation that is not necessarily representative of the polyglots’        purpose is to “consume” the leftover characters , ensuring the
ability to discover vulnerabilities in real-world code. Thus, in       parser proceeds without errors. While this step is usually un-
this chapter we set out to validate how well our XSS payloads          necessary in the HTML context due to the parser’s leniency, it
perform on actual websites with non-trivial codebases and              becomes critical in the JavaScript context. A suitable breakIn
to compare them to state-of-the-art techniques for detecting           would be to comment out the remainder of the document.
XSS that leverage targeted exploit generation.                            Finally, these three parts (breakOut, generated payload and
   More precisely, we evaluate our XSS polyglots on a set              breakIn) are concatenated and inserted into the URL at the
of recently found real-world client-side XSS (CXSS) vul-               appropriate position. For our running example, the insertion
nerabilities. CXSS has several advantages in the context of            point would be to simply append the generated exploit in the
our experiments: While exposing the same characteristics as            fragment of the URL. Therefore, and in contrast to our poly-
other classes of XSS, especially in respect to injection points        glots, each exploit generated with this approach is designed
and syntactical restrictions, it allows precise exploit payload        to work for one specific data flow on one website only.
generation, thanks to the availability of full data-flow infor-
mation [22, 26, 42] (see Sec. 4.1 for details). Furthermore,
research experiments utilizing CXSS offer the invaluable ben-          4.2    Validation Experiment Setup
efit that the complete exploitation attempt is conducted solely
                                                                       To compare the performance of different approaches on real-
on the client-side. Hence, potential negative side effects on
                                                                       world websites, we surveyed the top 10,000 domains accord-
the real world websites can reliably be prevented.
                                                                       ing to the Tranco list [20] as of Dec. 15, 2022, available at
                                                                       https://tranco-list.eu/list/W95V9. For each success-
4.1    Targeted XSS Exploit Generation                                 fully visited site, we queued up to 10 subpages, enabling us
                                                                       to capture vulnerable data flows that might not be apparent
As the baseline for the prevalence of CXSS vulnerabilities,            on the landing page. All relevant data flows for CXSS were
we re-use a state-of-the-art taint tracking engine [36] and the        stored in a database, and we concurrently visited the gener-
associated exploit generation by Bensalim et al. [4]. In the           ated exploit URLs to validate them. The exploit validation
following, we give a short overview of their approach, using           is done with legacy URL encoding, consistent with previous
the code in Figure 5 as an illustrative example throughout.            works [19, 22, 26, 41]. For each URL generated by the exploit
   In general, the idea is to browse the web with a modified           generator, we systematically replaced the targeted exploit with
taint browser while constantly monitoring and analyzing all            each of our 7 synthesized polyglots. Subsequently, we used
data flows. Once the taint browser detects a data flow that is         our crawler to visit these URLs, flagging the exploit as suc-



USENIX Association                                                                        33rd USENIX Security Symposium          6729
                                                                        contexts, they contain syntactic elements of several program-
                                                                        ming languages. Application code trying to parse the tainted
           Precise 18                                                   data can break, causing the vulnerable code paths to never
          Exploits                          Manual                      be executed at all. Take the polyglot from Section 2.2 as an
            (145)           109      18
                                            Polyglot
                                          8                             example. If data.split(':')[0] is called on it, it extracts
                                            (26)
                                                                        everything in front of the double colon, e.g., to retrieve a field
                                                                        from a complex data structure. For said polyglot this returns
                                     12                                 javascript, a harmless string. The precise exploit genera-
                                                                        tion never adds non HTML characters such as double colons,
                  Synthesized Polyglots (147)                           and as such its payload would be included in the extracted
                                                                        text.However, their rich syntactic structure is a positive in
Figure 6: Euler diagram of the performance of the three dif-
                                                                        other cases, because they are able to evade broken sanitizing
ferent XSS detection approaches on the Tranco Top-10,000.
                                                                        routines. One common mistake for input sanitization is mis-
                                                                        understanding the replace semantics and only replacing the
cessful if the callback function was triggered. To assess the           first occurrence of the needle by mistake according to Klein
effectiveness of our synthesized polyglots in comparison to             et al. [19]. Due to containing several code execution trig-
publicly available ones, we subjected the Ultimate XSS Poly-            gers, our polyglots are able to evade such a faulty sanitization
glot to the same treatment, like in Section 3.3. The Ultimate           routine whereas the generated exploit does not.
polyglot, like our polyglots, operated without the additional
                                                                    1       function read_href(url) {
information provided by the taint tracking browser, distin-         2         var div = window.document.createElement('div');
guishing it from precisely generated tainting exploits.             3         div.innerHTML = '<a href="' + url + '"></a>';
                                                                    4         return div.firstChild.href;
                                                                    5       }
                                                                    6       read_href(window.location.href); // somewhere else
4.3    Comparison of XSS Detection Rates
In total, we generated exploit URLs for 1010 of the visited
websites due to potentially security sensitive data flows. We           Figure 7: Problematic data flow not solved by our polyglots.
then applied each of the three approaches to see if they can
achieve JavaScript execution. Thereby, we were able to suc-               After demonstrating our polyglots’ exceptional perfor-
cessfully validate vulnerable data flows on a total of 165              mance in detecting CXSS flaws on real websites, we investi-
websites, resulting in XSS. Figure 6 depicts the results of             gate their suitability to discover blind XSS in the next section.
how our synthesized polyglots perform compared to both the
perfect-knowledge exploit generation strategy, as well as the
ultimate polyglot from prior work, thus answering RQ2. As
the figure shows, on 127 out of the 165 websites both our               5     Blind XSS in the Wild
polyglots and the exploit generation were successful. At the
same time, it also highlights that both approaches have their           So far, we have demonstrated how to synthesize polyglots
advantages as not a single one was able to discover all exploits.       and have found that their effectiveness in identifying reflected
However, the ultimate polyglot had the worst performance                XSS is comparable to existing approaches. In this section, we
by far, as it only worked on a fraction of the websites overall         design and conduct the first large-scale study of blind XSS
while not finding any additional exploits that were not already         in the wild. Our study is based on the synthesized polyglots.
covered by the other approaches.                                        Hence, it demonstrates their unique advantage in uncovering
   We then proceeded to manually investigated the successful            BXSS vulnerabilities. Additionally, we show the importance
exploits exclusively solved by either of the approaches. Ex-            of using a set of polyglots instead of a single one.
amples of data flows where the polyglots did not work as well              We are aware of our responsibility to conduct this study
as the generated exploits were highly specific edge cases such          in an ethical manner and, in accordance with the Menlo re-
as the one shown in Figure 7, the root cause behind 83% of              port [18], we designed it to prevent harm. Most importantly,
the websites where the polyglots were unsuccessful but the              if a polyglot should trigger, it will only connect back to in-
precise exploit generation succeeded. While this looks like a           form us about its execution. These benign tests allow us to
simple XSS vulnerability that the polyglots should be able to           measure the scope of the problem and warn website owners
solve, it is important to note that the dynamically created div         to close security vulnerabilities before they can be exploited.
is never added to the DOM. This prevents triggers that rely             We consulted our funding project’s institutional review board
on the onload event handler to fire. Another reason for the             (IRB) which concluded that the potential gain for system secu-
polyglots failing to trigger results from the general concept           rity predominates potential extra work for website operators.
of a polyglot (see Section 2.2). To be valid code in several            Further technical details are found in Section 5.4.



6730    33rd USENIX Security Symposium                                                                               USENIX Association
5.1    Polyglot Preparation and Monitoring                          5.2    Polyglot Transmission
                                                                    There are three general ways to transmit our synthesized poly-
A polyglot triggers all vulnerabilities it can cover. However,      glots to the websites we visit, where they can get passed to
due to the nature of blind XSS we cannot directly observe           backend systems: headers, URLs, and forms. In the following,
when this happens in a backend. Hence, we design the poly-          we will briefly outline considerations for each of them.
glots to notify our monitoring server if they are executed due      HTTP Headers. To test backend logging applications, we
to a vulnerability. We outsource this notification mechanism        submit polyglots in four request headers. The Referer header,
into a remote notification script instead of embedding the          often containing the previously visited URL, is valuable
required functionality into the polyglots for multiple reasons.     for analytics and tracking [24]. Similarly, the User-Agent
To begin with, using a replaceable remote script makes poly-        header aids analytics, by revealing browser and platform us-
glot synthesis easier, as we only have to optimize on import        age patterns. Polyglots in the Cookie header may get logged
mechanisms as our polyglots’ core functionality. Addition-          for failed authentication. Additionally, we utilize the less-
ally, testing is sped up, as the imported code can be easily        known Warning header, particularly warning code 199, used
replaced without syntactically changing the polyglots. In con-      to transmit loggable information [25]. Despite its deprecation,
trast, embedding the required notification functionality would      all major browsers still support it. We employ HTTP GET
introduce additional characters to the polyglots which would        requests to transmit each header, embedding the polyglots
increase their length and extend the required character set         as either direct values or in suitable contexts like Cookie:
which in turn may trigger additional input filters potentially      test=<polyglot>. To identify which header triggers feed-
reducing the polyglots effectiveness in the field. Finally, using   back, we individually send each polyglot ro the landing pages
a remote script enables us to render polyglots ineffective by       via a GET request for each header mentioned.
stopping to serve the notification script, e.g., once the study
concludes after a certain period.                                   HTTP URLs. Similarly to headers, URL submissions via
                                                                    the query and path are issued for each website with each
   To achieve traceability from polyglot submission to indi-        polyglot. For every landing page visit, we append an ar-
vidual vulnerabilities we assign each submission a unique           tificial subpath, followed by the polyglot as another sub-
12-character ID. This ID encodes how (URL, form, or                 path, e.g., http(s)://domain.com/<path>/<polyglot>.
header) which polyglot was submitted to and on what                 Analogically, in query submission, we employ an arti-
(backend) page it ended up being executed. This ID is               ficial query key with the polyglot as its value, e.g.,
embedded in the URL a polyglot’s import functionality               http(s)://domain.com?<query>=<polyglot>. We use
takes, e.g., JavaScript import statements or the src at-            artificial paths and query keys, because our goal is not to
tributes. Exemplarily, a polyglot requests the notification         find reflected and stored XSS flaws in existing functionality.
script from our monitoring server upon execution, e.g., via         Instead, our aim is to transmit our payloads to web-based
import('https://<ID>.<monitor_host>/s.js'). The                     backend systems with potential blind XSS vulnerabilities.
monitoring server can then extract the ID from the requested        Moreover, we perform this action only once on the landing
script’s URL and embed it into the notification script before       page, avoiding excessive warnings for website operators.
returning it. The script in turn includes this ID in the feedback
ping it returns back to our monitoring server when executed.        HTML Forms. Finally, we also analyze the HTML code
Using this submission ID, a backend vulnerability can be            for each page that we visit and extract all contained HTML
linked to a specific submission on a particular website.            forms. For each form, we first check if the allowed length of
                                                                    each input given by the maxlength attribute is enough for
                                                                    our longest polyglot. Moreover, we have measures in place
                                                                    to prevent duplicate form submissions. On par with previous
                                                                    work [28], a form is considered new if at least one value
Notification Script The notification script (Appendix A)            differs from previous forms: (a) its innerHTML representation
returns information required for accurate detection and effec-      (excluding default values and whitespace), or (b) the form’s
tive disclosure of a blind XSS vulnerability. When executed,        target domain. For all the remaining unique forms, we fill all
the script returns the document’s title, its URL, excluding         inputs with one polyglot at a time and submit the form.
query and fragment, as well as the JavaScript user agent and
platform. It encodes the information, the submission ID, and        5.3    Identifying Blind XSS
the current timestamp in the URL of an HTTP request bound
to our monitoring server. Upon receipt of such a request, we        Generally, we expect a mix of automated business logic tools,
indirectly receive the IP address of the sender, which we re-       and manually operated monitoring and administration plat-
quire for the disclosure process. Section 5.4 further discusses     forms to trigger our polyglots. The former may react to our
the usage and implications of the collected data.                   submissions instantly, while the latter may be bound to human



USENIX Association                                                                    33rd USENIX Security Symposium         6731
interaction and thus only trigger sporadically. Therefore, we       of real-world backends poses challenges, often necessitating
give each submission a time frame of 2 months during which          insights from active operators on their particular setups.
we monitor it. In the following, we explain our approach to            Real-world studies, especially a small-scale study with
confirm that triggered polyglots are of the blind XSS type.         prior operator consent, emerge as another solution, allowing
   We define three cascading filter steps to narrow down our        operators to take precautionary measures to minimize harm.
findings to blind XSS and thus discarding reflected and stored      Given the—at the time of our study—unknown prevalence of
XSS on the way: (1) Feedback pings have to come from an IP          BXSS and indications of its rarity [2, 8, 13, 34], we decided to
address different to our crawler’s IP, otherwise we triggered a     discard this study design. However, an appropriate selection
reflected XSS. (2) The URL where we submitted our polyglot          of operators might provide representative results.
has to differ from the URL where it triggers, otherwise we             We chose the final option, conducting a large-scale study
found a trivial stored XSS where the attacker could have            of the top-ranked website without acquiring operator consent.
adjusted their payload in this non-blind setting. (3) The URL       While offering a direct and unbiased approach to a repre-
where the polyglot triggers may not be publicly accessible,         sentative analysis of the subject, it is important to note that
only then we have discovered a blind XSS vulnerability with         this strategy is ethically problematic, even if tests are ex-
no way for the attacker to learn about the injection context.       tremely carefully designed. We remark that the other alter-
Otherwise, we found a non-trivial stored XSS, where the two         natives would also be applicable with different compromises
URLs differ and their connection needs to be discovered first,      between ethical implications and gained insights. In general,
but both are nevertheless publicly available.                       we recommend thoroughly considering different study de-
   To test this, our monitoring server initiates an additional      signs and additionally engaging with an IRB upfront. Thus
confirmation step for each newly reported BXSS candidate            far, our study has incurred no reported damages or problems,
URI immediately after receiving a feedback ping. In this            attesting to the effectiveness of our design in preventing harm.
step, the server conducts an extra visit to the reported URI        Our results revealed 20 vulnerabilities among the top 100,000
to assess its public accessibility. At this stage, our filter (3)   websites underlining our initial assumption of the rarity of
confirms invalid or local URIs, as well as private IP addresses     BXSS. Nonetheless, it is imperative to stress that any retro-
as BXSS instances where our polyglot reached and executed           spective analysis does clearly not provide justification for the
in a backend system. However, even if the page did load,            decisions made in a study.
some cases may still qualify as BXSS. For instance, we en-             It is crucial to highlight that conducting studies without
countered public pages that required authentication to access       proper consent or assuming consent from non-responsive par-
their content. Since the identification of login pages is hard to   ties is not ethically sound. Our research should thus not be
automate [9, 17], we manually investigated and labeled these        viewed as a template for similar studies. Based on our discus-
websites as either BXSS or false positives.                         sions with the IRB, we believe that our work represents a good
                                                                    compromise in this regard. However, we acknowledge that
                                                                    alternative study designs could have been employed to miti-
5.4    Ethical Considerations                                       gate the risk of harm more effectively, though at a higher risk
Conducting server-side studies requires careful ethical con-        of reduced insights. Scientific work often navigates complex
sideration. To this end, we followed best practices outlined        terrains, demanding thoughtful balancing of conflicting inter-
in the Menlo report [18], and aimed at uncovering real-world        ests. We selected—to the best of our knowledge and belief—a
BXSS scenarios while ensuring minimal impact on operators           suitable balance, which is certainly not without debate.
and users. We decided on a large-scale study without the op-
erators’ consent. This is a difficult and controversial decision    Side effects. All test requests contain minimal JavaScript
that requires a thorough investigation of the potential harms       payloads that do not affect the global namespace of the sur-
and risks. We discussed this decision in detail with our IRB        rounding application ensuring that no unintended side effects
and received approval. Nevertheless, we recognize the weight        on legitimate code occur. In the rare cases where the ini-
of this decision and the potential for alternative options, the     tial polyglot succeeds, a second script is retrieved from our
advantages and disadvantages of which we discuss below.             servers for data collection. This two-step process enables us
                                                                    to deactivate the notification script for specific IDs or entirely
Alternative study designs. Auditing open-source appli-              at any time, serving as an additional mitigation strategy.
cations for BXSS vulnerabilities offers a first choice. This           As a result, a test polyglot can only trigger on vulnerable
method comes with no ethical issues but its results are limited     pages, ensuring that non-vulnerable web applications, which
by the proprietary nature of production code and the unpre-         constitute the vast majority, receive only the polyglot without
dictable configurations of live websites.                           any unintended behavior or side effects. However, for vulner-
   Analyzing simulated backends in a lab environment of-            able websites, a notification function is essential to initiate
fers another choice. While ethically unproblematic within           disclosure to the affected parties and improve their security.
a confined environment, accurately mirroring the nuances            Otherwise, our blind XSS tests would remain “blind”.



6732    33rd USENIX Security Symposium                                                                         USENIX Association
Information collected. In alignment with user privacy our          as the vulnerability could have its root cause in a commonly
notification script (Section 5.1) only returns information that    used software component.
we use for accurate recognition and effective reporting of             We recognize that our data collection methods, though
blind XSS executions in backends. We verify instances of           designed with great care, are not without the risk of inad-
BXSS using the IP address and partial backend URL. As part         vertently capturing sensitive information in certain parts of
of the disclosure process, we can provide operators with both      our collected data. Specifically, titles and paths of websites
pieces of information, plus the user agent and platform strings.   could, in theory, contain credentials, authentication tokens, or
The user agent information offers operators an advantage in        other confidential data. It is widely recognized in the field of
assessing the potential impact of our reported vulnerability,      web development and design that embedding personal data in
as they help to distinguish between manual and automated           these fields is untypical and against best practices [cf. 32, 33].
operations. Finally, we utilize the backend path in conjunc-       Nonetheless, this remains a significant concern.
tion with the page’s title as indicators of shared root-cause          Our decision to collect this data was driven by the intent to
components, allowing us to additionally report our findings        notify operators of vulnerabilities in their systems, a necessary
directly to the developers of these components.                    step we believed was essential for our study. We recognize
                                                                   the potential pitfalls and admit that a more privacy-centered
Candidate selection. In our candidate selection process,           strategy could have been employed.
we adhere to the “fairness” principle outlined in the Menlo
                                                                       Our large-scale study was conducted without requesting
report by considering the top 100k Tranco domains. With
                                                                   consent. However, we could sometimes obtain informed con-
focus solely on blind XSS, we use a canary test to filter out
                                                                   sent for certain aspects of the study. Inspired by Utz et al. [46],
websites, like guest books, that mirror user inputs, avoiding
                                                                   we suggest an alternative approach for future research. In de-
stored and reflected XSS triggers. This test populates new
                                                                   tail, we could have abstained from collecting the backend’s
forms with random tokens, subsequently checking the HTTP
                                                                   title and path in our initial vulnerability tests. Then during
response and page’s HTML for them. To reduce load on
                                                                   the vulnerability disclosure, where we anticipated a limited
targets, we test each site’s functionality only once, ensuring
                                                                   but uncertain number of affected websites, we could have
unique submissions by checking for existing duplicate header,
                                                                   procured further information from them. If successful, we
URL, or form submissions, detailed in Section 5.2.
                                                                   could obtain permission to gather additional data, i.e., website
Transparency. For transparency and to facilitate an opt-out        titles, in a follow-up experiment, or directly ask about the uti-
procedure, our monitoring host offers information. Our noti-       lized software components. Such a two-fold approach would
fication script’s URLs’ landing page details the project, the      have enabled us to obtain informed consent from vulnerable
data we collect, and contact information for potential with-       entities while still learning about shared components.
drawal from the study. Through this channel we received two            Yet, this method is not without flaws. Our study found
notifications from one Internet services company regarding         a generally limited response rate, consistent with prior re-
suspicious traffic from our IP. We addressed this by excluding     search [44]. Hence, this approach poses the risk of missing
the respective domains from subsequent visits.                     insights into shared root causes if no responses are received.
   Though informing thousands of operators in advance is not       Nevertheless, future research might explore and evaluate this
scalable, we ensured a vulnerability notification was sent to      approach to determine its suitability in different contexts.
the technical contacts of all affected websites. This ensures
that the underlying defects are fixed and thus exploitation        5.5    Large-Scale Crawling Study
is no longer possible. Consequently, our study’s benefits in
improving website security outweigh potential negatives, like      To answer our last research question from Section 2.3 (RQ3),
polyglots causing a manual investigation.                          we perform a large-scale study on the top 100,000 domains
                                                                   according to the Tranco list [20] as of Oct. 9, 2022, available at
Design implications. Although these ethical measures can-          https://tranco-list.eu/list/824JV. We use a crawler
not completely eliminate the risk of a polyglot leading to a       based on the Chrome DevTools Protocol [12] to instrument
technical failure on one of the websites, we argue that the        Chromium 105.0.5195.102 in headless mode. For websites
gained insights about blind XSS and the notification of all        permitted by their robots.txt, our crawler explores same-site
affected sites jointly outweigh this risk and make our study a     and listed-domain links up to a depth of 5 or 30 subpages per
valuable contribution for improving web security.                  root domain, with random link selection when needed. Each
  When designing our methodology, we chose to directly             page receives a 60s load window; failure leads to flagging, and
collect paths and titles to identify shared root-cause compo-      the crawler proceeds to another page. Dynamic pages receive
nents. For instance, Table 1 indicates a common tool shared        3 seconds post-load event for pending network requests.
by backends D and F, discerned through paths. Backends B, D           We conducted our study over the course of 20 days using
and F even explicitly mention such a tool’s name in their title.   60 parallel crawler instances on Ubuntu 20.04.5 LTS. Our
We used that information to inform the respective vendors,         monitoring was online during this time to allow observing



USENIX Association                                                                    33rd USENIX Security Symposium           6733
each submission for at least 2 months. Of the 1,676,812 vis-        the polyglots submitted to these websites. In all three cases,
ited pages, approximately 7.4% failed to load. Regarding the        our notification script triggered in online web tools with no
failures, about 56.1% returned an HTTP error status code.           apparent relation to the website we tested, so we refer to this
22.7% of errors can be attributed to network or DNS resolu-         class of findings as 3rd -party XSS. In each case, the submitted
tion errors. Further 15.7% of aborted pages tried redirecting       headers were posted to evidently vulnerable online tools hours
outside of the top 100k domains, which we consider out of           to days after we sent our submissions. These tools include an
scope, or to an previously visited domain.The remaining 5.5%        online user-agent parser, an online XML editor and beautifier
are various errors e.g., timeouts when loading the page.            tool, as well as an online URL decoder / encoder. We man-
   Our ethical considerations regarding deduplication and ca-       ually confirmed the three reflected XSS vulnerabilities and
nary reduced the amount of HTML forms used for submitting           excluded them from our blind XSS results.
our polyglots. Collectively, these measures halved the amount          We disclosed our findings with all affected parties, includ-
of candidate forms, leaving 46.54% of identified candidates.        ing the previously mentioned 3rd -party web tools. Subse-
After respecting each input’s given maxlength attribute, we         quently, we received responses in about 19% of the cases,
submitted a total of 170k forms, along with around 1.9M             surpassing the access-rate reported in a recent notification
header and 954k URL submissions, equally distributed be-            study [44]. Notably, the responses we received were entirely
tween query and path submissions.                                   positive, with all respondents showing an effort to fix the issue
                                                                    we brought to their attention. Moreover, we were approached
5.6    Uncovered BXSS Vulnerabilities                               by two parties requesting us to retest their fixed website, em-
                                                                    phasizing the need for blind XSS testing strategies.
Our submissions triggered 20 different BXSS vulnerabilities
on 18 websites. In this section, we present our findings and        Backend Details. At this point, we discovered 18 vulnera-
discuss the uncovered blind XSS cases. Moreover, we also            ble backends. Table 1 aggregates the BXSS vulnerabilities we
discuss the efficacy of our polyglots and probing mechanisms.       uncovered, showing that our findings represent websites from
Vulnerable Backends. Regarding the given time frame and             a wide variety of Tranco ranks, popular and less popular. To
considering our initial filter (1) from Section 5.3, we received    preserve anonymity, we pseudonymized each domain in the
feedback pings from 28 unique domains. After discarding             table and shortened path and title for brevity. In many cases,
stored XSS candidates with the second filter (2), we are left       the combination of path and title are sufficient to derive the
with 21 potential backend domains. Of these 21 candidates,          backend tools’ purposes: We observe a mix of administration
the automated part of our final filter (3) confirmed 8 of them      tools for maintenance, management, and monitoring, as well
to be internal websites and thus BXSS, as their URLs were           as tools for infrastructure or business logic. In three instances,
unreachable e.g., because they were either private IPs, file        B, D, and F, a platform name could be directly derived from
URIs, local resources, or dotless hostnames [16]. Manual in-        the document title. In the first case, we discovered an inter-
vestigation of the remaining 13 reachable URLs confirmed            nal deployment of the frequently used log monitoring and
that 10 of them show clear signs of blind XSS: For once, 6          reporting platform Splunk 8.2.3 and its official utility app
of them were login-protected pages requiring credentials or         Lookup Editor with our polyglots. The other two turned out to
session cookies. Another case was a web interface for a local       be NetWitness Platform, a popular security information and
Web Socket server that doubles as an informative website if         event management tool. We contacted both vendors to share
no connection to the Web Socket port can be established, so         details of our findings. Similar paths and titles indicate that
our crawler flagged it as a public website. Interestingly, the      the same software is used in the respective backends of two
remaining 3 confirmed candidates are, to our understanding,         website pairs: D, F and I, K. While the sites do not necessarily
erroneously publicly available backend pages. Strong indica-        have to be connected, the location derived from their pings’
tors that the pages’ availability is unintended are on the one      IP addresses indicate proximity in both cases.
hand that they make protection-worthy data publicly avail-
able, including other visitors’ IP addresses and headers, and       BXSS Vulnerabilities. We count the backends based on the
on the other hand that their parent pages are in contrast access-   number of affected websites. Since one backend can poten-
protected. Ultimately, we count these 10 discussed findings         tially have multiple BXSS vulnerabilities, we further distin-
towards blind XSS, resulting in a total of 18 BXSS-vulnerable       guish between data flows originating from header, URL, and
websites. This demonstrates the polyglots’ proficiency at un-       forms. Figure 8 illustrates which submission type discovered
covering blind XSS vulnerabilities in the backends of real          which backend. When looking at the three groups—URL,
websites, thus answering RQ3.                                       header, and form submissions—the majority (89%) of the
   The remaining three candidates were manually excluded            backends were triggered by only one submission type. Since
and labeled as not in scope for BXSS, because the tested web-       the two remaining backends we discovered, I and L, were
site and its backend themselves were not vulnerable to our          triggered by both URL and header submissions, we count a
submissions, yet, we received feedback pings attributable to        total of 20 blind XSS vulnerabilities on 18 websites.



6734    33rd USENIX Security Symposium                                                                         USENIX Association
                         Table 1: BXSS Findings—the 18 backends with the corresponding website’s rank, shortened path and title.

    Rank                  Backend   Backend Path                                                            Backend Title
  90–100k                 A    ⊖    /admin/index.php                                                        "Welcome to service maintenance, admin!"(*)
   10–20k                 B    ⊖    /ja-JP/app/lookup_editor/lookup_edit                                    "Lookup Edit | Splunk 8.2.3"
   40–50k                 C    ◯    /intranet/tmp/integrity-BL-KILL.html
  90–100k                 D    ×    /investigate/events                                                     "Investigate - NetWitness Platform"
   30–40k                 E    ×    /last_one_day_-_blocked_events-_[timestamp].csv.html
   60–70k                 F    ×    /investigate/events                                                     "Investigate - NetWitness Platform"
   40–50k                 G    ⊖    /global_administrator.aspx                                              "Administrator"
   20–30k                 H    ×    /ajax/tst.php
    0–10k                 I    ×    /alabama_daily_blocks_harding__sa.[timestamp].csv.html
  90–100k                 J    ◯    /pagestats/toonstats.php
  90–100k                 K    ×    /alabama_daily_blocks_harding__sa.[timestamp].csv.html
   60–70k                 L    ⊖    /admin_area/visit/v2.php                                                "Visitor Status - Daily Visitor Search | vista"(*)
   80–90k                 M    ◯    /                                                                       "Simple WebSocket Server – GWSocket"
  90–100k                 N    ⊖    /0xu_x_admin/user_getip.asp                                             "China News Encyclopedia background management"(*)
   70–80k                 O    ⊖    /_admin/count/ip_count.asp                                              "Access Statistics"(*)
   50–60k                 P    ◯    /recent-referrers/                                                      "Referrers from past 2 days – [site]"
   60–70k                 Q    ×    blank
   70–80k                 R    ×    /llurl_fetcher_data/f78a3c[ ... ]042f01.html
◯ Backend URI is publicly available.                 ⊖ Backend URI is public, but requires authentication.               × Backend URI is unreachable.         (*) Title translated.


Submission Triggers. Generally speaking, we observed re-                                   amount of form submissions we sent compared to headers and
action times from submission to feedback ping ranging from a                               URLs, as well as forms being an expected input vector that
few seconds for automatic processes up to 10 days for human                                may have received more attention regarding sanitization and
interaction, with a median of around 6 hours. Regarding the                                encoding of data flowing into backends. Despite being the
geo location of machines where our polyglots triggered, we                                 commonly used attack vector [4, 19, 22, 26, 42, 43], URLs
received pings from IP addresses across the world, namely                                  still overperform as delivery type for BXSS payloads.
Asia, Europe, America, and Africa.
                                                                                           Polyglot Performance. As highlighted in Section 4.3, man-
                                                                                  1        ually created polyglots may excel in a controlled lab envi-
                t r e
   rm ery ath en re ki




                                                                             6             ronment but not necessarily demonstrate comparable perfor-
 Fo u P -Ag efeCoo




                                                             4                             mance in a real-world setting. Figure 9 displays the efficacy
                                                                       Header (10)
          r R




                                                 7
                                                             4
                                                                       URL (9)             of our seven polyglots in discovering blind XSS vulnerabil-
        se




                                                                       Form (1)
      U




                            1                                                              ities. It shows that all polyglots contributed to our study’s
    Q




                         A B C D E F G H I J K L M N O P Q R                               findings, with more than half of them exclusively triggering
                                  BXSS-vulnerable backends (18)                            certain individual vulnerabilities. Thus, justifying our divide-
                                                                                           and-conquer approach based on complementing polyglots.
Figure 8: Submission types that caused a polyglot to execute                               Overall, polyglot 4 was most successful regarding the number
in one of the 18 vulnerable backends.                                                      of backends triggered, as well as in the number of backends
                                                                                           that only polyglot 4 was able to trigger, followed by polyglot
   Next, we further investigate each submission type in Fig-
                                                                                           1, and 7 as the top-performing polyglots. Looking back at
ure 8. When distinguishing between query and path submis-
                                                                                           Figure 4 it is interesting to see that the polyglot that was most
sions, we found two cases (C and D) where both types trig-
                                                                                           successful in the wild is not our best on the GFR. Overall, this
gered in a backend. To clarify, we do not count these as sep-
                                                                                           both highlights the need for a set of polyglots, as well as the
arate vulnerabilities, since these likely follow the same data
                                                                                           need for a real-world evaluation in the wild.
flow. Interestingly, most other URL submissions that trig-
gered blind XSS were due to polyglots embedded in the path.
                                                                                                        1                                                          10
The three headers mainly triggered the respective backend                                               2                                            7
                                                                                             Polyglot




                                                                                                        3                          4
alone, with the Referer header as the most common trigger.                                              4                                                                       12
Finally, in only one specific case (L), BXSS in a backend was                                           5                                      6
                                                                                                        6                                      6              Header      Form
triggered by query, User-Agent, and Referer simultaneously.                                             7                                                 8   URL         Sole trig.


   Moreover, the figure also shows that HTTP header submis-                                                 0        2         4             6            8      10          12
                                                                                                                                       # Backends triggered
sions, with 10 cases, uncovered the most BXSS vulnerabil-
ities, followed by URL submissions with 9 vulnerabilities.
Notably, forms triggered the least BXSS instances with only                                Figure 9: Backends triggered by the submission types.
one occurrence. Potential reasons for this might be the lower                              Hatched vulnerabilities were only triggered by one polyglot.



USENIX Association                                                                                                         33rd USENIX Security Symposium                     6735
6   Related Work                                                    to the Ultimate polyglot. This led us to not further pursue
                                                                    this method. Ultimately, these blog posts lack systematic eval-
In the following, we discuss how publications in the area of        uation of their polyglots and, to the best of our knowledge,
XSS detection and polyglots relate to our work.                     none of the previous publications studied the application of
   Stored XSS. While reflected XSS has been extensively stud-       polyglots in the context of blind XSS vulnerability detection.
ied by prior work [e.g. 4, 19, 22, 26, 39, 40, 42, 43], few tried
to tackle the detection of stored XSS dynamically, i.e., without
access to the server-side source code. In 2014, Duchene et al.      7   Conclusion
[10] presented KameleonFuzz, a technique to fuzz web ap-
plications guided by a genetic algorithm and a taint tracking
                                                                    Our analysis sheds light on a web security problem that has
engine. In 2015, Parvez et al. [34] analyzed the effective-
                                                                    stayed in the dark, so far. While detecting and preventing XSS
ness of black-box web application scanners to detect stored
                                                                    vulnerabilities in front end code has been a prime topic of
vulnerabilities and found that while outperforming previous
                                                                    research, little attention has been paid to analyzing these is-
scanners [2, 8], the overall detection capabilities were still
                                                                    sues in backends, largely due to a lack of appropriate tools for
quite lacking at that time. Later in 2019, Steffens et al. [41]
                                                                    blind security testing. Our approach to synthesizing polyglots
expanded taint tracking techniques to also find Stored Client-
                                                                    fills this gap and provides the basis for the first large-scale
Side XSS vulnerabilities, i.e., flows from Web Storage and
                                                                    study of XSS vulnerabilities in backend code in the Web.
cookies to dangerous sinks. Moreover, Eriksson et al. [13] pre-
sented BlackWidow in 2021, which can discover intra-page                The generation of polyglots, however, is not only a tool
dependencies during black-box crawling and thus uncover             for research. Our synthesis approach is flexible. It can be nar-
Stored Server-Side XSS vulnerabilities.                             rowed down to specific vulnerabilities as well as expanded
   ML and XSS. Recently, the use of machine learning (ML),          by supplementing additional test cases. As a result, it pro-
particularly reinforcement learning (RL), has gained traction       vides a new and versatile instrument for web security that
in aiding XSS vulnerability detection. In 2021, Caturano et al.     cannot only help investigate public-to-internal flows in back-
[7] demonstrated RL’s utility in assisting human penetration        ends but ultimately serve as a “Swiss-army-knife” for general
testers in uncovering reflected XSS vulnerabilities. In 2022,       vulnerability assessment of web applications.
Lee et al. [21] introduced a fully automatic RL approach, al-
beit limited to reflected XSS. Additionally, Foley and Maffeis
[14] applied hierarchical RL to generate XSS payloads that          Acknowledgments
evade the current context and bypass sanitization.
   In summary, the dynamic XSS detection approaches dis-            We thank our shepherd and the anonymous reviewers for their
cussed earlier share common characteristics. They either rely       valuable suggestions and comments on this paper. Further-
on full information, employing taint tracking, are limited to       more, we would like to thank Tobias Jost, Vladislav Mladenov,
Client-side XSS, or require traversing the whole web applica-       and the remaining NDS team at Ruhr-Universität Bochum
tion to identify intra-page dependencies relying on a feedback      for their technical support, as well as Sebastian Lekies for his
loop to guide exploitation. In contrast, our polyglot-based ap-     support with the GFR, and Angela Sasse for her guidance in
proach can detect vulnerabilities blindly, without prior knowl-     our study design. We gratefully acknowledge funding by the
edge or direct interactions with the vulnerable page.               Deutsche Forschungsgemeinschaft (DFG, German Research
   XSS Polyglots. Some earlier work has also explored the           Foundation) under Germany’s Excellence Strategy – EXC
application of polyglots and related techniques in the web          2092 CASA – 390781972, the German Federal Ministry of
context. In 2009, Barth et al. [1] presented a PDF chameleon,       Education and Research (BMBF) under the project IVAN
which is a PostScript document that also contains some              (16KIS1168), the European Research Council (ERC) under
HTML, that led to XSS due to the browser’s content sniff-           the consolidator grant MALFOY (101043410) as well as from
ing algorithm. In 2013, Magazinius et al. [23] generalized          the European Union’s Horizon 2020 research and innovation
previous attacks such as the chameleon and the GIFAR [5]            programme under project TESTABLE, grant agreement No
attack under the term polyglot, and presented further attacks       101019206.
using PDF polyglots along with a small-scale study on 100
websites. Additionally, various blog posts regarding universal
XSS polyglots exist [11, 27, 45]. High performance of the
manually created Ultimate polyglot [11] on the GFR led us           Availability
to include it in our baseline (see Figure 4). Mutation-based
genetic algorithms [27] constitute an interesting generation        We have made our code publicly available in our companion
approach. However, initial experiments showed subpar results        GitHub repository at https://github.com/polyxss/bxss,
of the published polyglots in respect to the GFR compared           encouraging further research on polyglot synthesis.



6736    33rd USENIX Security Symposium                                                                       USENIX Association
References                                                                      [16] ICANN Security and Stability Advisory Committee. Report on Dotless
                                                                                     Domains. Technical report, SSAC, 2012.
 [1] Adam Barth, Juan Caballero, and Dawn Song. Secure Content Sniffing
     for Web Browsers, or how to stop papers from reviewing themselves.         [17] Hugo Jonker, Stefan Karsch, Benjamin Krumnow, and Marc Sleegers.
     In Proc. of IEEE Symposium on Security and Privacy, 2009.                       Shepherd: A Generic Approach to Automating Website Login. In
                                                                                     Proc. of Workshop on Measurements, Attacks, and Defenses for the
 [2] Jason Bau, Elie Bursztein, Divij Gupta, and John Mitchell. State of             Web (MADWeb), 2020.
     the art: Automated black-box web application vulnerability testing. In
     Proc. of IEEE Symposium on Security and Privacy, 2010.                     [18] Erin Kenneally and David Dittrich. The Menlo report: Ethical Princi-
                                                                                     ples Guiding Information and Communication Technology Research.
 [3] Enrico Bazzoli, Claudio Criscione, Federico Maggi, and Stefano                  Technical report, U.S. Department of Homeland Security, 2012.
     Zanero. XSS PEEKER: Dissecting the XSS exploitation techniques
     and fuzzing mechanisms of blackbox web application scanners. In ICT        [19] David Klein, Thomas Barber, Souphiane Bensalim, Ben Stock, and
     Systems Security and Privacy Protection, 2016.                                  Martin Johns. Hand sanitizers in the wild: A large-scale study of
                                                                                     custom javascript sanitizer functions. In Proc. of IEEE European
 [4] Souphiane Bensalim, David Klein, Thomas Barber, and Martin Johns.               Symposium on Security and Privacy (EuroS&P), 2022.
     Talking about my generation: Targeted DOM-based XSS exploit gener-
     ation using dynamic data flow analysis. In Proc. of European Workshop      [20] Victor Le Pochat, Tom Van Goethem, Samaneh Tajalizadehkhoob, Ma-
     on System Security (EUROSEC), 2021.                                             ciej Korczyński, and Wouter Joosen. Tranco: A research-oriented top
                                                                                     sites ranking hardened against manipulation. In Proc. of Network and
 [5] Ron Brandis. Exploring below the surface of the GIFAR Iceberg. an               Distributed System Security Symposium (NDSS), 2019.
     EWA Australia information security whitepaper. Electronic Warfare
     Associates-Australia, 2009.                                                [21] Soyoung Lee, Seongil Wi, and Sooel Son. Link: Black-box detection
                                                                                     of cross-site scripting vulnerabilities using reinforcement learning. In
 [6] Cameron B. Browne, Edward Powley, Daniel Whitehouse, Simon M.                   Proc. of the International World Wide Web Conference (WWW), 2022.
     Lucas, Peter I. Cowling, Philipp Rohlfshagen, Stephen Tavener, Diego
     Perez, Spyridon Samothrakis, and Simon Colton. A Survey of Monte           [22] Sebastian Lekies, Ben Stock, and Martin Johns. 25 Million Flows
     Carlo Tree Search Methods. In IEEE Transactions on Computational                Later: Large-scale detection of DOM-based XSS. In Proc. of ACM
     Intelligence and AI in Games (T-CIAIG), 2012.                                   Conference on Computer and Communications Security (CCS), 2013.

 [7] Francesco Caturano, Gaetano Perrone, and Simon Pietro Romano. Dis-         [23] Jonas Magazinius, Billy K Rios, and Andrei Sabelfeld. Polyglots:
     covering reflected cross-site scripting vulnerabilities using a multiob-        Crossing origins by crossing formats. In Proc. of ACM Conference on
     jective reinforcement learning environment. Computers & Security,               Computer and Communications Security (CCS), 2013.
     2021.
                                                                                [24] MDN web docs. Referer Header: Privacy and Security Concerns.
                                                                                     Online    https://developer.mozilla.org/en-US/docs/Web/
 [8] Adam Doupé, Marco Cova, and Giovanni Vigna. Why johnny can’t
                                                                                     Security/Referer_header:_privacy_and_security_concerns,
     pentest: An analysis of black-box web vulnerability scanners. In Proc.
                                                                                     2022.
     of Detection of Intrusions and Malware & Vulnerability Assessment
     (DIMVA), 2010.
                                                                                [25] MDN web docs.        Warning - HTTP | MDN.       Online
                                                                                     https://developer.mozilla.org/en-US/docs/Web/HTTP/
 [9] Kostas Drakonakis, Sotiris Ioannidis, and Jason Polakis. The Cookie
                                                                                     Headers/Warning, 2022.
     Hunter: Automated Black-Box Auditing for Web Authentication and
     Authorization Flaws. In Proc. of ACM Conference on Computer and            [26] William Melicher, Anupam Das, Mahmood Sharif, Lujo Bauer, and
     Communications Security (CCS), 2020.                                            Limin Jia. Riding out DOMsday: Towards detecting and preventing
                                                                                     DOM cross-site scripting. In Proc. of Network and Distributed System
[10] Fabien Duchene, Sanjay Rawat, Jean-Luc Richier, and Roland Groz.
                                                                                     Security Symposium (NDSS), 2018.
     KameleonFuzz: evolutionary fuzzing for black-box xss detection. In
     Proc. of ACM Conference on Data and Application Security and Pri-          [27] Alaeddine Mesbahi. Finding superhuman XSS polyglot payloads
     vacy (CODASPY), 2014.                                                           with Genetic Algorithms. Online https://blog.ostorlab.co/
                                                                                     polyglot-xss.html, 2021.
[11] Ahmed Elsobky. Unleashing an Ultimate XSS polyglot. Online
     https://github.com/0xsobky/HackVault/wiki/Unleashing-                      [28] Marius Musch, Robin Kirchner, Max Boll, and Martin Johns. Server-
     an-Ultimate-XSS-Polyglot, 2018.                                                 Side Browsers: Exploring the web’s hidden attack surface. In Proc.
                                                                                     of ACM Asia Conference on Computer and Communications Security
[12] DevTools engineering team. Chrome DevTools Protocol. Online                     (ASIA CCS), 2022.
     https://chromedevtools.github.io/devtools-protocol/,
     2023.                                                                      [29] OWASP Foundation. OWASP Top 10 – 2013. Online https://owasp.
                                                                                     org/www-pdf-archive/OWASP_Top_10_-_2013.pdf, 2013.
[13] Benjamin Eriksson, Giancarlo Pellegrino, and Andrei Sabelfeld. Black
     widow: Blackbox data-driven web scanning. In Proc. of IEEE Sympo-          [30] OWASP Foundation. OWASP Top Ten – 2017. Online https://www.
     sium on Security and Privacy, 2021.                                             owasp.org/images/7/72/OWASP_Top_10-2017_(en).pdf.pdf,
                                                                                     2017.
[14] Myles Foley and Sergio Maffeis. HAXSS: Hierarchical reinforcement
     learning for XSS payload generation. In Proc. of International Confer-     [31] OWASP Foundation. OWASP Top Ten – 2021. Online https://
     ence on Trust, Security and Privacy in Computing and Communications             owasp.org/Top10/, 2021.
     (TrustCom), 2022.
                                                                                [32] OWASP Foundation. CWE-598: Use of get request method with
[15] Google. GitHub google/firing-range 0.48. Online https://github.                 sensitive query strings. Online https://cwe.mitre.org/data/
     com/google/firing-range/tree/4f991a/, 2018.                                     definitions/598.html, 2021.




USENIX Association                                                                                    33rd USENIX Security Symposium                  6737
[33] OWASP Foundation.     Secure product design - OWASP cheat                        Appendices
     sheet series. Online https://cheatsheetseries.owasp.org/
     cheatsheets/Secure_Product_Design_Cheat_Sheet.html,
     2021.
                                                                                      A    Notification Script
[34] Muhammad Parvez, Pavol Zavarsky, and Nidal Khoury. Analysis of                   Figure 10 shows the self-executing notification script, which
     effectiveness of black-box web application scanners in detection of              collects minimal information about its execution environment
     stored sql injection and stored xss vulnerabilities. In 2015 10th Inter-         and transmits the information via XMLHttpRequest to an API
     national Conference for Internet Technology and Secured Transactions
     (ICITST), 2015.                                                                  endpoint of our monitoring server.
[35] Stuart J Russell. Artificial intelligence a modern approach. Pearson
     Education, Inc., 2010.                                                       1    /* Written for ECMAScript 5.1. Please visit <redacted> for
                                                                                        ↪ further information. Contact: <redacted> */
[36] SAP. Project Foxhound.            Online https://github.com/SAP/             2
     project-foxhound, 2023.                                                      3    (function () {
                                                                                  4      /* collect minimal information */
[37] Prateek Saxena, David Molnar, and Benjamin Livshits. SCRIPTGARD:             5      var data = {
     Automatic context-sensitive sanitization for large-scale legacy web          6        "id": "info",
     applications. In Proc. of ACM Conference on Computer and Communi-            7        "title": document.title,
                                                                                  8        "protocol": document.location.protocol.replace(":", ""),
     cations Security (CCS), 2011.                                                9        "domain": document.domain,
                                                                                 10        "port": document.location.port,
[38] David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre,      11        "pathname": document.location.pathname,
     George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou,         12        "navigator_ua": window.navigator.userAgent,
     Veda Panneershelvam, Marc Lanctot, et al. Mastering the game of Go          13        "navigator_platform": window.navigator.platform
     with deep neural networks and tree search. Nature, 2016.                    14      };
                                                                                 15
[39] Sooel Son and Vitaly Shmatikov. The Postman Always Rings Twice:             16       /* report */
     Attacking and defending postMessage in HTML5 websites. In Proc. of          17       var url = "https://<redacted>/callback?";
                                                                                 18       for (var key in data) {
     Network and Distributed System Security Symposium (NDSS), 2013.             19         url += key + "=" + encodeURIComponent(data[key]) + "&";
                                                                                 20       }
[40] Marius Steffens and Ben Stock. PMForce: Systematically analyz-              21       url += "timestamp=" + (new Date().getTime()).toString();
     ing PostMessage handlers at scale. In Proc. of ACM Conference on            22
     Computer and Communications Security (CCS), 2020.                           23      var xhr = new XMLHttpRequest();
                                                                                 24      xhr.open('GET', url, true);
[41] Marius Steffens, Christian Rossow, Martin Johns, and Ben Stock. Don’t       25      xhr.send();
     trust the locals: Investigating the prevalence of persistent client-side    26    })();
     cross-site scripting in the wild. In Proc. of Network and Distributed
     System Security Symposium (NDSS), 2019.

[42] Ben Stock, Stephan Pfistner, Bernd Kaiser, Sebastian Lekies, and Mar-                             Figure 10: Notification Script
     tin Johns. From Facepalm to Brain Bender: Exploring client-side
     cross-site scripting. In Proc. of ACM Conference on Computer and
     Communications Security (CCS), 2015.                                             B    Data Management
[43] Ben Stock, Martin Johns, Marius Steffens, and Michael Backes. How                Due to our notification script’s design, as detailed in Sec-
     the Web Tangled Itself: Uncovering the history of client-side web
     (in)security. In Proc. of USENIX Security Symposium, 2017.
                                                                                      tion 5.1 and Appendix A, we received only a minimal amount
                                                                                      of data. Notably, the backend URL’s query and fragment were
[44] Ben Stock, Giancarlo Pellegrino, Frank Li, Michael Backes, and Chris-            never transmitted. We expected to receive no personally iden-
     tian Rossow. Didn’t You Hear Me? - Towards More Successful Web
     Vulnerability Notifications. In Proc. of Network and Distributed System          tifiable information (PII) in either the path or the title of
     Security Symposium (NDSS), 2018.                                                 affected webpages. However, we prepared a data manage-
                                                                                      ment strategy to handle potential PII transmissions from our
[45] Kacper Szurek. XSS polyglot. Online https://security.szurek.
     pl/en/xss-polyglot/, 2019.                                                       notification script’s feedback pings. Our strategy entails to
                                                                                      manually replace potentially received PII with placeholders.
[46] Christine Utz, Sabrina Amft, Martin Degeling, Thorsten Holz, Sascha
     Fahl, and Florian Schaub. Privacy rarely considered: Exploring consid-
                                                                                      Fortunately, as shown in Table 1 neither the backend paths nor
     erations in the adoption of third-party services by websites. In Proc. of        titles contained such information. IP addresses have a distinc-
     Privacy Enhancing Technologies Symposium (PETS), 2023.                           tive role, as they are indirectly received via a feedback ping
[47] Christopher JCH Watkins and Peter Dayan. Q-learning. Machine                     from a vulnerable backend. Initially used to validate instances
     learning, 8:279–292, 1992.                                                       of blind XSS (Section 5.3), they later assist in meaningful
[48] Joel Weinberger, Prateek Saxena, Devdatta Akhawe, Matthew Finifter,
                                                                                      disclosure and forensic analysis. Supplying operators with
     Eui Shin, and Dawn Song. A systematic analysis of XSS sanitization               both the IP address and user agent information, facilitating
     in web application frameworks. In Proc. of European Symposium on                 distinction between manual actions and automated processes,
     Research in Computer Security (ESORICS), 2011.                                   helps them assess the vulnerability’s impact. Post-disclosure,
[49] WHATWG. HTML Standard - 13.2.4.5 Parse state: Other parsing                      all retained IP addresses and user agents were deleted. Ul-
     state flags. Online https://html.spec.whatwg.org/multipage/                      timately, the data this paper is based on will be archived as
     parsing.html#other-parsing-state-flags, 2023.                                    scientific evidence according to our institution’s guidelines.



6738     33rd USENIX Security Symposium                                                                                           USENIX Association
C    Alternative Generation Approaches                                Output: polyglot string
                                                                   1  sbest ← null
                                                                    2 rbest ← 0
Our polyglot synthesis for BXSS with MCTS has been suc-             3 s0 ← []
cessful in generating a complementary polyglot set. As our          4 while evaluation budget is not exceeded do

generation approach is agnostic to this algorithm, however,         5       for t ← 0; polyglot not complete; t ← t + 1 do
                                                                    6             if rand(0, 1) < pexp then
we investigate three alternative algorithms that could also         7                    at ← choose_random(st );
be applied to our setting for constructing polyglots: random        8             end
                                                                    9             else
selection, greedy selection, and Q-learning.                       10                    at ← maxa Q(st , a)
                                                                   11             end
   Random selection — This method leverages our MCTS               12             st+1 ← st + [at ]
implementation, as depicted in Algorithm 1, but incorporates       13             rt ← evaluate(st+1 )
                                                                   14             Q(st , at ) ← Q(st , at ) + α(rt + γ maxa Q(st+1 , a) − Q(st , at ))
random selection and a random playout phase. In the selection      15             if rt > rbest then
phase, each child is given an equal probability, and one is        16                    rbest ← rt
                                                                   17                    sbest ← st+1
selected at random. Once the end condition—specifically, the       18             end
maximum payload length—is met, the constructed polyglot            19             p ← max(Γ ⋅ p, pmin )
                                                                   20       end
undergoes evaluation on the small testbed.                         21 end
                                                                   22 return sbest
   Greedy selection — This method generates a polyglot by
continuously appending the best next token. Since we cannot
know in advance which token is the best, we probe each token           Algorithm 2: Generating a polyglot with Q-learning
by appending the respective token to the current polyglot and
evaluating the resulting polyglot on the testbed, thus imple-
                                                                   approach as boxplots. Plot (b) displays boxplots of the set
menting a greedy search. If multiple tokens achieve the same
                                                                   sizes the same approaches achieved. Generally, smaller poly-
performance, we select one randomly to append. In contrast
                                                                   glot set sizes are preferred because they would result in fewer
to MCTS and random selection, the greedy method evaluates
                                                                   requests being sent to a system under test when testing for
unfinished polyglots in order to choose the next token.
                                                                   client-side XSS (Section 4) or blind XSS (Section 5). While Q-
   Q-learning — This method builds on Q-learning [47], a           learning and greedy selection produce smaller polyglot sets,
popular reinforcement learning technique. The method pop-          their overall coverages on the GFR are significantly lower
ulates a table of state-action pairs Q(st ,at ) to determine the   than those of MCTS and random selection. We can there-
best action at in a given state st . Algorithm 2 shows our         fore discard both of them as alternative polyglot synthesis
Q-learning implementation. It first chooses either a random        approaches. In terms of coverage, the random method per-
action or the best next action and then evaluates the result-      forms only slightly worse than MCTS on average. However,
ing state on the testbed, updates the q-values and saves the       MCTS consistently achieves a lower set size than random
polyglot if it performed best. For Q-learning we set the learn-    selection. We believe this is the result of MCTS’s knowledge
ing rate α = 0.1 and the discount factor γ = 0.99 as well as       aggregated over multiple games, which allows it to generate
the simulated annealing parameters: initial exploration proba-     more powerful polyglots.
bility p = 1, minimal exploration probability pmin = 0.01 and
exploration decay Γ = 0.95.
                                                                   D       Google Firing Range
Comparative evaluation. We compare the approaches
based on the coverage they achieve on the GFR and the num-         In Section 3.3 we discuss the construction of our compre-
ber of polyglots they require to reach that coverage. The ex-      hensive XSS testbed, which was derived from a subset of the
periment consists of generating a set of 10 polyglots with         GFR [15] tests to determine the efficacy of the polyglots. This
each algorithm, evaluating the resulting sets on the GFR and       section details which tests were excluded and why.
removing polyglots from the sets that do not contribute to the        The GFR is structured as a crawlable list of subpages cover-
overall performance. To account for randomness, the experi-        ing different categories of web vulnerabilities. Each category
ment is repeated 10 times for each approach.                       produces tests from a mix of sink, source, and countermea-
   In the generation phase, each approach iteratively generates    sures. Due to this setup, certain combinations result in un-
polyglots on the small testbed. After each iteration, we remove    solvable tests. To create our comprehensive and solvable XSS
tests that are covered by the polyglots. Since calls to the        testbed, it is essential to first filter the GFR test cases.
testbed are computationally the most expensive component             To begin with, we omitted all test categories unrelated to
of each algorithm, all methods are given a budget of 12.000        XSS. As outlined in Table 2, the categories “Bad JavaScript
evaluation calls to the testbed during each iteration.             imports”, “CORS related vulnerabilities”, “Flash Injection”,
   The evaluation of our comparative experiment’s results          “Mixed content”, “Reverse Clickjacking”, “Vulnerable li-
are shown in Figure 11. Plot (a) aggregates the resulting set      braries”, “Leaked httpOnly cookie”, and “Invalid framing
coverage on the GFR of the 10 parallel repetitions of each         configuration” are out of scope as they are not related to XSS



USENIX Association                                                                             33rd USENIX Security Symposium                            6739
            (a) GFR Tests Covered                  (b) Minimal Set Size
 110                                     10                                    Table 2: Vulnerability categories of the GFR 0.48 and their
                                                                               general applicability for our blind XSS testbed
 100                                      9

  90                                      8                                      #    Category                              Scope     Reasoning
  80
                                          7                                      1    Address DOM XSS                         ✓       XSS-related
  70                                                                             2    Angular-based XSSes                     ✗       framework-specific
                                          6
  60
                                                                                 3    Bad JavaScript imports                  ✗       non-XSS-related
                                          5                                      4    CORS related vulnerabilities            ✗       non-XSS-related
  50                                                                             5    DOM XSS                                 ✓       XSS-related
                                          4
  40                                                                             6    Escaped XSS                             ✓       XSS-related
                                          3                                      7    Flash Injection                         ✗       non-XSS related
  30                                                                             8    Mixed content                           ✗       non-XSS related
  20                                      2                                      9    Redirect XSS                            ✓       XSS-related
                                                                                10    Reflected XSS                           ✓       XSS-related
  10                                      1
                                                                                11    Remote inclusion XSS                    ✓       XSS-related
   0                                      0                                     12    Reverse ClickJacking                    ✗       non-XSS related
                                                                                13    Tag based XSS                           ✓       XSS-related
        S


                 m


                         dy




                                               S


                                                       m
                                    ng




                                                               dy



                                                                          ng
       T




                                              T
               do




                                                     do
                                  ni




                                                                        ni
                        e




                                                               e
    C




                                           C
                     re




                                                            re


                                                                                14    URL-based DOM XSS                       ✓       XSS-related
             an




                                                   an
                                  ar




                                                                        ar
   M




                                          M
                     G




                                                           G
                              -le




                                                                    -le
            R




                                                   R
                              Q




                                                                    Q

                                                                                15    Vulnerable libraries                    ✗       non-XSS related
                                                                                16    Leaked httpOnly cookie                  ✗       non-XSS related
Figure 11: MCTS, Random, Greedy and Q-learning compari-                         17    Invalid framing configuration           ✗       non-XSS related
son; each generating 10 polyglots in 10 parallel runs                          ✓ category is generally in scope       ✗ category is out of scope



vulnerabilities. Additionally, we disregarded the “Angular-                    Table 3: Excluded GFR tests from the categories in scope,
based XSSes” category given its focus on a particular frame-                   referenced by path
work, AngularJS, which is beyond our study’s scope.
   From the categories that remained relevant post our prelim-                  No solution confirmed (20)
inary filtering, Table 3 provides a list of the excluded tests                  /dom/toxicdom/postMessage/improperOriginValidationWith
                                                                                PartialStringComparison,     /dom/toxicdom/postMessage/im
alongside reasons for their omission. For brevity, tests are
                                                                                properOriginValidationWithRegExp, /dom/javascripturi.html,
identified by their path, accessible by appending the test path                 /escape/serverside/encodeUrl/tagname,      /escape/server
to GFR’s main URL public-firing-range.appspot.com.                              side/encodeUrl/js_assignment,       /escape/serverside/en
   Our subsequent filtering entailed the removal of tests lack-                 codeUrl/js_eval,         /escape/serverside/escapeHtml/at
                                                                                tribute_script,        /escape/serverside/escapeHtml/href,
ing solutions. Some tests became unsolvable due to the combi-                   /escape/serverside/encodeUrl/href,    /tags/tag,   /tags/
nation of sinks and countermeasures, modern browser security                    tag/div, /tags/tag/img, /tags/tag/style, /tags/tag/iframe,
features, or obsoleted features. Fortunately, we acquired a list                /tags/tag/div/style, /tags/tag/a/href, /tags/tag/a/style,
of solvable GFR tests from Google. After manual confirma-                       /tags/tag/script/src, /tags/tag/body/onload, /urldom/loca
                                                                                tion/hash/script.src.partial_query
tion, we removed tests without a solution. Secondly, a handful
of tests were removed for technical reasons, such as being                      Technical reasons (5)
removed from the GFR (Stored XSS), or tests involving mul-                      /dom/toxicdom/document/referrer/eval,     /dom/toxicdom/
                                                                                document/referrer/innerHtml,   /dom/toxicdom/document/re
tiple windows. Tests with exceptionally restrictive solutions,                  ferrer/documentWrite, /stored/index.html, /urldom/loca
out-of-scope for a polyglot, were also ruled out, including                     tion/hash/window.open
those with stringent filters, or those solvable using only a                    Solution too narrow (12)
URL. Likewise, we omitted tests exceeding our technology
                                                                                /dom/toxicdom/postMessage/documentWrite,         /reflect
boundaries, such as those using Adobe Flash, Base64, and                        ed/url/href, /reflected/url/script_src, /remoteinclude/
SVG. This leaves us with 111 tests.                                             parameter/script, /remoteinclude/script_hash.html, /url
   The GFR tests involve various input sources, including                       dom/location/hash/base.href, /urldom/location/hash/fetch,
                                                                                /urldom/location/hash/script.href,          /urldom/loca
form submissions, URL parameters, or PostMessages. Some                         tion/hash/script.src,     /urldom/location/hash/xhr.open,
demand clicks or page reloads post-input. Using Puppeteer,                      /urldom/location/hash/script.src.partial_domain,     /url
our test software provides a polyglot to each relevant GFR                      dom/location/hash/script.src.partial_path
test through the suitable input method, meeting the post-                       Technology out-of-scope (8)
submission requisites. It then waits for an XSS success signal                  /remoteinclude/parameter/object_raw,     /remoteinclude/ob
through a specific log message. We use Puppeteer cluster to                     ject_hash.html,    /urldom/location/hash/embed.src,   /url
test one polyglot on multiple tests in parallel. After a run                    dom/location/hash/object.data,      /urldom/location/hash/
                                                                                param.code.value, /urldom/location/hash/param.movie.value,
concludes, the polyglot’s result in each test are returned. The                 /urldom/location/hash/param.src.value,        /urldom/loca
implementation of our testing approach is published in our                      tion/hash/param.url.value
companion repository.



6740        33rd USENIX Security Symposium                                                                                        USENIX Association
