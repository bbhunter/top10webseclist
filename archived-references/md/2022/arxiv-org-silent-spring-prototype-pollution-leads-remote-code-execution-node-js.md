---
type: Article
title: "Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js"
resource: "https://arxiv.org/abs/2207.11171"
tags: [article, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-12T16:02:04+00:00"
status: stable
stale_after: 2027-08-12
sources:
  - id: original
    resource: "https://arxiv.org/abs/2207.11171"
    title: "Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js"
    author: Mikhail Shcherbakov, Musard Balliu, Cristian-Alexandru Staicu
also_at:
  - "https://www.usenix.org/system/files/usenixsecurity23-shcherbakov.pdf"
authors:
  - Mikhail Shcherbakov
  - Musard Balliu
  - Cristian-Alexandru Staicu
canonical_url: ""
cited_by:
  - "2022.md:77"
commit: ""
content_sha256: 821d1064c9baac659476f1cfc98367e491473ed89a3faba80561539703c44cb0
depth: full
depth_reason: default
kind: article
language: ""
licence: unknown
original_url: "https://arxiv.org/abs/2207.11171"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 9bb46082408fbbedebaf1dbd0cbd5c4c56b359a7a02b1a4a6f6d2b0173b221fc
retrieved_from: "https://www.usenix.org/system/files/usenixsecurity23-shcherbakov.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-12T16:02:04+00:00"
slug: arxiv-org-silent-spring-prototype-pollution-leads-remote-code-execution-node-js
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js

**Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js** - Mikhail Shcherbakov, Musard Balliu, Cristian-Alexandru Staicu, Publisher not stated.

- Published: date not stated
- Original: <https://arxiv.org/abs/2207.11171>
- Also published at: <https://www.usenix.org/system/files/usenixsecurity23-shcherbakov.pdf>
- Preserved from: https://www.usenix.org/system/files/usenixsecurity23-shcherbakov.pdf (stored) on 2026-08-12
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js

--- page 1 ---

Silent Spring: Prototype Pollution Leads
 
to Remote Code Execution in Node.jsMikhail Shcherbakov and Musard Balliu, KTH Royal Institute of Technology; 
Cristian-Alexandru Staicu, CISPA Helmholtz Center for Information Securityhttps://www.usenix.org/conference/usenixsecurity23/presentation/shcherbakov

--- page 2 ---

This paper is included in the Proceedings of the 
32nd USENIX Security Symposium.August 9–11, 2023 • Anaheim, CA, USA978-1-939133-37-3Open access to the Proceedings of the 
32nd USENIX Security Symposium 
is sponsored by USENIX.

--- page 3 ---

Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js
Mikhail Shcherbakov
KTH Royal Institute of Technology
Musard Balliu
KTH Royal Institute of Technology
Cristian-Alexandru Staicu
CISPA Helmholtz Center for Information Security
AbstractPrototype pollution is a dangerous vulnerability affectingprototype-based languages like JavaScript and the Node.jsplatform. It refers to the ability of an attacker to inject prop-erties into an object's root prototype at runtime and subse-quently trigger the execution of legitimate code gadgets thataccess these properties on the object's prototype, leading toattacks such as Denial of Service (DoS), privilege escalation,and Remote Code Execution (RCE). While there is anecdo-tal evidence that prototype pollution leads to RCE, currentresearch does not tackle the challenge of gadget detection,thus only showing feasibility of DoS attacks, mainly againstNode.js libraries.In this paper, we set out to study the problem in a holisticway, from the detection of prototype pollution to detectionof gadgets, with the ambitious goal of nding end-to-endexploits beyond DoS, in full-edged Node.js applications.We build the rst multi-staged framework that usesmulti-labelstatic taint analysis to identify prototype pollution inNode.js libraries and applications, as well as a hybrid ap-proach to detectuniversal gadgets, notably, by analyzing theNode.js source code. We implement our framework on topof GitHub's static analysis framework CodeQL to nd 11universal gadgets in core Node.js APIs, leading to code exe-cution. Furthermore, we use our methodology in a study of 15popular Node.js applications to identify prototype pollutionsand gadgets. We manually exploit eight RCE vulnerabilitiesin three high-prole applications such as NPM CLI, ParseServer, and Rocket.Chat. Our results provide alarming evi-dence that prototype pollution in combination with powerfuluniversal gadgets lead to RCE in Node.js.
1 IntroductionIn recent years we have seen a growing interest in runningJavaScript outside of the browser. A prime example is Node.js,a popular server-side runtime that enables the creation offull-stack web applications. Its package management system,NPM, is the world's largest software repository with millionsof packages. Researchers have studied this ecosystem exten-sively to discover several security risks [14,20,31,44–47,51],showing that these risks are further exacerbated by the inter-connected nature of the ecosystem [52]. While most priorwork focuses on libraries, the problem of automatically de-tecting vulnerabilities in Node.js applications is still open.Prototype pollution is a JavaScript-driven vulnerability thatmanifests itself powerfully in the Node.js ecosystem. Thevulnerability is rooted in the permissive nature of the lan-guage, which allows the mutation of an important built-inobject in the global scope –Object.prototype– called theroot prototype. JavaScript's prototype-based inheritance en-ables accessing this important object through the prototypechain. Thus, attackers can instruct vulnerable code to mutatethe root prototype by providing well-crafted property namesto be accessed at runtime. As a consequence, every objectthat inherits from the root prototype, i.e., the vast majorityof objects in the runtime, inherits the mutation on the rootprototype, e.g, an attacker-controlled property. This vulner-ability was rst introduced by Arteau [12], showing that itis a widespread problem in Node.js libraries. Recently, Li etal. [31,32] explore static analysis to detect prototype pollutionvulnerabilities using object property graphs.The few prior works [25,27,31,32,51] on prototype pol-lution consider a successful attack any mutation of the rootprototype. An immediate consequence of such mutations isDenial of Service (DoS) due to the overwriting of importantbuilt-in APIs, e.g.,toString. By contrast, our work studiesthe implications of prototype pollution beyond DoS. In par-ticular, we propose a semi-automated approach for detectingRemote Code Execution (RCE) vulnerabilities pertaining toprototype pollution. While there is anecdotal evidence aboutthe possibility of such attacks [5,12], we are the rst to pro-pose a principled and systematic approach to detect them. Ourkey focus is on gadget identication and end-to-end exploita-tion which no prior work has addressed thoroughly.Moreover, we note the important similarities between ob-ject injection vulnerabilities (OIVs) [17,41] and RCEs based

--- page 4 ---

USENIX Association
32nd USENIX Security Symposium 5521

--- page 5 ---

on prototype pollution. These attacks work in two stages: (1)there is an untrusted ow from an application's untrusted entrypoints to aninjection sink, e.g., the property of an object; (2)there is a gadget that further propagates the attacker-controlleddata from the injection sink to a security-relevantattack sink.In analogy, the attacker loads the gun in stage one (by placingthe payload into the injection sink), while letting someoneelse (a gadget) pull the trigger in stage two and carry out theattack (through an attack sink). We propose calling the classof OIVs pertaining to prototype pollution,prototype-basedobject injection
vulnerabilities (POIV).In statically-typed languages, OIVs are enabled by inse-cure deserialization, which allows instantiating objects of anunexpected type, thus triggering otherwise unused methods.Similarly, in a duck-typed language like JavaScript, if an at-tacker mutates the root prototype, they change the dynamictype of multiple objects in the runtime. This in turn activatesotherwise unused code paths that correspond to the new type,e.g., objectfoohaving a propertybardened. Thus, codereuse is done at a ner granularity and in a less localizedmanner in dynamically typed languages. We also note that at-tackers can mutate several properties at once, hence chaininggadgets in the fashion of property-oriented programming [17].Our technical contribution is a multi-staged framework thatuses multi-label static analysis for detecting prototype pollu-tion, and a hybrid solution, i.e., combining dynamic and staticanalysis, for detecting gadgets. We observe that code patternsthat lead to prototype pollution, i.e., injection sinks, are ratherrare in real-world code. Thus, different from prior work, wepropose tuning the static analysis for improved recall, ratherthan precision. Additionally, to emphasize the feasibility ofthe attack, we detectuniversal gadgetsin Node.js' sourcecode, which can be exploited in a wide-range of applicationsas they come packaged with the Node.js runtime.Drawing on security advisories [10], we aggregate a set of100 vulnerable packages, which we use to design and validateour pollution detection analysis. In comparison with the state-of-the-art tool ODGen [32], we empirically show that one cansignicantly increase recall and scalability, while only payinga modest decrease in precision.We then design and evaluate our novel gadget detectionanalysis against four widely-used APIs for handling code orcommand execution in Node.js. We nd a total of 11 gadgetsthat can be triggered during typical execution of these APIs.While some gadgets enable code injection directly, othersallow attackers to load arbitrary les from the disk into theruntime, by confusing the module resolution mechanism. Wealso conduct a quantitative study on packages to estimate theprevalence of these gadgets in the Node.js ecosystem. Webelieve that we are the rst to show evidence that control owcan be hijacked in this way in Node.js, further emphasizingthe dangers of shipping unused code with applications [28].Finally, we analyze 15 popular Node.js applications, re-porting on the effort to nding RCE with our methodology.We identify eight exploitable RCE vulnerabilities in highly-popular applications such as NPM CLI, Parse Server andRocket.Chat. We have responsibly disclosed these criticalvulnerabilities to developers and they are now xed, acknowl-edging our contributions with a high-severity advisory (e.g.,CVE-2022-24760) and bug bounties.Contrary to established recommendations, this work em-braces false positives. We show that a motivated attacker cansieve through the manageable amount of false positives tond critical zero-day exploits against well-tested, mature ap-plications. We believe that vulnerability detection tools tunedfor offensive security can afford this luxury due to the highreturn on investment provided by a single true positive.
In summary, the paper offers the following contributions:
•We are the rst to study the impact of prototype pollutionvulnerabilities in full-edged Node.js applications, beyonddenial-of-service attacks.
•We present a principled approach for detecting RCE vulner-abilities that are enabled by prototype pollution.
•We show that our pipeline is directly applicable to real-world code: we nd 11 universal gadgets in Node.js' sourcecode and eight RCEs in popular applications.
•We provide initial evidence that unused code shipped withthe application, e.g., third-party dependencies, can be lever-aged as part of code reuse attacks in Node.js.
2 Context and Technical BackgroundThis section provides background information and discussesthe targeted threat model.
2.1 Prototype-based OIVPrototypesare a key feature to implement inheritance ofJavaScript properties and methods to form aprototype chain.When creating an empty object, e.g.,const obj = {}, it al-ready contains many built-in properties and functions, forinstance, thetoStringfunction. When invokingtoStringon an object, the runtime engine will rst check if the functionis explicitly dened for the given object. If not, it will recur-sively look for its denition on the object's prototype chain.Unfortunately, most objects share the same root prototype.For example, all objects created via the literal{}or thenew
Object()constructor share the same prototype unless it isexplicitly overridden. The following code snippet illustratesthe problem:
1
const
o1 = {};
2
const
o2 =
new
Object();
3
o1.__proto__.x = 42;
4
console.log(o2.x);Although objectso1ando2are unrelated, their prototypeproperties__proto__point to the same object. In fact, if weadd the new propertyxto the prototype of objecto1it will

--- page 6 ---

5522 32nd USENIX Security Symposium
USENIX Association

--- page 7 ---

also affect objecto2, resulting in a print of value42to theconsole. Therefore, if we modify the root prototype shared bydifferent objects, all these objects will reect the modication.We now explain the two stages needed to carry out aprototype-based attack that leads to code execution.Stage 1: Polluting the prototype.Listing 1 shows a contrivedexample to illustrate key ingredients dening aninjectionsinkin a POIV. We assume that the attacker controls all threearguments of functionentryPoint. The rst ingredient isan object that inherits a prototype that the attacker wantsto pollute, as shown by the object in line 2, which inheritsObject.prototype
.
1
function
entryPoint(arg1 , arg2 , arg3) {
2
const
obj = {};
3
const
p = obj[arg1];
4
p[arg2] = arg3;
5
return
p; }
Listing 1: Prototype pollution exampleThe second ingredient is the attacker-controlled access tothe prototype property, as shown in line 3 via the bracketnotation. The attacker can pass__proto__toarg1to storeObject.prototypein variablep. The last two ingredients re-quire creating a target property in the prototype and assigningan attacker-controlled value. In fact, line 4 assigns an attacker-controlled value to a property ofObject.prototype. Sincethe attacker controlsarg2andarg3, they can write any valueto any property. The JavaScript engine will create a new prop-erty, if such property does not exist. In general cases, theattacker cannot fully control all the ingredients, e.g., the prop-erty in
arg2
or the value in
arg3
.An immediate effect of this vulnerable pattern is the at-tacker's ability to perform a DoS attack, e.g, by executing thefunctionentryPoint("__proto__", "toString", 1);to alter the state to an unexpected integer value, i.e.,Object.prototype.toString = 1, thus, forcing anapplication that calls
toString()
to crash.Stage 2: Executing the gadget.This stage requires identify-ing gadgets that contain insecure ows from injection sinksto
attack sinks
that perform security-sensitive actions.
1
const
{ execSync } = require("child_process");
2
function
gadget(args , options) {
3
const
cmd = options.cmd || "cmd.exe /k";
4
return
execSync(`${cmd} ${args}`);
5
}
6
const
args = ...;
7
gadget(args , {});
Listing 2: Gadget exampleConsider the benign example in Listing 2, where a list ofargumentsargsand a command objectoptionsis passedto a functiongadgetwith the intention to execute commandoptionswith argumentsargs. The intended use of functiongadgetis to either execute the command that is speciedvia the propertycmdof theoptionsobject or execute thedefault commandcmd.exe. However, since the developerpassed an empty object to functiongadget(line 7), the pro-gram is expected to execute the default command, becauseoptions.cmd
is undened (line 3).Consider now an execution of the program in Listing 1 suchthatentryPoint("__proto__", "cmd", "calc.exe&");The attacker manipulates thecmdproperty of the root pro-totype, causing the undened propertyoptions.cmdto fallback to the value in the prototype chain. Hence, the attackercan control the command passed toexecSync, which leadsto code execution, launching a calculator via
calc.exe&
.
2.2 Threat ModelOur threat model targets an attacker that controls theun-trusted entry pointsof a Node.js application with the goalof exploiting prototype-based OIVs to perform arbitrary codeexecution on the application. These untrusted entry pointsare application-specic, however, candidates include HTTPconnections, untrusted database reads, and the like. We alsoconsider a weaker threat model targeting onlyuniversalgad-gets that occur in the source code of Node.js. Because thesegadgets appear in code that executes with the Node.js runtime,they are available for exploitation in any Node.js application.For this threat model, we assume that the attacker controls theinjection sinks pertaining to the execution of a gadget.
3 OverviewThis section provides an overview of our multi-staged analy-sis framework, illuminating on the key challenges in detectingand exploiting prototype-based object injection vulnerabili-ties. We use our newly-detected vulnerability in NPM CLIto illustrate the complexity and challenges of such an en-deavor. NPM CLI [9] is the command line client that allowsdevelopers to install and publish packages in NPM registries.It comes bundled with the Node.js runtime and consists of713,648 lines of code.Detecting prototype pollution.Figure 1 shows the simpliedcode fragment of the functiondiffApplyfrom NPM CLI'scodebase, which is subject to prototype pollution.The function takes the arraypathfrom the attacker-controlled parameterdiffand calls the built-in functionshift()that returns the rst element of the array. Thedata ow then goes through the loop storing a propertyvalue to the variableobj(red line). Because the attackerindirectly controls the property namethisPropin line 8,the property read allows them to access the object's rootprototype by settingthisPropto__proto__. Subsequently,the attacker can assign any value to any property of the rootprototype as illustrated by the assignment in line 11. Asa result, the attacker has full control of the injection sinkdenoted by the blue dotted lines. For instance, the function call

--- page 8 ---

USENIX Association
32nd USENIX Security Symposium 5523

--- page 9 ---

Figure 1: Injection sink in NPM CLI
diffApply({}, {path: ['__proto__', 'env'], value:
'payload', op: ADD})injects intoObject.prototype
the environment property
env
with payload
payload
.This code fragment illustrates the challenges that a staticanalysis should overcome. First, in contrast to standard taintanalysis, injection sinks cannot be identied syntactically asthey require specialized data ow analysis that record ac-cesses to object properties, as illustrated by the blue dottedline. The analysis should identify attacker-controlled inputsthat allow to control the prototype object, followed by usesof this prototype object as a receiver in a property assign-ment [31]. Second, the analysis should handle language con-structs such as loops and model the JavaScript built-in func-tions, e.g.,shift()to correctly propagate data ows. Third,given the size of the targeted codebases, the analysis shouldbe scalable, seeking the sweet spot between precision andrecall. While prior work achieves high precision, it reportslow recall, thus increasing the possibility to miss aws in realapplications [31,32]. These requirements lead us to our rstresearch question:How to design and implement a scalablestatic analysis that effectively identies prototype pollution inreal-world libraries and applications?To answer this ques-tion we develop a multi-label static taint analysis, which wediscuss in Section 4.1 and evaluate in Section 6.1.Detecting code gadgets.Recall that our threat model requiresidentifying code gadgets that read the attacker payloads fromthe injection sink and pass it into an attack sink. Figure 2shows a universal gadget we identied, stemming from thepopular
spawn
function of the Node.js standard library. Thisfunction rst callsnormalizeSpawnArgsand reads the valueof propertyopts.envin line 11. This optional parameter con-tains key-value pairs of the environment variables of a newprocess. If a developer passes an object without propertyenv,the JavaScript runtime will look up the property in the proto-type chain. Alternatively, attacker can inject the environmentvariable directly using thefor..inloop in line 13 to sub-sequently read it either from theopts.envorprocess.env
object in line 11.The reader may at this point wonder about our second re-search question:How to identify universal properties readssuch as
env
? In fact, a prerequisite for gadget detection is to
Figure 2: Universal gadget in Node.js standard libraryidentify property reads that delegate the lookup of the prop-erty to the prototype chain, while ltering out cases wherethe property is dened in the object itself. This is a compli-cated task for a static analysis, hence we use dynamic analysisinstead. We discuss the details in Section 4.2.Further, the gadget contains intricate data ows from theproperty read in line 11 to the attack sink in line 6 as de-noted by the red arrows. Specically, thefor..inloop enu-merates the property names of the read object and passesthem to an array through theArrayPrototypePushcall.This is an internal function that implements the seman-tics ofArray.prototype.pushand subsequently enumer-ates theenvKeysarray, storing key-value pairs by the tem-plate literal (line 18) and returning a new object with thepropertyenvPairs. Therefore, an analysis should modelthe semantics of internal functions, template literals, thefor..inandfor..ofstatements to propagate the attacked-controlled values properly. Moreover, functionspawn(line3) passes the modied objectoptsto methodspawnofthe internal wrapperProcess(line 6) that is implementedin the C++ component of Node.js. This method corre-sponds to the actual attack sink. Specically, if an attackeruses{GIT_SSH_COMMAND: 'calc&'}aspayloadfor func-tiondiffApply, they can simply wait for an invocation ofthe attack sinkspawnfrom the git command. The latteruses the specied command from the environment variableGIT_SSH_COMMANDwhen connecting to a remote system. Thisleads us to our third research question:How to identify theattack sinks and data ows from universal property readsto these attack sinks in Node.js?Gadget detection is a newchallenge with no prior research, except for some evidenceprovided by the practitioners' community [5,12]. To addressthis question, we develop a taint-based static analysis thattracks ows from property reads to attack sinks, which wediscuss in Section 4.2 and evaluate in Section 6.2.3.Putting it all together.The presence of prototype pollution

--- page 10 ---

5524 32nd USENIX Security Symposium
USENIX Association

--- page 11 ---

Figure 3: High-level workow: automated steps (green) andmanual steps (blue).and gadgets is not sufcient to carry out an end-to-end RCEattack. The attacker needs to identify application-specicuntrusted entry points that enable the payload to reach theinjection sinks, and to subsequently propagate this payloadto an attack sink via the gadget. This step requires us tocombine data ow analysis with the call ow analysis, startingat untrusted entry points, while driving the payload to reach anattack sink. This leads to our nal research question:How toidentify public entry points and payloads to demonstrate thefeasibility of RCE attacks?We use a combination of manualand automated analysis to drive the exploit towards success,as detailed in Section 4.3 and evaluated in Section 6.3.
4 MethodologyWe present a semi-automated analysis framework for detect-ing and exploiting prototype-based vulnerabilities. The frame-work is divided into three major steps: (i) automated prototypepollution detection; (ii) automated gadget detection; and (iii)manual exploit generation for end-to-end attacks. Figure 3illustrates the sequence of steps and their dependencies.The prototype pollution detection step takes as input thecode of an application or NPM package and performs amulti-labeltaint-based static analysis. Subsequently, the analysisreconstructs the call graph of the application to nd entrypoints that reach the prototype pollution, thus facilitating thetask of identifying attacked-controlled entry points. The gad-get detection step implements a hybrid solution. A dynamicanalysis rst detects which properties can be actually pollutedby executing Node.js APIs of interest in a testing environmentthat logs property accesses, ultimately returning a list of ac-cessed property names. These property names, together withthe source code of Node.js, are used as input to our secondstatic analysis to identify (universal) gadgets in Node.js. Eachgadget includes an entry point that reaches a targeted propertyread and an attack sink that is called with values read from thetarget property. The last step of the approach is the end-to-endexploit generation. This is a manual step that requires an in-vestigation of the target application's workow to validate theexploitability of the detected prototype pollution and gadgetto achieve code execution on the system.
4.1 Prototype Pollution DetectionMulti-label taint analysis.The detection of prototypepollution requires specialized data ow analysis thatidenties injection sinks boiling down to the patternobj[prototype][property] = value. We nd these pat-terns by means of a ow- and context-sensitivemulti-labeltaint analysis. Specically, we use two labelsinputandprototo capture the temporal relationship between (attacker-controlled) property accesses in an object. We use labelinputto mark parameters that are directly controlled by the attackerand labelprototo record that the attacker already controls theprototype of the labeled object.The analysis works as follows: initially, it marks the pa-rameters of the analyzed function with theinputlabel. Then,it performs (standard) taint analysis propagating this labelaccording to the JavaScript semantics until it reaches a prop-erty read with a tainted value in the property name, e.g.,obj[prototype]withprototypehaving labelinput. Thisindicates that the attacker may control the property name andget access to the root prototype. At this point, the label of theresulting property read, e.g.,obj[prototype], is changedto the labelprototo record that the attacker can now con-trol the prototype. Subsequently, the analysis continues thetaint propagation until it reaches a property assignment, e.g.,obj[prototype][property] = value, where the object ofthe property assignment, i.e.,obj[prototype], is markedwith theprotolabel, thus identifying the injection sink. Wenote that this a general characterization of injection sinks,where the attacker does not necessarily control the accessedproperty (property) and the assigned value (value), so longas they control the root prototype (prototoype). Becausethis setting is more difcult to exploit, our analysis supports aprioritymode to identify attacker-controlled property namesand values in a property assignment. Specically, it performstwo additional operations to check that the property read(property) and the value (value) are marked with labelin-put, indicating that they may be controlled by the attacker. Asexpected, these priority injection sinks are an easier target forexploitation in practice.Figure 1 illustrates the multi-label taint analysis for the pro-totype pollution vulnerability in NPM CLI. We consider thefunctiondiffApplyas target function and mark the parame-ters with labelinput. The red arrows depict the propagation oflabelinput. The parameterdiffis an object and the taint anal-ysis passes the tainted label to all its properties. The methodshiftis a built-in method that returns the rst element of thearray. The static analysis models JavaScript standard built-inobjects, and thereby, propagates theinputlabel tothisPropin line 4. The next node of the data ow is the property readin line 8, hence the analysis changes its label toproto. Theblue dotted lines then visualize theprotolabel propagation.The tainted value reaches the property assignment, and thealgorithm reports this expression as the injection sink. This

--- page 12 ---

USENIX Association
32nd USENIX Security Symposium 5525

--- page 13 ---

is also a priority sink because the parameterslastPropanddiff.value
in line 11 have label
input
.MethodologyWe dene the (attacker-controlled) targetfunctions in two ways: (i) a package's exported functions(dubbed Exported Functions) or (ii) any function of the an-alyzed codebase (dubbed Any Functions). We use the rstoption for the package analysis only, assuming that the at-tacker controls any exported function and class of a package.The second option allows us to analyze real-world applica-tions with no knowledge of the application's entry points,which usually depend on the specic threat model. We ndthis option useful in practice to overcome inherent limitationsof static analysis for JavaScript, which does not always sup-port the correct label propagation, e.g., due to callbacks ordynamically-generated code. In this case, the analysis allowsus to detect injection sinks by propagating theinputlabelfrom the nearest function on the call graph. Yet, the semanticmodeling of built-ins is key to increasing the true positiverate.Ideally, a taint analysis should provide precise and com-plete models of JavaScript constructs. CodeQL features manyperson-hour contributions into the modeling of built-in func-tions. Nonetheless, we observe that in practice these modelsare still insufcient. Our approach relies on the ground truthprovided by known vulnerabilities to improve the tool inmodeling features that pertain to these vulnerabilities, thusreducing the number of false negatives. Concretely, we re-view the CodeQL standard library to identify and x languagefeatures, e.g., Arrays and reection calls (see Section 5) thataffect the taint semantics for the considered packages. Weapplied this process iteratively to achieve high recall.Entry point detection.We propose a lightweight analysis todetect application-level entry points that may trigger the in-jection sinks. This helps with applications that receive tainteddata from external storage to nd the external action that trig-gers the data acquisition from the storage. The static analysisrst reconstructs a call graph where the functions with nocallers are represented by nodes with outgoing edges only.The algorithm considers such nodes as potential applicationentry points and reports the code paths to the injection sink.SummaryThis step provides information about the pollu-tion patterns and application's entry points for future manualvalidation and exploit generation. We contribute ve analysisvariants: one analysis for entry point detection; twopriorityanalyses (for each type of target function) that report injectionsinks with all tainted ingredients; and twogeneralanalyses(for each type of target function) that report injection sinkswith a tainted receiver only.
4.2 Gadget DetectionDynamic analysis.We rst parse the Node.js' source codeand syntactically extract all directly-accessed properties. Thedynamic analysis denes a custom handler with a property get-ter inObject.prototypefor each extracted property name.We systematically analyze the Node.js API documentation toidentify functions that potentially run processes or evaluatearbitrary code in the runtime. We then invoke these APIs tolog their attempt of property reads fromObject.prototype,which result in reading uninitialized properties and getting thevalueundefined. This means that the values of these prop-erties can be tampered via prototype pollution. The dynamicanalysis passes the collected property names to the next step.Static analysis.The analysis takes the Node.js' source codeand the property names as input. The algorithm rst performsthe call ow analysis of Node.js API functions, including in-formation about aliases, ultimately allowing us to reconstructa precise call graph of the analyzed functions. We then use thecall ow analysis to identify paths from any exported functionto polluted property reads (identied by the dynamic analy-sis) and subsequently combine it with context-sensitive tainttracking to identify paths from these property reads to attacksinks, represented as tainted arguments to internal functioncalls. Specically, the analysis propagates the taints on returnvalues only for functions that are reached by the Node.js APIon the analyzed call ow. Additionally, the analysis identiesaffected exported functions that were not analyzed dynami-cally. For instance, the analysis of functionspawnreports apossible pollution of propertyenv. The static analysis showsthe attack sinks that are affected byenvinclude additionalNode.js API functions such as
spawnSync
,
exec
and
fork
.The taint analysis considers internal functions, i.e., func-tions for which the analyzer cannot resolve the function body,as candidate attack sinks. We conservatively cover all func-tions with no implementation in the codebase. The taint analy-sis also uses multi-labels. For property assignments, the algo-rithm propagates the taint labelpollutedof the property andapplies the new labelreceiverto the receiver recursively. Forinstance, ifvaluein the assignmentobj.prop = valuehaslabelpolluted, then the analysis applies thereceiverlabel toobjand thepollutedlabel to its propertyprop. This is neededbecause we cannot enumerate all properties of an object whenthis object is used as parameter to an attack sink. Finally, thestatic analysis reports internal functions with no argumentsand either
polluted
or
receiver
labels as attack sinks.Figure 2 shows the analysis in action for propertyenv.The blue dotted arrows illustrate the call ow analysis fromthe exported functionspawnto the rst function call. ThenormalizeSpawnArgscontains the property readenvwhichis the starting node of the taint analysis (red arrows). Initially,the taint analysis propagates the labelpollutedthrough thedata ows. When the tainted value reaches the object creationstatement in line 21, the analysis keeps the taint label forthe propertyenvPairsand assigns the labelreceiverto thecreated object. This object is further propagated to the callerfunction and passed to the internal function_handler.spawnin line 6, thus reporting_handler.spawnas a candidate sink.

--- page 14 ---

5526 32nd USENIX Security Symposium
USENIX Association

--- page 15 ---

4.3 Exploit GenerationOur approach relies on the human-in-the-loop model for ex-ploit generation. For gadget exploits, the information aboutattack sinks allows us to evaluate the impact of a pollutedproperty and lter out non-malicious sinks. The call ow andtaint analysis help to explore the code slice that reaches theattack sink. We use this information to generate a payload andtest it on the detected Node.js APIs. We validate the detectedsinks and report new gadgets for Node.js in Section 6.2.3.A security analyst rst analyzes the prototype pollutionpatterns to lter out false positives and non-executable casesin the regular application workow, e.g., patterns in testingcode and development tools. For suspicious cases, the analystuses the automatically-detected entry points to generate therst version of a payload and validates it on the application. Ifan exploit fails, the analyst investigates the cause using othertools (e.g., a debugger) and modies the payload.If the validation of the prototype pollution succeeds, thenthe next step is to search for gadget triggers. We extend theuniversal gadget entry points (e.g.,spawn) with functionsthat evaluate JavaScript code represented as strings (eval(),new Function(),new vm.Script) and provide a call graphanalysis for these calls. The analyst may use the call graphanalysis to detect calls to these functions as well as the appli-cation's entry points that reach these calls.If the analyst detects a gadget trigger, they need to validatethat it is executed after the injection sink and then generate apayload that pollutes the required properties. If code evalua-tion function is detected, the analyst investigates the precondi-tions for invoking it with attacker-controlled data. The inputdata can be read from the polluted property, or the function'sexecution may be dependent on specic conditionals that usethe polluted property. These steps lead to arbitrary code exe-cution inside the Node.js instance. We estimate the effort ofusing such exploitation model in a study in Section 6.3.
5 ImplementationCodeQL [4] is a production-scale analysis engine to performsemantics-based search on a target codebase, essentially bytreating code as data. The analysis rst extracts a full hierar-chical representation of code (e.g., the AST) into a relationaldatabase. It then runs analysisqueriesagainst the databaseto compute result tuples, for instance, pairs of source loca-tions and error messages for bug nding. CodeQL queries arewritten in a declarative, object-oriented logic programminglanguage called QL, which uses Datalog as underlying seman-tic model [13]. It also provides astandard libraryof queriesthat implement control-ow and data-ow analyses, as well assupport for mainstream languages including JavaScript. TheJavaScript model and the analyses are part of the open-sourceQL standard library, making them amenable to extensions.
A key feature that we use in our analyses are
path queriesthat describe the data ow between a source and a sink inthe codebase. They support expandable taint tracking withthe possibility of using multiple ow labels. This is essen-tial to implement our analysis algorithms described in Sec-tion 4. Specically, we develop the custom path queries forpollution and gadget detection. We extend the taint trackingconguration to combine the call-ow and data-ow analy-ses, thus propagating tainted values through call ows in acontext-sensitive way. This feature is essential for some of ouranalyses, e.g., to analyze entry points that receive tainted datafrom a database and not propagate the taint labels throughcode that is reachable from other entry points. We also modelthe array built-in functionsreduce,filterand more, to cor-rectly propagate tainted values via callback functions passedas arguments. This allows us to detect vulnerabilities that usereducein the injection sink. We also resolve new functionscreated bybindcall to propagate taints from the providedvalues of thebindarguments to the bound function param-eters. Other changes include support for parameter passingviaapply()andcall()function calls, as well as the rest pa-rameter syntax and theargumentsobject. We also improvethe detection of exported functions of Node.js packages. Ouranalysis queries for pollution and gadget detection followthe methodology described in Section 6.1 and are publiclyavailable as complementary material [43].
6 EvaluationThis section presents our experiments to validate the useful-ness of our approach to detect and exploit POIVs. We performthe experiments on an Intel Core i7-8850H CPU 2.60GHz,16 GB of memory. The tool, the analysis results and data areavailable in the GitHub repository [43].
6.1 Evaluation of Prototype PollutionThis section evaluates the effectiveness of our tool to detectinjection sinks, reporting on precision and recall. While re-cent approaches already target this problem [27, 31, 32] forNode.js libraries, our key contribution is scalability with low-to-moderate precision loss, while achieving high recall. Incontrast to prior work on libraries, we nd that injection sinksare rare in real-world applications, motivating the need forhigh recall to identify exploitable vulnerabilities.Benchmark.We compile an open-source dataset of 100vulnerable Node.js packages, collected from the Snykdatabase [10]. By studying the proof-of-concept exploit pro-vided in the vulnerability report, we manually identify codelocations (le name and line number) of injection sinks per-taining to the assignment of an attacker-controlled value tothe polluted property. We observe that some packages containmultiple exploitable injection sinks, which we also add toour benchmark. This new dataset serves as ground truth to

--- page 16 ---

USENIX Association
32nd USENIX Security Symposium 5527

--- page 17 ---

evaluate the detection capabilities of static analyses. For com-parison, we also consider the dataset of 19 packages providedby the state-of-the-art work ODGen [32].Setup.We use our benchmark to calculate the rate of true pos-itives (TP), false positives (FP), and false negatives (FN) inan effort to identify the sweet spot between the precision andrecall of the analysis. The precision metric describes how wellthe tool identies exploitable injection sinks, while recall rep-resents the fraction of real vulnerabilities reported by a tool.Following the methodology in Section 4.1, we run our toolin four different modes with the goal of identifying the mosteffective approach for detecting injection sinks in real-worldapplications. Our benchmark shows that attackers can havedifferent levels of control over the injection sinks. While ingeneral it can be sufcient to control the injection of the rootprototype only, we notice that most exploits target injectionsinks with attackers controlling both the name and value of apolluted property. Therefore, our tool distinguishes betweenthe two cases, respectively, denoted asGeneral queriesandPriority queries. Moreover, since our analysis considers tran-sitive dependencies, we distinguish between target functionsconsideringExported FunctionsandAny Functions, with thegoal of identifying the best mode to analyze applications.We also compare our results with three analysis querieswhich CodeQL recently made available publicly. We considerthese CodeQL queries as baseline queries and run them onour benchmarks. Moreover, we conduct a direct comparisonwith ODGen [32] on the dataset of 119 libraries.Results.We report the evaluation results in Table 3 in Ap-pendix and here discuss only the precision and recall metricsin comparison with CodeQL's baseline queries and ODGen.CodeQL provides three queries to detect prototype pollu-tion, one of which yields no results, hence we discard it. Theremaining two queries detect vulnerabilities in 57 packages,with 47% and 67% precision and 42% and 21% recall, re-spectively. While our analysis queries have been developedindependently, our main goal is to achieve high recall withgood precision. A fair comparison with the CodeQL baselinecorresponds to ourGeneralqueries withExported Functions,which yields 35% precision and 88% recall. The improvedrecall is due to better support for exported functions, arraybuilt-in functions, and complete semantic modeling of re-ective invocations throughapply(),call()andbuild()functions. These results conrm the challenge of staticallyanalyzing data ows in JavaScript without precise models ofthe language semantics and built-in functions.Our second experiment is an evaluation ofGeneralquerieswithAny Functionsas entry points. The analysis achieves 31%precision and 97% recall, producing 5 false negatives. Thisfalse negatives are in packages such asTempl8andtotal_jswith injection sinks into code that is generated dynamicallyvianew Function(), which CodeQL does not support. Thehigh recall shows that injection sinks appear in a few adjacentfunctions, which reduces the risk of losing the taint marksbecause of missing models of built-in functions. However, pre-cision deteriorates because some detected patterns are not ac-tually reachable from the library API with attacker-controlledarguments. We also notice the precision loss is much less thanone would expect from an analysis with the strong assump-tion that any function's arguments are attacker-controlled. Webelieve this is due to the shape of injection sinks requiringpatterns that are not very common in real-world code (seeSection 4.1). While 31% precision in aggregate results is notideal, our analysis produces less than 10 false positives for90% of the benchmarks.Our third experiment is the evaluation ofPriorityquerieswithAny Functionsas entry points. In this setting, the attackercontrols the name and value of the polluted property, thusit can leverage any existing gadget. The analysis achieves40% precision and 93% recall. The additional restrictions onarguments increase the precision metric and keep high recall.Because the analysis starts from any function and does notrequire specifying the entry points, we can easily apply itto real-word application analysis. We identify this analysisquery as the sweet spot between precision and recall, and useit to detect vulnerabilities in real applications (Section 6.3).Our nal experiment is a direct comparison withODGen [32]. ODGen's analysis corresponds to ourGeneralqueries withExported Functions. ODGen is tailored towardshigh precision, while the authors recognize the need for highrecall. In fact, our experiment shows that ODGen achieves100% precision and 50% recall on the dataset of 19 libraries,while our analysis achieves 95% precision and 95% recall(see the evaluation results in [43]). Nonetheless, ODGendetects vulnerabilities in 17 out of the 19 libraries, but failsto detect some variants of these vulnerabilities. We furtherevaluate ODGen on our dataset of 100 packages to nd that itachieves 87% precision and 33% recall.
6.2 Gadget DetectionWe evaluate the feasibility of our universal gadget detectionanalysis and discuss the most important gadgets. We run ouranalysis on Node.js version 16.13.1 and exploit each gadgetboth on Linux and on Windows operating systems.
6.2.1 Dynamic AnalysisWe download the source code of Node.js and parse it to extractall directly-accessed properties. We obtain a total of 18,741property names for the analyzed codebase [8]. For each name,we install a getter onObject.prototoypeto detect any po-tential access to that property by Node.js' internals.Subsequently, we exercise the APIs under test withtypical inputs from the Node.js documentation, e.g., exe-cute thelscommand withspawn[7], and log any poten-tial accesses observed by the getter. In total, we analyzethree APIs, i.e.,child_process.spawnSync,require, and

--- page 18 ---

5528 32nd USENIX Security Symposium
USENIX Association

--- page 19 ---

vm.runInNewContext, and obtain 10, 11, and 16 candidateproperties, respectively. The usage of these properties is fur-ther analyzed in the Node.js' codebase, using static analysis.We note that the inputs used for driving the dynamic anal-ysis are by no means exhaustive. We probably cover only asmall part of the target APIs in our tests, potentially missingproperty accesses that only happen when the API is invokedwith certain arguments. Nonetheless, for such cases, the re-sulting gadgets would be of limited use, as they would requirethe target application to pass those exact arguments to triggerthe gadget. Instead of being comprehensive in our test case,we focus on the typical usages of the target APIs, which webelieve yields easy-to-trigger gadgets.Given the low number of properties detected in this step,one could directly fuzz these properties and build proof-of-concept exploits. However, we further trace their usage insidethe Node.js codebase to understand if they are exploitable.
6.2.2 Static AnalysisAs discussed in Section 4.2, our approach takes the JavaScriptsource code of Node.js and the property names from thedynamic analysis phase as input, and reports a call chainto reach a property read and a data ow from the propertyread to an internal function invocation. We only analyze theJavaScript code from the folderlibof the repository [8]. Theanalyzed codebase contains 70,493 lines of code (LOC).In total, we identify 778 exported functions that reach theproperty reads (sources), and 342 in which values read fromthese properties ow into internal functions (sinks). We notethat while inspecting all these code locations rigorously re-quires a signicant amount of manual effort, we opt for prag-matic exploration: we rst analyze the sink and decide if theinvoked API, usually a native binding to the C/C++ code, is arelevant injection sink. If so, we continue with inspecting thesources to see which JavaScript APIs we can use to reach aparticular code location.Let us consider the case ofshell, a universal prop-erty identied by our dynamic analysis. The static analy-sis identies 8 sources, meaning that the reads ofshellare reached from eight Node.js exported functions, mostlyfrom the lelib/child_process.js. By propagatingtaints from all detected property reads, we identify 11function invocations in which the tainted value leavesthe JavaScript world. One of them is located in the lelib/internal/child_process.jsand is a call to the na-tivespawnSyncin the C++ bindings. By studying the bind-ings and the way they are invoked, we conclude that theshell
universal property is a candidate for developing a gadget.We thus proceed to further study the operations performedon the value stored in the universal property inside the Node.jscodebase. CodeQL provides great support in this step, allow-ing us to jump at the relevant code locations where this valueis read and then manipulated. We already know from the dy-namic analysis step that the Node.js core performs a readfrom this universal property when the functionspawnSyncisinvoked, but by running a call graph reachability analysis weidentify four other APIs that reach one of the sources.We build a simple test case to rst pollute theshellprop-erty with the valuetouchand then invoke one of the affectedJavaScript API, i.e.,spawnSync. By observing the side-effectof this test case, i.e., the le creation in the current directory,we conclude that if an attacker can polluteshell, the APIunder test uses its value as command, instead of the argumentpassed by developers. We next discuss this gadget and others.6.2.3 Universal GadgetsWe open source all the detected gadgets for Node.js in aGitHub repository [42]. Table 1 overviews the gadgets for thetarget Node.js version. Some of the gadgets are OS-specic,while most of them run on both considered OSs. We empha-size the diverse set of universal properties involved, showingthat gadgets are not isolated buggy cases, but they are com-mon place. These gadgets correspond to a handful of targetAPIs inside the Node.js core, but that a motivated attackercan probably nd many more inside the codebase of a targetapplication. Finally, as we discuss below, some gadgets allowarbitrary code execution with a relatively strong precondition,while others allow hijacking the control ow with a weakerprecondition. More importantly, an attacker can combine twosuch gadgets to get the best of both worlds.We now discuss some of our most important gadgets andtheir assumptions to be fullled. Let us consider an applica-tion that invokes the
execSync
API with a string literal:
1
const
{ execSync } = require('child_process ');
2
console.log(execSync('echo "hi"').toString ());This benign looking code prints the stringhiin the console.Staicu et al. [45] report that such API calls are prevalent inthe NPM ecosystem, but they consider safe all call sites withconstants as arguments, like the one above. That is becausethey assume an attacker cannot manipulate the command'svalue as it is set to a xed value by developers. We nd thatthis assumption does not hold in the presence of prototypepollutions. If attackers can pollute arbitrary properties in theruntime, they can hijack both the command to be executed andits environment variables. Consider the polluted properties:
1
Object.prototype.shell = "node";
2
Object.prototype.env = {};
3
Object.prototype.env.NODE_OPTIONS =
"--inspect -brk =0.0.0.0:1337";They trick the benign code above into spawning a newNode.js process with the debug port open, acting as a reverseshell. This is because the polluted propertyshelloverwritesthe command given by developers andenv.NODE_OPTIONSis set as environment variable of the current process and sub-sequently copied to all children processes.

--- page 20 ---

USENIX Association
32nd USENIX Security Symposium 5529

--- page 21 ---

IDUniversal propertiesTriggerImpactOSG
1shell
,
envCall command injection APIExecute an arbitrary commandL+WG
2shell
,
envCall command injection APIExecute an arbitrary commandLG
3shell
,
inputCall command injection APIExecute an arbitrary commandWG
4mainImport a package without a declared "main"Import an arbitrary le from the disk
L+WG
5mainRequire a package without a declared "main"Require an arbitrary le from the disk
L+WG
6exports
,
1Require a le using a relative pathRequire an arbitrary le from the disk
L+WG
7'=C:'Resolve a le pathResolve the path to a different leWG
8contextExtensionsRequire a le using a relative pathOverwrite global variables of the leL+WG
9contextExtensionsCompile function in a new contextOverwrite function's global variablesL+WG
10shell
,
env
,
mainRequire a package without a declared "main"Execute an arbitrary commandL+WG
11shell
,
env
,
exports
,
1Require a le using a relative pathExecute an arbitrary commandL+W Table 1: A summary of the identied Node.js universal gadgets. For each gadget, we show the properties that the attacker mustpollute beforehand, the action that triggers the gadget, and the produced effect. The last column shows the operating system onwhich the gadget works: Linux (L), Windows (W), or both (L+W).denotes gadgets for which we have a Windows variant thatachieves arbitrary command execution using the SMB protocol.The presented gadget affects all the APIs for commandexecution in Node.js:spawn,spawnSync,exec,execSync,execFileSync. A precondition for this attack is that the tar-get command execution call site should not explicitly set anoptions argument, e.g., for anexecSynccall, there shouldbe no second argument passed. The existence of this gadgetimplies that every Node.js application that is vulnerable toprototype pollution and uses a command execution API aftera pollution is vulnerable to remote code execution.Now consider an application that does not directly use suchAPIs in user-facing code. An attacker can still leverage codethat is present on the machine to trigger a command executionAPI. We found three gadgets that exploit therequireandimport
methods. Consider the following example:
1
Object.prototype.main = "./../../ pwned.js"
2
// trigger call
3
require('my-package')A precondition for this gadget is thatmy-packagedoes nothave amainproperty dened in itspackage.json. If themainproperty of the root prototype is polluted, at requiretime, the value of this property is used for retrieving the codeto be executed, instead of the legitimate code of the module.The attacker can thus indicate an arbitrary le on the disk to beloaded in the engine. In particular, they can specify a le thatcontains calls to command execution APIs. For example, thepopulargrowlpackage [6] contains a le calledtest.jsthatinvokes the package with different test values. Consideringthatgrowlusesspawninternally, the attacker can successfullytrigger such APIs call by setting themainproperty to pointto thegrowl's test le. Moreover, we identied a le shippedwith the NPM command line tool that can be used for thesame nefarious purpose:
npm/scripts/changelog.js
.To the best of our knowledge, the gadget above is the rstevidence ever reported that shows that hijacking control owthrough code reuse attacks is possible in Node.js. This moti-vates the need for debloating techniques like Mininode [28].In addition to the already alarming ndings, an attackercan combine the two gadgets discussed above to obtain apowerful universal gadget:
1
// pollutions for the first gadget
2
Object.prototype.main = "/path/to/npm/scripts/
changelog.js";
3
// pollutions for the second gadget
4
Object.prototype.shell = "node";
5
Object.prototype.env = {};
6
Object.prototype.env.NODE_OPTIONS =
"--inspect -brk =0.0.0.0:1337";
7
// trigger call
8
require("bytes");When thebytespackage is loaded, the rst gadget in-structs the engine to load thechangelog.jsle. This lein turn invokesexecSync, which triggers the second gadget,starting a Node.js process with a debugging session.Finally, let us present another gadget that lets attackersload arbitrary les into the engine. By polluting the rootprototype's properties1andexports, an attacker can executean arbitrary le from the disk when a relative path is loaded:
1
let
rootProto = Object.prototype;
2
rootProto["exports"] = {".":"./ changelog.js"};
3
rootProto["1"] = "/path/to/npm/scripts/";
4
// trigger call
5
require("./target.js");While performing relative path resolution, therequiremethod checks if the target path points to an ES6 module.During this process, the polluted property1is inadvertentlyread when applying a destructuring operator in the le/internal/modules/cjs/loader.js
:
1
const
{ 1: name , 2: expansion = "" } =
StringPrototypeMatch (...) || [];Thus, the attacker-controlled value is assigned as the tar-get module's name. Thereafter, therequiremethod wrongly

--- page 22 ---

5530 32nd USENIX Security Symposium
USENIX Association

--- page 23 ---

concludes that the relative path./target.jsresolves to theattacker-controlled location/path/to/npm/scripts/andthat the path corresponds to an ES6 module. Theexportsproperty is used to confuse therequiremethod further byproviding the entry point for this non-existing module. Al-though at the attacker-controlled target location, there is nopackage.jsonle present, therequiremethod still con-cludes that this is a valid module path. We note that thisgadget is not portable to legacy Node.js versions, e.g., version14.15.0. Thus, an important precondition for exploitation isthat the target system must use a recent Node.js version.We emphasize once again how dangerous the identiedgadgets are. Many fairly-large applications would probablymeet the preconditions for an RCE, once a prototype pollutionis in place: (i) require a le using a relative path or a packagewith nomainentry, and/or (ii) have a dependency that uses acommand execution API when loaded.To further study the impact of our gadgets, we estimate theprevalence of their triggers in an experiment with the 10,000most dependent-upon NPM packages. We measure that 1,958have nomainentry in their package.json (G
4,G
5,G
10), 4,420use relatives paths inside require statements (G
6,G
8,G
11),and 355 directly use the command injection API (G
1,G
2,G
3).This indicates that many of our gadgets could be deployedagainst clients of these packages, once a pollution is in place.However, this is an upper bound on the actual prevalence ofthe gadgets because: (i) the attacker may have a hard timeinvoking the trigger's code through the public interface of thepackage, e.g., the code using the command injection API, (ii)some gadgets may not work out of the box because of side-effects in the target package, i.e., polluting the property1mayhave many unintended side-effects that can prevent the gadgetfrom working, (iii) an attacker may nd it difcult to deploya pollution before the gadget, e.g., for the require gadgets,very often, the pollution needs to happen in the application'sinitialization phase. Nonetheless, considering the power ofthese gadgets and their widely-available triggers, prototypepollution should be considered a critical security vulnerabilityin the current Node.js landscape.
6.3 End-to-End ExploitationWe evaluate our approach on popular Node.js applicationsfrom GitHub to validate its usefulness in a practical setting.Setup.We use the GitHub API to search for JavaScript repos-itories and order them by the number of stars. We then selectfor further analysis the top 14 web applications running onNode.js, as well as NPM CLI, the JavaScript package man-ager, because it is installed on every machine with Node.jsas default. NPM CLI is also the largest analyzed applica-tion in our dataset. We clone the GitHub repository of eachapplication locally and perform the analysis against it.Methodology.Following the workow described in Section 4,we rst run ourPriorityquery withAny Functionsas entrypoints against a target application. The query reports the po-tential injection sinks and a list of the functions that passtainted data to these sinks. The list contains functions thatare actual entry points of the application and functions thattake data from the environment (e.g., a database) and passit to the injection sink. For the latter, we perform a call owanalysis to detect the application entry points. Second, wemanually classify all reported cases as either false positivesorlocally exploitable. Based on the project structure, we alsolter out cases in testing and client-side code. We discardthese cases because the code does not execute on the serverand cannot lead to RCE. Third, we study the application'sthreat model to detect conditions for exploiting the remain-ing (locally exploitable) cases. This is a manual process thatrequires studying the documentation and code of the applica-tion. We match the entry points pertaining to the threat modelwith the detected entry points leading to the injection sinks.Fourth, we verify the matched entry points dynamically bydeploying the application locally and generating a payload topollute thetoStringproperty. Whenever the payload fails,we rely on the debugger by examining code transformationsand validations along the path, and modifying the payload ac-cordingly. Finally, once the pollution is conrmed, we searchfor the gadgets that may lead to RCE, as described in Section6.2. If the gadget can be triggered after the execution of the in-jection sink, we change the payload to pollute gadget-specicproperties.Results.Table 2 presents the analysis results for 15 widely-used Node.js applications.Totalprovides the number of de-tected prototype pollutions in the application's codebase andthe total time for their manual analysis. The analysis ndscases in 8 applications, which we investigate and classifymanually.False Positivescontains the false positives dueto over-approximate analysis;Client-SideandTesting Codeshow the cases that do not execute on a server-side directly.We mark the remaining cases (columnSuspicious) for fur-ther investigation. Suspicious cases are locally exploitablepatterns, i.e., they can be exploited if an attacker controlsall function parameters. We veried the suspicious cases tond eight prototype pollutions (in NPM CLI, Parse Serverand Rocket.Chat) that are exploitable according to the threatmodel of these applications. We also found the gadgets thatlead to RCE as explained below. As a sanity check, we runthe original CodeQL baseline queries for NPM CLI and ParseServer applications, however, they do not detect exploitableprototype pollutions.To estimate the manual effort, we track the time to verifythe reported cases by one of the authors. A false positive takesan average of 2.6 minutes because the analysis affects a smallcode fragment. Similarly, non server-side code and testingcode take on average 3.8 minutes and 1.2 minutes, respec-tively. The analysis of suspicious cases takes more time anddepends on the quality of the documentation and application'scode. The time inSuspiciouscolumn includes the study of the

--- page 24 ---

USENIX Association
32nd USENIX Security Symposium 5531

--- page 25 ---

Application's RepositoryStarsLines of codeTotalExploitableSuspiciousTesting CodeClient-Side CodeFalse PositivesCasesTimeCasesTimeCasesTimeCasesTimeCasesTimeCasesTimetypicode/json-server57,2572,3740-----expressjs/express54,88314,4500-----meteor/meteor42,673202,213262550521041085930strapi/strapi40,724168,99835000035TryGhost/Ghost38,944125,696455015002312hexojs/hexo33,66621,0731400140000sahat/hackathon-starter32,4312,3260-----koajs/koa31,9104,5960-----RocketChat/Rocket.Chat31,059242,94951555115003500150balderdashy/sails22,08524,4450-----emberjs/ember.js22,034113,74966002401100310fastify/fastify21,04337,0490-----parse-community/parse-server19,045107,909732255322000025docsifyjs/docsify18,9467,6030-----npm/cli5,371713,6481560323606230130610 Table 2: Evaluation results for the applications' analysis.Casesshows the number of detected cases of a certain category;Timeshows the time in minutes to manually classify and validate these cases.threat model and the matching of detected entry points. TheExploitablecolumn includes the time to set up an application,debugging and verication of prototype pollution, search forgadgets, and combination of all attack ingredients. For exam-ple, most time for the Parse Server exploit was spend to nda race condition that triggers the injection and attack sinksin the correct order. For NPM CLI, a time-consuming taskwas to nd a way to store the payload to NPM Registry via amalicious package and subsequently parse it during the pack-age installation. The analysis and exploitation of Rocket.Chatrequired an LDAP server setup that provides a payload to theinjection sink, and the conguration of a custom synchroniza-tion with the LDAP server. This process is not fully describedin the ofcial documentation and required a lot of manualtesting of various options.We now describe the RCE exploits for two applicationsand refer to the extended material for full details [43].
6.3.1 Parse Server RCEsParse Server is an open source Backend-as-a-Service (BaaS)framework that provides REST APIs to object and le stor-age, user authentication, push notications, dashboard, anduses MongoDB or PostgreSQL as database. The Parse Serverhas pioneered BaaS systems in 2011 and has brought theserverless, low-touch deployment model to web and mobilebackends.Threat model.The Parse Server can be deployed as a self-hosted solution. In this scenario, an attacker can send anyrequests to the server, but cannot modify any settings on theserver. Therefore, we expect that an application must be se-cure in the default conguration. In the second scenario, weconsider the Parse Server as a part of cloud infrastructure,e.g., Back4App [1]. The attacker can create their own accountand become the administrator of that account. This allows theattacker to change some settings, for example, the webhooktriggers. This scenario puts any available conguration at riskfor attacks including the default conguration.Detecting sinks.Our static analysis framework detects 7unique injection sinks. We marked 5 cases as suspicious bymanual validation. One of the suspicious cases is located inthe sanitizer of database records as shown in Listing 3.
1
function
expandResultOnKeyPath(obj , key , res) {
2
if
(key.indexOf('.') < 0) {
3
obj[key] = res[key];
4
return
obj;
5
}
6
const
path = key.split('.');
7
const
firstKey = path [0];
8
const
nextPath = path.slice (1).join('.');
9
obj[firstKey] = expandResultOnKeyPath(
10
obj[firstKey] || {},
11
nextPath , res[firstKey ]);
12
return
obj;
13
}
Listing 3: Injection sink in Parse ServerThis function can be abused to polluteObject.prototype.If the attacker controls the input data and passes the value"obj.__proto__.evalFunctions"to the parameterkeyand the object{obj:{__proto__:{evalFunctions: 1}}}toresult, then sanitization sets the new propertyevalFunctions
to Object's prototype.Following our methodology, we perform a call ow anal-ysis to detect entry points for the injection sink. A handlerof the GET request triggers data reading from the databaseand then executes the vulnerable sanitizing code. Other de-tected injection sinks may be triggered via a PUT request bya payload delivered from a third-party webhook application.In order to detect potential RCE gadgets, we search inParse Server codebase for universal gadgets and functions thatevaluate the code at runtime, e.g.,eval. The analysis reportsa gadget using therequirefunction, where an attacker candirectly control its argument through a polluted property. Theanalysis also reports an attack sink in the ofcial MongoDB

--- page 26 ---

5532 32nd USENIX Security Symposium
USENIX Association

--- page 27 ---

BSON parser [2] that deserializes objects from a database, andcan evaluate JavaScript code stored in this object. However,the code evaluation is possible only if we set the congurationparameterevalFunctions, see Listing 4. This option is notdened by default, but the attacker can pollute the prototypeand bypass the if-statement condition in line 5.
1
const
evalFunctions =
2
options['evalFunctions '] ==
null
3
?
false
4
: options['evalFunctions '];
5
if
(evalFunctions)
6
eval(functionString);
Listing 4: Attack sink in Parse ServerExploitation.The attacker should rst pollute the prototypevia the injection sink and then trigger the attack sink in asecond request. A challenge to exploit prototype pollution isthat the polluted property may break the application workow.In this setting, the web request handler throws an exceptionwheneverObject.prototypeis polluted. Thereby, the at-tacker cannot successfully handle the requests in the requiredorder. However, we could bypass it using arace conditioninthe application workow.Four of the RCE exploits for Parse Server use the same gad-get and attack sink in Listing 4 as follows: First, the attackersends requests to store payloads in the database. Second, itsends the GET request to trigger the attack sink but delaysits execution in the database until the next request. Third, theexploit sends the PUT request to trigger the injection sinks.Because the rst request takes longer, a payload triggers the in-jection sink while another payload reaches the attack sink andexecutes arbitrary code. The fth exploit adapts therequire
gadget discussed in Section 6.2.3.
6.3.2 NPM CLI RCEsNPM CLI [9] is the command line client that allows develop-ers to install and publish packages to NPM registries. Duringa package installation, NPM CLI puts modules in place sothat Node.js can load them, manages dependency conicts,and may run the pre- and post-install scripts from the package.Threat model.The public NPM registry can be untrusted,e.g., by storing malicious packages. Since it is a shell tool thatis run on a developer's machine, RCE attacks have the highestimpact. NPM CLI has the option--ignore-scriptsto dis-able running scripts specied inpackage.jsonles. There-fore, the threat model considers the arbitrary script executionthat breaks out of the--ignore-scriptsag as unintendedRCEs. We have the following constraint: the injection andattack sinks should be available during the execution of thecommand that installs a malicious package.Detecting sinks.The static analysis reports 15 uniqueinjection sinks. We marked 8 cases as suspicious. Dueto the restricted threat model, we then focus on match-ing the detected cases to the threat model. When NPMCLI installs the package, it parses the congurationlenpm-shrinkwrap.jsonfrom the package regardlessof the option--ignore-scripts. NPM CLI then in-vokesdiff-applyandcopyPathfunctions from theparse-conflict-jsonpackage to parse the congurationle. Two of the suspicious cases are located in these functions.Section 3 describes the injection sink indiff-applyand theattack sink for the RCE exploitation. We veried manuallythat the exploitation in both cases leads to RCE.Exploitation.The NPM CLI invokes thespawnfunctionto run thegitcommands for git-located package depen-dencies. This happens after parsing the conguration les,and therefore, after the injection sink execution. The gitsupports the command execution via the environmentvariableGIT_SSH_COMMAND. If this environment variableis set, git uses the specied command, instead of ssh, toconnect to a remote system. Thereby, the attacker cancraft the package conguration le to initiate the calldiffApply({}, {path:['__proto__','env'], value:
{GIT_SSH_COMMAND: 'calc &'}, op: ADD})and waitfor thespawninvocation of the git command. This payloadtriggers arbitrary code execution, here launching a calculator.7 Related WorkThis section discusses closely related work targeting objectinjection vulnerabilities in general and prototype pollution inparticular. We also discuss related security analyses for theNode.js ecosystem and client-side JavaScript security.Prototype pollution vulnerabilities.The security commu-nity became aware of prototype pollution vulnerabilities in2018 in a white paper of Arteau [12] which uses dynamic anal-ysis to showcase feasibility in a number of Node.js libraries aswell as an end-to-end exploit in the Ghost CMS platform. Therisks and the impact of prototype pollutions has been mainlydiscussed in security practitioner forums [3], with the excep-tion of a handful of recent research papers [25,27,31,32,51].Notably, the work of Li et al. [31, 32] proposesobject de-pendence graphsto statically nd injection vulnerabilities inNode.js libraries, including prototype pollution. Object de-pendent graphs allow identifying prototype injection sinkssimilar to our multi-taint analysis, though with higher preci-sion due to the analysis of branch conditions. By contrast,our approach trades precision for scalability to analyze fully-edged applications and libraries. In addition, our key focusis on universal gadget identication and end-to-end exploita-tion which no prior work has addressed systematically so far.Kim et al. [27] develop DAPP, a static analysis tool to detectprototype injection sinks in Node.js libraries by means ofpattern analysis. DAPP's lightweight analysis results in lowprecision and recall, while focusing only on libraries. Therecent work by Kang et al. [25] explores prototype pollutionon the client-side to exploit a range of vulnerabilities (XSS,

--- page 28 ---

USENIX Association
32nd USENIX Security Symposium 5533

--- page 29 ---

cookie and URL manipulation) by using dynamic taint track-ing. Compared with static analysis, dynamic analysis maymiss some gadgets because of code coverage limitations, yetit can be helpful to validate the reachability of our injectionand attack sinks, which we currently do manually. Xiao etal. [51] study hidden property attacks in Node.js applications,a type of vulnerability which is related to prototype pollution.Object injection vulnerabilities.We classify POIVs in thegeneral context of object injection vulnerabilities (OIVs).Prior work studies OIVs targeting insecure deserializationby mean of static analysis in a variety of languages includ-ing Java [24, 36], PHP [15, 17, 21], .NET [35, 41], and An-droid [39]. The work of Dahse et al. [16,17] develops staticanalysis to systematically detect OIV gadgets in PHP applica-tions. Shcherbakov and Balliu [41] propose a static analysisfor detecting object injection patterns for .NET application,including the framework and libraries, and implement a toolcalled SerialDetector. Arguably, our work faces similar chal-lenges with scaling the static analysis to real-world languages,though in the more intricate context of JavaScript.Node.js ecosystem security.There is an increasing interestin studying the security of Node.js, both in academia and inindustry. Most prior work has concentrated on so-called soft-ware supply chain security, i.e., studying security problemsthat are prevalent in libraries: injections [22,32,45], hiddenproperty abuse [51], prototype pollution [31,32], maliciouspackages [20, 52], running untrusted code [11, 49, 50], Re-DoS [18,19,33,44], code debloating [28]. There is also initialevidence that these problems in libraries affect websites inproduction [31, 44]. We are the rst to show the existenceof universal gadgets in Node.js and to study the impact ofprototype pollution, beyond denial-of-service attacks.Static analysis for Node.js.Madsen et al. [34] propose aug-menting call graphs with information about event propagationto nd bugs in Node.js programs. Staicu et al. [45] advo-cate using intra-procedural data ow analysis to infer run-time policies for injection sinks. Nielsen et al. [37] introducefeedback-driven abstract interpretation for detecting injec-tion vulnerabilities in Node.js code. More recently, Nielsenet al. [38] show how modular call graphs can be used to re-duce false positives alerts in software composition analysis.Li et al. [31, 32] propose using object dependency graphsfor nding prototype pollution, injection, and path traversalvulnerabilities. We are the rst to propose using static taintanalysis for detecting universal gadgets.Client-side JavaScript security.Lekies et al. [30] study XSSvulnerabilities on the web using ne-grained dynamic taintanalysis. Hedin et al. [23] present JSFlow, a more sophisti-cated information ow analysis for detecting integrity andcondentiality problems in web applications. Recently, Lekieset al. [29] discuss how script gadgets can be used to bypassexisting cross-site scripting mitigation. Roth et al. [40] furtherstudy the effect of script gadgets on content security poli-cies. Steffens and Stock [48] present PMForce, a lightweightdynamic analysis augmented with forced execution for study-ing post message handlers. Khodayari and Pellegrino [26]propose JAW, a hybrid analysis tool based on code propertygraph, showing its usefulness by studying client-side CSRFvulnerabilities. None of the work above studies the relationbetween prototype pollution and injection vulnerabilities.
8 ConclusionWe presented the rst principled study on the impact of pro-totype pollution vulnerabilities in Node.js. We propose asemi-automated approach for detecting end-to-end exploits,consisting of three phases: (i) static analysis for detectingpollutions, (ii) hybrid analysis for detecting gadgets, and (iii)static analysis with human-in-the-loop for developing end-to-end exploits. We apply our approach to large codebases tond eight exploitable RCE vulnerabilities directly enabled byprototype pollution, and eleven universal gadgets [42] thatare shipped with the Node.js runtime. Finally, we show thatuniversal gadgets introduce a new threat in the Node.js ecosys-tem: hijacking the control ow of a program to (ab)use unusedcode available in the application's dependencies.AcknowledgmentsThanks are due to anonymous review-ers for the helpful feedback on this work. This work waspartially supported by the Swedish Foundation for StrategicResearch (SSF) under projects CHAINS and Trustfull, DigitalFutures, Google, and Wallenberg AI, Autonomous Systemsand Software Program (WASP) funded by the Knut and AliceWallenberg Foundation.
References
[1] Back4App.
https://www.back4app.com
.
[2]BSON Parser for node and browser.https://github.
com/mongodb/js-bson
.
[3]Client-Side Prototype Pollution and useful ScriptGadgets.https://github.com/BlackFan/
client-side-prototype-pollution
.
[4] CodeQL.
https://codeql.github.com
.
[5]Exploiting prototype pollution – RCE in Kibana (CVE-2019-7609).https://research.securitum.com/
prototype-pollution-rce-kibana-cve-2019-7609.[6]Growl - NPM. Growl support for Node.js.https://
www.npmjs.com/package/growl
.
[7]Node.js documentation.https://nodejs.org/api/
child_process.html
.

--- page 30 ---

5534 32nd USENIX Security Symposium
USENIX Association

--- page 31 ---

[8]Node.js JavaScript runtime v16.13.1.https://github.
com/nodejs/node/tree/v16.13.1/lib
.
[9]NPM - a JavaScript package manager.https://
github.com/npm/cli
.
[10] Snyk.
https://snyk.io
.
[11]Mohammad M. Ahmadpanah, Daniel Hedin, MusardBalliu, Lars Eric Olsson, and Andrei Sabelfeld. Sand-Trap: Securing JavaScript-driven trigger-action plat-forms. In
USENIX Security Symposium
, 2021.
[12]Olivier Arteau. Prototype pollution attack in NodeJSapplication.
NorthSec
, 2018.
[13]Pavel Avgustinov, Oege De Moor, Michael PeytonJones, and Max Schäfer. Ql: Object-oriented querieson relational data. In30th European Conference onObject-Oriented Programming (ECOOP 2016). SchlossDagstuhl-Leibniz-Zentrum fuer Informatik, 2016.
[14]Fraser Brown, Shravan Narayan, Riad S. Wahby, Daw-son R. Engler, Ranjit Jhala, and Deian Stefan. Findingand preventing bugs in JavaScript bindings. InSympo-sium on Security and Privacy (S&P)
, 2017.
[15]Johannes Dahse and Thorsten Holz. Static detectionof second-order vulnerabilities in web applications. InUSENIX Security 14
, pages 989–1003, 2014.
[16]Johannes Dahse and Thorsten Holz. Static detectionof second-order vulnerabilities in web applications. InUSENIX Security Symposium
, 2014.
[17]Johannes Dahse, Nikolai Krein, and Thorsten Holz.Code reuse attacks in PHP: automated POP chain gener-ation. InConference on Computer and CommunicationsSecurity (CCS)
, pages 42–53, 2014.
[18]James C. Davis, Christy A. Coghlan, Francisco Servant,and Dongyoon Lee. The impact of regular expressiondenial of service (ReDoS) in practice: an empirical studyat the ecosystem scale. InJoint Meeting on Foundationsof Software Engineering (ESEC/FSE)
, 2018.
[19]James C. Davis, Francisco Servant, and Dongyoon Lee.Using selective memoization to defeat regular expres-sion denial of service (ReDoS). InSymposium on Secu-rity and Privacy (S&P)
, 2021.
[20]Ruian Duan, Omar Alrawi, Ranjita Pai Kasturi, Ryan El-der, Brendan Saltaformaggio, and Wenke Lee. Towardsmeasuring supply chain attacks on package managersfor interpreted languages. InNetwork and DistributedSystem Security Symposium (NDSS)
, 2021.
[21]Stefan Esser. Utilizing Code Reuse/ROP in PHP Ap-plication Exploits.Proceedings of the Black Hat USA,2010.
[22]François Gauthier, Behnaz Hassanshahi, and AlexanderJordan. AFFOGATO: runtime detection of injectionattacks for node.js. InInternational Symposium on Soft-ware Testing and Analysis (ISSTA)
, 2018.
[23]Daniel Hedin, Arnar Birgisson, Luciano Bello, and An-drei Sabelfeld. JSFlow: tracking information ow inJavaScript and its APIs. InSymposium on Applied Com-puting (SAC)
, 2014.
[24]Philipp Holzinger, Stefan Triller, Alexandre Bartel, andEric Bodden. An in-depth study of more than ten yearsof java exploitation. InConference on Computer andCommunications Security (CCS), pages 779–790, 2016.[25]Zifeng Kang, Song Li, and Yinzhi Cao. Probe the proto:Measuring client-side prototype pollution vulnerabili-ties of one million real-world websites. InNetwork andDistributed System Security Symposium (NDSS 2022),2022.
[26]Soheil Khodayari and Giancarlo Pellegrino. JAW: study-ing client-side CSRF with hybrid property graphs anddeclarative traversals. InUSENIX Security Symposium,2021.
[27]Hee Yeon Kim, Ji Hoon Kim, Ho Kyun Oh, Beom JinLee, Si Woo Mun, Jeong Hoon Shin, and KyounggonKim. Dapp: automatic detection and analysis of proto-type pollution vulnerability in Node.js modules.Inter-national Journal of Information Security, pages 1–23,2021.
[28]Igibek Koishybayev and Alexandros Kapravelos. Minin-ode: Reducing the attack surface of Node.js applications.In23rd International Symposium on Research in Attacks,Intrusions and Defenses (RAID)
, 2020.
[29]Sebastian Lekies, Krzysztof Kotowicz, Samuel Groß,Eduardo A. Vela Nava, and Martin Johns. Code-reuseattacks for the web: Breaking cross-site scripting miti-gations via script gadgets. InConference on Computerand Communications Security (CCS), pages 1709–1723,2017.
[30]Sebastian Lekies, Ben Stock, and Martin Johns. 25million ows later: large-scale detection of DOM-basedXSS. InConference on Computer and CommunicationsSecurity (CCS)
, pages 1193–1204, 2013.
[31]Song Li, Mingqing Kang, Jianwei Hou, and Yinzhi Cao.Detecting Node.js prototype pollution vulnerabilitiesvia object lookup analysis. InProceedings of the 29thACM Joint Meeting on European Software Engineer-ing Conference and Symposium on the Foundations ofSoftware Engineering, ESEC/FSE 2021, page 268–279,New York, NY, USA, 2021. Association for ComputingMachinery.

--- page 32 ---

USENIX Association
32nd USENIX Security Symposium 5535

--- page 33 ---

[32]Song Li, Mingqing Kang, Jianwei Hou, and Yinzhi Cao.Mining Node.js vulnerabilities via object dependencegraph and query. InUSENIX Security Symposium, 2022.[33]Yinxi Liu, Mingxue Zhang, and Wei Meng. Revealer:Detecting and exploiting regular expression denial-of-service vulnerabilities. InSymposium on Security andPrivacy (S&P)
, 2021.
[34]Magnus Madsen, Frank Tip, and Ondrej Lhoták. Staticanalysis of event-driven node.js javascript applications.InProceedings of the 2015 ACM SIGPLAN Interna-tional Conference on Object-Oriented Programming,Systems, Languages, and Applications, OOPSLA 2015,part of SPLASH 2015, Pittsburgh, PA, USA, October25-30, 2015
, 2015.
[35]Alvaro Muñoz and Oleksandr Mirosh. Friday the 13thjson attacks.
Proceedings of the Black Hat USA
, 2017.
[36]Alvaro Muñoz and Christian Schneider. Serial killer:Silently pwning your java endpoints, 2018.
[37]Benjamin Barslev Nielsen, Behnaz Hassanshahi, andFrançois Gauthier. Nodest: feedback-driven static anal-ysis of node.js applications. InJoint Meeting on Eu-ropean Software Engineering Conference and Sympo-sium on the Foundations of Software Engineering, (FSE),2019.
[38]Benjamin Barslev Nielsen, Martin Toldam Torp, andAnders Møller. Modular call graph construction for se-curity scanning of node.js applications. InInternationalSymposium on Software Testing and Analysis (ISSTA),2021.
[39]Or Peles and Roee Hay. One class to rule them all: 0-daydeserialization vulnerabilities in android. InWOOT'15,2015.
[40]Sebastian Roth, Michael Backes, and Ben Stock. As-sessing the impact of script gadgets on CSP at scale.InAsia Conference on Computer and CommunicationsSecurity, (ASIA CCS)
, 2020.
[41]Mikhail Shcherbakov and Musard Balliu. SerialDe-tector: Principled and Practical Exploration of ObjectInjection Vulnerabilities for the Web. In28th AnnualNetwork and Distributed System Security Symposium,NDSS 2021, virtually, February 21-25, 2021
, 2021.
[42]Mikhail Shcherbakov, Musard Balliu, and Cristian-Alexandru Staicu. Server-Side Prototype Pol-lution Gadgets.https://github.com/yuske/
server-side-prototype-pollution
.
[43]Mikhail Shcherbakov, Musard Balliu, and Cristian-Alexandru Staicu. Silent Spring: Prototype PollutionLeads to Remote Code Execution in Node.js - Artifacts.https://github.com/yuske/silent-spring
.
[44]Cristian-Alexandru Staicu and Michael Pradel. Freezingthe web: A study of redos vulnerabilities in JavaScript-based web servers. InUSENIX Security Symposium,2018.
[45]Cristian-Alexandru Staicu, Michael Pradel, and Ben-jamin Livshits. SYNODE: understanding and auto-matically preventing injection attacks on Node.js. InNetwork and Distributed System Security Symposium(NDSS)
, 2018.
[46]Cristian-Alexandru Staicu, Sazzadur Rahaman, ÁgnesKiss, and Michael Backes. Bilingual problems: Study-ing the security risks incurred by native extensions inscripting languages.arXiv preprint arXiv:2111.11169,2021.
[47]Cristian-Alexandru Staicu, Daniel Schoepe, Musard Bal-liu, Michael Pradel, and Andrei Sabelfeld. An empiricalstudy of information ows in real-world JavaScript. In14th ACM SIGSAC Workshop on Programming Lan-guages and Analysis for Security, PLAS
, 2019.
[48]Marius Steffens and Ben Stock. PMForce: System-atically analyzing postmessage handlers at scale. InConference on Computer and Communications Security(CCS)
, 2020.
[49]Nikos Vasilakis, Ben Karel, Nick Roessler, NathanDautenhahn, André DeHon, and Jonathan M. Smith.Breakapp: Automated, exible application compartmen-talization. InNetwork and Distributed System SecuritySymposium, (NDSS)
, 2018.
[50]Nikos Vasilakis, Cristian-Alexandru Staicu, GrigorisNtousakis, Konstantinos Kallas, Ben Karel, André De-Hon, and Michael Pradel. Preventing dynamic librarycompromise on Node.js via RWX-based privilege reduc-tion. InConference on Computer and CommunicationsSecurity (CCS)
, 2021.
[51]Feng Xiao, Jianwei Huang, Yichang Xiong, GuangliangYang, Hong Hu, Guofei Gu, and Wenke Lee. Abusinghidden properties to attack the Node.js ecosystem. InUSENIX Security Symposium
, 2021.
[52]Markus Zimmermann, Cristian-Alexandru, Cam Tenny,and Michael Pradel. Small world with high risks: Astudy of security threats in the npm ecosystem. InUSENIX Security Symposium
, 2019.

--- page 34 ---

5536 32nd USENIX Security Symposium
USENIX Association

--- page 35 ---

Appendix
8.1 Evaluation ResultsIn Table 3, we present the results of the evaluation of ODGen, the original CodeQL queries (Baseline queries) and our customqueries (
Priority queries
and
General queries
) against our benchmark of 100 vulnerable NPM packages.Package@VersionLoCBaseline queriesPriority queriesGeneral queriesODGenPrototype
Polluting
AssignmentPrototype
Polluting
FunctionExported
FunctionsAny
FunctionsExported
FunctionsAny
FunctionsTPFPTPFPTPFPTPFPTPFPTPFPTPFP101@1.6.32,3660/200/202/202/202/222/220/20arr-atten-unatten@1.1.41040/200/201/101/102/202/200/20asciitable.js@1.0.21730/101/111/101/111/101/111/10assign-deep@1.0.0560/101/101/101/101/111/110/10bmoor@0.8.113,7184/621/604/404/406/606/603/60bodymen@1.0.017,9931/130/101/121/161/181/1100/10changeset@0.1.01,4273/310/301/101/103/303/300/30class-transformer@0.1.17350/200/202/202/202/202/200/20confucious@0.0.127,0467/710/704/434/457/747/741/71connie@0.1.013,4330/301/311/101/113/303/340/30controlled-merge@1.0.01710/302/302/212/213/313/313/30copy-props@2.0.43481/110/100/100/100/101/110/10deap@1.0.06980/202/200/202/210/202/211/22deep-defaults@1.0.517,4750/131/101/121/141/181/180/11deep-override@1.0.0730/100/101/121/151/191/190/10deep-set@1.0.0410/100/101/101/101/111/111/10deephas@1.0.53510/100/101/101/101/111/110/10deeply@3.0.02380/100/100/100/100/100/100/10deepref@1.1.11360/100/100/101/100/101/100/10deeps@1.4.52311/111/101/101/101/121/121/10defaults-deep@0.2.4890/100/100/101/101/101/100/10dot-object@2.1.25,5002/450/404/424/464/4104/4200/40dot-prop@2.0.0341/111/101/101/101/111/110/10dot-notes@3.2.02231/110/101/101/101/111/111/10dotty@0.0.14751/110/101/101/101/111/111/10dset@1.0.0181/111/111/111/111/111/111/10expand-hash@1.0.1360/100/101/101/101/111/110/10extend@3.0.1630/101/101/111/111/111/111/10eld@1.0.1764/400/402/202/204/404/401/40@rebase/util@0.3.24,7250/404/404/404/404/404/400/40attenizer@0.0.54360/100/101/101/111/111/130/10gammautils@0.0.816,9191/130/111/111/111/141/141/10gedi@1.6.37,1601/160/121/121/131/171/180/10getobject@0.1.01261/110/101/101/101/111/110/10hoek@5.0.07640/100/121/131/141/151/150/10immer@8.0.05,1360/500/500/515/520/515/520/50ini-parser@0.0.2321/100/101/101/101/101/101/10js-data@3.0.814,0560/131/151/1111/1141/1171/1380/10js-extend@0.0.1530/101/100/101/100/101/101/10js_ini@1.2.05370/100/101/101/101/101/100/10json-ptr@1.1.01,6301/130/101/151/151/151/150/10json8-merge-patch@1.0.16350/101/101/101/101/101/100/10just-extend@3.0.0360/100/100/100/100/100/101/10keyd@1.3.42650/100/100/101/110/101/111/10keyget@2.2.03891/400/402/222/224/414/412/40libnested@1.5.02101/110/101/101/101/111/111/10linux-cmdline@1.0.0420/100/101/101/101/111/111/10locutus@2.0.1114,9941/110/101/121/121/131/140/10lodash@4.17.1117,3021/130/101/111/131/171/171/10madlib-object-utils@0.1.6811/110/101/101/101/111/111/10merge@2.1.01030/101/101/101/101/101/100/10merge-deep@3.0.04830/300/300/200/213/303/302/30

--- page 36 ---

USENIX Association
32nd USENIX Security Symposium 5537

--- page 37 ---

merge-recursive@0.0.3581/110/101/101/101/111/111/10mixin-deep@2.0.0290/101/101/101/101/101/100/10mout@2.0.0-alpha.19,3370/220/202/202/202/212/210/20mpath@0.4.11,8391/120/101/121/121/121/121/12nconf_toml@0.0.14,7430/100/101/101/111/121/120/10nested-property@0.0.5970/100/101/101/101/111/110/10nestie@1.0.0660/100/101/101/101/111/110/10nis-utils@0.6.1035,6692/201/211/191/1152/2182/2182/20node.extend@2.0.09580/101/101/111/111/111/111/10node-forge@0.9.017,9781/150/101/121/141/171/171/10nodee-utils@1.2.222,3852/201/201/151/1122/2112/2152/20object-collider@1.0.31430/200/202/212/212/212/210/20object-path-set@1.0.01852/200/201/111/112/202/202/20objnest@5.0.09710/100/101/101/101/131/130/10objtools@3.0.020,6930/552/504/5145/5164/5245/5240/50patchmerge@1.0.01380/101/101/121/121/161/160/10paypal-adaptive@0.4.12030/101/111/111/121/121/120/10phpjs@1.3.248,1161/140/101/131/171/181/1180/10predene@0.1.24880/100/101/111/111/111/110/10promisehelpers@0.0.51321/110/101/101/101/111/111/10properties-reader@2.0.01,2930/100/101/121/121/171/170/10property-expr@2.0.21961/100/100/101/101/101/101/10prototyped.js@2.0.07,9110/100/101/101/101/101/101/10putil-merge@3.0.0680/200/202/202/202/222/220/20querymen@2.1.318,2051/130/101/121/161/181/1100/11safe-at@2.0.02980/100/101/101/101/101/100/10safe-object2@1.0.31040/100/101/101/111/101/110/10safe-obj@1.0.02420/100/101/111/111/121/120/10safetydance@2.0.15700/100/100/101/100/101/111/10set-deep-prop@1.0.0111/100/101/101/101/101/101/10set-getter@0.1.01790/100/100/100/101/111/110/10set-in@2.0.01721/100/101/101/101/101/101/10set-object-value@0.0.51130/200/202/242/242/262/261/20set-or-get@1.2.101151/100/101/101/101/101/101/10set-value@3.0.01232/211/201/101/102/212/212/20shvl@2.0.1180/100/101/101/131/111/140/10smart-extend@1.7.38,9490/101/111/121/131/121/130/10@strikeentco/set@1.0.0271/110/101/101/101/111/110/10supermixer@1.0.39,8430/120/100/150/190/180/1120/10Templ8@0.7.07850/100/100/100/100/100/100/10tiny-conf@1.1.02554/400/402/202/214/404/411/40total.js@3.4.640,6990/130/110/110/120/140/170/10undefsafe@2.0.25440/100/101/101/101/101/100/10upmerge@0.1.71240/403/403/313/314/404/402/40utils-extend@1.0.82390/101/101/101/101/121/120/10worksmith@1.0.091,2940/140/100/171/1130/1191/1330/11y18n@3.2.11293/300/301/101/113/303/302/30yargs-parser@6.0.06776/620/602/242/256/636/630/60Total:42.146.621.367.382.249.693.340.188.435.39730.932.987.1Table 3: Evaluation results of our benchmark analysis. TheTPcolumns contain the number of detected cases / the total number of true positives for the package.TheFPcolumns contain the number of false positive cases for the package. TheTotalrow summarizes the data and presents the recall metric (in %) in theTPcolumns and the precision (in %) for the
FP
columns.

--- page 38 ---

5538 32nd USENIX Security Symposium
USENIX Association

--- page 39 ---

1functiondiffApply(obj,diff){2varlastProp=diff.path.pop();3varthisProp;4while((thisProp=diff.path.shift()) !=null){5if(!(thisPropinobj)) {6obj[thisProp]={};7}8obj=obj[thisProp];9}10if(diff.op===REPLACE||diff.op===ADD){11obj[lastProp]=diff.value;12}13}1

--- page 40 ---

1const{ArrayPrototypePush}=primordials;2const{Process}=internalBinding(Õprocess_wrapÕ);3functionspawn(file,args,opts){4opts=normalizeSpawnArgs(file,args,opts);5this._handle=newProcess();6this._handle.spawn(opts);7}89functionnormalizeSpawnArgs(file,args,opts){10letenvKeys=[],envPairs=[];11constenv=opts.env||process.env;12/*...*/13for(constkeyinenv)14ArrayPrototypePush(envKeys,key);1516for(constkeyofenvKeys){17constv=env[key];18ArrayPrototypePush(envPairs,Ô${key}=${v}Ô);19}2021return{/*...,*/envPairs/*,...*/};22}1

--- page 41 ---

ü +¯B�¯€ªÒ:BUà; Žc‡øqòfGk}Ô<:ÛââöÁ§1rÌfÔrÛí°zœ¬bH/=·¶wW·šúë½}‹óýgª�cö1šÅ4ÒW˜—Jg©±;�HP–¾LUF
U}¶é4mL¯ÏÑªn‡÷é›jƒ`gU$µX¥}@0Êo¯ž‘ä’WeRäC�
