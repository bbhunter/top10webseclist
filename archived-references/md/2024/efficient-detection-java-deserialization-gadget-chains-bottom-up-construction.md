---
type: Whitepaper
title: Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction
resource: "https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T22:35:19+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf"
    title: Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction
    author: Bofei Chen, Lei Zhang, Xinyou Huang, Yinzhi Cao, Keke Lian, Yuan Zhang, Min Yang
also_at: []
authors:
  - Bofei Chen
  - Lei Zhang
  - Xinyou Huang
  - Yinzhi Cao
  - Keke Lian
  - Yuan Zhang
  - Min Yang
canonical_url: ""
cited_by:
  - "2024.md:80"
commit: ""
content_sha256: bf9d778bd151ca2f6dd56d302fab1e988abc49f256f21f7c8628001e799dd4d2
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
retrieved_kind: manual-import
retrieved_utc: "2026-08-14T22:35:19+00:00"
slug: efficient-detection-java-deserialization-gadget-chains-bottom-up-construction
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction

**Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction** - Bofei Chen, Lei Zhang, Xinyou Huang, Yinzhi Cao, Keke Lian, Yuan Zhang, Min Yang, Publisher not stated.

- Published: date not stated
- Original: <https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf>
- Preserved from: https://secsys.fudan.edu.cn/_upload/article/files/8a/3c/d8d0e5a142dbbfaa39a58edc76b0/88ab6956-5447-4e4c-8ad8-6785c3fec057.pdf (manual-import) on 2026-08-14
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction

Efficient Detection of Java Deserialization Gadget Chains via Bottom-up Gadget
                   Search and Dataflow-aided Payload Construction

       Bofei Chen1 , Lei Zhang1∗ , Xinyou Huang1 , Yinzhi Cao2 , Keke Lian1∗ , Yuan Zhang1∗ , Min Yang1∗
                              1: Fudan University, {bfchen22, xinyouhuang22}@m.fudan.edu.cn
                          1∗: Fudan University, {zxl, kklian20, yuanxzhang, m yang}@fudan.edu.cn
                                      2: Johns Hopkins University, yinzhi.cao@jhu.edu


Abstract—Java Object Injection (JOI) is a severe type of              internal Java methods (called gadgets), finally achieving a
vulnerability affecting Java deserialization, which allows adver-     wide range of severe attack consequences, e.g., remote code
saries to inject a well-crafted, serialized object, thus triggering   execution (RCE) and denial of service (DoS) attacks.
a series of chained internal methods (called gadgets) and then            In past years, many works [1]–[4] have focused on the
achieving attack consequences such as Remote Code Execution           problem of JOI, and proposed several JOI vulnerability
(RCE). Prior works studied the problem of detecting and               detection techniques. For example, ODDFuzz [2] statically
chaining gadgets for JOI vulnerability using static search for        searches for possible gadgets via a Depth First Search (DFS)
possible gadget chains and dynamic construction of payload via        strategy, and then dynamically fuzzes the target program as
fuzzing. However, prior works face two following challenges:          a greybox for verifying gadget chains. However, existing
(i) path explosion in static gadget search and (ii) a lack of fine-   work still fell short in two major limitations, impacting their
grained object relations connected via object fields in dynamic       practicality and effectiveness.
payload construction.                                                     First, prior work often adopted a top-down static ap-
     In this paper, we design and implement a novel Java              proach for checking gadgets extensively from a source to a
deserialization gadget detection framework, called JDD. On            sink for potential paths. However, such a search often suffers
one hand, JDD solves the static path explosion problem by a           from path explosion, especially when common Java meth-
bottom-up approach, which first looks for gadget fragments            ods such as equals and put are involved in the gadget
and then chains gadget fragments from sinks to sources. The
                                                                      chain. For example, our experiment shows that the static
                                                                      analysis approach like ODDFuzz cannot finish analyzing a
approach reduces maximum static search time from exponen-
                                                                      small 3.6MB Java application. Fundamentally, the search
tial to polynomial, i.e., from O(eM n ) to O(M 2 n3 + enM ),
                                                                      complexity is exponential, i.e., O(eM n ), where n is the
where n is the number of dynamic function calls in a gadget
                                                                      number of dynamic function calls in a gadget chain, M is
chain, M is the average number of dynamic function call
                                                                      the average number of dynamic function call candidates, and
candidates, and e is the number of entry points. On the other
                                                                      e is the number of entry points.
hand, JDD constructs a so-called Injection Object Construction
                                                                          Second, many of prior tools conducted static analysis
Diagram (IOCD), which models the dataflow dependencies                against JOI vulnerability detection, thus inevitably having
between injection objects’ fields to facilitate dynamic fuzzing.      high false positives. Beyond these, ODDFuzz additionally
Our evaluation of JDD upon six real-world Java applica-               introduced dynamic fuzzing for reducing false positives.
tions reveals 127 zero-day, exploitable gadget chains with            However, ODDFuzz did not consider the constraints that
six Common Vulnerabilities and Exposures (CVE) identifiers            should be satisfied in each gadget. In particular, the fine-
assigned. We also responsibly reported these vulnerabilities to       grained data flows between different object fields in each
application developers and obtained their acknowledgments             gadget, leading to the imprecision of object structure and
and confirmations.                                                    thus an incorrect payload.
                                                                          In this paper, we design a novel gadget chain detection
1. Introduction                                                       framework, called JDD (Java Deserialization Vulnerability
                                                                      Detector), to statically detect possible gadget chains using a
    Java serialization and deserialization greatly facilitate         bottom-up approach and dynamically generate payloads, i.e.,
the cooperation and collaboration of different Java systems           exploitable injection objects, relying on dataflow relations
(e.g., server and client), allowing different Java programs           between object fields. JDD addresses the aforementioned
to conveniently exchange and share data and code. Despite             two challenges as follows.
their easiness and powerfulness, one well-known and serious               First, JDD addresses the path explosion challenge via a
security vulnerability faced in Java deserialization is an            bottom-up search strategy. JDD first searches for possible
implicit attack surface called Java Object Injection (JOI).           gadget fragments and then chains fragments together from
The JOI vulnerability enables a remote attacker to inject             sinks to sources. Our key observation here is that a top-down
a well-crafted serialized object, which triggers a chain of           search repeats the analysis of the same low-level gadget
fragment when a top-level gadget changes, leading to a              2.1. Background of JOI Attacks
huge redundancy and a waste of analysis time. Instead, the
bottom-up search adopted by JDD finds gadget fragments                   Java Naming and Directory Interface (JNDI) injection
that can be reused by different top-level gadgets in the chain.     is a commonly used technique in JOI attacks. The attack
Therefore, the search complexity changes from exponential           occurs because the JNDI interface’s lookup method can
to polynomial, i.e., from O(eM n ) to O(M 2 n3 + enM ).             remotely load a malicious Java class based on its param-
More importantly, JDD is able to reuse existing gadget frag-        eters (e.g., an attacker-controlled URL), thereby executing
ments discovered in previous vulnerabilities, which further         arbitrary code in the victim server. A typical scenario for this
speeds up the search process.                                       attack involves a web service running on the victim server,
    Second, JDD addresses the challenge of the lack of ob-          listening on a port and deserializing data received on the
ject field relations via a novel data structure, called Injection   port. During deserialization, if there is a JOI vulnerability,
Object Construction Diagram (IOCD), to better represent             the program execution will invoke some security-sensitive
the dataflow dependencies between injection objects’ fields.        methods based on the injected object.
The high-level idea is that JDD follows the call sequence                In addition to JNDI injection attacks, common meth-
in a statically-discovered gadget chain to construct dataflow       ods of exploiting JOI vulnerabilities to attack remote
dependencies between possible injection objects’ fields as an       servers include dynamic code loading (such as using
IOCD. Such an IOCD is further used by JDD in dynamic                URLClassLoader.loadClass to load remote class
fuzzing to exploit the JOI vulnerability.                           files or using ClassLoader.defineClass to directly
    We evaluate JDD upon six popular Java applications in           load bytecode files), and command execution (such as
their latest version, which finds 127 zero-day exploitable          Runtime.exec), etc. They all require: (1) An execution
gadget chains with six Common Vulnerabilities and Expo-             path that can invoke a security-sensitive method that can
sures (CVE) identifiers assigned. We also responsibly re-           execute malicious code (or upload arbitrary files, deny ser-
ported our findings of all 127 gadget chains to related devel-      vice, etc.) during the deserialization process, called gadget
opers and received their confirmation. For example, Dubbo’s         chain; (2) A serialized object that drives the execution of
developers not only acknowledged the gadget chains but also         the gadget chain, called injection object.
admitted that it is almost “impossible” for them to recognize            Thus, to detect JOI vulnerabilities, JDD has two major
all possible gadget chains, which emphasizes the urgency of         detection goals: (1) Uses static analysis to find potential
our automated tool.                                                 gadget chains in the victim server; (2) Dynamically gener-
    We also compare JDD with the state-of-the-art approach,         ates exploitable injection objects to verify the exploitability
namely ODDFuzz, in a well-known benchmark (i.e., the                of gadget chains. As a result, the exploitable gadget chains
ysoserial repository [5]) with 34 confirmed gadget chains.          detected by JDD can be used to help developers specify a
JDD missed only seven of 34 confirmed with a False Neg-             more complete blacklist defense mechanism to better defend
ative Rate (FNR) of 20.6% and identified 91 previously-             against JOI attacks.
unknown gadget chains (which were confirmed as correct in
manual analysis). As a comparison, OddFuzz only detected            2.2. A Motivating Example
16 gadget chains, resulting in an FNR of 52.9%, and it did
not discover any previously-unknown ones.                               Figure 1 illustrates a zero-day gadget chain found by
    We summarize the contributions of this paper as below:          JDD in sofa-rpc [6], i.e., popular Java libraries that
   ● JDD solves the path explosion problem of static search         are widely used in the server-side cloud of many enter-
      for chained gadgets via a bottom-up approach that dis-        prise companies, e.g., Alipay. The gadget chain starts from
      covers intermediate gadget fragments and then chains          a Java deserialization method (e.g., HashMap.put() in
      them together from sinks to sources.                          Line 4, shown in Figure 1). The chain ends up with a
   ● JDD constructs the so-called Injection Object Con-             Java reflection call at Line 54 and then launches a JNDI
      struction Diagram (IOCD) to better model dataflow             injection attack at Line 59. Note that each Java method
      dependencies between object fields and assist dynamic         call along the chain is considered as a gadget, e.g., the
      fuzzers for payload construction.                             put() method at Line 4. Then, Java method calls between
   ● JDD discovered 127 zero-day gadget chains of real-             two dynamically-dispatched methods are considered as a
      world Java applications in their latest version and out-      gadget fragment, e.g., the combination of methods get()
      performs ODDFuzz in detecting legacy gadget chains.           and getFromHashtable() in Figure 1 as Fragment IV,
                                                                    as the latter is statically determined. We also illustrate the
2. Overview                                                         exploit code in Figure 2. An adversary serializes the returned
                                                                    object in Line 22 of Figure 2 and sends it to the server, which
   In this section, we first provide a brief background on          triggers the gadget chain in Figure 1 for exploitation.
JOI attacks in Section 2.1, then describe Java deserialization          We first describe the gadget chain with five different
gadget chains in Section 2.2 using a real-world motivat-            gadget fragments of Figure 1 in detail. The gadget starts
ing example, and then present research challenges faced             from Fragment I (Line 1), where the put() method (Line
by state-of-the-art approaches in detecting this example in         4) of an object HashMap is invoked upon deserialization.
Section 2.3.                                                        If two elements in the HashMap have the same hash value,
  1   /* Gadget Fragment I : HashMap.put()->HashMap.putVal() */                               1   // Gadget Fragment IV
  2     class HashMap extends AbstractMap ...{                                                2     UIDefaults uft = new UIDefaults();
  3        Node<K,V>[] table;                                                                 3   // Gadget Fragment V
  4        V put(K key, V value) { return putVal(hash(key), key, value, ...); }               4     Object plv = createWithObjectNoArgsConstructor(
  5        V putVal(int hash, K key, V value,...) { ...                                       5             Class.forName(“javax.swing.UIDefaults$ProxyLazyValue”));
  6            Node<K,V> p = table[(int) index]; // p is an element in table                  6     uft.put(“aaa”, plv)
  7            if (p.hashCode() == key.hashCode() & p.key != key & key != null)               7    // Gadget Fragment VI
  8               key.equals(p.key);
                                                                                              8     setFieldValue(plv, “className”, “security-sensitive class name”);
  9       ... } n1              n2
                                                                     Candidates:2751
 10     }                                                                                     9     setFieldValue(plv, “args”, new Object[]{“malicious URL”});
 11    /* Gadget Fragment II: NodeImpl.equals()-> Object.equals(Line 17) */                  10     setFieldValue(plv, “methodName”, “security-sensitive method name”);
 12     class NodeImpl implements ... {                                                      11    // Gadget Fragment III
 13        Object key;                                                                       12     ConcurrentHashMap cctmap = new ConcurrentHashMap();
 14        int hashCode = -1;                                                                13     cctmap.put(“aaa”, “any”);
 15        boolean equals(Object obj) {                                                      14     // Gadget Fragment II
 16           if (o instanceof NodeImpl) { ...                                               15     NodeImpl n1 = createWithObjectNoArgsConstructor(NodeImpl.class);
 17               this.key.equals( ((NodeImpl) obj).key );                                   16     NodeImpl n2 = createWithObjectNoArgsConstructor(NodeImpl.class);
 18        }       cctmap                    uft
                                                                     Candidates:2751         17     setFieldValue(n1, “hashCode”, 3);
 19        int hashCode() {
 20               if (this.hashCode == -1) this.hashCode = this.buildHashCode();             18     setFieldValue(n2, “hashCode”, 3);
 21               return this.hashCode;                                                      19     setFieldValue(n1, “key”, cctmap);
 22     }                                                                                    20     setFieldValue(n2, “key”, uft);
 23    /* Gadget Fragment III: ConcurrentHashMap.equals()-> Map.get() */                     21     // Gadget Fragment I
 24     class ConcurrentHashMap<K,V> extends AbstractMap<K,V> ...{                           22     HashMap map = Gadgets.makeMap(n2, n1); // put n1 and n2 into a HashMap
 25        boolean equals(Object o) {
 26            if (o instanceof Map) { ...                                                   Figure 2: Exploit Code of Our Motivating Example in
 27               ((Map<?,?>)o).get(ConcurrentHashMap.this.table[index].key);
 28            ...}} uft                                   cctmap.table[i].key               Figure 1 (An adversary serializes the returned object in Line
 29   Candidates:148                                                                         20 and sends it to the server).
 30    }
 31   /* Gadget Fragment IV: UIDefaults.get()-> ... -> LazyValue.createValue() */
 32    class UIDefaults extends Hashtable<Object,Object>{
 33       Object get(Object key) { Object value = getFromHashtable( key ); ...}              ment IV, which further calls the getFromHashtable()
 34       Object getFromHashtable(final Object key) {             cctmap.table[i].key
 35         // UIDefaults.table should contain an Entry that “key” is key
                                                                                             method (Line 34). Lastly, the createValue() method
 36         Object value = super.get(key); cctmap.table[i].key                               calls at Line 39 invokes the polymorphic method definition
 37         if ((value != PENDING) && !(value instanceof ActiveValue) &&                     in Line 51 belong to Fragment V, which calls Java reflection
 38             !(value instanceof LazyValue)) return value;
 39         if (value instanceof LazyValue) ((LazyValue) value).createValue(this);           at Line 54 and thus the JNDI attack at Line 59 of Fragment
 40       }                                                   plv                uft         VI.
 41    }
 42    class Hashtable<K,V> ... {
                                                                                                 Next, we describe how an adversary utilizes the gadget
                                                                             Candidates:12
 43       Entry<K,V>[] table;                                                                chain with the exploit code in Figure 2. An adversary first in-
 44       V get(Object key) {                                                                stantiates a HashMap object at Line 22 of Figure 2 to trigger
 45          Entry<K,V> e = this.table[(int) index]; // e is an element of table
 46          if ((e.key.hash == key.hash) && e.key.equals(key)) return (V) e.value;          the put() method of Fragment I. Then, two NodeImpl
 47          return null; } cctmap.table[i].key                                   plv        objects are instantiated with the same hashCode (Lines
 48    }
 49   /* Gadget Fragment V: ProxyLazyValue.createValue()->...-> Method.invoke() */
                                                                                             15–18 of Figure 2) so that the equals() method in
 50    class ProxyLazyValue extends Hashtable<Object,Object> {                               Fragment II is invoked. Next, the adversary assigns n1.key
 51       Object createValue(final UIDefaults table) {...                                    as a ConcurrentHashMap object (Lines 12–13 and 19
 52          Class c = Class.forName(this.className);
 53          Method m = c.getMethod(this.methodName, this,args);                             of Figure 2) to trigger another equals() method in
 54          return MethodUtil.invoke(m, c, this.args); ...}                                 Fragment III. After that, the adversary assigns n2.key
 55    }                                      plv.args
 56   /* Gadget Fragment VI: InitialContext.doLookup()-> InitialContext.lookup() */
                                                                                             as a UIDefaults object (Lines 2 and 20 of Figure 2)
 57    class InitialContext implements Context {                                             to trigger the get() method in Fragment IV. Lastly, the
 58       static <T> T doLookup(String name) throws NamingException {                        adversary manipulates the elements stored in uft.table
 59          return (T) (new InitialContext()).lookup(name); // JNDI attack }
 60    }                                             plv.args                                to return a ProxyLazyValue object (Line 6 of Fig-
                                                                                             ure 2), which implements LazyValue interface with three
Figure 1: A Motivating Example of a Zero-day Gadget                                          values to trigger Fragment V. Specifially, the adversary
Chain with Five Fragments (Note that code is simplified                                      assigns the method InitialContext.doLookup() as
for easy understanding.)                                                                     the className and the methodName together with the
                                                                                             correct args (Lines 8–10 of Figure 2) to trigger Fragment
                                                                                             VI.
the equals() method (Line 8) will be invoked, which may
have a polymorphic implementation in NodeImpl class,                                         2.3. Challenges and Solution Overview
thus triggering Fragment II (Line 10). Then, the field key
of the NodeImpl class triggers another equals() method                                           We now describe two challenges faced by prior works
(Line 17), which may have a polymorphic implementation in                                    in their static and dynamic analysis using the motivating
the ConcurrentHashMap class, thus triggering Fragment                                        example presented in Figure 1. Then, we present the solu-
III (Line 25). Next, the get() method has a polymorphic                                      tions proposed by us in designing JDD to solve these two
implementation in the UIDefaults class, leading to Frag-                                     challenges.
                     HashMap                                         HashMap                as embedded or parallel objects. Figure 3 (a) shows the
                                                                                            injection object structure for our motivating example in
                        table                                          table                Figure 1. UIDfaults and ConcurrentHashMap are
            n2                         n1
                                                ...                                   ...   two keys under NodeImpl objects in a correct payload.
           NodeImpl               NodeImpl                          NodeImpl
                                                                                            However, prior works, such as ODDFuzz, only consider the
             key                    key                                 key                 class hierarchy inferred from the gadget chain and therefore
      uft                                   cctmap
                                                                                            they will generate a wrong object structure as shown in
           UIDfaults       ConcurrentHashMap                    ConcurrentHashMap
                                                                                            Figure 3 (b) because the get() method of UIDfaults
             table                  table                              table                is invoked after ConcurrentHashMap.
    plv
    ProxyLazyValue                                                   UIDfaults
                                                                                            Our Solution: Dataflow-aided Construction of Injection
                                                                                            Object Construction Diagram (IOCD). Our key obser-
                   Constraints Info
   i. n1.hashCode() == n2.hashCode()                                   table                vation is that different injection objects, e.g., their fields,
  ii. uft.containsKey(cctmap.table[i].key) == true                                          are connected via dataflows. Specifically, two dotted lines
 iii. Class.forName(plv.className)                               ProxyLazyValue             in different colors of Figure 1 show such two dataflows.
            .getMethod(plv.methodName,plv.args) != null
 iv. ...                                                                                    key (Line 8) flows to this.key (Line 17) and then
           (a) Correct Injection Object                   (b) Erroneous Injection Object    this.table[index].key (Line 27); then, p.key
                    Structure                             Structure Deduced by Oddfuzz      (Line 8) flows to ((NodeImpl) obj).key (Line 17)
                     Class Node                  Field Node
                                                                        Class-Field         and then (Map<?,?>)o (Line 27). Therefore, JDD infers
                                                                        Dependence          that there are two NodeImpl objects and UIDfaults
Figure 3: Injection Object Structure of Motivation Example.                                 is under the key of one NodeImpl object instead of
                                                                                            the table of ConcurrentHashMap. More specifically,
                                                                                            JDD constructs an IOCD like Figure 3 (a) following such
                                                                                            dataflows, which can be used for follow-up fuzzing.
Challenge I: Static Path Explosion. The first challenge
is that the number of all possible paths between sources
and sinks is exponential, leading to path explosion. Let
                                                                                            3. Design
us use Figure 1 as an example to describe the challenge.                                       In this section, we describe the system architecture of
The number of potential candidates for the equals()                                         JDD and then the detailed steps.
method between Fragments I and II could be 2,751 and
the same applies to the other equals() method between                                       3.1. System Architecture
Fragments II and III. Then, the candidate number is 148
for get() between Fragments III and IV, and 12 for                                               We show an overview of JDD ’s architecture with two
createValue() between Fragments IV and V. Therefore,                                        main stages in Figure 4. In Stage I, JDD detects possible
if a Depth-first-search (DFS) is used to find a gadget chain                                gadget chains and then in Stage II, JDD generates injection
like what ODDFuzz does, the total number execution path                                     objects to exploit the detected gadget chains for validation.
could be 2751×2751×148×12 = 13,440,769,776, which is                                        Specifically, there are five steps. In Step 1, JDD identifies
impossible to search from.                                                                  deserialization entry points. Then, in Step 2, JDD starts from
Our Solution: Bottom-up Gadget Search. Our key obser-                                       entry points to identify gadget fragments with static analysis.
vation is that a top-down search like a DFS will analyze                                    After that, JDD links gadget fragments to construct gadget
some methods multiple times, leading to redundancies. For                                   chains using a bottom-up approach, which finishes Stage 1
example, one get() method candidate between Fragments                                       with possible gadget chains. Next, in Step 4, JDD constructs
III and IV may be analyzed once for one equals()                                            Injection Object Construction Diagram (IOCD) based on the
method candidate between Fragments II and III and then                                      injection object related constraints. Lasty, in Step 5, JDD
again for another candidate between Fragments II and III.                                   utilizes IOCD-enhanced directional Fuzzing to verify gadget
Instead, JDD analyzes all possible gadgets between sources                                  chains’ exploitability.
and sinks once and forms them into gadget fragments. Then,                                       We now describe how each step works for our mo-
JDD adopts a bottom-up search from the sink to the source,                                  tivating example. Here is Stage I. First, in Step 1, JDD
which chains all the fragments into a chain. Specifically,                                  starts with identifying the entry points in sofa-rpc [6],
JDD only needs to analyze (12 + 2751 + 148) = 2,911                                         and then use them as the sources to begin our static taint
program execution paths and at most (2911 × 2911 - 2751                                     analysis. Second, in Step 2, JDD traverses the control- and
× 2751 - 148 ×148 - 12 × 12) × 2 + 2751 = 1,770,495                                         data-flow graph of the target program starting from each
times fragment linking check for our motivating example in                                  source (i.e., entry points in the beginning) until a dynamic
Figure 1, which is only 0.01% of the top-down approach,                                     method invocation and considers this as a fragment. Then,
significantly reducing the static gadget search space.                                      JDD treats the implementation of the dynamic method as
                                                                                            the new source until the next dynamic method invocation
Challenge II: Parallel and Embedded Injection Object                                        and considers code in between as a new fragment. During
Structure. The second challenge is that the payload, i.e.,                                  this process, JDD identifies some gadget fragments con-
the injection object, may have complex structures, such                                     taining a sink, e.g., MethodUtil.invoke() in Gadget
Fragment V. Then, in Step 3, JDD uses this fragment to                       Table 1: Popular Deserialization Protocols
find the gadget fragment IV that has a dynamic method                                                        Supported       Unserializable
                                                                      Protocol          Entry Points
invocation LazyValue.createValue() and the object                                                          Dynamic Feature   Class Support
                                                                                          readObject()
value that is used to invoke the createValue() method                                 readObjectNoData()
                                                                                                            Polymorphism
based on previous taint analysis result. Next, JDD uses the             JDK                                   Reflection          NO
                                                                                         readResolve()
                                                                                                                Proxy
Gadget Fragment IV as the new start to find the Gadget                                   readExternal()
                                                                                          readObject()
Fragment III and repeats this procedure until it reaches a                                                  Polymorphism
                                                                                      readObjectNoData()
                                                                       T3/IIOP                                Reflection          NO
source point, resulting in a gadget chain. After chaining the                            readResolve()
                                                                                                                Proxy
                                                                                         readExternal()
gadget fragments I-V, to complete the gadget chain, JDD                                    Map.put()        Polymorphism
                                                                       Hessian                                                   YES
will independently gather potential fragments that could                                    toString()        Reflection
                                                                                                            Polymorphism
execute remote attacker-controlled code, for example, the          Hessian-lite [7]       Map.put()
                                                                                                              Reflection
                                                                                                                                  NO
gadget fragments VI which contains a JNDI capability. Since        Hessian-sofa [8]
                                                                                          Map.put()         Polymorphism
                                                                                                                                 YES
                                                                                          toString()          Reflection
the gadget fragment V has a reflection capability and the                                                   Polymorphism
                                                                                         readObject()
parameter is controlled by the attacker, JDD would further            XStream
                                                                                          Map.put()
                                                                                                              Reflection         YES
                                                                                                                Proxy
connect it to the gadget fragment VI.
    We then describe Stage II. In Step 4, JDD extracts the
constraints for gadget chain chaining, which include (1)          3.3. Step 2: Identifying Gadget Fragments with
structured constraints (i.e. the class hierarchy relationships    Static Taint Analysis
between object and field instances), (2) field dependency
constraints (e.g., the hash code of n1.key and n2.key should          In this step, JDD detects useful gadget fragments that
be the same for our example), and (3) conditional branches.       could be chained together to construct gadget chains from
Note that JDD labels constraints shared by different execu-       entry points using static analysis. There are two substeps: (i)
tion paths as dominator, meaning that they are required by        gadget fragment formation and (ii) data-flow analysis within
all the execution paths. After extracting these constraints,      a fragment. First, JDD starts from each source, i.e., en-
JDD uses a novel data structure, termed Injection Object          try points or implementations of previous dynamic method
Construction Diagram (IOCD) to model dataflow depen-              invocation, until the next dynamic method invocation and
dencies between object fields and guide dynamic fuzzing.          treats code in between as a fragment. Second, JDD also
Lastly, in Step 5, JDD instruments the collected constraints      performs a data-flow analysis to record taint propagation
of the target program and uses the number of covered domi-        from the parameters of the first method in the fragment.
nator constraints to guide the fuzzing for generating an injec-   Specifically, we design a fragment-based summary that,
tion object that can exploit this gadget chain. Specifically,     for each gadget fragment, records the pollution behavior
JDD first initializes an instance object based on the class       between its first method and the last method parameters and
hierarchy in the IOCD graph. Then, for assigning adequate         maintains a sink-reachable condition record. Our purpose of
value for each field in the object, JDD utilizes a constraint     converting inter-procedure analysis of methods into jumps
solver to solve the dominator constraints. Then, JDD uses         between gadget fragments is to flexibly simulate dynamic
this object as the seed to drive the directional fuzzing          method invocations and reduce the computational complex-
and uses the number of covered dominator constraints to           ity of inter-procedure searches.
evaluate its energy.                                                  Next, we first describe the definitions of gadget frag-
                                                                  ments and then a classification of gadget fragments.
                                                                  Gadget Fragment Definition. A gadget fragment is a
3.2. Step 1: Identifying Deserialization Entry                    straight-line gadget sequence (i.e., methods could be exe-
Points                                                            cuted in Java deserialization), and its execution starts from
                                                                  the fragment’s head to its endpoint. For each fragment, its
                                                                  endpoint commonly is a security-sensitive method or a dy-
    The first step of our analysis is to identify the entry       namic method invocation that points to another fragment, for
points of deserialization in a given Java program. JDD ex-        example, Object.equals() could connect to almost all
tract such entry points from both the deserialization methods     the method “equals()” implemented by any class. During de-
of Java language and popular Java deserialization protocols       serialization, this kind of dynamic method invocation indeed
as shown in Table 1. There are two categories of entry meth-      introduces many possibilities of the program’s execution
ods: (i) deserialization methods provided by Java language,       direction, thus they work like the jump/goto instructions.
e.g., readObjectNoData(), readExternal() and                          In detail, the methods in a gadget fragment have:
readObject(), and (ii) interfaces provided by popular                ● Head, which is the entry method of this fragment
Java deserialization protocols, e.g., Map.put() for Hes-                and there exist some dynamic method invocations that
sian protocol. Note that since many of these entry points               could jump to this method.
are defined as interfaces, JDD further identifies and analyzes       ● End, which is the exit method of this fragment and
their overridden or implementation methods as the entry                 commonly a dynamic method invocation or security-
points.                                                                 sensitive method.
              1 Identify Entries   2   Identify Fragments              3 Link Fragments            4   Generate IOCD               5   Validate Exploitability

                   Entry                 Gadget                           Gadget                       Constrains                     Injection Object
                  Points                                                 Fragments        Gadget       Collection                  Generation & Mutation
                                        Fragments                                         Chains
  Target       Identification           Searching                         Linking                                                                      Dominator
Application                                                                                                                            Injection
                                                                                                                                                    Constraints-based
                                                                                                                                        Object
                                                                                                                                                       Feedback
                                         Reusable           Fragment
                                        Fragments                                                        IOCD                         Fuzzing-based
                                        Extraction          Data Set                                   Generation      IOCD       Exploitability Validation
 Exploits

                                                                                                                                  New Exploitable Injection Object
                             Stage I: Gadget Chain Detection                                             Stage II: Exploitable Injection Object Generation

                                            Figure 4: The Overall Architecture of JDD with Two Stages.


   ●   Other gadgets, which are non-dynamic methods and                               3.4. Step 3: Linking Gadget Fragments to Con-
       executed in sequence during deserialization to connect                         struct Gadget Chains using a Bottom-up Approach
       the head and end.
                                                                                          Upon completing the search of gadget fragments, JDD
Dynamic Method Invocation Types for Gadget Frag-                                      performs a bottom-up search to chain fragments together,
ments. There are the following three types of dynamic                                 thereby constructing all potential gadget chains as shown in
method invocations in gadget fragments:                                               Algorithm 1. First, JDD obtains three types of fragments: (1)
   ● Polymorphic: JDD recognizes the inheritance hierarchy                            Source Fragments, whose head is a source, e.g., the Gadget
     of the target program’s classes and identifies the over-                         Fragment I in Figure 1; (2) Free-State Fragments, which
     ridden methods. Then, when a method in a parent class                            records method exection sequence between two dynamic
     is invoked, JDD connects it to the corresponding over-                           method invocations, e.g., the Gadget Fragments II-IV in
     ridden methods implemented by its child classes. For                             Figure 1; (3) Sink Fragments, whose end is a sink, e.g.,
     example, considering a class B that overrides method                             Fragments V, VI in Figure 1. Then, JDD constructs potential
     ”m” of class C, any fragment, where End is C.m(),                                gadget chains by chaining Sink Fragments with Free-State
     could jump to other fragments, where Head is B.m().                              Fragments and then Source Fragments with the following
   ● Dynamic Proxy [9]: Java language supports objects                                steps. Note that JDD needs to consider taint requirements
     under type interface, Object and other generic                                   and method invocation conditions corresponding to different
     types to be implemented as a dynamic proxy instance,                             dynamic features. For example, sink fragments commonly
     and when the instance invokes any method, it would                               require specific parameters should be controlled by attack-
     be redirected to a specific invocation handler, i.e., the                        ers. Then, when finding precursors for Sink Fragments,
     invoke() method implemented in this proxy. Such                                  JDD would iteratively check if the corresponding parameters
     handlers commonly deploy method routes based on the                              could be tainted.
     properties (e.g. method name) of the trigger method.                                 We now describe the details in Algorithm 1. First, JDD
     Thus, for each handler, JDD conducts a path-sensitive                            connects the Free-State Fragments that can transition to Sink
     analysis to understand its method routs for ensuring                             Fragments. As shown in Algorithm 1, during each round
     the trigger method will not connect to a wrong ex-                               (Line 2–19), JDD traverses each fragment f ragf s in Free-
     ecution path in invocation handlers. In practice, JDD                            State Fragments. Based on the summary of f ragf s , JDD
     first identifies gadget fragments in all execution paths                         checks whether the linking conditions to sink fragments are
     inside an invocation handler and then labels the gadget                          satisfied. If so, f ragf s is added to newSinkFragments as
     fragments with corresponding method property require-                            the Sink Fragment (Line 8–9) for the next iteration, while
     ments based on their execution paths.                                            keeping track of the taint requirements to be satisfied for
   ● Reflection [10]: Unlike other dynamic features, Java                             the connection (merging them if they are identical to the
     reflection could invoke almost all methods imple-                                already recorded taint requirements) (Line 11). Since each
     mented in the program based on its parameters. JDD                               iteration can pick out all fragments that can potentially
     first checks if the reflection’s parameters are attacker-                        connect to the current sink fragments, the iteration process
     controlled (so that JOI can lead to RCE) and then                                terminates if there are no new Sink Fragments, i.e., when
     limits it to connect fragments that contain code ex-                             newSinkFragments is empty (Line 15–16) or reaching the
     ecution capabilities. Note that JDD allows reflection                            maximum number of search attempts. Next, the Source
     to connect any gadget in its successor fragments but                             Fragments are traversed, and the same approach is employed
     prefers two kinds of gadgets, based on the analysis of                           to detect connectable successor fragments, thereby obtaining
     existing gadget chains: (1) methods with no parameters,                          all potential gadget chains (Line 20–26).
     especially getter or is methods, and implementation of                               Lastly, assuming there are n′ distinct dynamic method
     interface methods, and (2) methods with one parameter                            invocations, let us explain why the upper limit for the
     of Boolean or String type.                                                       maximum number of iterations is n′ . If the number of
Algorithm 1 Gadget Fragments Linking                                                     linking, it will perform top-down class hierarchy infer-
Input: Sink Fragments Dataset Dsk                                                        ence according to the fragment connection sequence.
Input: Source Fragments Dataset Dsrc                                                     Specifically, for each gadget fragment, JDD first uses
Input: Free-state Fragments Dataset Df s
Output: Gadget Chain DataSet S                                                           dataflow analysis to determine which of its fields is
 1: // n′ is the number of distinct dynamic method invocations in context.               linked to the next fragment, and then uses the header
 2: for i ← 1 to n′ do
 3:     newSinkF ragments ← ∅                                                            method of the subsequent fragment to determine the
 4:     for f ragf s in Df s do                                                          actual type of the field. For example, in the Gadget
 5:         for f ragsucc in Dsk .getFragStartWith(f ragf s .end) do                     Fragment I in Figure 1, JDD finds the HashMap object
 6:              // Checking whether the taint requirements are satisfied
 7:              if isLinkable(f ragf s , f ragsucc ) then                               has a field table (Line 3) and table should store
 8:                  newSinkF ragments ← newSinkF ragments ∪ f ragf s                    two objects (i.e. n1, n2) based on the dataflow to Line
 9:                  Dsk .add(f ragf s )
10:                   // link f ragf s with f ragsucc and merge taint requirements       8. Another important problem here is to identify the
11:                   updateTaintRequirements(f ragf s , f ragsucc )                     exact class type of these fields, considering many of
12:               end if                                                                 them are defined as generic type or Object, e.g. the
13:          end for
14:      end for                                                                         key in Line 8, the field key of n1 and n2 (i.e. this.key,
15:      if newSinkF ragments == ∅ then                                                  obj.key) in Line 17, etc. To solve this problem, JDD
16:          break
17:      end if                                                                          continues the dataflow tracing and finds that the key
18:      Dsk ← newSinkF ragments                                                         connects Fragment I with II, and the header method
19: end for                                                                              of Fragment II is NodeImpl.equals. Thus, key
20: for f ragsrc in Dsrc do
21:      for f ragsucc in Dsk .getFragStartWith(f ragsrc .end) do                        should be a NodeImpl instance. Similarly, this.key
22:          if isLinkable(f ragsrc , f ragsucc ) then                                   and obj.key connect Fragment II with III and Fragment
23:               S ← S ∪ link(f ragsrc , f ragsucc )
24:          end if                                                                      III with IV, respectively. Therefore, JDD infers that
25:      end for                                                                         the field key of two NodeImpl instances, n1, n2 are
26: end for                                                                              ConcurrentHashMap and UIDefaults instances,
27: return S
                                                                                         as indicated by the header methods of successor Frag-
                                                                                         ment III and IV. Based on the approach, JDD ultimately
iterations exceeds n′ , the longest fragments will necessarily                           deduces the correct class hierarchy of the injection
contain candidates with two fragments whose ends are the                                 object as illustrated in Figure 3 (a).
                                                                                       ● Conditional branches related to fields, which exist in
same dynamic method. Since the attacker has the ability
to invoke any candidate with the same dynamic method,                                    the execution paths of the gadget chain, and note that
the attacker can directly supply the class implementation in                             JDD labels constraints shared by different execution
the latter call to the first to reduce the total length, so the                          paths as dominator meaning that they are required
path between two identical dynamic method invocations is                                 by all the execution paths. During the process of
redundant.                                                                               dataflow tracing, JDD concurrently collects conditional
                                                                                         branch constraints related to fields by identifying if the
Time Complexity. JDD reduces the static search time from                                 variables checked in the constraints could be tainted
O(eM n ) (i.e., those of state of the art, e.g., ODDFuzz [2])                            by fields. Moreover, to ensure the program execution
to O(M 2 n3 + enM ) according to Theorems 1 and 2 below.                                 would not trigger an exception, these exist several
Theorem 1. The search complexity of Algorithm 1 is                                       implicit constraints should be satisfied. For example, a
O(n3 M 2 +enM ), where n is the number of dynamic method                                 field could not be null when it invokes some methods.
invocations, M is the average number of candidates for                                   Another example is forced type casting, which requires
these invocations, and e is the number of entry points.                                  the field should be an instance of specific type.
                                                                                       ● Field dependency constraints, which encompass condi-
Proof. See Appendix A.1.                                                                 tional constraints among fields, i.e. the constraints i-iii
                                                                                         as shown in Figure 3. Note that sink points commonly
Theorem 2. The search complexity of ODDFuzz [2] is                                       require specific fields be controlled by the attacker
O(eM n ), where all notations follow Theorem 1.                                          to inject payloads. JDD would label these fields to
Proof. See Appendix A.2.                                                                 check if they can be tainted by input. To find field
                                                                                         dependency constraints, in general, JDD filters those
                                                                                         conditional constraints that affect multiple fields and
3.5. Step 4: Constructing IOCD based on Injection                                        then labels these fields with related constraints as field
Object related Constraints                                                               dependencies. Furthermore, JDD also considers specific
                                                                                         requirements for Java reflection. For example, the three
     There are two substeps here: (i) constraint extraction and                          fields className, methodName, and args used in
(ii) IOCD generation. First, JDD follows the call sequence                               Java reflection should ensure the target class contains
of this gadget chain to extract the execution paths, and then                            the target method.
uncovers three types of constraints that affect inputs:
    ● Class hierarchy relationships between object and field                            Second, after extracting these constraints, JDD uses
      instances. After JDD performs bottom-up fragment                               a novel data structure, termed Injection Object Construc-
tion Diagram (IOCD) to model the object structure and            existence of constraint dependencies between two fields,
dependencies of fields. There are two sub-steps. (i) JDD         JDD extracts dominator condition constraints from the rel-
treats the instantiated objects contained in a gadget chain      evant FieldNodes. These constraints are then solved using a
as ClassNodes. Each ClassNode stores the following infor-        constraint solver to find values that simultaneously satisfy
mation: the class name and the related FieldNodes, which         these constraints.
represent the fields that may be utilized during the deserial-
                                                                 Dependency-aware Seed Mutation. IOCD significantly
ization. The FieldNode, on the other hand, stores the relevant
                                                                 enhances the efficiency of fuzzing from the following three
constraint information for these fields and marks whether
                                                                 aspects: (1) Selecting appropriate fields for mutation; (2)
these constraints are statically determinable as dominator.
                                                                 Reducing the uncertain mutation space through constraint
(ii) Based on the structural constraints, the ClassNodes are
                                                                 information; (3) Considering fields dependencies and nested
interconnected through FieldNodes using directed edges,
                                                                 object structure. That is when mutating a field, the constraint
thereby indicating the hierarchical relationships between
                                                                 relationships between this field and other related fields or
instantiated objects. For example, in the motivation example,
                                                                 upper-level instance objects containing this field are consid-
JDD will construct ClassNodes representing the instances of
                                                                 ered. Detailed strategies can be found in Table 2.
NodeImpl, UIDfaults, and ConcurrentHashMap.
Then, following the structural constraints, JDD establishes          (i) Mutation based on condition constraints. Firstly,
edges from the UIDfaults and ConcurrentHashMap                   based on the feedback information obtained from seed ex-
ClassNodes to the same FieldNode (i.e. key) of the               ecution, JDD matches suitable condition constraints from
NodeImpl ClassNode, which implies the existence of               IOCD that are derived from the specified program execu-
at least two NodeImpl instances. Thus, JDD will in-              tion flow of gadget chains. And these condition constraints
clude an additional NodeImpl ClassNode to signify the            are utilized to selectively guide the structural mutation of
existence of two NodeImpl instances, where the field             injection objects. In order to record the selected condition
key of each instance is assigned to UIDfaults and                constraint strategies, JDD defines a unique identifier and
ConcurrentHashMap instances, respectively, as illus-             assigns a 2-bit flag to indicate the mutate strategy for each
trated in Figure 3 (a).                                          condition constraint. The first bit is used to indicate whether
                                                                 the constraint is used (0: not selected, 1: selected), and
                                                                 the second bit signifies whether the constraint is satisfied
3.6. Step 5: IOCD-enhanced Directional Fuzzing                   (true or false). With this identifier, JDD prefers to select
                                                                 unused strategies to cover more kinds of combinations of
    After modeling the structure of injection object and the     condition constraints. The following explains how to gener-
constraints should be satisfied, JDD further utilizes IOCD to    ate condition constraint branch strategies based on feedback
enhance our directional fuzzing. In general, given a gadget      information:
chain, the fuzzing goal is to generate an injection object
                                                                 (1) If JDD resolves the ClassCastException or
that could reach and exploit its sink point. Specifically,
                                                                     NullPointerException exception information,
JDD first generates initial seeds based on the IOCD and
                                                                     relevant fields causing the exception can be matched
then uses them to drive the fuzzing. In the exploration
                                                                     from IOCD based on error location information (class
phase of directional fuzzing, JDD utilizes the number of
                                                                     name, code line number), and JDD will require these
covered dominator constraints to evaluate the seed’s energy
                                                                     fields to satisfy specific constraints, i.e. f ield ! = null,
and guide the fuzzer to cover more dominator constraints
                                                                     f ield instanceof X.class.
until reach the sink point. In the exploitation phase of
                                                                 (2) Extract all constraints between the current reached and
directional fuzzing, JDD only mutates the fields related to
                                                                     the next dominator condition constraints, and select a
the sink point. During each field’s mutation, JDD adjusts
                                                                     mutation strategy based on each constraint’s identifier.
other related fields to fix the cross-field dependencies based
                                                                 (3) If there are no non-dominator condition constraints
on IOCD.
                                                                     between the current and the next dominator condition
IOCD based Seed Generation. Considering the cross-field              constraints, random mutation strategies are selected for
dependencies and nested object structure, JDD adopts the             the current dominator and the preceding conditional
IOCD-guided fuzzer to generate objects with the correct              constraints, note that dominator condition constraints
class hierarchy while taking into account the constraints            do not alter the second bit flag.
among fields. Specifically, JDD generates parameterless in-      (4) If the program has reached the sinks but has not
stances based on ClassNodes from the IOCD and estab-                 triggered the expected malicious instructions, JDD first
lishes the class hierarchy of these instances according to           checks whether there are multiple ways to construct
directed edges, as illustrated in Figure 3. Subsequently,            malicious data (i.e., constructed from different fields).
starting from the root ClassNode node, a Breadth-First               If such variations exist, JDD uses the information
traversal is performed on each FieldNode. JDD will extract           recorded in IOCD to call different fields to construct
dominator constraints of these FieldNodes, and invoke the            malicious data. Otherwise, randomly changing the con-
constraint solver to generate appropriate values, which are          dition constraints strategies.
then assigned to the corresponding fields. In situations where   (5) If all combinations of strategies for condition con-
bidirectional edges exist between FieldNodes, indicating the         straints have been used, a 50% probability is assigned
                                                     Table 2: Mutation Strategy.
  Property(prop)   Constraint(cnst)
                                      Example                                        Mutation Strategy
  Type             Type
                   Class              if(prop==cnst)                                 set prop to cnst
                   Method             if(prop.getDeclaredMethods().contains(cnst))   set prop to a Class instance that contains cnst Method
  Class                               if(prop.name==cnst)                            set prop to a Class instance of cnst
                   String             if(prop.superClassName==cnst)                  set prop to a Sub-Class instance of cnst
                                      if(prop.interfaceName==cnst)                   set prop to a Implementation Class instance of cnst
                   Class              if(prop.declaringClass==cnst)                  set prop to a Method instance of cnst Class
  Method           String             if(prop.name.startWith(cnst))                  set prop to a Method instance with proper name
                   int                if(prop.parameterNums==0)                      set prop to a Method instance with proper args numbers
  Object           Class              if(prop instanceof cnst)                       correct prop to an instance of cnst
                   int                if(prop.size ≥ cnst)                           add/remove elements
  Collection/Map   Class              if(prop.item instanceof cnst)                  correct the element type
                   Object             if(prop.contains(cnst))                        add/remove elements



      to randomly select fields from IOCD that have not                 mutators, i.e. nested field value reuse, sequential fixed ad-
      been marked with existing condition constraints for               justments.
      mutation.                                                            ● Nested field value reuse. After mutating a specific field
 (6) When the program reaches sinks and captures mali-                       (i.e., mutatedField), recursively check and adjust its
      cious instructions being written, that means the injec-                associated fields. Specifically, start by adjusting the
      tion object is exploitable, and the corresponding gadget               fields of mutatedField based on the relevant domina-
      chain is classified as exploitable. If the time threshold is           tor constraints on the IOCD. Then, detect the fields
      exceeded, or based on the specific type of information                 affected by the current constraint strategy, and reuse
      mentioned above, it can be directly determined as                      instances shared between the post-mutation and pre-
      non-exploitable, the current test is terminated, and the               mutation field instances.
      next IOCD corresponding to the next gadget chain is                  ● Sequential fixed adjustments. If JDD intends to mutate
      invoked to start a new round of testing.                               a specific field (i.e., field1), and there exists a constraint
    (ii) Mutation based on object structure constraints. After               associated with multiple fields (i.e., field2, field3), JDD
obtaining the condition constraints, JDD invokes the con-                    extracts the constraints relevant to these three fields
straint solver to adjust the object’s structure. Nevertheless,               separately. It then calls a constraint solver to find
as demonstrated by IOCD, there exist intricate constraint                    values for field1 that satisfy all related constraints while
relationships between fields. Modifying one of these fields                  minimizing field2 and field3 adjustments. Specifically,
can affect not only the corresponding ClassNode but also                     the constraint solver first fixes field2 and field3 and then
its fields and the fields associated with other ClassNodes.                  determines an appropriate value for field1. If it is unable
Consequently, a simplistic adjustment of an individual field                 to find a solution that satisfies the other constraints
based solely on condition constraints may compromise the                     on field1, it progressively adjusts field2 and field3 and
structural validity of the object.                                           continues the solving process.
    To address this issue, we propose our cascading mutation
strategy. When JDD adjust a field, it cascadingly exam-                 4. Implementation
ines whether other fields affected by this field also require
adjustments. If necessary, it adjusts them simultaneously
                                                                            We implemented JDD with over 25,000 lines of new Java
to maintain the structural validity of the injection object.
                                                                        code (excluding any third-party libraries). We will open-
Specifically, the mutation strategy can be categorized into
                                                                        source JDD in the camera-ready version of the paper. The
two levels: single-field and cross-field:
                                                                        static taint analysis module of JDD is implemented based
   ● Single-Field level. Mutating an individual field, which            on Soot [11] and FlowDroid [12], a flow-sensitive, object-
      does not have any constraints with other fields. Uti-             sensitive, and context-sensitive data-flow analysis tool. To
      lizing constraint solvers to resolve relevant conditional         identify the gadget fragments in dynamic proxies, we im-
      constraints for adjusting the assignment of the field.            plemented a path-sensitive analysis inner their method invo-
   ● Cross-Field level. When mutating a field with mutual               cation handlers. Moreover, we also conducted a lightweight
      constraints among other fields, ensure that relevant              pointer-to analysis to reduce the jump candidates in iden-
      information in associated fields is preserved, and main-          tifying gadget fragments. The dynamic fuzzing module of
      tain the validity of the object structure.                        JDD is implemented based on JQF [13], [14]. We first use
    (iii) Mutation based on field dependency constraints.               ASM [15] to instrument the target Java program for collect-
Based on the insight of making minimal modifications to                 ing the needed runtime context to guide our fuzzing engine.
the affected fields to avoid disrupting valid information after         Then, we customized JQF to build a directional fuzzing
mutation, and leveraging knowledge of class hierarchies,                framework for the generation of exploitable injection ob-
JDD has implemented the following two cross-field level                 jects. To avoid JDD stuck in a hard-to-detect chain, we set
the time limitation for identifying each gadget fragment in       variants of known chains) unique unknown chains in ysose-
the static analysis as 30 seconds and each round of fuzzing       rial repository, which is much larger than GadgetInspector
as 120 seconds, empirically.                                      (three known + zero unknown), SerHybrid (two known +
                                                                  zero unknown), and ODDFuzz (16 known + zero unknown).
5. Evaluation                                                         Note that JDD supports the identification and reuse of
                                                                  gadget fragments in known exploits. Since existing tools
     In this section, we evaluate the performance of JDD on       do not rely on known exploits, Table 3 does not include
real-world Java programs and compare it with state-of-the-        known exploits as input for the reason of fairness. We now
art tools via addressing four main research questions below:      describe the improvement if JDD is further improved by
                                                                  introducing the gadget fragments of known exploits. Take
● RQ1: How does JDD compare with state-of-the-art tools
                                                                  C3P0 as an example. If JDD is equipped with the known
  in detecting gadget chains?
                                                                  chain of C3P0, JDD can detect not only the gadget chains
● RQ2: How do the core modules of JDD contribute to its
                                                                  in Table 3 but also another five unknown gadget chains.
  performance?
                                                                  Additionally, in the expanded dataset of 26 gadget chains
● RQ3: How many zero-day JOI-based RCE vulnerabilities
                                                                  extracted from recently disclosed JOI vulnerabilities, JDD
  can JDD detect?
                                                                  also achieves a better result by detecting 24 known and 140
● RQ4: How does JDD perform in analyzing real-world Java
                                                                  unknown chains.
  applications?
                                                                  False Positive Rates. The existing tools for static detection
5.1. RQ1: Comparison with State of the Art                        of gadget chains commonly exhibit a high false positive
                                                                  rate. For example, GadgetInspector reaches a false positive
    In this section, we compare JDD with state-of-the-art         rate as high as 97.6%. However, SerHbrid, ODDFuzz, and
approaches in detecting (un)known gadget chains using             JDD reduce the false positive rate of final results to 0% by
two benchmarks. Specifically, we choose three state-of-           introducing dynamic verification.
the-art tools, namely GadgetInspector [3], SeHybrid [4],          False Negative Rates. As shown in Table 3, JDD missed
ODDFuzz [2]. To reduce randomness, we conducted five              seven known gadget chains in ysoserial, resulting in a false
repetitions of each experiment and reported the average           negative rate of 20.6% (7/34). GadgetInspector and ODD-
statistical results. All experiments were conducted on a          Fuzz have false negative rates of 91.2% (31/34) and 52.9%
Linux workstation with an Intel(R) Xeon(R) Gold 5218 CPU          (18/34) respectively. SerHybrid could not support the test
@ 2.30GHz and 128 GB of RAM, running Ubuntu 18.04                 of all Java apps in ysoserial. On the dataset they tested,
LTS.                                                              SerHybrid has a false negative rate of 83.3% (2/12). JDD
Benchmarks. We conducted this experiment using a dataset          demonstrated significantly lower rates of false negatives.
of 61 well-known gadget chains that can be exploited to con-          We then break down the seven known gadget chains
duct JOI attacks. Among these gadget chains, 34 come from         that missed by JDD. First, four of them require specific do-
the well-known ysoserial repository [5], which has been           main knowledge to identify some of their gadget fragments.
widely used in prior work [2]–[4]. Additionally, we collected     Specifically, JDD lacks domain knowledge of security-
26 other gadget chains by analyzing 32 recently disclosed         sensitive methods in Jython app, making it unable to
JOI vulnerabilties. These vulnerabilities could cover popular     detect the chain. Additionally, generating valid serialization
deserialization protocols that are not included in ysoserial,     data for the case in C3P0 requires rewriting a specific
for example, Hessian [16] and T3/IIOP [17] [18]. The new          method. Moreover, JDD lacks the knowledge about how the
benchmark will be available together with our open-source         return value of a dynamic proxy’s invocation handler affects
repository.                                                       program execution, thus failing to detect two chains in
                                                                  Spring (i.e. Spring1,2). As aforementioned, we could
Overall Results. Table 3 summarizes the overall results           use known exploits to further enhance JDD by identifying
of the experiment. In this table, we present the quantities       the gadget fragments used in them. For instance, JDD can
of gadget chains identified through static analysis (Iden-        automatically extract reusable fragments based on the ex-
tified chains), the number of gadget chains confirmed as          ploit of Spring1 and further identify Spring2. Second,
exploitable (confirmed chains), and the number of new-            the rest three gadget chains contain many fields with a
discovered gadget chains beyond the scope of the known            generic type, e.g., an Object type, leading to a time-out.
dataset (unknown chains). Note that, since SerHybrid, ODD-
Fuzz, and JDD have dynamic validation modules, their              Benefits in Supporting Java Dynamic Features. Bene-
confirmed chains come from the verified results of their          fiting from the bottom-up fragment search strategy, JDD
dynamic analysis. For GadgetInspector, a tool that is solely      has the capacity to support more Java dynamic features
reliant on static analysis, we manually verify the reported       to expand its detection capabilities, including Polymorphic,
results to determine the number of confirmed chains.              dynamic proxy and reflection, in which the last two are
     Overall, for the capability of detecting known gadget        commonly unsupported by existing tools. As a result, JDD
chains, the effectiveness of JDD is higher than existing tools.   could detect more gadget chains related to these dynamic
Particularly, JDD covers 27 known and 91 (including two           features than existing tools.
Table 3: Gadget chain detection comparison among GadgetInspector, SerHybrid, ODDFuzz, and JDD (Our Approach). The
number in parentheses indicates the detected known chains in the benchmark.
                                           GadgetInspector                 SerHybrid                      ODDFuzz                        JDD
                             Known
  Application                           Identified   Confirmed     Identified   Confirmed        Identified   Confirmed   Identified   Confirmed   Unkown
                             Chains
                                         Chains       Chains        Chains       Chains           Chains       Chains      Chains       Chains     Chains
                                                                     Ysoserial Benchmark
  AspectJWeaver                 1          8             0            N/A          N/A               9              0
  CommonsBeantuils              1          4             0             0            0                8              1       108†          25         20
  CommonsCollections            5          4             1             1            1               97              3
  BeanShell                     1          2             0             1            0                8              0        587          5           4
  C3P0                          1          2             0            N/A          N/A              13              1         15          0          0
  Click                         1          4             0            N/A          N/A               8              1          6          1           0
  Clojure                       1          12            1            N/A          N/A              184             1          6          3          2
  CommonsCollections4           2          4             0             1            1               112             2        230          26         24
  Groovy                        1          4             0             3            0               13              0        413          5          4
  JavassistWeld                 1          2             0            N/A          N/A               8              0          6          1           0
  JBossInterceptors             1          2             0            N/A          N/A               8              0          7          1          0
  JDK                           4          5             0            N/A          N/A               9              1         16          8           5
  JSON                          1          7             0            N/A          N/A               9              0        147          6          5
  Jython                        1          42            1            N/A          N/A              32              0          0          0           0
  MozillaRhino                  2          3             0            N/A          N/A               7              2          4          2          0
  Hibernate                     2          3             0             3            0                8              2         14          5           4
  Myfaces                       2          2             0            N/A          N/A               7              0         52          3          2
  ROME                          1          2             0             0            0                5              1         48          9           8
  Spring                        2          2             0            N/A          N/A              10              0          5          0          0
  Vaadin                        1          6             0            N/A          N/A              13              1        109          14         13
  FileUpload                    1          3             0            N/A          N/A               8              0          1          1          0
  Wicket                        1          3             0            N/A          N/A               7              0          1          1           0
  Total                        34          126         3 (3)           9           2 (2)            583        16 (16)      1362       116 (27)      91
                                                               Recently Disclosed Vulnerabilities
  Weblogic                     21          53            0            N/A          N/A             N/A          N/A          642         126        107
  MarshalSec(Hessian)‡         5           2             0            N/A          N/A             N/A          N/A          119          38         33
  Total                        26          55          0 (0)           -               -             -              -        761       164 (24)     140
  †
      Due to the shared use of the CommonsCollections dependency in detecting Gadget Chains in AspectJWeaver and CommonsBeanutils, we simultaneously
      conducted analysis on these three packages.
  ‡
      MarshalSec is a deserialization vulnerability exploitation tool, and we include its Hessian protocol-based Exploits as part of our evaluation dataset.


     First, due to its support for the dynamic proxy feature,                              ● JDD-top-down. We replace JDD’s bottom-up strategy
in our benchmark data set (i.e., the ysosearial repository),                                 with top-down strategy proposed by previous tools, i.e.
JDD can detect additional 16 gadget chains (3 known and                                      a Depth-first-search (DFS) starting from a source to a
13 unknown chains) compared to existing tools.                                               sink.
     Second, with the support of Java reflection, JDD can                                  ● JDD-NoIOCD. We remove JDD’s IOCD guidance in
detect more variants of gadget chains. An example is                                         the fuzzing module. Instead, JDD-NoIOCD employs an
Hibernate, which contains two variants of one unique                                         approach like ODDFuzz to infer the class hierarchy
chain in our benchmark. The difference of these two vari-                                    and randomly mutates fields based on a pre-defined
ants is in the last fragments, i.e, their targets of Java re-                                dictionary.
flection. JDD successfully detects three unique chains in                                  ● JDD-NoClassHierarchy: We replace JDD’s class hier-
Hibernate and additionally identifies two fragments that                                     archy inference approach with the approach proposed
could be linked as the targets of Java reflection to conduct                                 by previous tools, e.g., ODDFuzz.
code execution attacks. Another example is Vaadin. JDD                                     ● sys-NoConFd: We remove JDD’s condition-constraints-
first detects 14 gadget chains in it, which all end with Java                                aware and field-dependency-constraints-aware muta-
reflection and JDD additionally identifies three fragments                                   tion. Because these two types of constraints are closely
that could be linked to conduct code execution attacks.                                      related, we remove them together. Additionally, JDD-
                                                                                             NoConFd mutates fields randomly based on a pre-
5.2. RQ2: How do the core modules of JDD con-                                                defined dictionary, similar to ODDFuzz.
tribute to its performance?
                                                                                      First, we verify whether the bottom-up strategy is more
    We conducted two ablation studies on the task of gadget                       effective than the top-down strategy, by comparing how
chain detection and exploitability verification by comparing                      many exploitable gadget chains can be found by these
JDD with the following variants to evaluate the effectiveness                     two methods. JDD completed the analysis in seven min-
of JDD’s different modules:                                                       utes and 58 seconds with no timeouts and detected 116
           Table 4: The Detected Chains and Performance Evaluation Results of JDD on Real-World Java Apps.
                            Basic Information                    Detected Chains                                Performance
  Application
                                Class     Method    Identified   Confirmed         Vendor     Search and Link   Construct      Dynamic Verify
                    Stars
                               Number     Number     Chains       Chains            Reply      Gadget Chains     IOCD         (Detected Chains)
  Apache Dubbo       39K       88.5K      936.4K       31             7       CVE Assigned        8min29s           53s         36min15s (31)
  Motan               6K       53.7K      454.7K       695           93       CVE Assigned       15min25s        47min13s         6h (358)
  Solon             1.5K       280.9K    2,797.9K      117           35       CVE Assigned       39min56s        29min16s     2h35min59s (117)
  XXL-Job           24.5k      52.5K      411.1K       843          110       CVE Assigning       7min24s         52min8s         6h (363)
  Sofa-rpc          4.8K       94.9K      883.9K       205           43       CVE Assigned       37min15s         8min6s       3h43min3s (205)
  Apache Tapestry   0.1K       28.8K      241.1K       16             5       CVE Assigning         54s              9s         19min38s (16)



exploitable gadget chains. In comparison, JDD-top-down                       if they contain public entries for Java object injection and
took about 17 hours and only detected 15 gadget chains.                      deserialization. As a result, we successfully recognized six
After further analysis, we found that the analysis of 900                    apps (shown in Table 4) and use them as the dataset of this
sources in JDD-top-down timed out, thus missing 101 ex-                      experiment. For these six popular Java apps, we conducted
ploitable gadget chains. For example, in the analysis of                     our analysis based on the default or recommended configu-
CommonsCollections4 app, JDD-top-down failed to                              ration within their open-source projects. In this experiment,
complete the analysis of PriorityQueue.readObject                            the total time limitation for dynamic testing is 6 hours.
within the time threshold (e.g. five minutes). As a result,                      Table 4 shows the results, which indicates that JDD
JDD-top-down missed two exploitable chains.                                  successfully identified zero-day JOI vulnerabilities in all of
    Second, we evaluate the effectiveness of three types of                  these six Java apps as well as generated exploitable injection
guidance information in dynamic verification - class hier-                   objects for the 293 found gadget chains (127 unique chains).
archy constraints, conditional constraints and field depen-                  We have reported these gadget chains to the app developers
dency constraints, as well as the effectiveness of dataflow-                 and received confirmation from them. For example, the de-
based class hierarchy inference approach, by comparing                       velopers of Dubbo admitted that it is impossible for them to
the detection capabilities of JDD with JDD-NoIOCD, JDD-                      uncover these gadget chains, which indicates the urgency of
NoClassHierarchy and JDD-NoConFd on exploitable gadget                       our automatic tool. All 127 zero-day gadget chains detected
chains.                                                                      by JDD are capable of bypassing the latest patch defenses
    Experimental results show that JDD performs best, with                   at the time and, hence are vulnerabilities. Noting that, since
a total of 116 exploitable gadget chains detected, far ex-                   we reported multiple gadget chains for each attack point to
ceeding JDD-NoIOCD (31), JDD-NoClassHierarchy (41)                           help developers design and implement more comprehensive
and JDD-NoConFd (38). The experimental results prove                         defenses, we ultimately obtained six CVEs, less than the
that to generate exploitable injection objects for gadget                    total count of chains.
chains efficiently, the three types of constraint information in                 To demonstrate how our fragment based bottom-up ap-
IOCD (described in Section 3.5) are essential, especially for                proach can benefit the detecting of gadget chains, we use
complex chains. For example, for the chain in our motivat-                   real-world zero-day vulnerabilities found by JDD for case
ing example, JDD-NoClassHierarchy and JDD-IOCD will                          study.
infer the wrong class hierarchy as shown in Figure 3 (b),
causing subsequent mutations to be meaningless. Although                     Case Study #1: JOI based RCE Attacks. JDD discovered a
JDD-NoConFd can generate seeds with the correct class                        JOI based RCE vulnerability that impacts many popular Java
hierarchy, it is challenging to generate an object that si-                  apps such as Sofa, Solon, and XXL-Job, in which XXL-Job
multaneously satisfies the constraints (e.g. i-iii in Figure 3)              is a highly popular distributed task scheduling framework
within the time threshold, so this case is easily missed.                    with a remarkable number of GitHub stars (24.9k) and forks
                                                                             (10.3k) as well as be widely used by large enterprises with
    In addition, compared with ODDFuzz, JDD-NoIOCD
                                                                             over 256 million consumers. This vulnerability could allow
detected 15 more exploitable chains on the same benchmark
                                                                             attackers to take over the victim server by sending a request
ysoserial. This is because JDD ’s static analysis module
                                                                             with a well-crafted injection object.
can provide more high-quality candidate chains, which also
means that JDD ’s static analysis module can help to im-                         Thses application utilize the Hessian/Hessian-sofa
prove ODDFuzz’s detection capabilities.                                      protocol to deserialize the received serialized data. The
                                                                             main attack process for this vulnerability is illustrated
                                                                             in Figure 5, wherein the attacker initializes a HashMap
5.3. RQ3: Discovering Zero-day Vulnerabilities                               object and places two other HashMap objects (i.e. hmap1,
                                                                             hmap2) inside it, as well as ensures that hmap1, hmap2 have
    In this section, we run JDD atop real-world popular                      identical hash values to trigger the jump from Fragment
Java applications to detect zero-day JOI-based RCE vul-                      1 to 2. Then, to facilitate the jump from Fragment 2 to
nerabilities. Specifically, we first collected 80 popular Java               Fragment 3 and then to 4, the attacker needs to insert a
open-source apps from Github [19] with more than 100                         Type instance and a JSONObject instance into hmap1
stars. Then, we implement a semi-automatic tool to check                     and hmap2, and alternate the order of insertion. Then, based
       # Fragment 1     /* This HashMap stores                                                      only be invoked in a Unix-like system. For those non-Unix
       HashMap.put()     * hmap1 & hmap2
       HashMap.putVal() */
                                                                                                    systems, JDD could further find alternative fragments
       # Fragment 2                                                                                 to replace it thus fixing the chain, for example, using
       AbstractMap.equals()
       # Fragment 3                                                                                 ”getActiveServers()” method in ServerManagerImpl
       AudiofileFormat$Type.equals()
                                                                                                    class.
    # Case 1                                         # Case 2
   # Fragment 4a                                     # Fragment 4a
   fastjson2.JSONObject.toString()                   jackson.JSONObject.toString()
   # Fragment 5b                                     ...                                            5.4. RQ4: Performance
   fastjson2.JSONWriterUTF16.write()                 # Fragment 5b
   # Fragment 6c                                     jackson.SerializableSerializer.serialize()
   fastjson2.ObjectWriter2.write()                   # Fragment 6c
   # Fragment 7d                                     jackson.POJONode.serialize()                        In this section, we evaluate the performance of JDD in
   fastjson2.FieldWriterObject.write()
   fastjson2.getFieldValue.write()
                                                     ...
                                                     # Fragment 7d
                                                                                                    analyzing real-world Java apps. Table 4 shows the results.
   reflect.Method.invoke()                           jackson.BeanSerializer.serialize()             For the easy of statistic, we separate the analysis time of
                                                     ...
                                                     # Fragment 8                                   JDD into three parts: (i) the gadget chain searching and
                                                     jackson.BeanPropertyWrite.serializeAsField()
   # Fragment 9
   ServerManagerImpl.getActiveServer()               reflect.Method.invoke()                        linking (i.e., Steps 1–3 in Section 3), (ii) IOCD construction
   ServerTableEntry.isValid()                                                                       (i.e., Step 4 in Section 3), and (iii) directional Fuzzing (i.e.,
   ServerTableEntry.activate()
   Runtime.exec()                                    # Fragment 10                                  Step 5 in Section 3). The results indicate that JDD could
                                                     ContinuationContext.getTargetContext()
                                                     NamingManager.getContext()                     finish its analysis for most of real-world apps in the time
   # Fragment 11
   UnixPrintServiceLookup.getDefaultPrintService()
                                                     NamingManager.getObjectInstance()              limitation (six hours for each app).
   UnixPrintServiceLookup.getDefulatPrinterBSD()
   UnixPrintServiceLookup.execCmd()
                                                                                                         We have two observations. First, the static analysis part
   Runtime.exec()                                                                                   of JDD (Steps I–III) is very efficient, finishing with 20 mins
                                                                                                    in most cases. The reason is that JDD’s static search time is
Figure 5: Simplified Gadget Chains of Case Study #1 and
                                                                                                    polynomial, i.e., efficient in finding possible gadget chains.
Case Study #2, where Case #2 is an evolution of Case #1
                                                                                                    The analysis of Solon is slower but still within 40 minutes
with some gadget fragments being replaced.
                                                                                                    because the number of possible gadget fragments is large.
                                                                                                    Second, the dynamic analysis part of JDD may still have
on the information about the object (i.e., obj) contained                                           performance issues. Specifically, the analysis of Motan and
in the JSONObject instance, the deserialization process                                             Sofa-rpc times out after six hours due to false positives in
will jump from Fragment 4a to 7d, and subsequently                                                  gadget chains reported by JDD’s static analysis. The main
invoke reflective calls to methods related to the fields                                            reason is the imprecision in our points-to analysis and path
of obj, such as ”getDefaultPrintService()” method of                                                insensitivity outside invocation handlers of dynamic proxy.
a UnixPrintServiceLookup object. This method                                                        We leave the improvement of static analysis’s precision as
further leads to the execution of arbitrary commands                                                our future work.
injected by the attacker through Runtime.exec().
Alternatively, as a variant, this gadget chain also
can utilize Java reflection in Fragment 7d to invoke                                                6. Discussion
ContinuationContext.getTargetContext()
and carry out JNDI based code injection attacks.                                                    Expandability for Incomplete Patching Problem. One
Case Study #2: The Evolution of Case Study #1. By                                                   common problem facing JOI vulnerabilities and their
replacing certain fragments in a gadget chain, an attacker can                                      patches is that remote attackers may find alternatives for
rapidly discover new gadget chains that can affect another                                          the blocked gadgets in the patch and derive new exploitable
app. Taking the gadget chain introduced in Case Study 1                                             gadget chains from the original ones. For example, Figure 6
as an example, this chain can affect apps like Sofa-RPC,                                            illustrates the gadget chains’ reuse relationships among 23
solon, XXL-Job. However, due to the absence of the required                                         JOI vulnerabilities that affect WebLogic [21], a widely-
Java library dependency in Motan by default, this gadget                                            used J2EE application server employed by over 430K Java
chain cannot be used to exploit Motan, as some of its gadget                                        applications. Notably, CVE-2015-2852 continuously evaded
fragments missed.                                                                                   security patches by successively replacing parts of the frag-
    However, if the missed fragments could be replaced by                                           ments that were blacklisted, leading to a total of 11 follow-
gadget fragments in Motan, it could generate a new chain.                                           up CVEs over a period of six years.
Actually, in Motan, JDD detected an equivalent fragment                                                 There are two methods for users to expand JDD for
that depends on Jackson [20], a widely-used third-party                                             the incomplete patching problem. First, users may expand
dependency for data-binding functionality and tree-model.                                           the fragment data set of JDD with known fragments, e.g.,
Thus, the Fragment 4a-8 (in # Case 2) can replace the                                               all possible gadgets in CVE-2015-2852. Second, users may
Fragment 4a-7d (in # Case 1), resulting a new chain, as                                             expand the source set of JDD with known sources. These
illustrated in Figure 5.                                                                            two methods will help users to find possible derivative
    Furthermore, the gadget chain in Case Study                                                     vulnerabilities, thus making the patch more complete.
1 uses the ”getDefaultPrintService()” method of a                                                   Lightweight Pointer-to Analysis and Restricted Path-
UnixPrintServiceLookup object to load and execute                                                   sensitive Analysis. We leverage pointer-to analysis and
code from remote attackers. However, this method could                                              path-sensitive analysis to mitigate the erroneous generation
    Disclosed Vulnerability
The gadget fragments is used by                                                                                                     CVE-2020-2551

                                  CommonsCollections5(ysoserial)                                         CVE-2018-3191                                                                                     CVE-2022-21350
                                                                                                                                    CVE-2020-2883              CVE-2020-14825

                                                                                                                     CVE-2020-2555            CVE-2020-14645
                                                                                                                                                                                       CVE-2021-2136
  CVE-2015-2852               CVE-2016-0638           CVE-2016-3510                                     CVE-2018-3248                                                      CVE-2020-14756          CVE-2021-2394
                                                                CVE-2017-3248              CVE-2018-2893                                                                                                                          CVE-2023-21931
          JRMPListener(ysoserial)                                             CVE-2018-2826              CVE-2018-3245                                                                 CVE-2021-2135                   CVE-2023-21839

   Sep.2015     Mar.2016 Apr.2016 May.2016 Jul.2016                Jan.2017     Apr.2018      Jul.2018    Oct.2018       Jan.2020    Apr.2020       Jul.2020    Oct.2020    Jan.2021    Apr.2021       Jul.2021 Jan.2022   Jan.2023 Apr.2023


Figure 6: WebLogic’s JOI vulnerabilities and the reuse of their gadget fragments, which lead to the incomplete patch
problem.

and concatenation of fragments, thereby reducing false pos-                                                                    7.1. Deserialization Vulnerability Mining
itives in static analysis and lowering the computational load
of fuzzing.
    The misidentification of an object’s type can result                                                                           In recent years, a substantial body of research [22]–[24]
in the erroneous identification of dynamic method invo-                                                                        has been devoted to the automated mining of deserialization
cations, consequently leading to false positives in frag-                                                                      vulnerabilities using both static and dynamic methods.
ment generation and linking. The utilization of pointer-
to analysis techniques effectively reduces false positives                                                                         GadgetInspector [3] is one of the most well-known
caused by this issue. For instance, in the analysis of                                                                         automated gadget chain mining tools. It utilized static taint
the CommonCollections4 application, applying the                                                                               analysis to discover execution paths from manually defined
lightweight pointer-to analysis results in a reduction of 806                                                                  source points to sink points. However, its effectiveness is
false positive chains.                                                                                                         limited in intricate scenarios due to inherent design limi-
    Furthermore, dynamic proxies are widely used in many                                                                       tations in data-flow and control-flow analysis. Chen et al.
Java apps. Specifically, an invocation handler of dynamic                                                                      proposed Tabby [25], which utilizes Soot [11] to transform
proxy usually selects different program handling logic based                                                                   Java programs into Code Property Graphs (CPG) [26]–
on the method properties (e.g., method name) that triggers                                                                     [29] and imports them into Neo4j database [30]. Then,
the handler, resulting in many possible execution paths                                                                        they extract gadget chains through querying CPG, using
during static analysis. Thus, it requires a path-sensitive                                                                     manually crafted Cypher [31] statements. These approaches
analysis to identify accurate execution paths when linking                                                                     commonly demand significant expertise in deserialization
gadget fragments in invocation handlers of dynamic proxies.                                                                    vulnerabilities, thus constraining their scalability. Compared
But applying the path-sensitive analysis to a larger scope                                                                     with them, during static analysis, JDD do not rely on domain
(e.g., the entire codebase) will significantly slow down static                                                                knowledge about JOI vulnerabilities. It only leverages the
analysis with limited gains in reducing false positives, so                                                                    understanding of Java dynamic features to identify gadget
we limit the scope of path-sensitive analysis to balance                                                                       fragments and link them together. Moreover, JDD also de-
performance and false positives.                                                                                               signs a novel bottom-up approach to greatly improve the
                                                                                                                               efficiency of its static module.
Limitations. We discuss two limitations of JDD: (i) per-
                                                                                                                                    Considering that static analysis often introduces numer-
formance of dynamic analysis, and (ii) implicit constraints.
                                                                                                                               ous false positives, SerHybrid [4] proposed to automate
First, while JDD significantly improves the performance of
                                                                                                                               the verification of exploitable gadget chains through the
static analysis, the fuzzing part of dynamic analysis may
                                                                                                                               construction of heap abstractions for generating injection
still have performance issues during mutation, particularly
                                                                                                                               objects. Building upon Tabby, GCMiner [1] incorporated
when the number of false positives from static analysis is
                                                                                                                               an overriding-guided object generation strategy to automate
large for some Java applications due to over-approximation.
                                                                                                                               verification during fuzzing. And ODDFuzz [2] utilized di-
The main reasons for such false positives are that our points-
                                                                                                                               rected fuzzing to enhance verification efficiency. In addi-
to analysis is lightweight, leading to imprecisions in many
                                                                                                                               tion, black-box scanning tools like Marshalsec [32] and
cases, and our path sensitivity is restricted inside invocation
                                                                                                                               Java Deserialization Scanner [33] have also been proposed.
handlers of dynamic proxies, i.e., the analysis outside is
                                                                                                                               Compared with them, JDD guides fuzzing by recognizing
path insensitive. Second, while JDD considers some implicit
                                                                                                                               data-flow dependencies between injection objects’ fields. On
constraints, such as the nullpointer exceptions and forced
                                                                                                                               one hand, this approach enables the inference of complex
type casting, there are still other implicit constraints that
                                                                                                                               injection object structures, such as parallel and embedded
need to be solved during exploit generation.
                                                                                                                               injection object, which were commonly uncovered in pre-
                                                                                                                               vious work. Furthermore, JDD significantly improves seed
7. Related Work                                                                                                                mutation’s efficiency by considering constraints from the
                                                                                                                               program’s execution flow specified by gadget chains. It is
                                                                                                                               noteworthy that, to the best of our knowledge, JDD is the
     We describe both attacks and defenses related to dese-                                                                    first tool capable of automatic generation of exploitable
rialization vulnerabilities.                                                                                                   injection objects based on gadget chains.
7.2. Deserialization Vulnerability Defense                        application developers and obtained their acknowledgments
                                                                  and confirmations.
     Implementing effective strategies to enhance application
security is often necessary, particularly in the context of       Acknowledgments
defense against deserialization vulnerabilities [34]. Exist-
ing strategies are commonly referred to as look-ahead de-             We would like to thank the anonymous reviewers for
fenses [35], wherein an audit is conducted on classes that        their insightful comments that helped improve the qual-
require deserialization, and only those that are permitted can    ity of the paper. This work was supported in part by
be deserialized. One notable look-ahead defense is JEP290         the National Key Research and Development Program
[36], which offers a blacklist of prohibited malicious classes    (2021YFB3101200), National Natural Science Foundation
during deserialization, along with interfaces for user exten-     of China (62172104, 62172105, 61972099, 62102093,
sions. In addition to the JDK’s built-in standard solutions,      62102091), and National Science Foundation (NSF) (CNS-
Runtime Application Self-Protection (RASP) [37] frame-            21-54404 and CNS-20-46361). Yuan Zhang was supported
works [38] [39] are frequently employed to defend against         in part by the Shanghai Rising-Star Program under Grant
deserialization vulnerabilities. These frameworks leverage        21QA1400700 and the Shanghai Pilot Program for Basic
bytecode instrumentation tools to intercept risky APIs for        Research - FuDan University 21TQ1400100 (21TQ012).
auditing. Some work also concentrate on automating the            Dr. Yinzhi Cao was supported in part by Johns Hopkins
generation of deserialization strategies. Trusted [40] is a       Catalyst Awards and DARPA Young Faculty Award under
two-phase defense framework that learns from benign dese-         Grant Agreement D22AP00137-00 as well as a gift from
rialization workloads to create an allowlist, which is then en-   Visa Research. Min Yang is the corresponding author, and
forced during the deserialization process. Another approach       a faculty of Shanghai Institute of Intelligent Electronics &
by François et al. [41] involves training a Markov chain         Systems and Engineering Research Center of Cyber Security
with malicious Gadget Chains, which is then used to predict       Auditing and Monitoring.
malicious Injection Objects at runtime.
     In summary, this thread of work commonly enforce
security checks on risky sources, sinks, and gadgets used in      References
Java deserialization. Compared with them, JDD focuses on
another important research problem – mining risky sources,        [1]   S. Cao, X. Sun, X. Wu, L. Bo, B. Li, R. Wu, W. Liu, B. He,
                                                                        Y. Ouyang, and J. Li, “Improving java deserialization gadget chain
sinks, and gadgets that could be abused as much as possible.            mining via overriding-guided object generation,” in IEEE/ACM 45th
Thus, the output of JDD can significantly support them. Take            International Conference on Software Engineering (ICSE), 2023, pp.
the white list adopted by Trusted as an example. JDD could              397–409.
check if the classes in the white list are enough to construct    [2]   S. Cao, B. He, X. Sun, Y. Ouyang, C. Zhang, X. Wu, T. Su,
gadget chains. Another example is RASP based approach.                  L. Bo, B. Li, C. Ma, J. Li, and T. Wei, “Oddfuzz: Discovering java
Their efficiencies highly depend on the completeness of                 deserialization vulnerabilities via structure-aware directed greybox
                                                                        fuzzing,” in IEEE Symposium on Security and Privacy (SP), 2023,
risky sink points, and JDD could help to verify if specific             pp. 2726–2743.
methods could be exploited by injection objects and thus
                                                                  [3]   I. Haken, “Automated discovery of deserialization gadget chains,”
should be protected.                                                    Proceedings of the Black Hat USA, vol. 48, 2018.
                                                                  [4]   S. Rasheed and J. Dietrich, “A hybrid analysis to detect java se-
8. Conclusion                                                           rialisation vulnerabilities,” in Proceedings of the 35th IEEE/ACM
                                                                        International Conference on Automated Software Engineering, 2020,
     In this paper, we design a novel, scalable approach                pp. 1209–1213.
for automated detection and verification of JOI vulnerabil-       [5]   Ysoserial. https://github.com/frohoff/ysoserial.
ities, called JDD. On one hand, JDD solves the static path        [6]   Sofa-rpc. https://github.com/sofastack/sofa-rpc.
explosion problem by a bottom-up approach, which first
looks for gadget chain fragments and then chains gadget           [7]   https://github.com/apache/dubbo-hessian-lite.
fragments from sinks to sources. The approach reduces             [8]   https://github.com/sofastack/sofa-hessian.
static search time from exponential to polynomial, i.e., from     [9]   G. Fourtounis, G. Kastrinis, and Y. Smaragdakis, “Static analysis of
O(eM n ) to O(M 2 n3 + enM ), where n is the number of                  java dynamic proxies,” in Proceedings of the 27th ACM SIGSOFT
dynamic function calls in a gadget chain, M is the average              International Symposium on Software Testing and Analysis, 2018,
                                                                        pp. 209–220.
number of dynamic function call candidates, and e is the
number of entry points. On the other hand, JDD constructs         [10] Y. Li, T. Tan, and J. Xue, “Understanding and analyzing java reflec-
                                                                       tion,” ACM Transactions on Software Engineering and Methodology
a so-called Injection Object Construction Diagram (IOCD),              (TOSEM), vol. 28, no. 2, pp. 1–50, 2019.
which models the data-flow dependencies between injection
                                                                  [11] Soot. https://github.com/soot-oss/soot.
objects’ fields to facilitate dynamic fuzzing. Our evaluation
of JDD upon six real-world Java applications reveals 127          [12] S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein,
                                                                       Y. Le Traon, D. Octeau, and P. McDaniel, “Flowdroid: Precise
zero-day, exploitable gadget chains with six being assigned            context, flow, field, object-sensitive and lifecycle-aware taint analysis
with Common Vulnerabilities and Exposures (CVE) identi-                for android apps,” Acm Sigplan Notices, vol. 49, no. 6, pp. 259–269,
fiers. We also responsibly reported these vulnerabilities to           2014.
[13] R. Padhye, C. Lemieux, and K. Sen, “Jqf: Coverage-guided property-          [38] openrasp. https://github.com/baidu/openrasp.
     based testing in java,” in Proceedings of the 28th ACM SIGSOFT
     International Symposium on Software Testing and Analysis, 2019,             [39] P. Čisar and S. M. Čisar, “The framework of runtime application self-
     pp. 398–401.                                                                     protection technology,” in 2016 IEEE 17th International Symposium
                                                                                      on Computational Intelligence and Informatics (CINTI), 2016, pp.
[14] R. Padhye, C. Lemieux, K. Sen, M. Papadakis, and Y. Le Traon, “Se-               000 081–000 086.
     mantic fuzzing with zest,” in Proceedings of the 28th ACM SIGSOFT
     International Symposium on Software Testing and Analysis, 2019, pp.         [40] D. B. S. Cristall, E. Vignati and A. Lanzi, “Trusted execution path
     329–340.                                                                         for protecting java applications against deserialization of untrusted
                                                                                      data,” Research in Attacks, Intrusions, and Defenses, M. Bailey, T.
[15] Asm. https://asm.ow2.io/.
                                                                                      Holz, M. Stamatogiannakis, and S. Ioannidis, Eds. Cham: Springer
[16] Hessian    protocol.      https://en.wikipedia.org/wiki/Hessian (Web             International Publishing, pp. 445–464, 2018.
     service protocol).
                                                                                 [41] F. Gauthier and S. Bae, “Runtime prevention of deserialization
[17] T3    protocol.   https://docs.oracle.com/cd/E14571 01/web.1111/                 attacks,” in Proceedings of the ACM/IEEE 44th International
     e13721/rmi t3.htm#WLRMI143.                                                      Conference on Software Engineering: New Ideas and Emerging
[18] Iiop     protocol.    https://www.ibm.com/docs/en/iad/7.2.1?topic=i-             Results. New York, NY, USA: Association for Computing
     internet-inter-orb-protocol-iiop.                                                Machinery, 2022, p. 71–75. [Online]. Available: https://doi.org/10.
                                                                                      1145/3510455.3512786
[19] Github. https://github.com/.
[20] Jackson. https://github.com/FasterXML/jackson.                              [42] “Cauchy–Schwarz inequality - Wikipedia — en.wikipedia.org,” https:
                                                                                      //en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz inequality,
[21] Oracle weblogic server. https://www.oracle.com/java/weblogic/.                   [Accessed 04-08-2023].
[22] S. Park, D. Kim, S. Jana, and S. Son, “{FUGIO}: Automatic ex-
     ploit generation for {PHP} object injection vulnerabilities,” in 31st
     USENIX Security Symposium (USENIX Security 22), 2022, pp. 197–              Appendix A.
     214.                                                                        Time Complexity of Bottom-up and Top-down
[23] M. Shcherbakov and M. Balliu, “Serialdetector: Principled and prac-
     tical exploration of object injection vulnerabilities for the web,”
                                                                                 Approaches
     in Network and Distributed Systems Security (NDSS) Symposium
     202121-24 February 2021, 2021.
                                                                                 A.1. Proof of Theorem 1
[24] S. Cristalli, E. Vignati, D. Bruschi, and A. Lanzi, “Trusted execu-
     tion path for protecting java applications against deserialization of
     untrusted data,” in Research in Attacks, Intrusions, and Defenses:          Proof. If there are n dynamic method invocations in a chain,
     21st International Symposium, RAID 2018, Heraklion, Crete, Greece,          and the average number of candidates for these invocations
     September 10-12, 2018, Proceedings 21. Springer, 2018, pp. 445–
     464.                                                                        is M , the number of source is e. According to Lemma 1,
                                                                                 the search complexity for a source is O(n3 M 2 ).
[25] Z. J. Y. F. X. L. X. F. X. Chen, B. Wang and Q. Liu, “Tabby: Auto-
     mated gadget chain detection for java deserialization vulnerabilities,”         As for each source, the maximum number of connection
     2023.                                                                       checks is nM , and the overall search complexity of Algo-
[26] “Code property graph - Wikipedia — en.wikipedia.org,” https://en.           rithm 1 to search for all sources is O(n3 M 2 + enM ).
     wikipedia.org/wiki/Code property graph, [Accessed 04-08-2023].
[27] M. Martin, B. Livshits, and M. S. Lam, “Finding application errors          Lemma 1. The per-entry search complexity of Algorithm 1
     and security flaws using pql: a program query language,” Acm Sigplan        is O(M 2 n3 ), where n is the number of dynamic method
     Notices, vol. 40, no. 10, pp. 365–383, 2005.                                invocations, and M is the average number of candidates
[28] F. Yamaguchi, N. Golde, D. Arp, and K. Rieck, “Modeling and                 for these invocations.
     discovering vulnerabilities with code property graphs,” in 2014 IEEE
     Symposium on Security and Privacy. IEEE, 2014, pp. 590–604.
[29] M. Backes, K. Rieck, M. Skoruppa, B. Stock, and F. Yamaguchi,
                                                                                 Proof. In Algorithm 1, n′ represents the number of distinct
     “Efficient and flexible discovery of php application vulnerabilities,” in   dynamic method invocations, with each dynamic method
     2017 IEEE european symposium on security and privacy (EuroS&P).             having x1 , x2 , ..., xn′ , candidates, as difference groups,
     IEEE, 2017, pp. 334–349.                                                    and a total of N = x1 + ... + xn′ candidates. We can then
[30] neo4j. https://neo4j.com/.                                                  compute the searching complexity for Algorithm 1 through
[31] Cypher. http://opencypher.org/.                                             the following three steps.
[32] marshalsec. https://github.com/mbechler/marshalsec.                            ●   Max Searching Times per Round: By employing
[33] Java deserializer sanncer.        https://github.com/federicodotta/Java-           a bottom-up search, it becomes possible to store the
     Deserialization-Scanner.                                                           exact input requirements connecting each fragment to
[34] “CWE - CWE-502: Deserialization of Untrusted Data (4.12) —                         Sink Fragments and avoid repeated searching. Mean-
     cwe.mitre.org,” https://cwe.mitre.org/data/definitions/502.html, [Ac-              while, there will not be two Sink Fragments with the
     cessed 04-08-2023].                                                                same dynamic method implementation serving as the
[35] R. Seacord, “Combating java deserialization vulnerabilities with look-             Head. And the fragment with the candidate of the p-
     ahead object input streams (laois),” NCC Gr Whitepaper, 2017.                      th dynamic method invocation as the Head requires
[36] jeps290. https://openjdk.org/jeps/290.                                             checking for connections with a maximum of N − xp
[37] Z. L. Z. Yin and Y. Cao, “A web application runtime application self-              other fragments. Considering these most complex sce-
     protection scheme against script injection attacks,” p. 566–577, 2018.             narios, using equations (1) and (2), we can calculate
      the maximum number S of linkage detection attempts                  algorithm. The computational complexity of this process can
      during the search process.                                          be determined accordingly.
                                                                             ● The notation O(1) is defined as follows: when the tree
                    x1 + x2 + ... + xn′ = N <= M n                  (1)
                                                                               is an empty tree (has no nodes) or consists of only one
                          Sp = xp (N − xp )                         (2)        node, the number of paths is 0 or 1 respectively. This
                         S = N 2 − (x21 + ...x2n′ )                 (3)        serves as the termination condition for the recursion.
                                                                               The search complexity is denoted by S(1) = O(1).
      According to the Cauchy-Schwarz inequality [42], for
                                                                             ● The recursive hypothesis. Assuming that for a node
      any real numbers a1 , a2 , ..., an and b1 , b2 , ..., bn , we
                                                                               at a depth d in the tree, the searching complexity of
      have:
                                                                               the Depth-First Search (DFS) algorithm is denoted by
               (a21 + a22 + ... + a2n′ )(b21 + b22 + ... + b2n′ )              S (d).
                                                                             ● The recursive step: For a node at depth d − 1, we
                   >= (a1 b1 + a2 b2 + ... + an′ bn′ )2             (4)
                                                                               recursively invoke the DFS function to process its child
      When we set a1 = x1 , a2 = x2 , ..., an′ = xn′ , and b1 =                nodes. Each node can have M child nodes, so in the
      b2 = ... = bn′ = 1, equation (4) is transformed into (5),                worst case, the DFS function needs to be called M
                                          (x1 + x2 + ... + xn′ )2              times for each child node located at depth d − 1. Ac-
           (x21 + x22 + ... + x2n′ ) >=                                        cording to the induction hypothesis, the DFS processes
                                                   n′                          nodes at depth d − 1 with a searching complexity of S(d-
                               N2                                              1). Therefore, the time complexity to process a node at
                                                                    (5)
                                n′
                                    =
                                                                               depth d is O(M ) × S (d − 1).
      From equations (5) and (3), it follows that                              Based on the recursive relation, we can expand
                                 1
                            S <= N 2 (1 −        (6)
                                 n′
                                    )
                                                                                             S (d) = O(M ) × S (d − 1)
      , and the maximum value of S is obtained when                                                = O(M 2 ) × S (d − 2)
      x1 = x2 = ... = xn = nN′ .
                                                                                                   = ...
  ●   Searching Complexity Since the search requires a                                             = O(M d ) × S (0)
      maximum of n′ iterations, the overall algorithm’s max-                                       = O(M d )
      imum number of search attempts is
                                                                               Therefore, for a single source, the search complexity
                             1                                                 is O(M n ), and when performing DFS searches from e
                  n′ N 2 (1 −   ) < n′ N 2 <= n3 M 2    (7)                    entry points, the search complexity becomes O(eM n ).
                             n′
      We define the search complexity O(1) as a one-time
      fragment linking check. Note that, after JDD identi-
      fies the fragments, it will merge the fragments whose               Appendix B.
      headers are the implementations of the same dynamic                 An analysis of historical gadget chains
      method but meet the conditions based on the special
      cases described in Appendix B. The complexity of this                    We collected 79 gadget chains from well-known deseri-
      step is O(N); Therefore, the final maximum search                   alization vulnerability databases, including ysoserial, Mar-
      complexity is O(n3 M 2 + N ) = O(n3 M 2 ) for each                  shalSec, and 113 CVE reports of JOI vulnerabilities.
      source.                                                                  When studying these 79 gadget chains, we first explored
                                                                          which methods are typically chained after Java reflection.
                                                                          The results show that 39 of the 79 gadget chains use Java
A.2. Proof of Theorem 2                                                   reflection, and they can all be summarized into two major
                                                                          types. Specifically, 27 chains use parameterless methods as
Proof. All symbols follow the Theorem 1. Based on the                     follow-up methods. Of these 27 chains, six require getter
description in the ODDFuzz paper, when an attacker-                       or is methods and four must be overridden methods of
controllable dynamic method call is searched, all overridden              interface methods. The remaining 12 chains use methods
methods will continue to be searched. Therefore, under the                with a parameter of type String or Boolean as follow-up
assumption of a search strategy that avoids false negatives               methods to unsafe reflection. Therefore, we prioritize testing
as much as possible, and also considers the computational                 the two types of successor methods in Section 3.3.
complexity in the worst case, conducting a DFS (Depth-                         Then, among these 79 historical gadget chains, only
First Searching) for potential gadget chains from a source                nine have the same dynamic method calls nested, and the
to a sink can be equivalent to detecting all paths of a tree              reasons for nesting the same dynamic method calls can be
with depth n, and each node in the tree having an average                 attributed to two categories: (1) Implement chain calls of
of M branches, starting from the root node, using the DFS                 Method.invoke, sequentially calling insecure methods in
the program to execute malicious instructions, such as CVE-   Appendix C.
2020-2555. (2) Satisfy common specific strong constraints     Meta-Review
- hash collision, such as the conditional constraints shown
in Line 7 in Figure 1. Therefore, we let JDD support both.        The following meta-review was prepared by the program
                                                              committee for the 2024 IEEE Symposium on Security and
                                                              Privacy (S&P) as part of the review process as detailed in
                                                              the call for papers.

                                                              C.1. Summary

                                                                  This paper proposes JDD, a new framework to detect
                                                              Java deserialization vulnerabilities. The main focus in on
                                                              improving the efficiency of the analysis. First, it mitigate the
                                                              path explosion problem by employing a bottom-up search
                                                              strategy to avoid redundancies in top-down approaches,
                                                              which reduce the time needed for static gadget chain search
                                                              from exponential time to polynomial time. Second, it uses
                                                              the Injection Object Construction Diagram (IOCD) to track
                                                              dependencies between data fields of the various injected
                                                              objects, which reduces the search scope. Third, it tracks
                                                              control dependencies during fuzzing to collect more fine-
                                                              grained progress feedback. Evaluation shows that the proto-
                                                              type tool is able to find more deserialization gadget chains
                                                              than previous state-of-the-art approaches.

                                                              C.2. Scientific Contributions

                                                                ● Provides a New Data Set For Public Use
                                                                ● Creates a New Tool to Enable Future Science
                                                                ● Provides a Valuable Step Forward in an Established
                                                                  Field

                                                              C.3. Reasons for Acceptance

                                                               1) The paper is well-written
                                                               2) The paper tackles with an interesting and timely topic:
                                                                  deserialization vulnerabilities in Java
                                                               3) JDD discovered 127 unknown deserialization chains in
                                                                  6 real-world Java apps
                                                               4) JDD outperformed the previous state-of-the-art, in
                                                                  terms of scalability and false negative rate
