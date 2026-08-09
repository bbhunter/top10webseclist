---
type: Whitepaper
title: Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction
resource: "https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T10:26:21+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
    title: Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction
  - id: capture
    resource: "https://web.archive.org/web/20240415082249/https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2024.md:80"
commit: ""
content_sha256: 19f95cdab02ce4845ef5acd0ea89041b61bb6651d254d624f074f3e4469db434
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: c25310fe00c6ab261795383a802903771c1f86dd3127bf5437f776f985ac1812
retrieved_from: "https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-09T10:26:21+00:00"
slug: efficient-detection-java-deserialization-gadget-chains-bottom-up-construction
snapshot: 20240415082249
title_english: ""
translation_file: ""
translation_of: ""
---

# Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction

**Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction** - Author not stated, Publisher not stated.

- Published: date not stated
- Original: <https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf>
- Preserved from: https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf (stored) on 2026-08-09
- Capture timestamp: 20240415082249
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction

--- page 1 ---

Efcient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget
Search and Dataow-aided Payload Construction
Bofei Chen
1
, Lei Zhang
1
‡
, Xinyou Huang
1
, Yinzhi Cao
2
, Keke Lian
1
‡
, Yuan Zhang
1
‡
, Min Yang
1
‡
1: Fudan University,
f
bfchen22, xinyouhuang22
g
@m.fudan.edu.cn
1
‡
: Fudan University,
f
zxl, kklian20, yuanxzhang, myang
g
@fudan.edu.cn
2: Johns Hopkins University, yinzhi.cao@jhu.edu
Abstract
—Java Object Injection (JOI) is a severe type of
vulnerability affecting Java deserialization, which allows adver-
saries to inject a well-crafted, serialized object, thus triggering
a series of chained internal methods (called gadgets) and then
achieving attack consequences such as Remote Code Execution
(RCE). Prior works studied the problem of detecting and
chaining gadgets for JOI vulnerability using static search for
possible gadget chains and dynamic construction of payload via
fuzzing. However, prior works face two following challenges:
(i) path explosion in static gadget search and (ii) a lack of ne-
grained object relations connected via object elds in dynamic
payload construction.
In this paper, we design and implement a novel Java
deserialization gadget detection framework, called
JDD
. On
one hand,
JDD
solves the static path explosion problem by a
bottom-up approach, which rst looks for gadget fragments
and then chains gadget fragments from sinks to sources. The
approach reduces maximum static search time from exponen-
tial to polynomial, i.e., from
O
ˆ
eM
n
�
to
O
ˆ
M
2
n
3

enM
�
,
where
n
is the number of dynamic function calls in a gadget
chain,
M
is the average number of dynamic function call
candidates, and
e
is the number of entry points. On the other
hand,
JDD
constructs a so-called Injection Object Construction
Diagram (IOCD), which models the dataow dependencies
between injection objects' elds to facilitate dynamic fuzzing.
Our evaluation of
JDD
upon six real-world Java applica-
tions reveals 127 zero-day, exploitable gadget chains with
six Common Vulnerabilities and Exposures (CVE) identiers
assigned. We also responsibly reported these vulnerabilities to
application developers and obtained their acknowledgments
and conrmations.
1. Introduction
Java serialization and deserialization greatly facilitate
the cooperation and collaboration of different Java systems
(e.g., server and client), allowing different Java programs
to conveniently exchange and share data and code. Despite
their easiness and powerfulness, one well-known and serious
security vulnerability faced in Java deserialization is an
implicit attack surface called Java Object Injection (JOI).
The JOI vulnerability enables a remote attacker to inject
a well-crafted serialized object, which triggers a chain of
internal Java methods (called gadgets), nally achieving a
wide range of severe attack consequences, e.g., remote code
execution (RCE) and denial of service (DoS) attacks.
In past years, many works [1]–[4] have focused on the
problem of JOI, and proposed several JOI vulnerability
detection techniques. For example, ODDFuzz [2] statically
searches for possible gadgets via a Depth First Search (DFS)
strategy, and then dynamically fuzzes the target program as
a greybox for verifying gadget chains. However, existing
work still fell short in two major limitations, impacting their
practicality and effectiveness.
First, prior work often adopted a top-down static ap-
proach for checking gadgets extensively from a source to a
sink for potential paths. However, such a search often suffers
from path explosion, especially when common Java meth-
ods such as
equals
and
put
are involved in the gadget
chain. For example, our experiment shows that the static
analysis approach like ODDFuzz cannot nish analyzing a
small 3.6MB Java application. Fundamentally, the search
complexity is exponential, i.e.,
O
ˆ
eM
n
�
, where
n
is the
number of dynamic function calls in a gadget chain,
M
is
the average number of dynamic function call candidates, and
e
is the number of entry points.
Second, many of prior tools conducted static analysis
against JOI vulnerability detection, thus inevitably having
high false positives. Beyond these, ODDFuzz additionally
introduced dynamic fuzzing for reducing false positives.
However, ODDFuzz did not consider the constraints that
should be satised in each gadget. In particular, the ne-
grained data ows between different object elds in each
gadget, leading to the imprecision of object structure and
thus an incorrect payload.
In this paper, we design a novel gadget chain detection
framework, called
JDD
(JavaDeserialization VulnerabilityDetector), to statically detect possible gadget chains using a
bottom-up approach and dynamically generate payloads, i.e.,
exploitable injection objects, relying on dataow relations
between object elds.
JDD
addresses the aforementioned
two challenges as follows.
First,
JDD
addresses the path explosion challenge via a
bottom-up search strategy.
JDD
rst searches for possible
gadget fragments and then chains fragments together from
sinks to sources. Our key observation here is that a top-down
search repeats the analysis of the same low-level gadget

--- page 2 ---

YI-�Œl`®õî;`ÕçæAÐH:´® áYHb1“µâ»HÇ{¸wƒÇR^YÑš,
 $F¨Ô–HDÙòV?pòyÑ—¹PÞ%F=»‚ÂÇÆB‡öÙö¡GKØPh³~N´[¸IÊ_êˆ€CðTzÞÒf	ç	<Ó–”Œü�`4|mƒE1ÖJ'¼ýáÝ$`}R	‚Ú¨€âN2kf¢aóouJ73�ê´òváê¿ôKÛW{œMÓÞ3?×��©Mò]ù:W;v�…˜Xâ;„B’	‰§X�.PáI;?Ÿ!T¤ˆ .·sìöU]ä®ƒ’=ÑXŠþý’5´ÀŠ€r€Mt>y=¯†*ã�bC¾~^½tÅAr±¡l'¶øÅ¦•üóô÷ØŸÉL�ëƒ¡P“&7ttöuGz;Kg4ÚóÑ�;·u

--- page 3 ---

Æ¤Â%¥Ó•2V´–Á!ö|’�Ýçí¤EÎä�sûûm±â

--- page 4 ---

‰ÔwÂ9QÀ�‘æ«†�4’'­4à_°#¦äJì‘»�m“ãŒä¸˜${ýª¯S·:Úqâvö^²—ƒTÓÖA«U¶|oì0eÇÊ´ò×©˜Õ_GmæþVDyïÒÁù#«œÈÏÙ´÷ÆÙRÀéøÛ?˜l–úü‡ UQŒã‰

--- page 5 ---

fragment when a top-level gadget changes, leading to a
huge redundancy and a waste of analysis time. Instead, the
bottom-up search adopted by
JDD
nds gadget fragments
that can be reused by different top-level gadgets in the chain.
Therefore, the search complexity changes from exponential
to polynomial, i.e., from
O
ˆ
eM
n
�
to
O
ˆ
M
2
n
3

enM
�
.
More importantly,
JDD
is able to reuse existing gadget frag-
ments discovered in previous vulnerabilities, which further
speeds up the search process.
Second,
JDD
addresses the challenge of the lack of ob-
ject eld relations via a novel data structure, called Injection
Object Construction Diagram (IOCD), to better represent
the dataow dependencies between injection objects' elds.
The high-level idea is that
JDD
follows the call sequence
in a statically-discovered gadget chain to construct dataow
dependencies between possible injection objects' elds as an
IOCD. Such an IOCD is further used by
JDD
in dynamic
fuzzing to exploit the JOI vulnerability.
We evaluate
JDD
upon six popular Java applications in
their latest version, which nds 127 zero-day exploitable
gadget chains with six Common Vulnerabilities and Expo-
sures (CVE) identiers assigned. We also responsibly re-
ported our ndings of all 127 gadget chains to related devel-
opers and received their conrmation. For example, Dubbo's
developers not only acknowledged the gadget chains but also
admitted that it is almost “impossible” for them to recognize
all possible gadget chains, which emphasizes the urgency of
our automated tool.
We also compare
JDD
with the state-of-the-art approach,
namely ODDFuzz, in a well-known benchmark (i.e., the
ysoserial repository [5]) with 34 conrmed gadget chains.
JDD
missed only seven of 34 conrmed with a False Neg-
ative Rate (FNR) of 20.6% and identied 91 previously-
unknown gadget chains (which were conrmed as correct in
manual analysis). As a comparison, OddFuzz only detected
16 gadget chains, resulting in an FNR of 52.9%, and it did
not discover any previously-unknown ones.
We summarize the contributions of this paper as below:
Y
JDD
solves the path explosion problem of static search
for chained gadgets via a bottom-up approach that dis-
covers intermediate gadget fragments and then chains
them together from sinks to sources.
Y
JDD
constructs the so-called Injection Object Con-
struction Diagram (IOCD) to better model dataow
dependencies between object elds and assist dynamic
fuzzers for payload construction.
Y
JDD
discovered 127 zero-day gadget chains of real-
world Java applications in their latest version and out-
performs ODDFuzz in detecting legacy gadget chains.
2. Overview
In this section, we rst provide a brief background on
JOI attacks in Section 2.1, then describe Java deserialization
gadget chains in Section 2.2 using a real-world motivat-
ing example, and then present research challenges faced
by state-of-the-art approaches in detecting this example in
Section 2.3.
2.1. Background of JOI Attacks
Java Naming and Directory Interface (JNDI) injection
is a commonly used technique in JOI attacks. The attack
occurs because the JNDI interface's
lookup
method can
remotely load a malicious Java class based on its param-
eters (e.g., an attacker-controlled URL), thereby executing
arbitrary code in the victim server. A typical scenario for this
attack involves a web service running on the victim server,
listening on a port and deserializing data received on the
port. During deserialization, if there is a JOI vulnerability,
the program execution will invoke some security-sensitive
methods based on the injected object.
In addition to JNDI injection attacks, common meth-
ods of exploiting JOI vulnerabilities to attack remote
servers include dynamic code loading (such as using
URLClassLoader.loadClass
to load remote class
les or using
ClassLoader.defineClass
to directly
load bytecode les), and command execution (such as
Runtime.exec
), etc. They all require: (1) An execution
path that can invoke a security-sensitive method that can
execute malicious code (or upload arbitrary les, deny ser-
vice, etc.) during the deserialization process, called
gadget
chain
; (2) A serialized object that drives the execution of
the gadget chain, called
injection object
.
Thus, to detect JOI vulnerabilities,
JDD
has two major
detection goals: (1) Uses static analysis to nd potential
gadget chains in the victim server; (2) Dynamically gener-
ates exploitable injection objects to verify the exploitability
of gadget chains. As a result, the exploitable gadget chains
detected by
JDD
can be used to help developers specify a
more complete blacklist defense mechanism to better defend
against JOI attacks.
2.2. A Motivating Example
Figure 1 illustrates a zero-day gadget chain found by
JDD
in
sofa-rpc
[6], i.e., popular Java libraries that
are widely used in the server-side cloud of many enter-
prise companies, e.g., Alipay. The gadget chain starts from
a Java deserialization method (e.g.,
HashMap.put()
in
Line 4, shown in Figure 1). The chain ends up with a
Java reection call at Line 54 and then launches a JNDI
injection attack at Line 59. Note that each Java method
call along the chain is considered as a
gadget
, e.g., the
put()
method at Line 4. Then, Java method calls between
two dynamically-dispatched methods are considered as a
gadget fragment
, e.g., the combination of methods
get()
and
getFromHashtable()
in Figure 1 as Fragment IV,
as the latter is statically determined. We also illustrate the
exploit code in Figure 2. An adversary serializes the returned
object in Line 22 of Figure 2 and sends it to the server, which
triggers the gadget chain in Figure 1 for exploitation.
We rst describe the gadget chain with ve different
gadget fragments of Figure 1 in detail. The gadget starts
from Fragment I (Line 1), where the
put()
method (Line
4) of an object
HashMap
is invoked upon deserialization.
If two elements in the
HashMap
have the same hash value,

--- page 6 ---

1 /* Gadget Fragment I : HashMap.put()->HashMap.putVal() */ 2class HashMap extends AbstractMap ...{ 3 Node<K,V>[] table; 4 V put(K key, V value) { return putVal(hash(key), key, value, ...); } 5 V putVal(int hash, K key, V value,...) { ... 6 Node<K,V> p = table[(int) index]; // p is an element in table 7 if (p.hashCode() == key.hashCode() & p.key != key & key != null) 8key.equals(p.key); 9 ... }10}11 /* Gadget Fragment II: NodeImpl.equals()-> Object.equals(Line 17) */12class NodeImpl implements ... {13 Object key;14 int hashCode = -1;15 boolean equals(Object obj) {16 if (o instanceof NodeImpl) { ... 17this.key.equals( ((NodeImpl) obj).key );18 }19 int hashCode() { 20if (this.hashCode == -1) this.hashCode = this.buildHashCode();21return this.hashCode; 22} 23 /* Gadget Fragment III: ConcurrentHashMap.equals()-> Map.get() */24class ConcurrentHashMap<K,V> extends AbstractMap<K,V> ...{25 boolean equals(Object o) {26 if (o instanceof Map) { ... 27 ((Map<?,?>)o).get(ConcurrentHashMap.this.table[index].key);28 ...}}29 30}31 /* Gadget Fragment IV: UIDefaults.get()-> ... -> LazyValue.createValue() */32class UIDefaults extends Hashtable<Object,Object>{33 Object get(Object key) { Object value = getFromHashtable( key ); ...}34 Object getFromHashtable(final Object key) {35 // UIDefaults.table should contain an Entry that key is key36 Object value = super.get(key); 37 if ((value != PENDING) && !(value instanceof ActiveValue) &&38 !(value instanceof LazyValue)) return value;39 if (value instanceof LazyValue) ((LazyValue) value).createValue(this);40 }41}42class Hashtable<K,V> ... {43 Entry<K,V>[] table;44 V get(Object key) {45 Entry<K,V> e = this.table[(int) index]; // e is an element of table46 if ((e.key.hash == key.hash) && e.key.equals(key)) return (V) e.value;47 return null; }48}49 /* Gadget Fragment V: ProxyLazyValue.createValue()->...-> Method.invoke() */50class ProxyLazyValue extends Hashtable<Object,Object> {51 Object createValue(final UIDefaults table) {...52 Class c = Class.forName(this.className);53 Method m = c.getMethod(this.methodName, this,args);54 return MethodUtil.invoke(m, c, this.args); ...}55}56 /* Gadget Fragment VI: InitialContext.doLookup()-> InitialContext.lookup() */57class InitialContext implements Context {58 static <T> T doLookup(String name) throws NamingException {59 return (T) (new InitialContext()).lookup(name); // JNDI attack }60}Candidates:2751Candidates:12Candidates:2751Candidates:148n1n2cctmapuftuftcctmap.table[i].keycctmap.table[i].keycctmap.table[i].keyplvuftplvplv.argsplv.argscctmap.table[i].key

--- page 7 ---

1 // Gadget Fragment IV 2UIDefaults uft = new UIDefaults(); 3 // Gadget Fragment V 4Object plv = createWithObjectNoArgsConstructor( 5Class.forName(javax.swing.UIDefaults$ProxyLazyValue)); 6uft.put(aaa, plv) 7 // Gadget Fragment VI 8setFieldValue(plv, className, security-sensitive class name); 9setFieldValue(plv, args, new Object[]{malicious URL}); 10setFieldValue(plv, methodName, security-sensitive method name);11 // Gadget Fragment III12ConcurrentHashMap cctmap = new ConcurrentHashMap();13cctmap.put(aaa, any);14// Gadget Fragment II15NodeImpl n1 = createWithObjectNoArgsConstructor(NodeImpl.class);16NodeImpl n2 = createWithObjectNoArgsConstructor(NodeImpl.class);17 setFieldValue(n1, hashCode, 3);18 setFieldValue(n2, hashCode, 3);19setFieldValue(n1, key, cctmap);20setFieldValue(n2, key, uft);21// Gadget Fragment I22HashMap map = Gadgets.makeMap(n2, n1); // put n1 and n2 into a HashMap

--- page 8 ---

Figure 1: A Motivating Example of a Zero-day Gadget
Chain with Five Fragments (Note that code is simplied
for easy understanding.)
the
equals()
method (Line 8) will be invoked, which may
have a polymorphic implementation in
NodeImpl
class,
thus triggering Fragment II (Line 10). Then, the eld
key
of the
NodeImpl
class triggers another
equals()
method
(Line 17), which may have a polymorphic implementation in
the
ConcurrentHashMap
class, thus triggering Fragment
III (Line 25). Next, the
get()
method has a polymorphic
implementation in the
UIDefaults
class, leading to Frag-
Figure 2: Exploit Code of Our Motivating Example in
Figure 1 (An adversary serializes the returned object in Line
20 and sends it to the server).
ment IV, which further calls the
getFromHashtable()
method (Line 34). Lastly, the
createValue()
method
calls at Line 39 invokes the polymorphic method denition
in Line 51 belong to Fragment V, which calls Java reection
at Line 54 and thus the JNDI attack at Line 59 of Fragment
VI.
Next, we describe how an adversary utilizes the gadget
chain with the exploit code in Figure 2. An adversary rst in-
stantiates a
HashMap
object at Line 22 of Figure 2 to trigger
the
put()
method of Fragment I. Then, two
NodeImpl
objects are instantiated with the same
hashCode
(Lines
15–18 of Figure 2) so that the
equals()
method in
Fragment II is invoked. Next, the adversary assigns
n1.key
as a
ConcurrentHashMap
object (Lines 12–13 and 19
of Figure 2) to trigger another
equals()
method in
Fragment III. After that, the adversary assigns
n2.key
as a
UIDefaults
object (Lines 2 and 20 of Figure 2)
to trigger the
get()
method in Fragment IV. Lastly, the
adversary manipulates the elements stored in
uft.table
to return a
ProxyLazyValue
object (Line 6 of Fig-
ure 2), which implements
LazyValue
interface with three
values to trigger Fragment V. Specially, the adversary
assigns the method
InitialContext.doLookup()
as
the
className
and the
methodName
together with the
correct
args
(Lines 8–10 of Figure 2) to trigger Fragment
VI.
2.3. Challenges and Solution Overview
We now describe two challenges faced by prior works
in their static and dynamic analysis using the motivating
example presented in Figure 1. Then, we present the solu-
tions proposed by us in designing
JDD
to solve these two
challenges.

--- page 9 ---

HashMaptableNodeImplNodeImplkeykeyUIDfaultsConcurrentHashMaptabletableProxyLazyValue(a) Correct Injection ObjectStructureNodeImplkeyConcurrentHashMaptableUIDfaultstableProxyLazyValue(b) Erroneous Injection ObjectStructure Deduced by OddfuzzHashMaptable......Field NodeClass-FieldDependenceClass Noden2n1uftcctmapplv i. n1.hashCode() == n2.hashCode() ii. uft.containsKey(cctmap.table[i].key) == trueiii. Class.forName(plv.className) .getMethod(plv.methodName,plv.args) != nulliv. ...Constraints Info i. n1.hashCode() == n2.hashCode() ii. uft.containsKey(cctmap.table[i].key) == trueiii. Class.forName(plv.className) .getMethod(plv.methodName,plv.args) != nulliv. ...Constraints Info

--- page 10 ---

Figure 3: Injection Object Structure of Motivation Example.
Challenge I: Static Path Explosion.
The rst challenge
is that the number of all possible paths between sources
and sinks is exponential, leading to path explosion. Let
us use Figure 1 as an example to describe the challenge.
The number of potential candidates for the
equals()
method between Fragments I and II could be 2,751 and
the same applies to the other
equals()
method between
Fragments II and III. Then, the candidate number is 148
for
get()
between Fragments III and IV, and 12 for
createValue()
between Fragments IV and V. Therefore,
if a Depth-rst-search (DFS) is used to nd a gadget chain
like what ODDFuzz does, the total number execution path
could be 2751

2751

148

12 = 13,440,769,776, which is
impossible to search from.OurSolution:Bottom-upGadgetSearch. Our key obser-
vation is that a top-down search like a DFS will analyze
some methods multiple times, leading to redundancies. For
example, one
get()
method candidate between Fragments
III and IV may be analyzed once for one
equals()
method candidate between Fragments II and III and then
again for another candidate between Fragments II and III.
Instead,
JDD
analyzes all possible gadgets between sources
and sinks once and forms them into gadget fragments. Then,
JDD
adopts a bottom-up search from the sink to the source,
which chains all the fragments into a chain. Specically,
JDD
only needs to analyze (12 + 2751 + 148) = 2,911
program execution paths and at most (2911

2911 - 2751

2751 - 148

148 - 12

12)

2 + 2751 = 1,770,495
times fragment linking check for our motivating example in
Figure 1, which is only 0.01% of the top-down approach,
signicantly reducing the static gadget search space.
Challenge II: Parallel and Embedded Injection Object
Structure.
The second challenge is that the payload, i.e.,
the injection object, may have complex structures, such
as embedded or parallel objects. Figure 3 (a) shows the
injection object structure for our motivating example in
Figure 1.
UIDfaults
and
ConcurrentHashMap
are
two
key
s under
NodeImpl
objects in a correct payload.
However, prior works, such as ODDFuzz, only consider the
class hierarchy inferred from the gadget chain and therefore
they will generate a wrong object structure as shown in
Figure 3 (b) because the
get()
method of
UIDfaults
is invoked after
ConcurrentHashMap
.OurSolution:Dataow-aidedConstructionofInjectionObjectConstructionDiagram(IOCD). Our key obser-
vation is that different injection objects, e.g., their elds,
are connected via dataows. Specically, two dotted lines
in different colors of Figure 1 show such two dataows.
key
(Line 8) ows to
this.key
(Line 17) and then
this.table[index].key
(Line 27); then,
p.key
(Line 8) ows to
((NodeImpl) obj).key
(Line 17)
and then
(Map<?,?>)o
(Line 27). Therefore,
JDD
infers
that there are two
NodeImpl
objects and
UIDfaults
is under the
key
of one
NodeImpl
object instead of
the
table
of
ConcurrentHashMap
. More specically,
JDD
constructs an IOCD like Figure 3 (a) following such
dataows, which can be used for follow-up fuzzing.
3. Design
In this section, we describe the system architecture of
JDD
and then the detailed steps.
3.1. System Architecture
We show an overview of
JDD
's architecture with two
main stages in Figure 4. In Stage I,
JDD
detects possible
gadget chains and then in Stage II,
JDD
generates injection
objects to exploit the detected gadget chains for validation.
Specically, there are ve steps. In Step 1,
JDD
identies
deserialization entry points. Then, in Step 2,
JDD
starts from
entry points to identify gadget fragments with static analysis.
After that,
JDD
links gadget fragments to construct gadget
chains using a bottom-up approach, which nishes Stage 1
with possible gadget chains. Next, in Step 4,
JDD
constructs
Injection Object Construction Diagram (IOCD) based on the
injection object related constraints. Lasty, in Step 5,
JDD
utilizes IOCD-enhanced directional Fuzzing to verify gadget
chains' exploitability.
We now describe how each step works for our mo-
tivating example. Here is Stage I. First, in Step 1,
JDD
starts with identifying the entry points in
sofa-rpc
[6],
and then use them as the sources to begin our static taint
analysis. Second, in Step 2,
JDD
traverses the control- and
data-ow graph of the target program starting from each
source (i.e., entry points in the beginning) until a dynamic
method invocation and considers this as a fragment. Then,
JDD
treats the implementation of the dynamic method as
the new source until the next dynamic method invocation
and considers code in between as a new fragment. During
this process,
JDD
identies some gadget fragments con-
taining a sink, e.g.,
MethodUtil.invoke()
in Gadget

--- page 11 ---

Fragment V. Then, in Step 3,
JDD
uses this fragment to
nd the gadget fragment IV that has a dynamic method
invocation
LazyValue.createValue()
and the object
value
that is used to invoke the
createValue()
method
based on previous taint analysis result. Next,
JDD
uses the
Gadget Fragment IV as the new start to nd the Gadget
Fragment III and repeats this procedure until it reaches a
source point, resulting in a gadget chain. After chaining the
gadget fragments I-V, to complete the gadget chain,
JDD
will independently gather potential fragments that could
execute remote attacker-controlled code, for example, the
gadget fragments VI which contains a JNDI capability. Since
the gadget fragment V has a reection capability and the
parameter is controlled by the attacker,
JDD
would further
connect it to the gadget fragment VI.
We then describe Stage II. In Step 4,
JDD
extracts the
constraints for gadget chain chaining, which include (1)
structured constraints (i.e. the class hierarchy relationships
between object and eld instances), (2) eld dependency
constraints (e.g., the hash code of
n1.key
and
n2.key
should
be the same for our example), and (3) conditional branches.
Note that
JDD
labels constraints shared by different execu-
tion paths as
dominator
, meaning that they are required by
all the execution paths. After extracting these constraints,
JDD
uses a novel data structure, termed Injection Object
Construction Diagram (
IOCD
) to model dataow depen-
dencies between object elds and guide dynamic fuzzing.
Lastly, in Step 5,
JDD
instruments the collected constraints
of the target program and uses the number of covered domi-
nator constraints to guide the fuzzing for generating an injec-
tion object that can exploit this gadget chain. Specically,
JDD
rst initializes an instance object based on the class
hierarchy in the IOCD graph. Then, for assigning adequate
value for each eld in the object,
JDD
utilizes a constraint
solver to solve the dominator constraints. Then,
JDD
uses
this object as the seed to drive the directional fuzzing
and uses the number of covered dominator constraints to
evaluate its energy.
3.2. Step 1: Identifying Deserialization Entry
Points
The rst step of our analysis is to identify the entry
points of deserialization in a given Java program.
JDD
ex-
tract such entry points from both the deserialization methods
of Java language and popular Java deserialization protocols
as shown in Table 1. There are two categories of entry meth-
ods: (i) deserialization methods provided by Java language,
e.g.,
readObjectNoData()
,
readExternal()
and
readObject()
, and (ii) interfaces provided by popular
Java deserialization protocols, e.g.,
Map.put()
for Hes-
sian protocol. Note that since many of these entry points
are dened as interfaces,
JDD
further identies and analyzes
their overridden or implementation methods as the entry
points.
Table 1: Popular Deserialization Protocols Protocol Entry Points
Supported
Dynamic Feature
Unserializable
Class SupportJDK
readObject()
readObjectNoData()
readResolve()
readExternal()
Polymorphism
Reection
Proxy
NO
T3/IIOP
readObject()
readObjectNoData()
readResolve()
readExternal()
Polymorphism
Reection
Proxy
NO
Hessian
Map.put()
toString()
Polymorphism
Reection
YES
Hessian-lite
[7]
Map.put()
Polymorphism
Reection
NO
Hessian-sofa
[8]
Map.put()
toString()
Polymorphism
Reection
YES
XStream
readObject()
Map.put()
Polymorphism
YESReection
Proxy 3.3. Step 2: Identifying Gadget Fragments with
Static Taint Analysis
In this step,
JDD
detects useful gadget fragments that
could be chained together to construct gadget chains from
entry points using static analysis. There are two substeps: (i)
gadget fragment formation and (ii) data-ow analysis within
a fragment. First,
JDD
starts from each source, i.e., en-
try points or implementations of previous dynamic method
invocation, until the next dynamic method invocation and
treats code in between as a fragment. Second,
JDD
also
performs a data-ow analysis to record taint propagation
from the parameters of the rst method in the fragment.
Specically, we design a
fragment-based summary
that,
for each gadget fragment, records the pollution behavior
between its rst method and the last method parameters and
maintains a sink-reachable condition record. Our purpose of
converting inter-procedure analysis of methods into jumps
between gadget fragments is to exibly simulate dynamic
method invocations and reduce the computational complex-
ity of inter-procedure searches.
Next, we rst describe the denitions of gadget frag-
ments and then a classication of gadget fragments.
Gadget Fragment Denition.
A gadget fragment is a
straight-line gadget sequence (i.e., methods could be exe-
cuted in Java deserialization), and its execution starts from
the fragment's head to its endpoint. For each fragment, its
endpoint commonly is a security-sensitive method or a dy-
namic method invocation that points to another fragment, for
example,
Object.equals()
could connect to almost all
the method “equals()” implemented by any class. During de-
serialization, this kind of dynamic method invocation indeed
introduces many possibilities of the program's execution
direction, thus they work like the jump/goto instructions.
In detail, the methods in a gadget fragment have:
Y
Head
, which is the entry method of this fragment
and there exist some dynamic method invocations that
could jump to this method.
Y
End
, which is the exit method of this fragment and
commonly a dynamic method invocation or security-
sensitive method.

--- page 12 ---

Stage I: Gadget Chain DetectionStage II: Exploitable Injection Object GenerationReusable Fragments ExtractionGadget Fragments SearchingGadget FragmentsLinkingConstrainsCollectionInjection ObjectGeneration & MutationFuzzing-based Exploitability ValidationInjection ObjectNew Exploitable Injection ObjectDominatorConstraints-basedFeedbackIOCDGenerationFragment Data SetGadget ChainsIOCDEntryPointsIdentification1 Identify Entries1 Identify Entries Identify Fragments2 Link Fragments3 Generate IOCD4Validate Exploitability5ExploitsExploitsTarget ApplicationTarget Application

--- page 13 ---

Figure 4: The Overall Architecture of
JDD
with Two Stages.
Y
Other gadgets, which are non-dynamic methods and
executed in sequence during deserialization to connect
the head and end.
Dynamic Method Invocation Types for Gadget Frag-
ments.
There are the following three types of dynamic
method invocations in gadget fragments:
Y
Polymorphic
:
JDD
recognizes the inheritance hierarchy
of the target program's classes and identies the over-
ridden methods. Then, when a method in a parent class
is invoked,
JDD
connects it to the corresponding over-
ridden methods implemented by its child classes. For
example, considering a class
B
that overrides method
”m” of class
C
, any fragment, where
End
is
C.m()
,
could jump to other fragments, where
Head
is
B.m()
.
Y
Dynamic Proxy
[9]: Java language supports objects
under type
interface
,
Object
and other generic
types to be implemented as a dynamic proxy instance,
and when the instance invokes any method, it would
be redirected to a specic invocation handler, i.e., the
invoke()
method implemented in this proxy. Such
handlers commonly deploy method routes based on the
properties (e.g. method name) of the trigger method.
Thus, for each handler,
JDD
conducts a path-sensitive
analysis to understand its method routs for ensuring
the trigger method will not connect to a wrong ex-
ecution path in invocation handlers. In practice,
JDD
rst identies gadget fragments in all execution paths
inside an invocation handler and then labels the gadget
fragments with corresponding method property require-
ments based on their execution paths.
Y
Reection
[10]: Unlike other dynamic features, Java
reection could invoke almost all methods imple-
mented in the program based on its parameters.
JDD
rst checks if the reection's parameters are attacker-
controlled (so that JOI can lead to RCE) and then
limits it to connect fragments that contain code ex-
ecution capabilities. Note that
JDD
allows reection
to connect any gadget in its successor fragments but
prefers two kinds of gadgets, based on the analysis of
existing gadget chains: (1) methods with no parameters,
especially
getter
or
is
methods, and implementation of
interface methods, and (2) methods with one parameter
of
Boolean
or
String
type.
3.4. Step 3: Linking Gadget Fragments to Con-
struct Gadget Chains using a Bottom-up Approach
Upon completing the search of gadget fragments,
JDD
performs a bottom-up search to chain fragments together,
thereby constructing all potential gadget chains as shown in
Algorithm 1. First,
JDD
obtains three types of fragments: (1)
Source Fragments
, whose head is a source, e.g., the Gadget
Fragment I in Figure 1; (2)
Free-State Fragments
, which
records method exection sequence between two dynamic
method invocations, e.g., the Gadget Fragments II-IV in
Figure 1; (3)
Sink Fragments
, whose end is a sink, e.g.,
Fragments V, VI in Figure 1. Then,
JDD
constructs potential
gadget chains by chaining
Sink Fragments
with
Free-State
Fragments
and then
Source Fragments
with the following
steps. Note that
JDD
needs to consider taint requirements
and method invocation conditions corresponding to different
dynamic features. For example, sink fragments commonly
require specic parameters should be controlled by attack-
ers. Then, when nding precursors for Sink Fragments,
JDD
would iteratively check if the corresponding parameters
could be tainted.
We now describe the details in Algorithm 1. First,
JDD
connects the
Free-State Fragments
that can transition to
Sink
Fragments
. As shown in Algorithm 1, during each round
(Line 2–19),
JDD
traverses each fragment
frag
fs
in
Free-
State Fragments
. Based on the summary of
frag
fs
,
JDD
checks whether the linking conditions to sink fragments are
satised. If so,
frag
fs
is added to
newSinkFragments
as
the
Sink Fragment
(Line 8–9) for the next iteration, while
keeping track of the taint requirements to be satised for
the connection (merging them if they are identical to the
already recorded taint requirements) (Line 11). Since each
iteration can pick out all fragments that can potentially
connect to the current sink fragments, the iteration process
terminates if there are no new Sink Fragments, i.e., when
newSinkFragments
is empty (Line 15–16) or reaching the
maximum number of search attempts. Next, the
Source
Fragments
are traversed, and the same approach is employed
to detect connectable successor fragments, thereby obtaining
all potential gadget chains (Line 20–26).
Lastly, assuming there are
n
œ
distinct dynamic method
invocations, let us explain why the upper limit for the
maximum number of iterations is
n
œ
. If the number of

--- page 14 ---

Algorithm 1
Gadget Fragments LinkingInput:
Sink Fragments Dataset
D
sk
Input:
Source Fragments Dataset
D
src
Input:
Free-state Fragments Dataset
D
fs
Output:
Gadget Chain DataSet
S
1:
//
n
œ
is the number of distinct dynamic method invocations in context.
2:
for
i

1
to
n
œ
do
3:
newSinkF ragments

g
4:
for
frag
fs
in
D
fs
do
5:
for
frag
succ
in
D
sk
.getFragStartWith(
frag
fs
:end
)
do
6:
// Checking whether the taint requirements are satised
7:
if
isLinkable(
frag
fs
,
frag
succ
)
then
8:
newSinkF ragments

newSinkF ragments
8
frag
fs
9:
D
sk
.add(
frag
fs
)
10:
// link
frag
fs
with
frag
succ
and merge taint requirements
11:
updateTaintRequirements(
frag
fs
,
frag
succ
)
12:
end if
13:
end for
14:
end for
15:
if
newSinkF ragments

g
then
16:
break
17:
end if
18:
D
sk

newSinkF ragments
19:
end for
20:
for
frag
src
in
D
src
do
21:
for
frag
succ
in
D
sk
.getFragStartWith(
frag
src
:end
)
do
22:
if
isLinkable(
frag
src
,
frag
succ
)
then
23:
S

S
8
link
ˆ
frag
src
; frag
succ
�
24:
end if
25:
end for
26:
end for
27:
return
Siterations exceeds
n
œ
, the longest fragments will necessarily
contain candidates with two fragments whose ends are the
same dynamic method. Since the attacker has the ability
to invoke any candidate with the same dynamic method,
the attacker can directly supply the class implementation in
the latter call to the rst to reduce the total length, so the
path between two identical dynamic method invocations is
redundant.
Time Complexity.
JDD
reduces the static search time from
O
ˆ
eM
n
�
(i.e., those of state of the art, e.g., ODDFuzz [2])
to
O
ˆ
M
2
n
3

enM
�
according to Theorems 1 and 2 below.
Theorem 1.
The search complexity of Algorithm 1 is
O
ˆ
n
3
M
2

enM
�
, where
n
is the number of dynamic method
invocations,
M
is the average number of candidates for
these invocations, and
e
is the number of entry points.
Proof.
See Appendix A.1.Theorem 2.
The search complexity of ODDFuzz [2] is
O
ˆ
eM
n
�
, where all notations follow Theorem 1.
Proof.
See Appendix A.2.3.5. Step 4: Constructing IOCD based on Injection
Object related Constraints
There are two substeps here: (i) constraint extraction and
(ii) IOCD generation. First,
JDD
follows the call sequence
of this gadget chain to extract the execution paths, and then
uncovers three types of constraints that affect inputs:
Y
Class hierarchy relationships between object and eld
instances. After
JDD
performs bottom-up fragment
linking, it will perform top-down class hierarchy infer-
ence according to the fragment connection sequence.
Specically, for each gadget fragment,
JDD
rst uses
dataow analysis to determine which of its elds is
linked to the next fragment, and then uses the header
method of the subsequent fragment to determine the
actual type of the eld. For example, in the Gadget
Fragment I in Figure 1,
JDD
nds the
HashMap
object
has a eld
table
(Line 3) and
table
should store
two objects (i.e.
n1
,
n2
) based on the dataow to Line
8. Another important problem here is to identify the
exact class type of these elds, considering many of
them are dened as generic type or
Object
, e.g. the
key
in Line 8, the eld
key
of
n1
and
n2
(i.e.
this.key
,
obj.key
) in Line 17, etc. To solve this problem,
JDD
continues the dataow tracing and nds that the
key
connects Fragment I with II, and the header method
of Fragment II is
NodeImpl.equals
. Thus,
key
should be a
NodeImpl
instance. Similarly,
this.key
and
obj.key
connect Fragment II with III and Fragment
III with IV, respectively. Therefore,
JDD
infers that
the eld
key
of two
NodeImpl
instances,
n1
,
n2
are
ConcurrentHashMap
and
UIDefaults
instances,
as indicated by the header methods of successor Frag-
ment III and IV. Based on the approach, JDD ultimately
deduces the correct class hierarchy of the injection
object as illustrated in Figure 3 (a).
Y
Conditional branches related to elds, which exist in
the execution paths of the gadget chain, and note that
JDD
labels constraints shared by different execution
paths as
dominator
meaning that they are required
by all the execution paths. During the process of
dataow tracing,
JDD
concurrently collects conditional
branch constraints related to elds by identifying if the
variables checked in the constraints could be tainted
by elds. Moreover, to ensure the program execution
would not trigger an exception, these exist several
implicit constraints should be satised. For example, a
eld could not be
null
when it invokes some methods.
Another example is forced type casting, which requires
the eld should be an instance of specic type.
Y
Field dependency constraints, which encompass condi-
tional constraints among elds, i.e. the constraints i-iii
as shown in Figure 3. Note that sink points commonly
require specic elds be controlled by the attacker
to inject payloads.
JDD
would label these elds to
check if they can be tainted by input. To nd eld
dependency constraints, in general,
JDD
lters those
conditional constraints that affect multiple elds and
then labels these elds with related constraints as eld
dependencies. Furthermore,
JDD
also considers specic
requirements for Java reection. For example, the three
elds
className
,
methodName
, and
args
used in
Java reection should ensure the target class contains
the target method.
Second, after extracting these constraints,
JDD
uses
a novel data structure, termed Injection Object Construc-

--- page 15 ---

tion Diagram (
IOCD
) to model the object structure and
dependencies of elds. There are two sub-steps. (i)
JDD
treats the instantiated objects contained in a gadget chain
as
ClassNodes
. Each
ClassNode
stores the following infor-
mation: the class name and the related
FieldNodes
, which
represent the elds that may be utilized during the deserial-
ization. The
FieldNode
, on the other hand, stores the relevant
constraint information for these elds and marks whether
these constraints are statically determinable as
dominator
.
(ii) Based on the structural constraints, the
ClassNodes
are
interconnected through
FieldNodes
using directed edges,
thereby indicating the hierarchical relationships between
instantiated objects. For example, in the motivation example,
JDD
will construct
ClassNodes
representing the instances of
NodeImpl
,
UIDfaults
, and
ConcurrentHashMap
.
Then, following the structural constraints,
JDD
establishes
edges from the
UIDfaults
and
ConcurrentHashMap
ClassNodes
to the same
FieldNode
(i.e.
key
) of the
NodeImpl
ClassNode
, which implies the existence of
at least two NodeImpl instances. Thus,
JDD
will in-
clude an additional
NodeImpl
ClassNode
to signify the
existence of two
NodeImpl
instances, where the eld
key
of each instance is assigned to
UIDfaults
and
ConcurrentHashMap
instances, respectively, as illus-
trated in Figure 3 (a).
3.6. Step 5: IOCD-enhanced Directional Fuzzing
After modeling the structure of injection object and the
constraints should be satised,
JDD
further utilizes IOCD to
enhance our directional fuzzing. In general, given a gadget
chain, the fuzzing goal is to generate an injection object
that could reach and exploit its sink point. Specically,
JDD
rst generates initial seeds based on the IOCD and
then uses them to drive the fuzzing. In the exploration
phase of directional fuzzing,
JDD
utilizes the number of
covered dominator constraints to evaluate the seed's energy
and guide the fuzzer to cover more dominator constraints
until reach the sink point. In the exploitation phase of
directional fuzzing,
JDD
only mutates the elds related to
the sink point. During each eld's mutation,
JDD
adjusts
other related elds to x the cross-eld dependencies based
on IOCD.
IOCD based Seed Generation.
Considering the cross-eld
dependencies and nested object structure,
JDD
adopts the
IOCD-guided fuzzer to generate objects with the correct
class hierarchy while taking into account the constraints
among elds. Specically,
JDD
generates parameterless in-
stances based on
ClassNodes
from the
IOCD
and estab-
lishes the class hierarchy of these instances according to
directed edges, as illustrated in Figure 3. Subsequently,
starting from the root
ClassNode
node, a Breadth-First
traversal is performed on each
FieldNode
.
JDD
will extract
dominator
constraints of these
FieldNodes
, and invoke the
constraint solver to generate appropriate values, which are
then assigned to the corresponding elds. In situations where
bidirectional edges exist between
FieldNodes
, indicating the
existence of constraint dependencies between two elds,
JDD
extracts
dominator
condition constraints from the rel-
evant
FieldNodes
. These constraints are then solved using a
constraint solver to nd values that simultaneously satisfy
these constraints.
Dependency-aware Seed Mutation.
IOCD signicantly
enhances the efciency of fuzzing from the following three
aspects: (1) Selecting appropriate elds for mutation; (2)
Reducing the uncertain mutation space through constraint
information; (3) Considering elds dependencies and nested
object structure. That is when mutating a eld, the constraint
relationships between this eld and other related elds or
upper-level instance objects containing this eld are consid-
ered. Detailed strategies can be found in Table 2.(i)Mutationbasedonconditionconstraints. Firstly,
based on the feedback information obtained from seed ex-
ecution,
JDD
matches suitable condition constraints from
IOCD that are derived from the specied program execu-
tion ow of gadget chains. And these condition constraints
are utilized to selectively guide the structural mutation of
injection objects. In order to record the selected condition
constraint strategies,
JDD
denes a unique identier and
assigns a 2-bit ag to indicate the mutate strategy for each
condition constraint. The
rst bit
is used to indicate whether
the constraint is used (0: not selected, 1: selected), and
the
second bit
signies whether the constraint is satised
(true or false). With this identier,
JDD
prefers to select
unused strategies to cover more kinds of combinations of
condition constraints. The following explains how to gener-
ate condition constraint branch strategies based on feedback
information:
(1) If
JDD
resolves the
ClassCastException
or
NullPointerException
exception information,
relevant elds causing the exception can be matched
from
IOCD
based on error location information (class
name, code line number), and
JDD
will require these
elds to satisfy specic constraints, i.e.
field
!

null
,
field instanceof X:class
.
(2) Extract all constraints between the current reached and
the next
dominator
condition constraints, and select a
mutation strategy based on each constraint's identier.
(3) If there are no
non-dominator
condition constraints
between the current and the next
dominator
condition
constraints, random mutation strategies are selected for
the current
dominator
and the preceding conditional
constraints, note that
dominator
condition constraints
do not alter the
second bit
ag.
(4) If the program has reached the sinks but has not
triggered the expected malicious instructions,
JDD
rst
checks whether there are multiple ways to construct
malicious data (i.e., constructed from different elds).
If such variations exist,
JDD
uses the information
recorded in
IOCD
to call different elds to construct
malicious data. Otherwise, randomly changing the con-
dition constraints strategies.
(5) If all combinations of strategies for condition con-
straints have been used, a 50% probability is assigned

--- page 16 ---

Table 2: Mutation Strategy. Property(
prop
)
Type
Constraint(
cnst
)
TypeExample
Mutation StrategyClass
Class
Method
Stringif(
prop
==
cnst
)
if(
prop
.getDeclaredMethods().contains(
cnst
))
if(
prop.name
==
cnst
)
if(
prop.superClassName
==
cnst
)
if(
prop.interfaceName
==
cnst
)
set
prop
to
cnst
set
prop
to a Class instance that contains
cnst
Method
set
prop
to a Class instance of
cnst
set
prop
to a Sub-Class instance of
cnst
set
prop
to a Implementation Class instance of
cnst
Method
Class
String
intif(
prop.declaringClass==cnst
)
if(
prop.name
.startWith(
cnst
))
if(
prop.parameterNums
==0)
set
prop
to a Method instance of
cnst
Class
set
prop
to a Method instance with proper name
set
prop
to a Method instance with proper args numbers
Object
Classif(
prop
instanceof
cnst
)
correct
prop
to an instance of
cnst
Collection/Map
int
Class
Objectif(
prop
.size
C
cnst
)
if(
prop.item
instanceof
cnst
)
if(prop.contains(cnst))
add/remove elements
correct the element type
add/remove elements to randomly select elds from
IOCD
that have not
been marked with existing condition constraints for
mutation.
(6) When the program reaches sinks and captures mali-
cious instructions being written, that means the injec-
tion object is exploitable, and the corresponding gadget
chain is classied as exploitable. If the time threshold is
exceeded, or based on the specic type of information
mentioned above, it can be directly determined as
non-exploitable, the current test is terminated, and the
next
IOCD
corresponding to the next gadget chain is
invoked to start a new round of testing.(ii)Mutationbasedonobjectstructureconstraints. After
obtaining the condition constraints,
JDD
invokes the con-
straint solver to adjust the object's structure. Nevertheless,
as demonstrated by IOCD, there exist intricate constraint
relationships between elds. Modifying one of these elds
can affect not only the corresponding ClassNode but also
its elds and the elds associated with other ClassNodes.
Consequently, a simplistic adjustment of an individual eld
based solely on condition constraints may compromise the
structural validity of the object.
To address this issue, we propose our cascading mutation
strategy. When
JDD
adjust a eld, it cascadingly exam-
ines whether other elds affected by this eld also require
adjustments. If necessary, it adjusts them simultaneously
to maintain the structural validity of the injection object.
Specically, the mutation strategy can be categorized into
two levels: single-eld and cross-eld:
Y
Single-Field level. Mutating an individual eld, which
does not have any constraints with other elds. Uti-
lizing constraint solvers to resolve relevant conditional
constraints for adjusting the assignment of the eld.
Y
Cross-Field level. When mutating a eld with mutual
constraints among other elds, ensure that relevant
information in associated elds is preserved, and main-
tain the validity of the object structure.(iii)Mutationbasedonelddependencyconstraints.
Based on the insight of making minimal modications to
the affected elds to avoid disrupting valid information after
mutation, and leveraging knowledge of class hierarchies,
JDD
has implemented the following two cross-eld level
mutators, i.e. nested eld value reuse, sequential xed ad-
justments.
Y
Nested eld value reuse
. After mutating a specic eld
(i.e.,
mutatedField
), recursively check and adjust its
associated elds. Specically, start by adjusting the
elds of
mutatedField
based on the relevant
domina-
tor
constraints on the IOCD. Then, detect the elds
affected by the current constraint strategy, and reuse
instances shared between the post-mutation and pre-
mutation eld instances.
Y
Sequential xed adjustments
. If
JDD
intends to mutate
a specic eld (i.e.,
eld1
), and there exists a constraint
associated with multiple elds (i.e.,
eld2
,
eld3
),
JDD
extracts the constraints relevant to these three elds
separately. It then calls a constraint solver to nd
values for
eld1
that satisfy all related constraints while
minimizing
eld2
and
eld3
adjustments. Specically,
the constraint solver rst xes
eld2
and
eld3
and then
determines an appropriate value for
eld1
. If it is unable
to nd a solution that satises the other constraints
on
eld1
, it progressively adjusts
eld2
and
eld3
and
continues the solving process.
4. Implementation
We implemented
JDD
with over 25,000 lines of new Java
code (excluding any third-party libraries). We will open-
source
JDD
in the camera-ready version of the paper. The
static taint analysis module of
JDD
is implemented based
on Soot [11] and FlowDroid [12], a ow-sensitive, object-
sensitive, and context-sensitive data-ow analysis tool. To
identify the gadget fragments in dynamic proxies, we im-
plemented a path-sensitive analysis inner their method invo-
cation handlers. Moreover, we also conducted a lightweight
pointer-to analysis to reduce the jump candidates in iden-
tifying gadget fragments. The dynamic fuzzing module of
JDD
is implemented based on JQF [13], [14]. We rst use
ASM [15] to instrument the target Java program for collect-
ing the needed runtime context to guide our fuzzing engine.
Then, we customized JQF to build a directional fuzzing
framework for the generation of exploitable injection ob-
jects. To avoid
JDD
stuck in a hard-to-detect chain, we set

--- page 17 ---

the time limitation for identifying each gadget fragment in
the static analysis as 30 seconds and each round of fuzzing
as 120 seconds, empirically.
5. Evaluation
In this section, we evaluate the performance of
JDD
on
real-world Java programs and compare it with state-of-the-
art tools via addressing four main research questions below:
Y
RQ1: How does
JDD
compare with state-of-the-art tools
in detecting gadget chains?
Y
RQ2: How do the core modules of
JDD
contribute to its
performance?
Y
RQ3: How many zero-day JOI-based RCE vulnerabilities
can
JDD
detect?
Y
RQ4: How does
JDD
perform in analyzing real-world Java
applications?
5.1. RQ1: Comparison with State of the Art
In this section, we compare
JDD
with state-of-the-art
approaches in detecting (un)known gadget chains using
two benchmarks. Specically, we choose three state-of-
the-art tools, namely GadgetInspector [3], SeHybrid [4],
ODDFuzz [2]. To reduce randomness, we conducted ve
repetitions of each experiment and reported the average
statistical results. All experiments were conducted on a
Linux workstation with an Intel(R) Xeon(R) Gold 5218 CPU
@ 2.30GHz and 128 GB of RAM, running Ubuntu 18.04
LTS.
Benchmarks.
We conducted this experiment using a dataset
of 61 well-known gadget chains that can be exploited to con-
duct JOI attacks. Among these gadget chains, 34 come from
the well-known ysoserial repository [5], which has been
widely used in prior work [2]–[4]. Additionally, we collected
26 other gadget chains by analyzing 32 recently disclosed
JOI vulnerabilties. These vulnerabilities could cover popular
deserialization protocols that are not included in ysoserial,
for example, Hessian [16] and T3/IIOP [17] [18]. The new
benchmark will be available together with our open-source
repository.
Overall Results.
Table 3 summarizes the overall results
of the experiment. In this table, we present the quantities
of gadget chains identied through static analysis (Iden-
tied chains), the number of gadget chains conrmed as
exploitable (conrmed chains), and the number of new-
discovered gadget chains beyond the scope of the known
dataset (unknown chains). Note that, since SerHybrid, ODD-
Fuzz, and JDD have dynamic validation modules, their
conrmed chains come from the veried results of their
dynamic analysis. For GadgetInspector, a tool that is solely
reliant on static analysis, we manually verify the reported
results to determine the number of conrmed chains.
Overall, for the capability of detecting known gadget
chains, the effectiveness of
JDD
is higher than existing tools.
Particularly,
JDD
covers 27 known and 91 (including two
variants of known chains) unique unknown chains in ysose-
rial repository, which is much larger than GadgetInspector
(three known + zero unknown), SerHybrid (two known +
zero unknown), and ODDFuzz (16 known + zero unknown).
Note that
JDD
supports the identication and reuse of
gadget fragments in known exploits. Since existing tools
do not rely on known exploits, Table 3 does not include
known exploits as input for the reason of fairness. We now
describe the improvement if
JDD
is further improved by
introducing the gadget fragments of known exploits. Take
C3P0
as an example. If
JDD
is equipped with the known
chain of
C3P0
,
JDD
can detect not only the gadget chains
in Table 3 but also another ve unknown gadget chains.
Additionally, in the expanded dataset of 26 gadget chains
extracted from recently disclosed JOI vulnerabilities,
JDD
also achieves a better result by detecting 24 known and 140
unknown chains.
False Positive Rates.
The existing tools for static detection
of gadget chains commonly exhibit a high false positive
rate. For example, GadgetInspector reaches a false positive
rate as high as 97.6%. However, SerHbrid, ODDFuzz, and
JDD
reduce the false positive rate of nal results to 0% by
introducing dynamic verication.
False Negative Rates.
As shown in Table 3,
JDD
missed
seven known gadget chains in ysoserial, resulting in a false
negative rate of 20.6% (7/34). GadgetInspector and ODD-
Fuzz have false negative rates of 91.2% (31/34) and 52.9%
(18/34) respectively. SerHybrid could not support the test
of all Java apps in ysoserial. On the dataset they tested,
SerHybrid has a false negative rate of 83.3% (2/12).
JDD
demonstrated signicantly lower rates of false negatives.
We then break down the seven known gadget chains
that missed by
JDD
. First, four of them require specic do-
main knowledge to identify some of their gadget fragments.
Specically,
JDD
lacks domain knowledge of security-
sensitive methods in
Jython
app, making it unable to
detect the chain. Additionally, generating valid serialization
data for the case in
C3P0
requires rewriting a specic
method. Moreover,
JDD
lacks the knowledge about how the
return value of a dynamic proxy's invocation handler affects
program execution, thus failing to detect two chains in
Spring
(i.e.
Spring1,2
). As aforementioned, we could
use known exploits to further enhance
JDD
by identifying
the gadget fragments used in them. For instance,
JDD
can
automatically extract reusable fragments based on the ex-
ploit of
Spring1
and further identify
Spring2
. Second,
the rest three gadget chains contain many elds with a
generic type, e.g., an
Object
type, leading to a time-out.
Benets in Supporting Java Dynamic Features.
Bene-
ting from the bottom-up fragment search strategy,
JDD
has the capacity to support more Java dynamic features
to expand its detection capabilities, including
Polymorphic
,
dynamic proxy
and
reection
, in which the last two are
commonly unsupported by existing tools. As a result,
JDD
could detect more gadget chains related to these dynamic
features than existing tools.

--- page 18 ---

Table 3: Gadget chain detection comparison among GadgetInspector, SerHybrid, ODDFuzz, and
JDD
(Our Approach). The
number in parentheses indicates the detected known chains in the benchmark. Application
Known
ChainsGadgetInspector SerHybrid ODDFuzz JDDIdentied
Chains
Conrmed
ChainsIdentied
Chains
Conrmed
ChainsIdentied
Chains
Conrmed
ChainsIdentied
Chains
Conrmed
Chains
Unkown
ChainsYsoserial BenchmarkAspectJWeaver
18
0N/A
N/A9
0CommonsBeantuils
14
00
08
1108†
25
20
CommonsCollections
54
11
197
3BeanShell 12 01 08 0587 5 4
C3P0
12
0N/A
N/A13
115
0
0
Click 14 0N/A N/A8 16 1 0
Clojure
112
1N/A
N/A184
16
3
2
CommonsCollections4 24 01 1112 2230 26 24
Groovy
14
03
013
0413
5
4
JavassistWeld 12 0N/A N/A8 06 1 0
JBossInterceptors
12
0N/A
N/A8
07
1
0
JDK 45 0N/A N/A9 116 8 5
JSON
17
0N/A
N/A9
0147
6
5
Jython 142 1N/A N/A32 00 0 0
MozillaRhino
23
0N/A
N/A7
24
2
0
Hibernate 23 03 08 214 5 4
Myfaces
22
0N/A
N/A7
052
3
2
ROME 12 00 05 148 9 8
Spring
22
0N/A
N/A10
05
0
0
Vaadin 16 0N/A N/A13 1109 14 13
FileUpload
13
0N/A
N/A8
01
1
0
Wicket 13 0N/A N/A7 01 1 0Total
34126 3 (3)9 2 (2)583 16 (16)1362 116 (27) 91Recently Disclosed VulnerabilitiesWeblogic
2153
0N/A
N/AN/A
N/A642
126
107
MarshalSec(Hessian)‡ 52 0N/A N/AN/A N/A119 38 33Total
2655 0 (0)- -- -761 164 (24) 140†
Due to the shared use of the CommonsCollections dependency in detecting Gadget Chains in AspectJWeaver and CommonsBeanutils, we simultaneously
conducted analysis on these three packages.
‡
MarshalSec is a deserialization vulnerability exploitation tool, and we include its Hessian protocol-based Exploits as part of our evaluation dataset.
First, due to its support for the dynamic proxy feature,
in our benchmark data set (i.e., the ysosearial repository),
JDD
can detect additional 16 gadget chains (3 known and
13 unknown chains) compared to existing tools.
Second, with the support of Java reection,
JDD
can
detect more variants of gadget chains. An example is
Hibernate
, which contains two variants of one unique
chain in our benchmark. The difference of these two vari-
ants is in the last fragments, i.e, their targets of Java re-
ection.
JDD
successfully detects three unique chains in
Hibernate
and additionally identies two fragments that
could be linked as the targets of Java reection to conduct
code execution attacks. Another example is
Vaadin
.
JDD
rst detects 14 gadget chains in it, which all end with Java
reection and
JDD
additionally identies three fragments
that could be linked to conduct code execution attacks.
5.2. RQ2: How do the core modules of
JDD
con-
tribute to its performance?
We conducted two ablation studies on the task of gadget
chain detection and exploitability verication by comparing
JDD
with the following variants to evaluate the effectiveness
of
JDD
's different modules:
Y
JDD
-top-down. We replace
JDD
's bottom-up strategy
with top-down strategy proposed by previous tools, i.e.
a Depth-rst-search (DFS) starting from a source to a
sink.
Y
JDD
-NoIOCD. We remove
JDD
's
IOCD
guidance in
the fuzzing module. Instead,
JDD
-NoIOCD employs an
approach like ODDFuzz to infer the class hierarchy
and randomly mutates elds based on a pre-dened
dictionary.
Y
JDD
-NoClassHierarchy: We replace
JDD
's class hier-
archy inference approach with the approach proposed
by previous tools, e.g., ODDFuzz.
Y
sys-NoConFd: We remove
JDD
's condition-constraints-
aware and eld-dependency-constraints-aware muta-
tion. Because these two types of constraints are closely
related, we remove them together. Additionally,
JDD
-
NoConFd mutates elds randomly based on a pre-
dened dictionary, similar to ODDFuzz.
First, we verify whether the bottom-up strategy is more
effective than the top-down strategy, by comparing how
many exploitable gadget chains can be found by these
two methods.
JDD
completed the analysis in seven min-
utes and 58 seconds with no timeouts and detected 116

--- page 19 ---

Table 4: The Detected Chains and Performance Evaluation Results of
JDD
on Real-World Java Apps. Application
Basic Information Detected Chains PerformanceStars
Class
Number
Method
NumberIdentied
Chains
Conrmed
Chains
Vendor
ReplySearch and Link
Gadget Chains
Construct
IOCD
Dynamic Verify
(Detected Chains)Apache Dubbo 39K 88.5K 936.4K31 7 CVE Assigned8min29s 53s 36min15s (31)
Motan 6K 53.7K 454.7K695 93 CVE Assigned15min25s 47min13s 6h (358)
Solon 1.5K 280.9K 2,797.9K117 35 CVE Assigned39min56s 29min16s 2h35min59s (117)
XXL-Job 24.5k 52.5K 411.1K843 110 CVE Assigning7min24s 52min8s 6h (363)
Sofa-rpc 4.8K 94.9K 883.9K205 43 CVE Assigned37min15s 8min6s 3h43min3s (205)
Apache Tapestry 0.1K 28.8K 241.1K16 5 CVE Assigning54s 9s 19min38s (16) exploitable gadget chains. In comparison,
JDD
-top-down
took about 17 hours and only detected 15 gadget chains.
After further analysis, we found that the analysis of 900
sources in
JDD
-top-down timed out, thus missing 101 ex-
ploitable gadget chains. For example, in the analysis of
CommonsCollections4
app,
JDD
-top-down failed to
complete the analysis of
PriorityQueue.readObject
within the time threshold (e.g. ve minutes). As a result,
JDD
-top-down missed two exploitable chains.
Second, we evaluate the effectiveness of three types of
guidance information in dynamic verication - class hier-
archy constraints, conditional constraints and eld depen-
dency constraints, as well as the effectiveness of dataow-
based class hierarchy inference approach, by comparing
the detection capabilities of
JDD
with
JDD
-NoIOCD,
JDD
-
NoClassHierarchy and
JDD
-NoConFd on exploitable gadget
chains.
Experimental results show that
JDD
performs best, with
a total of 116 exploitable gadget chains detected, far ex-
ceeding
JDD
-NoIOCD (31),
JDD
-NoClassHierarchy (41)
and
JDD
-NoConFd (38). The experimental results prove
that to generate exploitable injection objects for gadget
chains efciently, the three types of constraint information in
IOCD (described in Section 3.5) are essential, especially for
complex chains. For example, for the chain in our motivat-
ing example,
JDD
-NoClassHierarchy and
JDD
-IOCD will
infer the wrong class hierarchy as shown in Figure 3 (b),
causing subsequent mutations to be meaningless. Although
JDD
-NoConFd can generate seeds with the correct class
hierarchy, it is challenging to generate an object that si-
multaneously satises the constraints (e.g. i-iii in Figure 3)
within the time threshold, so this case is easily missed.
In addition, compared with ODDFuzz,
JDD
-NoIOCD
detected 15 more exploitable chains on the same benchmark
ysoserial. This is because
JDD
's static analysis module
can provide more high-quality candidate chains, which also
means that
JDD
's static analysis module can help to im-
prove ODDFuzz's detection capabilities.
5.3. RQ3: Discovering Zero-day Vulnerabilities
In this section, we run
JDD
atop real-world popular
Java applications to detect zero-day JOI-based RCE vul-
nerabilities. Specically, we rst collected 80 popular Java
open-source apps from Github [19] with more than 100
stars. Then, we implement a semi-automatic tool to check
if they contain public entries for Java object injection and
deserialization. As a result, we successfully recognized six
apps (shown in Table 4) and use them as the dataset of this
experiment. For these six popular Java apps, we conducted
our analysis based on the default or recommended congu-
ration within their open-source projects. In this experiment,
the total time limitation for dynamic testing is 6 hours.
Table 4 shows the results, which indicates that
JDD
successfully identied zero-day JOI vulnerabilities in all of
these six Java apps as well as generated exploitable injection
objects for the 293 found gadget chains (127 unique chains).
We have reported these gadget chains to the app developers
and received conrmation from them. For example, the de-
velopers of Dubbo admitted that it is impossible for them to
uncover these gadget chains, which indicates the urgency of
our automatic tool. All 127 zero-day gadget chains detected
by
JDD
are capable of bypassing the latest patch defenses
at the time and, hence are vulnerabilities. Noting that, since
we reported multiple gadget chains for each attack point to
help developers design and implement more comprehensive
defenses, we ultimately obtained six CVEs, less than the
total count of chains.
To demonstrate how our fragment based bottom-up ap-
proach can benet the detecting of gadget chains, we use
real-world zero-day vulnerabilities found by
JDD
for case
study.
Case Study #1: JOI based RCE Attacks.
JDD
discovered a
JOI based RCE vulnerability that impacts many popular Java
apps such as Sofa, Solon, and XXL-Job, in which XXL-Job
is a highly popular distributed task scheduling framework
with a remarkable number of GitHub stars (24.9k) and forks
(10.3k) as well as be widely used by large enterprises with
over 256 million consumers. This vulnerability could allow
attackers to take over the victim server by sending a request
with a well-crafted injection object.
Thses application utilize the Hessian/Hessian-sofa
protocol to deserialize the received serialized data. The
main attack process for this vulnerability is illustrated
in Figure 5, wherein the attacker initializes a
HashMap
object and places two other
HashMap
objects (i.e.
hmap1
,
hmap2
) inside it, as well as ensures that
hmap1
,
hmap2
have
identical hash values to trigger the jump from Fragment
1 to 2. Then, to facilitate the jump from Fragment 2 to
Fragment 3 and then to 4, the attacker needs to insert a
Type
instance and a
JSONObject
instance into
hmap1
and
hmap2
, and alternate the order of insertion. Then, based

--- page 20 ---

# Fragment 1HashMap.put()HashMap.putVal()# Fragment 2AbstractMap.equals()# Fragment 3AudiofileFormat$Type.equals()# Case 1 # Fragment 4afastjson2.JSONObject.toString()# Fragment 5bfastjson2.JSONWriterUTF16.write()# Fragment 6cfastjson2.ObjectWriter2.write()# Fragment 7dfastjson2.FieldWriterObject.write()fastjson2.getFieldValue.write()reflect.Method.invoke()# Fragment 4ajackson.JSONObject.toString()...# Fragment 5bjackson.SerializableSerializer.serialize()# Fragment 6cjackson.POJONode.serialize()...# Fragment 7djackson.BeanSerializer.serialize()...# Fragment 8jackson.BeanPropertyWrite.serializeAsField()reflect.Method.invoke()# Fragment 10ContinuationContext.getTargetContext()NamingManager.getContext()NamingManager.getObjectInstance()# Case 2 # Fragment 9ServerManagerImpl.getActiveServer()ServerTableEntry.isValid()ServerTableEntry.activate()Runtime.exec()# Fragment 11UnixPrintServiceLookup.getDefaultPrintService()UnixPrintServiceLookup.getDefulatPrinterBSD()UnixPrintServiceLookup.execCmd()Runtime.exec()/* This HashMap stores * hmap1 & hmap2 */

--- page 21 ---

Figure 5: Simplied Gadget Chains of Case Study #1 and
Case Study #2, where Case #2 is an evolution of Case #1
with some gadget fragments being replaced.
on the information about the object (i.e.,
obj
) contained
in the
JSONObject
instance, the deserialization process
will jump from Fragment 4a to 7d, and subsequently
invoke reective calls to methods related to the elds
of
obj
, such as ”getDefaultPrintService()” method of
a
UnixPrintServiceLookup
object. This method
further leads to the execution of arbitrary commands
injected by the attacker through
Runtime.exec()
.
Alternatively, as a variant, this gadget chain also
can utilize Java reection in Fragment 7d to invoke
ContinuationContext.getTargetContext()
and carry out JNDI based code injection attacks.
Case Study #2: The Evolution of Case Study #1.
By
replacing certain fragments in a gadget chain, an attacker can
rapidly discover new gadget chains that can affect another
app. Taking the gadget chain introduced in Case Study 1
as an example, this chain can affect apps like Sofa-RPC,
solon, XXL-Job. However, due to the absence of the required
Java library dependency in Motan by default, this gadget
chain cannot be used to exploit Motan, as some of its gadget
fragments missed.
However, if the missed fragments could be replaced by
gadget fragments in Motan, it could generate a new chain.
Actually, in Motan,
JDD
detected an equivalent fragment
that depends on Jackson [20], a widely-used third-party
dependency for data-binding functionality and tree-model.
Thus, the Fragment 4a-8 (in # Case 2) can replace the
Fragment 4a-7d (in # Case 1), resulting a new chain, as
illustrated in Figure 5.
Furthermore, the gadget chain in Case Study
1 uses the ”getDefaultPrintService()” method of a
UnixPrintServiceLookup
object to load and execute
code from remote attackers. However, this method could
only be invoked in a Unix-like system. For those non-Unix
systems,
JDD
could further nd alternative fragments
to replace it thus xing the chain, for example, using
”getActiveServers()” method in
ServerManagerImpl
class.
5.4. RQ4: Performance
In this section, we evaluate the performance of
JDD
in
analyzing real-world Java apps. Table 4 shows the results.
For the easy of statistic, we separate the analysis time of
JDD
into three parts: (i) the gadget chain searching and
linking (i.e., Steps 1–3 in Section 3), (ii) IOCD construction
(i.e., Step 4 in Section 3), and (iii) directional Fuzzing (i.e.,
Step 5 in Section 3). The results indicate that
JDD
could
nish its analysis for most of real-world apps in the time
limitation (six hours for each app).
We have two observations. First, the static analysis part
of
JDD
(Steps I–III) is very efcient, nishing with 20 mins
in most cases. The reason is that
JDD
's static search time is
polynomial, i.e., efcient in nding possible gadget chains.
The analysis of Solon is slower but still within 40 minutes
because the number of possible gadget fragments is large.
Second, the dynamic analysis part of
JDD
may still have
performance issues. Specically, the analysis of Motan and
Sofa-rpc times out after six hours due to false positives in
gadget chains reported by
JDD
's static analysis. The main
reason is the imprecision in our points-to analysis and path
insensitivity outside invocation handlers of dynamic proxy.
We leave the improvement of static analysis's precision as
our future work.
6. Discussion
Expandability for Incomplete Patching Problem.
One
common problem facing JOI vulnerabilities and their
patches is that remote attackers may nd alternatives for
the blocked gadgets in the patch and derive new exploitable
gadget chains from the original ones. For example, Figure 6
illustrates the gadget chains' reuse relationships among 23
JOI vulnerabilities that affect WebLogic [21], a widely-
used J2EE application server employed by over 430K Java
applications. Notably, CVE-2015-2852 continuously evaded
security patches by successively replacing parts of the frag-
ments that were blacklisted, leading to a total of 11 follow-
up CVEs over a period of six years.
There are two methods for users to expand
JDD
for
the incomplete patching problem. First, users may expand
the fragment data set of
JDD
with known fragments, e.g.,
all possible gadgets in CVE-2015-2852. Second, users may
expand the source set of
JDD
with known sources. These
two methods will help users to nd possible derivative
vulnerabilities, thus making the patch more complete.
Lightweight Pointer-to Analysis and Restricted Path-
sensitive Analysis.
We leverage pointer-to analysis and
path-sensitive analysis to mitigate the erroneous generation

--- page 22 ---

CVE-2015-2852CVE-2016-0638CVE-2016-3510CVE-2017-3248CVE-2018-2826CVE-2018-2893Sep.2015Apr.2016Jul.2016Jan.2017Apr.2018Jul.2018CVE-2018-3245CVE-2018-3248CVE-2018-3191Oct.2018CVE-2020-2555Jan.2020CVE-2020-2883Apr.2020The gadget fragments is used byDisclosed VulnerabilityCVE-2020-14645Jul.2020Oct.2020CVE-2020-14825Jan.2021CVE-2020-14756Apr.2021CVE-2021-2135CVE-2021-2136Jul.2021CVE-2020-2551Jan.2022CVE-2021-2394Jan.2023CVE-2022-21350CVE-2023-21839Apr.2023CVE-2023-21931May.2016CommonsCollections5(ysoserial)Mar.2016JRMPListener(ysoserial)

--- page 23 ---

Figure 6: WebLogic's JOI vulnerabilities and the reuse of their gadget fragments, which lead to the incomplete patch
problem.
and concatenation of fragments, thereby reducing false pos-
itives in static analysis and lowering the computational load
of fuzzing.
The misidentication of an object's type can result
in the erroneous identication of dynamic method invo-
cations, consequently leading to false positives in frag-
ment generation and linking. The utilization of pointer-
to analysis techniques effectively reduces false positives
caused by this issue. For instance, in the analysis of
the
CommonCollections4
application, applying the
lightweight pointer-to analysis results in a reduction of 806
false positive chains.
Furthermore, dynamic proxies are widely used in many
Java apps. Specically, an invocation handler of dynamic
proxy usually selects different program handling logic based
on the method properties (e.g., method name) that triggers
the handler, resulting in many possible execution paths
during static analysis. Thus, it requires a path-sensitive
analysis to identify accurate execution paths when linking
gadget fragments in invocation handlers of dynamic proxies.
But applying the path-sensitive analysis to a larger scope
(e.g., the entire codebase) will signicantly slow down static
analysis with limited gains in reducing false positives, so
we limit the scope of path-sensitive analysis to balance
performance and false positives.
Limitations.
We discuss two limitations of
JDD
: (i) per-
formance of dynamic analysis, and (ii) implicit constraints.
First, while
JDD
signicantly improves the performance of
static analysis, the fuzzing part of dynamic analysis may
still have performance issues during mutation, particularly
when the number of false positives from static analysis is
large for some Java applications due to over-approximation.
The main reasons for such false positives are that our points-
to analysis is lightweight, leading to imprecisions in many
cases, and our path sensitivity is restricted inside invocation
handlers of dynamic proxies, i.e., the analysis outside is
path insensitive. Second, while
JDD
considers some implicit
constraints, such as the nullpointer exceptions and forced
type casting, there are still other implicit constraints that
need to be solved during exploit generation.
7. Related Work
We describe both attacks and defenses related to dese-
rialization vulnerabilities.
7.1. Deserialization Vulnerability Mining
In recent years, a substantial body of research [22]–[24]
has been devoted to the automated mining of deserialization
vulnerabilities using both static and dynamic methods.
GadgetInspector [3] is one of the most well-known
automated gadget chain mining tools. It utilized static taint
analysis to discover execution paths from manually dened
source points to sink points. However, its effectiveness is
limited in intricate scenarios due to inherent design limi-
tations in data-ow and control-ow analysis. Chen et al.
proposed Tabby [25], which utilizes Soot [11] to transform
Java programs into Code Property Graphs (CPG) [26]–
[29] and imports them into Neo4j database [30]. Then,
they extract gadget chains through querying CPG, using
manually crafted Cypher [31] statements. These approaches
commonly demand signicant expertise in deserialization
vulnerabilities, thus constraining their scalability. Compared
with them, during static analysis,
JDD
do not rely on domain
knowledge about JOI vulnerabilities. It only leverages the
understanding of Java dynamic features to identify gadget
fragments and link them together. Moreover,
JDD
also de-
signs a novel bottom-up approach to greatly improve the
efciency of its static module.
Considering that static analysis often introduces numer-
ous false positives, SerHybrid [4] proposed to automate
the verication of exploitable gadget chains through the
construction of heap abstractions for generating injection
objects. Building upon Tabby, GCMiner [1] incorporated
an overriding-guided object generation strategy to automate
verication during fuzzing. And ODDFuzz [2] utilized di-
rected fuzzing to enhance verication efciency. In addi-
tion, black-box scanning tools like Marshalsec [32] and
Java Deserialization Scanner [33] have also been proposed.
Compared with them,
JDD
guides fuzzing by recognizing
data-ow dependencies between injection objects' elds. On
one hand, this approach enables the inference of complex
injection object structures, such as parallel and embedded
injection object, which were commonly uncovered in pre-
vious work. Furthermore,
JDD
signicantly improves seed
mutation's efciency by considering constraints from the
program's execution ow specied by gadget chains. It is
noteworthy that, to the best of our knowledge,
JDD
is the
rst tool capable of automatic generation of exploitable
injection objects based on gadget chains.

--- page 24 ---

7.2. Deserialization Vulnerability Defense
Implementing effective strategies to enhance application
security is often necessary, particularly in the context of
defense against deserialization vulnerabilities [34]. Exist-
ing strategies are commonly referred to as look-ahead de-
fenses [35], wherein an audit is conducted on classes that
require deserialization, and only those that are permitted can
be deserialized. One notable look-ahead defense is JEP290
[36], which offers a blacklist of prohibited malicious classes
during deserialization, along with interfaces for user exten-
sions. In addition to the JDK's built-in standard solutions,
Runtime Application Self-Protection (RASP) [37] frame-
works [38] [39] are frequently employed to defend against
deserialization vulnerabilities. These frameworks leverage
bytecode instrumentation tools to intercept risky APIs for
auditing. Some work also concentrate on automating the
generation of deserialization strategies. Trusted [40] is a
two-phase defense framework that learns from benign dese-
rialization workloads to create an allowlist, which is then en-
forced during the deserialization process. Another approach
by Franc¸ois et al. [41] involves training a Markov chain
with malicious Gadget Chains, which is then used to predict
malicious Injection Objects at runtime.
In summary, this thread of work commonly enforce
security checks on risky sources, sinks, and gadgets used in
Java deserialization. Compared with them,
JDD
focuses on
another important research problem – mining risky sources,
sinks, and gadgets that could be abused as much as possible.
Thus, the output of
JDD
can signicantly support them. Take
the white list adopted by Trusted as an example.
JDD
could
check if the classes in the white list are enough to construct
gadget chains. Another example is RASP based approach.
Their efciencies highly depend on the completeness of
risky sink points, and
JDD
could help to verify if specic
methods could be exploited by injection objects and thus
should be protected.
8. Conclusion
In this paper, we design a novel, scalable approach
for automated detection and verication of JOI vulnerabil-
ities, called
JDD
. On one hand,
JDD
solves the static path
explosion problem by a bottom-up approach, which rst
looks for gadget chain fragments and then chains gadget
fragments from sinks to sources. The approach reduces
static search time from exponential to polynomial, i.e., from
O
ˆ
eM
n
�
to
O
ˆ
M
2
n
3

enM
�
, where
n
is the number of
dynamic function calls in a gadget chain,
M
is the average
number of dynamic function call candidates, and
e
is the
number of entry points. On the other hand,
JDD
constructs
a so-called Injection Object Construction Diagram (IOCD),
which models the data-ow dependencies between injection
objects' elds to facilitate dynamic fuzzing. Our evaluation
of
JDD
upon six real-world Java applications reveals 127
zero-day, exploitable gadget chains with six being assigned
with Common Vulnerabilities and Exposures (CVE) identi-
ers. We also responsibly reported these vulnerabilities to
application developers and obtained their acknowledgments
and conrmations.
Acknowledgments
We would like to thank the anonymous reviewers for
their insightful comments that helped improve the qual-
ity of the paper. This work was supported in part by
the National Key Research and Development Program
(2021YFB3101200), National Natural Science Foundation
of China (62172104, 62172105, 61972099, 62102093,
62102091), and National Science Foundation (NSF) (CNS-
21-54404 and CNS-20-46361). Yuan Zhang was supported
in part by the Shanghai Rising-Star Program under Grant
21QA1400700 and the Shanghai Pilot Program for Basic
Research - FuDan University 21TQ1400100 (21TQ012).
Dr. Yinzhi Cao was supported in part by Johns Hopkins
Catalyst Awards and DARPA Young Faculty Award under
Grant Agreement D22AP00137-00 as well as a gift from
Visa Research. Min Yang is the corresponding author, and
a faculty of Shanghai Institute of Intelligent Electronics &
Systems and Engineering Research Center of Cyber Security
Auditing and Monitoring.
References
[1] S. Cao, X. Sun, X. Wu, L. Bo, B. Li, R. Wu, W. Liu, B. He,
Y. Ouyang, and J. Li, “Improving java deserialization gadget chain
mining via overriding-guided object generation,” inIEEE/ACM45thInternationalConferenceonSoftwareEngineering(ICSE), 2023, pp.
397–409.
[2] S. Cao, B. He, X. Sun, Y. Ouyang, C. Zhang, X. Wu, T. Su,
L. Bo, B. Li, C. Ma, J. Li, and T. Wei, “Oddfuzz: Discovering java
deserialization vulnerabilities via structure-aware directed greybox
fuzzing,” inIEEESymposiumonSecurityandPrivacy(SP), 2023,
pp. 2726–2743.
[3] I. Haken, “Automated discovery of deserialization gadget chains,”ProceedingsoftheBlackHatUSA, vol. 48, 2018.
[4] S. Rasheed and J. Dietrich, “A hybrid analysis to detect java se-
rialisation vulnerabilities,” inProceedingsofthe35thIEEE/ACMInternationalConferenceonAutomatedSoftwareEngineering, 2020,
pp. 1209–1213.
[5] Ysoserial. https://github.com/frohoff/ysoserial.
[6] Sofa-rpc. https://github.com/sofastack/sofa-rpc.
[7] https://github.com/apache/dubbo-hessian-lite.
[8] https://github.com/sofastack/sofa-hessian.
[9] G. Fourtounis, G. Kastrinis, and Y. Smaragdakis, “Static analysis of
java dynamic proxies,” inProceedingsofthe27thACMSIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis, 2018,
pp. 209–220.
[10] Y. Li, T. Tan, and J. Xue, “Understanding and analyzing java reec-
tion,”ACMTransactionsonSoftwareEngineeringandMethodology(TOSEM), vol. 28, no. 2, pp. 1–50, 2019.
[11] Soot. https://github.com/soot-oss/soot.
[12] S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein,
Y. Le Traon, D. Octeau, and P. McDaniel, “Flowdroid: Precise
context, ow, eld, object-sensitive and lifecycle-aware taint analysis
for android apps,”AcmSigplanNotices, vol. 49, no. 6, pp. 259–269,
2014.

--- page 25 ---

[13] R. Padhye, C. Lemieux, and K. Sen, “Jqf: Coverage-guided property-
based testing in java,” inProceedingsofthe28thACMSIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis, 2019,
pp. 398–401.
[14] R. Padhye, C. Lemieux, K. Sen, M. Papadakis, and Y. Le Traon, “Se-
mantic fuzzing with zest,” inProceedingsofthe28thACMSIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis, 2019, pp.
329–340.
[15] Asm. https://asm.ow2.io/.
[16] Hessian protocol. https://en.wikipedia.org/wiki/Hessian(Webserviceprotocol).
[17] T3 protocol. https://docs.oracle.com/cd/E1457101/web.1111/
e13721/rmit3.htm#WLRMI143.
[18] Iiop protocol. https://www.ibm.com/docs/en/iad/7.2.1?topic=i-
internet-inter-orb-protocol-iiop.
[19] Github. https://github.com/.
[20] Jackson. https://github.com/FasterXML/jackson.
[21] Oracle weblogic server. https://www.oracle.com/java/weblogic/.
[22] S. Park, D. Kim, S. Jana, and S. Son, “
˜
FUGIO
�
: Automatic ex-
ploit generation for
˜
PHP
�
object injection vulnerabilities,” in31stUSENIXSecuritySymposium(USENIXSecurity22), 2022, pp. 197–
214.
[23] M. Shcherbakov and M. Balliu, “Serialdetector: Principled and prac-
tical exploration of object injection vulnerabilities for the web,”
inNetworkandDistributedSystemsSecurity(NDSS)Symposium202121-24February2021, 2021.
[24] S. Cristalli, E. Vignati, D. Bruschi, and A. Lanzi, “Trusted execu-
tion path for protecting java applications against deserialization of
untrusted data,” inResearchinAttacks,Intrusions,andDefenses:21stInternationalSymposium,RAID2018,Heraklion,Crete,Greece,September10-12,2018,Proceedings21. Springer, 2018, pp. 445–
464.
[25] Z. J. Y. F. X. L. X. F. X. Chen, B. Wang and Q. Liu, “Tabby: Auto-
mated gadget chain detection for java deserialization vulnerabilities,”
2023.
[26] “Code property graph - Wikipedia — en.wikipedia.org,” https://en.
wikipedia.org/wiki/Codepropertygraph, [Accessed 04-08-2023].
[27] M. Martin, B. Livshits, and M. S. Lam, “Finding application errors
and security aws using pql: a program query language,”AcmSigplanNotices, vol. 40, no. 10, pp. 365–383, 2005.
[28] F. Yamaguchi, N. Golde, D. Arp, and K. Rieck, “Modeling and
discovering vulnerabilities with code property graphs,” in2014IEEESymposiumonSecurityandPrivacy. IEEE, 2014, pp. 590–604.
[29] M. Backes, K. Rieck, M. Skoruppa, B. Stock, and F. Yamaguchi,
“Efcient and exible discovery of php application vulnerabilities,” in2017IEEEeuropeansymposiumonsecurityandprivacy(EuroS&P).
IEEE, 2017, pp. 334–349.
[30] neo4j. https://neo4j.com/.
[31] Cypher. http://opencypher.org/.
[32] marshalsec. https://github.com/mbechler/marshalsec.
[33] Java deserializer sanncer. https://github.com/federicodotta/Java-
Deserialization-Scanner.
[34] “CWE - CWE-502: Deserialization of Untrusted Data (4.12) —
cwe.mitre.org,” https://cwe.mitre.org/data/denitions/502.html, [Ac-
cessed 04-08-2023].
[35] R. Seacord, “Combating java deserialization vulnerabilities with look-
ahead object input streams (laois),”NCCGrWhitepaper, 2017.
[36] jeps290. https://openjdk.org/jeps/290.
[37] Z. L. Z. Yin and Y. Cao, “A web application runtime application self-
protection scheme against script injection attacks,” p. 566–577, 2018.
[38] openrasp. https://github.com/baidu/openrasp.
[39] P.

Cisar and S. M.

Cisar, “The framework of runtime application self-
protection technology,” in2016IEEE17thInternationalSymposiumonComputationalIntelligenceandInformatics(CINTI), 2016, pp.
000 081–000 086.
[40] D. B. S. Cristall, E. Vignati and A. Lanzi, “Trusted execution path
for protecting java applications against deserialization of untrusted
data,”ResearchinAttacks,Intrusions,andDefenses,M.Bailey,T.Holz,M.Stamatogiannakis,andS.Ioannidis,Eds.Cham:SpringerInternationalPublishing, pp. 445–464, 2018.
[41] F. Gauthier and S. Bae, “Runtime prevention of deserialization
attacks,” inProceedingsoftheACM/IEEE44thInternationalConferenceonSoftwareEngineering:NewIdeasandEmergingResults. New York, NY, USA: Association for Computing
Machinery, 2022, p. 71–75. [Online]. Available: https://doi.org/10.
1145/3510455.3512786
[42] “Cauchy–Schwarz inequality - Wikipedia — en.wikipedia.org,” https:
//en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarzinequality,
[Accessed 04-08-2023].
Appendix A.
Time Complexity of Bottom-up and Top-down
Approaches
A.1. Proof of Theorem 1
Proof.
If there are
n
dynamic method invocations in a chain,
and the average number of candidates for these invocations
is
M
, the number of
source
is
e
. According to Lemma 1,
the search complexity for a source is
O
ˆ
n
3
M
2
�
.
As for each source, the maximum number of connection
checks is
nM
, and the overall search complexity of Algo-
rithm 1 to search for all sources is
O
ˆ
n
3
M
2

enM
�
.Lemma 1.
The per-entry search complexity of Algorithm 1
is
O
ˆ
M
2
n
3
�
, where
n
is the number of dynamic method
invocations, and
M
is the average number of candidates
for these invocations.
Proof.
In Algorithm 1,
n
œ
represents the number of distinct
dynamic method invocations, with each dynamic method
having
x
1
,
x
2
, ...,
x
n
œ
, candidates, as difference groups,
and a total of
N

x
1

:::

x
n
œ
candidates. We can then
compute the searching complexity for Algorithm 1 through
the following three steps.
Y
Max Searching Times per Round
: By employing
a bottom-up search, it becomes possible to store the
exact input requirements connecting each fragment to
Sink Fragments
and avoid repeated searching. Mean-
while, there will not be two
Sink Fragments
with the
same dynamic method implementation serving as the
Head
. And the fragment with the candidate of the p-
th dynamic method invocation as the
Head
requires
checking for connections with a maximum of
N

x
p
other fragments. Considering these most complex sce-
narios, using equations (1) and (2), we can calculate

--- page 26 ---

the maximum number
S
of linkage detection attempts
during the search process.
x
1

x
2

:::

x
n
œ

N
@
Mn
(1)
S
p

x
p
ˆ
N

x
p
�
(2)
S

N
2

ˆ
x
2
1

:::x
2
n
œ
�
(3)
According to the Cauchy-Schwarz inequality [42], for
any real numbers
a
1
; a
2
; :::; a
n
and
b
1
; b
2
; :::; b
n
, we
have:
ˆ
a
2
1

a
2
2

:::

a
2
n
œ
�ˆ
b
2
1

b
2
2

:::

b
2
n
œ
�
A
ˆ
a
1
b
1

a
2
b
2

:::

a
n
œ
b
n
œ
�
2
(4)
When we set
a
1

x
1
; a
2

x
2
; :::; a
n
œ

x
n
œ
, and
b
1

b
2

:::

b
n
œ

1
, equation (4) is transformed into (5),
ˆ
x
2
1

x
2
2

:::

x
2
n
œ
�
A
ˆ
x
1

x
2

:::

x
n
œ
�
2n
œ

N
2n
œ
(5)
From equations (5) and (3), it follows that
S
@
N
2
ˆ
1

1n
œ
�
(6)
, and the maximum value of S is obtained when
x
1

x
2

:::

x
n

Nn
œ
.
Y
Searching Complexity
Since the search requires a
maximum of
n
œ
iterations, the overall algorithm's max-
imum number of search attempts is
n
œ
N
2
ˆ
1

1n
œ
�
@
n
œ
N
2
@
n
3
M
2
(7)
We dene the search complexity
O
ˆ
1
�
as a one-time
fragment linking check. Note that, after
JDD
identi-
es the fragments, it will merge the fragments whose
headers are the implementations of the same dynamic
method but meet the conditions based on the special
cases described in Appendix B. The complexity of this
step is O(N); Therefore, the nal maximum search
complexity is
O
ˆ
n
3
M
2

N
�
=
O
ˆ
n
3
M
2
�
for each
source
.A.2. Proof of Theorem 2
Proof.
All symbols follow the Theorem 1. Based on the
description in the ODDFuzz paper, when an attacker-
controllable dynamic method call is searched, all overridden
methods will continue to be searched. Therefore, under the
assumption of a search strategy that avoids false negatives
as much as possible, and also considers the computational
complexity in the worst case, conducting a DFS (Depth-
First Searching) for potential gadget chains from a
source
to a
sink
can be equivalent to detecting all paths of a tree
with depth
n
, and each node in the tree having an average
of
M
branches, starting from the root node, using the DFS
algorithm. The computational complexity of this process can
be determined accordingly.
Y
The notation O(1) is dened as follows: when the tree
is an empty tree (has no nodes) or consists of only one
node, the number of paths is 0 or 1 respectively. This
serves as the termination condition for the recursion.
The search complexity is denoted by S(1) = O(1).
Y
The recursive hypothesis.
Assuming that for a node
at a depth
d
in the tree, the searching complexity of
the Depth-First Search (DFS) algorithm is denoted by
S
ˆ
d
�
.
Y
The recursive step:
For a node at depth
d

1
, we
recursively invoke the DFS function to process its child
nodes. Each node can have
M
child nodes, so in the
worst case, the DFS function needs to be called
M
times for each child node located at depth
d

1
. Ac-
cording to the induction hypothesis, the DFS processes
nodes at depth
d

1
with a searching complexity of S(d-
1). Therefore, the time complexity to process a node at
depth d is
O
ˆ
M
�

S
ˆ
d

1
�
.
Based on the recursive relation, we can expand
S
ˆ
d
�

O
ˆ
M
�

S
ˆ
d

1
�

O
ˆ
M
2
�

S
ˆ
d

2
�

:::

O
ˆ
M
d
�

S
ˆ
0
�

O
ˆ
M
d
�
Therefore, for a single source, the search complexity
is
O
ˆ
M
n
�
, and when performing DFS searches from
e
entry points, the search complexity becomes
O
ˆ
eM
n
�
.Appendix B.
An analysis of historical gadget chains
We collected 79 gadget chains from well-known deseri-
alization vulnerability databases, including ysoserial, Mar-
shalSec, and 113 CVE reports of JOI vulnerabilities.
When studying these 79 gadget chains, we rst explored
which methods are typically chained after Java reection.
The results show that 39 of the 79 gadget chains use Java
reection, and they can all be summarized into two major
types. Specically, 27 chains use parameterless methods as
follow-up methods. Of these 27 chains, six require
getter
or
is
methods and four must be overridden methods of
interface methods. The remaining 12 chains use methods
with a parameter of type String or Boolean as follow-up
methods to unsafe reection. Therefore, we prioritize testing
the two types of successor methods in Section 3.3.
Then, among these 79 historical gadget chains, only
nine have the same dynamic method calls nested, and the
reasons for nesting the same dynamic method calls can be
attributed to two categories: (1) Implement chain calls of
Method.invoke
, sequentially calling insecure methods in

--- page 27 ---

the program to execute malicious instructions, such as CVE-
2020-2555. (2) Satisfy common specic strong constraints
- hash collision, such as the conditional constraints shown
in Line 7 in Figure 1. Therefore, we let
JDD
support both.
Appendix C.
Meta-Review
The following meta-review was prepared by the program
committee for the 2024 IEEE Symposium on Security and
Privacy (S&P) as part of the review process as detailed in
the call for papers.
C.1. Summary
This paper proposes
JDD
, a new framework to detect
Java deserialization vulnerabilities. The main focus in on
improving the efciency of the analysis. First, it mitigate the
path explosion problem by employing a bottom-up search
strategy to avoid redundancies in top-down approaches,
which reduce the time needed for static gadget chain search
from exponential time to polynomial time. Second, it uses
the Injection Object Construction Diagram (IOCD) to track
dependencies between data elds of the various injected
objects, which reduces the search scope. Third, it tracks
control dependencies during fuzzing to collect more ne-
grained progress feedback. Evaluation shows that the proto-
type tool is able to nd more deserialization gadget chains
than previous state-of-the-art approaches.
C.2. Scientic Contributions
Y
Provides a New Data Set For Public Use
Y
Creates a New Tool to Enable Future Science
Y
Provides a Valuable Step Forward in an Established
Field
C.3. Reasons for Acceptance
1) The paper is well-written
2) The paper tackles with an interesting and timely topic:
deserialization vulnerabilities in Java
3)
JDD
discovered 127 unknown deserialization chains in
6 real-world Java apps
4)
JDD
outperformed the previous state-of-the-art, in
terms of scalability and false negative rate
