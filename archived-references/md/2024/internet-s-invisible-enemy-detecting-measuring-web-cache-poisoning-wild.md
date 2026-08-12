---
type: Article
title: "Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild"
resource: "https://doi.org/10.1145/3658644.3690361"
tags: [article, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-12T15:52:08+00:00"
status: stable
stale_after: 2027-08-12
sources:
  - id: original
    resource: "https://doi.org/10.1145/3658644.3690361"
    title: "Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild"
    author: Yuejia Liang, Jianjun Chen, Run Guo, Kaiwen Shen, Hui Jiang, Man Hou, Yue Yu, Haixin Duan
also_at: []
authors:
  - Yuejia Liang
  - Jianjun Chen
  - Run Guo
  - Kaiwen Shen
  - Hui Jiang
  - Man Hou
  - Yue Yu
  - Haixin Duan
canonical_url: ""
cited_by:
  - "2024.md:144"
commit: ""
content_sha256: 4be10c9158c0dcae01eb090b504dce0213a8a40811b024aec300f2a503526fa0
depth: full
depth_reason: default
kind: article
language: ""
licence: unknown
original_url: "https://doi.org/10.1145/3658644.3690361"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: b674794b413376bfd17af6bfbd568ef845c966a1ef810aefb278dde0a6b16cd4
retrieved_from: "https://doi.org/10.1145/3658644.3690361"
retrieved_kind: manual-import
retrieved_utc: "2026-08-12T15:52:08+00:00"
slug: internet-s-invisible-enemy-detecting-measuring-web-cache-poisoning-wild
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild

**Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild** - Yuejia Liang, Jianjun Chen, Run Guo, Kaiwen Shen, Hui Jiang, Man Hou, Yue Yu, Haixin Duan, Publisher not stated.

- Published: date not stated
- Original: <https://doi.org/10.1145/3658644.3690361>
- Preserved from: https://doi.org/10.1145/3658644.3690361 (manual-import) on 2026-08-12
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

--- page 1 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache
Poisoning in the Wild
Yuejia Liang
Tsinghua University
Beijing, China
liangyj21@tsinghua.org.cn
Jianjun Chen
Tsinghua University; Zhongguancun
Laboratory
Beijing, China
jianjun@tsinghua.edu.cn
Run Guo
Tsinghua University
Beijing, China
gr15@tsinghua.org.cn
Kaiwen Shen
Tsinghua University; Clouditera Inc
Beijing, China
kaiwenshen17@gmail.com
Hui Jiang
Tsinghua University; Baidu Inc
Beijing, China
jianghui01@baidu.com
Man Hou
Zhongguancun Laboratory
Beijing, China
houman@zgclab.edu.cn
Yue Yu
Beijing University of Posts and
Telecommunications
Beijing, China
yuyue_999@bupt.edu.cn
Haixin Duan
Tsinghua University; Quancheng
Laboratory
Beijing, China
duanhx@tsinghua.edu.cn
ABSTRACTWeb cache poisoning (WCP) has posed signicant threats to Internetsecurity by causing the cache server to deliver malicious responsesto innocent users. This results in widespread denial of access towebsite resources and potential injection of harmful payloads. How-ever, prior works on WCP vulnerability have been fragmented andconducted in a case-by-case form, lacking a systematic analysisof the threat landscape. In this paper, we ll this research gap byconducting a systematic evaluation of WCP vulnerabilities at scale.We proposeHCache, a novel testing methodology to facilitates thewidespread identication of WCP vulnerabilities. We evaluatedour methodology against Tranco Top 1000 domains and their sub-domains, and found that over 1,000 websites across 172 domains,representing 17% of the evaluated domains, are vulnerable to WCP.In particular, we have identied 7 new attack vectors stemmingfrom previously unexplored caching headers. We have responsiblydisclosed the vulnerabilities to the aected websites and received ac-knowledgements and bug bounties from world-famous companies,such as Alibaba, Adobe, Huawei, and Microsoft.
CCS CONCEPTSˆNetworks!Network measurement;ˆSecurity and privacy!
Network security
;
Web application security
.
KEYWORDSNetwork Security, Measurement, Web Cache, Web Cache Poisoning*
Corresponding author.This work is licensed under a Creative Commons AttributionInternational 4.0 License.
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
©
2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0636-3/24/10
https://doi.org/10.1145/3658644.3690361
ACM Reference Format:Yuejia Liang, Jianjun Chen, Run Guo, Kaiwen Shen, Hui Jiang, Man Hou,Yue Yu, and Haixin Duan. 2024. Internet's Invisible Enemy: Detecting andMeasuring Web Cache Poisoning in the Wild. InProceedings of the 2024ACM SIGSAC Conference on Computer and Communications Security (CCS'24), October 1418, 2024, Salt Lake City, UT, USA.ACM, New York, NY, USA,15 pages. https://doi.org/10.1145/3658644.3690361
1 INTRODUCTIONTo prevent unnecessary Internet trac and enhance data transmis-sion eciency, web caching facilities are extensively used. Theystore frequently requested data resources, reducing the need forrepeated data transfers. Given web cache's advantages, it has be-come a critical infrastructure component of the Internet. How-ever, when compromised by malicious actors, web caching facilitiespose signicant risks to the Internet. Research indicates that issueswith web caching can lead various security consequences, such asDenial-of-Service (DoS), Cross-site scripting (XSS), and informationleakage [4, 16, 17, 19, 28].Attacks against web cache typically fall into two categories, theweb cache deception (WCD)and theweb cache poisoning (WCP)[24,25]. WCD aim to deceive the cache into making condential in-formation publicly available online, whereas WCP involve poi-soning the cache with harmful payloads that are then distributedto unsuspecting users. In recent years, Mirheidar et al. [24,25]studied the severity of WCD by measuring Alexa Top websites,demonstrating the widespread threats on the Internet. However,due to the complexity, WCP have been studied in a case-by-caseform [4,16,17,19,24,28], focusing on revealing the specic vul-nerabilities while lacking a global Internet view of the severity. Asthe WCP poses a severe threat to the Internet, it is urgent to detectand prevent the vulnerabilities ahead of the attacker on the globalscale.In this paper, we aim to ll this gap by performing a system-atic detection of WCP vulnerabilities at scale. To achieve this goal,

--- page 4 ---

AttackerVictimWeb CacheWeb Server GET /account.php/notexist.jpg 200 OK Cache-Control: no-store account.php <!> GET /profile/notexist.jpg200 OKaccount.php <!>

--- page 5 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.we need to address three research questions: (1) How can we gen-erate testing requests that systematically probe cache poisoningvulnerabilities? (2) How can we accurately detect potential webcache poisoning? (3) How can we assess the impact of web cachepoisoning while minimizing disruption to normal users?To address these questions, we introduce a novel testing method-ology,HCache, designed to detect WCP vulnerabilities. For therst question, we employ acache-key-awareapproach that sys-tematically generates and mutates requests to identify elds notincluded in cache keys, thereby exposing potential inconsistencies.For the second question, we utilize a three-step detection strategyinvolving the issuance of a normal request, an attack request, and avalidation request. This strategy allows us to analyze dierences inthe response's status code, content, and length to detect potentialWCP vulnerabilities. For the third question, we incorporatecachebustervariables in our request parameters, ensuring that our testingdoes not disrupt normal website operations while maintaining theecacy of our detection approach.We evaluatedHCacheagainst Tranco Top 1,000 domains in-volving 22,114 subdomains with 51,596 distinct URL links. Ourevaluation discovers more than 1,000 websites across 172 domains,constituting 17% of the domains evaluated, are vulnerable to WCP.Moreover, we identify 7 new attack variants to trigger WCP, includ-ing HTTP protocol headers, scope requests, conditional requests,and so on. Meanwhile, we investigated the caching dierences be-tween HTTP/2 and HTTP/1.1 and found that the WCP problem isalso prevalent in HTTP/2. Therefore, WCP is still a serious prob-lem, and network operators and caching service providers shouldtake appropriate measures to solve this problem. To the best of ourknowledge, this study represents the rst systematic, large-scaleevaluation of WCP within a scientic framework. We reportedthe vulnerabilities to the aected websites and received acknowl-edgements from over 15 companies, including globally renownedones like Adobe, Alibaba, Huawei, and Microsoft. Additionally, wereceived bug bounties totalling over $1,000 from these entities.
In summary, we make the following contributions:
We introduced a novel testing methodology for large-scaleevaluation of websites for WCP on the Internet, along witha practical detection system named
HCache
1
.
We carried out a comprehensive analysis of the Tranco Top1,000 domains and their subdomains, discovering over 1,000websites across 172 domains vulnerable to WCP, indicatingthat 17% of measured domains are at risk.
We discovered 7 new attack vectors that can cause WCP at-tacks and found the WCP issues are still prevalent in HTTP/2.We have responsibly reported the vulnerabilities to the af-fected websites and received acknowledgements and over$1,000 bug bounties from many companies such as Adobe,Alibaba, Huawei, and Microsoft.
2 BACKGROUND
2.1 Web CacheWeb cache reduces network trac and optimizes application per-formance by caching frequently used network resources. It can be1
https://github.com/phantomnothingness/HCache
Figure 1: Process of web cache deceptioncategorized into private caching and shared proxy caching. Privatecaches are caching mechanisms within the web client itself (e.g., thebrowser cache[30]) and within the web server (e.g., the WordPressplugin cache[36]). Shared proxy caching mainly includes variousproxy servers and CDNs.The reports released by the three major CDN providers, Akamai,Cloudare, and Fastly, indicate that a signicant amount of networktrac passes through caching proxy communication each year [34].A measurement study by Guo et al. [6] shows that among the top1,000 domains in the Alexa ranking list, 74% of websites utilizeCDN services for content distribution and network acceleration.Additionally, there are many independent caching proxies (such asSquid [32], Varnish [33]) and caching servers (such as Apache [10],Nginx [26]) distributed throughout the Internet, indicating thatweb caching devices have become critical infrastructure for theInternet.Cache servers typically store static and commonly accessed re-sources like HTML, JS, CSS, images, and other media. Most webcaches, due to their shared nature, do not cache dynamic, person-alized, or sensitive content. The HTTP/1.1 specication's Cache-Control header directs caching devices on handling responses,such as Cache-Control: no-store to prevent storage. Despite RFCmandates for adherence to these headers, some caching devices andCDNs oer options to bypass them. A prevalent caching strategyinvolves rules based on resource paths and extensions, like cachingonly JPG, ICO, CSS, or JS les.
2.2 Web Cache AttackAs an important infrastructure in the Internet, web cache requiresutmost security. There are primarily two attack vectors targetingcache servers based on their caching characteristics [25].Web Cache Deception (WCD)is an attack that tricks the appli-cation into storing sensitive content belonging to other users in thecache. Subsequently, the attacker retrieves this content from thecache. Figure 1 shows the process of WCD: 1)The attacker tricks thevictim into visiting a URL that requests/account.php/nonexist.jpg.2)The request reaches the web server and ignore the non-existentpart of the URL. Web server send back a successful response withaccount.php, which has victim's private account. The web cachestore the response, interpreting it as a static image. 3)The attackervisits the same URL accessing the victim's information stored inthe cache.Web Cache Poisoning (WCP)is to induce the application tostore malicious content in the cache. The normal requests from

--- page 6 ---

AttackerVictimWeb CacheWeb Server Send Malicious HTTP Request Forward Malicious Request Return Error Response Cacheable Send Normal HTTP Request Hit Malicous Cache

--- page 7 ---

Is Cache KeyNot Cache KeyGET /1.css?x=1 HTTP/1.1Host: example.comUser-Agent: Mozilla/5.0 Windows NT 10.0Accept: text/html,*/*Accept-Language: zh-CN,zhCache Key: GET | example.com | /1.css?x=1

--- page 8 ---

AttackerVictimWeb CacheWeb ServerGET /a/ HTTP/1.1Host: example.comX-Malicious-Header: valueGET /a/ HTTP/1.1Host: example.comX-Malicious-Header: valueGET /a/ HTTP/1.1Host: example.com...GET /a/ HTTP/1.1Host: example.com...MISSForward the requestCache with Cache Key : GET | /a/ | example.comHTTP/1.1 400 Bad Requestsome errorHTTP/1.1 400 Bad Requestsome errorHTTP/1.1 301 Moved PermanentlyLocation: attack.comHTTP/1.1 301 Moved PermanentlyLocation: attack.com<html>...<script>alert(1);</script><html>...<script>alert(1);</script>ORORMalicious Response AMalicious Response BMalicious Response CHas the same Cache KeyHITMalicious Response

--- page 9 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Figure 2: Process of web cache poisoningother users may hit the cache, resulting in access to maliciouscontent. Figure 2 shows the process of WCP: 1)The attacker sends acarefully crafted malicious HTTP request. 2)The cache server failsto lter the malicious request and forwards it to the web server.3)The malicious request triggers an exception at the web server,resulting in a harmful response that the cache server stores. 4)Anormal request initiated by the victim hits the cached maliciousresource.These two attacks have two main dierences. (1) The attacktechniques are dierent: WCD achieves its goal by constructingabnormal URLs, it requires the victim to click on the maliciousURL to deceive the cache. WCP can exploit various parts of theHTTP request to poison the cache, directly resulting in the victimreceiving abnormal responses. (2) The attack objectives are dierent:WCD aims to steal sensitive information from the cache, whereasWCP aims to make the victim access error responses in the cache.Researchers have conducted extensive measurement studies onWCD [24,25]. However, there is currently a lack of large-scalemeasurements regarding WCP. This study focuses on the researchgap in the decit of a global WCP threat overview, by designingand implementing theHCacheto study the severity on the Internet.WCP has the merit of a wide-range attacking impact with justa simple attack. Specically, attackers only need to send a singleattacking request, while aecting numerous global Internet users.The larger the trac of a website, the greater the impact it cancause. In the entire attack chain, WCP can be conducted in conjunc-tion with other attacking techniques to broaden the attack surface,and their nal impact closely depends on the injected maliciouspayloads. If an error response is returned, it can lead to a Denialof Service (DoS) attack. If the response is dynamically generated,injection of JavaScript code can result in Cross-Site Scripting (XSS)attacks. If the location of redirect responses can be manipulated,arbitrary page replacement can occur. In a word, when combin-ing WCP with other attack methods, the severity can be furtherexpanded.
2.3 Limitation of Existing ResearchCurrent studies share a common limitation as they are all case-by-case investigations heavily reliant on empirical knowledge. Chen etal. proposed a new method for WCP by exploiting the Host header,termed "Host of Trouble" [1]. James Kettle introduced a novel tech-nique to execute such attacks using HTTP request elds, includingX-Forwarded-Host, request parameters, fat get request [16,17].Nguyen et al. proposed CPDoS, using three methods to conduct aDoS attack [28]. Mirheidari et al. conducted large-scale measure-ments on the impact of WCD on the Internet [24, 25].These studies have two main limitation: (1) They are case-by-case studies and do not systematically analyze the cache poisoningvectors that may result from dierent HTTP elds, which couldmiss many new attack vectors, as we demonstrate later; (2) Theylack large-scale measurements. Existing studies have either onlyconducted manual testing for CDNs and HTTP implementations, oronly conducted small-scale testing for certain attack types, leadingto many vulnerability instance undiscovered. Therefore, there is anurgent need for a systematic tool capable of conducting large-scalemeasurements to identify WCP vulnerabilities.
3 OVERVIEW
3.1 Threat ModelEssentially, web cache poisoning (WCP) attacks stem from the prob-lem withcache key. The cache key serves as the unique identierto locate and isolate cached objects, determining whether a requesthits the cache or not. Figure 3 presents an example of cache keysin HTTP requests. It typically consists of the request method, host-name, and URI. A cache hit occurs when a new request matches thecache key of a previous stored object that still remains valid withinthe cache; if not, the resource is retrieved from the web server.Figure 3: A example schema for cache keys in HTTP request
Figure 4: An example of web cache poisoningFigure 4 presents a example of WCP, where an attacker con-structs a malicious request with evil content in the headers. The

--- page 10 ---

þ81ÿF?ÿ þ

--- page 11 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.cache server forwards this request, triggering a malicious responsefrom the web server. Malicious responses could be an error page, aredirection to a 3rd-party website controlled by the attacker, or apage containing malicious content. Finally, the cache server thencaches this evil response, and victim requests with the same cachekey hit the poisoned cache, leading to a WCP attack. While WCPhas posed a severe threat to the Internet, there is lack of systematicevaluation of such vulnerabilities at scale.
3.2 MethodologyIn this paper, we present a novel testing methodology to detectWCP on the Internet. However, developing such a methodologyneeds to answer the following research questions.Q1: How can we generate testing requests to systematicallyprobe web cache poisoning vulnerabilities?Previous works [24,25,27] usually utilize manual approachesor collect known exploits to generate testing requests, and do notsystematically explore various HTTP elds and specic cachingbehaviors. This can lead to incomplete testing and the potentialoversight of new attack vectors. To address this, we have developeda cache-key-aware approach to systematically generate and mu-tate HTTP requests to uncover WCP vulnerabilities. We start withstandardized HTTP requests to incorporate typical header elds byleveraging syntax rules derived from HTTP RFCs. We then enumer-ate dierent HTTP elds such as request line, headers, and body touncover those elds not included in cache keys. Then we mutatenon-cache-key elds and body of requests to probe inconsistenciesbetween web caches and web servers, aiming to uncover potentialexploits. This allows for a more targeted and systematic generationof test cases for essentially identifying potential WCP issues.
Q2: How can we detect Web Cache Poisoning accurately?We design a three-phase testing approach to detect WCP ac-curately. First, we send a normal request to establish a baselineresponse. This is followed by a especially crafted request, wherepotential vulnerabilities are systematically tested. The response tothis request is then compared to the baseline response, identifyingdiscrepancies that may indicate a successful poisoning attack. Fi-nally, a validation request is sent to conrm the initial assessmentof WCP vulnerability. This approach allows us to pinpoint the exactconditions under which WCP can occur, providing a reliable meansof assessment.Q3: How can we assess the impact of WCP while minimiz-ing disruption to normal users?Minimizing the impact on normal users while assessing WCPis crucial. To achieve this, we employcache bustervariables in ourrequest parameters to isolate web caches. These variables, craftedas unique random values and cache keys, ensure that normal userrequests do not intersect with our crafted testing requests, therebypreventing access to potentially poisoned caches. This techniqueensures that our testing process does not disrupt the normal oper-ations of the website or the access of legitimate users, while stillmaintaining the high ecacy of WCP detection.
4 HCACHE: DESIGN AND IMPLEMENTATION
4.1 WorkowBased on the above methodology, we developedHCache, a large-scale detection system to detect web cache poisoning (WCP), de-picted in Figure 5.HCachecomprises three core modules: thePre-processing Module, theTest-case Generation Module, and theCache-poisoning Detection Module
.(1) ThePreprocessing Moduleprocesses the seed domain listthrough expansion, survivability checks, deduplication, and cacheableURL identication, outputting detectable URLs.(2) TheTest-case Generation Moduleidenties cache keys, pro-duces standard requests, and generates test cases for potential WCP.(3) TheCache-poisoning Detection Modulesynthesizes the priormodules' outputs to craft attack requests and assesses WCP vulner-abilities using varied attack payloads.The following paragraphs present detailed information on therelated working steps and specic modules.
4.2 Stage A. PreprocessingFirst, the list of URLs to be tested needs to be determined before thefollowing real-world measurement. Thus, thePreprocessing Moduleincludes the initial three steps, including subdomain extension,target URL nding, and URL deduplication.Step A.1) Subdomain Extension.Starting from initial domains,this process recursively crawls related HTTP/HTTPS pages togather subdomains with a 200 status code, thereby expanding thedomain list for further steps. Domains that do not return a 200status code are disregarded, as they are not typically accessed byweb clients. The next step then generates the initial set of URLs fortesting based on the collected subdomains.Step A.2) Target URL Finding.This component is a websitecrawler that uncovers URL resources through deep traversal andautomates website visits using Python's Requests library. To en-hance eciency for large-scale detection of popular websites, itoperates with multiple concurrent threads. In summary, the pro-gram sequentially crawls the target domain's homepage, extractingstatic resources such as JavaScript, images, and videos.Relevant studies indicate that using the HTTP header elds inthe response (e.g. 'age', 'x-cache') to determine whether a page iscached is a relatively accurate method[25]. Pages detected usingthis approach form a true subset of all cached pages, as certainwebsites may omit cache-related information in their responses. Wereferenced ocial documentation from major caching vendors tounderstand the specic caching behavior of dierent cache identityheaders. Additionally, the crawler discovers numerous related URLson third-party websites, including OSS storage, JS hosting, and self-built CDN services, and automatically adds these domains into thedomain discovery list.Step A.3) URL Deduplication.The deduplication module en-hances the eciency of large-scale cache-poisoning detection. Manyweb applications generate customized pages based on query stringsor URL path parameters, leading to similar URL structures beingcached together with the same vulnerabilities. Exhaustive testingof each URL is time-consuming and resource-intensive. To avoid re-dundant detection of similar URLs, obtained URL lists are processed.Utilizing the SimHash algorithm [31], we developed a program for

--- page 12 ---

Tranco Top 1kBugsBugsSubdomain ExtensionTarget URL FindingURL DeduplicationStandard HTTP Request CreationHTTP Request Line MutationHTTP Request Headers MutationHTTP Request Body MutationOther Illegal HTTP Request MutationCache BusterCache BusterDetecting Request GenerationWeb ServerResponse Difference AnalysisPoisoning ValidationA. PreprocessingB. Test Case GenerationC. Cache Poisoning DetectionTarget URL List

--- page 13 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Figure 5: Overview of our large-scale measurement system:
HCachefuzzy matching and URL similarity calculation to consolidate simi-lar URLs.For example,example.com/users/bob/blog1andexample.com/users/alice/article2may exhibit high similarity. Initially, we generalizethem based on letters (represented by C), numbers (represented byD), and special characters (represented by S):example.com/CCCCC/CCC/CCCCD. Subsequently, we assign weights according to thehierarchical levels of the path, where higher-level directories havegreater weights. Next, we use a directory of dierent levels askeywords to calculate feature vectors. We compute similarity byutilizing the Hamming distance between feature vectors, and URLswith excessively high similarity are deduplicated. In the end, thisprocess yields a set of URLs for testing, and ltering out URLs in thismanner signicantly reduces the testing workload. It also avoidsoverconsumption of the target server's resources with redundantscans.
4.3 Stage B. Test Case GenerationThe test case generation is the core module ofHCachethat outputsdierent request variations to comprehensively cover dierent WCPmethods. It includes standard HTTP request generation, cache keydetection, and multiple request mutation methods.Step B.1) Standard HTTP Request Creation.Informed byexpert insights and trac analysis, we've crafted standard HTTPrequest templates for common methods like HEAD, GET, and POST.These templates are designed to avoid rejection by mimicking nor-mal HTTP trac, including typical header elds like`Host', `User-Agent', `Cookie', and`Accept-Encoding', with the `Host' eld adapt-ing to the target domain automatically. This equipsHCachewith abasic suite of HTTP requests.Step B.2) HTTP Request Line Mutation.The HTTP requestLine, comprising theMethod,URI, andProtocol Version, is often acache key, thus we explore the impact of dierent elds of non-cache keys, such as method case insensitivity, parameter changes,and protocol version arbitrarily specied variants. WCP can occurwhen a non-cache key eld aects content generation or causesserver errors. For parameter mutation, we collect a list of com-mon parameters, whichHCacheutilizes to mutate HTTP requestparameters.Step B.3) HTTP Request Headers Mutation.The requestheader includes elds both from standard RFC specications andpopular web servers and CDN vendors. This complexity, coupledwith variations between middlebox and web server, often leads toinconsistencies and potential WCP vulnerabilities. It also bringsa great challenge to the detection of WCP: how to cover as manytypes of attacks as possible? To this end, we propose the followingvariants based on the characteristics of dierent headers.i.Request Headers Scanning: Some elds in the HTTP requestheader may also aect the web server's execution logic. A commontrick is to utilize forwarding headers (e.g.,`X-Forwarded-Host', `X-Forwarded-Scheme', `X-Forward-Port'), which are often used to passinformation among multi-hop HTTP servers. WCP occurs whenthe cache server uses these elds for routing without adding themto the cache key. Similarly, web server that fetches cookie eldsto generate readback data dynamically is vulnerable. Meanwhile,numerous real-world headers may dynamically aect the cachingresults, and dierent CDN vendors have their customized headersfor access control. This method involves gathering common requestheaders on the Internet and systematically altering HTTP requestswith these headers to evaluate their eect on WCP.ii.Special Headers Scanning: Certain HTTP request headers, asdened in RFCs, have specic value requirements, such as the`If-Unmodied-Since'header specifying a date format. Besides, webservers will format the header of a request, if a header's value doesnot conform (e.g., a random string), it's disregarded by web servers,hindering WCP detection. To address this, we generate syntax-compliant values that adhere to RFC specications for testing.iii.Blacklist HTTP Request Mutation: While WAFs block scannersor crawlers by common ltering mechanisms (eg. return403 IllegalAccess Responsewhen detecting`User-Agent'as SQLMap), somecache servers may not include`User-Agent'in the cache key, cre-ating an opportunity for WCP.HCacheemploys a blacklist-based

--- page 14 ---

þ81ÿF?ÿ þ

--- page 15 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.mutation mechanism that assesses the impact of security scanners(e.g. Nuclei) and web crawlers (e.g. PyCurl) on the cache. Addition-ally, it tests the cache's resilience to malicious`Referer'messagesfrom phishing sites and common blacklist strings used by WAFs(e.g.
<script>alert(1)</script>
).Step B.4) HTTP Request Body Mutation.While GET requeststypically lack a body, some HTTP services process bodies in GETrequests, causing abnormal behaviors like redirects or 400 errorresponses. Additionally, rewriting methods like`X-HTTP-Method-Override'can extend the attack payload. When a cache server trans-parently forwards such requests, and the web server responds withan exception consequently, it becomes susceptible to WCP.Step B.5) Other Illegal HTTP Request Mutation.Beyondmutating the three main components of the HTTP request, wecrafted other illegal HTTP requests to probe WCP vulnerabilities,examining the eects of overly long headers and invalid characters.Cache Buster.To nalize the test requests for WCP, we em-ployed acache busterwith two objectives: on the one hand, mod-ifying the value of thecache busteravoids interactions betweentargeting the same URL and prevents invalidation caused by newattack requests hitting the previous cache. On the other hand, it en-sures that normal user requests do not trigger responses poisonedby our tests, as they do not carry our randomly generatedcachebuster
.
4.4 Stage C. Cache Poisoning DetectionUnder this component,HCacherst initiates WCP detection foreach URL in the pending list, then analyzes the response to identifyvulnerabilities.HCacheperforms multiple rounds of WCP testingrapidly using multi-threading, encompassing request generation,response analysis, and cache poisoning validation.Step C.1) Detecting Request Generation.This module is usedto generate three HTTP requests, which are normal request, attackrequest and validation request. The normal request is obtained byadding the request parameter A to the standard request generated inStep B.1), which aims to check whether the cache buster is eectiveand collect the normal response of the target website for subsequentanalysis. The attack request is obtained by adding the dierentrequest parameter B from the test cases generated in the previousstage. The validation request is similar to the normal request, theonly dierence is it has the same request parameter B as the attackrequest.Step C.2) Response Dierence Analysis.HCacheidentiespotential WCP by analyzing dierences between the response re-turned by a normal request and an attack request. It assesses threetypes of information: a) whether the status code of the HTTP re-sponse has changed; b) whether the length of the HTTP responsebody has changed; c) whether the HTTP response contains addi-tional content of the poisoning request compared with the normalrequest. If one of the above conditions occurs,HCachedeterminesthat the target server may be threatened by WCP.Step C.3) Poisoning Validation.WhenHCachends a websitethat may have WCP vulnerabilities, it will use the validation requestto verify if the cache will be poisoned. This validation request issent within 1 second to verify that the WCP vulnerability can besuccessfully exploited. If the website is vulnerable, the validationresponse matches the last poisoned content, and the cache identityeld should display
HIT
.False positives in the measurement process are caused by mul-tiple similar requests from the same client being rejected by theweb server. When both an attack request and a validation requestreturn the same error response,HCachemistakenly assumes thatthe error request was cached. In order to eliminate false positives,HCachewill initiate two subsequent tests of the potential WCPvulnerability detected after a certain period. And all discoveredpotential vulnerabilities will be cross-validated on clients in dier-ent regions. Finally, we also manually veried the discovered WCPvulnerabilities.
5 MEASUREMENT STUDY AND FINDINGS
5.1 Data CollectionOur work use Tranco Top 1,000 domains as seeds, and extractsa total of 114,560 subdomain information, among which 31,350surviving websites can be accessed via HTTP(S). On this basis,more resource is crawled on these websites by the crawler, thusexpanding the target domains to 4,427,590 dierent URL links. Toincrease the testing eciency, URLs with similar paths are de-emphasized during the experiment, and nally, 1,417,004 URL linksare obtained. Then, the websites that contain the cache identityheader in the HTTP response packet are selected as targets fortesting. A total of 22,114 domains containing 51,596 dierent URLlinks were tested in this chapter. Then we conducted detectionmeasurements from 7 dierent VPS servers across the world, suchas New York, Frankfurt, Sydney and Tokyo. For each detected case,multiple repeated experiments are conducted across dierent geo-locations to eliminate accidental false positives that may arise. Inthe end, more than 1,300 websites were found to have web cachepoisoning (WCP) vulnerabilities, containing 1,556 dierent URLlinks.
5.2 Cache Key DetectionTo prevent the poisoned cache from aecting normal users duringtesting, we use a cache buster to isolate the cache. The test requestmust carry a crafted cache key dierent from the normal user'srequest, and the cache key used for the cache buster should be"irrelevant" and its modication must not aect the normal responsecontent. To this end, we designed a pre-experiment on cache keydetection to nd the best cache buster.We determine which elds are commonly used as cache keys bymodifying dierent parts of the HTTP request. From all the cachableURLs detected, URLs were randomly selected for each accessibledomain of the Tranco top 1,000. In most cases, if the parametercannot be recognised by the server, it will ignore without aectingthe corresponding content, indicating that the request parameter isa kind of eective cache buster. It will be used in the subsequentlarge-scale cache poisoning measurement to avoid aecting thenormal user's access.
5.3 OverviewWe conducted large-scale WCP detection experiments on popularwebsites on the Internet, and found 1,354 WCP vulnerabilities,aecting some world-famous websites, which have high Tranco

--- page 16 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Table 1: Newly discovered attack vectors by
HCache Type Common Attack payloads Vulnerable Websites*Internal Route Header Attack
X-Request-Id: 123456789 wikia.com
Fastly-Client-Ip: 123456789 fandom.com
Gpt-Tags-Enabled: 123456789 ipage.com
X-Amz-Request-Id: 123456789 stanford.edu
Fastly-Soc-X-Request-Id: 123456789 domain.com
X-Amz-Website-Redirect-Location: 123456 marriott.comHTTP Identication Header Attack
Auth-Key: 123456789 sinaimg.cn
X-Auth-User: 123456789 bing.com
Authorization:123456789 wsimg.com
X-Authorization: 123456789 zidavis.com
Client-Proxy-Auth-Required:123456789 ccmbg.comHTTP If Header Attack
If-Match: 123456789 usa.gov
If-Range: 123456789 aig.com
If-None-Match: 123456789 bluehost.com
If-Modied-Since: 123456789 starbucks.comHTTP Protocol Header Attack
X-Forwarded-SSL: on/o/nonsense pcmag.com
X-Forwarded-Scheme: nothttps/http(s) cisco.com
X-Forwarded-Proto: http(s)/ssl/nonsense mashable.com
X-Forwarded-Protocol: http(s)/nothttps/nonsense getywheel.comHTTP Range Header Attack
Range: bytes=cow stats.com
Range: bytes=9-4 miele.co.nz
Range: bytes=-1024,0 starbucks.com
Range: bytes=0-,0-,0-,0- chiltondiy.comHTTP Upgrade Header Attack
Upgrade: 123456789 legaro.fr
Upgrade: HTTP/0.9 smtp2go.com
Upgrage: Websocket, RTA/x11 salesforce.com
Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9 disney.ioHTTP Coding Header Attack
Accept: 123456789 fcc.gov
Accept-Encoding: 12345 house.gov
Transfer-Encoding: error europa.eu
zTRANSFER-ENCODING: asdf landmarkcinemas.com*: The vulnerable websites in the table only show the base domain. The subdomains and paths were redacted forethical considerations.
Table 2: Detection datasets and vulnerable websites statistics Initial domain name Domain name extension Cache pages Cache Poisoning VulnerabilitiesNumber of domain names
1,000 114,560 22,114 1,354
Number of URLs
- 1,417,004 51,596 1,556 rankings and a large amount of web trac, as shown in Table 1and Table 2. Besides, some websites may even have more thanone vulnerabilities. Once an attacker compromises these websitesthrough one of the identied WCP vulnerabilities, it will aect alarge number of global Internet end-users.We compare our detection results with existing studies in Table3 and Table 4. Compared with previous work, our study is moresystematic and comprehensive in terms of attack vector coverageand measurement scale, with many new attack methods and vul-nerabilities discovered. In total, 14 types of attack techniques arediscovered by
HCache
, 7 of which are newly discovered vectors.Figure 6 shows the percentage of dierent attacks, from whichwe can nd that known attacks still account for more than halfof the websites found to have WCP vulnerabilities, indicating thatvarious vendors are still not in place to protect against knownWCP attacks. In addition to the known issues, we also found thatmany other new HTTP elds may lead to WCP. This suggests thatany non-cache key could potentially be at risk of WCP. Protectionagainst a single attack method is not enough to fully defend againstthe eects of WCP.Figure 7 presents the distribution of vulnerable websites withrespect to their Tranco ranks, exhibiting a fairly uniform. Thissuggests that Web Cache Poisoning is pervasive among the websitesin our dataset with no strong connection to their popularity ranking.Moreover, we tested the impact of WCP in HTTP/2, using thesame variant of the scanning test on websites deployed with HTTP/2.We found that all the vulnerabilities that existed in HTTP/1.1 stillexisted in HTTP/2. About 90% of the websites share caches between

--- page 17 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.Table 3: Number of websites with1 vulnerabilities foundby
HCache Attack type NumberNew Attack Vectors
Internal Route Header Attack 237
Identify Header Attack 118
If Request Attack 79
Protocol Header Attack 69
Range Request Attack 46
Upgrade Request Attack 25
Coding Header Attack 19Vectors in CPDoS
HTTP Header Oversize (HHO) 269
HTTP Method Override (HMO) 149
HTTP Meta Character (HMC) 56Vectors in Blogs
Forwarded Header Attack 96
HTTP Parameter Attack 84
Fat Get Request Attack 67
Blacklist Attack 40 Figure 6: Impact ratio of dierent attack vectorsFigure 7: Distribution of vulnerable websites in Tranco rank-ingHTTP/1.1 and HTTP/2, i.e., after sending an HTTP/1.1 request topoison a cache, a normal HTTP/2 request afterward will still hitthe poisoned cache, and vice versa. This suggests that an HTTP/2to HTTP/1.1 transition may have occurred, implying that attackstargeting HTTP/1.1 could aect services utilizing HTTP/2.
5.4 FindingsWe present an overview of our ndings about attack vectors. Weidentied 14 types of attack vectors that could lead to cache poison-ing, among which 7 types are newly discovered. Table 1 shows thenew attack vectors we discovered and lists some specic payloadsthat can cause poisoning as well as the aected websites.Internal Route Header Attack.A CDN is a large distributednetwork with a large number of internal nodes that perform dif-ferent transmission and caching functions. Therefore, CDNs alsoimplement some special headers to pass routing information duringinternal transmission. Attackers can abuse these headers to triggerCDNs to throw exceptions, ultimately leading to WCP. These head-ers includeFastly-Client-Ip, Fastly-Soc-X-Request-Id, X-Amz-Website-Redirect-Location, X-Amzn-CDN-Cache,etc. This is the attack foundto aect most websites besides the HTTP Header Oversize Attack,with 234 websites aected.HTTP Authentication Header Attack.In certain APIs or gate-way systems, authenticating HTTP requests is a common require-ment. Some services use headers likeAuthorization, X-Auth-UserandAuth-Keyfor this purpose. An attacker can exploit this by send-ing a request to the cache server with these headers. The cacheserver forwards them to the web server. The web server nds thatthe value of the header is illegal and returns a response with adenial of access. The cache server retains the incorrectly cachedresource, returning it for equivalent requests.HCachefound 118websites have this problem.HTTP Protocol Header Attack.Cache servers use headers likeX-Forwarded-SSL, X-Forwarded-Scheme, X-Forwarded-Proto, andX-Forwarded-Protocolto identify client connection protocols. However,these headers may impact web server processing. Some serversrespond with a 301 redirect. If the redirect request retains theseheaders and redirects to the URL itself, it causes a DoS attack dueto excessive redirects. As per the HTTP standard, 301 responsesare cached, leading victims to hit the cache. In this scenario, ifan attacker utilizes headers such asX-Forwarded-Hostto controlthe redirected link address, it becomes easy to direct victims to amalicious site for subsequent attacks. A total of 69 websites arevulnerable.HTTP Range Header Attack.Clients utilize the Range headerto request specic portions of a resource, widely supported bymost intermediate servers for tasks like multi-threaded downloads.However, certain web servers lack support, leading to potentialsemantic dierences with cache servers. Some web servers maysupport Range requests but report errors when processing mal-formed ones (e.g.Range: bytes=100-90).HCachefound 46 websiteshave this problem.HTTP If Header Attack.HTTP standard headers likeIf-Match,If-Range, andIf-Modied-Sincedetermine if a web server meets spec-ied conditions. However,HCachediscovered some web serversgenerate 4xx or 5xx errors when processing these requests. If thecache server caches this status code, it will result in WCP. HCachefound 79 websites have this problem.HTTP Upgrade Header Attack.HTTP protocol allows up-grading an established connection to a new, incompatible protocolusing mechanisms likeUpgrade: Websocket. If an attacker initiates

--- page 18 ---

HTTP Header Oversize20%HTTP Method Override11%Forwarded Header Attack7%HTTP Parameter Attack6%Fat Get Request Attack5%HTTP Meta Character4%Blacklist Attack3%Internal Route Header Identify Header Attack9%If Request Attack6%Protocol Header Attack5%Range Request Attack3%Upgrade Request Attack2%Coding Header Attack1%

--- page 19 ---

%# %-123333333333333332222100.-+

--- page 20 ---

%+/1233333333333333333321.

--- page 21 ---

.12333333333333321. 	
"'+-01223333333333333333333333333333320-'
"'+.0122333333333333333333333333333320,&
#'+.012233333333333333333333333333320,&
#'+.0122333333333333333333333333332/+%
#'+.012233333333333333333333333321/+$#'+.01223333333333333333333333321/*$#'+.0122333333333333333333333321.*##'+.012333333333333333333333321.,.012333333333321.

--- page 22 ---

0510152025Vulnerable SitesTranco Rank100200 300 400 500 600 700 800 900 1000

--- page 23 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Table 4: Comparison with existing research Research Attack Vector Target Vulnerable WebsitesCPDoS [27] HHO HMO HMC Alexa top 500 12
Redening Unexploitable blog[16] Forwarded Attack Manual testing 11*
Novel Pathways to Poisoning blog [17] Para, Blacklist, and Fat GET Manual testing 8*
Our work 14 types of attack Tranco top 1,000 domains and their subdomains 1,354*: The authors did not fully disclose the number of vulnerabilities in their blogs, and the statistics in the table are derived from the cases in theirreport.an unsupported upgrade request (e.g.,Upgrade: HTTP/3.0) or a mal-formed one (e.g.,Upgrade: HTTP/0.9), web server may return anincorrect status code, potentially leading to a WCP.HCachefound25 websites have this problem.HTTP Coding Header Attack.The HTTP protocol uses head-ers likeAccept, Accept-Encoding, andTransfer-Encodingto identifyencoding formats. If an attacker sets a malformed or illegal valuein these headers, it may trigger an exception at the web server,potentially resulting in WCP.
HCache
found 19 websites have this
problem.What's more,HCachealso found many websites have knownattacks. Although these attacks have been presented in previousarticles[16,17,28], they still account for more than half of all vul-nerabilities, so it is necessary to analyze how such attacks areexploited.HTTP Header Oversize Attack.The HTTP protocol standarddoes not impose a limit on the length of the request header. There-fore, dierent Web middleboxes implement dierent restrictions.A DoS attack may exist if the request length allowed by the cacheserver exceeds the limitations of the web server. An attacker caninitiate an HTTP request with a length between the cache serverand web server. The cache server forwards the malicious request tothe web server, and an error response triggered at the web serverthat would have resulted in a DoS attack had it been cached bythe cache server. Although this vulnerability is a known one andhas been disclosed for many years, it still aects the most targetedwebsites with a total of 269.HTTP Method Override Attack.HTTP denes request meth-ods like GET, POST, DELETE, and PUT. Some systems only supportGET and POST. To overcome this, web frameworks use helper head-ers likeX-HTTP-Method-Override. Attackers may exploit this bysending a GET request with an override eld set to DELETE. If theserver doesn't handle DELETE requests, it returns a 405 error. Asper RFC9110, cache servers cache this error, causing subsequentequivalent requests to result in a DoS attack. A total of 149 websiteswere found to have this issue.HTTP Meta Character Attack.This attack utilizes a requestheader with harmful metacharacters, exploiting semantic dier-ences between the cache server and the web server. The cacheserver may tolerate certain special characters, forwarding them,while the web server, processing the request, triggers an error page,resulting in a DoS attack. Metacharacters involved could includecontrol characters like newline (\r), carriage return (\n), or anyUnicode control character. Attackers leverage this to launch WCPagainst vulnerable websites.HCachefound 56 websites vulnerableto this attack.Fat GET Attack.Cache servers usually cache GET requests bydefault, excluding the HTTP request body as a cache key. Despitethe HTTP standard prohibiting GET requests from having a body,some web applications parse fat GET request bodies, allowing dy-namic responses. This opens the door to WCP.HCacheenhancesdetection with headers likeX-HTTP-Method-Override, expandingthe attack vector. The web server, inuenced byX-HTTP-Method-Override, treats the request as a POST, attempting to generate adynamic link from the body. The cache server, ignoring this, usesthe cache key of the original GET request and URL. When a usertriggers a regular request hitting the attacker's tainted cache, con-tent hijacking occurs.HCachefound 67 websites has this problem.HTTP Parameters Attack.There are many applications thatchoose to extract parameter values from requests to dynamicallygenerate response content. If the web server uses the values in therequest parameters to dynamically generate content, and the webserver does not perform any ltering on the string, an attacker canconstruct an XSS attack payload to launch an attack. If the cacheserver's cache key does not contain the request parameter eldsin the URL, the cache is hit when a normal user initiates a request,resulting in malicious cache samples being distributed to the client,ultimately causing an XSS attack. Similar aws were found on 84websites.HTTP Forwarded Header Attack.Reverse proxies (e.g., loadbalancers, CDNs) rely on routing host information to determinethe web server for fetching web resources. RFC7239 introducesthe Forward header for this purpose. However, headers likeHost,X-Forwarded-Host, X-Forwarded-Port, andForwardedare commonlyused by reverse proxies to identify the original routing host. Thiscan be exploited for WCP. Attackers can manipulate these headersto control the cache server's routes back to the source, potentiallycausing the cache server to read malicious data or the web serverto reject responses. As these headers are not part of the cache key,victims may unwittingly hit the attacker's poisoned cache, leadingto an attack.
HCache
found 96 websites have this vulnerability.Blacklist Attack.WAFs often use blacklists to block malicioustrac.HCacheexplores three blacklisting mechanisms: manipulat-ing User-Agent with security scanners (e.g., sqlmap) and crawlers(e.g., Crawler), inserting known phishing site domain names (e.g.spam.com) into the Referer header, and randomly adding commonattack payloads (e.g.<script>alert(1)</script>) to certain headers.HCacheexploits inconsistencies in blacklist support between cache

--- page 24 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.server and web server. An attacker sends a request with a mali-cious string, triggering an exception on the web server. The webserver's WAF responds with a 403 Forbidden Access. The cacheserver incorrectly caches the resource, blocking even normal usersfrom accessing the target site.HCachefound 40 websites have thisproblem.
6 THREAT ANALYSISThe victim website can suer from various losses, such as reputationdegradation, supply chain attacks, or even monetary loss. In thispaper, we further categorized these WCP vulnerabilities based onthe specic attacking threats. Table 5 shows the vulnerabilities thatcan result from dierent types of attacks.
Table 5: Threats that stem from dierent attack vectors DoS XSS AUR*Internal Route Header Attack
!
Identify Header Attack
!
If Request Attack
!
Protocol Header Attack
! !
Range Request Attack
!
Upgrade Request Attack
!
Coding Header Attack
!
HTTP Header Oversize (HHO)
!
HTTP Method Override (HMO)
!
HTTP Meta Character (HMC)
!
Forwarded Header Attack
! ! !
HTTP Parameter Attack
!
Fat Get Request Attack
!
Blacklist Attack
!*AUR: Arbitrary URL RedirectionCache Poisoned Denial of Service.DoS attack is the mostbasic attack that can be caused by web cache poisoning (WCP). Itcan be caused by simply constructing an attack request that triggersan error at the web server. We found that even though CPDoS hasbeen disclosed for many years, there are still many websites thatare subject to such attacks, such asharvard.edu, taobao.com, mail.ru,and
huawei.com
.We have also found many other HTTP headers that can lead toDoS attacks. All of the 7 new attack vectors discovered by us cancause service inaccessibility on subdomains ofadobe.com, intuit.com,skype.com,andsina.com.cn, etc. A common feature of this type ofattack is that the cache server does not comply with the RFCsand caches error status codes that should not be cached. Even ifthe RFCs were followed,X-HTTP-Method-Override: NONSENSEcanbe used to poisonvisualstudio.microsoft.comwith 405 Method NotAllowed.nvidia.comandsap.comwill return 404 Not Found whenprocessing a request withX-Forwarded-Host: attack.com. Both 404and 405 response status codes are heuristically cacheable in RFC.Cache Poisoned Cross-Site Scripting.An attacker can exploitthese WCP vulnerabilities to launch beyond DoS attacks on vic-tim websites. When exploited in conjunction with other attackingtechniques, it may also lead to more severe damage. In fat GETattack and request parameter attack, the web server dynamicallygenerates a response using the request parameters or request body,but the cache server caches these dynamically generated responsesas static pages. Therefore, the attacker can inject malicious XSSpayloads into the response.HCachefound that some websites willinclude parameters or request body in the response. Our furthervalidation revealed that some websites do not lter request con-tent and can inject XSS payloads.edu.sina.com.cn, in.ign.comandblackfriday.com
have such vulnerabilities.Cache Poisoned Arbitrary URL Redirection.Previous re-search found X-Forwarded-Host can be used to control the actual re-sponse page, but our results show that when websites receive theseheaders containing unknown URLs (such asX-Forwarded-Host: at-tack.com), they will ignore them or return an error response such as400 Bad Request. It suggests that many websites have already xedthis vulnerability. However, we newly discovered X-Forwarded-Proto header can re-establish the connection, and will return 301redirect responses. Combined with the X-Forwarded-Host header,the redirected page can be controlled, resulting in an arbitrary pageredirect attack. The attacker can implement subsequent higher-order attacks if the victim accesses the attacker-controlled page.Take one of the subpages inthemeforest.netas an example. First,we establish an HTTPS connection with it. Then we can senda request withX-Forwarded-Scheme: httpandX-Forwarded-Host:attack.com. The former changes the protocol to HTTP and returnsa redirection response, while the latter species the response'slocation, redirecting to an attacker-controlled website. 301 MovedPermanently is cached by the cache server, causing subsequentvictim requests to be redirected to attacker-controlled pages aswell.
7 DISCUSSION
7.1 Responsible DisclosureWe try our best to responsibly disclose the related vulnerabilitiesto the vendors of aected websites. First, we actively contacted theaected vendors through several third-party vulnerability disclo-sure platforms (e.g., Hackerone, Bugcrowd, and Intigriti), discussingthe security issues and related mitigations. Second, we have sentnotication emails to the administrators of the aected websites,disclosing the vulnerabilities and the specic detection methodolo-gies. According to the rank of vulnerable websites, we summarizethe related responses to responsible disclosure below:Microsoftmicrosoft.com (6th in Tranco Top 1,000): Respondedthat they have shared the report with the inner responsible team,and they will take appropriate actions as needed to help their cus-tomers be well protected.AliBaBataobao.com (23th in Tranco Top 1,000): Conrmed andpatched the discovered DoS attack vulnerability, assessed the vul-nerability asMedium Critical, providing a vulnerability bounty ofabout 100$.Adobeadobe.com (65th in Tranco Top 1,000): Conrmed the vul-nerability and discussed the scope of the attack. They respondedthat they are evaluating the vulnerability internally and will providea x for the vulnerability in the near future.NetEase163.com (187th in Tranco Top 1,000): Rated the vulnera-bility as
Medium Critical
.

--- page 25 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USAYelpyelp.com (207th in Tranco Top 1,000): Thanked for the resultsof this research and acknowledged the issues identied in thispaper. They will continue to monitor the subsequent impact of thevulnerability and x the issue when appropriate.Mashablemashable.com (426th in Tranco Top 1,000): Conrmedthe vulnerability and highly praised the work, and suggested look-ing deeper into the potential harm of the attack, such as usingthe `X-Forwarded-Host' header to discover more vulnerable assetsinternally.HuaWeihuawei.com (537th in Tranco Top 1,000): Conrmedthis problem and agreed that it was caused by irregularities in theNginx cache conguration. They rated our reported vulnerabilityas
Medium Critical
and awarded about 200$ for the vulnerability.SAPsap.com (969th in Tranco Top 1,000): SAP has released thex for this issue, and they oer acknowledgment by publishing ourteam information on its webpage.Knowyourteam: They specically thanked the researcher forthe vulnerability report and have started the vulnerability remedia-tion process. Also added our team to the list of vulnerability-xingacknowledgments and gave some vulnerability bounty 100$.Street Context: They rated the vulnerability found in this paperas
Medium Critical
and awarded about 300$ for the vulnerability.VidaXL: They thanked the work of this paper and considered itvaluable research. They evaluated our discovered vulnerabilities asHigh Risk
and gave a vulnerability reward of about 300$.BlackFriday, Asana, YoYoGames, Zi Davis, Nutanix, Star-bucks, WP Engine: Acknowledged and thanked us for the vul-nerability report and advised that The issue has been identiedinternally and is in the process of being xed.
7.2 MitigationWCP is a complex and severe security problem, it is not a vulnera-bility within a single caching system, but rather the vulnerability ofparsing dierences between multiple caching systems. As a result,traditional static analysis and white-box testing techniques on asingle system are dicult to detect and eliminate the problem. Arecommended solution is to employ several methods together inproduction environments to minimize the cache poisoning problem.Add additional headers as the cache key: From our discoveries,when exploiting headers that have not been implemented as thecache keys within the caching systems, such as `X-HTTP-Method-Override' and `X-Forwarded-Host', a successful web cache poisoning(WCP) happens. Therefore, it is applicable and benecial to enforcethese headers as the cache keys within the caching systems. Withthis mitigation, even if the attacker has successfully poisoned thecache with an error response, this poisoned cache is only privateto the specic request with the problematic headers. As a normalrequest does not contain the problematic header, it will not hit thepoisoned cache thus invalidating the attack.Adhere to the RFC specications: Most vulnerabilities found bytheHCacheare caused by the caching of error responses that aremaliciously triggered by attackers, while these caching behaviorsare implementation-specic and not specied by the related RFCs.Therefore, the eective mitigation is to strictly follow the RFCstandards, only caching the error status codes that are allowed bythe RFCs, and returning other status codes directly for requeststhat should not be cached.Enhance exception handling at the web server: Based on our nd-ings, an attacker can proactively trigger error responses at thewebsite web server, which results in WCP. Thus, to avoid returningan error response for malformed HTTP requests, we suggest thewebsite server enhance a good exception handling design, whichjust ignores the problematic request headers and returns a benignresponse instead, or directly returns an error code indicating thatthe response should not be cached by any on-path cache servers.Thus, normal users still obtain the correct response, invalidatingWCP.Disable caching of dynamic resources: Web caching should onlybe applied to accelerate static resources, not dynamically generatedpages. Therefore, caching should be disabled for resources thatneed to be dynamically generated according to request parameters.HCachehas found that, although resources (such as CSS and JS)are normally categorized as static resources, some websites gen-erate these resources using dynamic templates, actually turningthese static-looking resources into dynamic resources. Hence, thebest way to x this is to directly change these resources to staticresources. If this dynamic generation feature is essential for thewebsite operation, we suggest clearly indicating the dynamic natureof these resources to disable the caching behavior. Besides, the web-site can also add various XSS lters to proactively defend againstWCP resulting from the dynamically generated web content.Reduce the caching time of error pages:The caching system canalso reduce the impact by only caching error response within ashort time, such as 1 second. This approach can proactively limit theeective time of WCP and greatly increase the attacking diculty.7.3 LimitationDue to the complexity of WCP and the scale of our measurements,our work still has the following limitations, which can be furtheroptimized in future works.Testing scope.Our research only analyzes individual websitesfrom the top 1,000 Tranco domains. However, our proposed toolHCacheis also applicable to wider measurement, which apparentlycan further reveal the severe threat of WCP on the Internet.Detection on caching behaviors. HCachedetection presupposesthat the target caching system adopts relevant header identiersfor cache operations. However, there are still some cache servers inreal web environments that do not use such identiers. Therefore,the websites covered by the tests in this chapter are a subset ofwebsites running cache servers in the real world.Evaluation on web pages with crucial functionality. HCachedoesnot consider user permissions in detecting WCP. Commonly, web-sites have service-critical or data-sensitive pages that are only ac-cessible to users that require log in, while which are not included inour work. We believe more severe threats can be discovered whenfurther works incorporate the detection of login-related web pages.Measurements of poisoning techniques.Our work mainly focuseson the well-known WCP that mostly threatens the Internet, thusHCache's request variant module is based on four types of variantpatterns dened by expert knowledge. Although our framework

--- page 26 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.
has attempted to include various attacking techniques as much as
possible, there may still be WCP that
HCache
does not cover.
7.4 Ethical ConsiderationIn this study, we have taken our uttermost care to avoid any ethicalconcerns both in the design and implementation.For security concerns, the exception requests generated byour tests conform to the HTTP syntax specication and are onlylikely to cause the web server to return an incorrect response andthen close the connection, without aecting the normal operationof the server. We use cache buster to avoid the impact on normalusers; the request parameters of the test request are randomlygenerated, and normal user requests will not hit the poisoned cachebecause of the dierent cache key. In addition, our tests found thatmost of error responses have much shorter cache times relativeto normal responses, and unlike an attacker continuously sendingattack requests to poison the cache, our experiments sent only oneattack request, thus the poisoned caches will not survive for morethan 10 minutes according to the cache time in all experiments.Further, to ensure that the poisoned caches will not continue toexist, we sent normal requests to each potentially poisoned site afterour experiments, to make sure that the caches had been refreshedto normal responses. For performance concerns, we ltered a largenumber of target URL links using URL similarity detection. Westrictly limit the request rate, a single URL to 5 requests per second,which will not place an excessive performance load on the websitesand CDNs.For privacy concerns, only URL information related to cachepoisoning was captured and analyzed, and no privacy data of thetarget website was saved locally, nor was any content of the tar-get website indexed and otherwise made public. In addition, weuse an HTTP header (User-Agent) embedded with our researchpurpose and contact information during the scanning process. Ifwebsite administrators notice any adverse eects caused by theautomated scanning on their websites, they can timely contact us,and we will promptly cease the automated scanning of the targetwebsite. We strictly followed the principle of responsible disclosureto report discovered vulnerabilities to aected websites, by activelycontacting through various channels such as email and third-partysecurity disclosure communities. The case mentioned in the articlehas already been xed.
8 RELATED WORKOur research focuses on web cache poisoning (WCP) caused bynon-cache keys in HTTP requests, and delves deep into variousdetails of actual poisoning attacks and exploits. In addition, thereare several other attacking tricks to perform WCP or to exploitcache aws for other purposes. Host-of-Trouble attack exploitsinconsistencies in the parsing of the host header in HTTP requestsbetween the cache server and the web server, to perform WCP andWAF bypassing[1].HTTP Desync Attack poisons the cache by smuggling an addi-tional request to disrupt the responses with malicious payloads[14,18,20]. WCD tricks a web cache into erroneously storing sensitivecontent, thereby making it widely accessible on the Internet[4,24,25].Two detection tools are most relevant to the work in this paper.One isParam Miner[15], designed by James Kettle, which is usedto scan whether some headers and parameters are included incache keys to detect potential WCP. Another one isWeb CacheVulnerability Scanner[9], which summarizes some of the previouslyproposed methods of WCP, and allows for the detection of knownattack methods.HCacheworks as a superset of these two tools,it analyses the request line, request header, and request body ofan HTTP request to generate corresponding test cases that cancomprehensively test the dierent aspects of WCP.Since James Kettle demonstrated the severity and prevalence ofrequest smuggling in 2019, researchers have come up with severaltools to detect attacks on request smuggling[2,5,29]. T-reqs isa novel grammar-based dierential fuzzer to test HTTP requestsmuggling[12]. Frameshifter aim to discover the security impli-cations of HTTP/2-to-HTTP/1 conversion anomalies[11]. Large-scale measurements of web cache[27], HTTP(S)[3,23], CDN[13]e-mails[35] or other web attacks[25], provides insights into thecurrent security problems on the Internet, allowing us to betteraddress potential security risks. To our knowledge, our work isthe rst large-scale examination of the WCP attack, revealing theprevalence of this threat on the Internet.In addition to WCP, cache servers, especially CDN, have othersecurity issues. Its working mechanisms can also bring WCP [1,24],DoS attacks[8], or other forms of attacks[7,21,22]. Compared tothe above research on"forwarding", our work focuses on"caching",revealing the pervasive security risks posed by the inconsistentprocessing of requests between websites and cache servers. Ourwork highlights this widespread systemic problem, which can mo-tivate cache vendors and webmasters to properly implement andcongure the caching, strictly adhering to HTTP standards speci-cations.
9 CONCLUSIONWeb cache poisoning (WCP) has been a signicant threat on theInternet, however, it still lacks a global view of the severe impact atscale. We have proposed a systematic measuring platformHCache,which enables a large-scale evaluation of WCP threats on the real-world Internet. Based on Tranco Top 1K domains and their sub-domains, we have discovered more than 1,000 websites across 172domains (17% of measured domains) with WCP vulnerabilities. Ourwork rst reveals that WCP threat is a widespread security issue onthe Internet, and discloses that WCP threat still exists in the newincoming protocols. We have responsibly reported the vulnerabili-ties to the aected websites, receiving acknowledgments and over$1,000 bug bounties from world-famous companies such as Adobe,Alibaba, Huawei, and Microsoft.
ACKNOWLEDGMENTSWe sincerely thank all anonymous reviewers and our shepherd fortheir insightful and constructive feedback to improve the paper.This work is supported by the National Natural Science Foundationof China (grant #62272265).
REFERENCES
[1]Jianjun Chen, Jian Jiang, Haixin Duan, Nicholas Weaver, Tao Wan, and VernPaxson. Host of troubles: Multiple host ambiguities in http implementations. In

--- page 27 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USAProceedings of the 2016 ACM SIGSAC Conference on Computer and CommunicationsSecurity
, pages 15161527, 2016.
[2] Evan Custodio. Smuggler. https://github.com/defparam/smuggler, 2020.
[3]Zakir Durumeric, James Kasten, Michael Bailey, and J Alex Halderman. Analysisof the https certicate ecosystem. InProceedings of the 2013 conference on Internetmeasurement conference
, pages 291304, 2013.
[4] Omer Gil. Web cache deception attack.
Black Hat USA
, 2017, 2017.
[5]Mattias Grenfeldt, Asta Olofsson, Viktor Engström, and Robert Lagerström. At-tacking websites using http request smuggling: empirical testing of servers andproxies. In2021 IEEE 25th International Enterprise Distributed Object ComputingConference (EDOC)
, pages 173181. IEEE, 2021.
[6]Run Guo, Jianjun Chen, Baojun Liu, Jia Zhang, Chao Zhang, Haixin Duan, TaoWan, Jian Jiang, Shuang Hao, and Yaoqi Jia. Abusing cdns for fun and prot:Security issues in cdns' origin validation. In2018 IEEE 37th Symposium on ReliableDistributed Systems (SRDS)
, pages 110. IEEE, 2018.
[7]Run Guo, Jianjun Chen, Yihang Wang, Keran Mu, Baojun Liu, Xiang Li, ChaoZhang, Haixin Duan, and Jianping Wu. TemporalfCDN-Convexglens: AfCDN-Assistedgpractical pulsingfDDoSgattack. In32nd USENIX Security Symposium(USENIX Security 23)
, pages 61856202, 2023.
[8]Run Guo, Weizhong Li, Baojun Liu, Shuang Hao, Jia Zhang, Haixin Duan, KaiwenSheng, Jianjun Chen, and Ying Liu. Cdn judo: Breaking the cdn dos protectionwith itself. In
NDSS
, 2020.
[9]Hackmanit. Web cache vulnerability scanner. https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner.
[10]Apache http server project. caching guide. https://httpd.apache.org/docs/2.4/caching.html.
[11]Bahruz Jabiyev, Steven Sprecher, Anthony Gavazzi, Tommaso Innocenti, KaanOnarlioglu, and Engin Kirda.fFRAMESHIFTERg:fram security implications offHTTP/2-to-HTTP/1gconversion anomalies. In31st USENIX Security Symposium(USENIX Security 22)
, pages 10611075, 2022.
[12]Bahruz Jabiyev, Steven Sprecher, Kaan Onarlioglu, and Engin Kirda. T-reqs: Httprequest smuggling with dierential fuzzing. InProceedings of the 2021 ACMSIGSAC Conference on Computer and Communications Security, pages 18051820,2021.
[13]Lin Jin, Shuai Hao, Haining Wang, and Chase Cotton. Unveil the hidden presence:Characterizing the backend interface of content delivery networks. In2019 IEEE27th International Conference on Network Protocols (ICNP), pages 111. IEEE, 2019.[14]James Kettle. Http/2: The sequel is always worse. https://portswigger.net/research/http2.
[15] James Kettle. Parem miner. https://github.com/PortSwigger/param-miner.
[16]James Kettle. Practical web cache poisoning: Redening 'unexploitable'. https://portswigger.net/research/practical-web-cache-poisoning.
[17]James Kettle. Web cache entanglement: Novel pathways to poisoning. https://portswigger.net/research/web-cache-entanglement.
[18]James Kettle. Http desync attacks: Smashing into the cell next door.Black HatUSA
, 2019.
[19]Amid Klein. Divide and conquer.HTTP Response Splitting, Web Cache PoisoningAttacks and Related Topics, Sanctum whitepaper
, 2004.
[20]Amit Klein. Http request smuggling in 2020new variants, new defenses andnew challenges.
Black Hat Briengs USA
, 8, 2020.
[21]Weizhong Li, Kaiwen Shen, Run Guo, Baojun Liu, Jia Zhang, Haixin Duan, ShuangHao, Xiarun Chen, and Yao Wang. Cdn backred: amplication attacks based onhttp range requests. In2020 50th Annual IEEE/IFIP International Conference onDependable Systems and Networks (DSN)
, pages 1425. IEEE, 2020.
[22]Jinjin Liang, Jian Jiang, Haixin Duan, Kang Li, Tao Wan, and Jianping Wu. Whenhttps meets cdn: A case of authentication in delegated service. In2014 IEEESymposium on Security and Privacy
, pages 6782. IEEE, 2014.
[23]Abner Mendoza, Phakpoom Chinprutthiwong, and Guofei Gu. Uncovering httpheader inconsistencies and the impact on desktop/mobile websites. InProceedingsof the 2018 World Wide Web Conference
, pages 247256, 2018.
[24]Seyed Ali Mirheidari, Sajjad Arshad, Kaan Onarlioglu, Bruno Crispo, Engin Kirda,and William Robertson. Cached and confused: Web cache deception in the wild.In
29th USENIX Security Symposium (USENIX Security 20)
, pages 665682, 2020.
[25]Seyed Ali Mirheidari, Matteo Golinelli, Kaan Onarlioglu, Engin Kirda, and BrunoCrispo. Web cache deception escalates! In31st USENIX Security Symposium(USENIX Security 22)
, pages 179196, 2022.
[26]Nginx. Nginx content caching. https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/.
[27]Hoai Viet Nguyen, Luigi Lo Iacono, and Hannes Federrath. Mind the cache: large-scale explorative study of web caching. InProceedings of the 34th ACM/SIGAPPSymposium on Applied Computing
, pages 24972506, 2019.
[28]Hoai Viet Nguyen, Luigi Lo Iacono, and Hannes Federrath. Your cache has fallen:Cache-poisoned denial-of-service attack. InProceedings of the 2019 ACM SIGSACConference on Computer and Communications Security
, pages 19151936, 2019.
[29]PortSwigger. Exploiting http request smuggling vulnerabilities. https://portswigger.net/web-security/request-smuggling/exploiting, 2020.
[30]Mike Reddy and Graham P Fletcher. An adaptive mechanism for web browsercache management.
IEEE Internet Computing
, 2(1):7881, 1998.
[31]Caitlin Sadowski and Greg Levin. Simhash: Hash-based similarity detection,2007.
[32] Squid. Squid: Optimising web delivery. http://www.squid-cache.org/.
[33] Varnish. Varnish http cache. https://varnish-cache.org/.
[34]w3techs. Cloudare vs. akamai vs. fastly usage statistics. https://w3techs.com/technologies/comparison/cn-akamai,cn-cloudflare,cn-fastly.
[35]Chuhan Wang, Kaiwen Shen, Minglei Guo, Yuxuan Zhao, Mingming Zhang,Jianjun Chen, Baojun Liu, Xiaofeng Zheng, Haixin Duan, Yanzhong Lin, et al. Alarge-scale and longitudinal measurement study offDKIMgdeployment. In31stUSENIX Security Symposium (USENIX Security 22)
, pages 11851201, 2022.
[36] WordPress. Wp super cache. https://wordpress.org/plugins/wp-super-cache/.

--- page 28 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.
A CACHE IDENTIFICATION FIELD
Table 6: Common caching status elds used by major service vendors Cache Service/Software Response Header Hit MissAzure X-Cache TCP_HIT TCP_MISS
Fastly X-Cache HIT MISS
Akamai X-Cache, Server-Timing desc=HIT desc=MISS
CDN77 X-Cache, X-77-Cache HIT MISS
CloudFront X-Cache Hit from cloudfront Miss from cloudfront
UDomain X-Cache-Status HIT MISS
KeyCDN X-Cache HIT MISS
Cloudare CF-Cache-Status HIT MISS
GCoreLabs Cache HIT MISS
ChinaCache X-cc-via *[H,*] *[M,*]
Github Pages X-Cache HIT MISS
Google Cloud cdn_cache_status hit mis
Incapsula CDN X-Iinfo ...0CNN... ...PNNN...
AlibabaCloud X-Cache HIT TCP_IMS_HIT MISS TCP_MISS
Tencent Cloud X-Cache-Lookup Hit From * / Cache Hit Cache Miss
HUAWEI CLOUD X-Cache-Lookup Hit From * Miss From *
Baidu AI Cloud CDN X-Cache-Status HIT MISSApache Trac Server X-Cache HIT MISS
Squid X-Cache Hit From * Miss From *
Varnish X-Cache HIT MISS
Nginx Cache_status, X-Proxy-Cache HIT MISS
Apache X-Cache HIT MISS
Rack Cache X-Rack-Cache Hit Fresh/Miss

--- page 29 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild CCS '24, October 1418, 2024, Salt Lake City, UT, USA
B KNOWN ATTACK VECTORS
Table 7: Examples of known attack vectors discovered by
HCache Type Common Attack payloads Vulnerable Websites*HTTP Header Oversize
taobao.com
X-Oversized-Header-[1-N]: nvidia.com
Big-Value-000000000000...000000000000 mail.ru
dropbox.comHTTP Method Override
X-HTTP-Method: PUT house.gov
X-HTTP-Method: TRACE bmw.com
X-Method-Override: TRACE mailchimp.com
X-HTTP-Method-Override: POST huawei.com
X-HTTP-Method-Override: DELETE microsoft.comHTTP Meta Character
Header\u:1234 aadcoinst.com
X-Metachar-Header: \0 house.gov
X-Metachar-Header: \b house.govFat GET
GET /?id=1 HTTP/1.1 nih.gov
X-HTTP-Method-Override: POST sina.com.cn
... gouvernement.lu
attack=<script>alert(1);</script> adobe.comHTTP Parameters
/app?cong=<script>alert(1);</script>// ign.com
/base.css?exp=<script>alert(1);<script> hotelscombined.com
/index.js?utm_medium=x;callback=alert(1)// cdlvr.netHTTP Forwarded Header
Host: example.com:1337 grab.careers
Forwarded: Host=attack.com bing.com
X-Forwarded-Host: attack.com blackfriday.com
X-Forwarded-Port: 1337 yoyogames.comBlacklist
Referer: spam.com yelp.com
Referer: <script>alert(1)</script> alipayobjects.com
Any-Header:.burpcollaborator.net salesforce.com
User-Agent: sqlmap/1.3.11#stable jfrogchina.com
User-Agent: Nmap Scripting Engine alipay.com*: The vulnerable websites in the table only show the base domain. The subdomains and paths wereredacted for ethical considerations.

--- page 30 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
B KNOWN ATTACK VECTORS
Table 7: Examples of known attack vectors discovered by
HCacheT
ype
Common Attack payloads
Vulnerable Websites*H
TTP Header Oversize
taobao.com
X-Oversized-Header-[1-N]:
nvidia.com
Big-Value-000000000000...000000000000
mail.ru
dropbox.comH
TTP Method Override
X-HTTP-Method: PUT
house.gov
X-HTTP-Method: TRACE
bmw.com
X-Method-Override: TRACE
mailchimp.com
X-HTTP-Method-Override: POST
huawei.com
X-HTTP-Method-Override: DELETE
microsoft.comH
TTP Meta Character
Header\u:1234
aadcoinst.com
X-Metachar-Header: \0
house.gov
X-Metachar-Header: \b
house.govFat
GET
GET /?id=1 HTTP/1.1
nih.gov
X-HTTP-Method-Override: POST
sina.com.cn
...
gouvernement.lu
attack=<script>alert(1);</script>
adobe.comH
TTP Parameters
/app?cong=<script>alert(1);</script>//
ign.com
/base.css?exp=<script>alert(1);<script> hotelscombined.com
/index.js?utm_medium=x;callback=alert(1)//
cdlvr.netH
TTP Forwarded Header
Host: example.com:1337
grab.careers
Forwarded: Host=attack.com
bing.com
X-Forwarded-Host: attack.com
blackfriday.com
X-Forwarded-Port: 1337
yoyogames.comBlacklist
Refer
er: spam.com
yelp.com
Referer: <script>alert(1)</script>
alipayobjects.com
Any-Header:.burpcollaborator.net
salesforce.com
User-Agent: sqlmap/1.3.11#stable
jfrogchina.com
User-Agent: Nmap Scripting Engine
alipay.com*: The vulnerable websites in the table only show the base domain. The subdomains and paths wereredacted for ethical considerations.

--- page 31 ---

2°-9°"@*+:<$9°
±99±²999°&µ"$9±7	³*+-/$9°°901'#'7672327&#"'4?654'&"&#"5674#"'672BVüTT×Dzh>DjmHX;�oN7Í–QD! VþN%-þÎV%v%ºN><'+³N¹²6+´H6+²?+°+3°/±!é³+°3´+°2°O/°;Ö±Fé°2°F±é°/°F±N+´3 +°3° Ö±é°/±	é±P+±F³@A$9°µ$6BCH$9°N³+,$9°	±-99°3°.9±?H±3;99±!³	$901"&54632"&54632%!".54>3!2'727!".5'727!2>5m>5/%!3ü™%/0$#11+þWªÉ%E%ðþÙP•š^%‡%Xd�P-¸+@
+25$9±°9±±%099°*³	
5$9±%°9°5°'9°0±"99±°9012#".546'64>7632#"'6&'.#"3267`_?<B+DÍ®1-278$9±2°49°
²-999012#".5462654.#"'732632#"'&"'6;`_?<B+C99±°9°
°-9014"3252632#"'2&! '5437>54&/"=7áRTTRTäX¼Éïä'/?8dþùþö`5?21@5`˜NMúNNsÍ‡ËÌün+'''%-â-$'XþÛRPL²+´+²+°
/´+° /°Ö´+° Ö±
é°
2±!+±µ	$9015673#.".5473jTTR10Ú/4;`J
bŽƒTÙL#PZ
2ý´1#5/u!žo¨/#LPöš	J°/´"+°/´"+°/°Ö´,+°±+´ +±+±°9±±9901324'&#"&547672#"Ñdf=fJ7HD[^@FJ?_o5þð;u;XýðZ�šdX^š®ZL‘åéF°/´ +°/°Ö´+°2°´,+°/±+±±99°´
$901462"4'7672&#0567‘%6&&6
'I+@�6&&6%þ¬žB
mtZ�eR”'þ“!$X²+°/°3´"9+°2°%/°!Ö°#2´,+°2²!
+³@	+±&+±!²	999±"°9°±$9901"'476532732+&#"567'3d;}œ*$9°±99°
²99901654#"5654'&#"#'7632#"/?7^-y–7FzT6;�D+3VHojF!6+ž%T3†+5V;%G…!%+Hj8/>V9'ÿ/Å!$K°/°3´"9+°2°%/°!Ö°#2´,+°2²!
+³@	+±&+±!²	999±"°901"'476532732+&#"567'3d;}œ++

--- page 32 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.
A CACHE IDENTIFICATION FIELD
Table 6: Common caching status elds used by major service vendorsCache
Service/Software Response Header
Hit
MissAzur
e
X-Cache
TCP_HIT
TCP_MISS
Fastly
X-Cache
HIT
MISS
Akamai
X-Cache, Server-Timing desc=HIT
desc=MISS
CDN77
X-Cache, X-77-Cache HIT
MISS
CloudFront
X-Cache
Hit from cloudfront Miss from cloudfront
UDomain
X-Cache-Status
HIT
MISS
KeyCDN
X-Cache
HIT
MISS
Cloudare
CF-Cache-Status
HIT
MISS
GCoreLabs
Cache
HIT
MISS
ChinaCache
X-cc-via
*[H,*]
*[M,*]
Github Pages
X-Cache
HIT
MISS
Google Cloud
cdn_cache_status
hit
mis
Incapsula CDN
X-Iinfo
...0CNN...
...PNNN...
AlibabaCloud
X-Cache
HIT TCP_IMS_HIT MISS TCP_MISS
Tencent Cloud
X-Cache-Lookup
Hit From * / Cache Hit Cache Miss
HUAWEI CLOUD X-Cache-Lookup
Hit From *
Miss From *
Baidu AI Cloud CDN X-Cache-Status
HIT
MISSApache
Trac Server X-Cache
HIT
MISS
Squid
X-Cache
Hit From *
Miss From *
Varnish
X-Cache
HIT
MISS
Nginx
Cache_status, X-Proxy-Cache HIT
MISS
Apache
X-Cache
HIT
MISS
Rack Cache
X-Rack-Cache
Hit
Fresh/Miss

--- page 33 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USAProceedings of the 2016 ACM SIGSAC Conference on Computer and CommunicationsSecurity, pages 15161527, 2016.
[2] Evan Custodio. Smuggler. https://github.com/defparam/smuggler, 2020.
[3]Zakir Durumeric, James Kasten, Michael Bailey, and J Alex Halderman. Analysis
of the https certicate ecosystem. In
Proceedings of the 2013 conference on Internetmeasurement conference, pages 291304, 2013.
[4] Omer Gil. Web cache deception attack.
Black Hat USA, 2017, 2017.
[5]Mattias Grenfeldt, Asta Olofsson, Viktor Engström, and Robert Lagerström. At-tacking websites using http request smuggling: empirical testing of servers andproxies. In
2021 IEEE 25th International Enterprise Distributed Object ComputingConference (EDOC), pages 173181. IEEE, 2021.
[6]Run Guo, Jianjun Chen, Baojun Liu, Jia Zhang, Chao Zhang, Haixin Duan, TaoWan, Jian Jiang, Shuang Hao, and Yaoqi Jia. Abusing cdns for fun and prot:Security issues in cdns' origin validation. In
2018 IEEE 37th Symposium on ReliableDistributed Systems (SRDS), pages 110. IEEE, 2018.
[7]Run Guo, Jianjun Chen, Yihang Wang, Keran Mu, Baojun Liu, Xiang Li, ChaoZhang, Haixin Duan, and Jianping Wu. TemporalfCDN-Convexglens: AfCDN-Assistedgpractical pulsingfDDoSgattack. In
32nd USENIX Security Symposium(USENIX Security 23), pages 61856202, 2023.
[8]Run Guo, Weizhong Li, Baojun Liu, Shuang Hao, Jia Zhang, Haixin Duan, KaiwenSheng, Jianjun Chen, and Ying Liu. Cdn judo: Breaking the cdn dos protectionwith itself. In
NDSS, 2020.
[9]Hackmanit. Web cache vulnerability scanner. https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner.
[10]Apache http server project. caching guide. https://httpd.apache.org/docs/2.4/caching.html.
[11]Bahruz Jabiyev, Steven Sprecher, Anthony Gavazzi, Tommaso Innocenti, KaanOnarlioglu, and Engin Kirda.fFRAMESHIFTERg:fram security implications offHTTP/2-to-HTTP/1gconversion anomalies. In
31st USENIX Security Symposium(USENIX Security 22), pages 10611075, 2022.
[12]Bahruz Jabiyev, Steven Sprecher, Kaan Onarlioglu, and Engin Kirda. T-reqs: Httprequest smuggling with dierential fuzzing. In
Proceedings of the 2021 ACMSIGSAC Conference on Computer and Communications Security, pages 18051820,2021.
[13]Lin Jin, Shuai Hao, Haining Wang, and Chase Cotton. Unveil the hidden presence:Characterizing the backend interface of content delivery networks. In
2019 IEEE27th International Conference on Network Protocols (ICNP), pages 111. IEEE, 2019.[14]James Kettle. Http/2: The sequel is always worse. https://portswigger.net/research/http2.
[15] James Kettle. Parem miner. https://github.com/PortSwigger/param-miner.
[16]James Kettle. Practical web cache poisoning: Redening 'unexploitable'. https://portswigger.net/research/practical-web-cache-poisoning.
[17]James Kettle. Web cache entanglement: Novel pathways to poisoning. https://portswigger.net/research/web-cache-entanglement.
[18]James Kettle. Http desync attacks: Smashing into the cell next door.
Black HatUSA, 2019.
[19]Amid Klein. Divide and conquer.
HTTP Response Splitting, Web Cache PoisoningAttacks and Related Topics, Sanctum whitepaper, 2004.
[20]Amit Klein. Http request smuggling in 2020new variants, new defenses andnew challenges.
Black Hat Briengs USA, 8, 2020.
[21]Weizhong Li, Kaiwen Shen, Run Guo, Baojun Liu, Jia Zhang, Haixin Duan, Shuang
Hao, Xiarun Chen, and Yao Wang. Cdn backred: amplication attacks based onhttp range requests. In
2020 50th Annual IEEE/IFIP International Conference onDependable Systems and Networks (DSN), pages 1425. IEEE, 2020.
[22]Jinjin Liang, Jian Jiang, Haixin Duan, Kang Li, Tao Wan, and Jianping Wu. Whenhttps meets cdn: A case of authentication in delegated service. In
2014 IEEESymposium on Security and Privacy, pages 6782. IEEE, 2014.
[23]Abner Mendoza, Phakpoom Chinprutthiwong, and Guofei Gu. Uncovering httpheader inconsistencies and the impact on desktop/mobile websites. In
Proceedingsof the 2018 World Wide Web Conference, pages 247256, 2018.
[24]Seyed Ali Mirheidari, Sajjad Arshad, Kaan Onarlioglu, Bruno Crispo, Engin Kirda,and William Robertson. Cached and confused: Web cache deception in the wild.In
29th USENIX Security Symposium (USENIX Security 20), pages 665682, 2020.
[25]Seyed Ali Mirheidari, Matteo Golinelli, Kaan Onarlioglu, Engin Kirda, and BrunoCrispo. Web cache deception escalates! In
31st USENIX Security Symposium(USENIX Security 22), pages 179196, 2022.
[26]Nginx. Nginx content caching. https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/.
[27]Hoai Viet Nguyen, Luigi Lo Iacono, and Hannes Federrath. Mind the cache: large-scale explorative study of web caching. In
Proceedings of the 34th ACM/SIGAPPSymposium on Applied Computing, pages 24972506, 2019.
[28]Hoai Viet Nguyen, Luigi Lo Iacono, and Hannes Federrath. Your cache has fallen:
Cache-poisoned denial-of-service attack. In
Proceedings of the 2019 ACM SIGSACConference on Computer and Communications Security, pages 19151936, 2019.
[29]PortSwigger. Exploiting http request smuggling vulnerabilities. https://portswigger.net/web-security/request-smuggling/exploiting, 2020.
[30]Mike Reddy and Graham P Fletcher. An adaptive mechanism for web browsercache management.
IEEE Internet Computing, 2(1):7881, 1998.
[31]Caitlin Sadowski and Greg Levin. Simhash: Hash-based similarity detection,2007.
[32] Squid. Squid: Optimising web delivery. http://www.squid-cache.org/.
[33] Varnish. Varnish http cache. https://varnish-cache.org/.
[34]w3techs. Cloudare vs. akamai vs. fastly usage statistics. https://w3techs.com/technologies/comparison/cn-akamai,cn-cloudflare,cn-fastly.
[35]Chuhan Wang, Kaiwen Shen, Minglei Guo, Yuxuan Zhao, Mingming Zhang,Jianjun Chen, Baojun Liu, Xiaofeng Zheng, Haixin Duan, Yanzhong Lin, et al. Alarge-scale and longitudinal measurement study offDKIMgdeployment. In
31stUSENIX Security Symposium (USENIX Security 22), pages 11851201, 2022.
[36] WordPress. Wp super cache. https://wordpress.org/plugins/wp-super-cache/.

--- page 34 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.
has attempted to include various attacking techniques as much as
possible, there may still be WCP that
HCache
does not cover.
7.4 Ethical ConsiderationIn this study, we have taken our uttermost care to avoid any ethicalconcerns both in the design and implementation.For security concerns, the exception requests generated by
our tests conform to the HTTP syntax specication and are onlylikely to cause the web server to return an incorrect response andthen close the connection, without aecting the normal operationof the server. We use cache buster to avoid the impact on normalusers; the request parameters of the test request are randomlygenerated, and normal user requests will not hit the poisoned cachebecause of the dierent cache key. In addition, our tests found thatmost of error responses have much shorter cache times relativeto normal responses, and unlike an attacker continuously sendingattack requests to poison the cache, our experiments sent only oneattack request, thus the poisoned caches will not survive for morethan 10 minutes according to the cache time in all experiments.
Further, to ensure that the poisoned caches will not continue toexist, we sent normal requests to each potentially poisoned site afterour experiments, to make sure that the caches had been refreshedto normal responses. For performance concerns, we ltered a largenumber of target URL links using URL similarity detection. Westrictly limit the request rate, a single URL to 5 requests per second,
which will not place an excessive performance load on the websitesand CDNs.For privacy concerns, only URL information related to cachepoisoning was captured and analyzed, and no privacy data of thetarget website was saved locally, nor was any content of the tar-
get website indexed and otherwise made public. In addition, we
use an HTTP header (User-Agent) embedded with our research
purpose and contact information during the scanning process. If
website administrators notice any adverse eects caused by theautomated scanning on their websites, they can timely contact us,and we will promptly cease the automated scanning of the targetwebsite. We strictly followed the principle of responsible disclosure
to report discovered vulnerabilities to aected websites, by activelycontacting through various channels such as email and third-partysecurity disclosure communities. The case mentioned in the articlehas already been xed.
8 RELATED WORKOur research focuses on web cache poisoning (WCP) caused by
non-cache keys in HTTP requests, and delves deep into variousdetails of actual poisoning attacks and exploits. In addition, thereare several other attacking tricks to perform WCP or to exploit
cache aws for other purposes. Host-of-Trouble attack exploitsinconsistencies in the parsing of the host header in HTTP requestsbetween the cache server and the web server, to perform WCP andWAF bypassing[1].HTTP Desync Attack poisons the cache by smuggling an addi-tional request to disrupt the responses with malicious payloads[14,18,20]. WCD tricks a web cache into erroneously storing sensitivecontent, thereby making it widely accessible on the Internet[4,24,25].Two detection tools are most relevant to the work in this paper.One is
Param Miner
[15], designed by James Kettle, which is usedto scan whether some headers and parameters are included in
cache keys to detect potential WCP. Another one is
Web CacheVulnerability Scanner
[9], which summarizes some of the previouslyproposed methods of WCP, and allows for the detection of knownattack methods.
HCache
works as a superset of these two tools,
it analyses the request line, request header, and request body of
an HTTP request to generate corresponding test cases that cancomprehensively test the dierent aspects of WCP.Since James Kettle demonstrated the severity and prevalence of
request smuggling in 2019, researchers have come up with severaltools to detect attacks on request smuggling[2,5,29]. T-reqs is
a novel grammar-based dierential fuzzer to test HTTP request
smuggling[12]. Frameshifter aim to discover the security impli-
cations of HTTP/2-to-HTTP/1 conversion anomalies[11]. Large-
scale measurements of web cache[27], HTTP(S)[3,23], CDN[13]
e-mails[35] or other web attacks[25], provides insights into the
current security problems on the Internet, allowing us to better
address potential security risks. To our knowledge, our work isthe rst large-scale examination of the WCP attack, revealing theprevalence of this threat on the Internet.In addition to WCP, cache servers, especially CDN, have othersecurity issues. Its working mechanisms can also bring WCP [1,24],DoS attacks[8], or other forms of attacks[7,21,22]. Compared tothe above research on
"forwarding", our work focuses on
"caching",revealing the pervasive security risks posed by the inconsistent
processing of requests between websites and cache servers. Ourwork highlights this widespread systemic problem, which can mo-tivate cache vendors and webmasters to properly implement andcongure the caching, strictly adhering to HTTP standards speci-cations.
9 CONCLUSIONWeb cache poisoning (WCP) has been a signicant threat on theInternet, however, it still lacks a global view of the severe impact atscale. We have proposed a systematic measuring platform
HCache,which enables a large-scale evaluation of WCP threats on the real-world Internet. Based on Tranco Top 1K domains and their sub-domains, we have discovered more than 1,000 websites across 172domains (17% of measured domains) with WCP vulnerabilities. Our
work rst reveals that WCP threat is a widespread security issue onthe Internet, and discloses that WCP threat still exists in the newincoming protocols. We have responsibly reported the vulnerabili-ties to the aected websites, receiving acknowledgments and over$1,000 bug bounties from world-famous companies such as Adobe,Alibaba, Huawei, and Microsoft.
ACKNOWLEDGMENTSWe sincerely thank all anonymous reviewers and our shepherd fortheir insightful and constructive feedback to improve the paper.This work is supported by the National Natural Science Foundationof China (grant #62272265).
REFERENCES
[1]Jianjun Chen, Jian Jiang, Haixin Duan, Nicholas Weaver, Tao Wan, and VernPaxson. Host of troubles: Multiple host ambiguities in http implementations. In

--- page 35 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USAYelp
yelp.com (207th in Tranco Top 1,000)
: Thanked for the resultsof this research and acknowledged the issues identied in thispaper. They will continue to monitor the subsequent impact of thevulnerability and x the issue when appropriate.Mashable
mashable.com (426th in Tranco Top 1,000)
: Conrmedthe vulnerability and highly praised the work, and suggested look-ing deeper into the potential harm of the attack, such as usingthe `X-Forwarded-Host' header to discover more vulnerable assetsinternally.HuaWei
huawei.com (537th in Tranco Top 1,000)
: Conrmedthis problem and agreed that it was caused by irregularities in theNginx cache conguration. They rated our reported vulnerabilityas
Medium Critical
and awarded about 200$ for the vulnerability.SAP
sap.com (969th in Tranco Top 1,000)
: SAP has released thex for this issue, and they oer acknowledgment by publishing ourteam information on its webpage.Knowyourteam: They specically thanked the researcher forthe vulnerability report and have started the vulnerability remedia-tion process. Also added our team to the list of vulnerability-xingacknowledgments and gave some vulnerability bounty 100$.Street Context: They rated the vulnerability found in this paperas
Medium Critical
and awarded about 300$ for the vulnerability.VidaXL: They thanked the work of this paper and considered it
valuable research. They evaluated our discovered vulnerabilities asHigh Risk
and gave a vulnerability reward of about 300$.BlackFriday, Asana, YoYoGames, Zi Davis, Nutanix, Star-bucks, WP Engine: Acknowledged and thanked us for the vul-
nerability report and advised that The issue has been identiedinternally and is in the process of being xed.
7.2 MitigationWCP is a complex and severe security problem, it is not a vulnera-bility within a single caching system, but rather the vulnerability ofparsing dierences between multiple caching systems. As a result,traditional static analysis and white-box testing techniques on asingle system are dicult to detect and eliminate the problem. Arecommended solution is to employ several methods together inproduction environments to minimize the cache poisoning problem.Add additional headers as the cache key
: From our discoveries,
when exploiting headers that have not been implemented as thecache keys within the caching systems, such as `X-HTTP-Method-Override
' and `X-Forwarded-Host
', a successful web cache poisoning
(WCP) happens. Therefore, it is applicable and benecial to enforcethese headers as the cache keys within the caching systems. Withthis mitigation, even if the attacker has successfully poisoned thecache with an error response, this poisoned cache is only privateto the specic request with the problematic headers. As a normalrequest does not contain the problematic header, it will not hit thepoisoned cache thus invalidating the attack.Adhere to the RFC specications
: Most vulnerabilities found bythe
HCache
are caused by the caching of error responses that aremaliciously triggered by attackers, while these caching behaviorsare implementation-specic and not specied by the related RFCs.Therefore, the eective mitigation is to strictly follow the RFCstandards, only caching the error status codes that are allowed bythe RFCs, and returning other status codes directly for requeststhat should not be cached.Enhance exception handling at the web server
: Based on our nd-ings, an attacker can proactively trigger error responses at thewebsite web server, which results in WCP. Thus, to avoid returningan error response for malformed HTTP requests, we suggest thewebsite server enhance a good exception handling design, whichjust ignores the problematic request headers and returns a benignresponse instead, or directly returns an error code indicating thatthe response should not be cached by any on-path cache servers.
Thus, normal users still obtain the correct response, invalidatingWCP.Disable caching of dynamic resources
: Web caching should onlybe applied to accelerate static resources, not dynamically generatedpages. Therefore, caching should be disabled for resources thatneed to be dynamically generated according to request parameters.HCache
has found that, although resources (such as CSS and JS)
are normally categorized as static resources, some websites gen-
erate these resources using dynamic templates, actually turningthese static-looking resources into dynamic resources. Hence, thebest way to x this is to directly change these resources to static
resources. If this dynamic generation feature is essential for thewebsite operation, we suggest clearly indicating the dynamic nature
of these resources to disable the caching behavior. Besides, the web-site can also add various XSS lters to proactively defend againstWCP resulting from the dynamically generated web content.Reduce the caching time of error pages:
The caching system canalso reduce the impact by only caching error response within ashort time, such as 1 second. This approach can proactively limit theeective time of WCP and greatly increase the attacking diculty.7.3 LimitationDue to the complexity of WCP and the scale of our measurements,our work still has the following limitations, which can be furtheroptimized in future works.Testing scope.
Our research only analyzes individual websites
from the top 1,000 Tranco domains. However, our proposed toolHCache
is also applicable to wider measurement, which apparentlycan further reveal the severe threat of WCP on the Internet.Detection on caching behaviors. HCache
detection presupposes
that the target caching system adopts relevant header identiersfor cache operations. However, there are still some cache servers inreal web environments that do not use such identiers. Therefore,the websites covered by the tests in this chapter are a subset ofwebsites running cache servers in the real world.Evaluation on web pages with crucial functionality. HCache
doesnot consider user permissions in detecting WCP. Commonly, web-sites have service-critical or data-sensitive pages that are only ac-cessible to users that require log in, while which are not included inour work. We believe more severe threats can be discovered whenfurther works incorporate the detection of login-related web pages.Measurements of poisoning techniques.
Our work mainly focuseson the well-known WCP that mostly threatens the Internet, thusHCache
's request variant module is based on four types of variantpatterns dened by expert knowledge. Although our framework

--- page 36 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.server and web server. An attacker sends a request with a mali-
cious string, triggering an exception on the web server. The web
server's WAF responds with a 403 Forbidden Access. The cacheserver incorrectly caches the resource, blocking even normal usersfrom accessing the target site.
HCache
found 40 websites have thisproblem.
6 THREAT ANALYSISThe victim website can suer from various losses, such as reputationdegradation, supply chain attacks, or even monetary loss. In thispaper, we further categorized these WCP vulnerabilities based onthe specic attacking threats. Table 5 shows the vulnerabilities thatcan result from dierent types of attacks.
Table 5: Threats that stem from dierent attack vectorsDoS
XSS AUR*Internal
Route Header Attack
!
Identify Header Attack
!
If Request Attack
!
Protocol Header Attack
!
!
Range Request Attack
!
Upgrade Request Attack
!
Coding Header Attack
!
HTTP Header Oversize (HHO)
!
HTTP Method Override (HMO)
!
HTTP Meta Character (HMC)
!
Forwarded Header Attack
! ! !
HTTP Parameter Attack
!
Fat Get Request Attack
!
Blacklist Attack
!*
AUR: Arbitrary URL RedirectionCache Poisoned Denial of Service.
DoS attack is the mostbasic attack that can be caused by web cache poisoning (WCP). Itcan be caused by simply constructing an attack request that triggersan error at the web server. We found that even though CPDoS hasbeen disclosed for many years, there are still many websites thatare subject to such attacks, such as
harvard.edu, taobao.com, mail.ru,and
huawei.com.We have also found many other HTTP headers that can lead toDoS attacks. All of the 7 new attack vectors discovered by us cancause service inaccessibility on subdomains of
adobe.com, intuit.com,skype.com,
and
sina.com.cn, etc. A common feature of this type ofattack is that the cache server does not comply with the RFCs
and caches error status codes that should not be cached. Even ifthe RFCs were followed,
X-HTTP-Method-Override: NONSENSE
canbe used to poisonvisualstudio.microsoft.com
with 405 Method NotAllowed.
nvidia.com
and
sap.com
will return 404 Not Found when
processing a request with
X-Forwarded-Host: attack.com
. Both 404and 405 response status codes are heuristically cacheable in RFC.Cache Poisoned Cross-Site Scripting.An attacker can exploitthese WCP vulnerabilities to launch beyond DoS attacks on vic-tim websites. When exploited in conjunction with other attackingtechniques, it may also lead to more severe damage. In fat GETattack and request parameter attack, the web server dynamicallygenerates a response using the request parameters or request body,
but the cache server caches these dynamically generated responsesas static pages. Therefore, the attacker can inject malicious XSSpayloads into the response.
HCache
found that some websites willinclude parameters or request body in the response. Our further
validation revealed that some websites do not lter request con-tent and can inject XSS payloads.
edu.sina.com.cn, in.ign.com
andblackfriday.com
have such vulnerabilities.Cache Poisoned Arbitrary URL Redirection.
Previous re-search found X-Forwarded-Host can be used to control the actual re-
sponse page, but our results show that when websites receive theseheaders containing unknown URLs (such as
X-Forwarded-Host: at-tack.com
), they will ignore them or return an error response such as
400 Bad Request. It suggests that many websites have already xedthis vulnerability. However, we newly discovered X-Forwarded-Proto header can re-establish the connection, and will return 301redirect responses. Combined with the X-Forwarded-Host header,the redirected page can be controlled, resulting in an arbitrary pageredirect attack. The attacker can implement subsequent higher-order attacks if the victim accesses the attacker-controlled page.Take one of the subpages in
themeforest.net
as an example. First,we establish an HTTPS connection with it. Then we can send
a request with
X-Forwarded-Scheme: http
and
X-Forwarded-Host:attack.com. The former changes the protocol to HTTP and returnsa redirection response, while the latter species the response'slocation, redirecting to an attacker-controlled website. 301 MovedPermanently is cached by the cache server, causing subsequent
victim requests to be redirected to attacker-controlled pages aswell.
7 DISCUSSION
7.1 Responsible DisclosureWe try our best to responsibly disclose the related vulnerabilitiesto the vendors of aected websites. First, we actively contacted theaected vendors through several third-party vulnerability disclo-sure platforms (e.g., Hackerone, Bugcrowd, and Intigriti), discussingthe security issues and related mitigations. Second, we have sentnotication emails to the administrators of the aected websites,disclosing the vulnerabilities and the specic detection methodolo-gies. According to the rank of vulnerable websites, we summarizethe related responses to responsible disclosure below:Microsoft
microsoft.com (6th in Tranco Top 1,000)
: Respondedthat they have shared the report with the inner responsible team,and they will take appropriate actions as needed to help their cus-tomers be well protected.AliBaBa
taobao.com (23th in Tranco Top 1,000)
: Conrmed andpatched the discovered DoS attack vulnerability, assessed the vul-
nerability as
Medium Critical, providing a vulnerability bounty ofabout 100$.Adobe
adobe.com (65th in Tranco Top 1,000)
: Conrmed the vul-nerability and discussed the scope of the attack. They respondedthat they are evaluating the vulnerability internally and will providea x for the vulnerability in the near future.NetEase
163.com (187th in Tranco Top 1,000)
: Rated the vulnera-bility as
Medium Critical.

--- page 37 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Table 4: Comparison with existing researchResear
ch
Attack Vector
Target
Vulnerable WebsitesCPDoS
[27]
HHO HMO HMC
Alexa top 500
12
Redening Unexploitable blog[16] Forwarded Attack
Manual testing
11*
Novel Pathways to Poisoning blog [17] Para, Blacklist, and Fat GET
Manual testing
8*
Our work
14 types of attack Tranco top 1,000 domains and their subdomains 1,354*: The authors did not fully disclose the number of vulnerabilities in their blogs, and the statistics in the table are derived from the cases in theirreport.an unsupported upgrade request (e.g.,
Upgrade: HTTP/3.0
) or a mal-formed one (e.g.,
Upgrade: HTTP/0.9
), web server may return anincorrect status code, potentially leading to a WCP.
HCache
found25 websites have this problem.HTTP Coding Header Attack.
The HTTP protocol uses head-ers like
Accept, Accept-Encoding, and
Transfer-Encoding
to identifyencoding formats. If an attacker sets a malformed or illegal valuein these headers, it may trigger an exception at the web server,potentially resulting in WCP.
HCache
found 19 websites have this
problem.What's more,
HCache
also found many websites have known
attacks. Although these attacks have been presented in previousarticles[16,17,28], they still account for more than half of all vul-nerabilities, so it is necessary to analyze how such attacks areexploited.HTTP Header Oversize Attack.
The HTTP protocol standarddoes not impose a limit on the length of the request header. There-fore, dierent Web middleboxes implement dierent restrictions.A DoS attack may exist if the request length allowed by the cacheserver exceeds the limitations of the web server. An attacker caninitiate an HTTP request with a length between the cache serverand web server. The cache server forwards the malicious request tothe web server, and an error response triggered at the web serverthat would have resulted in a DoS attack had it been cached bythe cache server. Although this vulnerability is a known one andhas been disclosed for many years, it still aects the most targetedwebsites with a total of 269.HTTP Method Override Attack.
HTTP denes request meth-ods like GET, POST, DELETE, and PUT. Some systems only support
GET and POST. To overcome this, web frameworks use helper head-ers like
X-HTTP-Method-Override. Attackers may exploit this bysending a GET request with an override eld set to DELETE. If theserver doesn't handle DELETE requests, it returns a 405 error. Asper RFC9110, cache servers cache this error, causing subsequentequivalent requests to result in a DoS attack. A total of 149 websiteswere found to have this issue.HTTP Meta Character Attack.
This attack utilizes a requestheader with harmful metacharacters, exploiting semantic dier-
ences between the cache server and the web server. The cache
server may tolerate certain special characters, forwarding them,while the web server, processing the request, triggers an error page,resulting in a DoS attack. Metacharacters involved could include
control characters like newline (\r), carriage return (\n), or anyUnicode control character. Attackers leverage this to launch WCPagainst vulnerable websites.
HCache
found 56 websites vulnerableto this attack.Fat GET Attack.
Cache servers usually cache GET requests bydefault, excluding the HTTP request body as a cache key. Despitethe HTTP standard prohibiting GET requests from having a body,some web applications parse fat GET request bodies, allowing dy-namic responses. This opens the door to WCP.
HCache
enhances
detection with headers like
X-HTTP-Method-Override, expandingthe attack vector. The web server, inuenced by
X-HTTP-Method-Override, treats the request as a POST, attempting to generate adynamic link from the body. The cache server, ignoring this, usesthe cache key of the original GET request and URL. When a usertriggers a regular request hitting the attacker's tainted cache, con-tent hijacking occurs.
HCache
found 67 websites has this problem.HTTP Parameters Attack.
There are many applications thatchoose to extract parameter values from requests to dynamicallygenerate response content. If the web server uses the values in therequest parameters to dynamically generate content, and the webserver does not perform any ltering on the string, an attacker canconstruct an XSS attack payload to launch an attack. If the cacheserver's cache key does not contain the request parameter eldsin the URL, the cache is hit when a normal user initiates a request,resulting in malicious cache samples being distributed to the client,ultimately causing an XSS attack. Similar aws were found on 84websites.HTTP Forwarded Header Attack.
Reverse proxies (e.g., loadbalancers, CDNs) rely on routing host information to determine
the web server for fetching web resources. RFC7239 introducesthe Forward header for this purpose. However, headers like
Host,X-Forwarded-Host, X-Forwarded-Port
, and
Forwarded
are commonlyused by reverse proxies to identify the original routing host. Thiscan be exploited for WCP. Attackers can manipulate these headersto control the cache server's routes back to the source, potentiallycausing the cache server to read malicious data or the web serverto reject responses. As these headers are not part of the cache key,victims may unwittingly hit the attacker's poisoned cache, leadingto an attack.
HCache
found 96 websites have this vulnerability.Blacklist Attack.
WAFs often use blacklists to block malicioustrac.
HCache
explores three blacklisting mechanisms: manipulat-ing User-Agent with security scanners (e.g., sqlmap) and crawlers(e.g., Crawler), inserting known phishing site domain names (e.g.spam.com) into the Referer header, and randomly adding commonattack payloads (e.g.
<script>alert(1)</script>) to certain headers.HCache
exploits inconsistencies in blacklist support between cache

--- page 38 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.Table 3: Number of websites with1 vulnerabilities foundby
HCacheAttack
type
NumberNe
w Attack Vectors
Internal Route Header Attack 237
Identify Header Attack
118
If Request Attack
79
Protocol Header Attack
69
Range Request Attack
46
Upgrade Request Attack
25
Coding Header Attack
19V
ectors in CPDoS
HTTP Header Oversize (HHO) 269
HTTP Method Override (HMO) 149
HTTP Meta Character (HMC) 56V
ectors in Blogs
Forwarded Header Attack
96
HTTP Parameter Attack
84
Fat Get Request Attack
67
Blacklist Attack
40
Figur
e 6: Impact ratio of dierent attack vectorsFigure 7: Distribution of vulnerable websites in Tranco rank-ingHTTP/1.1 and HTTP/2, i.e., after sending an HTTP/1.1 request topoison a cache, a normal HTTP/2 request afterward will still hitthe poisoned cache, and vice versa. This suggests that an HTTP/2to HTTP/1.1 transition may have occurred, implying that attackstargeting HTTP/1.1 could aect services utilizing HTTP/2.
5.4 FindingsWe present an overview of our ndings about attack vectors. Weidentied 14 types of attack vectors that could lead to cache poison-ing, among which 7 types are newly discovered. Table 1 shows thenew attack vectors we discovered and lists some specic payloadsthat can cause poisoning as well as the aected websites.Internal Route Header Attack.
A CDN is a large distributednetwork with a large number of internal nodes that perform dif-ferent transmission and caching functions. Therefore, CDNs alsoimplement some special headers to pass routing information duringinternal transmission. Attackers can abuse these headers to triggerCDNs to throw exceptions, ultimately leading to WCP. These head-
ers include
Fastly-Client-Ip, Fastly-Soc-X-Request-Id, X-Amz-Website-
Redirect-Location, X-Amzn-CDN-Cache,
etc. This is the attack foundto aect most websites besides the HTTP Header Oversize Attack,with 234 websites aected.HTTP Authentication Header Attack.
In certain APIs or gate-way systems, authenticating HTTP requests is a common require-ment. Some services use headers like
Authorization, X-Auth-Userand
Auth-Key
for this purpose. An attacker can exploit this by send-ing a request to the cache server with these headers. The cacheserver forwards them to the web server. The web server nds thatthe value of the header is illegal and returns a response with a
denial of access. The cache server retains the incorrectly cached
resource, returning it for equivalent requests.
HCache
found 118websites have this problem.HTTP Protocol Header Attack.
Cache servers use headers likeX-Forwarded-SSL, X-Forwarded-Scheme, X-Forwarded-Proto, and
X-Forwarded-Protocol
to identify client connection protocols. However,these headers may impact web server processing. Some servers
respond with a 301 redirect. If the redirect request retains theseheaders and redirects to the URL itself, it causes a DoS attack dueto excessive redirects. As per the HTTP standard, 301 responses
are cached, leading victims to hit the cache. In this scenario, if
an attacker utilizes headers such as
X-Forwarded-Host
to controlthe redirected link address, it becomes easy to direct victims to amalicious site for subsequent attacks. A total of 69 websites arevulnerable.HTTP Range Header Attack.
Clients utilize the Range headerto request specic portions of a resource, widely supported bymost intermediate servers for tasks like multi-threaded downloads.However, certain web servers lack support, leading to potential
semantic dierences with cache servers. Some web servers may
support Range requests but report errors when processing mal-formed ones (e.g.
Range: bytes=100-90
).
HCache
found 46 websiteshave this problem.HTTP If Header Attack.
HTTP standard headers like
If-Match,
If-Range, and
If-Modied-Since
determine if a web server meets spec-ied conditions. However,
HCache
discovered some web serversgenerate 4xx or 5xx errors when processing these requests. If thecache server caches this status code, it will result in WCP. HCachefound 79 websites have this problem.HTTP Upgrade Header Attack.
HTTP protocol allows up-grading an established connection to a new, incompatible protocolusing mechanisms like
Upgrade: Websocket. If an attacker initiates

--- page 39 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Table 1: Newly discovered attack vectors by
HCacheT
ype
Common Attack payloads
Vulnerable Websites*Internal
Route Header Attack
X-Request-Id: 123456789
wikia.com
Fastly-Client-Ip: 123456789
fandom.com
Gpt-Tags-Enabled: 123456789
ipage.com
X-Amz-Request-Id: 123456789
stanford.edu
Fastly-Soc-X-Request-Id: 123456789
domain.com
X-Amz-Website-Redirect-Location: 123456
marriott.comH
TTP Identication Header Attack
Auth-Key: 123456789
sinaimg.cn
X-Auth-User: 123456789
bing.com
Authorization:123456789
wsimg.com
X-Authorization: 123456789
zidavis.com
Client-Proxy-Auth-Required:123456789
ccmbg.comH
TTP If Header Attack
If-Match: 123456789
usa.gov
If-Range: 123456789
aig.com
If-None-Match: 123456789
bluehost.com
If-Modied-Since: 123456789
starbucks.comH
TTP Protocol Header Attack
X-Forwarded-SSL: on/o/nonsense
pcmag.com
X-Forwarded-Scheme: nothttps/http(s)
cisco.com
X-Forwarded-Proto: http(s)/ssl/nonsense
mashable.com
X-Forwarded-Protocol: http(s)/nothttps/nonsense getywheel.comH
TTP Range Header Attack
Range: bytes=cow
stats.com
Range: bytes=9-4
miele.co.nz
Range: bytes=-1024,0
starbucks.com
Range: bytes=0-,0-,0-,0-
chiltondiy.comH
TTP Upgrade Header Attack
Upgrade: 123456789
legaro.fr
Upgrade: HTTP/0.9
smtp2go.com
Upgrage: Websocket, RTA/x11
salesforce.com
Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9
disney.ioH
TTP Coding Header Attack
Accept: 123456789
fcc.gov
Accept-Encoding: 12345
house.gov
Transfer-Encoding: error
europa.eu
zTRANSFER-ENCODING: asdf
landmarkcinemas.com*: The vulnerable websites in the table only show the base domain. The subdomains and paths were redacted forethical considerations.T
able 2: Detection datasets and vulnerable websites statisticsInitial
domain name Domain name extension Cache pages Cache Poisoning VulnerabilitiesNumb
er of domain names
1,000
114,560
22,114
1,354
Number of URLs
-
1,417,004
51,596
1,556rankings and a large amount of web trac, as shown in Table 1
and Table 2. Besides, some websites may even have more thanone vulnerabilities. Once an attacker compromises these websitesthrough one of the identied WCP vulnerabilities, it will aect alarge number of global Internet end-users.We compare our detection results with existing studies in Table3 and Table 4. Compared with previous work, our study is moresystematic and comprehensive in terms of attack vector coverageand measurement scale, with many new attack methods and vul-nerabilities discovered. In total, 14 types of attack techniques arediscovered by
HCache, 7 of which are newly discovered vectors.Figure 6 shows the percentage of dierent attacks, from whichwe can nd that known attacks still account for more than halfof the websites found to have WCP vulnerabilities, indicating thatvarious vendors are still not in place to protect against knownWCP attacks. In addition to the known issues, we also found thatmany other new HTTP elds may lead to WCP. This suggests thatany non-cache key could potentially be at risk of WCP. Protectionagainst a single attack method is not enough to fully defend againstthe eects of WCP.Figure 7 presents the distribution of vulnerable websites with
respect to their Tranco ranks, exhibiting a fairly uniform. Thissuggests that Web Cache Poisoning is pervasive among the websites
in our dataset with no strong connection to their popularity ranking.Moreover, we tested the impact of WCP in HTTP/2, using thesame variant of the scanning test on websites deployed with HTTP/2.We found that all the vulnerabilities that existed in HTTP/1.1 stillexisted in HTTP/2. About 90% of the websites share caches between

--- page 40 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.mutation mechanism that assesses the impact of security scanners(e.g. Nuclei) and web crawlers (e.g. PyCurl) on the cache. Addition-ally, it tests the cache's resilience to malicious
`Referer'
messagesfrom phishing sites and common blacklist strings used by WAFs(e.g.
<script>alert(1)</script>).Step B.4) HTTP Request Body Mutation.
While GET requeststypically lack a body, some HTTP services process bodies in GETrequests, causing abnormal behaviors like redirects or 400 errorresponses. Additionally, rewriting methods like
`X-HTTP-Method-Override'
can extend the attack payload. When a cache server trans-
parently forwards such requests, and the web server responds withan exception consequently, it becomes susceptible to WCP.Step B.5) Other Illegal HTTP Request Mutation.
Beyond
mutating the three main components of the HTTP request, wecrafted other illegal HTTP requests to probe WCP vulnerabilities,examining the eects of overly long headers and invalid characters.Cache Buster.
To nalize the test requests for WCP, we em-ployed a
cache buster
with two objectives: on the one hand, mod-ifying the value of the
cache buster
avoids interactions betweentargeting the same URL and prevents invalidation caused by newattack requests hitting the previous cache. On the other hand, it en-sures that normal user requests do not trigger responses poisonedby our tests, as they do not carry our randomly generated
cachebuster.
4.4 Stage C. Cache Poisoning DetectionUnder this component,
HCache
rst initiates WCP detection foreach URL in the pending list, then analyzes the response to identifyvulnerabilities.
HCache
performs multiple rounds of WCP testingrapidly using multi-threading, encompassing request generation,response analysis, and cache poisoning validation.Step C.1) Detecting Request Generation.
This module is used
to generate three HTTP requests, which are normal request, attackrequest and validation request. The normal request is obtained byadding the request parameter A to the standard request generated in
Step B.1), which aims to check whether the cache buster is eective
and collect the normal response of the target website for subsequentanalysis. The attack request is obtained by adding the dierentrequest parameter B from the test cases generated in the previousstage. The validation request is similar to the normal request, theonly dierence is it has the same request parameter B as the attackrequest.Step C.2) Response Dierence Analysis.
HCache
identiespotential WCP by analyzing dierences between the response re-turned by a normal request and an attack request. It assesses threetypes of information: a) whether the status code of the HTTP re-sponse has changed; b) whether the length of the HTTP responsebody has changed; c) whether the HTTP response contains addi-tional content of the poisoning request compared with the normalrequest. If one of the above conditions occurs,
HCache
determinesthat the target server may be threatened by WCP.Step C.3) Poisoning Validation.
When
HCache
nds a website
that may have WCP vulnerabilities, it will use the validation requestto verify if the cache will be poisoned. This validation request is
sent within 1 second to verify that the WCP vulnerability can besuccessfully exploited. If the website is vulnerable, the validationresponse matches the last poisoned content, and the cache identityeld should display
HIT.False positives in the measurement process are caused by mul-tiple similar requests from the same client being rejected by theweb server. When both an attack request and a validation requestreturn the same error response,
HCache
mistakenly assumes thatthe error request was cached. In order to eliminate false positives,HCache
will initiate two subsequent tests of the potential WCP
vulnerability detected after a certain period. And all discoveredpotential vulnerabilities will be cross-validated on clients in dier-ent regions. Finally, we also manually veried the discovered WCPvulnerabilities.
5 MEASUREMENT STUDY AND FINDINGS
5.1 Data CollectionOur work use Tranco Top 1,000 domains as seeds, and extracts
a total of 114,560 subdomain information, among which 31,350
surviving websites can be accessed via HTTP(S). On this basis,
more resource is crawled on these websites by the crawler, thusexpanding the target domains to 4,427,590 dierent URL links. Toincrease the testing eciency, URLs with similar paths are de-emphasized during the experiment, and nally, 1,417,004 URL linksare obtained. Then, the websites that contain the cache identity
header in the HTTP response packet are selected as targets fortesting. A total of 22,114 domains containing 51,596 dierent URLlinks were tested in this chapter. Then we conducted detectionmeasurements from 7 dierent VPS servers across the world, suchas New York, Frankfurt, Sydney and Tokyo. For each detected case,multiple repeated experiments are conducted across dierent geo-locations to eliminate accidental false positives that may arise. Inthe end, more than 1,300 websites were found to have web cachepoisoning (WCP) vulnerabilities, containing 1,556 dierent URLlinks.
5.2 Cache Key DetectionTo prevent the poisoned cache from aecting normal users duringtesting, we use a cache buster to isolate the cache. The test requestmust carry a crafted cache key dierent from the normal user's
request, and the cache key used for the cache buster should be"irrelevant" and its modication must not aect the normal responsecontent. To this end, we designed a pre-experiment on cache keydetection to nd the best cache buster.We determine which elds are commonly used as cache keys bymodifying dierent parts of the HTTP request. From all the cachableURLs detected, URLs were randomly selected for each accessible
domain of the Tranco top 1,000. In most cases, if the parametercannot be recognised by the server, it will ignore without aectingthe corresponding content, indicating that the request parameter isa kind of eective cache buster. It will be used in the subsequent
large-scale cache poisoning measurement to avoid aecting thenormal user's access.
5.3 OverviewWe conducted large-scale WCP detection experiments on popularwebsites on the Internet, and found 1,354 WCP vulnerabilities,
aecting some world-famous websites, which have high Tranco

--- page 41 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Figure 5: Overview of our large-scale measurement system:HCachefuzzy matching and URL similarity calculation to consolidate simi-lar URLs.For example,
example.com/users/bob/blog1
and
example.com/users/alice/article2
may exhibit high similarity. Initially, we generalizethem based on letters (represented by C), numbers (represented byD), and special characters (represented by S):
example.com/CCCCC/CCC/CCCCD. Subsequently, we assign weights according to thehierarchical levels of the path, where higher-level directories havegreater weights. Next, we use a directory of dierent levels as
keywords to calculate feature vectors. We compute similarity byutilizing the Hamming distance between feature vectors, and URLswith excessively high similarity are deduplicated. In the end, thisprocess yields a set of URLs for testing, and ltering out URLs in thismanner signicantly reduces the testing workload. It also avoidsoverconsumption of the target server's resources with redundantscans.
4.3 Stage B. Test Case GenerationThe test case generation is the core module of
HCache
that outputs
dierent request variations to comprehensively cover dierent WCPmethods. It includes standard HTTP request generation, cache keydetection, and multiple request mutation methods.Step B.1) Standard HTTP Request Creation.
Informed byexpert insights and trac analysis, we've crafted standard HTTPrequest templates for common methods like HEAD, GET, and POST.These templates are designed to avoid rejection by mimicking nor-mal HTTP trac, including typical header elds like
`Host', `User-Agent', `Cookie', and
`Accept-Encoding', with the `Host' eld adapt-ing to the target domain automatically. This equips
HCache
with abasic suite of HTTP requests.Step B.2) HTTP Request Line Mutation.
The HTTP requestLine, comprising the
Method,
URI, and
Protocol Version, is often a
cache key, thus we explore the impact of dierent elds of non-cache keys, such as method case insensitivity, parameter changes,and protocol version arbitrarily specied variants. WCP can occurwhen a non-cache key eld aects content generation or causes
server errors. For parameter mutation, we collect a list of com-mon parameters, which
HCache
utilizes to mutate HTTP requestparameters.Step B.3) HTTP Request Headers Mutation.
The requestheader includes elds both from standard RFC specications andpopular web servers and CDN vendors. This complexity, coupledwith variations between middlebox and web server, often leads toinconsistencies and potential WCP vulnerabilities. It also bringsa great challenge to the detection of WCP: how to cover as manytypes of attacks as possible? To this end, we propose the followingvariants based on the characteristics of dierent headers.i.Request Headers Scanning
: Some elds in the HTTP requestheader may also aect the web server's execution logic. A commontrick is to utilize forwarding headers (e.g.,
`X-Forwarded-Host', `X-Forwarded-Scheme', `X-Forward-Port'
), which are often used to passinformation among multi-hop HTTP servers. WCP occurs whenthe cache server uses these elds for routing without adding themto the cache key. Similarly, web server that fetches cookie eldsto generate readback data dynamically is vulnerable. Meanwhile,numerous real-world headers may dynamically aect the cachingresults, and dierent CDN vendors have their customized headersfor access control. This method involves gathering common requestheaders on the Internet and systematically altering HTTP requestswith these headers to evaluate their eect on WCP.ii.Special Headers Scanning
: Certain HTTP request headers, asdened in RFCs, have specic value requirements, such as the
`If-Unmodied-Since'
header specifying a date format. Besides, webservers will format the header of a request, if a header's value does
not conform (e.g., a random string), it's disregarded by web servers,hindering WCP detection. To address this, we generate syntax-compliant values that adhere to RFC specications for testing.iii.Blacklist HTTP Request Mutation
: While WAFs block scannersor crawlers by common ltering mechanisms (eg. return
403 IllegalAccess Response
when detecting
`User-Agent'
as SQLMap), some
cache servers may not include
`User-Agent'
in the cache key, cre-ating an opportunity for WCP.
HCache
employs a blacklist-based

--- page 42 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.cache server forwards this request, triggering a malicious responsefrom the web server. Malicious responses could be an error page, aredirection to a 3rd-party website controlled by the attacker, or a
page containing malicious content. Finally, the cache server thencaches this evil response, and victim requests with the same cachekey hit the poisoned cache, leading to a WCP attack. While WCPhas posed a severe threat to the Internet, there is lack of systematicevaluation of such vulnerabilities at scale.
3.2 MethodologyIn this paper, we present a novel testing methodology to detect
WCP on the Internet. However, developing such a methodologyneeds to answer the following research questions.Q1: How can we generate testing requests to systematicallyprobe web cache poisoning vulnerabilities?Previous works [24,25,27] usually utilize manual approachesor collect known exploits to generate testing requests, and do notsystematically explore various HTTP elds and specic caching
behaviors. This can lead to incomplete testing and the potentialoversight of new attack vectors. To address this, we have developeda cache-key-aware approach to systematically generate and mu-tate HTTP requests to uncover WCP vulnerabilities. We start withstandardized HTTP requests to incorporate typical header elds by
leveraging syntax rules derived from HTTP RFCs. We then enumer-
ate dierent HTTP elds such as request line, headers, and body touncover those elds not included in cache keys. Then we mutatenon-cache-key elds and body of requests to probe inconsistenciesbetween web caches and web servers, aiming to uncover potentialexploits. This allows for a more targeted and systematic generationof test cases for essentially identifying potential WCP issues.
Q2: How can we detect Web Cache Poisoning accurately?We design a three-phase testing approach to detect WCP ac-
curately. First, we send a normal request to establish a baseline
response. This is followed by a especially crafted request, wherepotential vulnerabilities are systematically tested. The response tothis request is then compared to the baseline response, identifyingdiscrepancies that may indicate a successful poisoning attack. Fi-nally, a validation request is sent to conrm the initial assessmentof WCP vulnerability. This approach allows us to pinpoint the exact
conditions under which WCP can occur, providing a reliable meansof assessment.Q3: How can we assess the impact of WCP while minimiz-ing disruption to normal users?Minimizing the impact on normal users while assessing WCPis crucial. To achieve this, we employ
cache buster
variables in ourrequest parameters to isolate web caches. These variables, craftedas unique random values and cache keys, ensure that normal userrequests do not intersect with our crafted testing requests, therebypreventing access to potentially poisoned caches. This techniqueensures that our testing process does not disrupt the normal oper-ations of the website or the access of legitimate users, while stillmaintaining the high ecacy of WCP detection.
4 HCACHE: DESIGN AND IMPLEMENTATION
4.1 WorkowBased on the above methodology, we developed
HCache, a large-
scale detection system to detect web cache poisoning (WCP), de-picted in Figure 5.
HCache
comprises three core modules: the
Pre-processing Module, the
Test-case Generation Module, and the
Cache-poisoning Detection Module.(1) The
Preprocessing Module
processes the seed domain listthrough expansion, survivability checks, deduplication, and cacheableURL identication, outputting detectable URLs.(2) The
Test-case Generation Module
identies cache keys, pro-duces standard requests, and generates test cases for potential WCP.(3) The
Cache-poisoning Detection Module
synthesizes the priormodules' outputs to craft attack requests and assesses WCP vulner-abilities using varied attack payloads.The following paragraphs present detailed information on therelated working steps and specic modules.
4.2 Stage A. PreprocessingFirst, the list of URLs to be tested needs to be determined before thefollowing real-world measurement. Thus, the
Preprocessing Moduleincludes the initial three steps, including subdomain extension,target URL nding, and URL deduplication.Step A.1) Subdomain Extension.
Starting from initial domains,this process recursively crawls related HTTP/HTTPS pages togather subdomains with a 200 status code, thereby expanding thedomain list for further steps. Domains that do not return a 200status code are disregarded, as they are not typically accessed byweb clients. The next step then generates the initial set of URLs fortesting based on the collected subdomains.Step A.2) Target URL Finding.
This component is a websitecrawler that uncovers URL resources through deep traversal andautomates website visits using Python's Requests library. To en-
hance eciency for large-scale detection of popular websites, it
operates with multiple concurrent threads. In summary, the pro-gram sequentially crawls the target domain's homepage, extractingstatic resources such as JavaScript, images, and videos.Relevant studies indicate that using the HTTP header elds inthe response (e.g. 'age', 'x-cache') to determine whether a page iscached is a relatively accurate method[25]. Pages detected using
this approach form a true subset of all cached pages, as certainwebsites may omit cache-related information in their responses. Wereferenced ocial documentation from major caching vendors tounderstand the specic caching behavior of dierent cache identity
headers. Additionally, the crawler discovers numerous related URLs
on third-party websites, including OSS storage, JS hosting, and self-built CDN services, and automatically adds these domains into thedomain discovery list.Step A.3) URL Deduplication.
The deduplication module en-hances the eciency of large-scale cache-poisoning detection. Many
web applications generate customized pages based on query stringsor URL path parameters, leading to similar URL structures beingcached together with the same vulnerabilities. Exhaustive testingof each URL is time-consuming and resource-intensive. To avoid re-
dundant detection of similar URLs, obtained URL lists are processed.Utilizing the SimHash algorithm [31], we developed a program for

--- page 43 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache Poisoning in the Wild
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Figure 2: Process of web cache poisoningother users may hit the cache, resulting in access to maliciouscontent. Figure 2 shows the process of WCP: 1)The attacker sends acarefully crafted malicious HTTP request. 2)The cache server failsto lter the malicious request and forwards it to the web server.
3)The malicious request triggers an exception at the web server,
resulting in a harmful response that the cache server stores. 4)A
normal request initiated by the victim hits the cached maliciousresource.These two attacks have two main dierences. (1) The attack
techniques are dierent: WCD achieves its goal by constructing
abnormal URLs, it requires the victim to click on the malicious
URL to deceive the cache. WCP can exploit various parts of theHTTP request to poison the cache, directly resulting in the victimreceiving abnormal responses. (2) The attack objectives are dierent:WCD aims to steal sensitive information from the cache, whereas
WCP aims to make the victim access error responses in the cache.Researchers have conducted extensive measurement studies on
WCD [24,25]. However, there is currently a lack of large-scalemeasurements regarding WCP. This study focuses on the researchgap in the decit of a global WCP threat overview, by designingand implementing the
HCache
to study the severity on the Internet.WCP has the merit of a wide-range attacking impact with justa simple attack. Specically, attackers only need to send a singleattacking request, while aecting numerous global Internet users.The larger the trac of a website, the greater the impact it cancause. In the entire attack chain, WCP can be conducted in conjunc-tion with other attacking techniques to broaden the attack surface,and their nal impact closely depends on the injected malicious
payloads. If an error response is returned, it can lead to a Denialof Service (DoS) attack. If the response is dynamically generated,injection of JavaScript code can result in Cross-Site Scripting (XSS)attacks. If the location of redirect responses can be manipulated,
arbitrary page replacement can occur. In a word, when combin-
ing WCP with other attack methods, the severity can be furtherexpanded.
2.3 Limitation of Existing ResearchCurrent studies share a common limitation as they are all case-by-case investigations heavily reliant on empirical knowledge. Chen etal. proposed a new method for WCP by exploiting the Host header,termed "Host of Trouble" [1]. James Kettle introduced a novel tech-nique to execute such attacks using HTTP request elds, includingX-Forwarded-Host, request parameters, fat get request [16,17].Nguyen et al. proposed CPDoS, using three methods to conduct aDoS attack [28]. Mirheidari et al. conducted large-scale measure-ments on the impact of WCD on the Internet [24, 25].These studies have two main limitation: (1) They are case-by-case studies and do not systematically analyze the cache poisoningvectors that may result from dierent HTTP elds, which couldmiss many new attack vectors, as we demonstrate later; (2) Theylack large-scale measurements. Existing studies have either onlyconducted manual testing for CDNs and HTTP implementations, oronly conducted small-scale testing for certain attack types, leadingto many vulnerability instance undiscovered. Therefore, there is an
urgent need for a systematic tool capable of conducting large-scalemeasurements to identify WCP vulnerabilities.
3 OVERVIEW
3.1 Threat ModelEssentially, web cache poisoning (WCP) attacks stem from the prob-lem with
cache key. The cache key serves as the unique identierto locate and isolate cached objects, determining whether a requesthits the cache or not. Figure 3 presents an example of cache keysin HTTP requests. It typically consists of the request method, host-name, and URI. A cache hit occurs when a new request matches the
cache key of a previous stored object that still remains valid withinthe cache; if not, the resource is retrieved from the web server.Figure 3: A example schema for cache keys in HTTP request
Figure 4: An example of web cache poisoningFigure 4 presents a example of WCP, where an attacker con-
structs a malicious request with evil content in the headers. The

--- page 44 ---

CCS '24, October 1418, 2024, Salt Lake City, UT, USA
Yuejia Liang et al.we need to address three research questions: (1) How can we gen-erate testing requests that systematically probe cache poisoning
vulnerabilities? (2) How can we accurately detect potential webcache poisoning? (3) How can we assess the impact of web cachepoisoning while minimizing disruption to normal users?To address these questions, we introduce a novel testing method-ology,
HCache, designed to detect WCP vulnerabilities. For the
rst question, we employ a
cache-key-aware
approach that sys-
tematically generates and mutates requests to identify elds notincluded in cache keys, thereby exposing potential inconsistencies.For the second question, we utilize a three-step detection strategyinvolving the issuance of a normal request, an attack request, and a
validation request. This strategy allows us to analyze dierences inthe response's status code, content, and length to detect potentialWCP vulnerabilities. For the third question, we incorporate
cachebuster
variables in our request parameters, ensuring that our testingdoes not disrupt normal website operations while maintaining theecacy of our detection approach.We evaluated
HCache
against Tranco Top 1,000 domains in-
volving 22,114 subdomains with 51,596 distinct URL links. Ourevaluation discovers more than 1,000 websites across 172 domains,constituting 17% of the domains evaluated, are vulnerable to WCP.Moreover, we identify 7 new attack variants to trigger WCP, includ-ing HTTP protocol headers, scope requests, conditional requests,and so on. Meanwhile, we investigated the caching dierences be-tween HTTP/2 and HTTP/1.1 and found that the WCP problem isalso prevalent in HTTP/2. Therefore, WCP is still a serious prob-lem, and network operators and caching service providers shouldtake appropriate measures to solve this problem. To the best of ourknowledge, this study represents the rst systematic, large-scale
evaluation of WCP within a scientic framework. We reportedthe vulnerabilities to the aected websites and received acknowl-edgements from over 15 companies, including globally renownedones like Adobe, Alibaba, Huawei, and Microsoft. Additionally, wereceived bug bounties totalling over $1,000 from these entities.
In summary, we make the following contributions:
We introduced a novel testing methodology for large-scaleevaluation of websites for WCP on the Internet, along witha practical detection system named
HCache
1
.
We carried out a comprehensive analysis of the Tranco Top1,000 domains and their subdomains, discovering over 1,000websites across 172 domains vulnerable to WCP, indicatingthat 17% of measured domains are at risk.
We discovered 7 new attack vectors that can cause WCP at-tacks and found the WCP issues are still prevalent in HTTP/2.We have responsibly reported the vulnerabilities to the af-
fected websites and received acknowledgements and over$1,000 bug bounties from many companies such as Adobe,Alibaba, Huawei, and Microsoft.
2 BACKGROUND
2.1 Web CacheWeb cache reduces network trac and optimizes application per-formance by caching frequently used network resources. It can be
1
https://github.com/phantomnothingness/HCache
Figure 1: Process of web cache deceptioncategorized into private caching and shared proxy caching. Privatecaches are caching mechanisms within the web client itself (e.g., thebrowser cache[30]) and within the web server (e.g., the WordPressplugin cache[36]). Shared proxy caching mainly includes variousproxy servers and CDNs.The reports released by the three major CDN providers, Akamai,
Cloudare, and Fastly, indicate that a signicant amount of network
trac passes through caching proxy communication each year [34].A measurement study by Guo et al. [6] shows that among the top1,000 domains in the Alexa ranking list, 74% of websites utilize
CDN services for content distribution and network acceleration.Additionally, there are many independent caching proxies (such asSquid [32], Varnish [33]) and caching servers (such as Apache [10],Nginx [26]) distributed throughout the Internet, indicating that
web caching devices have become critical infrastructure for theInternet.Cache servers typically store static and commonly accessed re-sources like HTML, JS, CSS, images, and other media. Most webcaches, due to their shared nature, do not cache dynamic, person-
alized, or sensitive content. The HTTP/1.1 specication's Cache-Control header directs caching devices on handling responses,such as Cache-Control: no-store to prevent storage. Despite RFCmandates for adherence to these headers, some caching devices andCDNs oer options to bypass them. A prevalent caching strategyinvolves rules based on resource paths and extensions, like cachingonly JPG, ICO, CSS, or JS les.
2.2 Web Cache AttackAs an important infrastructure in the Internet, web cache requiresutmost security. There are primarily two attack vectors targetingcache servers based on their caching characteristics [25].Web Cache Deception (WCD)
is an attack that tricks the appli-
cation into storing sensitive content belonging to other users in thecache. Subsequently, the attacker retrieves this content from thecache. Figure 1 shows the process of WCD: 1)The attacker tricks thevictim into visiting a URL that requests
/account.php/nonexist.jpg.2)The request reaches the web server and ignore the non-existentpart of the URL. Web server send back a successful response withaccount.php, which has victim's private account. The web cachestore the response, interpreting it as a static image. 3)The attackervisits the same URL accessing the victim's information stored inthe cache.Web Cache Poisoning (WCP)
is to induce the application tostore malicious content in the cache. The normal requests from

--- page 45 ---

Internet's Invisible Enemy: Detecting and Measuring Web Cache
Poisoning in the Wild
Yuejia Liang
Tsinghua University
Beijing, China
liangyj21@tsinghua.org.cn
Jianjun Chen
Tsinghua University; Zhongguancun
Laboratory
Beijing, China
jianjun@tsinghua.edu.cn
Run Guo
Tsinghua University
Beijing, China
gr15@tsinghua.org.cn
Kaiwen Shen
Tsinghua University; Clouditera Inc
Beijing, China
kaiwenshen17@gmail.com
Hui Jiang
Tsinghua University; Baidu Inc
Beijing, China
jianghui01@baidu.com
Man Hou
Zhongguancun Laboratory
Beijing, China
houman@zgclab.edu.cn
Yue Yu
Beijing University of Posts and
Telecommunications
Beijing, China
yuyue_999@bupt.edu.cn
Haixin Duan
Tsinghua University; Quancheng
Laboratory
Beijing, China
duanhx@tsinghua.edu.cn
ABSTRACTWeb cache poisoning (WCP) has posed signicant threats to Internet
security by causing the cache server to deliver malicious responsesto innocent users. This results in widespread denial of access towebsite resources and potential injection of harmful payloads. How-ever, prior works on WCP vulnerability have been fragmented andconducted in a case-by-case form, lacking a systematic analysis
of the threat landscape. In this paper, we ll this research gap byconducting a systematic evaluation of WCP vulnerabilities at scale.We propose
HCache, a novel testing methodology to facilitates thewidespread identication of WCP vulnerabilities. We evaluatedour methodology against Tranco Top 1000 domains and their sub-domains, and found that over 1,000 websites across 172 domains,representing 17% of the evaluated domains, are vulnerable to WCP.In particular, we have identied 7 new attack vectors stemmingfrom previously unexplored caching headers. We have responsiblydisclosed the vulnerabilities to the aected websites and received ac-knowledgements and bug bounties from world-famous companies,such as Alibaba, Adobe, Huawei, and Microsoft.
CCS CONCEPTSˆ
Networks!Network measurement;
ˆ
Security and privacy!
Network security
;
Web application security
.
KEYWORDSNetwork Security, Measurement, Web Cache, Web Cache Poisoning
Corresponding author.This work is licensed under a Creative Commons AttributionInternational 4.0 License.
CCS '24, October 1418, 2024, Salt Lake City, UT, USA
©
2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0636-3/24/10
https://doi.org/10.1145/3658644.3690361
ACM Reference Format:Yuejia Liang, Jianjun Chen, Run Guo, Kaiwen Shen, Hui Jiang, Man Hou,Yue Yu, and Haixin Duan. 2024. Internet's Invisible Enemy: Detecting andMeasuring Web Cache Poisoning in the Wild. In
Proceedings of the 2024ACM SIGSAC Conference on Computer and Communications Security (CCS'24), October 1418, 2024, Salt Lake City, UT, USA.
ACM, New York, NY, USA,15 pages. https://doi.org/10.1145/3658644.3690361
1 INTRODUCTIONTo prevent unnecessary Internet trac and enhance data transmis-sion eciency, web caching facilities are extensively used. They
store frequently requested data resources, reducing the need for
repeated data transfers. Given web cache's advantages, it has be-
come a critical infrastructure component of the Internet. How-ever, when compromised by malicious actors, web caching facilitiespose signicant risks to the Internet. Research indicates that issueswith web caching can lead various security consequences, such asDenial-of-Service (DoS), Cross-site scripting (XSS), and informationleakage [4, 16, 17, 19, 28].Attacks against web cache typically fall into two categories, theweb cache deception (WCD)
and the
web cache poisoning (WCP)
[24,25]. WCD aim to deceive the cache into making condential in-
formation publicly available online, whereas WCP involve poi-soning the cache with harmful payloads that are then distributedto unsuspecting users. In recent years, Mirheidar et al. [24,25]
studied the severity of WCD by measuring Alexa Top websites,
demonstrating the widespread threats on the Internet. However,
due to the complexity, WCP have been studied in a case-by-case
form [4,16,17,19,24,28], focusing on revealing the specic vul-nerabilities while lacking a global Internet view of the severity. Asthe WCP poses a severe threat to the Internet, it is urgent to detectand prevent the vulnerabilities ahead of the attacker on the globalscale.In this paper, we aim to ll this gap by performing a system-atic detection of WCP vulnerabilities at scale. To achieve this goal,
