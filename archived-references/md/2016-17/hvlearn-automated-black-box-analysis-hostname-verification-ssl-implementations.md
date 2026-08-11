---
type: Whitepaper
title: "HVLearn: Automated Black-box Analysis of Hostname Verification in SSL/TLS Implementations"
resource: "http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:34:23+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf"
    title: "HVLearn: Automated Black-box Analysis of Hostname Verification in SSL/TLS Implementations"
    author: Suphannee Sivakorn, George Argyros, Kexin Pei, Angelos D. Keromytis, Suman Jana
also_at: []
authors:
  - Suphannee Sivakorn
  - George Argyros
  - Kexin Pei
  - Angelos D. Keromytis
  - Suman Jana
canonical_url: ""
cited_by:
  - "2016-17.md:97"
commit: ""
content_sha256: 8e327e02a89c62ea9353b3ed2dc420f42cf768a286f182e333b6815024b2236e
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: ad81042304892fe70dccf189ca8c13c14d68054fe1e2effbe0fb6f65cfc575ce
retrieved_from: "http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:34:23+00:00"
slug: hvlearn-automated-black-box-analysis-hostname-verification-ssl-implementations
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# HVLearn: Automated Black-box Analysis of Hostname Verification in SSL/TLS Implementations

**HVLearn: Automated Black-box Analysis of Hostname Verification in SSL/TLS Implementations** - Suphannee Sivakorn, George Argyros, Kexin Pei, Angelos D. Keromytis, Suman Jana, Publisher not stated.

- Published: date not stated
- Original: <http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf>
- Preserved from: http://www.cs.columbia.edu/~suman/docs/hvlearn.pdf (stored) on 2026-08-11
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# HVLearn: Automated Black-box Analysis of Hostname Verification in SSL/TLS Implementations

--- page 1 ---

HVLearn: Automated Black-box Analysis of
Hostname Verication in SSL/TLS Implementations
Suphannee Sivakorn, George Argyros, Kexin Pei, Angelos D. Keromytis, and Suman Jana
Department of Computer Science
Columbia University, New York, USA
f
suphannee, argyros, kpei, angelos, suman
g
@cs.columbia.edu
Abstract
—SSL/TLS is the most commonly deployed family of
protocols for securing network communications. The security
guarantees of SSL/TLS are critically dependent on the correct
validation of the X.509 server certicates presented during the
handshake stage of the SSL/TLS protocol. Hostname verication
is a critical component of the certicate validation process that
veries the remote server's identity by checking if the hostname
of the server matches any of the names present in the X.509
certicate. Hostname verication is a highly complex process
due to the presence of numerous features and corner cases such
as wildcards, IP addresses, international domain names, and so
forth. Therefore, testing hostname verication implementations
present a challenging task.
In this paper, we present HVLearn, a novel black-box testing
framework for analyzing SSL/TLS hostname verication imple-
mentations, which is based on automata learning algorithms.
HVLearn utilizes a number of certicate templates, i.e., certi-
cates with a common name (CN) set to a specic pattern, in
order to test different rules from the corresponding specication.
For each certicate template, HVLearn uses automata learning
algorithms to infer a Deterministic Finite Automaton (DFA) that
describes the set of all hostnames that match the CN of a given
certicate. Once a model is inferred for a certicate template,
HVLearn checks the model for bugs by nding discrepancies
with the inferred models from other implementations or by
checking against regular-expression-based rules derived from the
specication. The key insight behind our approach is that the
acceptable hostnames for a given certicate template form a
regular language. Therefore, we can leverage automata learning
techniques to efciently infer DFA models that accept the
corresponding regular language.
We use HVLearn to analyze the hostname verication im-
plementations in a number of popular SSL/TLS libraries and
applications written in a diverse set of languages like C, Python,
and Java. We demonstrate that HVLearn can achieve on aver-
age
11
:
21%
higher code coverage than existing black/gray-box
fuzzing techniques. By comparing the DFA models inferred by
HVLearn, we found
8
unique violations of the RFC specications
in the tested hostname verication implementations. Several
of these violations are critical and can render the affected
implementations vulnerable to active man-in-the-middle attacks.
I. I
NTRODUCTION
The SSL/TLS family of protocols are the most commonly
used mechanisms for protecting the security and privacy
of network communications from man-in-the-middle attacks.
The security guarantees of SSL/TLS protocols are critically
dependent on correct validation of X.509 digital certicates
presented by the servers during the SSL/TLS handshake phase.
The certicate validation, in turn, depends on hostname ver-
ication for verifying that the hostname (i.e., fully qualied
domain name, IP address, and so forth) of the server matches
one of the identiers in the “SubjectAltName” extension or
the “Common Name” (CN) attribute of the presented leaf
certicate. Therefore, any mistake in the implementation of
hostname verication could completely undermine the security
and privacy guarantees of SSL/TLS.
Hostname verication is a complex process due to the pres-
ence of numerous special cases (e.g., wildcards, IP addresses,
international domain names, etc.). For example, a wildcard
character (`*') is only allowed in the left-most part (separated
by `.') of a hostname. To get a sense of the complexities
involved in the hostname verication process, consider the
fact that different parts of its specications are described
in ve different RFCs [18], [20], [21], [24], [25]. Given
the complexity and security-critical nature of the hostname
verication process, it is crucial to perform automated analysis
of the implementations for nding any deviation from the
specication.
However, despite the critical nature of the hostname ver-
ication process, none of the prior research projects dealing
with adversarial testing of SSL/TLS certicate validation [36],
[38], [45], [50], support detailed automated testing of host-
name verication implementations. The prior projects either
completely ignore testing of the hostname verication process
or simply check whether the hostname verication process
is enabled or not. Therefore, they cannot detect any subtle
bugs where the hostname verication implementations are
enabled but deviate subtly from the specications. The key
problem behind automated adversarial testing of hostname
verication implementations is that the inputs (i.e., hostnames
and certicate identiers like common names) are highly
structured, sparse strings and therefore makes it very hard
for existing black/gray-box fuzz testing techniques to achieve
high test coverage or generate inputs triggering the corner
cases. Heavily language/platform-dependent white-box testing
techniques are also hard to apply for testing hostname veri-
cation implementations due to the language/platform diversity
of SSL/TLS implementations.
In this paper, we design, implement, and evaluate HVLearn,
a black-box differential testing framework based on automata
learning, which can automatically infer Deterministic Finite
Automata (DFA) models of the hostname verication imple-
mentations. The key insight behind HVLearn is that hostname
verication, even though very complex, conceptually closely

--- page 2 ---

resemble the regular expression matching process in many
ways (e.g., wildcards). This insight on the structure of the
certicate identier format suggests that the acceptable host-
names for a given certicate identier, as suggested by the
specications, form a regular language. Therefore, we can
use black-box automata learning techniques to efciently infer
Deterministic Finite Automata (DFA) models that accept the
regular language corresponding to a given hostname verica-
tion implementation. Prior results by Angluin et al. have shown
that DFAs can be learned efciently through black-box queries
in polynomial time over the number of states [31]. The DFA
models inferred by HVLearn can be used to efciently perform
two main tasks that existing testing techniques cannot do well:
(i) nding and enumerating unique differences between mul-
tiple different implementations; and (ii) extracting a formal,
backward-compatible reference specication for the hostname
verication process by computing the intersection DFA of the
inferred DFA models from different implementations.
We apply HVLearn to analyze a number of popular
SSL/TLS libraries such as OpenSSL, GnuTLS, MbedTLS,
MatrixSSL, CPython SSL and applications such as Java
HttpClient and cURL written in diverse languages like C,
Python, and Java. We found
8
distinct specication violations
like the incorrect handling of wildcards in internationalized
domain names, confusing domain names with IP addresses,
incorrect handling of NULL characters, and so forth. Several
of these violations allow network attackers to completely break
the security guarantees of SSL/TLS protocol by allowing
the attackers to read/modify any data transmitted over the
SSL/TLS connections set up using the affected implementa-
tions. HVLearn also found
121
unique differences, on average,
between any two pairs of tested application/library.
The major contributions of this paper are as follows.

To the best of our knowledge, HVLearn is the rst testing
tool that can learn DFA models for implementations
of hostname verication, a critical part of SSL/TLS
implementations. The inferred DFA models can be used
for efcient differential testing or extracting a formal
reference specication compatible with multiple existing
implementations.

We design and implement several domain-specic opti-
mizations like equivalence query design, alphabet selec-
tion, etc. in HVLearn for efciently learning DFA models
from hostname verication implementations.

We evaluate HVLearn on 6 popular libraries and 2 appli-
cations. HVLearn achieved signicantly higher (
11
:
21%
more on average) code coverage than existing black/gray-
box fuzzing techniques and found
8
unique previously
unknown RFC violations as shown in Table II, several
of which render the affected SSL/TLS implementations
completely insecure to man-in-the-middle attacks.
The remainder of this paper is organized as follows: Sec-
tion II presents the descriptions of the SSL/TLS hostname
verication process. We discuss the challenges in testing host-
name verication and our testing methodology in Section III.
Section IV describes the design and implementation details
of HVLearn. We present the evaluation results for using
HVLearn to test SSL/TLS implementations in Section V.
Section VI presents a detailed case study of several security-
critical bugs that HVLearn found. Section VII discusses the
related work and Section VIII concludes the paper. For the
detailed developer responses on the bugs found by HVLearn,
we refer interested readers to Appendix X-B.
II. O
VERVIEW OF HOSTNAME VERIFICATION
As part of the hostname verication process, the SSL/TLS
client must check that the host name of the server matches
either the “common name” attribute in the certicate or one
of the names in the “subjectAltName” extension in the certi-
cate [21]. Note that even though the process is called hostname
verication, it also supports verication of IP addresses or
email addresses.
In this section, we rst provide a brief summary of the
hostname format and specications that describe the format
of the common name attribute and subjectAltName extension
formats in X.509 certicate. Figure 1 provides a high-level
summary of the relevant parts of an X.509 certicate. Next,
we describe different parts of the hostname verication process
(e.g., domain name restrictions, wildcard characters, and so
forth) in detail.
Fig. 1. Fields in an X.509 certicate that are used for hostname verication.
A. Hostname verication inputs
Hostname format.
Hostnames are usually either a fully
qualied domain name or a single string without any `.'
characters. Several SSL/TLS implementations (i.e., OpenSSL)
also support IP addresses and email addresses to be passed
as the hostname to the corresponding hostname verication
implementation.
A domain name consists of multiple “labels”, each separated
by a `.' character. The domain name labels can only contain
letters a-z or A-Z (in a case-insensitive manner), digits 0-9
and the hyphen character `-' [16]. Each label can be up to
63 characters long. The total length of a domain name can
be up to 255 characters. Earlier specications required that
the labels must begin with letters [21]. However, subsequent
revisions have allowed labels that begin with digits [17].
Common names in X.509 certicates.
The Common Name
(CN) is an attribute of the “subject distinguished name”

--- page 3 ---

X.509 CertiÞcateSubject:X509v3 extensionsX509v3 Subject Alternative Name:CN= X520CommonNamearbitrarytypeformatDNS:IP Address:email:IA5StringIA5StringIA5StringtypeformatdNSNameiPAddressrfc822Name

--- page 4 ---

eld in an X.509 certicate. The common name in a server
certicate is used for validating the hostname of the server as
part of the certicate verication process. A common name
usually contains a fully qualied domain name, but it can also
contain a string with arbitrary ASCII and UTF-8 characters
describing a service (e.g., CN=`Sample Service'). The only
restriction on the common name string is that it should follow
the X520CommonName standard (e.g., should not repeat the
substring `CN=') [21]. Note that this is different from the
hostname specications that are very strictly dened and only
allow certain characters and digits as described above.
SubjectAltName in X.509 certicates.
Subject alternative
name (subjectAltName) is an X.509 extension that can be
used to store different types of identity information like fully
qualied domain names, IP addresses, URI strings, email
addresses, and so forth. Each of these types has different
restrictions on allowed formats. For example, dNSName(DNS)
and uniformResourceIdentier(URI) must be valid IA5String
strings, a subset of ASCII strings [21]. We refer interested
readers to Section 4.1.2.6 of RFC 5280 for further reading.
B. Hostname verication rules
Matching order.
RFC 6125 recommends SSL/TLS imple-
mentations to use subjectAltName extensions, if present in
a certicate, over common names as the common name is
not strongly tied to an identity and can be an arbitrary string
as mentioned earlier [24]. If multiple identiers are present
in a subjectAltName, the SSL/TLS implementations should
try to match DNS, SRV, URI, or any other identier type
supported by the implementation and must not match the
hostname against the common name of the certicate [24].
The Certicate Authorities (CAs) are also supposed to use the
dNSName instead of common name for storing the identity
information while issuing certicates [18].
Wildcard in common name/subjectAltName.
if a server
certicate contains a wildcard character `*', an SSL/TLS
implementation should match hostname against them using
the rules described in RFC 6125 [24]. We provide a summary
of the rules below.
A wildcard character is only allowed in the left-most label.
If the presented identier contains a wildcard character in any
label other then the left-most label (e.g., www.*.example.com
and www.foo*.example.com), the SSL/TLS implementations
should reject the certicate. A wildcard character is allowed to
be present anywhere in the left-most label, i.e., a wildcard does
not have to be the only character in the left-most label. For ex-
ample, identiers like bar*.example.com, *bar.example.com,
or f*bar.example.com valid.
While matching hostnames against the identiers present
in a certicate, a wildcard character in an identier should
only apply to one sub-domain and an SSL/TLS implemen-
tation should not compare against anything but the left-
most label of the hostname (e.g., *.example.com should
match foo.example.com but not bar.foo.example.com or ex-
ample.com).
Several special cases involving the wildcards are allowed in
the RFC 6125 only for backward compatibility of existing
SSL/TLS implementations as they tend to differ from the
specications in these cases. RFC 6125 clearly notes that
these cases often lead to overly complex hostname verication
code and might lead to potentially exploitable vulnerabilities.
Therefore, new SSL/TLS implementations are discouraged
from supporting such cases. We summarize some of them:
(i) a wildcard is all or part of a label that identies a
public sufx (e.g., *.com and *.info), (ii) multiple wildcards
are present in a label (e.g., f*b*r.example.com), and (iii)
wildcards are included as all or part of multiple labels (e.g.,
*.*.example.com).
International domain name (IDN).
IDNs can contain charac-
ters from a language-specic alphabet like Arabic or Chinese.
An IDN is encoded as a string of unicode characters. A domain
name label is categorized as a U-label if it contains at least one
non-ASCII character (e.g., UTF-8). RFC 6125 species that
any U-labels in IDNs must be converted to A-labels domain
before performing hostname verication [24]. U-label strings
are converted to A-labels, an ASCII-compatible encoding,
by adding the prex `xn
--
' and appending the output of
a Punycode transformation applied to the corresponding U-
label string as described in RFC 3492 [19]. Both U-labels and
A-labels still must satisfy the standard length bound on the
domain names (i.e. up to 255 bytes).
IDN in subjectAltName.
As indicated in RFC 5280, any
IDN in X.509 subjectAltName extension must be dened as
type IA5String which is limited only to a subset of ASCII
characters [21]. Any U-label in an IDN must be converted
to A-label before adding it to the subjectAltName. Email
addresses involving IDNs must also be converted to A-labels
before.
IDNs in common name.
Unlike IDNs in subjectAltName,
IDNs in common names are allowed to contain a Printa-
bleString (A-Z, a-z, 0-9, special characters
' = ( ) + ,
- . / : ?
, and space) as well as UTF-8 characters [21].
Wildcard and IDN.
There is no specication dening how
a wildcard character may be embedded within A-labels or
U-labels of an IDN [23]. As a result RFC 6125 [24] rec-
ommends that SSL/TLS implementations should not match
a presented identier in a certicate where the wildcard
is embedded within an A-label or U-label of an IDN
(e.g., xn
--
kcry6tjko*.example.com). However, SSL/TLS im-
plementations should match a wildcard character in an IDN
as long as the wildcard character occupies the entire left-most
label of the IDN (e.g. *.xn
--
kcry6tjko.example.com).
IP address.
IP addresses can be part of either the common
name attribute or the subjectAltName extension (with an `IP:'
prex) in a certicate. Section 3.1.3.2 of RFC 6125 species
that an IP address must be converted to network byte order
octet string before performing certicate verication [24].
SSL/TLS implementations should compare this octet string
with the common name or subjectAltName identiers. The
length of the octet string must be 4 bytes and 18 bytes for
IPv4 and IPv6 respectively. The hostname verication should

--- page 5 ---

succeed only if both octet strings are identical. Therefore,
wildcard characters are not allowed in IP address identiers,
and the SSL/TLS implementations should not attempt to match
wildcards.
Email.
Email can be embedded in common name as the
emailAddress attribute in legacy SSL/TLS implementations.
The attribute is not case sensitive. However, new implemen-
tations must add email addresses in rfc822Name format to
subject alternative name extension instead of the common
name attribute [21].
Internationalized email.
As similar to IDNs in subjec-
tAltName extensions, an internationalized email must be
converted into the ASCII representation before verica-
tion. RFC 5321 also species that network administrators
must not dene mailboxes (local-part@domain/address-literal)
with non-ASCII characters and ASCII control characters.
Email addresses are considered to match if the local-part
and host-part are exact matches using a case-sensitive and
case-insensitive ASCII comparison respectively (e.g., MYE-
MAIL@example.com does not match myemail@example.com
but matches MYEMAIL@EXAMPLE.COM) [21]. Note that
this specication contradicts that of the email addresses em-
bedded in the common name that is supposed to be completely
case-insensitive.
Email with IP address in the host part.
RFCs 5280 and 6125
do not specify any special treatment for IP address in the host
part of email and only allow email in rfc822Name format. The
rfc822Name format supports both IPv4 and IPv6 addresses in
the host part. Therefore, an email with an IP address in the
host part is allowed to be present in a certicate [22].
Wildcard in email.
There is no specication that wildcard
should be interpreted and attempted to match when they are
part of an email address in a certicate.
Other identiers in subjectAltName.
There are other iden-
tiers that can be used to perform identity checks e.g.,
UniformResourceIdentier(URI), SRVName, and otherName.
However, most popular SSL/TLS libraries do not support
checking these identiers and leave it up to the applications.
III. M
ETHODOLOGY
In this section, we describe the challenges behind automated
testing of hostname verication implementations. Albeit small
in size, the diversity of these implementations and the sub-
tleties in the hostname verication process make these im-
plementations difcult to test. We then proceed to describe an
overview of our methodology for testing hostname verication
implementations using automata learning algorithms. We also
provide a brief summary of the basic setting under which
automata learning algorithms operate.
A. Challenges in hostname verication analysis
We believe that any methodology for automatically ana-
lyzing hostname verication functionality should address the
following challenges:
1. Ill-dened informal specications.
As discussed in Sec-
tion II, although the relevant RFCs provide some exam-
ples/rules dening the hostname verication process, many
corner cases are left unspecied. Therefore, it is necessary
for any hostname verication implementation analysis to take
into account the behaviors of other popular implementations to
discover discrepancies that could lead to security/compatibility
aws.
2. Complexity of name checking functionality.
Hostname
verication is signicantly more complex than a simple string
comparison due to the presence of numerous corner cases and
special characters. Therefore, any automated analysis must
be able to explore these corner cases. We observe that the
format of the certicate identier as well as the matching
rules closely resemble a regular expression matching problem.
In fact, we nd that the set of accepted hostnames for each
given certicate identier form a regular language.
3. Diversity of implementations.
The importance and pop-
ularity of the SSL/TLS protocol resulted in a large number
of different SSL/TLS implementations. Therefore, hostname
verication logic is often implemented in a number of different
programming languages such as C/C++, Java, Python, and so
forth. Furthermore, some of these implementations might be
only accessible remotely without any access to their source
code. Therefore, we argue that a black-box analysis algorithm
is the most suitable technique for testing a large variety of
different hostname verication implementations.
B. HVLearn's approach to hostname verication analysis
Motivated by the challenges described above, we now
present our methodology for analyzing hostname verication
routines in SSL/TLS libraries and applications.
The main idea behind our HVLearn system is the following:
For different rules in the RFCs as well as for ambiguous rules
which are not well dened in the RFC, we generate “template
certicates” with common names which are specically de-
signed in order to check a specic rule. Afterward, we use
automata learning algorithms in order to extract a DFA which
describes the set of all hostname strings which are matching
the common name in our template certicate. For example,
the inferred DFA from an implementation for the identier
template “aaa.*.aaa.com” can be used to test conformance with
the rule in RFC 6125 prohibiting wildcard characters from
appearing in any other label than the leftmost label of the
common name.
Once a DFA model is generated by the learning algorithm,
we check the model for violations of any RFC rules or for
other suspicious behavior. HVLearn offers two methods to
check an inferred DFA model:
Regular-expression-based rules.
The rst option allows
the user to provide a regular expression that species a set of
invalid strings. HVLearn can ensure that the inferred DFAs do
not accept any of those strings. For example, RFC 1035 states
that only characters in the set [A-Za-z0-9] and the characters `-
' and `.' should be used in hostname identiers. Users therefore
can construct a simple regular expression that can be used by
HVLearn to check whether any of the tested implementations
accept a hostname with a character outside the given set.

--- page 6 ---

Fig. 2.
Exact learning from queries:
the active learning model under which
our automata learning algorithms operate.
Differential testing.
The second option offered by HVLearn
is to perform a differential testing between the inferred model
and models inferred from other implementations for the same
certicate template. Given two inferred DFA models, HVLearn
generates a set of
unique differences
between the two models
using an algorithm which we discuss in Section IV-E. This
option is especially useful for nding bugs in corner cases
which are not well dened in the RFCs.
We summarize the advantages of our approach below:

Adopting a black-box learning approach ensures that
our analysis method is language independent and we
can easily test a variety of different implementations.
Our only requirement is the ability to query the target
library/application with a certicate and a hostname of
our choice and nd whether the hostname is matching
the given identier in the certicate.

As pointed out in the previous section, hostname verica-
tion is similar to regular expression matching. Given that
regular expressions can be represented as DFAs, adopting
an automata-based learning algorithm for representing the
inferred models for each certicate template is a natural
and effective choice.

Finally, an additional advantage of having DFA models is
that we can efciently compare two inferred models and
enumerate all differences between them. This property is
very important for differential testing as it helps us in
analyzing the ambiguous rules in the specications.
Limitations.
A natural trade-off of choosing to implement
our system as a black-box analysis method is that we cannot
guarantee completeness or soundness of our models. However,
each difference inferred by HVLearn can be easily veried by
querying the corresponding implementations. Moreover, since
our system will nd all differences among implementations,
it will not report a bug that is common among all implemen-
tations unless a rule is explicitly specied for it, as described
above. Finally, we point out that not all discrepancies among
systems are necessarily security vulnerabilities; they may
represent equally acceptable design choices for ambiguous
parts of the RFCs.
C. Automata Learning Algorithms
We will now describe the automata learning algorithms that
allow us to realize our automata-based analysis framework.
Learning model.
We utilize learning algorithms that work in
an active learning model which is called
exact learning from
queries
. Traditional supervised learning algorithms, such as
those used to train deep neural networks, work on a given set
of labeled examples. In contrast, active learning algorithms in
our model work by adaptively selecting inputs that they use
to query a target system and obtain the correct label.
Figure 2 presents an overview of our learning model. A
learning algorithm attempts to learn a model of a target
system by querying the target system with inputs of its choice.
Eventually, by querying the target system multiple times, the
learning algorithm infers a model of the target system. This
model is then checked for correctness through an
equivalence
oracle
, an oracle that checks whether the inferred model
correctly summarizes the behavior of the target system. If the
model is correct, i.e., it agrees with the target system on all
inputs, then the learning algorithm will output the generated
model and terminate. On the other hand, if the model is in-
correct, the equivalence oracle will produce a
counterexample
,
i.e., an input under which the target system and the model
produce different outputs. The learning algorithm then uses
the counterexample to rene the inferred model. This process
iterates until the learning algorithm produces a correct model.
To summarize, a learning algorithm in the exact learning
model is able to interact with the target system using two
types of queries:

Membership queries:
The input to this type of query is a
string
s
and the output is
Accept
or
Reject
depending
on whether the string
s
is accepted by the target system
or not.

Equivalence queries:
The input to an equivalence query
is a model
M
and the output of the query is either
True
,
if the model
M
is equivalent to the target system on all
inputs, or a counterexample input under which the model
and target system produce different outputs.
Automata learning in practice.
The rst algorithm for
inferring DFA models in the exact learning from queries
model was developed by Angluin [31] and was followed by a
large number of optimizations and variations in the following
years. In our system, we use the Kearns-Vazirani (KV) algo-
rithm [54]. The KV algorithm utilizes a data structure called
the discrimination tree and it is in practice more efcient in
terms of the amount of queries it requires to infer a DFA
model.
The most signicant challenge that one should address in
order to use the KV algorithm and other automata learning
algorithms in practice, is how to implement an efcient and ac-
curate equivalence oracle in order to simulate the equivalence
queries performed by the learning algorithm. Since we only
have black-box access to the target system, any method for
implementing equivalence queries is necessarily incomplete.
In HVLearn, we use the Wp-method [49], for implementing
equivalence queries. The Wp-method checks the equivalence
between an inferred DFA and a target system using only
black-box queries to the target system. Essentially, the Wp-
method approximates an equivalence oracle by using multiple

--- page 7 ---

Learning AlgorithmModel MEquivalence OracleTarget SystemMembership queryIs model M correct? Yes/No with counter-exampleLearning Model

--- page 8 ---

Fig. 3. Overview of learning a hostname verication implementation using
HVLearn.
membership queries. The algorithm is given as input the DFA
to be checked and an upper bound on the number of states in
the target system when modeled as a DFA, a parameter which
we call
depth
. Then, the algorithm creates a set of test inputs
S
, which are then submitted to the target system. If the target
system agrees with the DFA model on all inputs in the test set
S
, then the DFA and the target system are proved equivalent
under the assumption that the upper bound on the number of
states of the target system is correct.
In theory, one can set the depth parameter of the Wp-method
to a very large value in order to design an equivalence oracle
which is, in practice, complete. However, the size of the set
of test inputs produced by the Wp-method is on the order of
O
(
n
2
j

j
m

n
+1
)
where

is the input alphabet for the DFA,
m
is the upper bound on the number of states of the target system
and
n
is the number of states in the input DFA. Therefore,
using the Wp-method with a large depth (i.e., upper bound on
the number of states of the target system) is impractical. Note
that, the bound on the number of test inputs produced by the
Wp-method is not a worst case bound; on the contrary, the
number of test inputs produced is usually of that order.
Consequently, it is essential for the efciency of our system
to maintain a small alphabet for our DFAs and also set a small
upper bound (depth) on the number of states of the target
system while using the Wp-method. We address both of these
issues in the next section.
IV. A
RCHITECTURE OF
HVL
EARN
In this section, we describe the design and implementation
of our system, HVLearn, based on automata learning tech-
niques. Specically, we describe the technical challenges that
arise when we attempt to use automata learning algorithms in
practice. We also summarize the optimizations that HVLearn
implements to address these challenges and efciently learn
DFA models of hostname verication implementations.
A. System overview
Figure 3 presents an overview of how HVLearn is used to
analyze the hostname verication functionality of an SSL/TLS
library. To use HVLearn, the user provides HVLearn access to
the hostname verication function that takes an X.509 certi-
cate and a hostname as input and returns
accept/reject
depending on whether the provided hostname is matching the
identier in the certicate. We describe how we implement
this interface in Section IV-C. Our system includes a number
of certicate templates, which are certicates designed to test
the SSL/TLS implementation on a number of different rules as
described in Section IV-B. For each such template, HVLearn
will learn a DFA model describing the set of hostnames
accepted by a given implementation for the given certicate
template. To produce a DFA model, HVLearn utilizes the
LearnLib [59] library which contains implementations of both
the KV algorithm and the Wp-method. To avoid setting the
maximum depth of the Wp-method to impractically high
values, we optimize the equivalence oracle as described in
Section IV-D.
Once a model is generated, our system proceeds to analyze
the model as described in Section IV-E. The results of our
analysis, both the inferred models and the differences between
models are then saved for reuse. Optionally, HVLearn can also
utilize the inferred models for a certicate template to extract a
formal specication for the corresponding certicate template
as described in Section V-F.
B. Generating certicate templates
To cover all different rules and ambiguous practices in
hostname verication, we created a set of 23 certicates with
different identier templates, where each certicate is designed
to test a specic rule from the specication. These certicates
are selected to cover all the rules we described in Section II.
For example, a certicate with common name “xn
--
a*.aaa”
will test if the implementation allows wildcards as part of an
A-label in an IDN, something which is explicitly forbidden by
RFC 6125. Our template certicates are self-signed X.509 v3
certicates generated using the GnuTLS library. We choose
to use GnuTLS for certicate generation because it allows
identiers with embedded NULL characters in both subject
common name and SAN. The template identier to be tested
is placed in either Subject CN and/or SAN (as dNSName,
iPAddress, or email).
C. Performing membership queries
In order to utilize the learning algorithms in LearnLib
(including the Wp-method), we implement a
membership
query
function that performs all queries to the target system.
This function accepts input as a string and returns a binary
value. In our system, we use the hostname verication function
from the target SSL/TLS implementation. We note here that,
since LearnLib is written in Java while many of our tested
SSL/TLS implementations are written in C/C++/Python, we
utilized the Java Native Interface (JNI) [10] to efciently
perform membership queries to the target in such cases.
D. Automata learning parameters and optimizations
In this section, we describe the architectural decisions and
optimizations that we implemented to efciently scale the KV

--- page 9 ---

Optimized Wp-MethodLearnLibKV algorithmcertiÞcate templatesHVLearnoutput Þnal model for test certiÞcate templateDFA modelequivalence querycounter- examplehostname (membership queries)Wp-methodÕs test hostnamesaccept/rejectmatch (hostname, test cert)?SSL/TLS hostname veriÞcation implementationtest certiÞcate template

--- page 10 ---

algorithm for testing complex real-world SSL/TLS hostname
verication implementations.
Alphabet size.
The rst important decision we have to make
to utilize the KV algorithm is to select an alphabet that will
be used by the algorithm. The alphabet refers to the set of
symbols that the learning algorithm will test.
A straightforward approach is to use a very general set
of characters such as the set of ASCII characters. However,
this will impose an unnecessary overhead in our system's
performance since the performance of both the KV algorithm
and the Wp-method rely heavily on the underlying alphabet
size. Our main insight is that we can reduce the alphabet to
a small set of representative characters that will thoroughly
test all different aspects of hostname verication. In particular
we select the set
 =
f
a, 1, dot,
n
s, @, A, =, *, x, n, -
,
n
u4F60, NULL
g
as an input alphabet in our experiments.
In the presented alphabet, `dot' denotes the `.' character,
n
s
denotes the space character (ASCII value 32), NULL denotes
the zero byte character, and
n
u4F60 denotes the unicode
character with hexadecimal value 4F60.
Note that this set of symbols is adequate for analyz-
ing hostname verication implementations since it includes
characters from all different categories such as lowercase,
uppercase, digits, unicode, etc., as well as special characters
like the NULL character. The lowercase characters `x', `n' in
conjunction with the `-' character are necessary in order to
encode IDN hostnames. Finally, the inclusion of some non-
alphanumeric characters such as the `=' character allows us
to detect violations where an implementation accepts invalid
hostnames.
Note that, even though the hostnames generated using this
alphabet set will often not resolve to a real IP address when
processed as DNS names, it does not affect the accuracy
of our analysis in any way. This is a side-effect the fact
that the hostname verication routines are not responsible for
resolving the provided DNS name to an IP address. It simply
checks whether the given hostname matches the identier in
the provided certicate.
Caching membership queries.
To avoid the communi-
cation cost of repeated querying of the SSL/TLS im-
plementations with same inputs, we utilize LearnLib's
DFALearningCache
class to cache the results of the mem-
bership queries. The cache is checked on each new query, and
a cached result is used whenever found. This optimization
is particularly useful for cutting down the overhead of the
repeated queries generated by the Wp-method across multiple
equivalence queries.
Optimizing equivalence queries.
In practice, the rst model
generated by the learning algorithm is usually just single
state DFA which rejects all hostnames. The reason is that
the learning algorithm is not able to generate any accepting
hostname and thus cannot distinguish between the initial state
and any other state in the target system. Sometimes, to force
the KV algorithm to produce an accepting hostname using the
Wp-method, a very large depth is required. This may cause
efciency issues in the system. However, if we supply the
model with an accepting hostname, then trivial models will
be improved quickly without having to utilize excessive depth
parameters in the Wp-method.
Recall here that the exponential term in the Wp-method is
dependent on the difference between the number of states in
the model and the provided depth. Therefore, once we discover
an accepting state in the target system, the Wp-method with a
much smaller depth will still be able to explore many different
aspects of the hostname verication implementation.
In order to generate an accepting hostname, we perform
the following test during an equivalence query and before
calling the Wp-method. First, we search for any wildcard
characters (*) in the provided common name and replace them
with random characters from our alphabet to obtain a concrete
hostname. Next, we check that the generated model and the
target hostname verication implementation agree on a set
of hostnames generated using this method. If not, we return
the hostname for which they differ as a counterexample. The
main advantage of this heuristic is that it allows us to quickly
produce accepting hostnames that uncover new states in the
target system without invoking the Wp-method with very large
depth values. Once these states are uncovered, and the quality
of the inferred models improve, the Wp-method, with a small
depth parameter, is utilized to discover additional states in the
target system.
E. Analysis and comparison of inferred DFA models
After HVLearn outputs a model, the next task for our
system is to analyze the produced model for RFC violations or,
confusing/ambiguous rules in the RFC, to compare different
inferred models and analyze any discrepancies found between
different implementations.
Analyzing a single DFA model.
In the case of a single model,
we would like to determine whether the model is accepting
invalid hostnames prohibited by the RFC specication. If the
specication is unclear, our analysis can still be used in order
to manually inspect the behavior of the implementation on the
specic certicate template besides the differential analysis
described below.
Our system offers two options for performing analysis of
a single model. First, our system generates inputs that will
exercise all simple paths (i.e., paths without loops) that lead
to accepting states, in the inferred model. Intuitively, these
inputs are a small set of inputs that describe all different avors
of hostnames that will be accepted for the given certicate
template. By inspecting these certicates, we can determine if
the implementation is accepting invalid hostnames. Second,
HVLearn allows the user to specify a regular expression
rule to be checked against the inferred model. In this case,
the user species a regular expression and HVLearn veries
that the regular expression and the inferred model does not
share any common strings. This option allows to easily check
certain RFC violations by utilizing simple regular expression
rules. For example, consider the rule specifying that no non-
alphanumeric characters should be part of a matching host-
name. By specifying the regular expression rule “(.)*=(.)*”

--- page 11 ---

we can check whether there exists any matching hostname
that contains the `=' character in the inferred model.
Comparing unique differences between DFA models.
For
analyzing certain corner cases which are not specied in the
RFC, testing a single model may not be enough. Instead, we
compare the inferred models for different SSL/TLS imple-
mentations and nd inputs under which the implementations
behave differently. To perform this analysis, we utilize the
difference enumeration algorithm from [33]. In a nutshell, this
algorithm computes the product DFA between two, or more,
given models and then nds all simple paths to states in which
the DFAs are producing different output.
F. Specication Extraction
As we discussed already, the RFC specications leave cer-
tain aspects of hostname verication up to the implementations
by not specifying the correct behavior in all cases. In these
cases imposing specic restrictions in the implementations is
challenging since we have to be careful to avoid breaking
compatibility with existing implementations and valid cer-
ticates. In this section, we describe how the inferred DFA
models for the different certicate templates can be used to
infer a formal specication, which is compatible with existing
implementations, for the cases where RFC specications are
vague.
Our main insight is the following:
For each certicate
template, we can use the DFA accepting the set of host-
names accepted by all SSL/TLS implementations as a formal
specication of the corresponding rule template.
The intuition
behind this choice is that this specication is avoiding small
idiosyncrasies of each library and it is thus very compact. On
the other hand, if a vulnerability exists in this specication
then this vulnerability must also exist in all tested implemen-
tations. Since each implementation is audited independently,
our choice gives us condence that our specication is se-
cure from simple vulnerabilities while maintaining backward
compatibility with the tested implementations.
Computing the specication.
In order to compute the cor-
responding specication for each certicate template, we pro-
ceed as follows: First, we obtain DFA models for all hostname
verication implementations under test using HVLearn. Next,
we compute the product DFA for all the inferred models. The
product DFA accepts the intersection of the regular languages
of each DFA. We compute the product DFA using standard
automata algorithms [60]. The inferred formal specication for
our set of implementations is represented by the product DFA
of each DFA model. This product DFA can be then converted
back to a regular expression to improve readability.
Finally, we would like to point out that computing the
intersection of
k
DFAs have a worst case time complexity
of
O
(
n
k
)
where
n
is the number of states in each DFA [55].
However, in our case, the inferred DFAs are mostly similar
and thus, the product construction is very efcient because
intersecting two DFAs is not adding a signicant number of
states in the resulting product DFA. We provide more evidence
supporting this hypothesis in Section V.
V. E
VALUATION
The main goals of our evaluation of HVLearn to answer
the following questions: (i) how effective HVLearn is in
nding RFC violations in real-world hostname verication
implementations? (ii) How much do our optimizations help
in improving the performance of HVLearn? (iii) how does
HVLearn perform compare to existing black-box or coverage-
guided gray-box techniques (iv) can HVLearn infer backward-
compatible specications from the inferred DFAs of real-world
hostname verication implementations.
A. Hostname verication test subjects
We use HVLearn to test hostname verication imple-
mentations in six popular open-source SSL/TLS implemen-
tations, namely OpenSSL, GnuTLS, MbedTLS (PolarSSL),
MatrixSSL, JSSE, and CPython SSL, as well as in two popular
SSL/TLS applications: cURL and HttpClient. Note that as
several libraries like OpenSSL versions prior to 1.0.1 do not
provide support for hostname verication and leave it up to
the application developer to implement it. Therefore, applica-
tions like cURL/HttpClient that support different libraries are
often forced to write their own implementations of hostname
verication.
Among the libraries that support hostname verication,
some like OpenSSL provide separate API functions for match-
ing each type of identier (i.e., domain name, IP addresses,
email, etc.) and leave it up to application to select the appro-
priate one depending on the setting. In contrast, others like
MatrixSSL combine all supported types of identiers in one
function and gure out the appropriate by inspecting the input
string. Table I shows the hostname verication function/class
names for all implementations that we tested and the types of
identier(s) that each of them supports. The last column shows
physical source lines of code (SLOC) for each host matching
function/class as reported by the SLOCCount [14] tool. Note
that the shown SLOC only count the parts of the code that
perform hostname matching.
B. Finding RFC violations with HVLearn
We use HVLearn to produce DFA models for each distinct
certicate template corresponding to different patterns from
the RFCs. Afterward, we detect potentially buggy behavior
by both performing differential testing of output DFAs as
well as checking individual DFAs for violations of regular-
expression-based rules that we created manually as described
in Section IV-E.
Table II presents the results of our experiments. We eval-
uated a diverse set of rules from four different RFCs [16],
[17], [21], [24]. We found that every rule that we tested is
violated by at least one implementation, while on average each
implementation is violating three RFC rules. Several of these
violations have severe security implications (e.g., mishandling
wildcard characters in international domain names, confusing
IP addresses as domain names etc.). We describe these cases
along with their security implications in detail in Section VI.

--- page 12 ---

TABLE I
H
OSTNAME VERIFICATION FUNCTIONS
(
ALONG WITH THE TYPES OF
SUPPORTED IDENTIFIERS
)
IN
SSL/TLS
LIBRARIES AND APPLICATIONSSSL/TLS Version Supported Hostname Matching Approx.
Libs/Apps Identier(s) Function/Class Name SLOCOpenSSL
6
1.0.1 – – –
OpenSSL
>
1.0.2 CN/DNS X509checkhost 314
IP X509checkip 308
IP X509checkipasc 417
EMAIL X509checkemail 314GnuTLS
3.5.3 CN/DNS/IP gnutlsx509crtcheckhostname, 195
gnutlsx509crtcheckhostname2
EMAIL gnutlsx509crtcheckemail 149MbedTLS
2.3.0 CN/DNS mbedtlsx509crtverify, 193
mbedtlsx509crtverifywithproleMatrixSSL
3.8.4 CN/DNS/IP/ matrixValidateCerts 130
EMAILJSSE
1.8 CN/DNS/IP HostnameChecker 202CPython SSL
3.5.2 CN/DNS/IP matchhostname 59HttpClient
4.5.2 CN/DNS/IP DefaultHostnameVerier 257cURL
7.50.3 CN/DNS/IP verifyhost, 300
CurlverifyhostNote that the library with the most violations is JSSE
(four violations), while HttpClient is the application with the
most violations (ve violations). OpenSSL, MbedTLS, and
CPython SSL only have two violations each, having common
the violation of matching invalid hostnames. The interested
reader can nd an extended description of our results in the
Appendix (Table VIII).
C. Comparing unique differences between DFA models
In order to evaluate the discrepancies between all differ-
ent hostname verication implementations, we computed the
number of differences for each pair of hostname verication
implementations in our test set. Recall that for two given DFA
models we dene the number of differences as the number of
simple paths in the product DFA which lead to a different
output being produced by the two models [33].
Table III presents the results of our experiment. For exam-
ple, OpenSSL and GnuTLS have 95 discrepancies in total. This
is obtained by summing up the number of unique paths that are
different between the inferred DFAs for each common name
in Table VIII. Note that all pairs of implementations contain
a large number of unique cases under which they produce a
different output. As seen in Table III, each pair of tested im-
plementation has
127
unique differences on average between
them. We note that some differences only imply ambiguous
RFC rules while some reveal the potential invalid hostnames
or RFC violation bugs. The interested reader can nd a more
detailed list of the unique strings that each implementation
is accepting in Table VIII in the Appendix. In any case,
we nd the fact that all implementations of such a security
critical component of the SSL/TLS protocol present such a
larger number of discrepancies to be an alarming issue since
it signies either a poor implementation of the specication
or vagueness in the specication itself. Our analysis suggests
that both cases are present in practice.
D. Comparing code coverage of HVLearn and black/gray-box
fuzzing
In order to compare HVLearn's effectiveness in nding
bugs with that of black/gray-box fuzzing, we investigate the
following research question:
RQ.1: How HVLearn's code coverage differ from black/gray-
box fuzzing techniques?
We compare the code coverage of the tested hostname veri-
cation implementations achieved by HVLearn and two other
techniques, black-box fuzzing, and coverage-guided gray-box
fuzzing. We describe our testing setup briey below.
HVLearn
: HVLearn leverages automata learning that invokes
the hostname verication matching routine with a predened
certicate template and alphabet set. HVLearn adaptively
renes a DFA corresponding to the test hostname verication
implementation by querying the implementation with new
hostname strings. We measure the code coverage achieved
during the learning process until it nishes. We also monitor
the total number of queries
NQ
, which comes from both the
membership and the equivalence queries.
Black-box fuzzing
: With the same alphabet and certicate
template used by HVLearn, we randomly generate
NQ
strings
and query the target SSL/TLS hostname verication function
with the same certicate template. Note that the black-box
fuzzer generates independent random strings without any sort
of guidance.
Coverage-guided gray-box fuzzing
: Unlike black-box
fuzzing, coverage-guided gray-box fuzzing tries to generate
more interesting inputs by using evolutionary techniques to
the input generation process. In each generation, a new batch
of inputs are generated from the previous generation through
mutation/cross-over and only the inputs that increase code
coverage are kept for further changes. Coverage-guided gray-
box fuzzing is a popular technique for nding bugs in large
real-world programs [6], [11].
To make it a fair comparison with HVLearn, we imple-
mented our own coverage-guided gray-box fuzzer as existing
tools like AFL do not provide an easy way of restricting
the mutation outputs within a given alphabet. With the same
alphabet set, we initialize the fuzzer with a set of strings of
varying lengths as the seeds maintained in a queue
Q
. The
seeds are then used by the fuzzer to query the target hostname
verication implementation. After nishing querying, using
the seeds, the fuzzer gets the string
S
=
dequeue
(
Q
)
. It
randomly mutates one character within
S
and obtains
S
0
. Then
it uses the mutated
S
0
to query the target. If the mutated
string
S
0
increased code coverage, we store it in the queue for
further mutation, i.e.,
enqueue
(
S
0
; Q
)
. Otherwise, we throw
it away. The fuzzer is thus guided to always mutate on the
strings that have better code coverage. The fuzzer iteratively
performs this enqueue/dequeue operations for
NQ
rounds,
and we obtain the nal code coverage
COV
randmu
of each

--- page 13 ---

TABLE II
A
SUMMARY OF
RFC
VIOLATIONS AND DISCREPANT BEHAVIORS FOUND BY
HVL
EARN IN THE TESTED
SSL/TLS
LIBRARIES AND APPLICATIONSRFC ViolationsRFC OpenSSL
GnuTLS
MbedTLS
MatrixSSL
JSSE
CPython SSL cURL
HttpClient
HttpClient* Invalid hostname characterOnly alphanumeric and `-' matches in hostname10357 7 7 3 7 77 7 7Case-insensitive hostnameMatch CN in case-insensitive manner5280, 61253 3 3 3 3 33 7 7WildcardNot attempt to match wildcard not in left-most label (CN/DNS: aaa.*.aaa)61253 3 3 3 7 33 7 3IDN and wildcardNot attempt to match wildcard fragment in IDN (xn
--
a*.aaa)61253 3 3 3 7 33 7 3Common name and subjectAltNameNo CN checked when DNS presents61253 3 3 7 3 33 3 3
No CN checked when any SAN ID presents6125–
7
–
7 7 33 7 7Email-based certicateCase-sensitive on local-part of email attribute in SAN52803 3
–
7
– –– – –IP address-based certicateNot attempt to match IP address with DNS (DNS: 1.1.1.1)1123–
7 7 7 3 33 3 3DiscrepanciesWildcardAttempt to match wildcard with empty label (hostname: .aaa.aaa with CN/DNS: *.aaa.aaa)–3 3 7 7 7 77 3 3
Attempt to match wildcard in public sufx (CN/DNS: *.co.uk)61253 7 3 3 3 33 3 7Embedded NULL characterAllowed NULL character in CN–3 3 3 7 3 33 3 3
Allowed NULL character in SAN–3 3 7 7 3 33 3 3
Match NULL character hostname: b.b
n
0.a.a, CN/DNS: b.b
n
0.a.a–7 7 7 7 3 37 3 3Other invalid hostnamePartially match sufx (hostname: .a with CN/DNS: a.a, a.a.a)10353 7 7 7 7 77 7 7
Match trailing dot (hostname: aaa.aaa with CN/DNS: aaa.aaa)–7 7 7 7 7 73 7 7HttpClient*
: HttpClient with
PublicSuffixMatcher
For RFC Violation:
3
= OK,
7
= RFC violate, – = libs/apps do not support

For Discrepancies:
3
= Accept,
7
= Reject
TABLE III
N
UMBER OF UNIQUE DIFFERENCES BETWEEN AUTOMATA INFERRED FROM
DIFFERENT
SSL/TLS
IMPLEMENTATIONS OpenSSL
GnuTLS
MbedTLS
MatrixSSL
JSSE
CPython HttpClient
Curl OpenSSL– 95 98 99 282 92482 187GnuTLS–
– 6 38 127 34214 56MbedTLS–
–
– 44 97 28220 50MatrixSSL–
–
–
– 37 2558 94JSSE–
–
–
–
– 69177 110CPython–
–
–
–
–
–108 54HttpClient–
–
–
–
–
–– 414Curl–
–
–
–
–
––
–functions SSL/TLS implementations. Note that we keep the
test certicate template xed during the entire test.
We use the percentage of lines executed, which are extracted
by Gcov [51], as the indicator for the code coverage. Consider-
ing that hostname verication is a small part of an SSL/TLS
implementation, we do not compute the percentage of lines
covered with respect to the total number of lines. Instead, we
calculate the percentage of line coverage within each function
and only take into account the functions that are related to
Fig. 4. Comparison of code coverage achieved by HVLearn, gray-box fuzzing,
and black-box fuzzing for OpenSSL hostname verication.
hostname verication.
Result 1:
HVLearn achieves 11.21% increase in code
coverage on average when comparing to the black/gray-
box fuzzing techniques.Therefore, let LE(
f
) be the number of lines executed of
function
f
in the
SI
and L(
f
) be the total number of lines
of
f
, the code coverage can be dened in the following equa-

--- page 14 ---

0 10 20 30 40 50 60 70 80 90 100 0 10000 20000 30000 40000 50000% of line coverageNumber of queries
HVLearnCoverage-guided gray-box fuzzingBlackbox fuzzing

--- page 15 ---

tion:
coverage
=
P
m
i
=1
LE
(
f
i
)P
m
i
=1
L
(
f
i
)
, where
f
1
; f
2
;
  
; f
m
are the
functions that are relevant to hostname verication. Figure 4
illustrates the code coverage comparison, which shows that
HVLearn achieves signicantly better code coverage compared
to the black/gray-box fuzzing techniques.
E. Automata learning performance
HVLearn is largely based on the KV algorithm and the
Wp-method in order to perform its analysis. It is therefore
crucial to thoroughly evaluate the different parameters of these
algorithms and their impact on the performance of HVLearn.
We will now evaluate the effect of each different parameter
of the learning algorithms in the overall performance of
HVLearn.
RQ.2: How does the alphabet size affect HVLearn's perfor-
mance in practice?
As discussed in Section III-C, the alphabet size impacts
the performance of our system. In theory, the performance of
both the KV algorithm and the Wp-method, depends on the
size of the input alphabet. We perform two experiments for
evaluating the extent to which the alphabet size affects the
performance of our learning algorithm component in practice.
In the rst experiment, we evaluate the effect of increasing
the size of the alphabet in real world DNS names. For this
experiment, we used our system in the default conguration
with all optimizations (e.g., query cache and EQ optimizations)
enabled and we set the Wp-method depth to 1. We used the
CPython's SSL implementation as the hostname verication
function for these experiments.
Figure 5 shows the results of our experiment. Notice that,
starting from an alphabet size of 9, each additional character
we include in the alphabet will cause the learning algorithm
to perform at least 10% more queries in order to produce a
model, for both DNS names, while this percentage is only
increasing when in larger alphabet sizes.
We also measure the effect of increasing the alphabet size
on the overall running time of our system. To perform this
experiment we used the same setup as our previous experiment
and evaluated the performance of HVLearn with a certicate
containing the common name “*.aaa.aaa”. Table IV shows
the results of this experiment. We notice that the increase
in the membership queries directly translates in an increased
running time. Specically, by adding 5 additional characters
in the alphabet (from 2 to 5), we notice that the running time
increases 7 times. Similar results can be observed when we
add more characters in the alphabet set.
Result 2:
Adding just one symbol in the alphabet set
incurs at least 10% increase in the number of queries.
Thus, the succinct alphabet set utilized by HVLearn is
crucial for the system's performance.RQ.3: Does membership cache improve the performance of
HVLearn?
Table IV presents the number of queries required to infer
a model for the certicate template with common name
Fig. 5. Number of queries required to learn an automaton with different
alphabet sizes (with Wp-method depth=1 and equivalence query optimization).
TABLE IV
HVL
EARN PERFORMANCE FOR COMMON NAME
*
.
A A A
.
A A A
WITH
W
P
-
METHOD DEPTH
=1 (CP
YTHON
SSL
IMPLEMENTATION
)Alphabet
SizeW/o CacheWith Cache#Queries#QueriesAverage
Time
(sec)TotalTotalMembershipEquivalenceCounterexampleMembership28832261362903.1053,0491,58243621,14621.6175,1633,15663622,52042.24109,3396,52293625,58686.921518,97914,8121,436213,376196.35 Fig. 6. The number of queries needed to learn the DFA model of CPython
certicate verication for different Wp-method depth values (without equiv-
alence query optimization).
“*.aaa.aaa” with and without utilizing a membership query
cache over different alphabet sizes. We notice that the cache
is consistently helping to reduce the number of membership
queries required to infer a model. Overall, the cache is
reducing the number of queries by 42%, thus signicantly
improving the efciency of our system. Therefore, for the rest
of the experiments in this section, we utilize our system with
the membership query cache enabled.
Result 3:
Membership cache is offering, on average,
a 42% decrease on the number of membership queries
made by the learning algorithm.RQ.4: How does Wp-method's depth parameter affect
HVLearn's performance and accuracy?
As discussed in Section IV-D, the number of queries per-
formed by the Wp-method is exponential on the customizable
depth parameter. We evaluated how this exponential term is

--- page 16 ---

5000 10000 15000 20000 25000 30000 3500091011121314Number of queriesAlphabet size*.google.comtwitter.com

--- page 17 ---

0 20000 40000 60000 80000 100000 120000 1 2 3 4 5 6 7 8 9 10(n): n inferred states(1) (1) (1) (1) (1) (1)
(1)
(11)
(11)
(11)Number of queriesWP-method depth

--- page 18 ---

affecting the number of queries in practice and moreover, what
is the effect of different values of the depth parameter on the
correctness of the models inferred by HVLearn.
For our rst experiment, we explore the correlation between
the overall number of membership queries and the corre-
sponding depth parameter. The results of this experiment are
presented in Figure 6 and Table V. In order to ensure that
the experiment nishes within a reasonable time, we further
reduced the alphabet size only to two symbols. the results
clearly show that the dependence between the depth parameter
and the overall number of queries performed by the learning
algorithm is clearly exponential, and in fact exactly matches
the
O
(
j

j
d
)
bound where
d
is the depth parameter as discussed
in Section IV-D. Notice that when the depth parameter of the
Wp-method is set to a value less than 8, HVLearn fails to
infer any aspect of the target implementation and outputs a
single state DFA model that rejects all hostnames as shown in
Table V.
Result 4:
Large values of the Wp-method depth pa-
rameter result in impractical running times while small
values result in incomplete models.RQ.5: How much improvement is offered by the equivalence
query optimization in HVLearn?
The previous experiment clearly demonstrates that the Wp-
method alone is not efcient enough to accurately analyze a
variety of different templates with HVLearn. Using our full
alphabet, inferring a complete model for the common name
“*.aaa.aaa” requires the depth parameter to be

8
as shown
in Table V. With our full alphabet of 13 symbols this would
require around
2
30
queries based on the query complexity of
the algorithm. We nd that even running the algorithm with a
depth of 6, which is still not able to infer a complete model,
results in more than 68 million queries.
Therefore, our equivalence query optimization is a crucial
component of HVLearn that allows it to produce accurate
DFA models that can be used to evaluate the security and
correctness of the implementations. As we can see from
Table V, using our equivalence query optimization and a
depth parameter of just 1, our system is able to produce a
complete model for a given certicate template. Running the
same experiment with the alphabet size 15, we found that
HVLearn infers a correct model using only 14,812 queries as
shown in Table IV.
Result 5:
EQ optimization is providing, in some cases,
over one order of magnitude improvement on the number
of queries required to infer a complete DFA model.F. Specication Extraction
Let us now examine how we can utilize HVLearn's spec-
ication extraction functionality in order to infer a practical
specication for the rule corresponding to the common name
“*.a.a”. This rule corresponds to the basic wildcard certicate
case where a wildcard is found in the leftmost label of the
TABLE V
T
HE NUMBER OF QUERIES NEEDED TO LEARN THE
DFA
MODEL OF
CP
YTHON CERTIFICATE VERIFICATION FOR DIFFERENT
W
P
-
METHOD
DEPTH VALUESWp.
DepthW/o EQ OptimizationWith EQ Optimization#Queries #States Complete?#Queries #States Complete?17 1
7226 11
3215 1
7448 11
3331 1
7890 11
3463 1
71,778 11
35127 1
73,554 11
36255 1
77,104 11
37511 1
714,207 11
3828,415 11
328,415 11
3956,831 11
356,831 11
310113,663 11
3113,663 11
3 (a) OpenSSL
(b) GnuTLS, JSSE,
and HttpClient
(c) MbedTLS,
MatrixSSL, and
CPython
(d) cURL
(e) Intersection
Fig. 7. SSL/TLS implementations' DFA and intersection DFA with CN/DNS:
*
.a.a
and alphabet:
f
a
,
.
g
identier. Nevertheless, Figure 7 demonstrates that even for
this simple rule, the corresponding DFA models for different
implementations present obvious discrepancies. For example,
DFA model (a) accepts the hostname “.a”, model (b) accepts
the hostname “.a.a”, while model (d) accepts the hostname
“a.a.a.”. Only model (c) perform the most intuitive matching

--- page 19 ---

02dot5a16dot8aadot34adotdotadota7adotadotadot

--- page 20 ---

0a4dot12a5dotadot3dotaadotadot

--- page 21 ---

05a6dot12adotadot3dota4adotdotaadot

--- page 22 ---

05a6dot12adota7dot3dota4adotdotaadotadot

--- page 23 ---

02dot6a1adotadot3adot4adot5dotadota

--- page 24 ---

by only accepting hostnames matching the regular expression
“a+.a.a” (here `+' denotes one or more repetitions of the
character `a').
By computing the intersection between all DFA models, we
obtain the intersection DFA model (e). Our rst observation
is that the intersection DFA has only 6 states and it is thus
very compact as discussed in Section V-F. Furthermore, we
notice that the intersection DFA is the same as DFA (c)
that corresponds to the most natural implementation of the
corresponding rule. More importantly, even if we compute the
intersection without including model (c), we will still infer
the same specication. Thus, we conclude that computing the
intersection of DFA models, even from implementations which
fail in different ways, can often produce compact and natural
specications.
Size of inferred models.
In general, the actual size of the
inferred models is heavily dependent on the implementation
details of the tested system. However, we expect that the DFA
models inferred by our system will have around
l
+ 2
states,
where
l
is the length of the common name in the certicate
template. Indeed, if we consider the inferred DFAs in Figure 7
we can notice that, for the common name “*.a.a” with length
l
= 5
, the average number of states is 6.9, which is very close
to the expected
7
states. Intuitively, the reasoning behind this
size is that a DFA for matching a string of length
l
is expected
to have
l
+ 2
states in general where
l
states are moving the
DFA forward towards the accepting state while the additional
2 states include the initial state and a
sink
state where the DFA
goes when no match is found.
VI. C
ASE
S
TUDY OF
B
UGS
The goal of our study aims at understanding the severity of
potential exploitation by incorrect or unclear hostname check
in certicate verication. We are also interested in nding any
inconsistency of SSL/TLS implementations' hostname checks
with what RFC species. In this section, we present some
interesting cases we achieved from the result of our experiment
or corner cases we found.
A. Wildcards within A-labels in IDN identiers
RFC 6125 strictly prohibits matching a certicate with an
identier containing wildcards embedded within an A-label
of an IDN. For a certicate with an identier of the form
“xn
--
aa*”, it is very difcult to predict the set of unicode
strings that will be matched after they are transformed into the
punycode format due to the complexity of the transformation
process. This inability to easily predict the set of hostnames
which match an A-label with an embedded wildcard often
present avenues for man-in-the-middle attacks.
Hostname verication implementations which match iden-
tiers with wildcards embedded within A-labels have been
found recently in the Ruby OpenSSL extension [28] and the
NSS library used by Mozilla Firefox [27]. These issues were
identied as security vulnerabilities by the developers of the
corresponding products.
Using HVLearn, we identied that both JSSE and Http-
Client (without using
PublicSuffixMatcher
in construc-
tor) were also vulnerable to this issue. Our tool also reported
that the other tested libraries/applications were not affected.
B. Confusing order of checking between CN and SAN identi-
ers.
RFC 6125 explicitly species that applications should not
attempt to match the hostname with the subject CN when any
subjectAltName identiers are present, regardless of whether
there is a match in subjectAltName as shown in Section II).
We found a number of violations of that rule using HVLearn as
described in Table II. We also found that MatrixSSL exhibits
an interesting behavior in such cases.
More specically, MatrixSSL matches the CN identier
before attempting to match any identiers in the SAN even
if they are present in the certicate. Note here that the CN
does not have any strong restrictions on its content and may
even contain non-FQDN characters (e.g., UTF-8).
Therefore, it is possible that certain certicate authorities,
following the instructions in RFC 6125, will not check the CN
in the presence of SAN identiers and will issue a certicate
regardless of the value in the CN as long as the user is
successfully identied as the owner of the domains in the SAN
identier. Albeit natural, this choice will render applications
using MatrixSSL vulnerable to a simple man-in-the-middle
attack.
Specically, an attacker can generate a signed certicate
with a SAN identier for a domain owned by the attacker, say
“www.attacker.com” and have the CN eld set to the victim
domain, say “www.bank.com”. MatrixSSL will rst check
the CN and omit to check the SAN identiers. Therefore,
MatrixSSL will allow the attacker to hijack any domain which
is present in the CN eld (e.g., www.bank.com).
C. Hijacking IP-based certicates
Section 2.3.1 of domain names implementation and speci-
cation in RFC [16] dictates that the preferred name (label)
should only begin with a letter character. However, RFC [17]
changed this restriction to allow the rst character to be a letter
or a digit. This change introduced valid DNS names which are
identical to IP addresses.
Unfortunately, the fact that IP addresses are also valid DNS
names may open a new avenue for an attack as we describe
below. Notice that, for this attack to become practical, a
numeric Top Level Domain (TLD) in the range 0-255 must
exist, something that is currently unavailable. Nevertheless,
our description should be taken as a precautionary note for
new TLDs.
The attack is based on the fact that certain implementations
rst check if the given hostname matches the certicate's
CN/SAN as a domain name and afterward as IP address.
Therefore, consider an attacker controlling an IP address,
say 80.50.12.33 and holding an IP-based certicate with that
IP address. Then, assuming that “33” is a valid TLD, the
same entity is automatically in possession of a certicate for

--- page 25 ---

TABLE VI
B
EHAVIORS OF
SSL/TLS
IMPLEMENTATIONS FOR
X.509
CERTIFICATES
WITH
IP
V
4
ADDRESSES IN
CN/
SUBJECT
A
LT
N
AMESSL/TLSCerticate with IPv4 inLibs/AppsSubject CNSubjectAltName DNSOpenSSLappappGnuTLSacceptacceptMbedTLSaccept*accept*MatrixSSLacceptacceptJSSErejectrejectCPython SSLacceptrejectHttpClientacceptrejectcURLacceptrejectapp: library lets application choose the identier type.
accept*: library/application does not support IP-based certication verication
but allows IPv4-format string in hostname verication.
the
domain name
“80.50.12.33” and can perform man-in-the-
middle attacks on that domain!
We evaluated whether this attack is feasible in current
SSL/TLS implementations. Table VI shows the results of our
evaluation. All libraries/applications which are marked with
an
accept
either in the subject CN or subjectAltName DNS
columns are vulnerable to this attack. Even though this issue
is not currently exploitable, it presents a security risk for these
libraries in case numerical TLDs are introduced in future.
D. Embedded NULL bytes in CN/SAN identiers
In 2008, Kaminsky et al. [53] demonstrated a vulnerabil-
ity in the hostname verication implementations of popular
SSL/TLS libraries where early NULL-byte (
n
0) terminations
in an X.509 CN causes some libraries to recognize different
CN values. In a nutshell, a client accepts certicate from an
attacker's subdomain “www.bank.com
n
0.attacker.com” when
attempting to connect to “www.bank.com” and therefore allow
the attacker to hijack the connection.
In order to defend against this attack, two lines of defense
were followed. The rst option was to reject any certicate
containing NULL bytes embedded within any CN/SAN iden-
tiers. The second line was to simply patch the API functions
which retrieve the CN/SAN identiers from the certicate in
order to recover the entire identier even in the presence of
embedded NULL bytes.
We thoroughly evaluated the defense implemented in each
SSL/TLS library. Table VII presents the results of our evalu-
ation. The second column describes whether the SSL/TLS li-
brary allows embedded NULL bytes, the third column presents
the corresponding API function which is used to retrieve the
CN/SAN identier, and the fourth column describes whether
the API call also returns the length of the corresponding
CN/SAN identier. Note that this is a very important feature
since, otherwise, the application using the SSL/TLS library
cannot know where the identier string is terminating. We no-
tice that this important feature is implemented by all libraries
except JSSE. Notice though that, even though JSSE is not
returning the length of the corresponding identier, since JSSE
is written in Java, it is not vulnerable to the embedded NULL
byte attacks because Java strings are not NULL terminated.
TABLE VII
S
UPPORT FOR EMBEDDED NULL CHARACTER IN
CN/
SUBJECT
A
LT
N
AME
IN DIFFERENT
SSL/TLS
LIBRARIESSSL ID Allows Function / Structure Name Returns
Libraries Embedded Length
NULL?OpenSSL
CN
3
X509NAMEgettextbyNID()
3
CN
3
X509NAMEgettextbyOBJ()
3
CN
3
X509NAMEgetindexbyNID()
1
3
CN
3
X509NAMEgetindexbyOBJ()
1
3
SAN
3
X509getextd2i()
2
3GnuTLS
CN
3
gnutlsx509crtgetdnbyoid()
3
SAN
3
gnutlsx509crtgetsubjectaltname()
3MbedTLS
CN
3
mbedtlsx509name
3
SAN
7
mbedtlsx509sequence
3MatrixSSL
CN
7
x509DNattributest
7
SAN
7
x509GeneralNamet
3JSSE
CN
3
getSubjectX500Principal()
7
SAN
3
getSubjectAlternativeNames()
7CPython SSL
— Functionality not exposed to apps —1
followed by X509NAMEgetentry()
2
followed by skGENERALNAMEvalue()
Despite the fact that SSL/TLS implementations take pre-
cautions against embedded NULL byte attacks, this doesn't
imply that the applications using the libraries are also secure.
Indeed, applications implementing the hostname verication
functionality must ensure that they do not use vulnerable
functions such standard string comparison function from libc
(e.g.,
strcmp, strcasecmp, fnmatch
), as they match
strings in NULL-termination style.
In order to evaluate the security of applications using
SSL/TLS libraries against embedded NULL byte attacks, we
conducted a manual audit against several applications. Un-
fortunately, we found several popular applications being vul-
nerable to man-in-the-middle attacks using embedded NULL
byte certicates. Some examples include FreeRadius server [8]
which is one of the most widely deployed RADIUS (Remote
authentication dial-in user service) servers, OpenSIPS [12]
which is a popular open-source SIP server, Proxytunnel [13]
which is a stealth tunneling proxy, and Telex Anticensorship
system [15] which is an open-source censorship-circumventing
software.
An important takeaway from this section is that embedded
NULL byte attacks, even though addressed at the SSL/TLS
library level, still present a very realistic and overlooked threat
for applications using these libraries.
VII. R
ELATED
W
ORK
A. Securing SSL/TLS Implementations
The security analysis of different components of SSL/TLS
implementations has been examined in a large number of
projects. We provide a summary of the most related projects
below. The key difference between these projects and ours
is that none of these projects focused on automatically an-
alyzing the correctness of the hostname verication part of
SSL/TLS certicate validation implementations. Prior works
didn't cover analyzing hostname verication in detail primarily

--- page 26 ---

due to the hardness of accurately modeling the implementa-
tions. In this paper, we solve this problem by using automata
learning techniques and demonstrating that they can accurately
and efciently infer DFA models of hostname verication
implementations in a black-box manner.
Automated Analysis of SSL/TLS implementations.
Brubaker et al. [36] and subsequently Chen et al. [39] used
mutation-based differential testing to nd certicate validation
issues. However, in their case, the hostname verication
functionality of the libraries under test is disabled in order
to discover other certicate validation issues and thus, they
cannot uncover bugs discovered by our work. He et al. [52]
used static analysis to detect incorrect usage of SSL/TLS
libraries APIs. Somorovsky [61] created TLS-Attacker a tool
to fuzz the TLS implementations systematically. However,
TLS-Attacker focused on nding bugs in the protocol level
and did not analyze the hostname verication functionalities
of SSL/TLS implementations. Finally, de Ruiter and Poll [41]
used automata learning algorithms to infer models of the
TLS protocol and manually inspected the machines to nd
bugs. Contrary to our approach, where we focus on analyzing
hostname verication implementations, their work focused
on the TLS state machine induced by the different messages
exchanged during the TLS handshake.
Certicate validation.
Georgiev et al. [50] studied different
ways that SSL/TLS API was abused in non-browser software.
They manually identied pervasive incorrect certicate valida-
tion in different SSL/TLS implementations on which critical
software rely. Fahl et al. [45] investigated the incorrect usage
of SSL/TLS API in Android apps. However, unlike HVLearn,
none of these projects looked into the implementations of the
API functions.
Parsing X.509 certicates with embedded NULL character.
Kaminsky et al. [53] demonstrated that several hostname ver-
ication implementations mishandled embedded NULL char-
acters in X.509 certicates and can be used to trick a CA into
issuing a valid leaf certicate with the wrong subject name.
However, they found this issue manually and did not have
any automated techniques for analyzing hostname verication
implementations. Moreover, these issues were supposed to be
xed by the SSL/TLS implementations but we nd that several
applications using incorrect APIs for extracting the identier
strings from a certicate still suffer from these vulnerabilities
as described in Section VI.
Cryptographic attacks and implementation bugs.
There is
a large body of work on various cryptographic attacks on
the SSL/TLS protocol implementations. The interested reader
may consult [40] for a survey. These attacks include various
protocol based attacks [35], [43], [44], [46] as well as timing
attacks [37] and aws in pseudo-random number genera-
tors [57]. Besides cryptographic attacks, implementation bugs
may cause severe security vulnerabilities as demonstrated by
recently discovered attacks [26], [56].
B. Automata inference and applications
Angluin [31] invented the
L

algorithm for learning deter-
ministic nite automata (DFA) from membership and equiv-
alence queries. In the following years, many variations and
optimizations were developed, including the Kearns-Vazirani
algorithm used in HVLearn [54]. The interested reader can
read the paper by Balcazzar et al. [34] for a unied presen-
tation of popular algorithms. Automata learning algorithms
have been applied to infer models for various protocols such
as EMV bank cards [29], electronic passports [30], TLS
protocols [41] and TCP/IP implementations [47], [48].
Argyros et al. [33] utilized symbolic nite automata learning
algorithms to create a differential testing framework and lever-
aged it to discover bugs in Web application rewalls. While
our approach is similar in nature, we counter the problem
of large alphabets by using only the necessary symbols for
our analysis. Moreover, instead of using differential testing to
simulate equivalence queries, our approach uses an optimized
version of the Wp-method, which offers stronger correctness
guarantees.
VIII. C
ONCLUSION
We designed, implemented and extensively evaluated
HVLearn, an automated black-box automata learning frame-
work for analyzing different hostname verication imple-
mentations. HVLearn supports automated extraction of DFA
models from multiple different implementations as well as
efcient differential testing of the inferred DFA models. Our
extensive evaluation on a broad spectrum of hostname veri-
cation implementations found
8
RFC violations with serious
security implications. Several of these RFC violations could
enable active man-in-the-middle attacks. We also discovered
121
unique differences on average between each pair of
inferred DFA models. In addition, given that the RFC speci-
cations are often ambiguous about corner cases, we expect
that the models inferred by HVLearn will be very useful
to the developers for checking their hostname verication
implementations against the RFC specications and therefore
can help in reducing the chances of undetected security aws.
We have made HVLearn open-source so that the community
can continue to build on it. The framework can be accessed
at https://github
:
com/HVLearn.
IX. A
CKNOWLEDGMENTS
We would like to thank the anonymous reviewers for
their feedback. This work was supported by the NSF under
grants CNS-13-18415 and CNS-16-17670. Author Suphannee
Sivakorn is also partially supported by the Ministry of Science
and Technology of the Royal Thai Government. Any opinions,
ndings, conclusions, or recommendations expressed herein
are those of the authors, and do not necessarily reect those
of the US Government or the NSF.
R
EFERENCES
[1] https://gitlab
:
com/gnutls/gnutls/mergerequests/314.
[2] https://gitlab
:
com/gnutls/gnutls/issues/185.

--- page 27 ---

[3] https://gitlab
:
com/gnutls/gnutls/issues/187.
[4] http://www
:
matrixssl
:
org/blog/releases/matrixssl390.
[5] https://issues
:
apache
:
org/jira/browse/HTTPCLIENT-1802.
[6] American Fuzzy Lop (AFL) Fuzzer. http://lcamtuf
:
coredump
:
cx/a/.
[7] cURL - Compare SSL Libraries. https://curl
:
haxx
:
se/docs/ssl-
compared
:
html.
[8] FreeRADIUS. http://freeradius
:
org/.
[9] GnuTLS 3.5.10: X509 certicate API. https://goo
:
gl/ZSbNGb.
[10] Java Native Interface (JNI). https://docs
:
oracle
:
com/javase/8/docs/
technotes/guides/jni/.
[11] libFuzzer - A Library for Coverage-guided Fuzz Testing. http://llvm
:
org/
docs/LibFuzzer
:
html.
[12] OpenSIPS. https://github
:
com/OpenSIPS/opensips.
[13] proxytunnel. http://proxytunnel
:
sf
:
net.
[14] SLOCCount. https://www.dwheeler.com/sloccount/.
[15] Telex Anticensorship. https://github
:
com/ewust/telex.
[16] RFC 1035 - DOMAIN NAMES - IMPLEMENTATION AND SPECI-
FICATION. https://tools
:
ietf
:
org/html/rfc1035, November 1987.
[17] RFC 1123 - Requirements for Internet Hosts – Application and Support.
https://tools
:
ietf
:
org/html/rfc1123, October 1989.
[18] RFC 2818 - HTTP Over TLS. https://tools
:
ietf
:
org/search/rfc2818, May
2000.
[19] RFC 3492 - Punycode: A Bootstring encoding of Unicode for Interna-
tionalized Domain Names in Applications (IDNA). https://tools
:
ietf
:
org/
html/rfc3492, March 2003.
[20] RFC 4985 - Internet X.509 Public Key Infrastructure Subject Alternative
Name for Expression of Service Name. https://tools
:
ietf
:
org/html/
rfc4985, August 2007.
[21] RFC 5280 - Internet X.509 Public Key Infrastructure Certicate and
Certicate Revocation List (CRL) Prole. https://tools
:
ietf
:
org/html/
rfc5280, May 2008.
[22] RFC 5321 - Simple Mail Transfer Protocol. https://tools
:
ietf
:
org/html/
rfc5321, October 2008.
[23] RFC 5890 - Internationalized Domain Names for Applications (IDNA):
Denitions and Document Framework. https://tools
:
ietf
:
org/html/
rfc5890, August 2010.
[24] RFC 6125 - Representation and Verication of Domain-Based Appli-
cation Service Identity within Internet Public Key Infrastructure Using
X.509 (PKIX) Certicates in the Context of Transport Layer Security
(TLS). https://tools
:
ietf
:
org/html/rfc6125, March 2011.
[25] RFC 6818 - Updates to the Internet X.509 Public Key Infrastruc-
ture Certicate and Certicate Revocation List (CRL) Prole. https:
//tools
:
ietf
:
org/html/rfc6818, January 2013.
[26] CVE-2014-0092, March 2014.
[27] CVE-2014-1492, March 2014.
[28] CVE-2015-1855, March 2015.
[29] F. Aarts, J. D. Ruiter, and E. Poll. Formal Models of Bank Cards
for Free. In
Proceedings of the International Conference on Software
Testing, Verication and Validation Workshops
, pages 461–468, 2013.
[30] F. Aarts, J. Schmaltz, and F. Vaandrager. Inference and Abstraction
of the Biometric Passport. In
Proceedings of the International Confer-
ence on Leveraging Applications of Formal Methods, Verication, and
Validation
, pages 673–686, 2010.
[31] D. Angluin. Learning Regular Sets from Queries and Counterexamples.
Inf. Comput.
, 75(2):87–106, 1987.
[32] Apache Software Foundation. Apache HttpComponents - HttpCom-
ponents HttpClient Overview. https://hc
:
apache
:
org/httpcomponents-
client-ga/.
[33] G. Argyros, I. Stais, S. Jana, A. D. Keromytis, and A. Kiayias. SFAD-
iff: Automated Evasion Attacks and Fingerprinting Using Black-box
Differential Automata Learning. In
Proceedings of the ACM SIGSAC
Conference on Computer and Communications Security
, pages 1690–
1701, 2016.
[34] J. L. Balc
´
azar, J. D
´
az, R. Gavalda, and O. Watanabe.
Algorithms for
Learning Finite Automata from Queries: A Unied View
, pages 53–72.
Springer, 1997.
[35] D. Bleichenbacher. Chosen ciphertext attacks against protocols based on
the RSA encryption standard PKCS# 1. In
Proceedings of the Annual
International Cryptology Conference on Advances in Cryptology
, pages
1–12, 1998.
[36] C. Brubaker, S. Jana, B. Ray, S. Khurshid, and V. Shmatikov. Using
Frankencerts for Automated Adversarial Testing of Certicate Validation
in SSL/TLS Implementations. In
Proceedings of the IEEE Symposium
on Security and Privacy
, pages 114–129, 2014.
[37] D. Brumley and D. Boneh. Remote Timing Attacks Are Practical. In
Proceedings of the USENIX Conference on Security Symposium
, pages
1–1, 2003.
[38] Y. Chen and Z. Su. Guided Differential Testing of Certicate Validation
in SSL/TLS Implementations. In
Proceedings of the Joint Meeting on
Foundations of Software Engineering
, pages 793–804, 2015.
[39] Y. Chen and Z. Su. Guided Differential Testing of Certicate Validation
in SSL/TLS Implementations. In
Proceedings of the Joint Meeting on
Foundations of Software Engineering
, pages 793–804, 2015.
[40] J. Clark and P. C. van Oorschot. SoK: SSL and HTTPS: Revisiting
Past Challenges and Evaluating Certicate Trust Model Enhancements.
In
Proceedings of the IEEE Symposium on Security and Privacy
, pages
511–525, 2013.
[41] J. De Ruiter and E. Poll. Protocol State Fuzzing of TLS Implementa-
tions. In
Proceedings of the USENIX Conference on Security Symposium
,
pages 193–206, 2015.
[42] Docjar. HostnameChecker. http://www
:
docjar
:
com/docs/api/sun/
security/util/HostnameChecker
:
html.
[43] T. Duong and J. Rizzo. Here Come The

Ninjas. 2011.
[44] T. Duong and J. Rizzo. The CRIME Attack. 2012.
[45] S. Fahl, M. Harbach, T. Muders, L. Baumg
¨
artner, B. Freisleben, and
M. Smith. Why Eve and Mallory Love Android: An Analysis of Android
SSL (in)Security. In
Proceedings of the ACM SIGSAC Conference on
Computer and Communications Security
, pages 50–61, 2012.
[46] N. J. A. Fardan and K. G. Paterson. Lucky thirteen: Breaking the tls
and dtls record protocols. In
Proceedings of the IEEE Symposium on
Security and Privacy
, pages 526–540, 2013.
[47] P. Fiter

au-Bros¸tean, R. Janssen, and F. Vaandrager. Learning Fragments
of the TCP Network Protocol. In
Proceedings of the International
Conference on Formal Methods for Industrial Critical Systems
, pages
78–93, 2014.
[48] P. Fiter

au-Bros¸tean, R. Janssen, and F. Vaandrager. Combining Model
Learning and Model Checking to Analyze TCP Implementations. In
Proceedings of the International Conference on Computer Aided Veri-
cation
, pages 454–471, 2016.
[49] S. Fujiwara, G. v. Bochmann, F. Khendek, M. Amalou, and
A. Ghedamsi. Test Selection Based on Finite State Models.
IEEE
Transactions on software engineering
, 17(6):591–603, 1991.
[50] M. Georgiev, S. Iyengar, S. Jana, R. Anubhai, D. Boneh, and
V. Shmatikov. The Most Dangerous Code in the World: Validating
SSL Certicates in Non-browser Software. In
Proceedings of the ACM
SIGSAC Conference on Computer and Communications Security
, pages
38–49, 2012.
[51] GNU Compilers. Gcov - Using the GNU Compiler Collection (GCC).
https://gcc
:
gnu
:
org/onlinedocs/gcc-4
:
8
:
1/gcc/Gcov
:
html.
[52] B. He, V. Rastogi, Y. Cao, Y. Chen, V. Venkatakrishnan, R. Yang, and
Z. Zhang. Vetting SSL usage in applications with SSLint. In
Proceedings
of the IEEE Symposium on Security and Privacy
, pages 519–534, 2015.
[53] D. Kaminsky, M. L. Patterson, and L. Sassaman. PKI Layer Cake:
New Collision Attacks Against the Global x.509 Infrastructure. In
Proceedings of the International Conference on Financial Cryptography
and Data Security
, pages 289–303, 2010.
[54] M. J. Kearns and U. V. Vazirani.
An Introduction to Computational
Learning Theory
. MIT Press, 1994.
[55] D. Kozen. Lower Bounds for Natural Proof Systems. In
Proceedings
of the Annual Symposium on Foundations of Computer Science
, pages
254–266, 1977.
[56] A. Langley. Apple's SSL/TLS Bug. https://goo.gl/DzRLNq, 2014.
[57] A. Lenstra, J. P. Hughes, M. Augier, J. W. Bos, T. Kleinjung, and
C. Wachter. Ron was wrong, Whit is right.
International Association
for Cryptologic Research
, 2012.
[58] Oracle. Java Cryptography Architecture Oracle Providers Documen-
tation. https://docs
:
oracle
:
com/javase/7/docs/technotes/guides/security/
SunProviders
:
html.
[59] H. Raffelt, B. Steffen, and T. Berg. LearnLib: A Library for Automata
Learning and Experimentation. In
Proceedings of the International
Workshop on Formal Methods for Industrial Critical Systems
, pages
62–71, 2005.
[60] M. Sipser.
Introduction to the Theory of Computation
. Thomson Course
Technology Boston, 2006.
[61] J. Somorovsky. Systematic Fuzzing and Testing of TLS Libraries.
In
Proceedings of the ACM SIGSAC Conference on Computer and
Communications Security
, pages 1492–1504, 2016.

--- page 28 ---

X. A
PPENDIX
A. Details of test hostname verication implementations
OpenSSL.
has separate checking functions for each type
identiers as shown in Table I. In our testing, we use the
default setup that supports matching wildcards. OpenSSL
also provides support for applications to turn some of these
hostname verication functions on or off by calling different
setup functions (e.g.,
X509_VERIFY_PARAM_set1_host
and
X509_VERIFY_PARAM_set1_email
).
GnuTLS.
The GnuTLS check hostname function is de-
signed for certicate verication for HTTPS supporting do-
main names, IPv4, and IPv6. Like OpenSSL, GnuTLS also
provides the application to select whether to verify hostname
with wildcard or not. By default, GnuTLS wildcard matching
is enabled. We use the default setting for our experiments.
MbedTLS.
The hostname verication functions in
MbedTLS only supports checking for domain name
verication.
MatrixSSL.
A single function
matrixValidateCerts
is responsible for checking all different types of identiers
(e.g., DNS, IPv4, and email). The library does not include
support for IPv6 yet. MatrixSSL also provides a separate
function,
psX509ValidateGeneralName
that should be
used before calling matrixValidateCerts for name checking for
ltering out invalid input.
JSSE (Java Secure Socket Extension).
SunJSSE [58],
as part of the JSSE release, has internal built-in hostname
checking support (sun.security.util.HostnameChecker [42]). It
supports domain name, IPv4, and IPv6 verication through the
HostnameChecker.match interface.
CPython SSL.
CPython is the oldest and one of the
most popular Python VM implementation. CPython's inbuilt
SSL support depends on the OpenSSL library, but does
not use OpenSSL's hostname verication function. Instead,
it includes its own hostname verication implementation,
match_hostname
function. Currently, it only supports do-
main name and IP address verication but does not support
email verication.
HttpClient.
(Apache HttpClient) is used extensively
in Web-services middleware such as Apache Axis 2
It supports IPv4, IPv6, and domain name verica-
tion [32]. By default the library provides a verify func-
tion in
DefaultHostnameVerifier
to perform the
identity verication. The verier can also be used with
PublicSuffixMatcher
object to perform additional
checks.
cURL.
By default, it uses OpenSSL [7] but implements
its own hostname verication function
verifyhost
that
supports domain name, IPv4, and IPv6 verication.
B. Developer Responses
We notied the developers of each affected
library/application for all of our ndings, including RFC
violations and discrepancies. In this section, we present
an overview of the developer responses for each different
library/application.
GnuTLS.
The GnuTLS team is currently working on a
patch to x the issue of seeking a match in the CN when
an IP address identier is in the subjectAltName [1]. The
developers also plan to provide a way to specify the identier
type in order to avoid the confusion between hostnames and
IP addresses [2]. Additionally, the team plans to remove a
fallback option which matches an IP address with a subjectAlt-
Name DNS [9], thus resolving the potential attack presented
in Section VI-C [3]. Finally, GnuTLS has recently introduced
IDNA2008 support in version 3.5.9 and performs extensive
checks to verify the format of the DNS names stored in the
certicate.
MbedTLS.
We are currently discussing the discovered
issues with the MbedTLS team.
MatrixSSL.
MatrixSSL is prioritizing the xes for the RFC
violations, including the incorrect order of checking between
subject CN and subjectAltName identier (violation of RFC
6125) and matching the local-part of an email address in a
case-insensitive manner (violation of RFC 5280). These xes
are deployed in their new version 3.9.0 [4]. This version also
addresses other discrepancies we reported by providing an
optional ag for hostname input validation, and providing
parameters for users in order to specify the type of the
identier (e.g., DNS, IP ADDR) in order to address the attack
discussed in Section VI-C.
JSSE.
The JSSE team does not consider RFC 6125 com-
pliance to be a feature of the current version of the library.
However, the team informed us that they are currently working
on plans to add compliance with RFC 6125 in the next versions
of the library.
CPython SSL.
CPython plans to deprecate their hostname
verication implementation and directly use OpenSSL's im-
plementation in the next release.
OpenSSL.
The OpenSSL team decides not to address the
issue of matching a partial hostname sufx of a subject
CN/subjectAltName, as this discrepancy is not an RFC viola-
tion. For the other discrepancies e.g., matching a wildcard in
a public sufx or matching an invalid hostname, the OpenSSL
team believes that they should be handled at the application
level or by certicate authorities and therefore, they should
not be xed in the library itself.
HttpClient.
The HttpClient team has addressed the viola-
tions of matching a subject CN in case sensitive manner (viola-
tion of RFC 6125 and RFC 5280) and attempting to match sub-
ject CN when a subjectAltName is present (violation of RFC
6125). These issues are resolved in version 4.5.3, which is cur-
rently an alpha release [5]. The HttpClient team decided not to
address the other reported issues as they are handled correctly
if the application calls the
DefaultHostnameVerifier
with the
PublicSuffixMatcher
in the verier construc-
tor.
C. Detailed list of discrepancies
In Table VIII, we present a detailed list of the discrepancies
discovered between various SSL/TLS libraries and applica-
tions.

--- page 29 ---

TABLE VIII
S
AMPLE STRINGS ACCEPTED BY THE AUTOMATA INFERRED FROM DIFFERENT HOSTNAME VERIFICATION IMPLEMENTATIONSTest Certicate Identier Template OpenSSL GnuTLS MbedTLS MatrixSSL JSSE CPython SSL HttpClient cURLWildcard in Certicate*.aaa.aaa
a.aaa.aaa
.aaa.aaa
*.aaa.aaa
.aaa
a.aaa.aaa
n
0
.aaa.aaa
n
0
.aaa
n
0
*.aaa.aaa
n
0
.aaa.aaa
.aaa.aaa
n
0
a.aaa.aaa
a.aaa.aaa
n
0
a.aaa.aaa
a.aaa.aaa
n
0
a.aaa.aaa a.aaa.aaa .aaa.aaa
a.aaa.aaa
a.aaa.aaa.
n
0
a.aaa.aaa
n
0
a.aaa.aaa.aaa.*.aaa
aaa.*.aaa
.aaa
.*.aaa
aaa.*.aaa
n
0
.aaa
n
0
.*.aaa
n
0
aaa.*.aaa
aaa.*.aaa
n
0
aaa.*.aaa
aaa.*.aaa
n
0
none aaa.a.aaa aaa.*.aaa aaa..aaa
aaa.*.aaa
aaa.*.aaa.
n
0
aaa.*.aaa
n
0
aaa.*.aaa.a*.aaa.aaa
aa.aaa.aaa
a.aaa.aaa
a*.aaa.aaa
.aaa.aaa
.aaa
aa.aaa.aaa
n
0
a.aaa.aaa
n
0
a*.aaa.aaa
n
0
.aaa.aaa
n
0
.aaa
n
0
a*.aaa.aaa
a*.aaa.aaa
n
0
a*.aaa.aaa
a*.aaa.aaa
n
0
none a.aaa.aaa a.aaa.aaa a.aaa.aaa
aa.aaa.aaa
aa.aaa.aaa.
n
0
aa.aaa.aaa
n
0
aa.aaa.aaa.aaa.a*.aaa
aaa.a*.aaa
.aaa
.a*.aaa
aaa.a*.aaa
n
0
.aaa
n
0
.a*.aaa
n
0
aaa.a*.aaa
aaa.a*.aaa
n
0
aaa.a*.aaa
aaa.a*.aaa
n
0
none aaa.a.aaa aaa.a*.aaa aaa.a.aaa
aaa.a*.aaa
aaa.a*.aaa.
n
0
aaa.a*.aaa
n
0
aaa.a*.aaa.xn
--
aaa*.aaa
.aaa
.aaa
n
0
xn
--
aaa*.aaa
xn
--
aaa*.aaa
n
0
xn
--
aaa*.aaa
xn
--
aaa*.aaa
n
0
none xn
--
aaa.aaa xn
--
aaa*.aaa xn
--
aaa.aaa
xn
--
aaa*.aaa
xn
--
aaa*.aaa.
n
0
xn
--
aaa*.aaa
n
0
xn
--
aaa*.aaa.*.xn
--
aaa.aaa
a.xn
--
aaa.aaa
.aaa
.xn
--
aaa.aaa
*.xn
--
aaa.aaa
a.xn
--
aaa.aaa
n
0
.aaa
n
0
.xn
--
aaa.aaa
n
0
*.xn
--
aaa.aaa
n
0
.xn
--
aaa.aaa
.xn
--
aaa.aaa
n
0
.xn
--
aaa.aaa
.xn
--
aaa.aaa
n
0
none a.xn
--
aaa.aaa a.xn
--
aaa.aaa .xn
--
aaa.aaa
a.xn
--
aaa.aaa
a.xn
--
aaa.aaa.
n
0
a.xn
--
aaa.aaa
n
0
a.xn
--
aaa.aaa.xn
--
aaa.*.aaa
.aaa
.*.aaa
xn
--
aaa.*.aaa
.aaa
n
0
.*.aaa
n
0
xn
--
aaa.*.aaa
n
0
xn
--
aaa.*.aaa
xn
--
aaa.*.aaa
n
0
xn
--
aaa.*.aaa
xn
--
aaa.*.aaa
n
0
none xn
--
aaa.a.aaa xn
--
aaa.*.aaa xn
--
aaa..aaa
xn
--
aaa.*.aaa
xn
--
aaa.*.aaa.
n
0
xn
--
aaa.*.aaa
n
0
xn
--
aaa.*.aaa.Wildcard Unclear Practices*.aaa
.aaa
*.aaa
.aaa
n
0
*.aaa
n
0
none
a.aaa
a.aaa
n
0
a.aaa
a.aaa
n
0
a.aaa a.aaa .aaa
*.aaa
*.aaa.
n
0
*.aaa
n
0
*.aaa.a*b*c*.aaa.aaa
a*b*c*.aaa.aaa
.aaa.aaa
.aaa
a*b*c*.aaa.aaa
n
0
.aaa.aaa
n
0
.aaa
n
0
a*b*c*.aaa.aaa
a*b*c*.aaa.aaa
n
0
a*b*c*.aaa.aaa
a*b*c*.aaa.aaa
n
0
none abc.aaa.aaa none ab*c*.aaa.aaa
aab*c*.aaa.aaa
aab*c*.aaa.aaa.
n
0
aab*c*.aaa.aaa
n
0
aab*c*.aaa.aaa.*.*.aaa.aaa
.aaa.aaa
.*.aaa.aaa
*.*.aaa.aaa
.aaa
.aaa.aaa
n
0
.aaa
n
0
.*.aaa.aaa
n
0
*.*.aaa.aaa
n
0
.*.aaa.aaa
.*.aaa.aaa
n
0
a.*.aaa.aaa
a.*.aaa.aaa
n
0
none a.a.aaa.aaa a.*.aaa.aaa .*.aaa.aaa
a.*.aaa.aaa
a.*.aaa.aaa.
n
0
a.*.aaa.aaa
n
0
a.*.aaa.aaa.*b.aaa.aaa
ab.aaa.aaa
b.aaa.aaa
.aaa.aaa
*b.aaa.aaa
.aaa
ab.aaa.aaa
n
0
b.aaa.aaa
n
0
.aaa.aaa
n
0
.aaa
n
0
*b.aaa.aaa
n
0
b.aaa.aaa
b.aaa.aaa
n
0
*b.aaa.aaa
*b.aaa.aaa
n
0
none
ab.aaa.aaa
b.aaa.aaa
b.aaa.aaa b.aaa.aaa
ab.aaa.aaa
ab.aaa.aaa.
n
0
ab.aaa.aaa
n
0
ab.aaa.aaa..aaa.aaa
.aaa.aaa
.aaa
.aaa.aaa
n
0
.aaa
n
0
none
.aaa.aaa
.aaa.aaa
n
0
none aaa.aaa .aaa.aaa .aaa.aaa
.aaa.aaa
.aaa.aaa.
n
0
.aaa.aaa
n
0
.aaa.aaa.Email AddressSAN email: *@aaa.aaa
*@aaa.aaa
*@aaa.aaa
n
0
*@aaa.aaa
*@aaa.aaa
n
0
– none – – – –SAN email: aaa@*
aaa@*
aaa@*
n
0
aaa@*
aaa@*
n
0
– none – – – –SAN email: aaa@*.aaa
aaa@*.aaa
aaa@*.aaa
n
0
aaa@*.aaa
aaa@*.aaa
n
0
– none – – – –SAN email: aaa@aaa.*
aaa@aaa.*
aaa@aaa.*
n
0
aaa@aaa.*
aaa@aaa.*
n
0
– none – – – –SAN email: AAA@aaa.aaa
AAA@aaa.aaa
AAA@aaa.aaa
n
0
AAA@aaa.aaa
AAA@aaa.aaa
n
0
–
aaa@aaa.aaa
aaa@aaa.aaa
n
0
– – – –SAN email: aaa@AAA.aaa
aaa@aaa.aaa
aaa@aaa.aaa
n
0
aaa@aaa.aaa
aaa@aaa.aaa
n
0
–
aaa@aaa.aaa
aaa@aaa.aaa
n
0
– – – –IP AddressSAN IP Addr: *.111.111.111 none none – none none none none none

--- page 30 ---

Ý“í5ÌÈ&à©ZÒ³!/¯›Þâh¸Yh³"¾

--- page 31 ---

YI-�Œl`®õî;`ÕçæAÐH:´® áYHb1“µâ»HÇ{¸wƒÇR^YÑš,
 $F¨Ô–HDÙòV?pòyÑ—¹PÞ%F=»‚ÂÇÆB‡öÙö¡GKØPh³~N´[¸IÊ_êˆ€CðTzÞÒf	ç	<Ó–”Œü�`4|mƒE1ÖJ'¼ýáÝ$`}R	‚Ú¨€âN2kf¢aóouJ73�ê´òváê¿ôKÛW{œMÓÞ3?×��©Mò]ù:W;v�…˜Xâ;„B’	‰§X�.PáI;?Ÿ!T¤ˆ .·sìöU]ä®ƒ’=ÑXŠþý’5´ÀŠ€r€Mt>y=¯†*ã�bC¾~^½tÅAr±¡l'¶øÅ¦•üóô÷ØŸÉL�ëƒ¡P“&7ttöuGz;Kg4ÚóÑ�;·u
