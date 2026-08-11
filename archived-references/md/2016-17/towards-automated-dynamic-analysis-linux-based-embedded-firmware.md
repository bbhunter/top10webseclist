---
type: Whitepaper
title: Towards Automated Dynamic Analysis for Linux-based Embedded Firmware
resource: "https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:44:26+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf"
    title: Towards Automated Dynamic Analysis for Linux-based Embedded Firmware
    author: Daming D. Chen, Manuel Egele, Maverick Woo, David Brumley
also_at: []
authors:
  - Daming D. Chen
  - Manuel Egele
  - Maverick Woo
  - David Brumley
canonical_url: ""
cited_by:
  - "2016-17.md:69"
commit: ""
content_sha256: 686f1fdf2ed0c9346f694fb73760cbff0580f63b6eeb4b280c8519d39d941693
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: a88844595fe037215474deb87860cf29ebd3b68d5b832d3b3089b24ef800f888
retrieved_from: "https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:44:26+00:00"
slug: towards-automated-dynamic-analysis-linux-based-embedded-firmware
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Towards Automated Dynamic Analysis for Linux-based Embedded Firmware

**Towards Automated Dynamic Analysis for Linux-based Embedded Firmware** - Daming D. Chen, Manuel Egele, Maverick Woo, David Brumley, Publisher not stated.

- Published: date not stated
- Original: <https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf>
- Preserved from: https://www.ndss-symposium.org/wp-content/uploads/2017/09/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf (stored) on 2026-08-11
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Towards Automated Dynamic Analysis for Linux-based Embedded Firmware

--- page 1 ---

Towards Automated Dynamic Analysis for
Linux-based Embedded Firmware
Daming D. Chen

, Manuel Egele
y
, Maverick Woo

, and David Brumley


Carnegie Mellon University
{ddchen, pooh, dbrumley}@cmu.edu
y
Boston University
{megele}@bu.edu
Abstract
—Commercial-off-the-shelf (COTS) network-enabled
embedded devices are usually controlled by vendor rmware
to perform integral functions in our daily lives. For example,
wireless home routers are often the rst and only line of defense
that separates a home user's personal computing and information
devices from the Internet. Such a vital and privileged position in
the user's network requires that these devices operate securely.
Unfortunately, recent research and anecdotal evidence suggest
that such security assumptions are not at all upheld by the devices
deployed around the world.
A rst step to assess the security of such embedded device
rmware is the accurate identication of vulnerabilities. However,
the market offers a large variety of these embedded devices,
which severely impacts the scalability of existing approaches in
this area. In this paper, we present FIRMADYNE, the rst
automated
dynamic analysis system that specically targets Linux-
based rmware on network-connected COTS devices in a scalable
manner. We identify a series of challenges inherent to the dynamic
analysis of COTS rmware, and discuss how our design decisions
address them. At its core, FIRMADYNE relies on software-based
full system emulation with an instrumented kernel to achieve the
scalability necessary to analyze thousands of rmware binaries
automatically.
We evaluate FIRMADYNE on a real-world dataset of 23,035
rmware images across 42 device vendors gathered by our system.
Using a sample of 74 exploits on the 9,486 rmware images that
our system can successfully extract, we discover that 887 rmware
images spanning at least 89 distinct products are vulnerable to one
or more of the sampled exploit(s). This includes 14 previously-
unknown vulnerabilities that were discovered with the aid of
our framework, which affect 69 rmware images spanning at
least 12 distinct products. Furthermore, our results show that
11 of our tested attacks affect rmware images from more than
one vendor, suggesting that code-sharing and common upstream
manufacturers (OEMs) are quite prevalent.
I. I
NTRODUCTIONWith the proliferation of the so-called “Internet of Things”,an increasing number of embedded devices are being connectedto the Internet at an alarming rate. Commodity networkingequipment such as routers and network-attached storage boxesare joined by IP cameras, thermostats, or even remotely-controllable power outlets. These devices frequently sharecertain technical characteristics, such as embedded systemon a chip (SOC) designs based on ARM or MIPS CPUs,network connectivity via Ethernet or WiFi, and a wide varietyof communication interfaces such as GPIO, I2C, or SPI.Nevertheless, many of these devices are controlled by vendorand chipset-specic rmware that is rarely, if ever, updated toaddress security vulnerabilities affecting these devices.Unfortunately, the poor security practices of these devicevendors are only further exacerbated by the privileged networkposition that many of these devices occupy. For example, awireless router is frequently therst and onlyline of defensebetween a user's computing equipment (e.g., laptops, mobilephones, and tablets) and the Internet. An attacker that succeedsin compromising such a networking device is able to gainaccess to the user's network, and can further recongure thedevice to tamper with arbitrary network trafc. Since mostvendors have not taken any initiative to improve the security oftheir devices, millions of home and small business networks areleft vulnerable to both known and unknown threats. As a rststep towards improving the security of commodity computerequipment, we propose to address the challenge ofaccuratelyidentifying vulnerabilities in embedded rmware
head-on.Previous research on the security of embedded rmwarecan be categorized based on various analysis approaches. Forexample, Zaddach et al. [19] perform dynamic analysis bypartially ofoading execution of rmware to actual hardware.While such an approach is precise, it incurs signicant hurdlesfor large-scale analysis. First, the requirement that the analystmust obtain the physical hardware for the device undertest poses a signicant nancial burden. Second, and moreimportantly, the manual effort needed to identify and interfacewith the debugging port on the device places strict limits on thescalability of this technique, especially for consumer equipmentthat may not support hardware debugging functionality.In contrast, Costin et al. [8] utilize static analysis techniquesto unpack the rmware of embedded devices and identifypotentially vulnerable code or binaries inside. While thisapproach scales to thousands of rmware images, it suffersfrom the classic trade-offs of static analysis. Namely, either theanalysis is very generic and produces a large number of falsepositives [5], or the analysis is too specic and results in manyPermission to freely reproduce all or part of this paper for noncommercialpurposes is granted provided that copies bear this notice and the full citationon the rst page. Reproduction for commercial purposes is strictly prohibitedwithout the prior written consent of the Internet Society, the rst-named author(for reproduction of an entire paper only), and the author's employer if thepaper was prepared within the scope of employment.
NDSS '16, 21-24 February 2016, San Diego, CA, USA
Copyright 2016 Internet Society, ISBN 1-891562-41-X
http://dx.doi.org/10.14722/ndss.2016.23415

--- page 2 ---

false negatives. Additionally, static analysis techniques based onprogram analysis usually target a specic problem domain, suchas the C, PHP, or Java programming language, or alternativelybinary code. Unfortunately, commodity networking equipmenttypically contains an amalgamation of various programs andscripts, written in a variety of compiled or interpreted pro-gramming languages. Oftentimes, custom modications areeven made to the language runtime to cater to the uniquerequirements of embedded systems.To overcome the shortcomings of previous work in this area,we leverage software-based full system emulation to enablelarge-scale and automated dynamic analysis for commodityembedded rmware. Since our approach does not rely onphysical hardware to perform the analysis, it scales withadditional computational resources. Additionally, our fullsystem emulation approach transparently provides dynamicanalysis capabilities, regardless of the programming languageused to develop a specic application or script. Furthermore, weinherit the precision of other dynamic analysis techniques—ifthe analysis nds that a rmware image contains a vulnerability,then it provides actionable results in the form of a successfulexploit. Finally, we address a number of challenges that arecharacteristic for embedded devices, such as the presence ofvarious hardware-specic peripherals, storage of persistent con-guration in non-volatile memory (NVRAM), and dynamically-generated conguration les.We implementedFIRMADYNEto demonstrate our ap-proach to automated dynamic analysis. Using rmware imageles distributed on vendor support websites, we automaticallyunpack the contents to identify the kernel and extract thelesystem. Since the majority of these extracted rmware areLinux-based, we initially focus on support for Linux-basedrmware by pre-compiling modied Linux kernels. UsingtheQEMU[4] full system emulator, we are able to boot ourinstrumented kernels with the extracted lesystem from theoriginal rmware images. In order to collect a dataset of thesermware images,FIRMADYNEincludes a web crawler thatautomatically downloads metadata and rmware images fromvarious vendor websites, which are then fed into the dynamicanalysis system.However, even with full system emulation, an emulatedenvironment must be congured correctly to interact with thenetwork interfaces of the guest rmware. Therefore, our systeminitially emulates the guest in an isolated network environment,and monitors all network interactions to infer the correctconguration for subsequent analyses. Once this informationis collected,FIRMADYNEwill re-congure the emulatedenvironment with the inferred network conguration, enablingnetwork interaction between the emulated guest rmware andthe analysis host.With the aid of our analysis and introspection capabilities,we identied 14 previously-unknown vulnerabilities for whichwe were able to manually develop proof-of-concept exploits.Of these, across our dataset of 23,035 rmware imagesgathered from 42 device vendors, we identied 69 vulnerablermware images spanning at least 12 distinct products fromthe 9,486 rmware images that were successfully extracted.Since the process of emulating and testing rmware images inFig. 1: Architectural diagram ofFIRMADYNEshowingthe emulation life-cycle for an example rmware image, asdescribed in §II-A.FIRMADYNEis automated, it was straightforward to integratea subset of the existing exploits from the popular MetasploitFramework [2].Using these results, we observe that the most prolic exploitaffects the rmware of up to ve different vendors, and the mosteffective exploit affects 10% of all network inferred rmwareimages in our dataset. While code-reuse of vulnerable open-source applications is one explanation, our attacks also affectapplications whose source is not publicly available, suggestingthat code-sharing and common upstream manufacturers (OEMs)are quite prevalent.To summarize, the contributions of this work are as follows:We presentFIRMADYNE, our implementation of anautomated and scalable dynamic analysis technique specif-ically designed to accurately identify vulnerabilities inLinux-based embedded rmware (§II).
Our implementation ofFIRMADYNEaddresses char-acteristic challenges of embedded systems, such as thepresence of hardware-specic peripherals, usage of non-volatile memory (NVRAM), and creation of dynamically-generated les (§IV).
We gathered a dataset of 23,035 rmware images down-loaded from 42 different vendors, and evaluatedFIR-MADYNEon the 9,486 rmware images that weresuccessfully extracted, using a set of 14 previously-unknown and 60 known exploits (§V).
In support of open science, we make our system availableto the research community under an open-source licenseto encourage further research into embedded systems.For more information, please see https://github.com/rmadyne/.
2

--- page 3 ---

NetworkIdentificationNetworkReachableExploitVerificationeth0: 192.168.1.100eth1: 192.168.1.101eth2: 192.168.1.102FTPSitesSupportWebsitesFilesystemKernelArchitectureIdentification&& cat 0xDEADBEEFInitialEmulationMIPSLittle-Endian

--- page 4 ---

II. O
VERVIEWIn this section we describe the design of various componentsthat compriseFIRMADYNE, and our motivations for such anarchitectural design.
A. ComponentsAs depicted in Fig. 1,FIRMADYNEconsists of four majorcomponents.
1)Crawling Firmware:The rst and largely independentcomponent is a web crawler, which downloads rmware imagesfrom vendor websites. At present, we support 42 device vendors(see §IV-A). We manually wrote parsing templates for each ofthese websites, allowing us to distinguish between rmwareimages and other binary content. This targeted crawling effortprovided us with metadata for each gathered rmware image,including information such as the build date, release version,and links to Management Information Base (MIB) les forthe Simple Network Management Protocol (SNMP). Suchmetadata proved useful for our automated analyses and exploitdevelopment (see §V-B3). For dynamic websites that weredifcult to crawl automatically, we instead crawled the vendor'sFTP site, at the expense of no metadata.
2)Extract Firmware Filesystem:In the second step,FIR-MADYNEuses a custom-written extraction utility built aroundthebinwalk[1] API to extract the kernel (optional) and theroot lesystem contained within a rmware image (see §IV-B).3)Initial Emulation:Once a lesystem is extracted,FIR-MADYNEidenties the hardware architecture of the rmwareimage; in Fig. 1, we have chosenMIPS Little-Endianas an example. Then, our system uses a pre-built Linux kernelin an instance of theQEMUfull system emulator that matchesthe architecture, endianness, and word-width of the targetrmware image. Currently three combinations are supported:little-endian ARM, little-endian MIPS, and big-endian MIPS.An initial emulation is performed to infer the system andnetwork conguration, shown as three IP address assignmentstoeth0,eth1, andeth2for the example in Fig. 1. Thisis achieved by intercepting system calls to the lesystem,networking, and other relevant kernel subsystems.
4)Dynamic Analysis:The forth and nal step can berepeated for any dynamic analysis supported byFIRMADYNE.To this end, the environment is dynamically recongured tomatch the expectations of the rmware image (see §IV-C)as inferred in the previous step. Note thatFIRMADYNEis designed for easy extensibility to include new dynamicanalyses or exploits. The results of each individual analysis areaggregated in a database for ease of inspection. In the exampleabove, shown in Fig. 1, a command injection vulnerability isbeing tested on the target rmware image.To illustrate this versatility, we have developed threevulnerability detection passes, which are able to assist innding vulnerabilities and precisely identify whether a givenexploit succeeds by monitoring events from our instrumentedkernel. These passes helped us detect 14 previously unknownvulnerabilities, which were automatically conrmed to affect69 rmware images, based on proof-of-concept exploits thatwe developed (see §V-B). We further demonstrate the exibilityofFIRMADYNEby seamlessly integrating 60 known exploitsmostly from the popular Metasploit [2] exploit framework. Intotal, both vulnerability types affect 887 rmware images fromour dataset.
B. MotivationDynamic analysis targeting embedded system rmwareaddresses a variety of design points in the abstraction hierarchyof embedded systems. We discuss a selection of potentialvantage points for such analysis, illustrate challenges andshortcomings, and argue why dynamic analysis based on fullsystem emulation is the most promising approach to tackle thischallenge.
1)Application-Level:Perhaps the most straightforwardapproach is to statically extract application-specic data, andexecute it natively with a supported application. For example, itis possible to copy the webpages served by a web server withinan embedded system, and serve the content using a regularweb server such as Apache. Unfortunately, this approach hasmultiple drawbacks that are incompatible with our design goalof creating a generic platform for dynamic analysis of embeddedrmware.An analysis of the rmware images in our dataset showsthat many of these contain webpages which rely on non-standard extensions to server-side scripting languages (e.g.,PHP) for access to hardware-specic functionality, such asNVRAM values. For example, hundreds of images in ourdataset make use of the custom functionsget_conf()inPHPandnvram_get()inASP.NETto obtain deviceconguration values. Unfortunately, this functionality is acustom addition to the web server that is not supported bytheir upstream open-source counterparts. Additionally, otherrmware images do not place these webpages on the lesystem,but instead embed their HTML content within the binary of acustom web server.Finally, an analysis approach focused on application-datacan only detect vulnerabilities within the application-specicdata (e.g., command injection vulnerabilities inPHPles), butnot those present within the original application or other systemcomponents.
2)Process-Level:Another feasible approach for analyzingembedded systems is to emulate the behavior of individualprocesses within the context of the original lesystem. Thiscan be achieved by executingQEMUin user-mode as a singleprocess emulator, constrained usingchrootto the originallesystem. Thus, one could simply launch the original webserver from the rmware image inQEMU, and then that processwould emulate the router web interface.Unfortunately, this approach only partially obviates theconcerns mentioned above. While an application would beable to execute within the context of the lesystem, specichardware peripherals (e.g., NVRAM) are still unavailable. Asa result, when an application attempts to access the NVRAMperipheral via
/dev/nvram
, it will likely terminate in error.Similarly, minor differences in the execution environmentcan have a signicant effect on program behavior. For example,thealphafsweb server used by multiple rmware images3

--- page 5 ---

veries hardware-dependent product and vendor IDs beforeaccessing NVRAM. If these values are not present at prede-termined physical memory addresses, the web server ceasesoperation and terminates with an error message. To this end, theweb server uses themmap()system call to access memory via/dev/mem, and checks specic offsets for theProductID
and
VendorID
of supported EEPROM chips.Emulating such behavior with a user-mode emulator wouldbe complex, as the emulator would need to track le handles andsystem calls that map memory to determine program behavior.Then, the emulator would need to identify the semanticdenition of various memory addresses, and replace the valuesas appropriate (e.g., a valid
ProductID
and
VendorID
).Additionally, due to limited write cycles on the primarystorage device, many rmware images mount a temporarymemory-backed lesystem at boot for volatile data. Thislesystem is mounted and generated dynamically. As a result,the directories/dev/and/etc/may be symbolic links tosubdirectories within the temporary lesystem, thus appearingbroken when examined statically. For example, the rmwarefor the D-Link DIR-865L wireless router uses a startupscript to populate conguration for applications, including thelighttpdweb server. This conguration le is then passed tothe web server binary with the`-c'command line argument.As a result, simple dynamic emulation of thelighttpdbinarywill fail, even with the original lesystem in place.These types of environmental differences can have asignicant effect on the presence of vulnerabilities. For example,many information disclosure vulnerabilities can simply be xedwith proper access control policies. Likewise, the effect ofa directory traversal attack on a web server can be greatlyaffected by the system conguration.Although this approach is clearly more accurate than theprevious approach, it should be apparent that it suffers from anumber of shortcomings due to low emulation delity. Withoutprecise knowledge of the runtime system environment, thehost environment can inadvertently affect dynamic analysis ofindividual processes by altering program execution.
3)System-Level:In comparison, a system-level emulationapproach is able to overcome the aforementioned challenges.Expected interfaces to hardware peripherals will be present,allowing their functionality to be gracefully emulated. Accurateemulation of the system environment permits dynamically-generated data to be created in the same manner as on the realdevice. All processes launched by the system can be analyzed,including various daemons responsible for protocols such asHTTP, FTP, and Telnet.During the design process, we explicitly chose full systememulation as the basis forFIRMADYNEfor these reasons.By leveraging the built-in hardware abstraction provided bythe kernel, we replace the existing kernel with our modiedkernel specically designed and instrumented for our emulationenvironment. Then, in conjunction with a custom user-spaceNVRAM implementation, we boot the extracted lesystemand our pre-built kernel within theQEMUfull system emulator.Otherwise, booting the original kernel would result in a fatalexecution crash, since it is only compiled to support a specichardware platform. Using the system boot sequence providedby theinitandrcSbinaries on the original lesystem, weare able to initialize user space to a state consistent with theoriginal device, despite platform changes.Our results (see §V-A) show that this approach is successfulfor initial emulation of over 96.6% of all Linux-based rmwareimages in our dataset. This is likely due to the stable andconsistent interface between user-space and kernel on Linuxsystems, with the exception of customIOCTL's introduced byvendor-specic kernel modules. In fact, Linux kernel developerswill revert kernel changes that break backwards-compatibilityfor user-space applications; for example, programs built forpre-0.9 (pre-1992) kernels will still function correctly even onthe latest kernel releases.
1However, this does not hold for kernel modules; indeed,one of the drawbacks of our current implementation is the lackof emulation support for out-of-tree kernel modules located onthe lesystem and so differences in kernel version may resultin system instability. Nevertheless, our dataset shows that suchsupport is generally not necessary, as more than 99% of allout-of-tree kernel modules within the rmware images in ourdataset are not useful for our system (§V-A3). One major reasonis because newer kernels, such as those that we build, providein-tree equivalents for functionality previously developed asout-of-tree extensions. In particular, 58.8% of out-of-tree kernelmodules are used to implement various networking protocolsand ltering mechanisms that may not have been present inolder kernels, and 12.7% provide support for specic hardwareperipherals. For example, older 2.4-series mainline kernelslackednetfilterconnection tracking and NAT support forvarious application-specic protocols such as TFTP, G.323,and SIP, which became available in-tree around kernel version2.6.20. In comparison, the third-party NetUSB kernel module,which was recently identied to contain a remotely-exploitablebuffer overow vulnerability, comprises less than 0.2% of allkernel modules from our dataset (§V-A3).
III. C
ONCEPTThis section provides an overview of the concept behind ourdynamic analysis framework for Linux-based rmware images.For specic challenges encountered and implementation details,please see §IV.
A. ArchitectureAs shown in Fig. 1, our system features a rmwarerepository server that is used to store the binaries correspondingto each rmware image and a database that keeps track ofinformation pertaining to each rmware image. This includesthe extraction status, architecture, brand of each image, as wellas each le within a given image.A set of virtualized worker nodes are used to extract theroot lesystem and kernel (optional) from each rmware image.Throughout this process, the database is updated with thecurrent experiment progress. If the extraction is successful,the rmware repository will cache the archived lesystem.Next, these workers enter the learning phase, where rmware1
https://www.kernel.org/doc/Documentation/stable_api_nonsense.txt
4

--- page 6 ---

images are assigned a default conguration and the networkinginteractions are recorded. This allows our system to infer thecorrect emulated network environment. Finally, the workersenter the analysis phase, where each rmware image is emulatedwith the inferred network environment, and individual analysesare performed.
B. AcquisitionIn order to gather a representative dataset of rmwareimages, we developed a custom web crawler. Instead of usinga blind crawling methodology, we wrote smart parsers for thesupport pages of each of our 42 preselected vendors (§A). Thisallowed us to distinguish between rmware updates and unde-sired binaries such as drivers, conguration utilities, and otherbinaries. Additionally, with a better semantic understandingof the target website, we recovered important metadata abouteach rmware image, such as vendor, product name, releasedate, version number, changelog, etc.Where applicable, this was supplemented with probablermware images that were mirrored from the FTP websitesof target vendors. Although this latter source of rmware wasless rich in metadata, it provided us with additional binariesthat were not directly accessible for all end-users, includingbetas and test binaries with limited releases. A few brands ofrmware images, for which it was difcult to automate, orwhen the vendors did not provide direct rmware downloadsfor end-users, were gathered by hand.
C. ExtractionWe developed a custom extraction utility using the APIof thebinwalkrmware extraction tool to recover the rootlesystem and (optionally) kernel from each rmware image.These were normalized by storing them as compressedTAR
archives within our rmware repository.
D. EmulationOnce the root le system has been extracted from a rmwareimage,FIRMADYNEperforms a series of analysis steps toinfer the system conguration expected by the rmware image.First, we examine theELFheader of binaries located withinthe extracted root lesystem to identify the target architectureand endianness. For each rmware image, we use theQEMUfull system emulator for the corresponding architecture to bootthe extracted lesystem with a matching kernel. Currently, wehave pre-compiled kernels for ARM little-endian, MIPS little-endian, and MIPS big-endian platforms, as our data shows thatthese architectures constitute 90.8% of our dataset (§V-A1).Next, during the initial emulation phase, the system isexecuted in a special “learning” mode, in which our modiedkernel records all system interactions with the networkingsubsystem, including IP address assignments for individualnetwork interfaces.Finally, after collecting this information,FIRMADYNEenters the actual emulation phase, in which a matchingnetwork environment is congured to communicate with theemulated rmware. To verify successful network conguration,FIRMADYNElaunches the emulated rmware image andperforms a series of network connectivity checks.
E. Automated AnalysesWe implemented three basic automated analysis passeswithin our dynamic analysis framework in order to demonstratethe effectiveness of our system. These contributed to ourdetection of 14 previously-unknown vulnerabilities that affect69 rmware images, and a total of 74 vulnerabilities that affect887 rmware images (see §V).
IV. I
MPLEMENTATIONThis section discusses the implementation behind each ofthe components mentioned in §II-A and §III.
A. AcquisitionOur custom web crawler was developed using theScrapyframework, with an individual spider written for each ofthe 42 vendors in our dataset. To increase representativeness,our dataset includes vendors for networking products rangingfrom consumer to professional network equipment, such asIP cameras, routers, access points, NAS's, smart TV's, cablemodems, satellite modems, and even third-party or open-sourcermware. We created individual parsers for the support pagesof each vendor using XPath selectors to enumerate and expandspecic elements of input webpages. In addition, we alsoattempted to crawl multiple geographic locations of eachvendor's website, including United States (English), China(Chinese), Russia (Russian), European (English), Germany(German), and South Africa (English).Some vendors that made heavy use of dynamically-generated content on their websites, such as D-Link and ZyXEL,were crawled through their FTP mirror site instead. OnlyFTP les that appeared relevant were downloaded, which wasgenerally limited to the following lename extensions:img,chk,bin,stk,zip,tar,sys,rar,pkg, andrmt. Othervendors, such as Cisco, which made their website difcult toautomatically crawl, or limited most rmware downloads tocustomers with valid support contracts, were manually crawled.Supported metadata elds that were automatically gatheredfrom vendor websites include the product name, vendor name,version, build, date, changelog, SNMP MIB le, source codeURL, and rmware image URL. This allows us to distinguishbetween multiple products that share the same rmware image,since we deduplicate downloaded rmware image binaries.However, not all vendors had such information available, andno metadata was available for vendors crawled through FTPor manually.
B. ExtractionThrough manual experimentation, we determined that thebuilt-in recursive extraction mechanism (“Matryoshka”) withinbinwalkwas insufcient for our purposes. In particular, thisextraction was vulnerable to path explosion by attemptingto recursively extract compressed data from within an ELFexecutable or every le within a lesystem, and not guaranteed5

--- page 7 ---

to terminate, especially in the presence of false positivesignature matches.Instead, we developed a custom goal-driven extraction utilityusing thebinwalkAPI that minimized disk space and runtimeby terminating when our extraction goals were achieved; namelyobtaining root lesystem and (optionally) kernel from withineach rmware image. In addition, we implemented a set ofheuristics for early detection of non-rmware les, whichwould otherwise waste computational resources. This includedblacklisting input les that were any type of structured binary,including PE32 executables for Windows, ELF executables forLinux, and universal binaries for Macintosh, as well as bytecodeand relocatable objects. Other common formats that wereexcluded included PDF les and Microsoft Ofce documents,which would otherwise appear as compressed archives thatrequire recursive extraction.After blacklist verication, the extraction process used a setof priority-ranked signatures that were executed sequentially inthe order of condence. These signatures can be categorizedas follows: archive formats, rmware headers, kernel magicor version strings, UNIX-like root lesystems, and nallycompressed data. Matches for archive formats or compresseddata were then extracted recursively. We verify that UNIX-likeroot lesystems are successfully extracted by checking for thepresence of at least four standard root directories from a subsetof the Filesystem Hierarchy Standard
2
.Our method allowed us to reduce the effect of false positivesignature matches by prioritizing higher-condence signaturematches (e.g., rmware headers) over more generic signaturematches (e.g., compressed GZIP data). For example, if upstreambinwalkdetects compressed data within the kernel image ofa rmware image and recursive extraction is enabled, it willwaste resources attempting to fully extract this data.Another improvement that we made to the extraction processwas utilizing the third partyjeffersonandsasquatchextraction tools forJFFS2andSquashFSlesystems, re-spectively, which can be difcult to extract. This is because theuserspace extraction utilities provided by lesystem developers,jffsdumpandunsquashfs, frequently fail to extract real-world lesystems of these types.In part, this is because these user-mode extraction utilitiesare rarely updated and can lag behind the in-kernel lesystemcode in terms of lesystem support. More importantly, manydevice manufacturers have modied existing compressionalgorithms or even implemented new compression algorithmsfor these lesystems, making their variants incompatible withother implementations.To resolve this problem, other rmware extraction utilitiessuch asbatandfirmware-mod-kitrely on a set ofheuristics and precompiledunsquashfsbinaries gatheredfrom the GPL source code releases for various routers. However,this approach is incomplete and ineffective, as maintainers forthese extraction utilities need to manually compile new binariesand implement the appropriate heuristics.2
http://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdfIn contrast, we utilize tools that are specically writtento extract the contents of these modied lesystems fromuserspace.sasquatch, which was developed by the authorofbinwalk, is designed to support as many modiedSquashFSimplementations as possible by adapting to changesin compression algorithms, and recognizing the structure ofSquashFS
lesystems instead of specic magic strings.During this process, we identied a number of bugs andmade improvements to bothbinwalkandjefferson,which were submitted to the respective upstream projects. Themajority of our submitted patches have already been mergedinto the ofcial release, and some are still pending maintainerreview.Although these improvements contribute to our successrates, not all rmware images can be extracted by our currentimplementation. For example, some vendors only distributepartial rmware images for their products, preventing us fromreconstructing the root lesystem. Other vendors distributermware images with multiple embedded or partial lesystems,which require additional logic to reassemble partial lesystems,or lesystems mounted on top of one another. Furthermore,other vendors distribute encrypted rmware images, rmwareimages within a binary updater executable, non-Linux-basedrmware images, or Linux-based rmware images with un-recognized lesystems, all of which we do not support. As aresult, these images are categorized as unknown in Table II.
C. Emulation
1)NVRAM:From a cursory inspection, at least 52.6% ofall extracted rmware images (4,992 out of 9,486) access ahardware non-volatile memory (NVRAM) using a shared librarynamedlibnvram.soto persist device-specic congurationparameters. For routers and other networking equipment,this includes settings shown on the web-based congurationinterface, which can include wireless network settings, networkadapter MAC addresses, and access credentials for the webinterface.Since this peripheral is typically abstracted as a key-value store, we developed a custom userspace library thatintercepts calls to NVRAM-related functions, such asconst
char
*
nvram_get(const char
*
key)andint
nvram_set(const char
*
key, char
*
val), whichare respectively used to get and set parameters from NVRAM.By modifying the system environment passed by the kernelto theinitbinary to include this library viaLD_PRELOAD,we ensure that all userspace processes inherit the sameenvironment, since they are child processes ofinit. Atemporary mountpoint on the lesystem is used as the root ofour key-value store, allowing us to reimplement this interfacein userspace without emulating hardware-specic peripherals.During testing, a common challenge we encountered wasthat our dataset of rmware images was compiled with differentC toolchains, some of which we do not have access to. Asshown in §V-A, this diversity was problematic for our sharedlibrary, since all dynamically-loaded ELF binaries must specifythe path to the dynamic loader for which they were compiled,as well as the lenames of dynamically-loaded dependencies,which were different depending on the system.
6

--- page 8 ---

Initially, we attempted to resolve this problem by compilingour NVRAM implementation statically. However, we soondiscovered that not only did these C runtime libraries useincompatible implementations of built-in C features such asthread-local storage, but they were also not built as position-independent code (PIC) to support static compilation. As aresult, we could neither build our NVRAM library staticallyagainst a single C runtime library, nor could we dynamicallybuild our shared library specically for each rmware image.Fortunately, ELF dynamic loaders for Linux systems supportlazy linking, which allows the resolution of external functionsymbols to be delayed until usage. Typically, the compilerimplements this by placing stub code within the ProcedureLinkage Table (PLT) that initializes the Global Offset Table(GOT) entry for a given imported function when the function
is called for the rst time.Since the ELF loader uses a global symbol lookup scopeduring resolution [12], we were able to compile our NVRAMlibrary with the-nostdlibcompiler ag, delaying resolutionof external symbols until after thecalling processhad alreadyloaded the system C runtime library. Effectively, this allowedour shared library to appear as a static binary while dynamicallyutilizing functions made available by the calling process,including the standard C runtime library.Another challenge we encountered was the fact that ourNVRAM implementation was not useful without a set of system-specic default values. Unfortunately, these values are normallyembedded within the hardware NVRAM peripheral at thefactory, and having a hardware dependency for our systemwould preclude our goal of performing a large-scale analysis.Simply returningNULLor the empty string was also insufcient,as this would eventually cause the system to crash at startup orenter an erroneous state, e.g., by callingitoa()orstrcpy()on aNULLpointer, or inserting bad arguments to programinvocations such asifconfig. Initially, we attempted tohardcode a set of default NVRAM values into our library, butwe soon discovered that this was infeasible since an averagermware image can reference hundreds of NVRAM keys atstartup.After manually examining rmware images that failed toemulate, we realized that most images embedded a set of defaultNVRAM values into a few common locations, e.g., within a textle named/etc/nvram.default,/etc/nvram.conf,or/var/etc/nvram.default. Others would export asymbolrouter_defaultsorNvramsof typechar
*
[]within built-in libraries such aslibnvram.soorlibshared.so. We were able to access these symbols bydeclaring them as weak references and checking if they wereinitialized, since we could not utilizelibdl.so(not typicallyloaded by the calling executable) or leave them as regularreferences (external data symbol resolution is not lazy).Unfortunately, our NVRAM emulation implementation doesnot work for all rmware images. This can be due to awide variety of reasons. For example, some images may callNVRAM-related functions that we do not emulate; othersmay expect different semantics from these emulated functionsin terms of parameter passing, return values, or caller/calleememory allocation; some others may implement NVRAM as acustom data structure on a MTD partition, which we currentlycannot initialize to a valid state. We believe failures in NVRAMemulation are likely to be a signicant contributor to the dropin emulation progress between columns two and three of Fig. 2.As an inconvenient truth, improving the emulation successrates or xing network conguration detection for rmwareimages from, e.g., Tomato by Shibby, is a manual process. Itrequires an analyst to manually examine system logs in orderto identify and classify emulation failures based on root cause,then make the changes that are necessary to support theseimages. Oftentimes, this may be a cyclic process, as there canbe multiple causes of emulation failure.
2)Kernel:As mentioned in §II-B, we do not utilize theextracted kernel, but instead replace it with our own custompre-built kernels for the ARM and MIPS architectures, whichtogether account for 90.8% of our dataset.During the kernel compilation process, we implement ouranalysis within our custom Linux kernel module that is used toaid debugging and emulating the original system environment.By hooking 20 system calls using the kernel dynamic probes(kprobes) framework, we are able to intercept calls thatalter the execution environment. This includes operationssuch as assigning MAC addresses, creating a network bridge,rebooting the system, and executing a program, all of which aremonitored by our framework to properly congure the emulatednetworking environment. This functionality can also be used toprovide automatic conrmation of vulnerabilities, especially inconjunction with predened poison values (e.g.,0xDEADBEEF,0x41414141
) that should never appear in system calls.Since some rmware images expect certain lesystemsto be mounted at boot, e.g.,/devor/proc, we use therdinitkernel parameter to run a custom script that initializesthese lesystems beforeinitis executed. Additionally, weload thenandsimkernel module at startup, which emulatesthe memory technology device (MTD) partitions accessedvia/dev/mtdXthat are frequently used on these embeddeddevices.In addition, since our emulation of NVRAM is volatile, weprohibit the guest from rebooting the system and emulate thisbehavior by restarting theinitprocess. This kernel modulealso emulates vendor-specic or device-specic interfaces, suchas custom device nodes,procfsentries, or non-standardIOCTL
's by returning success with a generic stub.For the MIPS architecture, we build separate kernels forbig-endian and little-endian systems, both targeting the MIPSMalta development platform, which is well-supported by bothQEMUand the Linux kernel. In fact, this platform even supportsMIPS 64-bit code, although we have not implemented supportfor it since it comprises less than 0.6% of our dataset. Thiskernel is currently at version 2.6.32.68, which is a long-termsupport release, and includes our backported commits for fullkprobes
support.For the ARM architecture, we support only little-endiansystems, since big-endian systems comprise less than 1.1% ofour dataset and are unsupported by mainlineQEMU
3. We targetthe ARM Versatile Express development platform, which uses3
https://lists.gnu.org/archive/html/qemu-devel/2014-06/msg03257.html
7

--- page 9 ---

an emulated Cortex-A9 (ARMv7-A) processor. This platformoffers better hardware compatibility than the standard ARMVersatile Platform Baseboard development board, which uses anemulated ARM926 (ARMv5) processor that does not supportnewer ARM instructions found in some rmware images.Unfortunately, this platform supports only up to one emulatedEthernet device due to the lack of an emulated PCI bus inQEMU. In the future, we plan to switch to the ARM VirtualMachine platform, which supports multiple virtualized devicesvia VirtIO, but this will require a kernel upgrade from 3.10.92to 4.1.12, a newer long-term support release that fully supportsVirtIO functionality on ARM.As the above discussion suggests, adding support for anew hardware architecture, such as x86, is not an automatedprocess. In particular, selecting a supported hardware platformin QEMU can be tricky, as support for either VirtIO or anemulated PCI bus is typically required to attach more thanone virtual networking interface. At the same time, the chosenhardware platform in QEMU must be supported by the selectedversion of the Linux kernel, which needs to be sufcientlyup-to-date forkprobesand VirtIO support. Developing acompatible conguration for the kernel can also be tricky, aswe need to enable all the features that off-the-shelf rmwarerelies on. Furthermore, we need to rebase our custom kernelmodule implementation to the chosen kernel version, whichmay require manual compatibility xes to account for internalkernel API changes.
3)System Conguration:Since we are mainly interested inrmware that implements network functionality, such as routers,network attached storage, or surveillance equipment, we need tomake device-specic changes to the emulated hardware. Ideally,all network devices would automatically congure themselvesvia the DHCP protocol. Unfortunately, certain network devices,especially routers and some managed switches, are designedto provide DHCP services to other devices. Additionally, thesedevices tend to have different numbers of network interfaces;for example typical consumer routers have at least four Ethernetinterfaces, in comparison to just one on an IP camera.Our system initially executes each emulated rmwarein a “learning” phase for 60 seconds. In this phase, theemulator is congured with the default hardware peripheralsfor the emulated target platform (MIPS Malta or ARM VirtualExpress), plus up to four emulated network adapters, usingthe built-in socket networking backend withinQEMU. Duringthis time, information is gathered about the expected networkconguration. In particular, we keep track of IP addresses thatare assigned to network interfaces, as well as the presenceof IEEE 802.1d bridges used to aggregate multiple networkinterfaces. Additionally, we check for tagging and separationof Ethernet frames using IEEE 802.1Q VLANs, which is usedby some routers to segregate wireless guest networks from thephysical network.This information is then fed back into our emulationframework to develop a more accurateQEMUcongurationfor this system. We instantiate a network tap (TAP) device onthe host, which is associated with one of the emulated networkinterfaces within the rmware (e.g.,eth0) that correspond toa LAN interface. For rmware images that use VLANs, weassign a corresponding VLAN ID to the TAP interface, in orderto communicate successfully with emulated network services.Next, theTAPinterface is congured with an IP address thatresides in the same subnet as the IP address assigned to theemulated interface by the rmware. Finally, we check fornetwork connectivity by sending ICMP requests and performinga port scan using the
Nmap
[3] utility.
4)QEMU:Aside from NVRAM, we expect embeddedsystems to rely on other hardware-specic peripherals such aswatchdog timers or additional ash storage devices. Unfortu-nately, some device manufacturers do not follow good softwareengineering practices and implement such functionality directlyin userspace, instead of using a device driver in kernelspace.As a result, we cannot simply abstract away these devicesand cleanly emulate this behavior within our custom kernelmodule. For example, thealphafswebserver mentioned in§II-Bmaps part of physical memory from the/dev/memdevice node directly into its own address space. It expects con-guration information for the ash memory chip to be mappedat0x1e000000, with theVendorIDandProductIDidentication parameters matching a chip supported by thesoftware; otherwise it simply terminates.To support the 138 affected rmware images inFIRMA-DYNE, we modied the appropriate sixteen bytes inQEMU'ssource code for the emulated platform ash device to respondwith known good values.
D. Automated AnalysesCurrently, we have implemented three basic automateddynamic analysis passes within our system. Each is registeredas a callback within our system, such that when a rmwareimage enters the network inferred state, registered callbacksare triggered sequentially. These contributed to our detection of14 previously-unknown vulnerabilities that affect 69 rmwareimages, and 74 known vulnerabilities that affect 887 rmwareimages (see §V).
1)Accessible Webpages:To help detect various informationdisclosure, buffer overow, and command injection vulnera-bilities, we wrote a simple analysis that looks for publiclyaccessible webpages from the LAN interface of rmwareimages. A custom-written Python test harness iterates througheach le within the rmware image that appears to be servedby a webserver (e.g., located within/www/), veries that it isnot a static resource (e.g., *.png, *.css, *.js), and attempts toaccess it directly over the web interface.Responses that contained non-2xx HTTP status codes wereignored, since these were typically inaccessible web pages(403/404), web pages that required authentication (401), orinvalid responses caused by socket timeouts or incomplete reads.Successful responses that contained redirects were agged aslower condence results, since we experimentally determinedthat a large number of these were used to implement soft-authentication pages.Perhaps as a more user-friendly authentication mechanism,these soft-authentication pages checked whether client requestswere authenticated using a client cookie or server IP addresslog instead of the basic or digest authentication mechanisms8

--- page 10 ---

built-into the HTTP protocol (which would return 401). Thus,these pages were marked with lower condence, while all otherweb pages were marked with regular condence. These resultswere aggregated across our rmware dataset to determine whichURLs were most accessible, and then prioritized for furtheranalysis in order of popularity.
2)SNMP Information:We were curious about the preva-lence and security of Simple Network Management Protocol(SNMP) implementations across our dataset, and so we wrote abasic analysis using our framework to dump all unauthenticatedSNMP information from the “public” and “private” communi-ties using thesnmpwalktool. Using MIB les gathered bythe crawler, the results for a subset of these were manuallyinterpreted to check for the presence of sensitive information.The corresponding object identiers (OIDs) were recorded, anda simple proof-of-concept was developed for each, based onwhether information was returned when the OID was queried.3)Vulnerabilities:Using 60 known exploits, mostly fromthe Metasploit Framework, we initially checked all rmware im-ages across our dataset for known security vulnerabilities. Eachexploit was executed sequentially, with a remote shell payloadif applicable, then the corresponding exploit log was checkedfor success. This provided a lower-bound on the number ofvulnerabilities within our dataset, since an exploit may fail evenif a vulnerability is present. The tested vulnerabilities weremanually selected for relevance to applications and daemonsknown to be present on embedded devices, and spanned variousexploit categories such as buffer overow, command injection,information disclosure, and denial of service.For the new vulnerabilities that we discovered, we manuallydeveloped proof-of-concepts exploits, which leveraged ourpredened poisoned arguments such as0xDEADBEEF. Then,we specied a verication condition for each exploit, whichwas typically the presence of the poisoned argument in our in-strumented kernel log; other examples included a segmentationfault at
0x41414141
or a WPS PIN in a webpage.
E. Additional CapabilitiesWe also developed a number of additional capabilities thatassisted the development and debugging of our emulationframework and exploits. These include dynamic tracing ofcode execution, which can be imported into existing reverseengineering tools, such asIDA Pro. Our custom kernel wasmodied to disable inlining of thecontext_switch()function, which allowed the emulator to trace the executionof given userspace processes. Additionally, at startup wealso launch a special console application on the device node/dev/ttyS1, which is forwarded byQEMUto a temporarysocket on the host system. This provided us with a convenientmechanism for modifying the emulated rmware image atruntime, especially if no default console is launched.
V. E
VALUATIONIn this section, we evaluate our implementation ofFIR-MADYNE. First, we examine the composition of our inputdataset, and analyze its effect on the emulation delity at everystage in the emulation pipeline. Second, we demonstrate howwe leveraged our system to identify 14 previously-unknownvulnerabilities within the collected rmware samples. Usingproof-of-concept exploits that we developed for each of thesevulnerabilities, we use our system to assess their prevalenceand impact on our dataset. Finally, we demonstrate the analysisexibility of our system by supplementing it with 60 knownexploits, mostly from the Metasploit Framework [2], and assessthe prevalence and impact of these known exploits on ourdataset.It is important to note that the distribution of rmwareimages across product lines and device vendors is not uniform,and thus may skew interpretation of the results. In particular,although we attempt to scrape metadata about the model numberand version number of each rmware image, this informationis not always available, nor is it present in a format that caneasily establish a temporal ordering. For example, vendors mayre-release a given product with different hardware, or releasea product with different hardware or rmware in each region,preventing direct comparisons between two rmware imageswith the exact same model. As a result, it is difcult to identifywhich rmware images are deprecated, and which rmwareimage(s) is (are) the current version(s).Furthermore, it is difcult to establish a mapping betweenrmware images and products, since there is not a direct one-to-one correspondence. For example, some vendors, such asMikrotik, distribute a single rmware image for each hard-ware architecture whereas other vendors, such as OpenWRT,distribute a single rmware image for each hardware chipset.Additionally, some vendors, such as QNAP and Synology,develop a master rmware image that is only lightly customizedfor each product in terms of hardware support and productstrings, whereas other vendors, such as OpenWRT, distributedifferent binary releases of the same rmware image usingvarious encapsulation formats. Given two different rmwarebinaries, this raises the question of how functionally identicalthey may be, which we do not address. Nevertheless, we attemptto provide a lower-bound on the number of affected products,where possible.
A. Statistics
1)Architectures:For all rmware images with extractedroot lesystems, we were able to identify the architecture ofthe corresponding rmware image by examining the formatheader of thebusyboxbinary on the system, or alternativelybinaries in
/sbin/
if we could not locate
busybox
.Table I shows that the majority of our rmware images are32-bit MIPS (both big-endian and little-endian), which consti-tute approximately 79.4%. The next most popular architecturetype is 32-bit little-endian ARM, which constitutes approx-imately 8.9%. Combined, these two architectures constitute90.8% of all rmware images, with the remainder formingthe little-tail of this distribution, suggesting that additionaldevelopment effort to support the remaining architectures wouldrequire some other strong justications.
2)Operating Systems:By combining our statistics for rootlesystem extraction and signature matches for the Linux andVxWorks kernels, we noticed that the largest proportion ofour rmware images were UNIX-based at 48%, as shown inTable II. If the lesystem of a rmware image was positively9

--- page 11 ---

identied as UNIX-based, but failures were encountered duringthe kernel extraction process, then the image was labeled asUNIX-like. Potential causes for this include path explorationconstraints, unsupported compression algorithms, or even thelack of a kernel within the rmware image. Barely 3.5% ofour rmware images were identied as VxWorks, showing thatimplementing support for these devices is a low priority.As discussed previously in the last paragraph of §IV-B,the unknown rmware images can be attributed to a numberof extraction failures. These include rmware images thatappeared to be Linux-based, but for which we were unableto reassemble the entire lesystem, extracted only a partialUNIX-like lesystem, or extracted a lesystem that did notmeet our threshold to be deemed UNIX-like. Some of theseare known to use ZynOS, a proprietary real-time operatingsystem developed by ZyXEL Communications. ZynOS usesthe ThreadX kernel and an unknown lesystem type, for whichwe lack a kernel version signature and lesystem extractionutility.Other unknown rmware images are monolithic rmwareimages that do not utilize a distinct kernel or lesystem. As aresult, emulating these rmware images would be extremelydifcult without hardware documentation, as chipset-speciccode may be distributed throughout the binary. This type ofrmware image is known to be used by u-blox, which isincluded in our dataset.
3)Kernel Modules:Across all of our extracted rmwareimages, we performed a basic categorization of all out-of-tree kernel modules based on lename, shown in Table III.These numbers indicate that 58.8% of these modules implementvarious network-related functionality, such as packet ltering(iptables,xtables,netfilter,ebtables), protocolimplementations (pptp,ppp,adsl), and interface support(mii,tun,tap). The next largest subset of 12.7% were usedto provide support for various peripherals, including wirelessadapters (wl,ath9k,sierra), platform chipsets (ar7240,ar7100,bcm963xx), and various other devices (acos_nat,pl2303). Many of the remaining kernel modules appeared tobe in-tree kernel modules that were compiled as loadable mod-ules, including generic USB interface implementations (ehci,uhci,xhci), lesystems (fat,fuse,ext3), cryptographicfunctions (sha512,crypto), and various other miscellaneouskernel routines (ts_fsm,sch_hfsc). Less than 0.2% ofthese kernel modules were identied as the KCodes NetUSBkernel module, a proprietary USB over IP kernel module thatis known to contain a remotely-exploitable buffer overowvulnerability.
4
4)Network Services:To assess the prevalence of listeningnetwork services on our rmware image dataset, we used thenmapnetwork scanning tool to check the 1,971 images thatrespond to ICMP echo requests. We scanned all TCP ports withknown services from thenmap-servicesle, as well as thecontinuous port range 1–1024, which is the default scanningbehavior ofnmap. The top ten results, shown in Table IV,indicate that out of the 1,971 devices that were networkreachable, 47.3% likely support a web-based conguration4https://www.sec-consult.com/fxdata/seccons/prod/temedia/advisories_txt/20150519-0_KCodes_NetUSB_Kernel_Stack_Buffer_Overow_v10.txt
Architecture (Endian)# Image(s)TILE (LE)1
ARC (LE)10
Motorola 68k (BE)10
x86 (LE)31
MIPS 64-bit (BE)50
PPC (BE)84
ARM (BE)102
x86-64 (LE)147
Unknown439
ARM (LE)843
MIPS (BE)3,137
MIPS (LE)4,632Total9,486TABLE I: Breakdown of rmware images by architecture, basedon binary ngerprinting of extracted root lesystems.
Type# ImagesLinux9,379
Unidentied (UNIX-like)2,187
VxWorks857
Unknown10,612Total23,035TABLE II: Breakdown of rmware images by operating system,based on kernel ngerprinting and root lesystem extraction.
Category# ModulesNetUSB853
Unclassied1,384
Cryptography12,603
USB30,683
Filesystems43,271
Miscellaneous55,344
Peripheral Drivers64,085
Networking296,592Total504,815TABLE III: Breakdown of kernel modules by category, basedon path and lename.
# ImagesTCP Port/Service# Vendor(s)92880/http9
70823/telnet7
53653/domain6
2503333/dec-notes1
188443/https7
1875000/upnp2
1361900/upnp1
16249152/unknown4
632602/ripd2
575555/freeciv3TABLE IV: Breakdown of listening network services by numberof rmware images and number of vendors.
10

--- page 12 ---

Fig. 2: Breakdown of rmware images by emulation progress,colored by vendor.interface (HTTP or HTTPS). Of these, only 9.5% supportedHTTPSfor the conguration interface, which is 19.8% of thedevices that support
HTTP
.Remote shell access is supported by 37.4% of devices overeither theTelnetorSSHprotocols. Note, however, thatSSHis not among the top ten results; in fact, it ranks 13th at 2.2%,or 1.9% of the devices that supportTelnet. This is worsethan the percentage of devices supportingHTTPSout of thedevices that support
HTTP
.Based on the presence of theDNSservice, it appears thatat least 27.2% of these rmware images are routers, whichtypically act as a local DNS proxy. Another 16.4% ship withUniversal Plug and Play (UPnP) enabled by default, whichallows LAN devices to automatically congure port forwardingfrom the WAN interface.Port 2602 is known to be used by the Routing Informa-tion Protocol (RIP) protocol, which is typically enabled onenterprise-class routers for automatic network routing.According to various customer support forums, ports 3333and 5555 are known to be open on certain Netgear devices,although we have not checked our Netgear rmware imagesto identify the responsible service. Port 49152 is known to bethe rst port in the dynamic port address range forwarded byvarious applications through UPnP, though we do not have anyUPnP clients in our network conguration and are uncertainof the default forwarding state.
5)Emulation Progress:As shown in Fig. 2, of the 8,617 ex-tracted rmware images for which we identied an architecture,our system initially emulated 96.6% (8,591) successfully. Thefailures can be attributed to a number of causes, including thelack of aninitbinary in a standard location (/bin/init,/etc/init, or/sbin/init), or an unbootable lesystem.For example, certain images containing Ralink chipsets areknown to name theirinitbinaryralink_init, which wecurrently do not support. Likewise, extraction failures discussedin the last paragraph of §IV-Bcan also affect success ofthe initial emulation. Since we only extract the rst UNIX-like lesystem from rmware images that contain multiplelesystems, it is likely that only part of the lesystem has beenextracted, leading to a boot failure. Reassembling such systemsinto a single lesystem is not straightforward because eachlesystem can potentially be mounted on top of another atarbitrary locations.Of the 8,591 rmware images that entered the “learning”phase, only 32.3% (2,797) had their networking congurationsuccessfully inferred. We believe that this decrease occurreddue to failures in the boot process while attempting to infer thenetwork conguration. As we previously discussed in the lastparagraph of §IV-C1, problems with NVRAM emulation area signicant contributor to these failures. For example, somerouters may not initialize correctly if our NVRAM implemen-tation was not able to override the built-in implementation,if insufcient default NVRAM values were loaded by ourimplementation, or if the built-in NVRAM implementationexpected different semantics from NVRAM-related functions.These manifest as various crashes or hangs during the bootprocess, especially if memory or string manipulation functions(memcpy(),strcpy(), etc.) are called onNULLvaluesreturned by our NVRAM implementation for nonexistentkeys. Additionally, it is also possible that some images donot use a NVRAM hardware peripheral, but instead writeconguration values directly to a MTD partition, which wemay not successfully emulate.Other potential sources of networking failures includedifferent naming conventions for networking devices. Forexample, devices that utilize Atheros or Ralink chipsets mayexpect platform networking devices to be named similarlytoath0orra0, respectively, instead of the genericeth0.Likewise, other devices may expect the presence of a wirelessnetworking interface such aswlan0, and fail otherwise. Inaddition, since our ARM little-endian emulation platformcurrently supports only up to one emulated Ethernet device, thismay prevent some rmware images from correctly conguringnetworking.Only 70.8% (1,971) of the 2,797 images with an inferrednetwork conguration are actually reachable from the networkusingping. This may be caused by rewall rules on theemulated guest that lter ICMP echo requests, resulting infalse negatives, or various other network conguration issues.For example, our system may have mistakenly assigned thehost TAP interface inQEMUto the WAN interface of theemulated device instead of a LAN interface, or identied thedefault IP address of the WAN interface instead of the LANinterface. Similarly, rmware may change the MAC address ofthe emulated network device after it has booted, resulting instale ARP cache entries and a machine that appears unreachable.Surprisingly, our results show that 45% (887 out of 1,971rmware images) of the network reachable rmware imagesare vulnerable to at least one exploit. We discuss this furtherin §V-B, where we give a breakdown by exploit.
11

--- page 13 ---

Architecture
Identified
0
2000
4000
6000
8000
10000
Initially
Emulated
Network
Inferred
Network
Reachable
Exploited

--- page 14 ---

Exploit ID# Images# ProductsAffected Vendor(s)472821621, 22, 37
561691416, 21, 35
641692712, 21, 37
451361321
43881012
202491112, 16, 21, 36, 37, 42
20735621
603197, 12, 19, 21, 37
20516521
20614421
20313512
599N/A12
2008121
2017121
2107212
46N/A12
245119, 42
2134121
2144121
393N/A12
2093112
2123121
612142
2041N/A21
2111121TABLE V: Breakdown of exploits by number of affectedrmware images, number of affected products, and affectedvendor(s), indexed into Table VII. Note:N/Aindicates that wedo not have sufcient metadata to compute a lower-bound onaffected products.
# Exploits# Images# Vendor(s)# Products5211
4813
330210
286514
1761977
01,91022263Total2,79742322TABLE VI: Breakdown of successful exploits by number ofrmware images, number of vendor(s), and number of affectedproducts.
B. ResultsIn Table V, we provide a breakdown of all successfulexploits by exploit. Exploits in the range #0 – #100 are sourcedfrom the Metasploit Framework, whereas most exploits greaterthan or equal to #200 are previously-unknown vulnerabilities forwhich we developed proof-of-concepts (POC's). This excludes#202, which is a known vulnerability but not sourced fromthe Metasploit Framework. Each of these previously-unknownvulnerabilities has been reported to the respective vendor,following the policies of responsible disclosure. We discussa few specic vulnerabilities below in greater detail as casestudies.By tabulating the results from Table V for each rmwareimage, we obtain Table VI, which provides a breakdown ofthe rmware images by the number of successful exploits.This shows that a small number of these rmware images arevulnerable to more than two exploits, with the least secureimage suffering from ve exploits. Interestingly, all 40 of thesermware images vulnerable to more than two exploits arerouters and access points manufactured by D-Link and Netgear;however, this data may be skewed by the distribution of ourexploits and rmware images, which is not uniform. Theseresults initially seem to decay exponentially, with less than half(39.8%) of rmware images vulnerable to zero exploits beingvulnerable to one exploit, but then there is a long-tail in thevulnerability distribution, with only 4.5% (126) of rmwareimages affected by more than one exploit.
1)Command Injection (#200, #201, #204 – #206, #208):While analyzing the aggregate results of our automatedaccessible webpages analysis (§IV-D1), we discovered sixpreviously-unpublished command injection vulnerabilities thataffect 24 rmware images for wireless routers and access pointsmanufactured by Netgear. All six vulnerabilities were withinPHP server-side scripts that provided debugging functionalitybut appeared to be accidentally included within productionrmware releases. In particular, ve of these were used tochange system parameters such as the MAC address of theWLAN adapter, and the region of the rmware image (e.g.,World Wide [WW], United States [US], or Japan [JP]). Theremaining one was used to write manufacturing data such asMAC address, serial number, or hardware version into ashmemory. Our manual analysis of the PHP source code revealedthat all were straightforward command injection vulnerabilitiesthrough the$_REQUESTsuper-global and unsafe use of theexec()function. After discovering these potential vulnera-bilities, we leveragedFIRMADYNEto automatically verifytheir exploitability across our entire dataset.
2)Buffer Overow (#203):Another new vulnerability thatwe manually discovered, using the results of our automatedaccessible webpages analysis, was a buffer overow vulnera-bility within rmware images for certain D-Link routers. Toimplement user authentication, the webserver sets a client-sidecookie labeleddlink_uidto a unique value that is associatedwith each authenticated user. Instead of verifying the valueof this cookie within the server-side scripting language of thewebpage, this authentication functionality was actually hard-coded within the webserver, which uses the standard libraryfunctionsstrstr(),strlen(), andmemcpy()to copythe value of the cookie. As a result, we were able to set the valueof this cookie to an overly-long value to cause the webserverto crash at0x41414141, another poisoned argument that wemonitor for.
3)Information Disclosure (#207, #209 – #214):Using theautomated webpage analysis, we also discovered seven newinformation disclosure vulnerabilities across our dataset thataffect 51 rmware images for various routers manufacturedby both D-Link and Netgear. One of these (#207) was withinan unprotected webpage that provides diagnostic informationfor the router, including the WPS PIN and passphrases for alllocally-broadcast wireless networks.
12

--- page 15 ---

The remaining six vulnerabilities (#209 – #214) were withinthe Simple Network Management Protocol (SNMP) daemon ofboth manufacturers. This feature was enabled by default likelybecause these routers were targeted towards small businessesrather than home users. To interpret results obtained fromSNMP queries, one needs access to a Management InformationBase (MIB) le that describes the semantics of each individualobject (OID) eld. As discussed in §III-B, our crawlers recordlinks to MIB les in the collected metadata, enabling manualverication of the obtained results.Our automated exploit verication showed that thesermware images would respond to unauthenticated SNMPv2c queries for thepublicandprivatecommunities, andreturn values for the OID's that contain web-based accesscredentials for all users on the device, and wireless credentialsfor all locally-broadcast wireless networks.
4)Sercomm Conguration Dump (#47):This exploit, re-ported as CVE-2014-06595and sourced from the MetasploitFramework, attacks undocumented and badly-designed featuresof thescfgmgrservice to remotely dump system congurationvariables from NVRAM and obtain a shell. Public documenta-tion for this vulnerability suggests that, as of 2015-01-28, it wasknown to affect rmware for networking devices manufacturedby Cisco, Linksys, Netgear, and a variety of smaller vendors.This is corroborated by our automated analysis, which alsoconrmed the presence of this vulnerability within devicesmanufactured by On Networks and TRENDnet. More precisely,our results suggest that this single vulnerability affects 14.3%of all network reachable rmware images from our dataset.This is because Sercomm Corporation is likely the originalequipment manufacturer (OEM) for these devices, which werethen re-branded and re-sold by various vendors.
5)MiniUPnPd Denial of Service (#56):Reported as CVE-2013-02296, this exploit takes advantage of parsing aws for theSimple Service Discovery Protocol (SSDP) within MiniUPnP7,an open-source UPnP daemon implementation, to trigger adenial of service attack on this service.According to our results, 8.5% of all network reachablermware images from our dataset are vulnerable to this attack,which was xed on 2009-10-30 with the release of MiniUPnP1.4. Affected vendors include Huawei, Netgear, and Tomato byShibby, which is a community-developed third-party rmwarefor various wireless routers. Statistics released by Rapid7,the developers of the Metasploit Framework and the originalreporters of this vulnerability, indicate that as of 2013-01-29, 332 products used MiniUPnP 1.0, with over 69% of allMiniUPnP ngerprints corresponding to version 1.0 or older.Again, these results emphasize the prevalence of cross-vendorvulnerabilities due to shared software components, whetheropen-source or proprietary.
6)OpenSSL ChangeCipherSpec (#64):This vulnerabilitywas reported as CVE-2014-02248, and takes advantage of abad state machine implementation for the SSL/TLS handshake5
https://github.com/elvanderb/TCP-32764
6https://community.rapid7.com/servlet/JiveServlet/download/2150-1-16596/SecurityFlawsUPnP.pdf
7
http://miniupnp.free.fr/
8
http://ccsinjection.lepidum.co.jp/process in all versions of OpenSSL before 0.9.8za, 1.0.0m,and 1.0.1h. Exploitation of this vulnerability allows an attackerto downgrade the cipher specication between a client anda server, potentially permitting a man-in-the-middle (MITM)attack. Our results show that 8.5% of all network reachablermware images are vulnerable to this attack, which is 89.9%of all rmware images that acceptHTTPSconnections. Thisexploit also affects 8.4% of all products in our dataset, the mostout of all exploits. Affected vendors include D-Link, Netgear,and TRENDnet.
C. Discussion and LimitationsAlthoughFIRMADYNEperformed well in our experi-ments, there is certainly room for improvement. As discussedpreviously in §IV-B, §IV-C1, and §IV-C2, additional manualeffort can improve the system by, e.g., xing extraction failures,adding support for additional hardware architectures, or cor-recting emulation failures. These changes require an analyst tomanually classify failures by root cause and perform the changesthat are necessary to increase compatibility. Implementing anew analysis pass also requires manual labor, though we canpotentially reap a large benet from it because each newly-implemented analysis can be automatically executed on allsupported rmware images from our dataset.In addition, as mentioned in §V, our results can be difcultto evaluate due to the lack of a mechanism for quantifying real-world impact in terms of unique products (instead of uniquermware images). Likewise, our results are affected by skewcaused by differences in vendor composition of our dataset,and of network reachable rmware images.Other limitations ofFIRMADYNEinclude the usage ofcustom pre-built kernels, which currently do not load out-of-tree kernel modules from the lesystem. As a result, oursystem cannot be used to conrm vulnerabilities in kernels orkernel modules shipped by the vendor within rmware images.For example, we are unable to assess the prevalence of theKCodes NetUSB kernel module buffer-overow across ourdataset because of this limitation.Likewise, we do not identify which network port is usedas the uplink (or WAN) port, and which network port(s) areused for the downlink (or LAN) port(s). This prevents us fromdetermining whether detected vulnerabilities are exploitablefrom the Internet, or only by locally-connected clients.Nevertheless, a number of techniques can be used by remoteattackers to pivot from the WAN interface to the LAN interfaceover a web browser, including Cross-Site Request Forgery(CSRF), Cross-Site Scripting (XSS), or even DNS rebindingattacks. Additionally, with the increasing deployment of IPv6,local machines are now being assigned globally-routable IPaddresses. This potentially allows attackers to access the LANinterface of consumer devices, even though routers can stillact as rewalls. An increasing number of wireless routers andaccess points also now support network isolation or clientisolation features, which can segregate trafc between variouswireless or physical interfaces. However, the presence of thesevulnerabilities within the gateway router clearly compromises
this protection.
13

--- page 16 ---

VI. R
ELATED
W
ORKWith the increasing prevalence of embedded devices, severalrelated works have performed large-scale analyses of rmwareimages, using a variety of analysis techniques. For exam-ple, Heffner9performed large-scale extraction of embeddedrmware images to gather a database of over2
;
000hardcodedSSL private keys. Likewise, Rapid710used a similar analysisfor hardcoded SSH private keys, albeit on a smaller scale.Using static analysis, Costin et al. [8] recently analyzeda dataset of approximately32
;
000rmware images. Theydiscovered a total of38previously-unknown vulnerabilities,including hard-coded back-doors, embedded private key-pairs,and XSS vulnerabilities, all of which were obtained “withoutperforming sophisticated static analysis”.Another effective technique for large-scale measurement ofembedded device security is network scanning, which avoidsdirect analysis of rmware images. Using tools such as Nmap,Cui and Stolfo [10] identied approximately540
;
000publicly-accessible embedded devices withdefaultaccess credentials.Over the course of a4-month longitudinal study, they discoveredthat less than3%of access credentials were changed, whichsuggests that user awareness is lacking. Likewise, using theZMap [13] network scanner, Heninger et al. [14] showed thatembedded devices can also suffer from entropy problems.Their results indicate that2
:
45%of TLS certicates maybe vulnerable to brute-force attacks due to faulty RSA keygeneration, and that1
:
03%of DSA private keys are factorabledue to nontrivial common factors.Additionally, previous work has discovered specic vul-nerabilities that affect various classes of embedded devices.Using HP LaserJet printers as a case study, Cui et al. [9]demonstrated that remote rmware update functionality canbe exploited by attackers to insert malware. Weinmann [18]showed that deployed cellular baseband implementations sufferfrom remotely exploitable memory corruption vulnerabilities,which can be used to execute arbitrary code on the basebandprocessor. Similarly, Bonkoski et al. [6] showed that remotemanagement functionality on server motherboards is riddledwith security vulnerabilities, allowing a remote attacker to takecontrol of the system. Finally, Maskiewicz et al. [16] and Nohlet al. [17] showed that malicious functionality can be insertedinto the rmware of USB peripherals, allowing an attacker totake control of host systems and exltrate data.To defend against this attack vector, several differenttechniques have been developed to nd vulnerabilities inembedded devices. For example, Davidson et al. [11] havedeveloped a symbolic executor using the KLEE [7] symbolicexecution engine to detect vulnerabilities in embedded devices.Their work discovered21memory safety bugs across a corpusof99open-source rmware programs for the MSP430 familyof8-bit embedded micro-controllers. At a lower level, Liet al. [15] ported theQEMUemulator into the BIOS to modelhardware peripherals for validation of an embedded SoC duringdevelopment.9
https://github.com/devttys0/littleblackbox
10
https://github.com/rapid7/ssh-badkeysRecently, Zaddach et al. [19] have also developed aframework for performing dynamic analysis of embeddedrmware by forwarding I/O accesses from within an emulatorthe actual hardware for execution. However, this approach doesnot scale in terms of analysis cost and time, which is whywe have designedFIRMADYNEto perform robust hardwareemulation and vulnerability verication in anautomaticmanner.VII. C
ONCLUSION
& F
UTURE
W
ORKBy developingFIRMADYNE, our automated dynamicanalysis framework, we hope to lower the bar for discoveringnew vulnerabilities within embedded systems. At the same time,FIRMADYNEimplements an automated approach to assessthe prevalence of newly-discovered security vulnerabilitiesin a large population of embedded device rmware images.Given the weak security posture of these devices, we believethat greater attention to these devices by security researchers,hobbyists, and other interested parties can motivate devicemanufacturers to address security issues in their products moreswiftly. This is especially true for OEMs, who are responsiblefor a signicant fraction of the vulnerabilities in existingdeployed devices.As shown in Fig.V-A, the next-largest category (afterLinux) of embedded rmware from our dataset are fromvarious proprietary real-time operating systems (RTOS) suchas VxWorks. This presents a potential avenue for future work,especially given the existence of published vulnerabilities thataffect these platforms. In particular, we would be interested indeveloping a compatibility layer for these applications usingexisting real-time Linux development frameworks such asXenomai on our emulation platform.A considerable number of source code releases are availablefor many Linux-based embedded rmware due to the termsof common open-source software licenses. Since our datasetincludes links to applicable source code for each rmwareimage, this could provide a mechanism for implementingeffective static analysis, in conjunction with our existingframework for performing dynamic analysis.Finally, statistical analysis techniques could be utilized toimprove the rmware extraction component of our framework.Firmware images that appear obfuscated or encrypted could behandled by a separate extraction pathway. For example, it iswell-known that rmware for Buffalo LinkStation devices areencrypted, but passwords and decryption utilities are publiclyavailable.11The same applies to various rmware distributedfor QNAP devices.
12Acknowledgment:This work was supported in part bygrants from the Department of Defense through the NationalDefense Science & Engineering Graduate Fellowship Programand under contract no. N66001-13-2-4040, and the Ofce ofNaval Research under grant N00014-15-1-2948. Any opinions,ndings and conclusions or recommendations expressed in thismaterial are those of the authors and do not necessarily reectthose of the sponsor.11
http://buffalo.nas-central.org/wiki/Firmware_update
12
http://pastebin.com/KHbX85nG
14

--- page 17 ---

R
EFERENCES
[1] “Binwalk.” [Online]. Available: http://binwalk.org/
[2]“Metasploit.” [Online]. Available: http://www.metasploit.com/
[3]“Nmap security scanner.” [Online]. Available: https://nmap.org/
[4]F. Bellard, “QEMU, a fast and portable dynamic translator,”inProceedings of the USENIX 2005 Annual TechnicalConference. USENIX, 2005, pp. 41–46. [Online].Available: https://www.usenix.org/legacy/publications/library/proceedings/usenix05/tech/freenix/bellard.html
[5]A. Bessey, K. Block, B. Chelf, A. Chou, B. Fulton,S. Hallem, C. Henri-Gros, A. Kamsky, S. McPeak,and D. Engler, “A few billion lines of code later,”Communications of the ACM, vol. 53, no. 2, pp. 66–75,2010. [Online]. Available: http://portal.acm.org/citation.cfm?doid=1646353.1646374
[6]A. Bonkoski, R. Bielawski, and J. A. Halderman,“Illuminating the security issues surroundinglights-out server management,” inProceedingsof the 7th USENIX Workshop on OffensiveTechnologies. USENIX, 2013, pp. 1–9. [Online].Available: https://www.usenix.org/conference/woot13/workshop-program/presentation/bonkoski
[7]C. Cadar, D. Dunbar, and D. Engler, “KLEE: Unassistedand automatic generation of high-coverage tests forcomplex systems programs,” inProceedings of the 8thUSENIX Symposium on Operating System Design andImplementation. USENIX, 2008, pp. 209–224. [Online].Available: https://www.usenix.org/legacy/events/osdi08/tech/
[8]A. Costin, J. Zaddach, A. Francillon, and D. Balzarotti,“A large-scale analysis of the security of embeddedrmwares,” inProceedings of the 23rd USENIXSecurity Symposium. USENIX, 2014, pp. 95–110.[Online]. Available: https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/costin
[9]A. Cui, M. Costello, and S. J. Stolfo, “Whenrmware modications attack: A case study ofembedded exploitation,” inProceedings of the 20thAnnual Network and Distributed System SecuritySymposium. The Internet Society, 2013. [Online]. Avail-able: http://www.internetsociety.org/doc/when-rmware-modications-attack-case-study-embedded-exploitation
[10]A. Cui and S. J. Stolfo, “A quantitative analysis of theinsecurity of embedded network devices: Results of awide-area scan,” inProceedings of the 26th AnnualComputer Security Applications Conference, 2010, pp.97–106. [Online]. Available: http://www.scopus.com/inward/record.url?eid=2-s2.0-78751540482&partnerID=40&md5=759904ebe0eca35e4297072f7224cf55
[11]D. Davidson, B. Moench, S. Jha, and T. Ristenpart,“FIE on rmware: Finding vulnerabilities inembedded systems using symbolic execution ndingvulnerabilities in embedded systems using symbolicexecution,” inProceedings of the 22nd USENIXSecurity Symposium. USENIX, 2013, pp. 463–478.[Online]. Available: https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/davidson
[12] U. Drepper, “How to write shared libraries,” 2006.
[13]Z. Durumeric, E. Wustrow, and J. A. Halderman,“ZMap: Fast internet-wide scanning and its securityapplications,” inProceedings of the 22nd USENIXSecurity Symposium. USENIX, 2013, pp. 605–619.[Online]. Available: https://www.usenix.org/conference/usenixsecurity13/technical-sessions/paper/durumeric
[14]N. Heninger, Z. Durumeric, E. Wustrow, and J. A.Halderman, “Mining your Ps and Qs: Detectionof widespread weak keys in network devices,” inProceedings of the 21st USENIX Security Symposium.USENIX, 2012, pp. 205–220. [Online]. Avail-able: https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/heninger
[15]H. Li, D. Tong, K. Huang, and X. Cheng, “FEMU:A rmware-based emulation framework for SoCverication,” inProceedings of the 2010 IEEE/ACM/IFIPInternational Conference on Hardware/Software Codesignand System Synthesis, no. 257. IEEE, 2010, pp. 257–266.[Online]. Available: http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5751510&tag=1
[16]J. Maskiewicz, B. Ellis, J. Mouradian, and H. Shacham,“Mouse trap: Exploiting rmware updates in USBperipherals,” inProceedings of the 8th USENIX Workshopon Offensive Technologies. USENIX, 2014, pp. 1–10.[Online]. Available: https://www.usenix.org/conference/woot14/workshop-program/presentation/maskiewicz
[17]K. Nohl and J. Lell, “BadUSB—on acces-sories that turn evil,” 2014. [Online]. Avail-able: https://www.blackhat.com/us-14/briengs.html#badusb-on-accessories-that-turn-evil
[18]R.-P. Weinmann, “Baseband attacks: Remote exploitationof memory corruptions in cellular protocol stacks,”inProceedings of the 6th USENIX Workshop onOffensive Technologies. USENIX, 2012, pp. 1–10.[Online]. Available: https://www.usenix.org/conference/woot12/workshop-program/presentation/weinmann
[19]J. Zaddach, L. Bruno, A. Francillon, and D. Balzarotti,“Avatar: A framework to support dynamic security analysisof embedded systems' rmwares,” inProceedings of the2014 Network and Distributed System Security Symposium.The Internet Society, 2014, pp. 23–26. [Online]. Available:http://dx.doi.org/10.14722/ndss.2014.23229
A
PPENDIX
A. Dataset BreakdownIn Table VII to follow, we show the progress ofFIRMA-DYNEin analyzing the rmware images in our dataset, groupedby vendor. Approximately 10% of all extracted rmware imageswere exploited.
15

--- page 18 ---

IndexVendorDownloadExtractedArch. IdentiedInitial EmulationNetwork InferredNetwork ReachableExploited1Actiontec14 (6)8 (4)5 (3)8 (4)0 (0)0 (0)0 (0)
2Airlink10115 (12)1 (1)1 (1)1 (1)1 (1)0 (0)0 (0)
3Apple9 (N/A)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
4Asus3 (1)1 (1)1 (1)1 (1)0 (0)0 (0)0 (0)
5AT&T25 (1)6 (1)4 (1)6 (1)2 (1)0 (0)0 (0)
6AVM132 (N/A)7 (N/A)7 (N/A)7 (N/A)0 (0)0 (0)0 (0)
7Belkin140 (61)55 (29)55 (29)53 (29)7 (4)3 (2)2 (2)
8Buffalo143 (61)6 (5)5 (4)6 (5)4 (3)0 (0)0 (0)
9CenturyLink31 (4)9 (4)9 (4)9 (4)1 (1)1 (1)0 (0)
10Cerowrt14 (N/A)14 (N/A)14 (N/A)8 (N/A)8 (N/A)0 (0)0 (0)
11Cisco61 (N/A)43 (N/A)39 (N/A)34 (N/A)2 (N/A)0 (0)0 (0)
12D-Link4,688 (434)1,124 (113)1,089 (109)1,121 (119)609 (65)458 (48)219 (32)
13Forceware2 (N/A)2 (N/A)2 (N/A)0 (0)0 (0)0 (0)0 (0)
14Foscam56 (23)5 (5)5 (5)5 (5)5 (5)0 (0)0 (0)
15Haxorware7 (N/A)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
16Huawei29 (17)5 (3)5 (3)5 (3)3 (2)2 (1)2 (1)
17Inmarsat47 (N/A)2 (N/A)2 (N/A)2 (N/A)2 (N/A)0 (0)0 (0)
18Iridium17 (N/A)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
19Linksys126 (29)105 (24)101 (21)105 (24)43 (9)36 (8)5 (3)
20MikroTik13 (4)5 (N/A)4 (N/A)2 (N/A)0 (0)0 (0)0 (0)
21Netgear5,280 (372)2,135 (156)2,109 (155)2,054 (149)1,297 (92)1,078 (79)628 (47)
22On Networks28 (N/A)15 (N/A)15 (N/A)15 (N/A)11 (N/A)10 (N/A)7 (N/A)
23Open Wireless1 (N/A)1 (N/A)1 (N/A)1 (N/A)1 (N/A)0 (0)0 (0)
24OpenWrt1,498 (41)1,303 (27)1,303 (27)1,295 (25)326 (8)8 (4)0 (0)
25pfSense256 (60)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
26Polycom644 (6)24 (1)7 (1)7 (1)0 (0)0 (0)0 (0)
27QNAP464 (88)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
28RouterTech12 (N/A)12 (N/A)0 (0)12 (N/A)0 (0)0 (0)0 (0)
29Seiki16 (10)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
30Supermicro150 (77)26 (17)26 (17)26 (17)0 (0)0 (0)0 (0)
31Synology2,094 (170)181 (51)34 (12)16 (12)0 (0)0 (0)0 (0)
32Tenda244 (55)59 (22)52 (19)59 (22)1 (1)1 (1)0 (0)
33Tenvis49 (4)26 (3)26 (3)26 (3)17 (3)17 (3)0 (0)
34Thuraya18 (N/A)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
35Tomato by Shibby2,942 (6)2,940 (6)2,940 (6)2,940 (6)21 (2)20 (2)1 (1)
36TP-Link1,072 (367)302 (103)302 (103)300 (102)245 (81)206 (73)3 (1)
37TRENDnet822 (162)272 (46)269 (45)270 (46)132 (26)94 (17)15 (1)
38Ubiquiti51 (11)36 (8)25 (5)36 (8)0 (0)0 (0)0 (0)
39u-blox16 (N/A)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
40Verizon37 (1)2 (N/A)1 (N/A)2 (N/A)0 (0)0 (0)0 (0)
41Western Digital1 (N/A)0 (0)0 (0)0 (0)0 (0)0 (0)0 (0)
42ZyXEL1,768 (252)161 (38)159 (38)159 (39)59 (18)37 (13)5 (1)Total4223,035 (2,331)8,893 (667)8,617 (611)8,591 (625)2,797 (322)1,971 (252)887 (89)TABLE VII: Breakdown of analysis progress by vendor, in terms of rmware images (products). Note:N/Aindicates that we donot have sufcient metadata to compute a lower-bound on affected products.
16

--- page 19 ---

YI-�Œl`®õî;`ÕçæAÐH:´® áYHb1“µâ»HÇ{¸wƒÇR^YÑš,
 $F¨Ô–HDÙòV?pòyÑ—¹PÞ%F=»‚ÂÇÆB‡öÙö¡GKØPh³~N´[¸IÊ_êˆ€CðTzÞÒf	ç	<Ó–”Œü�`4|mƒE1ÖJ'¼ýáÝ$`}R	‚Ú¨€âN2kf¢aóouJ73�ê´òváê¿ôKÛW{œMÓÞ3?×��©Mò]ù:W;v�…˜Xâ;„B’	‰§X�.PáI;?Ÿ!T¤ˆ .·sìöU]ä®ƒ’=ÑXŠþý’5´ÀŠ€r€Mt>y=¯†*ã�bC¾~^½tÅAr±¡l'¶øÅ¦•üóô÷ØŸÉL�ëƒ¡P“&7ttöuGz;Kg4ÚóÑ�;·u
