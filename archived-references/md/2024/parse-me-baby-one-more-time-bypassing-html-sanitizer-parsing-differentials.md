---
type: Whitepaper
title: "Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials"
resource: "https://www.ias.cs.tu-bs.de/publications/parsing_differentials.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T22:36:05+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "https://www.ias.cs.tu-bs.de/publications/parsing_differentials.pdf"
    title: "Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials"
    author: David Klein, Martin Johns
also_at: []
authors:
  - David Klein
  - Martin Johns
canonical_url: ""
cited_by:
  - "2024.md:113"
commit: ""
content_sha256: 5d22ae6287462f02b7aeeba848635f75f04dc8431a2e02978c6fff31e7c51a84
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://www.ias.cs.tu-bs.de/publications/parsing_differentials.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: c30129a01ccf1fd656ca00e6420099ebf4d553f14d3516bdd9403be09a1136e2
retrieved_from: "https://www.ias.cs.tu-bs.de/publications/parsing_differentials.pdf"
retrieved_kind: manual-import
retrieved_utc: "2026-08-14T22:36:05+00:00"
slug: parse-me-baby-one-more-time-bypassing-html-sanitizer-parsing-differentials
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials

**Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials** - David Klein, Martin Johns, Publisher not stated.

- Published: date not stated
- Original: <https://www.ias.cs.tu-bs.de/publications/parsing_differentials.pdf>
- Preserved from: https://www.ias.cs.tu-bs.de/publications/parsing_differentials.pdf (manual-import) on 2026-08-14
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials

Parse Me, Baby, One More Time: Bypassing HTML Sanitizer via Parsing Differentials

                                                 David Klein and Martin Johns
                                              Technische Universität Braunschweig
                                           {david.klein,m.johns}@tu-braunschweig.de

Abstract—Websites rely on server-side HTML sanitization to               Instead, we propose to take a step back and ask the
defend against the ever-present threat of cross-site scripting       question: Is server-side HTML sanitization even possible
attacks. Parsing arbitrary pieces of markup to assess whether        without mangling benign input?
they contain an exploit payload is far from trivial. This                Over the last years, the security community realized that
complexity leads to divergences between the parsing results of       accurate HTML sanitization is only possible with detailed
the sanitizer and the user’s browser. These so-called parsing        information on where in the website the sanitized result is
differentials open the door for the unexplored category of           inserted [14]. While this information is possibly available for
mutation-based attacks. Here, an attacker abuses the sanitizer’s     client-side sanitization, as the currently proposed Sanitizer
incorrect HTML parser to either directly bypass it or coerce it      API shows, it is out of reach for server-side sanitizers. This
to transform benign markup into a dangerous exploit payload.         context sensitivity influenced the design of the sanitizer
    In this work, we study the prevalence of such parsing            API, which does not allow to perform a string-to-string
differentials and their security impact. To this end, we built a
                                                                     transformation [15], declaring it generally unsafe to do so.
generator for HTML fragments that are difficult to parse and
                                                                     On the server, this is the only type of transformation available,
                                                                     as ultimately, the sanitizer’s output ends up in an HTTP
evaluated how 11 sanitizers across five programming languages
                                                                     response, which is text-based.
deal with such inputs. We found that parsing differentials are
                                                                         Server-side sanitization routines face an additional chal-
commonplace, as each assessed sanitizer has at least several
                                                                     lenge. To accurately sanitize an HTML fragment, that is,
functional deficiencies leading to overzealous removal of benign
                                                                     only to remove the actively dangerous part, a sanitizer has
input. Even worse, we were able to automatically bypass all
                                                                     to parse it in the same fashion as a browser. A cursory
but two of the 11 sanitizers, painting a dire picture of the state   glance at the HTML specification suffices to highlight the
of server-side HTML sanitization.                                    complexity of writing such a parser. Even if the sanitizer
                                                                     implements the specification perfectly, this does not suffice
1. Introduction                                                      either, as browsers can and do diverge from the specification.
                                                                     Therefore, to accurately sanitize, a sanitizer would have to
                                                                     parse its input exactly like the user’s browser would. This
     There are two frontiers to protect against cross-site           requires information on the client’s browser, the parsing
scripting (XSS): on the client and on the server-side. Tra-          mode, and the exact injection context to adjust the sanitizer’s
ditionally, client-side XSS protection has been seen as the          behavior accordingly. This is not supported by any server-side
difficult one, as the client offers no protection mechanisms,        sanitizer. This problem is further aggravated by browsers
and writing custom sanitization code is notoriously error-           accepting invalid HTML input. Instead of aborting the parsing
prone [1]. Google, for example, directly acknowledges this           process, they try to rewrite and correct the input, i.e., mutating
fact in their report on Trusted Type adoption: “More than            it and changing the HTML structure in the process. While
half of the DOM XSS root causes were due to bugs in HTML             this behavior is partially specified, it adds another difficulty
sanitizers” [2]. The academic community has also mainly              for the authors of parsing and sanitization routines: Their
focused on client-side XSS, from prevalence scanning [3–             software would need to support the same behaviors to assess
8] to studying employed protection mechanisms [1, 9], the            the security impact of HTML fragments correctly. Otherwise,
body of work is extensive. Conversely, the exploration of            it opens the door to mutation-based XSS vulnerabilities.
server-side XSS remains notably underrepresented. Large-                 These issues raise two interesting questions: Is it feasible
scale server-side security scanning is comparatively scarce,         to write a sanitizer that is both accurate, i.e., does not mangle
primarily due to ethical and legal challenges [10].                  benign content, and secure? And how do popular open-source
     Due to modern server-side web development’s heavy               sanitizing libraries fare in this respect?
reliance on frameworks, one might assume robust defense              These are the questions we will answer in this work.
mechanisms are in place. Such defenses could come in the                 To assess the prevalence of parsing divergences, we first
form of automatic sanitizer placement, as suggested in past          analyzed the HTML specification, selecting HTML tags and
work [11–13]. However, after inspecting the documentation            edge cases that might lead to interesting parsing behavior.
of 11 popular web frameworks about their XSS protections,            We then present MutaGen, an HTML fragment generator
we found this assumption to be lacking.                              with a special focus on fragments prone to mutations, and
evaluate such fragments on our testbed. Here, we sanitize                A stream-based HTML parser, i.e., a parser that emits the
each generated fragment with 11 different sanitizers and             result of each step in the tree construction stage, can never
evaluate their outputs in all major browsers. We also record         be specification-compliant. Scattered across the specification
the DOM-like structure resulting from both the sanitizers as         are points where the parser has to rearrange previously
well as the browsers’ parsing processes. This allows us to           processed elements. For example, inside a table, if the
automatically assess if and where parsing behavior diverges          parser encounters a tag that is not allowed to occur in
and how this can lead to sanitizer bypasses. We detect severe        this position, the foster parenting algorithm is invoked to
parsing discrepancies between the evaluated sanitizers as            rearrange the DOM and rehome the offending tag [18]. For
well as between the major browsers.                                  the input, <table><div><tbody> a stream parser would
    Our contributions are the following:                             emit the opening tags table, div and tbody. As the div
   • MutaGen: A generator for HTML fragments prone to                tag is not a valid child of table, the parser invokes the
     mutations during parsing.                                       foster parenting algorithm to correct the input. This results
   • An analysis framework that detects diverging parsing            in <div></div><table><tbody>, i.e., it moves div
     behavior between sanitizers and web browsers.                   in front of the opening table. Consequently, a stream
   • We then use these building blocks to assess how 11              parser has to invalidate already emitted events, defeating its
     sanitization libraries are affected by parsing differentials.   purpose. Thus, accurately parsing HTML is only possible in
     We found new bypass vectors for all but two and parsing         a single pass. This complexity is a direct result of the desire
     deficiencies in all of them.                                    to be always able to render a website, even if it violates
The remainder of this paper is structured as follows: First,         the HTML specification in one way or another. Instead
we provide a recap on the required background in Section 2.          of rejecting invalid markup, modern browsers attempt to
We then detail the design of MutaGen and our evaluation              repair the input and display it regardless. This repair step
and analysis framework (Section 3), followed by an overview          involves the aforementioned DOM transformations, such as
of our findings and the efficacy of the presented approach           foster parenting, effectively mutating the input. Websites
in Section 4. Afterward, we discuss some major takeaways             violating the specification are commonplace even today [19],
and mitigation approaches (Section 5) and related work               preventing browser vendors from tightening the parsing
(Section 6) before we conclude in Section 7.                         process without breaking the web.
                                                                         Another noteworthy aspect is that modern browsers sup-
2. Background                                                        port two HTML parsing algorithms, document and fragment
                                                                     parsing [20]. Document parsing is the regular parsing mode
    In this section, we first introduce the intricacies of           which processes a whole document. The fragment parsing
HTML parsing. Afterward, we discuss (mutation) cross-                mode instead relies on a context element and returns a DOM
site scripting and how sanitization can protect against such         fragment, i.e., a tree of nodes rooted at the context element.
attacks. Lastly, we showcase how parsing differentials lead          It is, for example, used for .innerHTML assignments.
to HTML sanitizer bypasses.                                          Differences in the behavior of these two modes are another
                                                                     source of potential issues. A well-known difference between
2.1. Complexities of HTML Parsing                                    the two parsing modes is the handling of script tags,
                                                                     which are only executed in the document parsing mode.
    HTML is the premiere markup language on the web,                 The HTML standard mandates support for both of these
supported by all browsers. However, its evolution has not            two parsing algorithms. However, modern browsers might
been straightforward. This is acknowledged in the official           implement several parsers for each parsing mode. Chromium,
specification, which states “that many aspects of HTML               for example, has two fragment parsing algorithms. The
appear at first glance to be nonsensical and inconsistent.” [16].    fastpath parser is used if the fragment only contains tags that
Despite being seemingly simple, parsing and rendering                do not require DOM rearrangements, and upon encountering
HTML is a very involved process. From a visual point                 such a tag, it bails out to the regular one, which supports the
of view, one would assume that parsing HTML and XML                  whole tag range [21]. By not considering all the intricacies of
has many commonalities. They both derive from SGML                   HTML, the fastpath parser is generally faster. To top things
and consequently share most syntax. Modern XML parsers               off, HTML allows embedding so-called foreign content to
offer two profiles: SAX-based [17] parsing and DOM-based             support increasingly complex use cases. Both typesetting
parsing. For the latter, the whole document is parsed into           instructions for math formulas (via MathML [22]) and vector
a tree structure and returned at once. SAX parsing has a             graphics (via SVG [23]) can be directly inserted into HTML
lighter memory footprint as it is a stream-based parsing             documents. As they also share HTML’s ancestry, they also
approach. As the parser reads the input, it emits parsing            share some syntactic structure (and even tag names at times),
events (e.g., opening tags) as it comes across them. One             but additional complexities arise due to this combination.
would assume the same is possible for HTML, but this would
be a misconception. HTML parsing is divided into two stages:         Example.       Consider the input from Figure 2a, which
tokenization, i.e., turning incoming bytes into tokens, and          serves as the running example throughout this section. When
tree construction, which builds a Document Object Model              assigning it to the .innerHTML attribute of a div element,
(DOM) tree from said tokens.                                         Chromium parses the first img tag as an HTML element
                          div                                             context                                 div
                                                                   img              math
            img          math           img                                                               math           img
                                                                                iframe
                        iframe                                                                           iframe
                                                                                    #text
         (a) Chrome parsing the running example                                                       (c) Chrome parsing the result
                                                              (b) Sanitizer parse tree
                                      Figure 1: Parsing differential leading to sanitizer bypass


1    <img src=x onerror=f()> <math> <iframe> <img                        2.3. Sanitization
     ,→  src=x onerror=f()>

                          (a) User input
                                                                             To prevent XSS, special care is required to ensure user
1    <math> <iframe> <img src=x
     ,→  onerror=f()></iframe></math>                                    input is free from unwanted HTML markup. In this case,
                                                                         unwanted means tags executing code (such as the img tag
                        (b) Sanitized result                             in the example) but can also include tags changing the
    Figure 2: Payload before (2a) and after (2b) sanitization.           website’s layout in an undesirable fashion. The process of
                                                                         removing such unwanted markup is called sanitization. To
                                                                         do this accurately, the sanitizer has to determine whether a
 and adds it as the context nodes (i.e., the div element), first         specific piece of text includes markup that might execute
 child. Then, upon encountering the math tag, the parser                 code. A common approach to sanitization is to parse the
 switches to the MathML mode (i.e., nodes are added with                 input according to the HTML specification and to operate
 their namespace set to MathML) and adds math as the                     on the resulting DOM tree. The sanitizer then traverses the
 second child. The following iframe tag is also parsed in                DOM and removes or transforms nodes according to, e.g.,
 MathML mode and added as the first child of math. Next,                 an allowed list of harmless tags or a block list of tags to
 the second img is processed. It is among the list of elements           remove. Afterward, the sanitized DOM is serialized back
 that cause the parser to switch back to the HTML [24]. To               into its textual representation and returned to the caller.
 do so, it closes the currently open elements (i.e., iframe                  For example, a sanitizer configured to allow both math
 and math) and inserts the img tag as the context’s third                and iframe tags and to remove all img tags. When
 child, resulting in Figure 1a. HTML nodes are depicted in               processing the running example from Figure 2a, its parsing
 blue, and those in the MathML namespace are in yellow.                  result is depicted in Figure 1b with a synthetic node as its
                                                                         root. To remove harmful tags, it considers each node in the
 2.2. Cross-Site Scripting                                               tree and removes the first image node, highlighted in red. All
                                                                         other nodes (colored green) are in its allow list (text nodes
    Cross-site scripting (XSS) is the most common vulnera-               implicitly) and, therefore, stay untouched. The serialization
bility class on the web. The goal behind an XSS attack is                step again traverses the tree and converts each node to its
for the attacker to execute code within the security domain              HTML representation. Here, the input is usually cleaned
of the website. This allows them to exfiltrate data such as              beyond removing XSS payloads. As depicted in Figure 2b,
cookies or inputs, perform actions on behalf of the user,                the sanitizer adds closing tags that were omitted from the
or manipulate the website’s content to trick the user into               input.
performing unwanted actions. An XSS vulnerability requires                   Sanitization stands in contrast to encoding, another pop-
the attacker to be able to control some parts of the markup              ular form of ensuring attacker-controlled input is free from
of the website. Due to the fact that in HTML, there is no                markup. The difference is that sanitization allows certain tags
distinction between markup and data, at every point where                to pass through and only removes (or encodes) potentially
user-controlled data ends up on a website, there is a potential          dangerous parts of the string. Encoding, on the other hand,
XSS vulnerability.                                                       replaces control characters with their escaped form. If a
    Consider a website allowing users to leave comments, a               string is inserted in the HTML context, e.g., inside a div
basic form of community building. If a malicious user puts               tag <div>${name}</div>, it would suffice to replace all
in the running example from Figure 2a, every other visitor’s             control characters with their character references. Turning
browser parses the supposed comment as in Section 2.1. The               <script> into &lt;script&gt; would reliably prevent
example string contains two img tags, both referencing an                injection attacks in this case. Encoding should be used if the
unavailable destination. Upon failing to load the nonexisting            user shall not be able to influence the markup while saniti-
images, the browser executes their error handlers and calls              zation allows the input to contain markup. They, therefore,
f () twice, highlighted by the warning sign in Figure 2a.                serve different purposes. We only focus on sanitization; the
The call to f happens inside the website’s origin, giving the            security of encoding-based protection schemes is outside the
attacker complete access to each visitor’s session.                      scope of this work.
2.4. Mutation Cross-Site Scripting                                                                                  Sanitizer Runner


    Mutation Cross Site Scripting (mXSS) is a subclass of the
                                                                                     Central Database
generic XSS vulnerability group popularized by Heiderich
et al. [25]. Such a vulnerability occurs if an HTML fragment                                                     Java              PHP

is parsed, serialized, and yields a different result upon being
parsed again. Initially, this was limited to cases where, due                                                               .NET
to updates to the DOM, the browser’s HTML parser would              MutaGen
                                                                                                               JavaScript          Ruby
parse an HTML fragment a second time. These vulnerabilities
were based on problematic behavior of the browsers, i.e.,
bugs, and were resolved there.
                                                                              Chromium    Firefox     WebKit
    However, over time, the vulnerability class mXSS also
                                                                                 Browser Evaluation Testbed
started encompassing what Heiderich called “mutation based
attacks”. Here, the initial parsing and serialization steps                    Figure 3: Sanitizer Evaluation Setup
happen inside a sanitizer, and only the second parsing
step occurs inside the browser. For such a vulnerability to
manifest, the combination of HTML parsers of the sanitizer
and the browser must diverge in a way that the sanitizer          as well as past sanitizer bypasses based on parsing differen-
can be bypassed. This happens if, for example, the sanitizer      tials [27–30]. Based on inspecting the HTML element [31]
parses the part of the input containing the exploit payload as    semantics and their corresponding parsing specifications [32],
part of a text node and returns it unchanged. If the browser,     we collected elements with complex parsing rules. The
upon parsing the sanitizer’s output, parses the assumed text      element specification provides a general description of all
content as markup, the payload is executed, introducing an        elements, including restrictions on where they can occur,
XSS vulnerability.                                                whether closing tags can be omitted, and their content
    A sanitizer affected by a parsing differential could parse    model. The content model of an element specifies what other
the example as shown in Figure 1b. We detail the differences      elements are allowed as its children. The parsing specification,
in the parsing and how this opens the door to a bypass in         on the other hand, describes how the parser constructs the
the following. The sanitizer is unaware of the namespace          DOM tree.
transition rules for foreign content and considers all elements       An example of a tag with complex parsing rules is the
as if they were parsed according to the HTML parsing rules.       iframe tag. It is noteworthy as its element specification
In HTML mode, everything inside the iframe tag is parsed          and parsing specification disagree. Its content model is
as text. If the sanitizer simply echoes back text nodes, the      nothing [33], stating the element “must contain no Text
second img tag passes through unmodified.                         and no element nodes” [34] but the parsing specification
    Upon parsing the output in Chromium, the iframe tag is
                                                                  instructs to parse its content as text, directly violating the
parsed as a custom MathML tag, and when encountering the
                                                                  content model. We identified a total of 47 tags, which can
img tag, the parser switches back to HTML mode, closing
                                                                  be divided into the following groups of elements: 1) Those
all open MathML tags in the process. The XSS payload is
                                                                  with restrictions on their content (e.g., select can only
thus lifted out of the iframe and moved as a direct child of
                                                                  contain specific child elements) 2) restrictions on where
the context element, causing code execution upon evaluation,
                                                                  they can occur (e.g., tr can only occur inside a table)
shown in Figure 1c. Thus, mutation-based bypasses are
                                                                  3) constraints on how often they can occur (e.g., there can
possible whenever there is a difference in parsing behavior
                                                                  only be one title while forms can not be nested) 4) with
between the browser and sanitizer. These kinds of bypasses
                                                                  disagreements between parsing and element specification
are the focus of this work.
                                                                  (e.g., iframe) 5) causing namespace transitions (e.g., svg
                                                                  or math) 6) and lastly those that are deprecated (e.g., xmp,
3. Uncovering Parsing Differentials                               which used to display HTML code without executing it) The
    To detect parsing differentials and mutation-based sani-      full list of tags with reasoning for their selection is provided
tizer bypasses, we built a testing framework consisting of        in Table 7.
three stages: Input generation, sanitization, and evaluation.          The parsing specification contains a “parse errors” [35]
The framework is depicted in Figure 3. We made the source         section, which is an additional source of parsing quirks we
code for the testing framework, i.e., MutaGen and the             identified as potentially challenging to implement. While the
testbed, available online [26]. We now first detail the results   specification explicitly allows a parser to abort the parsing
of analyzing the HTML specification and then detail each          process upon encountering such an error, no parser does this.
stage of our testing framework in the following.                  Instead, they emit erroneous output or rewrite the input. The
                                                                  identified quirks include 1) incorrect comments 2) invalid
3.1. HTML Analysis                                                attributes 3) attributes inside closing tags.
    With the goal of generating mutation-prone HTML                  These identified complexities are the foundation for our
fragments in mind, we first analyzed the HTML specification       generation approach.
        Generation                       Serialization
                                                                                 Table 1: Examined Sanitizing Libraries

                                                                    Name                       Version Total Downloads         Language       Vulns.
    Payload(Img_tag)             <img src=x onerror=f()>
                                                                                               2.3.10                                         1
                                                                    DOMPurify (*)                      399,001,216
       Close_tag                       </noscript>                                             3.0.3                                          1
  (NoScript, Prepend)            <img src=x onerror=f()>                                                                       JavaScript ‡
                                                                    sanitizer                  0.1.3   41,063,147
                                                                                                                                              †
 Enclose_tag_attr (Div,           <div id="</noscript>              google-caja-sanitizer      1.0.4   242,850
  Id, Enclosed(Double))         <img src=x onerror=f()>">           sanitize-html              2.7.0   276,882,692                            0
        Open_tag                       <noscript>                   HtmlSanitizer              8.0.601 19,800,000                             2
                                                                                                                               .NET
  (NoScript, Prepend)             <div id="</noscript>              HtmlRuleSanitizer          1.6.0.1 306,100                                2
                                <img src=x onerror=f()>">
                                                                    Typo3 html-sanitizer       2.0.15 1,950,185                PHP            4
            ⊥
                                                                    rgrove/sanitize            6.0.0   60,928,006                             1
                                                                                                                               Ruby
Figure 4: Simplified Payload Generation and Serialization.          loofah                     2.21.3 396,621,861                             0
                                                                    AntiSamy                   1.7.3                                          3
                                                                                                       No data available       Java
                                                                    JSoup                      1.16.1                                         2
3.2. MutaGen: HTML Fragment Generator
                                                                    *: jsdom version 19 and 22, †: Based on the same code base, both abandoned;
     The basic idea behind MutaGen is to approach the              therefore vulnerabilities not broken down, ‡: Retrieved with https://npm-stat.com
generation process iteratively. We first select an initial
payload P , i.e., a piece of HTML triggering JavaScript            parameterized. For example, the Enclose_tag_attr
execution, and subsequently extend P with surrounding              transformation in Figure 4 is parameterized over the tag,
HTML structure. The initial payload is as basic as possible        the attribute’s key, and quotes. The full list is provided in
by design. Generally, two kinds of injection vectors lead to       Table 6 and their parameters in Section A.1.
XSS: tag-based and attribute-based injections. Consequently,
we chose two payloads (i.e., script and img tags) to               Example. One HTML parsing aspect we discovered as
represent these categories. These are the most well-known          problematic for most sanitizers is correctly terminating
payloads for their respective categories. Hence, we expect         noscript tags. Figure 4 details a simplified generation
every sanitizer to handle them. During the HTML analysis,          run yielding a payload capable of generating a payload
we noticed that the specification instructs parsers to rewrite     that bypasses several sanitizers. On the Generation side in
image to img tags. This behavior represents a third class,         Figure 4, a list of transformations is created, starting from
parsing quirks, and thus, we added image to the set of             an initial payload, here an img tag. With each subsequent
initial payloads to cover this class of behaviors as well. While   transformation, MutaGen adds surrounding structure to the
more advanced payloads may uncover additional bypasses,            payload. First, it prepends a closing noscript tag and then
detecting vulnerabilities due to, e.g., a sanitizer missing        encloses the accumulated payload inside the double-quoted
specific event handlers in a block list was not the focus of       id attribute of a div tag. Next, an opening noscript
this work.                                                         tag is prepended again, and the generation terminates with
     Once an initial payload is selected, MutaGen randomly         the ⊥ transformation. This yields the list of transformations
selects transformations which, when applied to the current         given on the Generation side in Figure 4 top to bottom. To
payload, modify it. An example of such a transformation is         hand this sample to a sanitizer, it first has to be serialized
to prepend an opening tag such as div, i.e., transforming          into HTML code. Each step of this process is shown on the
P into <div >P . Upon reaching a predefined limit on the           right side (captioned Serialization) of Figure 4.
number of transformations (set to 25 for our experiment) or
selecting the termination transformation (denoted as ⊥), the       3.3. Payload Sanitization
generation is complete. The ⊥ transformation allows us to
generate payloads of varying length, as always applying 25             For each generated fragment, we now want to analyze
transformations results in payloads of uniform length. We          how different sanitizers process it. We selected the sanitizers
then check that the generated payload is unique, i.e., has not     in our testbed by searching the package repositories of
been generated by a prior run, and that it is not entirely made    JavaScript, .NET, Ruby, PHP, and Java for popular server-
up of whitespace or closing tags. Such a payload can never         side HTML sanitizers. We then inspected their source code
cause interesting behavior, as closing tags without opening        to determine whether they use an HTML parser that we can
tags are discarded. If both conditions hold, we serialize it to    access to retrieve its internal state.
its string representation and store both its abstract as well          Using an actual HTML parser is a necessary prerequisite
as its textual representation in a central database.               to be affected by parsing differentials, i.e., to be in scope for
     This approach allows us to trivially add transformations      our work. Therefore, we did not include any sanitizer that
that alter the whole accumulated payload, e.g., to perform         simply cleans the input based on, e.g., regular expressions.
XML encoding. We implemented the HTML fragment                     Attempting to process HTML via regular expressions is
generator in slightly over 1,100 lines of OCaml code; it           problematic in its own right but not the focus of this
manipulates payloads with 23 transformations, most of them         work. We refer the reader to [1, 9, 36–38] for security
                                                                        Table 2: Number of Evaluated and Executed Samples
assessment of such sanitization approaches. This allows us
to focus on detecting HTML parsing divergences and their              Sanitizer                         Evaluated         JS Executions
effects on sanitizers. To perform a meaningful analysis                                       Default        Lax         Default Lax
of different parsing behaviors, we also require access to
                                                                      None                    12,000,000                855,290
their internal state. That is, how did the underlying HTML
parser understand the input the sanitizer attempts to clean?          DOMPurify               1,770,812      2,210,713  0         341
This internal parsing state is not made public in any of the          DOMPurify (jsdom19)     1,518,562      1,716,177  31        154
considered sanitizers. Therefore, we added functionality to           sanitizer               2,721,962                 4,971
extract it. This was either done by setting appropriate hooks,        google-caja-sanitizer   2,866,299                 5,354
e.g., for DOMPurify, or by modifying the code, e.g., for              sanitize-html           1,347,494      4,330,265  0         0
Google Caja-based ones, while keeping the sanitization logic          HtmlSanitizer           7,512,576      7,652,333  0         966
untouched. Thus, for every sanitizer invocation, we store             HtmlRuleSanitizer       607,496        7,269,990  5,080     34,384
a DOM-like structure (representing the sanitizer’s internal           Typo3                   11,705,381     11,710,159 4,754     52,214
state) together with the sanitizer result. This allows us a           rgrove/sanitize         1,816,383      4,988,545  0         2,178
meaningful comparison between sanitizers. This resulted in            loofah                  4,452,547                 0         0
11 sanitizing libraries across 5 programming languages. Their         AntiSamy                5,473,627      6,696,708  7         2,116
exact version numbers as well as additional meta information,         JSoup                   5,970,206      8,132,379  0         13,265
are detailed in Table 1.

3.3.1. Sanitizer Configuration. Most of the tested sanitizers        the document’s body element, while for document parsing,
allow for a wide range of configuration options. Those usually       we directly insert it into the body of the page. This allows
include allowing or restricting additional tags, restricting         us to detect differentials between the parsing behavior of the
which attributes are allowed, and so on.                             two algorithms or bypasses that only manifest in either of
    We tested each sanitizer in its default configuration but        them.
also considered a more lenient variant, explicitly allowing              As modern web browsers are highly complex pieces of
all tags and attributes generated by our tool if such a              software, the evaluation step is rather time-consuming. To
customization is possible. loofah, a sanitizer for Ruby, or          ensure that – even under heavy system load – we do not
both Caja-based ones do not allow for such customizations.           miss any calls to the reporting function, we waited for 75 ms
Consequently, they are only tested in the default configura-         after inserting the payload into the page. Together with the
tion.                                                                surrounding setup code, such as opening a new page inside
    We did not attempt to enforce misconfigurations. One             the browser, evaluating a single payload took about 90 ms.
sanitizer in our test set, namely sanitize-html, requires setting
an aptly named flag (called allowVulnerableTags) to                  4. Parsing Differentials: Prevalence and Impact
enable some tags generated by MutaGen. We did not set
these, as the documentation clearly states that setting them             We generated 12 million unique payloads for this study.
renders the sanitizer pointless. Instead, we limited ourselves       The generation, sanitization, and evaluation pipeline took
to allowing tags via the regular mechanisms.                         14.5 days in total, running concurrently on a server powered
    Each generated payload was consequently sanitized by             by an AMD EPYC 7702P 64-Core CPU and 512GB of
every sanitizer from Table 1 in both their default and relaxed       main memory.         During the evaluation, each call to the
configuration. Their outputs were inspected to check whether         reporting function from our payloads was recorded, and the
they still contained a call to our reporting function, and if that   corresponding sample was marked as causing code execu-
was the case, they were marked for evaluation. In addition,          tion. The total numbers of samples marked for evaluation
every generated payload was also marked for evaluation               and samples causing JavaScript execution per sanitizer are
without sanitizing it first.                                         provided in Table 2.
                                                                         The number of evaluated samples already gives a hint
3.4. Payload Evaluation                                              about different strategies employed to clean input. Sani-
                                                                     tizers with few evaluations (e.g., sanitize-html or DOM-
    While the sanitizer’s parsing state is sufficient to deduce      Purify) remove problematic parts, while others, such as
parsing differentials between sanitizers, finding bypasses           the Typo3 sanitizer tend to keep the basic structure in
requires evaluating the output in a real browser. To do this,        place. An example to showcase this behavior is the payload
we leveraged the browser automation framework Playwright             <textarea><script>f(). One strategy is to delete
in version 1.27.0. It automates running Chromium, Firefox,           the content of textarea, e.g., employed by sanitize-html,
and WebKit in versions 107.0.5304.18, 105.0.1, and 16.0,             which in turn deletes the call to our reporting function, f ().
respectively. Our framework evaluates each sample marked             A second strategy, for example used by DOMPurify, is to en-
for evaluation in each browser and parsing mode combination.         code the content of textarea, i.e., turning <script>f()
That is, to ensure both document and fragment parsing modes          into &lt;script&gt;f(). Both approaches prevent the
are evaluated, each marked sample is evaluated twice. For            execution of the XSS trigger but have tradeoffs in terms of
fragment parsing, we assign the payload to innerHTML of              usability. Any benign content of such a textarea tag is
equally deleted when applying the first strategy. There is,                                 context
however, no correlation between employing either strategy
                                                                                              div
and being more susceptible to bypasses. HtmlRuleSanitizer,
sanitizer and google-caja-sanitizer are among those with the                       #text      img         #text
fewest evaluated samples in their default configurations but
have the most samples with JavaScript execution.                      Figure 5: DOM structure of <div>HT<img>ML
    Please note that payloads causing JavaScript execution
after sanitization are not a direct subset of those executing    however, would lead to an infeasible number of payloads to
JavaScript without sanitization. In total, 875,133 payloads      evaluate. Therefore, we set a very permissive configuration
were executed at least in one configuration. Without applying    in which we minimized the changes required for the specific
sanitization first, 855,290 payloads did cause JavaScript        bypass before reporting them.
execution. This means that 19,843 payloads did not execute
on their own but required the sanitization step to turn them
from a benign into a dangerous payload.                          4.1. Prevalence of Parsing Differentials
    One would expect the number of executed payloads to
be equal across browsers. This is not the case. Chromium             The reason for using an HTML sanitizer is to allow
executed 862,780 and 668,897 in document and fragment            the user to preserve some form of user-provided markup.
parsing mode, respectively, the numbers are fairly similar for   Suppose one wants to ensure input does not influence the
WebKit with 863,071 and 668,893 executions. Both browsers        website’s markup at all. In that case, the safe way is to
originate from the same code base, so similar behavior is        simply encode the input (cf. Section 2.3), ensuring only text
expected. For Firefox, however, the results are significantly    content ends up in the final document. Therefore, we assume
different. It executed 858,523 payloads in document and only     that users of these sanitizers expect them to remove only
497,941 payloads in fragment parsing mode. The reasoning         the actual XSS trigger and other forbidden elements while
for this significantly different number of executed payloads     preserving benign HTML structures as is. To do this, the
rests in a deviation from the specification for Firefox, which   sanitizer’s parsing result has to be as close to the browser’s
we detail in Section 4.4.                                        as possible. Otherwise, benign parts of the DOM might get
    Note that the number of executed samples for fragment        removed, degrading the website’s functionality.
parsing is lower across the board. This is expected, as              To assess the similarity between parsing results, we first
payloads using script tags as code execution triggers            select a metric to compare DOM trees.
never execute in fragment parsing mode.
    All payloads that executed JavaScript despite having         4.1.1. Bag of XPaths Similarity Score. The Bag of XPaths
been sanitized were marked as bypasses and consequently          metric [39] is one way to calculate the similarity between
analyzed. We filtered them for common root causes (i.e., two     two websites, i.e., DOM trees. Here, each document is
payloads containing the same issue and different surrounding     converted into a set of XML Path Language (XPath) ex-
markup) and disclosed the vulnerability to the respective        pressions, one for each leaf node in the DOM. For example
maintainers. This was greatly aided by us storing the internal   the fragment <div>HT<img>ML has the DOM structure
parsing result of each sanitizer, as it allows us to quickly     pictured in Figure 5 and is converted into three XPath ex-
asses what root causes led to the bypass. All bypasses found     pressions: /div[0]/text[0], /div[0]/img[0], and,
over the course of this study are summarized in Table 3. We      /div[0]/text[1]. To calculate the similarity between
did not break down the issues found in the two Caja-based        two documents D1 and D2 , we first compute the set of
sanitizers for brevity, as they are both unmaintained.           XPaths for both, resulting in n1 and n2 , respectively. We
    We were able to bypass all evaluated sanitizers except       then take the intersection of n1 and n2 to compute c and
sanitize-html and loofah. 6 out of 11 sanitizers were af-        apply Equation (1).
fected in the default configuration, which tends to be rather                                                 |c|
restrictive. For three additional sanitizers, we only found               similarity(D1 , D2 ) =                            (1)
                                                                                                      |n1 | + |n2 | − |c|
bypasses in the more permissive configuration. However,
due to each website having unique needs in terms of tags to      If two documents share no common XPaths, their similarity
allow, we assume that adjusting the default configuration is     is 0, and if they have exactly the same set of XPaths, i.e.,
commonplace. This can be seen when looking at libraries          their DOM trees are equal, the result is 1.0. We have slightly
such as AntiSamy, which ships with configurations taken          adapted the metric to better fit our setting. Compared to
from popular websites such as Slashdot or eBay. The              the original implementation of this metric, we omitted the
provided configurations contain very different allow lists,      notion of generalized XPaths, which are supposed to express
with the eBay one, for example, being very permissive, even      repeating patterns. Such patterns are very likely to occur
allowing tags such as noscript.                                  on actual websites, e.g., multiple rows of a table all have
    While the relaxed configuration set by us is extremely       the same structure. MutaGen, however, does not generate
permissive, all bypasses found by us usually only require        such structured markup. Therefore, generalized XPaths might,
adding one or two tags to the allow list, i.e., only a subset    at best, introduce noise in our case, as the generalization
is needed. Testing these different subsets independently,        would detect patterns where there are none. Additionally, we
                                             Table 3: Sanitizer Bypasses Found with MutaGen
 Id   Sanitizer name               Config.    Cause          Description                                                                 Status
      google-caja-sanitizer (*)
                                   Default                   Various                                                                     Abandoned Projects
      sanitizer (*)
 1    DOMPurify (jsdom 19)         Default    SI 6           Decodes and reflects text content                                           Independently fixed
 2    DOMPurify                    Relaxed    PI 1           noframes not parsed correctly                                               Resolved
 3    Typo3                        Default    PI 4           CDATA sections not parsed correctly                                         2022-23499 ‡
 4    Typo3                        Default    PI 5           Closing bang comment not detected                                           2022-36020
 5    Typo3                        Relaxed    PI 1           Namespace confusion                                                         2022-23499 ‡
 6    Typo3                        Relaxed    PI 2           noscript content parsed as HTML instead of as text                          2023-38500
 7    AntiSamy                     Default    †              Tags not listed in the configuration not handled securely                   Acknowledged
 8    AntiSamy                     Relaxed    PI 5           Closing bang comment not detected                                           Acknowledged
 9    AntiSamy                     Relaxed    PI 1           Tags with text content are not closed if they contain a comment             2023-43643
 10   HtmlRuleSanitizer            Default    PI 5           Closing bang comment not detected                                           Resolved
 11   HtmlRuleSanitizer            Relaxed    PI 1           Wrong parsing of tags with text content allows to break out of attributes   Reported
 12   HtmlSanitizer                Relaxed    PI 2           noscript content parsed as markup.                                          Resolved
 13   HtmlSanitizer                Relaxed    PI 3           Firefox parsing differential                                                Acknowledged
 14   rgrove/sanitize              Relaxed    PI 2           noscript content parsed as markup instead of as text                        2023-23627
 15   JSoup                        Relaxed    PI 3           Namespace confusion                                                         Resolved
 16   JSoup                        Relaxed    PI 2           noscript content parsed as markup instead of as text                        Resolved
†: Logic bug. *: Based on the same code base, largely affected by the same vulnerabilities. ‡: Two separated vulnerabilities got grouped into this CVE.


added the notion of text nodes. The original metric is only                       internal representations to all have the same shape. The
concerned with the relationship between tags. However, if                         results are provided in Table 4. If the sanitizer’s HTML
text nodes are moved from one tag to a different one during                       parser would perfectly match the browser’s, the similarity
sanitization, this has a profound impact on the rendering of                      score would be 1.0. A score of below 0.5, on the other hand,
the resulting fragment. Thus, we decided to add text nodes as                     means that for two DOM trees, more than half of their leaf
well. The same applies to comments and CDATA sections                             nodes only occur in either DOM tree. That is, they differ by
if the parser recognizes those. While they do not influence                       a significant amount.
the rendering, parsing them incorrectly leads to a different                          As the table shows, the similarity scores vary greatly
result upon serialization. To model this influence, we also                       between sanitizers. While some (e.g., DOMPurify, HtmlSan-
add XPaths for text, comment, and CDATA nodes, as they                            itizer or rgrove/sanitize) are operating on a fairly accurate
are always leaf nodes.                                                            internal structure, others such as HtmlRuleSanitizer produce
                                                                                  wildly different parsing results.
Table 4: Similarity of Sanitizers and Browsers Parse Tree.                            Interesting to note is that while the similarity of fragment
 Sanitizer                    Chrome           Webkit            Firefox          and document parsing modes are very similar for Chromium
                             F     D          F      D          F       D         and WebKit, the scores for Firefox diverge noticeably. This
 DOMPurify                  0.87    0.87     0.87     0.87    0.81     0.86
                                                                                  is a result of the Firefox fragment parser deviating from the
 DOMPurify (jsdom19)        0.88    0.88     0.88     0.88    0.82     0.88       specification, which we discuss in depth later on.
 sanitizer                  0.36    0.36     0.36     0.36    0.37     0.36
 google-caja-sanitizer      0.50    0.50     0.50     0.50    0.50     0.50
 sanitize-html              0.39    0.39     0.39     0.39    0.41     0.39
                                                                                  4.3. Classifying Parsing Deficiencies
 HtmlSanitizer              0.90    0.90     0.90     0.90    0.84     0.90
 HtmlRuleSanitizer          0.15    0.15     0.15     0.15    0.15     0.15           As shown previously, the different parsers do not always
 Typo3                      0.52    0.52     0.52     0.52    0.53     0.52       accurately parse their inputs, compared to the major browsers.
 rgrove/sanitize            0.94    0.94     0.94     0.94    0.88     0.94       Having access to the sanitizer’s internal representation allows
 loofah                     0.22    0.22     0.22     0.22    0.25     0.22
 AntiSamy                   0.58    0.58     0.58     0.58    0.58     0.58       us to also analyze where their HTML parsers violate the
 JSoup                      0.51    0.51     0.51     0.51    0.52     0.51       specification. Such violations do not necessarily imply a
F: fragment parsing, D: document parsing                                          security issue but, especially when several can be combined,
                                                                                  are often building blocks for bypasses. In any case, they are
                                                                                  functional deficiencies, frequently manifesting as overzealous
4.2. Parsing Accuracy                                                             transformations of the output.

     We calculate this by retrieving the resulting DOM trees                     4.3.1. Parsing. We found five distinct parsing issues (PI),
after rendering each unsanitized payload in all browsers                         each affecting one or more different sanitizers.
and configurations and comparing them to the internal                            1: Incorrect Parsing of Tags with Text Content Several tags
representation of the sanitizer. Due to implementation                           instruct the parser to switch to parsing modes recognizing
differences, these internal DOM-like structures can look                         textual content such as RCDATA [40]. In the RCDATA
fairly different. DOMPurify, for example, creates a complete                     state, the parser interprets everything between the opening
HTML document with head and body sections, while others                          tag until a matching closing tag as text, decoding character
operate on a document fragment. Thus, we first unify the                         references in the process. If the parser does not model these
transitions, it parses the text content as if it were HTML          ing result is <svg><desc><div>X</div></desc>
markup. This can allow an attacker to trick the parser into         </svg><img>. Both div and img are among the tags
parsing regular markup as if it were an attribute. Consider         terminating foreign content. The desc tag, however, serves
the string: <iframe><div id=’</iframe>’>. Upon                      as an HTML integration point, allowing the div tag to
encountering an opening iframe tag, the parser switches to          be part of the svg block. Meanwhile, upon encountering
the RCDATA state, everything up until the closing iframe            the img tag without such a preceding integration point, the
tag is parsed as text and added as a text node below the            parser closes all open SVG tags and attaches the img directly
iframe node. If the sanitizer does not model this transition        to the parent node. To correctly model the behavior of each
from HTML parsing to text parsing, it would parse the string        tag, the parser has to be aware of the tag’s namespace, and
as if the iframe had a div node with an id attribute                as such, it has to model these namespace transitions. Failing
containing the string </iframe> as its child. Then, the             to do so, e.g., by attaching the img tag as a child of the
parser continues to look for further child elements of the          svg element, falls into this category.
iframe node until a top-level closing iframe tag occurs.                 We detect this by first assigning namespace labels ac-
Effectively, the parser attaches content that should be outside     cording to the specification. This allows us to scan the DOM
of the iframe tag as its children. This problem class               for invalid states, such as an img tag as a child of a svg
affects all tags that have textual content, namely textarea,        tag.
xmp, noframes, noembed, iframe, title, style                        4: Incorrect CDATA Handling XML documents allow
and plaintext.                                                      enclosing content that shall be interpreted literally and not
     One possibility for why this error occurs is using a regular   parsed as markup in so-called CDATA sections. It can be used
XML parser to parse HTML documents, as XML does not                 to represent text containing special characters or XML syntax
have such transitions. This problem only applies to tags in         without additional escaping. A CDATA section is written as
the HTML namespace; if, e.g., a xmp tag was parsed as SVG,          follows: <![CDATA[<b> to emphasize]]>.
it would have regular content. As sanitizers do not tend to              While HTML is derived from SGML, the parser
make namespace information (if they are aware of it in the          treats CDATA sections outside of foreign content as
first place) available, we automatically labeled their DOM          errors. As HTML parsing never fails, it also speci-
trees with the namespaces based on the rules for namespace          fies how erroneous CDATA sections shall be handled:
transitions from the parsing specification [24].                    the opening [CDATA] and closing ]]> strings shall
     The detection approach for this issue class works as           be treated as comments [42]. This handling, however,
follows: Examine the children of all nodes, which, according        is rather unintuitive. <![CDATA[a<b]]> is treated as
to the specification, shall only have text children. If at least    <!--[CDATA[a<b]]-->, matching the specification.
one child is not a text node, the parser is affected by PI 1.       However, if the CDATA section does contain a clos-
2: Incorrect Parsing of noscript This case is a special             ing angle bracket, the resulting comment terminates
case of PI 1, but due to additional complexities, it is             early. The input <![CDATA[<b><t>)]]> is parsed as
listed separately. The noscript tag has unusual parsing             <!--[CDATA[<b--><t>)]]&gt;, with the t tag out-
semantics, even for the convoluted HTML specification.              side of the comment and part of the regular DOM. If a
Its semantics rely on a parsing state flag, the scripting           parser expects the CDATA section as a whole to be treated
flag [41], which signals JavaScript support. In the case            as a comment, it is at risk for a bypass based on the second
of JavaScript support, the content of noscript shall be             example. If the tag t was an XSS payload instead, the
parsed as text, otherwise as markup. This feature was used          parser would see the payload as part of a comment and thus
to provide fallback solutions to legacy browsers without            harmless. If a CDATA node containing one or more closing
JavaScript support. While such browsers do exist, they are          angle brackets is returned in the DOM, we mark the sample
outside the threat model of XSS attacks. A sanitizer parsing        as causing PI 4.
noscript as if no JavaScript support was available is at            5: Closing Bang Comments HTML specifies the syntax
risk for bypasses. This class can be detected in the same           for comments as: <!-- content -->. However, it also
fashion as PI 1.                                                    accepts incorrectly closed comments, that is, comments
3: Foreign Content and Namespace Transitions When                   closed with --!> [43]. If an HTML parser misses this detail,
parsing foreign content, i.e., SVG or MathML segments, sev-         it would treat a string such as <!-- c--!><t>--> as if
eral integration points are available to switch the parser back     the t tag was inside the comment. This allows the smuggling
to HTML mode. For example, via the foreignObject                    of XSS payloads through comments if they are included in
tag, a piece of HTML can be embedded into an SVG graphic,           the output. We detect this issue by scanning the DOM for
allowing the reuse of CSS styles. Similar integration points        comments containing the string --!>.
exist for MathML, e.g., mtext. It is important to note that
they integrate an HTML block into the foreign content.              4.3.2. Serialization. To return the sanitized result to the
     A number of HTML tags also have special meaning inside         caller, the sanitizer has to turn the internal representation
foreign content [24]. Instead of a seamless integration, they       back into its textual form, called serialization. This section
however instruct the parser to close the currently open non-        is concerned with problematic implementations of the seri-
HTML elements. As an example, consider <svg><desc>                  alization step. The serialization usually is implemented in
<div>X</div></desc><img>. Consequently, the pars-                   the HTML parser, but if it does not handle these aspects
securely, the sanitizer should take care of them to avoid easy      Table 5: Parsing and Handling Issues Affecting Each Sanitizer
bypasses. We derived two categories of serialization issues
                                                                                                             Parsing                 Serialization
(SI) the bypasses are based on.




                                                                                               PI 1

                                                                                                      PI 2

                                                                                                               PI 3

                                                                                                                       PI 4

                                                                                                                              PI 5

                                                                                                                                     SI 6

                                                                                                                                            SI 7
6: Decodes Text Values The HTML specification instructs              Sanitizer
the parser to decode character references. Character refer-
                                                                     AntiSamy
ences have the form of e.g., &lt; to encode <. To render a
                                                                     sanitizer                        #                #      #      #
document, a browser has to decode such character references,
                                                                     google-caja-sanitizer            #                #      #      #
as is mandated by the specification. However, if a sanitizer
decodes character references and does not encode them again          DOMPurify                                         #      #             G
                                                                                                                                            #
during serialization, there is potential to make the sanitizer       DOMPurify (jsdom19)                               #      #
turn benign input into dangerous output. This issue can              HtmlSanitizer                                     #      #      G
                                                                                                                                     #      #
                                                                                                                                            G
occur in several parts of the DOM, namely inside text nodes,         HtmlRuleSanitizer                                 #             #
attributes, or comments.                                             JSoup                                                    #      G
                                                                                                                                     #      #
                                                                                                                                            G
     Based on the abstract representation of the generated           loofah                                            #      #      #      #
payload, we can easily derive which encodings were applied           sanitize                                  H
                                                                                                               #       #      #             G
                                                                                                                                            #
to the XSS trigger. If at least one encoding was applied and         sanitize-html                                     #      #      #      #
the decoded payload can be found inside one of the named             Typo3                                                                  #
node types, the sanitizer is affected by PI 6.                        : Affected, G
                                                                                  #: Affected in relaxed configuration, #: Unaffected,
7: Failure to Encode Text Values Nodes parsed as text               H
                                                                    #: Affected but not in scope of threat model
that the sanitizer does not encode during serialization are a
significant risk for bypasses. If there is a parsing differential       The first problematic aspect is the correct parsing of
between the sanitizer and the users’ browser, the assumed           tags with textual content. Every analyzed parser fails at this
text node might be parsed as markup and a trivial bypass            task for at least some samples. Similarly, the handling of
occurs. An example of how this can occur is <select>                noscript, which not only requires a parsing transition
<iframe><script>f(), one of the bypasses affecting                  but also relies on runtime information in the browser, is a
both Caja-based sanitizers. According to the specification,         frequent source of mistakes. How HTML parsers implement
the content of iframe tags shall be parsed as text. Conse-          this aspect differs, with some requiring users to pick a value
quently, <script>f() would be seen as benign content                for the scripting flag, e.g., as AngleSharp for .NET. Others,
and attached as a text node below it. However, when a               such as the Nokogiri HTML parser for Ruby, do not offer
browser parses the whole fragment, it behaves differently.          a choice at all. The sensitive default for sanitization code
An iframe tag violates select’s content model. The                  would be to default to scripting being active. Only the Google
select tag can only contain option, optgroup, hr tags               Caja-based sanitizers had this setting, however.
and “script supporting elements” [44]. Script supporting ele-           If the parser is mainly used for tasks such as web scraping,
ments include script and template tags. Consequently,               defaulting to false seems sensible. It is, however, a potential
an iframe is not a valid child of select, and the browser           security issue, as bypasses 6, 16 and 14 show. This quirk
drops it during tree construction. This turns the supposedly        received considerable media attention in 2019 when Masato
harmless text node into markup that is regularly parsed, and        Kinugawa found a bypass in the Google Search Bar [45]
the script is finally executed.                                     based on the duality of noscript. Nevertheless, as our
     To defend against such attacks, a sanitizer would have         results show, this has not led to awareness for authors of
to consequently encode all text nodes and attribute values.         sanitizing libraries.
Performing such encoding would have prevented all bypasses              Foreign content (PI 3) is similarly a common source
from Table 3 but bypass 1 and 7. We detect missed encoding          of mistakes. The rules on when to switch namespaces are
steps by checking if the XSS trigger is located inside a text       not correctly implemented in any analyzed sanitizer. All
node or attribute value in the sanitizer’s internal DOM and         sanitizers we were able to bypass are also affected by at
whether it occurs in the output in unencoded form.                  least one serialization issue, as those bypasses usually rely
                                                                    on a parsing mistake combined with a lack of encoding to
4.3.3. Affected Sanitizers. Table 5 breaks down what                succeed. Interestingly, HtmlRuleSanitizer allows the user to
sanitizers are affected by which parsing or serialization issues.   configure if HTML entities in text nodes shall be encoded.
In summary, we detected functional deficiencies in every            Giving control to the user might seem desirable, but without
analyzed parser and problematic handling of text values in all      additional warning, enabling this option allows to trivially
but two. The two sanitizers not affected by either serialization    bypass the sanitizer.
issue, i.e., those that do not remove encodings from their
input and consequently encode text nodes, are the two where         4.4. Browser Parsing Differentials
we found no bypasses.
    The fact that each parser is at least affected by two parsing       Another issue for authors of sanitization routines is
issues is cause for concern and highlights the complexity of        the aspect that browsers might diverge from the HTML
the parsing task.                                                   specification in some cases. Firefox’s fragment parser, for
                                              context              5. Discussion
   context
                                                svg
             svg
                                                                       The results presented in the previous section paint a dire
                                               embed               picture of the state of server-side HTML sanitization, directly
             embed                                                 answering the initial questions. Due to the lack of information
                                               iframe
                                                                   available to the sanitizers, it is not feasible to build one that
             iframe                             desc               is both accurate and secure, and popular sanitizers fall well
                                                                   short of this goal.
                      #text                     img                    We now discuss some problematic aspects in depth,
(a) Chrome parsing result            (b) Firefox parsing result    detail the disclosure process, explain how to mitigate XSS
                                                                   vulnerabilities in the presence of parsing differentials and
Figure 6: Parsing differential between Chrome and Firefox.         finally provide a general outlook.
Blue nodes have the HTML namespace, green ones SVG.
                                                                   5.1. Foreign Content

                                                                        The fact that HTML allows embedding foreign content,
example, does not parse foreign content correctly, i.e., it is     i.e., SVG or MathML snippets, adds significant difficulties
affected by PI 3. Instead of closing the foreign namespace         for authors of parsing and sanitization libraries. As every
upon encountering an HTML tag supposed to terminate                namespace transition changes the semantics of several tags,
foreign content, it stays in the current parsing mode. Nor-        missing even a single one is often enough to introduce
mally, this simply results in a website being rendered             a vulnerability. As shown in the previous Section, none
incorrectly. However, such differences can be abused to            of the tested sanitizers implement this correctly, and even
bypass sanitizers as well. A payload exemplifying this is-         the major browsers do not always get it right. This makes
sue is <svg><embed><iframe><desc><img src=x                        the question of how sanitizers should handle such mixed
onerror=f()>. The parsing results for Chromium (Fig-               documents an interesting one. rgrove/sanitize deviates from
ure 6a) and Firefox (Figure 6b) are provided in Figure 6.          the remaining libraries, as it explicitly warns that it does
Chromium terminates the SVG context upon encountering              not support sanitization of foreign content. It defaults to
the embed tag and parses the remaining input as HTML.              simply removing everything it parses as foreign content,
Therefore, the opening desc and the image tag are parsed           which frequently includes regular HTML content due to
as text and attached under the iframe node, preventing the         not implementing the complex namespace transition rules.
execution of the error handler. Firefox, on the other hand,        This warning is not enforced in the library itself, as it is
parses both embed and iframe as SVG tags, causing them             possible to add the offending tags to its allow list without
to lose their HTML semantics. Then, upon encountering              further warning. We have reported issues related to incorrectly
desc, the parsing rules for SVG apply, and the parser              parsing foreign content to rgrove/sanitize’s maintainers, and
switches back to HTML [46]. Consequently, Firefox parses           they added additional protection mechanisms, such as always
the img tag as a regular HTML tag and executes its                 escaping the content of text nodes.
onerror handler, calling f . A sanitizing routine purely
relying on the specification to assess whether a tag needs
                                                                   5.2. Weaponizing Sanitizers
sanitization is, therefore, vulnerable to bypasses such as the
one described here. Thus, to accurately sanitize input, a
sanitizer either has to be aware of all possible browser quirks         Surprisingly, in some cases, the sanitizer turned ini-
or put users of selected browsers at risk. Without information     tially harmless HTML fragments into a dangerous pay-
about the browser of the specific user, it then has to find        load. Such cases occur if the sanitizer relies on the
the lowest common denominator, degrading its output. We            underlying parser’s serialization functionality. DOMPu-
found the example provided above during our study affecting        rify, using jsdom v19, was affected by such an issue,
HtmlSanitizer with a relaxed configuration (bypass 13).            namely bypass 1. When sanitizing <svg><style>&lt;
                                                                   img src=x onerror=f()&gt;<keygen> the sani-
    Resolving this issue has proven to be involved, as it is       tizer recognized the escaped img tag as harmless text.
unclear who is responsible for fixing such bugs. A sanitizer       It then returned the string <svg><style><img src=x
adding a workaround for a browser bug would degrade the            onerror=f()> which is clearly problematic. During se-
output for compliant browsers. Not fixing it, however, leaves      rialization, the XML encoded text node, i.e., the img tag,
users of non-compliant browsers at risk.                           got decoded, which armed the payload. The presence of
                                                                   a trailing void (i.e., self-closing) element caused jsdom to
     We have reported this parsing differential to Mozilla, and    XML decode the text node, which was then picked up by
it awaits resolution at this time. Please note that this example   the browser’s DOM parser. This validates the inclusion of
also manifests in a more involved form. For example, we            destructive transformations, such as encoding operations, for
detected payloads for JSoup where this difference allows           our payload generation. URI encoding, on the other hand,
lifting the payload from an attribute value.                       was never reverted by any tested sanitizer.
5.3. Disclosure Process                                           with the high rate of proposals being made toward the web
                                                                  platform, increasing the maintenance effort for sanitizing
    We divided the disclosure process into two parts: vulner-     and parsing library authors. One recent example of this
abilities and functional deficiencies. Each sanitizer bypass      churn is the deprecation of Bleach, an HTML sanitizer for
puts a considerable amount of website operators at risk of        Python [48]. It relied on an unmaintained HTML parser,
exploitation and, consequently should be resolved quickly.        leading the maintainer to the conclusion that attempting to
All vulnerabilities stemming from parsing differentials can       build upon an unreliable foundation is futile.
be prevented without solving the underlying issue. This               Thus, a long-term vision for input sanitization is required.
usually requires degrading the output quality but might be an     Such a vision is developing on the client side, thanks to
attractive short-term solution. Resolving parsing issues such     the Sanitizer API [14]. Ensuring the browser ships with a
as PI 3 or PI 1, on the other hand, often requires fundamental    secure by default sanitizer, which guarantees to keep up with
reengineering of the parser itself. We are currently working      changes to the HTML and related standards, prevents a large
on reporting the parsing issues discussed in Section 4.3.3        class of XSS vulnerabilities. On the server side, such a
as well as more basic parsing errors we uncovered to their        unified solution is not feasible. Due to the heterogeneous
respective maintainers. HtmlRuleSanitizer for example parses      ecosystems found on the web, a one-size-fits-all sanitizer
the input <div id= <div> as <div id=""><div>.                     is not possible. In addition, the update situation remains
This behavior does not follow the specification, which            problematic, as a deployed sanitizer can get out of sync
mandates it to be parsed as <div id="<div/">.                     with the HTML, SVG, or MathML specification. On the
Vulnerability Disclosure. We contacted the corresponding          client side, this is solved by automatic updates employed
maintainers of all actively maintained libraries from the test    by all major browsers. Server-side dependency management
set regarding our findings. At the time of writing, most of       solutions (e.g., npm) require manual intervention to install
them have been fixed, as shown in the Status column in            updates, with popular websites being slow to deploy new
Table 3.                                                          versions [49].
    As the main focus of DOMPurify [47] lies on client-side           One helpful aspect could be to provide an HTML parsing
usage, using it on the server is more involved. Here, it relies   reference implementation, usable for differential testing.1
on an external HTML parsing library to produce a DOM              This would require a commitment from the browser vendors
tree, with the manual recommending jsdom. The chosen              to resolve parsing divergences but would greatly simplify
HTML parsing library then has to be manually installed and        the validation of new parsers. Approaches such as the one
managed. Consequently, updating DOMPurify itself does             presented here could then provide a large corpus of parsing
not update the underlying parser. This opens the door for         edge case inputs against which new implementations can be
vulnerabilities to persist, as parsing differentials in jsdom     validated. To facilitate this process, we are currently working
itself are no security issues. This requires users to assess      on turning the samples with diverging behavior into tests
the necessity for updating jsdom without any aid from the         and submitting them to the Web Platform Tests project [50]
library. While bypass 1, affecting DOMPurify in its default       (WPT). WPT currently serves as a benchmark on how well
configuration, had been independently fixed in jsdom version      different browsers implement various aspects of the web
20 before we were able to report it, deployment of the fix        platform. As the major browser vendors monitor their WPT
required manually updating jsdom.                                 scores, this hopefully helps to shine light on these issues.
    We, therefore, searched for open-source projects using            While rooting out parsing differentials reduces the likeli-
the vulnerable combination of DOMPurify and jsdom in              hood of sanitizer bypasses, vulnerabilities due to logic errors
version 19 to disclose our findings. This did affect projects     will remain. As every software contains bugs, especially
from Mozilla and Grafana Labs, and they have resolved the         when dealing with a byzantine topic such as parsing HTML,
issue by now.                                                     a second layer of defense is required.
    The two libraries based on Google Caja, i.e., google-caja-
sanitizer and sanitizer, are abandoned projects relying on        5.5. Mitigating Sanitizer Bypasses
the Caja codebase, which is itself abandoned. Consequently,
reporting bugs in those libraries is infeasible, as they simply       Several approaches have been proposed to prevent server-
repackage the Google code. Therefore, we are currently            side XSS vulnerabilities, including document structure in-
analyzing open-source projects using a Caja-based sanitizer       tegrity [51] or Noncespaces [52], both attempting to clearly
to see whether they are susceptible to the bypasses we found.     differentiate user-provided content from regular markup.
So far, this led to a change in sanitizers in an Adobe project,   However, none of these proposals made it into the web
but it is an ongoing effort.                                      platform itself.
                                                                      The most realistic solution today is deploying a se-
5.4. Outlook                                                      cure Content Security Policy (CSP) to enforce the sep-
                                                                  aration of markup and code. A sufficiently strict CSP,
    Many of the defects uncovered in the work are rooted
in the overwhelming complexity of the HTML specification.            1. One can argue that developing a reference implementation together
While resolving them improves the state of server-side sani-      with updates to the specification should also improve its structure, as related
tization, the fundamental problem persists. This is coupled       information is frequently scattered across several places at the moment.
1   <script nonce="rAnd0m">g('HTML');</script>                      6.1. (Differential) Fuzzing of Web Technologies
2   <script>f();</script>
                                                                        Detecting vulnerabilities via automated test case gen-
 Figure 7: Two inline scripts, one with nonce and one without       eration is the domain of the so-called fuzz testing. When
                                                                    applied to the web, it is mainly used to detect memory
                                                                    errors inside the browser. Fuzzing JIT compilers to detect
which, e.g., bans inline event handlers and requires                miscompilations leading to crashes and potential remote
nonces or hashes to execute inline scripts, would pre-              code execution vulnerabilities is a particularly active field
vent typical XSS vulnerabilities, even in the presence              of research [e.g., 59–61]. Similarly, the browser’s HTML
of a sanitizer bypass. Such a CSP realizing such a                  parser implementation can and has been tested via fuzzing,
separation could look like this: script-src ’self’                  for example, by Xu et al. [62] with FREEDOM.
https://jscdn.com ’nonce-rAnd0m’;. This pol-                            Semantic errors, i.e., bugs that do not manifest in crashes
icy allows loading JavaScript files from both the same origin       but unexpected or undesirable behavior, are a target less
as the site (due to the ’self’ source) as well as from              frequently considered for automated testing. This is due
jscdn.com over HTTPS. Additionally, it allows inline scripts        to fuzzing relying on so-called oracles to detect unexpected
declared with nonce attribute set to r4nd0m. Inline event           behavior. Adding an oracle to detect, e.g., buffer overflows
handlers and scripts without a matching nonce are blocked.          only requires compiling the browser with modified settings.
In Figure 7, the first script declares a nonce matching the         Creating an oracle detecting semantic issues is much more
header, and g(’HTML’) executes. The second script has               involved, as it requires analysis of the semantics of the
no nonce attribute and is blocked due to the CSP. Such a            application output.
separation requires care, however. This nonce-based approach            One recent example where fuzzing was applied to detect
is easily defeated by directly putting attacker-controlled input    semantic errors is by Kim et al. [63], who searched for
into the script’s content, e.g., if an attacker can influence the   universal cross-site scripting (UXSS) vulnerabilities. UXSS
value ’HTML’.                                                       is universal in the sense that it does not only affect a single
    In general, deploying secure CSPs has proven to be              origin but allows the attacker to run their code in all origins.
challenging for most websites. Difficulties stem from third-            A fuzzing technique focused on detecting divergences
party code relying on inline scripts, forcing to forgo strict       in behavior among different implementations for the same
separation of markup and code by requiring directives such          specification is differential fuzzing [64]. Here, inputs are gen-
as unsafe-inline, which break the separation as shown               erated and fed into several applications that, if correct, should
by Steffens et al. [53]. Integrating third-party code is far        behave the same. Differential fuzzing has been successfully
from the only issue with deploying secure CSPs, as a wide           applied to detect bugs in JavaScript JIT compilers [59],
range of research shows [e.g., 54–57].                              CPUs [65] and implementations of various protocols [66–
                                                                    68] or specifications [69]. While we consider a similar setting,
 5.6. Limitations & Future Work                                     applying differential testing to HTML parsing is problematic.
                                                                    When validating a certificate, implementations are expected
                                                                    to always return the same result. This is not necessarily the
    In its current version, MutaGen only generates outputs          case for HTML parsing, as some aspects are underspecified
containing HTML, SVG, and MathML structure. All three               and the negative consequences much less obvious.
of these are syntactically similar. Consequently, all sanitizers
process them accordingly. However, HTML has additional              6.2. Cross-Site Scripting
integration points. Both CSS (Cascading Style Sheets) as
well as JavaScript can be integrated directly into HTML                 As the most prevalent vulnerability class on the web,
documents. As they are entirely different from a syntactical        XSS has undergone extensive study.
point of view, sanitizers must implement additional parsing             Client-side XSS is the easiest to detect, as it takes place
modes to support this. Some of the tested sanitizers, such as       inside the client’s browser. Using a taint-tracking enabled
AntiSamy, do this, for example, by integrating an additional        browser, one can readily detect data flows susceptible to
parsing library for CSS. However, the interaction between           client-side XSS. This approach was successfully used to
these languages is also a cause for bypasses, highlighted           study the prevalence of client-side XSS [3–6, 8], improved
by a recent vulnerability in rgrove/sanitize [58]. Extending        exploit generation strategies [7] and potential defenses [70].
MutaGen to generate such payloads might be an exciting              Similarly, Steffens et al. [71] studied the prevalence of client-
opportunity for future work.                                        side stored cross-site Scripting via dynamic taint tracking.
                                                                    The most related aspects to this work are those covering the
                                                                    generation of XSS exploit payloads [e.g., 3–7]. However, all
 6. Related Work                                                    the noted works rely on detailed insights into the application
                                                                    gained via taint-tracking to craft targeted exploits. Our
     We group related work into three categories: (differential)    approach, on the other hand, has no information into the
 fuzzing of web technologies, differential fuzzing, cross-site      inner workings of the sanitizers or the browser’s HTML
 scripting, and security analysis of sanitizing routines.           parser.
     The complexity of HTML parsing and its impact on              parsing algorithms, but we were also able to bypass all but
sanitizers has received less attention. Louw and Venkatakr-        two of them automatically. These findings highlight the sorry
ishnan [72] suggested circumventing this issue by making the       state of server-side HTML parsing and sanitization, a topic
browser build the DOM programmatically without relying             left unexplored for far too long.
on it parsing the response in the same fashion. Simplifying
the HTML specification is another seemingly attractive idea.       Acknowledgments
By removing problematic tags and features, most of the
issues presented in this work could be prevented. However,             We gratefully acknowledge funding by the Deutsche
according to a recent study by Hantke and Stock [19], a large      Forschungsgemeinschaft (DFG, German Research Founda-
                                                                   tion) under Germany’s Excellence Strategy – EXC 2092
portion of Websites rely on HTML parsing quirks. Thus,             CASA – 390781972 as well as from the European Union’s
simplifying the parsing process is not a realistic option in the   Horizon 2020 research and innovation programme under
near future. mXSS vulnerabilities have seen comparatively          project TESTABLE, grant agreement No 101019206.
little academic attention, with only the seminal work by
Heiderich et al. [25] covering it in depth. Its primary focus,     References
however, was on browser-based mXSS vectors, while we               [1]  D. Klein, T. Barber, S. Bensalim, B. Stock, and M. Johns, “Hand
focus on what they called “mutation based attacks” [25].                Sanitizers in the Wild: A Large-scale Study of Custom JavaScript
                                                                        Sanitizer Functions,” in European Symposium on Security and Privacy,
6.3. Sanitizer Analysis                                                 2022.
                                                                   [2] K. Kotowicz, “Trusted types - mid 2021 report,” https://research.
                                                                        google/pubs/pub50512, Google Research, Tech. Rep., 2021.
    A lot of work has studied the security properties of           [3] S. Lekies, B. Stock, and M. Johns, “25 Million Flows Later: Large-
HTML sanitizers, both on the client [1, 9, 37] as well on the           scale Detection of DOM-based XSS.” in Conference on Computer
server-side [36, 73–75]. However, These works focus on                  and Communications Security, 2013.
implementation mistakes in the actual sanitizer code, i.e., by     [4] W. Melicher, A. Das, M. Sharif, L. Bauer, and L. Jia, “Riding
                                                                        out DOMsday: Towards Detecting and Preventing DOM Cross-Site
analyzing string modification chains. The bugs we consider              Scripting.” in Network and Distributed Systems Security, 2018.
are frequently outside the sanitizer’s direct control due to       [5] B. Stock, M. Johns, M. Steffens, and M. Backes, “How the Web
the used HTML parsers returning false parsing results.                  Tangled Itself: Uncovering the History of Client-Side Web (In)Security.”
    That relying on custom HTML parsing code is prob-                   in USENIX Security Symposium, 2017.
                                                                   [6] B. Stock, S. Pfistner, B. Kaiser, S. Lekies, and M. Johns, “From
lematic has been highlighted by and integrated into DOM-                Facepalm to Brain Bender: Exploring Client-Side Cross-Site Scripting.”
Purify [47]. However, as shown in Section 4, the chosen                 in Conference on Computer and Communications Security, 2015.
approach only works reliably on the client, as the sanitizer       [7] S. Bensalim, D. Klein, T. Barber, and M. Johns, “Talking About
can access the browser’s HTML parsing logic.                            My Generation: Targeted DOM-based XSS Exploit Generation using
                                                                        Dynamic Data Flow Analysis,” in European Workshop on Systems
                                                                        Security, 2021.
7. Conclusion                                                      [8] D. Klein, M. Musch, T. Barber, M. Kopmann, and M. Johns, “Accept
                                                                        All Exploits: Exploring the Security Impact of Cookie Banners,” in
    While HTML has an official specification codifying                  Proc. of the Annual Computer Security Applications Conference, 2022.
                                                                   [9] D. Bates, A. Barth, and C. Jackson, “Regular Expressions Considered
expected parsing behavior, implementing it correctly is                 Harmful in Client-Side XSS Filters,” in WWW, 2010.
challenging. This even affects the major browsers, which can       [10] F. Hantke, S. Roth, R. Mrowczynski, C. Utz, and B. Stock, “Where
not always agree on how a piece of markup shall be parsed.              are the red lines? towards ethical server-side scans in security and
The situation is even worse for server-side HTML sanitizers             privacy research,” in IEEE Symposium on Security and Privacy, 2024.
                                                                   [11] J. Weinberger, P. Saxena, D. Akhawe, M. Finifter, E. Shin, and D. Song,
despite them being an integral part of most websites’ security          “A Systematic Analysis of XSS Sanitization in Web Application
apparatus. On the server, HTML sanitizers are fighting a                Frameworks,” in ESORICS, 2011.
losing battle, as they do not have sufficient information to       [12] M. Samuel, P. Saxena, and D. Song, “Context-sensitive auto-
accurately parse attacker-controlled input in the same way              sanitization in web templating languages using type qualifiers,” in
                                                                        Conference on Computer and Communications Security, 2011.
a browser does. The used parsing mode, dynamic parsing             [13] P. Saxena, D. Molnar, and B. Livshits, “SCRIPTGARD: Automatic
state flags, the employed browser, and its quirks are all               Context-Sensitive Sanitization for Large-Scale Legacy Web Appli-
information out of reach for the sanitizer. Lacking this                cations,” in Conference on Computer and Communications Security,
information, it has to make an educated guess, frequently               2011.
                                                                   [14] W. P. I. C. Group, “HTML Sanitizer API,” https://wicg.github.io/
with devastating consequences. Parsing differentials, i.e.,             sanitizer-api, 2022, accessed 8.12.2023.
diverging parsing behaviors between sanitizer and browser,         [15] ——, “HTML Sanitizer API,” https://wicg.github.io/sanitizer-api/
are one consequence of these problems and a direct security             #strings, 2022, accessed 8.12.2023.
threat: Either allowing nefarious actors to bypass the sanitizer   [16] WHATWG, “HTML Standard: 1.7 Design Notes,” https://html.spec.
                                                                        whatwg.org/#design-notes, accessed 8.12.2023.
completely or to abuse the supposed protection mechanisms,         [17] D. Megginson, “SAX,” http://www.saxproject.org/, 2004, accessed:
making it transform benign input into harmful exploits.                 8.12.2023.
    In this paper, we presented MutaGen, a generator for           [18] WHATWG, “HTML Standard: 13.2.10.3 Unexpected markup in tables,”
mutation-prone pieces of HTML. Using MutaGen and our                    https://html.spec.whatwg.org/multipage/parsing.html#unexpected-
                                                                        markup-in-tables, accessed 8.12.2023.
evaluation testbed, we assessed how 11 sanitizers across five      [19] F. Hantke and B. Stock, “HTML Violations and Where to Find Them:
programming languages deal with these kinds of inputs. Not              A Longitudinal Analysis of Specification Violations in HTML,” in
only did we uncover functional deficiencies in each of their            Internet Measurement Conference, 2022.
[20] WHATWG, “HTML Standard: 13.4 Parsing HTML fragments,” https://               comment,” https://html.spec.whatwg.org/multipage/parsing.html#parse-
     html.spec.whatwg.org/multipage/parsing.html#fragment-case, accessed          error-incorrectly-closed-comment, accessed 8.12.2023.
     8.12.2023.                                                              [44] ——, “HTML Standard: 13.2.6.4.16 The ”in select” insertion
[21] T. C. Authors, “html document parser fastpath.cc,” https:                    mode,” https://html.spec.whatwg.org/multipage/parsing.html#parsing-
     //source.chromium.org/chromium/chromium/src/+/main:third party/              main-inselect, accessed 8.12.2023.
     blink/renderer/core/html/parser/html document parser fastpath.cc,       [45] T. Nidecki, “Mutation XSS in Google Search,” https://www.acunetix.
     accessed 8.12.2023.                                                          com/blog/web-security-zone/mutation-xss-in-google-search, 2019, ac-
[22] W3C, “Mathematical Markup Language (MathML) Version 3.0 2nd                  cessed: 8.12.2023.
     Edition,” https://www.w3.org/TR/MathML3, accessed 8.12.2023.            [46] W3C, “Document Structure – SVG 2,” https://svgwg.org/svg2-draft/
[23] ——, “Scalable Vector Graphics (SVG) 2,” https://svgwg.org/svg2-              struct.html#DescriptionDefinitions, accessed 8.12.2023.
     draft, accessed 8.12.2023.                                              [47] M. Heiderich, C. Späth, and J. Schwenk, “DOMPurify: Client-Side
[24] WHATWG, “HTML Standard: 13.2.6.5 the rules for parsing tokens                Protection against XSS and Markup Injection,” in ESORICS, 2017.
     in foreign content,” https://html.spec.whatwg.org/multipage/parsing.    [48] W. Kahn-Greene, “bleach is deprecated; statement on project going
     html#parsing-main-inforeign, accessed 8.12.2023.                             forward (2023-01-23),” https://github.com/mozilla/bleach/issues/698,
[25] M. Heiderich, J. Schwenk, T. Frosch, J. Magazinius, and E. Z.                2023, accessed 8.12.2023.
     Yang, “mXSS Attacks: Attacking well-secured Web-Applications            [49] N. Demir, T. Urban, K. Wittek, and N. Pohlmann, “Our (in)Secure
     by using innerHTML Mutations,” in Conference on Computer and                 Web: Understanding Update Behavior of Websites and Its Impact on
     Communications Security, 2013.                                               Security,” in Passive and Active Network Measurement Conference,
[26] D. Klein, “HTML Parsing Differentials,” https://github.com/ias-tubs/         2021.
     HTML parsing differentials, 2023, accessed: 8.12.2023.                  [50] web-platform-tests contributors, “The web-platform-tests project,”
[27] M. Bentkowski, “HTML sanitization bypass in Ruby Sanitize                    https://github.com/web-platform-tests/wpt, accessed 8.12.2023.
     <5.2.1,” https://research.securitum.com/html-sanitization-bypass-in-    [51] Y. Nadji, P. Saxena, and D. Song, “Document structure integrity:
     ruby-sanitize-5-2-1, 2020, accessed 8.12.2023.                               A robust basis for cross-site scripting defense.” in Network and
[28] ——, “Write-up of DOMPurify 2.0.0 bypass using mutation XSS,”                 Distributed System Security Symposium, 2009.
     https://research.securitum.com/dompurify-bypass-using-mxss, 2019,       [52] M. V. Gundy and H. Chen, “Noncespaces: Using randomization to
     accessed 8.12.2023.                                                          enforce information flow tracking and thwart cross-site scripting
[29] ——, “Mutation XSS via namespace confusion – DOM-                             attacks.” in Network and Distributed System Security Symposium,
     Purify <2.0.17 bypass,” https://research.securitum.com/mutation-             2009.
     xss-via-mathml-mutation-dompurify-2-0-17-bypass, 2019, accessed         [53] M. Steffens, M. Musch, M. Johns, and B. Stock, “Who’s Hosting the
     8.12.2023.                                                                   Block Party? Studying Third-Party Blockage of CSP and SRI,” in
[30] E. Yalon, “Mutation Cross-Site Scripting (mXSS) Vulnerabilities              Network and Distributed System Security Symposium, 2021.
     Discovered in Mozilla-Bleach,” https://securityboulevard.com/2020/      [54] M. Weissbacher, T. Lauinger, and W. K. Robertson, “Why Is CSP
     07/mutation-cross-site-scripting-mxss-vulnerabilities-discovered-in-         Failing? Trends and Challenges in CSP Adoption,” in Research in
     mozilla-bleach, 2020, accessed 8.12.2023.                                    Attacks, Intrusions and Defenses, 2014.
[31] WHATWG, “HTML Standard: 4 The elements of HTML,” https:                 [55] S. Calzavara, A. Rabitti, and M. Bugliesi, “Content security problems?:
     //html.spec.whatwg.org/multipage/semantics.html#semantics, accessed          Evaluating the effectiveness of content security policy in the wild,” in
     8.12.2023.                                                                   Conference on Computer and Communications Security, 2016.
[32] ——, “HTML Standard: 13.2 Parsing HTML documents,” https://html.         [56] L. Weichselbaum, M. Spagnuolo, S. Lekies, and A. Janc, “CSP is dead,
     spec.whatwg.org/multipage/parsing.html, accessed 8.12.2023.                  long live CSP! On the insecurity of whitelists and the future of content
[33] ——, “HTML Standard: 4.8.5 the iframe element,” https:                        security policy,” in Conference on Computer and Communications
     //html.spec.whatwg.org/multipage/iframe-embed-object.html#the-               Security, 2016.
     iframe-element, accessed 8.12.2023.                                     [57] S. Roth, T. Barron, S. Calzavara, N. Nikiforakis, and B. Stock,
[34] ——, “HTML Standard: 3.2.5.1 the ”nothing” content model,”                    “Complex Security Policy? A Longitudinal Analysis of Deployed
     https://html.spec.whatwg.org/multipage/dom.html#the-nothing-                 Content Security Policies,” in Network and Distributed Systems
     content-model, accessed 8.12.2023.                                           Security, 2020.
[35] ——, “HTML Standard: 13.2.2 Parse errors,” https://html.spec.whatwg.     [58] R. Grove, “Insufficient neutralization of ‘style‘ element content may
     org/multipage/parsing.html#parse-errors, accessed 8.12.2023.                 allow XSS in Sanitize,” https://github.com/rgrove/sanitize/security/
[36] D. Balzarotti, M. Cova, V. Felmetsger, N. Jovanovic, E. Kirda,               advisories/GHSA-f5ww-cq3m-q3g7, 2023, accessed 8.12.2023.
     C. Kruegel, and G. Vigna, “Saner: Composing Static and Dynamic          [59] L. Bernhard, T. Scharnowski, M. Schloegel, T. Blazytko, and T. Holz,
     Analysis to Validate Sanitization in Web Applications.” in IEEE              “JIT-Picking: Differential Fuzzing of JavaScript Engines,” in Confer-
     Symposium on Security and Privacy, 2008.                                     ence on Computer and Communications Security, 2022.
[37] M. Alkhalaf, T. Bultan, and J. L. Gallegos, “Verifying Client-Side      [60] H. Han, D. Oh, and S. K. Cha, “CodeAlchemist: Semantics-Aware
     Input Validation Functions using String Analysis,” in International          Code Generation to Find Vulnerabilities in JavaScript Engines,” in
     Conference on Software Engineering, 2012.                                    Network and Distributed System Security Symposium, 2019.
[38] M. Alkhalaf, A. Aydin, and T. Bultan, “Semantic Differential Repair     [61] S. Groß, S. Koch, L. Bernhard, T. Holtz, and M. Johns, “Fuzzilli:
     for Input Validation and Sanitization,” in International Symposium on        Fuzzing for JavaScript JIT Compiler Vulnerabilities,” in Network and
     Software Testing and Analysis, 2014.                                         Distributed Systems Security, 2023.
[39] S. Joshi, N. Agrawal, R. Krishnapuram, and S. Negi, “A Bag of Paths     [62] W. Xu, S. Park, and T. Kim, “FREEDOM: Engineering a State-of-the-
     Model for Measuring Structural Similarity in Web Documents,” in              Art DOM Fuzzer,” in Conference on Computer and Communications
     International Conference on Knowledge Discovery and Data Mining,             Security, 2020.
     2003.                                                                   [63] S. Kim, Y. M. Kim, J. Hur, S. Song, G. Lee, and B. Lee, “FuzzOrigin:
[40] WHATWG, “HTML Standard: 13.2.5.2 RCDATA state,” https://                     Detecting UXSS vulnerabilities in browsers through origin fuzzing,”
     html.spec.whatwg.org/multipage/parsing.html#rcdata-state, accessed           in USENIX Security Symposium, 2022.
     8.12.2023.                                                              [64] T. Petsios, A. Tang, S. J. Stolfo, A. D. Keromytis, and S. Jana,
[41] ——, “HTML Standard: 13.2.4.5 Parse state: Other parsing                      “NEZHA: Efficient Domain-Independent Differential Testing,” in IEEE
     state flags,” https://html.spec.whatwg.org/multipage/parsing.html#           Symposium on Security and Privacy, 2017.
     other-parsing-state-flags, accessed 8.12.2023.                          [65] J. Hur, S. Song, D. Kwon, E. Baek, J. Kim, and B. Lee, “DifuzzRTL:
[42] ——, “HTML Standard: 13.2.2 Parse errors: cdata-in-html-content,”             Differential Fuzz Testing to Find CPU Bugs,” in IEEE Symposium on
     https://html.spec.whatwg.org/#parse-error-cdata-in-html-content, ac-         Security and Privacy, 2021.
     cessed 8.12.2023.                                                       [66] B. Jabiyev, S. Sprecher, K. Onarlioglu, and E. Kirda, “T-Reqs: HTTP
[43] ——, “HTML Standard: 13.2.2 Parse errors: incorrectly-closed-                 Request Smuggling with Differential Fuzzing,” in Conference on
     Computer and Communications Security, 2021.                               encoding(): Returns an encoding function applicable to
[67] G. S. Reen and C. Rossow, “DPIFuzz: A Differential Fuzzing                another value. Possible values are {None, Xml} with
     Framework to Detect DPI Elusion Strategies for QUIC,” in Annual
     Computer Security Applications Conference, 2020.
                                                                               P(N one) = 0.4 and P(Xml) = 0.1.
[68] C. Brubaker, S. Jana, B. Ray, S. Khurshid, and V. Shmatikov,              quote(): This function returns an optionally encoded
     “Using Frankencerts for Automated Adversarial Testing of Certificate      quote character. Possible values are chosen from:
     Validation in SSL/TLS Implementations,” in IEEE Symposium on              {Backtick(e), Single(e), Double(e)} where e = encoding()
     Security and Privacy, 2014.
[69] S. Wi, T. T. Nguyen, J. Kim, B. Stock, and S. Son, “DiffCSP:
                                                                               with respective probabilities of P(Single) = 0.45,
     Finding Browser Bugs in Content Security Policy Enforcement through       P(Double) = 0.45 and P(Backtick) = 0.1.
     Differential Testing,” in Network and Distributed System Security             This function is used to determine how attributes are
     Symposium, 2023.                                                          quoted. Only single and double quotes are valid according
[70] B. Stock, S. Lekies, T. Mueller, P. Spiegel, and M. Johns, “Precise       to the specification, so they are generated more frequently.
     Client-side Protection against DOM-based Cross-Site Scripting,” in
     USENIX Security Symposium, 2014.                                          quoted(v): Determines how an attribute’s value (provided
[71] M. Steffens, C. Rossow, M. Johns, and B. Stock, “Don’t Trust the          as v ) is quoted. Possible values are chosen from the set:
     Locals: Investigating the Prevalence of Persistent Client-Side Cross-
     Site Scripting in the Wild.” in Network and Distributed System Security           {Unquoted, Enclosed(quote()),
     Symposium, 2019.
[72] M. T. Louw and V. N. Venkatakrishnan, “Blueprint: Robust preven-
                                                                                        Front(quote()), Back(quote()),
     tion of cross-site scripting attacks for existing browsers.” in IEEE               Mixed(quote(), quote())}
     Symposium on Security and Privacy, 2009.
[73] P. Hooimeijer, B. Livshits, D. Molnar, P. Saxena, and M. Veanes,          Unquoted results in an unquoted value and Mixed in a
     “Fast and Precise Sanitizer Analysis with BEK.” in USENIX Security        value with potentially mismatching quotes, depending on
     Symposium, 2011.
[74] G. Argyros, I. Stais, A. Kiayias, and A. D. Keromytis, “Back in Black:
                                                                               the return values of its parameters. Both Front and Back
     Towards Formal, Black Box Analysis of Sanitizers and Filters,” in         result in a quote on either side of the value, and Enclosed
     IEEE Symposium on Security and Privacy, 2016.                             properly quotes the value. Their respective probabilities
[75] J. Dahse and T. Holz, “Experience Report: An Empirical Study of           are P(U nquoted) = 0.5, P(M ixed) = 0.25, P(F ront) =
     PHP Security Mechanism Usage,” in International Symposium on
     Software Testing and Analysis, 2015.
                                                                               0.25, P(Back) = 0.25 and P(Enclosed) = 1.0.
                                                                               attr key():     Returns      a    string    from    the    set
                                                                               {id, name, title, foo, data-foo} with equal
Appendix A.                                                                    probability. We chose this selection to cover different
Implementation                                                                 attribute types that do not execute JavaScript on their own.
                                                                               We avoided generating event handlers that might directly
                                                                               cause JavaScript execution, as testing the completeness of
    The payload generation is based on randomly selecting
                                                                               block lists would offer no additional insight into the parsing
a sequence of transformations to consecutively build up the
                                                                               behavior.
final payload.
                                                                               attr form(): To represent invalid attribute values, we in-
    Whenever a transformation or one of its parameters is
                                                                               troduce the possibility of generating incorrectly format-
selected, each option is chosen with a relative probability
                                                                               ted attributes. This function returns values from the set
P. Take the div and br tags as an example, their relative
                                                                               {Regular, Space, Slash}, modeling such issues. Their
probabilities are: P(div) = 1.0 and P(br) = 0.5. This means
                                                                               probabilities are P(Regular) = 0.9, P(Space) = 0.05 and
MutaGen generates twice as many div tags as br tags.
                                                                               P(Slash) = 0.05.
                                                                               attr(v): Generates a potentially quoted HTML attribute with
A.1. Parameterized Transformations                                             the value v . Based on the return values of k = attr key(),
                                                                               f = attr f orm() and q = quoted() an attribute is se-
    Most of the transformations applied by MutaGen are                         rialized as follows: An attribute is serialized as follows
parameterized. We now give a short overview of the different                     k = quoted(v) if f = Regular. For f equals Space, a
parameter types, their respective values, and how likely they                  whitespace character precedes the value, and if f is Slash,
are applied.                                                                   the initial space is replaced with a slash character.
payload(): This function returns an initial payload. They are                  tag(): Selects one of the HTML, SVG, or MathML tags
chosen from the following set: {Img, Image, Script}                            listed in Table 7 with a sequence of attributes with static
with relative probability of P(Img) = 0.6, P(Image) = 0.2,                     values. The relative probabilities for each tag are provided
P(Script) = 0.2. Each payload is serialized as follows:                        in column P. These probabilities were assigned manually
   • Img: <img src=x onerror=f()>                                              to group similar elements such as mi, mo, mn, and ms to
   • Image: <image src=x onerror=f()>                                          uncover a wide breadth of different payloads.
   • Script: <script>f()</script>                                              bracket(): Returns either an opening or closing angle bracket
We decided to mainly generate XSS payloads based on img                        with equal possibility.
tags as it is the most universally applicable tag.                             bang(): Selects whether the generated XML comment should
place(): Returns whether the transformation should change                      be closed according to the HTML specification (i.e., -->)
the beginning or the end of P , returning either Prepend                       or with a bang comment (i.e., --!>). Values are chosen
or Append with equal probability.                                              from the set: {No_bang, Bang} with equal probability.
                     Table 6: Complete List of Transformations Applied to the Accumulated Payload P
Name                     P        Parameters       Effect                              Description
Payload                           pl = payload()   P = pl
                                                       (                               Select an initial Payload
                                  t = tag()               <t>P, if p = Prepend
Open tag                 1.0                       P=                                  Add opening tag t to P
                                  p = place()             P <t>, if p = Append
                                                       (
                                  t = tag(),              <t/>P, if p = Prepend
Self closing tag         1.0                       P=                                  Add self closing tag t to P
                                  p = place()             P <t/>, if p = Append
Enclose tag              1.0      t = tag()        P = <t>P </t>                       Enclose P in tag t
                                  t = tag(),
Enclose tag attr         0.75                      P = <t a(P) >                       Enclose P in attribute a of tag t
                                  a = attr()           (
                                  t = tag()              </t>P, if p = Prepend
Close tag                1.0                       P=                                  Add closing tag t to P
                                  p = place()            P </t>, if p = Append
                                                       (
                                                         <!- -P, if p = Prepend
Open XML Comment         0.125    p = place()      P=                                  Add opening XML comment to P
                                                         P <!- -, if p = Append
                                                       (
                                  p = place(),           - -b>P, if p = Prepend
Close XML Comment        0.125                     P=                                  Add closing XML comment to P
                                  b = bang()             P - -b>, if p = Append
Enclose XML Comment      0.125    b = bang()       P = <!- -P - -b>                    Enclose P with XML comment
Enclose JS Comment       0.01                      P=/ (*P */                          Enclose P in JavaScript comment
                                                         /*P, if p = Prepend
Open JS Comment          0.005    p = place()      P=                                  Add opening JavaScript comment to P
                                                         P /*, if p = Append
                                                       (
                                                           /P, if p = Prepend
Close JS Comment         0.005    p= place()       P= *                                Add closing JavaScript comment to P
                                                         P */, if p = Append
Enclose CDATA            0.05                      P = <!CDATA[
                                                       (            P ]]>              Enclose P in CDATA section.
                                                         <!CDATA[P, if p = Prepend
Begin CDATA              0.05     p = place()      P=                                  Add begin CDATA directive to P
                                                         P <!CDATA[, if p = Append
                                                       (
                                                         ]]>P, if p = Prepend
End CDATA                0.05     p = place()      P=                                  Add end CDATA directive to P
                                                         P ]]>, if p = Append
                                                       (
                                                         <!P, if p = Prepend
Parsing directive        0.05     p = place()      P=                                  Add incomplete parsing directive to P
                                                         P <!, if p = Append
                                                       (
                                  p = place(),           bP, if p = Prepend
Angle bracket            0.2                       P=                                  Add angle bracket b to P
                                  b = bracket()          P b, if p = Append
                                                       (
                                  q = quote(),           qP, if p = Prepend
Quote                    0.25                      P=                                  Add a quote to P
                                  p = place()            Pq, if p = Append
                                                       (
                                                           P, if p = Prepend
Space                    1.00     p = place()      P=                                  Add a space to P
                                                         P , if p = Append
XML Encode               0.025                     P = xml_encode(P)                   Perform XML encoding on P
EncodeURI                0.0005                    P = encodeURI(P)                    Perform URI encoding on P
EncodeURIComponent       0.0005                    P = encodeURIComponent(P)           Perform URI Component encoding on P
⊥                        0.05                      P                                   Terminate the generation run
                             Table 7: Tags Generated by MutaGen and their Selection Criteria
 Tag              P      NS (*)      Selection Criteria
 img
                         H           Typical XSS payloads
 script
 image                   H, S , M    In HTML treated as img, valid SVG or MathML element
 div            1.0
                                     Basic HTML elements, terminate foreign content
 span           1.0
 object         0.5                  Basic HTML element.
 form           1.0                  form elements can not be nested, enforced by parsing specification
 dfn            1.0
                                     Both can not be nested, not enforced by parsing specification
 header         1.0
 p              0.5                  Optional end tag, terminates foreign content
 br             0.5
                                     No end tag, no content allowed, terminate foreign content
 embed          0.5
 input          1.0                  No end tag, no content allowed
 a              1.0                  No interactive content allowed, e.g., iframe, not enforced by parsing specification
 noscript       1.0                  Parsed differently depending on scripting flag: either HTML or JavaScript content
 table          0.25                 Opens a table, parsing specification enforces no nesting, terminates foreign content
 td             0.25
 tr             0.25                 Restrictive content, together they make up a table
 colgroup       0.25     H
 select         1.0                  Only option, optgroup and script-supporting content allowed. Special parsing rules when inside table
 option         1.0                  Restrictions on where it can occur, depending on attribute values allowed content changes
 textarea       1.0                  Only text content
 keygen         1.0                  Not supported anymore, no content, no end tag.
 xmp            1.0                  No element specification anymore, still has parsing rules, used to render markup as text without executing it
 frameset       0.5                  No element specification anymore, still has parsing rules
 listing        1.0                  No element specification anymore, still has parsing rules, used to display code
 li             0.5
                                     Make up a list, allowed to contain script-supporting elements, terminate foreign content
 ul             0.5
 pre            1.0
                                     Only allowed to contain phrasing content, terminate foreign content
 var            1.0
 dl             0.5                  Restricted content model, terminates foreign content
 dt             0.5                  Shall only occur inside dl, terminates foreign content
 plaintext      1.0                  Deprecated. Renders everything below as plain text. Can not be closed
 noframes       1.0
                                     No element specification anymore, still have parsing rules. Contain raw text content
 noembed        1.0
 iframe         1.0                  iframe element specification says no content allowed, but parsing specification says raw text content
 svg            1.0                  Namespace transition from H to S
 foreignObject 1.0
                         S
 desc           1.0                  Allow to embed HTML segments inside a SVG
 path           1.0
 math           1.0                  Namespace transition from H to M
 mtext          0.5
 mglyph         0.5
 mi             0.25
                         M
 mo             0.25                 Allow to embed HTML segments inside MathML
 mn             0.25
 ms             0.25
 annotation-xml 1.0
 style          1.0                  Text content when in H, otherwise markup
                         H, S
 font           1.0                  Deprecated for both HTML and SVG
                         H           Text content, Singleton: not enforced by parsing specification
 title            1.0
                         S           Can contain markup
*: H: HTML namespace, S : SVG namespace, M: MathML namespace
Appendix B.
Meta-Review
    The following meta-review was prepared by the program
committee for the 2024 IEEE Symposium on Security and
Privacy (S&P) as part of the review process as detailed in
the call for papers.

B.1. Summary

    The paper conducts an analysis of server-side HTML
sanitization and parsing libraries and their vulnerabilities.
They evaluated 11 such libraries using their HTML fragment
generator MutaGen and uncovered security issues in nine
of them. The authors then categorize the root causes of
these vulnerabilities into five main parsing issues and two
serialization problems.

B.2. Scientific Contributions

  •   Identifies an Impactful Vulnerability
  •   Creates a New Tool to Enable Future Science

B.3. Reasons for Acceptance

 1) Identifies an Impactful Vulnerability: This study offers
    an examination of issues arising in sanitization libraries
    as a result of incorrect parsing of HTML snippets.
    Their findings show the existence of HTML parsing and
    sanitization flaws that can lead to significant security
    vulnerabilities, as evidenced by the presence of CVEs.
 2) Creates a New Tool to Enable Future Science: MutaGen
    or the design idea behind the tool might be interesting
    for future research, e.g. altering the tool to focus on
    stylesheet injections instead of XSS.

B.4. Noteworthy Concerns

 1) The paper does not adequately explain the criteria for
    selecting the analyzed sanitizers. The current selection
    could be biased, and the results may not represent server-
    side sanitizers that are actually used in the wild.
 2) Some reviewers raised concerns that the approach does
    not consider CSS injections.
