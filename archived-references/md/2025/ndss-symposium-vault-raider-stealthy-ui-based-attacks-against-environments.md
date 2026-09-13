---
type: Whitepaper
title: "Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments"
description: Conference paper explaining password-manager UI attacks and validation paths. Original source code was already public in August 2025; later conference measurements must not be used to date the original technical release.
resource: "https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf"
tags: [whitepaper, webseclist-reference, ndss-symposium, password-manager, autofill, identity, case-study, owasp-a07-2021]
generated:
  by: webseclist-refs/1
  at: "2026-09-13T22:21:11+00:00"
verified:
  - by: AI archive validation
    at: 2026-09-13
status: stable
stale_after: 2027-09-13
sources:
  - id: original
    resource: "https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf"
    title: "Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments"
    author: Andrea Infantino, Mir Masood Ali, Kostas Solomos, Jason Polakis
also_at: []
authors:
  - Andrea Infantino
  - Mir Masood Ali
  - Kostas Solomos
  - Jason Polakis
canonical_url: ""
cited_by:
  - "2025.md:120"
commit: ""
content_sha256: dc15e62e65248c41979a76cc0913588c64233e89e283083e32f796d3946f984b
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf"
published: ""
publisher: NDSS Symposium
publisher_english: ""
raw_sha256: 7e37ed3c8304e3d28fd4475638950ffb0d7cf826782a8fb986c915a8049b3e12
retrieved_from: "https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf"
retrieved_kind: live
retrieved_utc: "2026-09-13T22:21:11+00:00"
slug: ndss-symposium-vault-raider-stealthy-ui-based-attacks-against-environments
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments

**Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments** - Andrea Infantino, Mir Masood Ali, Kostas Solomos, Jason Polakis, NDSS Symposium.

- Published: date not stated
- Original: <https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf>
- Preserved from: https://www.ndss-symposium.org/wp-content/uploads/2026-s1067-paper.pdf (live) on 2026-09-13
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Vault Raider: Stealthy UI-based Attacks Against
      Password Managers in Desktop Environments
                          Andrea Infantino, Mir Masood Ali, Kostas Solomos, and Jason Polakis
                                                    University of Illinois Chicago
                                            {ainfan5, mali92, ksolom6, polakis}@uic.edu


   Abstract—Password managers significantly improve password-           face [9]. This includes users choosing weak or guessable
based authentication by generating strong and unique passwords,         passwords [10], [11], their inability to remember strong
while also streamlining the actual authentication process through       passwords [12], the impact of an ever-increasing number
autofill functionality. Crucially, autofill provides additional secu-
rity protections when employed within a traditional browsing            of accounts and passwords [13] which leads to password
environment, as it can trivially thwart phishing attacks due to         reuse across services [14], [15], and, finally, users’ inherent
the website’s domain information being readily available. With          susceptibility to phishing attacks [16], [17].
the increasing trend of major web services deploying standalone            At the heart of these issues lie the natural limitations of
native apps, password managers have also started offering               humans, which motivated the proposal of password managers
universal autofill and other user-friendly capabilities for desktop
environments. However, it is currently unknown how password             as a means to address the aforementioned shortcomings. Even
managers’ security protections operate in these environments. In        though their core functionality and goals remain unchanged,
this paper, we fill that gap by presenting the first systematic         password managers have evolved considerably compared to
empirical analysis of the autofill-related functionalities made         early academic proposals [18], [19], [20], with a particular
available by popular password managers (including 1Password             focus on improving usability concerns [21], [22], [23] that can
and LastPass) in major desktop environments (macOS, Windows,
Linux). We experimentally find that password managers adopt             hinder wider adoption. As a result, popular password manager
different strategies for interacting with desktop apps and employ       browser extensions have millions of downloads in Google
widely different levels of safeguards against UI-based attacks. For     Chrome’s Web Store. Apart from the ability to generate
instance, on macOS, we find that a high level of security can be        strong and unique passwords, these browser extensions also
achieved by leveraging OS-provided APIs and checks, while on            automatically fill out (i.e., autofill) user credentials in websites’
Windows we identify a lack of proper security checks mainly
due to OS limitations. In each scenario, we demonstrate proof-          account registration and log-in forms, thereby significantly
of-concept attacks that allow other apps to bypass the security         streamlining the authentication process. By verifying the vis-
checks in place and stealthily steal users’ credentials, one-time       ited website’s domain, which is made readily available by
passwords, and vault secret keys through unobservable simulated         browsers through the URL Web API [24], password managers
key presses. Accordingly, we propose a series of countermeasures        protect against phishing attacks. Importantly, certain password
that can mitigate our attacks. Due to the severity of our attacks,
we disclosed our findings and proposed countermeasures to the           managers also operate as authenticators for two-factor authen-
analyzed password manager vendors, which has kickstarted the            tication, further mitigating the effects of phishing or credential
remediation process for certain vendors and also been awarded a         stuffing attacks [25].
bug bounty. Finally, we will share our code to facilitate additional       While web browsers continue to mediate a significant por-
research towards fortifying password managers.                          tion of users’ online activities, many major web services have
                       I. I NTRODUCTION                                 started to offer standalone desktop apps as a means to improve
                                                                        the user experience (this can, at least partially, be attributed
   As the modern web revolves around predominantly dynamic
                                                                        to the declining performance of browsers due to bloat [26],
and personalized content, authentication remains an integral
                                                                        [27]). Accordingly, this migration from browsers to native apps
and critical aspect of users’ browsing experience [1], [2],
                                                                        has necessitated that password managers also pivot to desktop
[3], [4]. While passwordless authentication paradigms have
                                                                        ecosystems. Given the key importance of autofill functionality
emerged in recent years [5], [6], passwords remain the de
                                                                        and the paramount importance of usability, certain password
facto method for end-user authentication in many settings [7],
                                                                        managers have started offering universal autofill functionality,
[8]. Password-based authentication has been extensively an-
                                                                        wherein they will autofill users’ credentials in the login forms
alyzed in prior research spanning more than two decades,
                                                                        of non-browser applications. Despite autofill functionality
detailing their various shortcomings and the challenges users
                                                                        being conceptually straightforward, securely completing the
                                                                        autofill process outside of the sandboxed and isolated confines
                                                                        of a browser requires introducing new types of safeguards.
                                                                        Moreover, it is unknown what system-level features and APIs
                                                                        are made available across different operating systems that
Network and Distributed System Security (NDSS) Symposium 2026
23-27 February 2026, San Diego, CA, USA                                 could facilitate, or undermine, this process.
ISBN 979-8-9919276-8-0                                                     In this paper, we address this gap by offering the first,
https://dx.doi.org/10.14722/ndss.2026.231067
www.ndss-symposium.org
to the best of our knowledge, empirical security analysis of                  managers for safeguarding autofill-related functionality.
password managers for native desktop application environ-                   • We demonstrate novel attacks that exploit password
ments. Specifically, we focus on autofill and other functionality             managers’ functionality and manipulate UI features for
features that aim to obviate the friction that can arise during the           stealthily exfiltrating secrets from their vaults.
authentication process. To that end, we first explore the various           • We propose countermeasures that can be incorporated by
user-friendly features offered by popular managers across dif-                password managers for effectively mitigating our attacks.
ferent platforms. Subsequently, we analyze popular password                 • We have responsibly disclosed our findings to the af-
managers in-depth and uncover what mechanisms are in place                    fected vendors to kickstart remediation efforts. To enable
for preventing applications from exploiting their autofill func-              additional research on password manager security, our
tionality for credential-stealing attacks. We also explore what,              source code and attack demonstrations are available on
if any, OS-level APIs and features are leveraged as part of                   our artifacts page [28].
their security posture. Our analysis uncovers a tale of extreme
divergence in terms of safeguards employed by password                              II. BACKGROUND AND T HREAT M ODEL
managers within the same operating system, as well as for the                Here we provide background information on password man-
same password managers across different operating systems.                ager features and functionality, and detail our threat model.
Indicatively, we find that 1Password on macOS employs a                      Form Autofill Functionality. Autofill functionality is a core
series of countermeasures against phishing apps, including de-            feature in modern web browsers, designed to store and auto-
tecting multiple active processes with the same Bundle ID,                matically populate data such as login credentials, addresses,
mapping applications to trusted Associated Domains,                       payment details, and other frequently used information in web
and verifying apps through macOS’ Code Signing APIs.                      forms [29]. When users input data into form fields, browsers
In contrast, 1Password for Windows does not employ com-                   typically prompt them to save this information for subsequent
parable security checks due to the lack of corresponding OS-              use. Once stored, the autofill mechanism identifies matching
level mechanisms, highlighting the challenge of implementing              fields across different web pages and retrieves the corre-
autofill when faced with insufficient platform support.                   sponding data to streamline form completion. This browser
   Guided by our findings, we demonstrate novel attacks that              functionality is integrated across devices, enabling consistent
exploit the functionality offered by desktop password man-                user experiences. Sensitive data, including login credentials,
agers for exfiltrating users’ data, including their credentials,          is stored locally within the browser and can be synchronized
2FA codes, and vault secret key. For less secure password                 with cloud services [30], [31], [32].
managers (e.g., Keeper), the attacks can be as simple as spoof-              The autofill process operates by identifying and interpret-
ing the target application’s Bundle ID, while in more secure              ing form field elements through the analysis of visible and
apps (e.g., 1Password), we use synthetic keyboard clicks for              hidden attributes, such as usernames and passwords, and
leveraging the password manager’s Quick Access functionality.             associating them with previously stored credentials. Detection
We then detail how a series of system-specific UI-related                 mechanisms adapt to variations in web forms by analyzing
features can be leveraged by malicious applications for hiding            structural features and semantic markers (e.g., the HTML5 aut-
the password manager functionalities that they trigger from               ofill attribute) [33]. These mechanisms also handle additional
users, thereby rendering our attacks stealthy. Interestingly,             obfuscated or dynamically generated fields to support more
we find that macOS and Windows support multiple window                    advanced web structures. Once fields are classified, the system
manipulation techniques that allow for fully stealthy attacks             selects the best-matching stored data for automatic completion.
without visual artifacts. To make matters worse, we also                     Password Managers. Password managers are available
demonstrate that our attacks enable local privilege escalation            both as integrated browser features and as standalone ap-
by harvesting system passwords, and allow an attacker to                  plications for desktop and mobile platforms. Browser-based
replicate a user’s vault on a separate device by extracting               password managers focus on credential autofill while offering
the secret key. Guided by our attack techniques, we propose               additional features such as password generation, secure stor-
mitigations that would allow password managers to detect our              age, and password strength analysis, for enhancing account
attacks and avoid exposing users’ data. Due to the critical               protection [34]. In addition to their browser-focused im-
role of password managers and the severe implications of our              plementations,password managers also operate as standalone
attacks, we have already disclosed our findings and proposed              desktop applications, integrating into native environments.
mitigations to the respective vendors. Certain vendors have               These applications, such as 1Password [35], LastPass [36],
acknowledged the severity of our attacks and have initiated               and Keeper [37], provide cross-platform synchronization, en-
remediation efforts to mitigate the underlying weaknesses that            abling users to securely access their data across multiple
could significantly impact their user bases.                              devices. Password managers also support the management
   In summary, our research contributions are:                            and secure storage of a wide range of sensitive information,
   • We present the first in-depth empirical analysis of                  including credit card information, one-time passwords (OTPs),
      password manager functionality in desktop application               and identity information, ensuring comprehensive protection
      ecosystems. We also explore what mechanisms are ex-                 and accessibility. Given the sensitivity of the information
      posed by operating systems and adopted by password                  they manage, password managers implement robust security



                                                                      2
measures, including master passwords and two-factor au-                      TABLE I: Summary of analyzed password managers.
thentication (2FA) [38]. User authentication is required to              Password Manager       Version           OS                    Popularity
access encrypted data, with advanced tools employing zero-                                                        !      "
knowledge encryption, ensuring that even service providers               1Password              8.10.48     ✁      ✁      "
                                                                                                                          !        >15M users [53]
cannot access stored information [39].                                   Keeper                 16.10.13    ✁      ✁     N/A     >1M paying users [54]
   Threat Model. Our research focuses on the operation of                LastPass               4.14.1.0   N/A     ✁     N/A       >33M users [55]
                                                                         KeePassXC                2.7.9     ✁      ✁      ✁     >691K Linux installs [56]
standalone password managers that offer autofill functionality           MacPass                  0.8.1     ✁     N/A    N/A    >6.8K GitHub stars [57]
outside of the confines of web browsers. As such, we adopt               ! indicates partial support, where a password manager is available on the operating
                                                                         "
the typical threat model used in security studies that focus on         system but lacks full feature compatibility.
native app ecosystems (i.e., non-browser environments). We
assume that the user has installed a malicious application —
the specific propagation method is outside the scope of our             as a common utility. Once active, it targets specific password
study. Malicious or invasive software is a common occurrence            managers and exfiltrates stored credentials (usernames and
in desktop environments, including macOS despite the wide               passwords), banking information, one-time passwords, and
misconceptions that exist about its purported immunity to               vault secret keys (if applicable). Our malicious application
malware [40]. In practice, attackers can achieve this through           prototype operates entirely at the user-level space, without
straightforward social engineering attacks, or more advanced            exploiting kernel-level vulnerabilities or requiring special ad-
attacks that pass Apple’s app vetting process [41], or a man-in-        ministrative privileges (beyond the Accessibility permission
the-middle attack against Apple’s Wireless Direct Link [42].            in macOS). Our attacks exploit design flaws in password
It is important to note that macOS’s default app protection             managers’ autofill-related functionality and UI-related features
mechanism, Gatekeeper, does not prevent users from installing           for extracting sensitive data in a stealthy manner. We em-
malware. Instead, it primarily serves as a warning system,              phasize that the attack does not rely on zero-day exploits or
verifying that downloaded apps are signed by an identified              implementation bugs, but instead leverages existing function-
developer and notarized by Apple [43]. Notarization is a one-           ality intended for users. Through variations across different
time verification process that does not provide continuous              password managers and OSes, our research demonstrates an
monitoring, allowing apps to introduce malicious behavior               advanced threat that exploits vulnerabilities in the handling of
post-installation. In practice, while Gatekeeper can issue warn-        UI elements and synthetic user events. By manipulating these
ings for unsigned or unnotarized applications, signed malicious         components, the attacker bypasses existing security checks and
software continues to be distributed and executed [44], [45],           tricks the password managers into exposing sensitive data.
[40]. Recent macOS malware campaigns have, in fact, explic-
                                                                                              III. E XPERIMENTAL S ETUP
itly leveraged signed binaries to evade Gatekeeper’s protec-
tions [46]. Moreover, users can override system protections                Selecting and Configuring Password Managers. We
to install unverified applications [47], [48], [49]—a common            selected password managers based on two criteria: (i) the
practice for software distributed outside the App Store.                presence of autofill functionality in native applications and
   Prerequisites. For simplicity, in our analysis we assume that        (ii) broad platform support. While password managers pro-
the user’s password manager application is running, which               vide autofill capabilities in web browsers—typically through
is a reasonable assumption as these applications are often              browser extensions—fewer have implemented this feature for
left open in the background for convenience. Nonetheless,               native applications. Since our study focuses on attacks target-
malicious apps can leverage system-level APIs (e.g., ps on              ing autofill functionality beyond the browser, we prioritized
macOS or tasklist on Windows) to monitor active pro-                    password managers that explicitly support autofill in native
cesses and launch the attack only after confirming that the             applications. Table I summarizes the key characteristics of the
password manager is running, thereby reducing the risk of               evaluated password managers, including their supported plat-
detection. Moreover, on macOS, we assume that the mali-                 forms and popularity. Notably, a subset of password managers
cious app obtains the Accessibility permission during                   offer full cross-platform support, while others, like MacPass,
installation, a typical permission required by a wide range             are restricted to specific operating systems.
of legitimate software, including screen recording and remote              Attack Workflow. Our credential harvesting attack is exe-
control applications [50]. Notably, permission requests and             cuted through a custom phishing application that performs the
UI automation have been leveraged in real-world malware                 required steps to exfiltrate credentials. The attack proceeds
campaigns to perform tasks such as simulated input events and           through the following stages: (i) Upon launch, the application
data exfiltration [51], [52]. In our attack, Accessibility access       renders its interface and embeds input components for creden-
is incorporated into the broader workflow that ultimately               tial capture, such as hidden form fields. (ii) To impersonate a
exploits password managers’ autofill behavior. We further               trusted application and bypass verification checks, it modifies
discuss our assumptions’ practicality in §IV and how to relax           identity attributes such as the window title, bundle metadata,
our propagation vector assumptions in §VIII.                            or display name. (iii) It generates synthetic keyboard inputs
   Malicious application. The application appears to be legit-          to trigger the password manager’s autofill or credential access
imate and can be bundled with popular software or disguised             components (e.g., Quick Access). (iv) Once verification suc-



                                                                    3
TABLE II: Overview of our attacks across different password managers and platforms. Credential Types indicates the categories
of sensitive data that can be harvested: usernames, passwords, one-time passwords (OTPs), and credit card information.
Permissions indicates whether the attack requires additional OS-level permissions (✁) or not (✂) for the respective platform;
N/A denotes that the password manager is not supported on that platform. Stealthiness denotes whether the attack is fully
stealthy (#), partially stealthy (!
                                  "), or not stealthy (✂) on each OS. Performance reports the time required to harvest a pair of
credentials under the primary attack variant on macOS, where applicable.
         Password Manager                Credential Types                       Permissions           Stealthiness       Performance
                              Username    Password    OTP    CC Info               !         "          !          "
         1Password               ✁           ✁         ✁        ✁           ✁       ✂      ✂       !      !       ✂          11s
         Keeper                  ✁           ✁         ✁        ✁           ✁       ✂     N/A      "
                                                                                                   #      !      N/A          4s
         LastPass                ✁           ✁         ✁        ✁          N/A      ✂     N/A     N/A     !      N/A          5s
         KeePassXC               ✁           ✁         ✁        ✂           ✁       ✂      ✂       !      !       ✂          17s
         MacPass                 ✁           ✁         ✁        ✂           ✁      N/A    N/A      !     N/A     N/A          5s
         macOS Keychain          ✁           ✁         ✂        ✂           ✂      N/A    N/A     N/A    N/A     N/A         N/A



ceeds, the password manager either injects credentials directly          §IV-B, §IV-C, and §IV-D, we extend our analysis and intro-
into the phishing application’s hidden fields or displays the            duce variations of the attack across other password managers,
vault contents for selection. The phishing application then              highlighting commonalities and differences in their verification
simulates interactions to extract the displayed credentials and          mechanisms. We focus our presentation on 1Password for the
transfer them into its own interface for exfiltration (e.g., copy-       following reasons: (i) it is one of the most popular password
paste actions). (v) To maintain stealthiness, the application            managers, (ii) it is highly recommended (e.g., The New York
overlays distracting content (e.g., a video player) and lever-           Times has recommended it multiple times as the best password
ages window layering attributes to remain in the foreground              manager [60], [61]), and (iii) it incorporates the most OS-
and/or hide password manager windows. The methodology is                 specific safeguards, thereby providing a prime example of the
consistent across password managers; differences arise from              level of security that can be achieved in macOS.
OS-level constraints or manager-specific behavior.                          macOS Features and Security Mechanisms. Autofill
   Testing Environment. We created test accounts with each               functionality in standalone password managers introduces
password manager to ensure that no real user data was at                 additional security challenges not present in their typical
risk. All evaluated password managers supported keyboard                 browser-based usage, where credentials are filled within a
shortcuts to trigger autofill by default, except KeePassXC,              well-structured and sandboxed environment. Here we outline
which disables this feature by default; for consistency, we              structural and security-relevant aspects of macOS applications
enabled autofill for our tests. Prior to each experiment, we             that are pertinent to our threat model.
ensured the password managers were running, unlocked, and                   App Components. macOS apps are built upon a structured
populated with fake credentials associated with real services.           packaging system and robust security mechanisms, designed to
We deployed our malicious application using the Electron                 ensure their integrity, usability, and interaction with the operat-
framework and its window management capabilities [58], en-               ing system. Specifically, they are distributed as bundles—self-
abling consistent cross-platform deployment. To simulate user            contained directories that include executable code, resources,
interactions and trigger autofill mechanisms, we integrated the          and metadata required for the app’s functionality. A funda-
RobotJS library [59]. All experiments were conducted locally             mental component of the bundle is the Information Property
on macOS (MacBook Pro, M3, Sonoma 14.6.1), Windows                       List (Info.plist), a configuration file that stores essential
(Galaxy Book Pro 360, Windows 11 Home), and Linux (HP                    app information [62]. It specifies the version number, sup-
15-bw0xx, Ubuntu 22.04.5 LTS).                                           ported architectures, localization settings, and entitlements for
   Overview. Table II summarizes our attacks, detailing the              accessing system resources.
targeted OSes, required privileges, stealthiness, and perfor-
                                                                            Each app includes a unique Bundle ID [63], which the
mance for the primary attack variant (e.g., email-password
                                                                         OS uses to manage app identity, enforce permissions, and
credentials). For password managers available in multiple
                                                                         isolate inter-application interactions. Similarly, the Bundle
OSes, we report the performance on macOS. In the following
                                                                         Display Name serves as the primary label that users rely
sections, we discuss each scenario in detail, highlighting any
                                                                         on to interact with apps in the system’s interface, such as
unique features employed by each password manager, as well
                                                                         the Finder, ensuring accurate app identification. macOS also
as the intricacies of our attack in each scenario.
                                                                         enforces a robust security model to ensure the integrity and
                                                                         authenticity of apps. Another key component is code signing,
            IV. MAC OS PASSWORD M ANAGERS
                                                                         a process that allows developers to cryptographically sign their
  Here, we analyze the autofill functionalities of macOS                 apps [64], [65]. This mechanism verifies app integrity and
password managers. In §IV-A, we demonstrate our analysis                 authenticity, ensuring it has not been modified by other apps,
of 1Password to achieve effective credential harvesting. In              malware, or during distribution.



                                                                     4
   Permissions. The Accessibility API serves as a foundational
component that enables apps to support assistive technolo-
gies [66]. It allows developers to programmatically test and
enhance app usability by simulating interactions, identifying
missing accessibility labels, and optimizing layouts. Access to
the Accessibility API requires explicit user approval, managed
through macOS privacy settings, where users must explicitly
                                                                                       Fig. 1: 1Password’s Quick Access window.
grant the permission for the API to become available.
   Credential Autofill Mechanisms. Across evaluated pass-
word managers, we identify two primary credential mech-                  access and credential exfiltration, 1Password incorporates pro-
anisms: Autofill and AutoType. Autofill populates UI                     tections against malicious applications that attempt to exploit
fields directly by leveraging Accessibility API and interacts            its autofill functionality. These protections align with the types
with input elements based on their context (e.g., email) [67]. In        of attacks outlined in our threat model, further emphasizing
contrast, AutoType emulates user-triggered keystrokes for aut-           the realistic threat that such attacks pose to users. Due to the
ofill, without programmatic interaction or field validation [68],        proprietary closed-source nature of the 1Password application,
[69]. In our evaluation, we determine the adopted mechanism              we conduct an empirical black-box analysis to identify its
for each password manager and exploit it accordingly.                    internal security mechanisms and verification processes.
   Attack Vectors. As macOS enforces stricter authentication                Application Verification. 1Password associates credential
and verification models, it provides a representative platform           records with applications based on their Bundle ID, each app’s
for evaluating attack feasibility under robust OS-level con-             unique identifier, and this mapping ensures that credentials are
straints. We focus our analysis on macOS to demonstrate                  only autofilled into the intended app. However, our analysis
that password managers are vulnerable to credential-harvesting           reveals that Bundle IDs are not a reliable indicator of appli-
attacks, despite operating within environments that adopt                cation integrity, as they can be tampered with by modifying
advanced platform-level defenses. Specifically, our analysis             an app’s Info.plist file or spoofed by changing another
reveals inconsistencies in autofill validation that allow attack-        app’s Bundle ID to match that of a legitimate application. We
ers to bypass verification mechanisms and extract credentials.           experimentally found that 1Password rejects autofill when con-
Our attacks exploit three primary flaws: (i) manipulation of             flicting Bundle IDs are detected. Additionally, we confirmed
application identification (e.g., spoofed Bundle IDs), (ii) ex-          the specific conditions enforced by its verification mechanism.
ploitation of UI interactions, and (iii) abuse of system-level           Based on our experimental insights, we have reconstructed the
configurations (e.g., window layering). By leveraging these              autofill verification workflow employed by 1Password, which
techniques, an attacker can systematically and stealthily har-           we summarize in Algorithm 1.
vest credentials from multiple password managers. We note
here that all variations of our attack leverage the macOS                    Algorithm 1: 1Password Autofill Workflow on macOS
                                                                            Input: A: Target Application, BID: Bundle ID
Accessibility permission to programmatically interact with the           1  if No records linked to BID then
password manager and automate the credential harvesting.                  2      Select a record to link
   Given that legitimate applications request Accessibility per-         3    if Multiple active apps are linked to BID then
                                                                          4        Abort autofill
missions, we consider this assumption to be realistic. Specifi-
                                                                         5    if A is devoid of Code Signature then
cally, our analysis of 100 of the most popular free apps from             6        Abort autofill
the macOS App Store revealed that approximately 20% request              7  Link the selected record with BID if not yet linked
this permission, which suggests that users are accustomed to             8  if A’s Code Signature is untrusted or invalid then
                                                                          9      Abort autofill
often granting this permission to apps they install. Moreover,
                                                                         10 DevID → Apple Developer ID associated with Code Signature
prior studies in different domains (e.g., Android) have assumed          11 if DevID ↑ Verified Developers then
or explored the presence of malicious applications with the              12      if BID ↑/ Verified Bundle IDs for DevID then
                                                                         13           Abort autofill
Accessibility permission [70], [71], [72], [73] or reported its
use by malware in the wild [52].                                         14   else if BID ↑ Existing Developer ID — Bundle ID associations then
                                                                         15         Abort autofill
A. 1Password                                                             16   Perform autofill

   We focus our initial analysis on uncovering potential secu-
rity and verification flaws that would allow effective credential           The process begins by identifying the currently running
harvesting attacks against 1Password.                                    application and extracting its Bundle ID – if no records are
   Autofill Verification. The autofill mechanism provided by             linked, the user is prompted to select a record for future autofill
1Password is activated through dedicated keyboard short-                 actions. 1Password also performs checks to detect whether
cuts [74], enabling users to launch a search interface known             multiple running applications are sharing the same Bundle ID.
as the Quick Access Window (Figure 1). This interface offers             If such a conflict is detected, the autofill process is aborted
a list of stored credentials that users can select for autofilling       and the ID is flagged as potentially spoofed. Subsequently,
into the corresponding application. To mitigate unauthorized             1Password verifies the application’s code signature by access-



                                                                     5
ing the designated folder in its contents. If the application is        signed to remain in the foreground, appearing above all other
not digitally signed, the autofill process is aborted. Otherwise,       active windows to ensure that it remains accessible and visible
it checks the code signature to ensure it is both (a) valid,            to the user. However, macOS allows developers to assign
confirming that the code has not been tampered with, and                different window levels to control the visibility and layering
(b) trusted, indicating that it is signed by a verified                 of app windows [75], [76]. By default, windows are assigned
Apple Developer. In the final step, 1Password checks the                the normal level, but 1Password elevates the Quick Access
Apple Developer ID associated with the code signature, and              window to the pop-up-menu level. Our attack exploits this
ensures that the Bundle ID matches a verified list of IDs               capability by elevating the attacker’s window to the screen-
for that developer. For popular applications (e.g., Discord,            saver level, to conceal the Quick Access interface from the
Slack), 1Password maintains a list of known Developer IDs               user while harvesting credentials in the background.
to manage verification effectively. When encountering a new                Hidden Text Fields. Hidden text fields are HTML in-
unrecognized Bundle ID, it treats the first valid and trusted           put elements with their visibility intentionally concealed
signature as legitimate and prompts the user to confirm the             from the user interface, typically through CSS rules
association. Once this verification is complete, future autofill        (e.g., display:none). Although not visible to users, these
requests from the same Developer ID are processed without               fields remain accessible to scripts, allowing applications to
additional prompts. When all checks are successfully passed,            access, store, and transmit data. As such, attackers can leverage
1Password proceeds with the autofill operation. The multitude           them to exfiltrate credentials within an application, without
of safeguards in place strongly suggest that local deceptive            users being made suspicious or alerted [77].
apps are a valid concern for desktop password managers, and                Attack execution. To assess the practical implications of
also reveal the numerous macOS features that can be leveraged           1Password’s security flaws, we developed a proof-of-concept
to enhance their robustness.                                            phishing application that systematically extracts stored cre-
   User Confirmation. The first time a user attempts to autofill        dentials while evading detection, by combining all of our
credentials into an app, 1Password displays an alert window             aforementioned findings. The attack targets the Quick Access
prompting the user to confirm the action (see Figure 3 in               feature, leveraging window management inconsistencies, syn-
the Appendix). Upon confirmation, 1Password establishes an              thetic user interactions, and distraction techniques to stealthily
association between the credentials and the app, blocking any           exfiltrate credentials. The application automates the triggering
future attempts to modify this existing association.                    of Quick Access, bypassing user interaction requirements by
   Experimental findings. Here, we detail a series of em-               simulating keyboard input events. Once activated, it retrieves
pirical experimental findings, which constitute the individual          credential records by programmatically searching stored en-
“ingredients” that will then be combined into our proof-of-             tries and extracting usernames, passwords, and two-factor
concept attack. While 1Password conducts multiple verifica-             authentication (TOTP) tokens. Unlike default autofill, Quick
tion checks before performing an autofill operation, we have            Access does not validate the requesting application, allowing
identified omissions in their verification process. Accordingly,        credentials to be retrieved without enforcing application verifi-
we have developed an automated phishing application exploit-            cation. To conceal the exfiltration process, the attack exploits
ing those weaknesses, specifically in the Quick Access feature.         window layering mechanisms, by dynamically elevating the
   Application Validation. In 1Password’s primary autofill              attacker’s window above the Quick Access interface, it ensures
workflow, the password manager verifies the identity of the             that credential retrieval remains hidden from the user. Addi-
target application before injecting credentials, establishing a         tionally, the extracted credentials are stored in the phishing
binding between the credential item and its intended des-               application’s hidden input fields, not visible by the user. After
tination. In contrast, the Quick Access interface does not              credential exfiltration, the application restores its window to
perform application-level validation; it does not verify whether        the default window level to minimize post-execution traces.
the application receiving the credentials matches the expected          This harvesting approach can be extended to exfiltrate stored
origin (e.g., bundle identifier). This omission allows any local        payment information from the vault. The phishing application
application to retrieve stored credentials without triggering           enumerates vault entries and accesses items labeled with
user alerts or verification prompts. The absence of target              payment-related keywords (e.g., Visa, Card). Autofill proceeds
validation in this component weakens the security guarantees            if the target window includes the expected form fields (e.g.,
provided by the primary autofill mechanism.                             card number, expiration date). However, the availability of
   Interaction Origin. 1Password does not differentiate be-             sensitive fields depends on the user’s stored data and settings
tween physical and synthetic keyboard inputs. This allows an            (e.g., CVV autofill requires explicitly storing it [78]). Once
attacker to programmatically simulate user interactions, such           populated, payment information becomes accessible to the
as key presses, to trigger the Quick Access window and access           attacker. Finally, to enhance stealthiness, the application intro-
stored credentials. The attack leverages crafted interactions           duces obfuscation mechanisms during execution, and overlays
with the 1Password vault and automatically harvests creden-             distraction content, such as a video player UI, to divert user
tials without additional user input, thereby bypassing Quick            attention. This mechanism can be further augmented with
Access’s built-in security measures.                                    additional realistic content, such as a simulated software in-
   Window management. The Quick Access window is de-                    stallation or documentation text, to maintain user engagement.



                                                                    6
   Attack Performance. To evaluate the performance of our                1Password with system credential records under different
attack, we populated 1Password with five credential records              configurations. In ten iterations targeting five different user
corresponding to different services and conducted 10 itera-              profiles, the attack required an average of 6 seconds to locate
tions targeting different sets each time. On average, creden-            and extract system credentials. The attack was highly accurate
tial extraction requires 11 seconds per username-password                in detecting the default naming conventions and the associated
pair. We further extend our evaluation to include two-factor             credentials. This highlights the practicality and stealthiness of
authentication (2FA) codes, by populating 1Password with                 the attack, allowing the attacker to escalate privileges once
three records containing Time-Based One-Time Passwords                   they gain access to the system’s credentials.
(TOTPs). We then measured the time required to harvest                      1Password Command Line Interface. A key feature
a record comprising a username, password, and TOTP. Our                  of 1Password is its Command Line Interface (CLI) tool,
results show that harvesting a TOTP adds approximately four              accessible through the op command, which allows users
seconds to the attack execution, resulting in a total time of            to interact with their vault directly from the terminal [80].
15 seconds for extracting a complete credential record. Since            Primarily designed to automate vault operations and manage
TOTPs typically remain valid for at least 30 seconds [79],               credentials programmatically, the CLI tool provides flexibility
attackers have sufficient time to leverage the stolen credentials        for advanced users but can also introduce new security risks
before expiration. Overall, our evaluation demonstrates that the         if improperly secured. Our analysis revealed major flaws in
proposed attack is practical, highly stealthy, and effective at          the 1Password CLI tool that can be exploited to extract
harvesting credentials from 1Password.                                   sensitive credentials, including the Secret Key — a critical
   Credential Binding Flaw. We identified an additional design           component required to decrypt the vault. Unlike standard
flaw in 1Password’s credential association logic that enables            credentials, the Secret Key is not transmitted to 1Password’s
a denial-of-service attack that affects legitimate applications.         servers and must be used alongside the master password
Although this issue does not allow credential harvesting, it can         to unlock the vault [81]. If both the master password and
prevent users from accessing their vault. We describe this flaw          Secret Key are compromised, an attacker can authenticate on
in detail in Appendix C.                                                 a different device, gaining full access to the user’s 1Password
   Privilege Escalation: Harvesting System Password.                     account and resulting in a total compromise of the user’s data.
1Password supports storing system credentials, which enables                Authorization Bypass. When a process triggers the 1Pass-
users to autofill directly into terminal apps, such as the default       word CLI tool for the first time, a pop-up window is shown
Terminal. In 1Password, system credentials are saved as                  to confirm access to the vault. However, this authorization
standard vault entries and are assigned a record name based              pop-up inherits the same flaws as the Quick Access window.
on the device’s name by default. This naming convention                  Specifically, it is assigned the pop-up-menu window level,
introduces a security risk since attackers can predict record            allowing it to be hidden by higher-level windows. Critically,
names and directly locate system credentials in the vault.               it does not differentiate between physical and synthetic user
For example, a user named “Alice” using a MacBook Pro                    interactions, allowing an attacker to programmatically simulate
would have their system password saved under a record named              user inputs and approve CLI access without the user’s consent.
Alice’s MacBook Pro. Since device names often contain                    By exploiting this flaw, an attacker can stealthily enable CLI
personally identifiable information, including usernames, this           functionality and gain persistent access to the vault.
feature significantly reduces the effort required for an attacker           Default User Records. Once authorized, the CLI provides
to identify and extract system credentials.                              access to the vault, including a record named 1Password
   Attack Evaluation. This attack is a variation of the pre-             Account, which is automatically created during account
viously introduced credential-harvesting attack and relies on            setup. This record stores both the master password and the
the same configuration and permissions. The attacker appli-              Secret Key, retrieved in plaintext upon access. While 1Pass-
cation first retrieves the system’s device name and logged-              word enforces restrictions on retrieving the Secret Key through
in user information using standard macOS APIs, such as                   the Quick Access window, these restrictions do not extend
scutil --get ComputerName and whoami. Using this                         to the CLI tool, which allows programmatic extraction of
information, it constructs the expected system credential                the Secret Key through command-line queries. The ability
record name. Subsequently, it queries the 1Password vault                to extract the Secret Key has severe implications for the
through the Quick Access feature and searches for records                user, as it allows an attacker to recreate the user’s vault
matching the device name. Since the naming scheme is                     on a separate device and completely decrypt its contents by
predictable, the attacker can directly identify system creden-           bypassing 1Password’s authorization mechanisms. Essentially,
tials without the need for exhaustive searching. After locat-            this enables full account impersonation, bypasses recovery
ing the system credential record, the attacker executes the              protections, and grants persistent access—even if the master
aforementioned credential exfiltration technique. With access            password is changed.
to the system password, the attacker can execute privileged                 Attack Execution & Evaluation. To exploit these vulner-
commands using sudo, and disable system security features,               abilities, an attack begins by executing the op command
modify configurations, or install persistence mechanisms.                to trigger the CLI authorization prompt. Since the prompt
   To further assess the attack’s performance, we populated              is not protected against synthetic interactions, the attacker



                                                                     7
programmatically approves the request without requiring user
intervention. After authorization is granted, the attack retrieves
the record ID associated with the user’s account by execut-
ing the op item list command, followed by op get item
<recordID> --reveal, which exposes the Secret Key
and master password. The attack completes in approximately
three seconds, with two seconds required for the authorization
bypass and less than one second for the credential extraction.
The efficiency and low interaction overhead render this attack
highly practical for stealthy credential exfiltration.
                                                                                      Fig. 2: KeePassXC pop-up window.
B. Keeper
   Features and Protections. Keeper is a popular password                Contents folder. To further minimize detection, Hider
manager that provides autofill functionality for login creden-           leverages techniques from our 1Password attack, setting its
tials in macOS applications. Keeper verifies applications us-            window level to screen-saver to remain above all other
ing the Bundle Display Name rather than an immutable                     windows. Moreover, the window frame is omitted to prevent
identifier, such as the Bundle ID. This introduces a critical            visual artifacts, such as blurring when focus shifts between
vulnerability, as an attacker can spoof the Bundle Display               applications. Additionally, the malicious app’s icon is omit-
Name to bypass authentication checks. Notably, modifying                 ted from the Dock, using Electron’s app.dock.hide()
the Bundle Display Name requires neither elevated privileges             API [83], effectively hiding itself from the user.
nor OS-level permissions. To initiate autofill, Keeper provides             Attack Evaluation. The attacker configures a JSON file
keyboard shortcuts for different credential types, such as               listing target applications, with each entry containing the
usernames, passwords, payment info, and one-time passwords               Bundle Display Name of a target. During initialization, the
(OTPs), allowing users to fill these fields individually [82].           malicious application adopts the first target’s Bundle Display
While this approach improves usability, it also constitutes an           Name from the list. Once active, it simulates key presses to
attack vector since a malicious application can programmat-              trigger Keeper’s autofill and extract the credentials associated
ically simulate the required keyboard inputs to exploit the              with the current Bundle Display Name. After harvesting, the
autofill process and harvest credentials without user consent.           application modifies its Bundle Display Name to the next
   Bypassing Autofill Protections. To evaluate Keeper’s autofill         target in the list and restarts, iterating through all specified
functionality, we analyzed its reliance on an application’s              targets. Our analysis indicates that the phishing application
Bundle Display Name for credential autofill validation. We               requires an average of three seconds to retrieve a pair of
developed a malicious macOS application that mimicked a                  credentials per target, with an additional one second to restart
legitimate one by modifying its Bundle Display Name to                   and update its identity. This results in a total execution time of
match a trusted target, and tested whether Keeper would                  four seconds per target, demonstrating the attack’s efficiency
autofill credentials into the spoofed application’s text fields.         and feasibility for large-scale credential harvesting.
Our analysis confirmed that the malicious application success-              Limitations. Despite the aforementioned strategies to en-
fully triggered the autofill functionality, populating the fields        hance the attack’s stealth, certain visual indicators may still
with credentials associated with the legitimate target. Unlike           reveal its presence to the users. First, macOS automatically
1Password, which implements stricter validation, Keeper’s                hides the mouse pointer when a text field is focused using
reliance on a modifiable identifier allows unauthorized access           the Tab key. Since the malicious application relies on this
to stored credentials with minimal effort, extending to other            behavior to trigger autofill, users may notice the pointer
sensitive record types, such as payment information.                     disappearing at regular intervals. Second, macOS adjusts a
   Stealthiness. While the baseline attack is technically effec-         window’s shadow opacity when it is inactive. Although the
tive, its practicality for undetected execution is impacted by           auxiliary application remains on top level, it cannot maintain
visual artifacts during the autofill process. Text fields remain         continuous focus, leading to minor visual effects that users
visible, the malicious application’s window briefly flashes on           might detect. Finally, while the malicious application’s icon
the screen, and its icon momentarily appears in the Dock dur-            is hidden from the Dock to avoid detection, brief flashes or
ing system restarts, increasing the risk of detection. To address        momentary appearances may still occur during application
these issues, we developed an auxiliary application, which we            restarts due to macOS’s built-in app launching behavior.
call Hider, designed to mask the malicious app’s activity
and enhance the attack’s stealthiness (we provide a detailed             C. KeePassXC
description in Appendix B). The auxiliary application operates              Features. Next, we focus our analysis on KeePassXC,
in the foreground to maintain user engagement, while the                 another widely used password manager, to evaluate its aut-
malicious application executes exclusively in the background             ofill mechanism and security flaws. KeePassXC leverages
to perform the attack. Also, to achieve stealthier deployment,           the AutoType feature and supports usernames, passwords,
we deploy the malicious app within the auxiliary application’s           and one-time passwords (OTPs). However, OTP autofill is



                                                                     8
not enabled by default and requires users to configure each            window title (i.e., the label displayed on the window frame)
record individually [84]. Also, it disables autofill by default,       instead of using immutable identifiers. When an application
requiring users to manually enable the feature by configuring          with a matching window title triggers the autofill, MacPass
a keyboard shortcut in the settings. Additionally, users are           submits the associated credentials directly into the application.
required to manually associate credentials with specific appli-        This linking mechanism introduces a critical verification flaw,
cations, similar to Keeper (§IV-B) and MacPass (§IV-D). This           making MacPass vulnerable to credential exfiltration.
association relies on the application’s Bundle Display Name               Window Title Spoofing. In this attack variation, the primary
rather than an immutable identifier like the Bundle ID, making         requirement for the attacker is to modify the malicious appli-
it vulnerable to manipulation. Once configured, the autofill           cation’s window title to impersonate a trusted application—a
process is triggered via a user-defined keyboard shortcut and          straightforward task that requires no elevated permissions. To
requires manual confirmation through a pop-up prompt.                  enhance stealthiness, we omit the window frame entirely from
   Verification Mechanisms. Similar to Keeper, KeePassXC               the malicious application, preventing the window title from
leverages the app’s Bundle Display Name to match and                   being displayed to the user. Furthermore, an attacker can also
autofill credentials without additional validation. However,           recreate the window frame through custom UI design, making
if the requesting application’s window is positioned above             the phishing application visually indistinguishable from the
KeePassXC’s window (i.e., has a higher window level), the              legitimate target.
AutoType feature disables autofill and instead displays a                 Attack Evaluation. The attack follows a series of coordi-
manual credential selection popup, effectively blocking auto-          nated steps to effectively harvest the credentials. Initially, the
matic credential injection. Instead of completing the autofill,        malicious application dynamically modifies its window title
KeePassXC displays a pop-up window (Figure 2) listing all              to match a predefined list of target applications – once Mac-
available vault credentials where the user must manually               Pass detects the spoofed title, the application triggers autofill
select the desired credentials before autofill is completed. Fi-       using the default keyboard shortcut, capturing and storing the
nally, KeePassXC does not provide a default autofill shortcut,         credentials. This process repeats iteratively, with the malicious
requiring attackers to identify the user’s specific keyboard           application updating its window title for each subsequent target
configuration before launching an attack.                              in the list. Our evaluation finds that each cycle—including
   AutoType Exploitation. To detect the keyboard short-                modifying the window title, triggering the AutoType feature,
cut configured for the AutoType feature, we implemented                and capturing a pair of credentials—requires approximately
a brute-force technique that targets commonly used short-              five seconds. This efficiency allows attackers to harvest multi-
cuts [85], [86]. The malicious application emulates keyboard           ple credentials while bypassing any need for user interaction.
combinations while monitoring for focus changes, which in-
dicate that a shortcut has successfully triggered the autofill.        E. Alternative Local Credential-Stealing Attack Vectors
Once the appropriate shortcut is identified, the attack pro-              To assess the broader scope and impact of our attacks, we
ceeds by automating the credential extraction process. The             compare them to a traditional local attack vector for stealing
malicious application navigates the pop-up list using synthetic        passwords: keyloggers, which monitor user inputs to capture
key presses to select entries and confirms the autofill opera-         credentials, have limited effectiveness against password man-
tion. This process is systematically repeated until all stored         agers as credentials are autofilled or typed programmatically.
credentials are extracted. The primary overhead in this attack         Importantly, the macOS Secure Input Mode adds another layer
lies in inferring the user-configured shortcut for Autotype.           of protection by blocking keyloggers from accessing keyboard
To evaluate this process in detail, we conducted a dedicated           events when sensitive fields, such as password inputs, are in fo-
performance analysis measuring the time required to exhaust            cus [87]. Moreover, the Secure Keyboard Entry in the macOS
each phase of our shortcut inference strategy (we provide              Terminal provides protection against keylogging by preventing
more details in Appendix E). Testing the most common default           other applications from intercepting keystrokes; however, this
shortcuts requires approximately ten seconds. Once the correct         feature is not enabled by default [88]. Nonetheless, enabling
shortcut is triggered, credential extraction proceeds at an            Secure Keyboard Entry reduces the risk of unauthorized access
average rate of seven seconds per credential pair. These results       to sensitive inputs, such as sudo passwords, but may also
demonstrate that the attack is both practical and scalable under       introduce compatibility issues with legitimate tools that rely on
realistic conditions for targeting a user’s account credentials        keyboard input interception [89]. In summary, keyloggers have
for a set of popular services.                                         limited effectiveness on macOS, while our attacks are capable
                                                                       of exfiltrating critical user data from password managers.
D. MacPass
   Next, we analyze MacPass and explore its internal ver-                         V. W INDOWS PASSWORD M ANAGERS
ification flaws. Similar to KeePassXC, MacPass adopts the                We shift our focus to the Windows platform, analyze how
AutoType feature for credential injection. However, AutoType           the selected password managers implement their functionality,
is enabled by default and can be triggered using a predefined          and identify vulnerabilities that enable credential exfiltration.
keyboard shortcut [57]. MacPass employs a unique credential              Security Mechanisms & Features. Contrary to macOS,
association method, linking credentials to an application’s            Windows does not enforce strict application verification. Apps



                                                                   9
are not required to use immutable identifiers, and code sign-           absence of security checks in 1Password’s Windows imple-
ing is not mandatory or enforced [90]. Instead, password                mentation allows the attack to execute more efficiently than on
managers rely on mutable properties like window titles for              macOS. While the macOS attack requires separate interactions
autofill verification. In addition, Windows permits inter-app           to access usernames and passwords sequentially, the Windows
interactions without elevated privileges, allowing any app to           variant completes autofill with a single keyboard shortcut. As
simulate keystrokes, manipulate window focus and position,              a result, credential harvesting takes approximately 7 seconds
or change titles. Following the priorly established exploitation        per record, improving performance while maintaining the same
methodology for macOS, we demonstrate attacks that system-              level of effectiveness.
atically extract credentials by exploiting these design flaws.
                                                                        B. Keeper
A. 1Password                                                                Keeper’s autofill functionality on Windows relies on the
                                                                        AutoType mechanism where users associate credential en-
   On Windows, 1Password exposes its autofill functionality             tries with application windows based on their titles, and autofill
via the Quick Access interface, while it differs from its               is triggered via a keyboard shortcut [82].
macOS implementation, where autofill behavior is tied to                    Bypassing Autofill Mechanism. Unlike its macOS coun-
application identity and verified more strictly. Upon activa-           terpart, Keeper associates credentials with window titles rather
tion, the user selects a vault record, and the corresponding            than application metadata. However, it does not continuously
credentials are inserted into the target application. Notably,          verify titles—instead, validation is triggered only when the
this process does not create any persistent association between         application loses and then regains focus. As a result, if the title
the application and the credentials being filled.                       is modified while the application remains in focus, the change
   Platform-specific Mechanisms. In contrast to macOS, the              goes undetected. Attackers are able to manipulate window
Windows version performs no target validation, and our analy-           titles and trick Keeper into autofilling credentials in unautho-
sis confirms that any active window receiving focus is eligible         rized applications. For example, a malicious application can
for autofill, regardless of its origin or developer’s identity.         dynamically alter its window title to impersonate a trusted
Moreover, the Quick Access window persists as long as the               target without triggering a re-validation check. Additionally,
1Password background process is running, enabling repeated              Windows’ permissive security model allows malicious apps
interactions without user reauthentication. These properties            to exploit Keeper’s autofill mechanism without requiring ad-
highlight critical security flaws in 1Password’s Windows im-            ditional permissions. We leverage these weaknesses to de-
plementation compared to its macOS distribution, regarding              ploy a fully automated phishing attack that triggers autofill
permission controls and validation during autofill.                     by spoofing trusted window titles. The phishing application
   Exploiting AutoType. 1Password’s AutoType feature fills              emulates legitimate targets by modifying its title at runtime,
credentials into any active text field, without verifying the           bypassing validation and causing Keeper to inject credentials
identity of the target app. As a result, credentials can be             into unauthorized contexts without user interaction.
injected into arbitrary windows under the attacker’s control.               Stealthiness. To achieve stealthiness, the phishing applica-
We replicate our approach for MacPass (§IV-D), automating               tion omits its window frame to conceal spoofed titles and
input events to trigger AutoType and direct output into                 avoid visual cues. The attack exploits a flaw in Keeper’s
hidden fields within a phishing app.                                    window title verification logic, which performs validation
   Stealthiness. Windows does not enforce window layering               only when the application loses and regains focus. At launch
constraints, and the most recently focused window is always             time, the phishing application spawns two windows: a visible
positioned in the foreground. As a result, prior stealthiness           main window presenting benign content and a secondary,
techniques that rely on display-level manipulation are in-              hidden window used for title spoofing. The hidden window
effective. However, the Quick Access window remains ac-                 is concealed using two techniques: (i) it is configured to be
tive as long as 1Password’s background process is run-                  omitted from the system taskbar and (ii) it is programmat-
ning. Leveraging this persistence, we use the Node.js library           ically repositioned outside the visible screen area using the
node-window-manager [91] in our application to repo-                    node-window-manager library [92]. This configuration
sition the Quick Access interface beyond the visible screen             ensures that the spoofing window remains undetectable, al-
boundaries. Since Windows does not restrict these operations,           lowing the phishing application to manipulate window titles
the interface remains fully functional even when hidden from            and trigger autofill without user awareness.
view. Additionally, 1Password preserves the window’s last                   Attack Evaluation. The malicious app maintains a pre-
known position, ensuring all subsequent activations occur off-          defined list of target apps and their corresponding window
screen without user awareness.                                          titles. For each target, it dynamically modifies its visible main
   The attack follows the priorly established methodology               window’s title to mimic a legitimate app. To trigger autofill,
(§IV), adapted to the Windows environment. Regarding                    the attack simulates a focus-switching sequence, ensuring
stealthiness in this attack variant, the malicious application          Keeper registers the new title. The app momentarily shifts
repositions the Quick Access window off-screen at the start of          focus to the hidden secondary window and then returns focus
execution, preventing the user from noticing its presence. The          to the main window, exploiting Keeper’s reliance on user-



                                                                   10
driven focus changes for title verification. Also, crafted timing          configured. File modification completes in under one second,
delays ensure the spoofed title is detected accurately. Keeper             and the total execution time is approximately five seconds,
identifies the spoofed title instantly, and the focus-switching            which is comparable to the MacPass attack.
process completes in under 1 second. The remaining time is
spent autofilling credentials into text fields. Overall, the attack                    VI. L INUX PASSWORD M ANAGERS
successfully extracts a set of credentials in approximately 3                 On Linux, only 1Password and KeePassXC support autofill
seconds, demonstrating both efficiency and effectiveness.                  for native applications, making it significantly more limited
                                                                           than on Windows or macOS. We applied the previously intro-
C. LastPass & KeepassXC                                                    duced attack methodology, and while the attacks remained ef-
   LastPass. On Windows, LastPass deploys the autofill fea-                fective, platform-specific constraints prevented them from be-
ture using the AutoType mechanism, and users are expected                  ing stealthy. Specifically, Linux does not support display-level
to explicitly associate credentials with target apps. Similar to           distinctions, such as screen-saver and pop-up-menu,
Keeper, LastPass identifies target windows by their titles, and            preventing overlay-based concealment of password manager
it additionally monitors title changes in real time, eliminating           windows. Additionally, Linux enforces an OS-level policy
the need for focus-switching to trigger verification. While                that restricts window positioning within the visible screen
this improves autofill responsiveness, it does not address the             area. We further explored alternative methods to manipulate
underlying vulnerability of relying on mutable window titles.              window behavior using tools such as xdotool [93]. This
Our analysis shows that LastPass exhibits identical vulnera-               approach was ineffective since 1Password’s Quick Access win-
bilities to those previously identified in MacPass (§IV-D). As             dow and KeePassXC’s authorization prompt remained visible
a result, they are similarly susceptible to credential harvesting          throughout the attack. While KeePassXC remains vulnerable
via phishing apps. This attack variation executes with compa-              to the same AutoType-based credential extraction technique,
rable efficiency across platforms, with credentials extracted in           the attack is noticeable due to the persistent visibility of
approximately five seconds.                                                password manager windows. Due to space constraints, we
   KeePassXC. KeePassXC on Windows and macOS share the                     provide additional details in Appendix D.
same deployment model, relying on the AutoType feature,
                                                                                            VII. ATTACK M ITIGATION
which is disabled by default and requires user confirmation
for autofill (§IV-C). Once enabled, triggering AutoType                       Given the significant implications of our attacks, we propose
prompts the user before credentials are inserted. However, the             a series of countermeasures that can be incorporated by
underlying implementation differs across platforms, resulting              password managers or enforced at the OS level.
in distinct attack surfaces.                                                  Security checks enhancement. Our analysis of 1Password
   Platform-Specific Mechanisms. On Windows, KeePassXC                     on macOS uncovered a series of security checks that are
identifies target apps by their window titles. When a match                employed for ensuring the legitimacy of the application trig-
is found, it displays an authorization prompt requiring user               gering autofill. Surprisingly, the majority of the password
confirmation. However, this behavior can be disabled via a                 managers did not employ the extensive security measures
configuration setting. If the confirmation prompt is turned off,           that 1Password does, resulting in highly insecure applications
KeePassXC automatically fills credentials into any matching                that can be trivially tricked into autofilling user credentials.
window title without user interaction. We identified an ad-                The first step for fortifying password managers on macOS is
ditional flaw in KeePassXC configuration storage. Both the                 to leverage all of the OS-level mechanisms that are readily
confirmation prompt setting and the keyboard shortcut used                 available. This countermeasure can only be implemented by
to trigger AutoType are stored in a plaintext configuration                macOS password managers, as Windows and Linux currently
file located in the user’s app folder1 . This file is unprotected          do not expose the required OS-level properties and callbacks.
and can be modified by any app with user-level access. A                   Finally, specifically for 1Password on macOS, we emphasize
malicious app may disable the confirmation prompt and assign               that the checks performed on the main autofill process should
a known shortcut. Even though these changes require a restart              also be employed for the secondary ones that we exploit. In
of KeePassXC, this can be triggered programmatically or may                other words, the robustness of the autofill process should not
occur during regular user activity.                                        be undermined by additional usability features.
   Attack Workflow & Performance. The attack follows the                      Window placement: z-index level. As mentioned
strategy deployed against LastPass and MacPass (§IV-D). The                before, macOS distinguishes between pop-up-menu
phishing app first modifies the configuration file to disable              and screen-saver window levels. As a result,
the prompt and set a predefined shortcut, eliminating the                  screen-saver level windows can hide any focused
need for user interaction. After restarting KeePassXC, the app             windows at the pop-up-menu level, even the ones
triggers AutoType and captures the injected credentials. The               meant to always stay at the screen’s top level. A
attack outperforms the brute-force shortcut inference approach             straightforward mitigation involves modifying password
required on macOS, since the keyboard shortcut is explicitly               manager implementations to reposition their pop-up
                                                                           interfaces (e.g., 1Password’s Quick Access window and
   1 C:\Users\<user>\AppData\Roaming\KeePassXC                             CLI authorization prompt) to the screen-saver window



                                                                      11
level, rather than the default pop-up-menu level. At this                   limited customization, they benefit from privileged rendering
elevated level, attacker-controlled windows placed at the same              behavior enforced by the OS.
layer will appear behind the password manager interface.                       Windows prototype. We developed our defensive tool as
Since the system brings to the front the most recently                      a C++ application. The core mechanism intercepts keyboard
interacted window when autofill is triggered via a keyboard                 events at a low level and analyzes them to determine their
shortcut, this approach ensures that the password manager’s                 origin. The tool utilizes a low-level keyboard hook proce-
interface remains visible to the user.                                      dure by calling the SetWindowsHookEx function with the
   Window Placement and Screen Boundaries. In Windows,                      WH_KEYBOARD_LL hook type [94]. This allows the appli-
the pop-up-menu and screen-saver window levels are                          cation to monitor all keyboard input events at the system
treated equivalently, preventing the use of window layering                 level before they reach any applications. The hook proce-
for reliably prioritizing sensitive UI elements. Our attack                 dure (LowLevelKeyboardProc) processes each keyboard
is stealthy since it leverages the node-window-manager                      event encapsulated in the KBDLLHOOKSTRUCT structure.
library to reposition the 1Password Quick Access window                     We focus on events where the nCode parameter equals
beyond the visible screen boundaries. Preventing such off-                  HC_ACTION, indicating a keyboard event that should be pro-
screen placement at the OS level (e.g., by constraining window              cessed. Within this procedure, we verify the flags field of the
coordinates to the physical display area) would significantly               KBDLLHOOKSTRUCT to determine if the event was generated
limit our attack’s stealthiness.                                            synthetically. Specifically, we access the LLKHF_INJECTED
   Synthetic Click Detection. Our attacks rely on emulated                  flag, which signifies that the event was injected by an applica-
keyboard presses, making synthetic input detection a critical               tion rather than originating from a physical keyboard press. If
countermeasure. However, legitimate apps, such as terminal                  such a synthetic event is detected, our tool launches an alert
emulators and accessibility tools, also use synthetic input for             window to warn the user about the synthetic keyboard input.
automation and usability. Password managers should integrate                We designed the alert window to be displayed at the topmost
detection mechanisms that differentiate between user-triggered              level of the screen by using the MessageBox function with
autofill and external manipulation, rather than enforcing uni-              the MB_TOPMOST flag. This ensures that the alert window
form OS-level restrictions. For instance, MacPass (§IV-D)                   stays above all other windows, including those set to the
relies on synthetic input for autofill, and rejecting synthetic             topmost level by other applications.
events would break its intended functionality. Instead, pass-
word managers should validate the requesting process ID and                                       VIII. D ISCUSSION
restrict autofill to explicitly linked applications, preventing                Disclosures. We have responsibly disclosed our findings to
unauthorized input injection while preserving legitimate au-                the developers of all the evaluated password managers, all of
tomation. To evaluate this defense, we develop a prototype                  whom have acknowledged our reports. Keeper and MacPass
tool for macOS and Windows that detects synthetic input from                found our suggestions especially helpful and are actively
running applications and issues security warnings to users.                 working on implementing fixes. Keeper further acknowledged
   macOS prototype. We have developed a prototype detection                 our efforts with a bug bounty reward. 1Password stated that
tool as a Swift application. The primary mechanism employed                 while they want to deploy countermeasures, they are “really
by the detection tool is to listen for Key Pressed events (i.e.,            restricted by the platform as to what defences we can deploy
when the CGEventType instance is set to .keyDown) and                       to defend against attacks such as this.” We will continue to
check if at least one of the following conditions is true: (i) The          work with all vendors upon request, sharing countermeasures
Process ID of the application that generated the synthetic event            and assisting them in navigating OS limitations to improve
is equal to 0, which indicates that the event originated at the             security.
system level. (ii) The User ID associated with the process is                  Stealthiness. Our attack employs various concealment tech-
equal to 0, i.e., the root. (iii) The User ID associated with the           niques to eliminate visible execution traces. The majority
process is equal to 244, i.e., the specific system user account             are stealthy, with two exceptions: Keeper on macOS, which
associated with input device handling (e.g., keyboard).                     exhibits minor visual artifacts, and Linux, which is limited by
   If any of the conditions is satisfied, it indicates that the user        internal UI constraints. On macOS, window layering, Dock
has physically pressed the detected key; otherwise, a poten-                suppression, and visual overlays effectively eliminate all attack
tially untrusted application has triggered the interaction. In the          indicators. On Windows, the absence of layering constraints
latter case, our defense mechanism triggers a visual alert and              allows the application’s windows to be repositioned off-screen
notifies the user. However, in a production deployment, this                without triggering visual alerts. Video demonstrations of all
signal can be leveraged to enforce stricter mitigations, such as            the attack variants are available on our artifact page [28].
immediately locking the vault and requiring re-authentication                  Real-world Applicability. To evaluate the scalability of
(e.g., master password, biometrics, OS credential) to prevent               our attacks, we include details about the performance of each
unauthorized autofill. Our prototype interface is implemented               attack variant to highlight the limited time each of our exploits
as a system-level window to ensure it is always rendered                    takes to complete exfiltration. We include performance values
above all other windows, including those manually elevated to               for the primary attack variant against each password manager
the screen-saver level. While system-level windows offer                    in Table II. Additionally, our attacks on macOS rely on users



                                                                       12
enabling the Accessibility permissions for our malicious app,            cross-platform attacks from a desktop against mobile super
which we found to be a common practice and hence, a                      apps like WeChat.
reasonable assumption, since 20% of the 100 most popular                    Password Managers. In 2012, Bonneau et al. [119] found
free apps on the App Store request this permission (see §IV.)            that password managers are not resilient to internal observa-
   Additional Credential Mechanisms. Our attack targets tra-             tion, i.e., an attacker can impersonate a user by intercepting
ditional autofill mechanisms in standalone password managers.            from inside the user’s device. Li et al. [120] in 2014 and
We also evaluated whether similar techniques could be ap-                Oesch and Ruoti [121] in 2020 found that web-based pass-
plied to OS-level credential stores and modern authentication            word managers use insecure defaults and include unencrypted
alternatives. Specifically, macOS Keychain Access [95] does              metadata, which makes them vulnerable to credential stealing
not expose autofill capabilities for native applications, and            and clickjacking attacks. Fabrega et al. [122] used injection
credential retrieval typically requires explicit user interaction        attacks against password managers that allowed attackers
via system dialogs, which falls outside our threat model.                to extract confidential information from observing protected
Similarly, passkey-based authentication [96], [97], increas-             data. Finally, studies have also demonstrated vulnerabilities in
ingly supported by password managers, relies on challenge-               password managers’ autofill implementations.
response protocols (e.g., WebAuthn [98]) and bypasses form-
based credential injection. Since they do not rely on typical            A. Comparison with Prior Work
input field submission, and password managers interface with                Next, we provide a detailed comparison between our work
browser or app APIs, our credential harvesting attacks do not            and prior research on credential-stealing attacks against pass-
directly apply to passkeys. We leave a systematic evaluation             word managers, which we summarize in Table III.
of passkey-specific threat models and additional credential                 Silver et al. [99] evaluated desktop and mobile password
management mechanisms to future work.                                    managers’ functionality within web browsers. Their exploits
                                                                         can be largely categorized based on attacker placement —
                    IX. R ELATED W ORK                                   first, a malicious website carefully crafts a web page to extract
   UI Attacks. Early works addressing secure UI proposed                 information from autofilled values; and second, a malicious
isolated window systems via solutions like EROS [103] and                attacker intercepts traffic when on the same network as the
TrustedX [104]. Recent work on UI security has focused                   victim (e.g., public Wi-Fi in a coffee shop). While the attacks
on mobile platforms [105], [106], [107], [101], [108], [109],            require initial user interaction to trigger the attack (e.g., the
[110]. Bianchi et al. [106] exploited Android’s full-screen              user interacts with the website or joins a new Wi-Fi network),
overlay to trick users into interacting with phishing apps that          subsequently the attack can be executed in a stealthy manner,
mimic the GUI of legitimate apps. Fratantonio et al. [101]               by triggering password managers to autofill hidden iframes or
demonstrated users’ susceptibility to granting permissions that          browser windows.
could enable malicious apps to take over the UI feedback loop.              Lin et al. [77] demonstrated vulnerabilities in password
Lee et al. [107] found iOS apps that use stealthy and malicious          managers’ handling of autofill on websites. They developed
crowdturfing UIs to manipulate app ranking. Researchers have             curated web forms that remain hidden from the victim, with
also studied UI attacks on non-traditional display settings.             the help of CSS attributes, overlays, and off-screen placement.
Mahdad et al. [111] used deceptive overlays on limited-                  When the victim visits and interacts with the web page, pass-
display FIDO2 authenticators that trick users into authorizing           word managers autofill hidden form fields, enabling stealthy
malicious sign-in requests. Cheng et al. [112] demonstrated UI           credential exfiltration. Fu and Wang [100] extended prior
attacks on popular AR platforms from Apple, Google, Meta,                work by exploring password managers’ handling of hidden
Microsoft, and within the WebXR API in the browser.                      <input> elements when autofilling forms on sites within
   Desktop Apps. Our threat model exploits password man-                 web browsers.
agers using a malicious desktop app. Prior work has shown                   Fratantonio et al. [101] demonstrated vulnerabilities in
several vulnerabilities in desktop apps; Xiao et al. [113]               Android’s implementation of Accessibility permissions. While
demonstrated that vulnerable cross-context flows can allow               they did not explicitly demonstrate attacks against password
attackers to perform Remote Code Execution (RCE) and take                managers, the same techniques the paper demonstrated could
over an operating system. Ali et al. [114] showed that popular           be used to access the vault of a password manager installed
Electron apps may have insecurities that can lead to RCEs, and           on the mobile device. Gangwal et al. [102] exploited the
Paloscia et al. [115] explored how migrating web application             WebView functionality used to load web pages within Android
code to desktop apps suffers from inherent flaws due to the              apps. They demonstrated that while an app may load an
differences that exist between the two different execution               external login page within a WebView, an autofill attempt
environments. Jin et al. [116] demonstrated an exploit within            on this WebView can leak credentials to the underlying app.
Microsoft Teams and developed a DOM-based defense mech-                  Their work demonstrated shortcomings in the autofill design
anism. Ahmadpanah et al. [117] found vulnerabilities in local            of mobile password managers and Android’s system-level
deployments of trigger-action platforms, e.g., Node-RED, that            intermediation for autofill.
execute code across multiple applications. Finally, Wang et                 This work. Native password managers expose a funda-
al. [118] exploited lax privilege checks on Windows to launch            mentally different attack surface compared to their browser-



                                                                    13
TABLE III: Comparison with prior work on attacks against password managers. Here, we consider Device (! = Desktop, ! =
Mobile) evaluated in the study, the attacker’s Placement in regard to the victim (! / ! = on-device, ! = in a web browser,
" = on-network), whether the victim needs to interact with the vulnerable platform (i.e., app or web browser) to Trigger
the attack (! = Requires UI, " = No UI), whether the attacks are Stealthy (" = Stealthy, # = Not stealthy), and the
Platform (! = web browser, ! = mobile phone, ! = desktop), along with the corresponding exploited Feature.
                                               Attacker            Victim                                Vulnerability
          Reference                  Device
                                              Placement   UI Trigger    Stealthiness     Platform                Feature
          Silver et al. [99]         ! !       ! "           !                "             !         Hidden iframes and windows
          Lin et al. [77]             !         !            !                "             !         Hidden form fields
          Fu and Wang [100]           !         !            !                "             !         Hidden <input> fields
          Fratantonio et al. [101]    !         !            "                "             !         Android’s Permission Model
          Gangwal et al. [102]        !         !            !                #             !         Android’s Autofill Intermediation
          Vault Raider (this work)    !         !            "                "             !         Native Desktop Autofill



based or mobile counterparts. Prior work has focused on those           We demonstrate a range of UI-based attacks that compromise
environments by exploiting form heuristics, insecure inter-app          sensitive user credentials, financial information, and even
communication, or overlay-based UI attacks [77], [102], [100],          bypass 2FA. Our work examines multiple popular password
[101]. Their attacks operate within different security contexts         managers across major operating systems, uncovering critical
and constraints, such as the browser sandbox or Android’s               security vulnerabilities that enable compromising users’ online
permission architecture. Also, prior threat models assume               accounts. To mitigate these risks, we have designed straight-
additional conditions, such as user interaction or compromised          forward techniques for detecting synthetic user input events
origins. In contrast, our attack targets standalone desktop             and preventing our attacks. Accordingly, we have disclosed
password managers, for which completely different safeguards            our findings and mitigations to the respective developers,
exist (e.g., see §IV for macOS-specific mechanisms). We                 encouraging them to implement the necessary safeguards. Our
exploit intended autofill-related functionality and the absence         work advances ongoing efforts of enhancing the security of
of robust application identity verification to harvest creden-          password managers and ensuring that they remain a trustwor-
tials without user interaction. Our attack leverages native OS          thy tool for users.
features and verification inconsistencies, exposing a novel and
previously unexplored threat vector. Nonetheless, our attack                               E THICAL C ONSIDERATIONS
also incorporates hidden form elements and manipulates UI-                All experiments were conducted using desktop environ-
related features to achieve stealthiness, and UI-based deception        ments, configurations, and applications under our control.
has been used against autofill [77]. Importantly, we demon-             Password manager evaluations relied on synthetic credentials
strate attacks that target the credentials of a password man-           and test accounts created for this study. No real user data,
ager’s vault itself. Overall, we highlight features that remain         accounts, or devices were used at any stage, and our attacks
unavailable in web browsers and mobile apps, and therefore              did not affect any actual users. Moreover, as detailed in §VIII,
uncover vulnerabilities left unexplored by prior research.              we have notified all of the affected password manager vendors
   Despite extensive research into password managers’ usabil-           of our findings and our proposed mitigation techniques.
ity and security, their analysis has been limited to mobile
and browser-based platforms. Our work highlights unique                                       ACKNOWLEDGEMENTS
challenges that password managers face on desktop platforms,
which have variable security models that make them suscepti-               We thank the anonymous reviewers and shepherd for their
ble to UI-based attacks. We hope that our work inspires further         helpful feedback. This project was supported by the Na-
research on the nuances of desktop-based deployments and                tional Science Foundation (CNS-2211574, CNS-2143363).
incentivizes operating systems to standardize and secure native         The views in this paper are only those of the authors and
autofill functionality similar to mobile platforms.                     may not reflect those of the US Government or the NSF.

                                                                                                    R EFERENCES
                       X. C ONCLUSIONS
                                                                          [1] M. Ghasemisharif, C. Kanich, and J. Polakis, “Towards automated
   While years of research have identified barriers to password               auditing for account and session management flaws in single sign-on
managers’ adoption, developers have made notable progress                     deployments,” in 2022 IEEE Symposium on Security and Privacy (SP).
in addressing these issues by introducing desktop applications            [2] K. Drakonakis, S. Ioannidis, and J. Polakis, “The cookie hunter:
                                                                              Automated black-box auditing for web authentication and authorization
and features like universal autofill and quick access. How-                   flaws,” in Proceedings of the 2020 ACM SIGSAC Conference on
ever, these advancements also introduce new attack vectors.                   Computer and Communications Security (CCS).
In this work, we highlight how desktop operating systems’                 [3] M. Ghasemisharif, A. Ramesh, S. Checkoway, C. Kanich, and J. Po-
                                                                              lakis, “O single {Sign-Off}, where art thou? an empirical analysis of
unique architectures, features, and constraints can augment or                single {Sign-On} account hijacking and session management on the
undermine the security mechanisms of password managers.                       web,” in 27th USENIX security symposium (USENIX Security ’18).




                                                                   14
 [4] S. Sivakorn, I. Polakis, and A. D. Keromytis, “The cracked cookie jar:            [30] T. Verge, “Google chrome password manager integrates with android
     Http cookie hijacking and the exposure of private information,” in 2016                autofill,” https://www.theverge.com/2024/10/18/24273369/google-
     IEEE symposium on security and privacy (SP).                                           chrome-android-password-manager-native-autofill, 2024.
 [5] L. Lassak, E. Pan, B. Ur, and M. Golla, “Why aren’t we using                      [31] M. Foundation, “Firefox sync features,” https://www.mozilla.org/en-
     passkeys? obstacles companies face deploying FIDO2 passwordless                        US/firefox/features/sync/, 2024.
     authentication,” in USENIX Security ’24.                                          [32] A. Inc., “Set up icloud keychain to autofill information on mac,”
 [6] L. Lassak, A. Hildebrandt, M. Golla, and B. Ur, “”it’s stored, hopefully,              https://support.apple.com/guide/mac-help/set-icloud-keychain-autofill-
     on an encrypted server’’: Mitigating users’ misconceptions about                       information-mac-mh43699/mac., 2024.
     FIDO2 biometric WebAuthn,” in USENIX Security ’21.                                [33] M. W. Docs, “Html attribute: autocomplete,” https://developer.mozilla.
 [7] C. Herley and P. Van Oorschot, “A research agenda acknowledging the                    org/en-US/docs/Web/HTML/Attributes/autocomplete, 2024.
     persistence of passwords,” IEEE Security & privacy, vol. 10, no. 1, pp.           [34] TechTarget, “Password manager,” https : / / www . techtarget . com /
     28–36, 2011.                                                                           searchsecurity/definition/password-manager, 2024.
 [8] J. Blessing, D. Hugenroth, R. J. Anderson, and A. R. Beresford,                   [35] 1Password, “1Password: Password Manager for Families, Businesses,
     “Sok: Web authentication in the age of end-to-end encryption,” 2024.                   Teams,” 2024, accessed: 2024-11-06. [Online]. Available: https:
     [Online]. Available: https://arxiv.org/abs/2406.18226                                  //1password.com/
 [9] S. Komanduri, R. Shay, P. G. Kelley, M. L. Mazurek, L. Bauer,                     [36] LastPass, Inc., “Lastpass,” https://www.lastpass.com/, 2024, accessed:
     N. Christin, L. F. Cranor, and S. Egelman, “Of passwords and people:                   2024-11-06.
     measuring the effect of password-composition policies,” in ACM CHI                [37] Keeper Security, Inc., “Keeper security,” https://www.keepersecurity.
     ’11.                                                                                   com/, 2024, accessed: 2024-11-06.
[10] J. Bonneau, “The science of guessing: analyzing an anonymized corpus              [38] Wikipedia contributors, “Multi-factor authentication — Wikipedia,
     of 70 million passwords,” in 2012 IEEE S&P.                                            the free encyclopedia,” 2024, [Online; accessed 6-November-
[11] D. Wang, Z. Zhang, P. Wang, J. Yan, and X. Huang, “Targeted online                     2024]. [Online]. Available: https://en.wikipedia.org/wiki/Multi-factor
     password guessing: An underestimated threat,” in ACM CCS ’16.                          authentication
[12] J. Bonneau, E. Bursztein, I. Caron, R. Jackson, and M. Williamson,                [39] 1Password, “Zero-knowledge encryption in 1password,” https : / /
     “Secrets, lies, and account recovery: Lessons from the use of personal                 1password.com/features/zero-knowledge-encryption/, 2024.
     knowledge questions at google,” in WWW ’15.                                       [40] C. Topcuoglu, A. Martinez, A. Acar, S. Uluagac, and E. Kirda, “Macos
[13] D. Florêncio, C. Herley, and P. C. van Oorschot, “Password portfolios                 versus microsoft windows: A study on the cybersecurity and privacy
     and the Finite-Effort user: Sustainably managing large numbers of                      user perception of two popular operating systems.”
     accounts,” in USENIX Security ’14.                                                [41] T. Wang, K. Lu, L. Lu, S. Chung, and W. Lee, “Jekyll on iOS:
[14] D. Florencio and C. Herley, “A large-scale study of web password                       When benign apps become evil,” in 22nd USENIX Security Symposium
     habits,” in WWW ’07.                                                                   (USENIX Security ’13).
[15] A. Nisenoff, M. Golla, M. Wei, J. Hainline, H. Szymanek, A. Braun,                [42] M. Stute, S. Narain, A. Mariotto, A. Heinrich, D. Kreitschmann,
     A. Hildebrandt, B. Christensen, D. Langenberg, and B. Ur, “A {Two-                     G. Noubir, and M. Hollick, “A billion open interfaces for eve and
     Decade} retrospective analysis of a university’s vulnerability to attacks              mallory: MitM, DoS, and tracking attacks on iOS and macOS through
     exploiting reused passwords,” in USENIX Security ’23.                                  apple wireless direct link,” in 28th USENIX Security Symposium
[16] D. Florêncio, C. Herley, and B. Coskun, “Do strong web passwords                      (USENIX Security ’19).
     accomplish anything?” HotSec, vol. 7, no. 6, p. 159, 2007.                        [43] A. Cunningham. (2025) macos sequoia makes you jump through more
                                                                                            hoops to disable gatekeeper app checks. [Online]. Available:
[17] K. Thomas, F. Li, A. Zand, J. Barrett, J. Ranieri, L. Invernizzi,
                                                                                            https://arstechnica.com/gadgets/2024/08/macos- 15- sequoia- makes-
     Y. Markov, O. Comanescu, V. Eranti, A. Moscicki et al., “Data
                                                                                            you-jump-through-more-hoops-to-disable-gatekeeper-app-checks/
     breaches, phishing, or malware? understanding the risks of stolen
     credentials,” in Proceedings of the 2017 ACM CCS.                                 [44] T. Yin, Z. Gao, Z. Xiao, Z. Ma, M. Zheng, and C. Zhang, “{KextFuzz}:
                                                                                            Fuzzing {macOS} kernel {EXTensions} on apple silicon via exploiting
[18] J. A. Halderman, B. Waters, and E. W. Felten, “A convenient method
                                                                                            mitigations,” in 32nd USENIX Security Symposium (USENIX Security
     for securely managing passwords,” in WWW ’05.
                                                                                            23), 2023, pp. 5039–5054.
[19] B. Ross, C. Jackson, N. Miyake, D. Boneh, and J. C. Mitchell,
                                                                                       [45] Y. Wang, Y. Hu, X. Xiao, and D. Gu, “iservice: Detecting and evaluat-
     “Stronger password authentication using browser extensions.” in
                                                                                            ing the impact of confused deputy problem in appleos,” in Proceedings
     USENIX Security ’05.
                                                                                            of the 38th Annual Computer Security Applications Conference, 2022.
[20] S. Chiasson, P. C. van Oorschot, and R. Biddle, “A usability study and            [46] D. Winder, “Forbes - mac users warned as ‘fully undetectable’ security
     critique of two password managers.” in USENIX Security ’06.                            backdoor confirmed,” https://www.forbes.com/sites/daveywinder/2025/
[21] A. Karole, N. Saxena, and N. Christin, “A comparative usability                        02/04/mac- users- warned- as- fully- undetectable- security- backdoor-
     evaluation of traditional password managers,” in Information Security                  confirmed/, 2025.
     and Cryptology-ICISC 2010: 13th International Conference.                         [47] C. Z. Harris. (2024) Apple’s macos sequoia changes how you install
[22] D. McCarney, D. Barrera, J. Clark, S. Chiasson, and P. C. van Oorschot,                unsigned apps. [Online]. Available: https://www.idownloadblog.com/
     “Tapas: design, implementation, and usability evaluation of a password                 2024/08/07/apple-macos-sequoia-gatekeeper-change-install-unsigned-
     manager,” ser. ACSAC ’12.                                                              apps-mac/
[23] S. Pearman, S. A. Zhang, L. Bauer, N. Christin, and L. F. Cranor,                 [48] T. Holwerda. (2024) Bug or intentional? macos 15.1 completely
     “Why people (don’t) use password managers effectively,” in Fifteenth                   removes ability to launch unsigned applications. [Online]. Available:
     Symposium on Usable Privacy and Security (SOUPS 2019), 2019.                           https://www.osnews.com/story/141055/bug-or-intentional-macos-15-
[24] “Mdn web docs - url,” https://developer.mozilla.org/en-US/docs/Web/                    1-completely-removes-ability-to-launch-unsigned-applications/
     API/URL, 2024.                                                                    [49] Apple Support Communities. (2024) How to run unsigned apps in
[25] K. Thomas, J. Pullman, K. Yeo, A. Raghunathan, P. G. Kelley,                           macos 15.1? [Online]. Available: https://discussions.apple.com/thread/
     L. Invernizzi, B. Benko, T. Pietraszek, S. Patel, D. Boneh et al.,                     255759797?sortBy=rank
     “Protecting accounts from credential stuffing with password breach                [50] TeamViewer, “Remote control a mac,” https://www.teamviewer.com/
     alerting,” in USENIX Security ’19.                                                     en/global/support/knowledge-base/teamviewer-classic/remote-control/
[26] J. Nejati, M. Luo, N. Nikiforakis, and A. Balasubramanian, “Need for                   remote-control-a-mac/, 2023.
     mobile speed: A historical analysis of mobile web performance,” 2020.             [51] P. Wardle, “Proton: Osx rat,” https://objective-see.org/blog/blog 0x14.
[27] C. Qian, H. Koo, C. Oh, T. Kim, and W. Lee, “Slimium: debloating                       html, 2017.
     the chromium browser with feature subsetting,” in ACM CCS ’20.                    [52] C. W. Charlie Osborne, “Mami malware targets mac os x dns settings,”
[28] A. Infantino, M. M. Ali, K. Solomos, and J. Polakis, “[Artifact] Vault                 https://www.zdnet.com/article/mami-malware-targets-mac-os-x-dns-
     Raider: Stealthy UI-based Attacks Against Password Managers in                         settings/, 2018.
     Desktop Environments,” 2026. [Online]. Available: https://doi.org/10.             [53] Team Signhouse, “1Password Revenue and Growth Statistics (2024),”
     5281/zenodo.16996391                                                                   Aug. 2024. [Online]. Available: https://usesignhouse.com/blog/
[29] web.dev, “Autofill in forms,” https://web.dev/learn/forms/autofill/, 2023.             1password-stats/




                                                                                  15
[54] Keeper Security, “Keeper Reaches 1 Million Customers Worldwide,”                           Request for Comments RFC 6238, May 2011. [Online]. Available:
     May 2020, publisher: Keeper Security. [Online]. Available: https:                          https://datatracker.ietf.org/doc/rfc6238/
     //www.keepersecurity.com/blog/2020/05/27/keeper-reaches-1-million-                    [80] 1Password, “1password cli documentation: Get started,” https : / /
     customers-worldwide/                                                                       developer.1password.com/docs/cli/get-started/, 2025.
[55] M. Kapko, “What’s at stake for 33M compromised LastPass users?”                       [81] ——, “Secret key security,” https://support.1password.com/secret-key-
     Cybersecurity Dive, Jan. 2023. [Online]. Available: https://www.                           security/, 2025.
     cybersecuritydive.com/news/lastpass-breach-high-stakes/639838/                        [82] Keeper Security, “Keyboard shortcuts: Tips and tricks,” 2024.
[56] KeePassXC Team, “Install KeePassXC on Linux,” Dec. 2024. [Online].                         [Online]. Available: https://docs.keeper.io/en/user- guides/tips- and-
     Available: https://flathub.org/apps/org.keepassxc.KeePassXC                                tricks/keyboard-shortcuts
[57] HicknHack Software GmbH, “MacPass,” Jan. 2025, original-                              [83] Electron Contributors, “app.dock.hide() - electron documentation,”
     date: 2012-07-21T00:48:01Z. [Online]. Available: https://github.com/                       https://www.electronjs.org/docs/latest/api/app#appdockhide- macos,
     MacPass/MacPass                                                                            2024.
[58] Electron. (2024) Browserwindow: setAlwaysOnTop flag, level, and                       [84] KeePassXC Team, “Keepassxc user guide,” 2024. [Online]. Available:
     relativelevel. Accessed: 2024-10-11. [Online]. Available: https://www.                     https://keepassxc.org/docs/KeePassXC UserGuide
     electronjs.org/docs/latest/api/browser-window#winsetalwaysontopflag-                  [85] K. Team, “Keyboard shortcuts,” 2025. [Online]. Available: https:
     level-relativelevel                                                                        //keepass.info/help/kb/keyb shortcuts.html
[59] J. Stallings, “RobotJS: Desktop automation for node.js,” https://robotjs.             [86] 1Password, “Keyboard shortcuts — 1password support,” 2024.
     io/, 2015, accessed: October 11, 2024.                                                     [Online]. Available: https://support.1password.com/keyboard-shortcuts/
[60] M. Eddy, “The Best Password Managers,” The New York Times,                            [87] N. Turner, “macos secure input mode: Understanding its purpose
     Oct. 2024. [Online]. Available: https://www.nytimes.com/wirecutter/                        and implications,” https://nickjvturner.com/macos-secure-input-mode,
     reviews/best-password-managers/                                                            2024.
[61] S. Gilbertson, “The Best Password Managers to Secure Your Digital                     [88] Apple Inc., Use Secure Keyboard Entry in Terminal on Mac, https://
     Life,” Wired, Apr. 2024. [Online]. Available: https://www.wired.com/                       support.apple.com/guide/terminal/use-secure-keyboard-entry-trml109/
     story/best-password-managers/                                                              mac#, 2024.
[62] Apple Developer, “Managing your app’s information property                            [89] Tenable, “5.10 Ensure Secure Keyboard Entry Terminal.app Is En-
     list,” accessed: 2024-11-06. [Online]. Available: https://developer.                       abled,” https : / / www. tenable . com / audits / CIS Apple macOS 12 . 0
     apple.com/documentation/bundleresources/information property list/                         Monterey Cloud-tailored v1.0.0 L1, 2025.
     managing your app s information property list                                         [90] Microsoft Docs, “Use code signing for better control and protec-
[63] Apple Inc., The Bundle Identifier, 2021. [Online]. Avail-                                  tion,” Microsoft Learn, 2025, https : / / learn . microsoft . com / en - us /
     able: https://developer.apple.com/documentation/bundleresources/                           windows/security/application-security/application-control/app-control-
     information property list/cfbundleidentifier                                               for- business / deployment / use - code - signing - for- better- control - and -
[64] Code       Signing      Guide,       “About       Code      Signing,”    Sep.              protection.
     2016,       publisher:        Apple       Inc.      [Online].      Available:         [91] npm, “node-window-manager,” 2024. [Online]. Available: https:
     https://developer.apple.com/library/archive/documentation/Security/                        //www.npmjs.com/package/node-window-manager
     Conceptual/CodeSigningGuide/Introduction/Introduction.html                            [92] npm contributors, “node-window-manager: Node.js library for man-
[65] “Code signing process of macos applications,” https://support.apple.                       aging native application windows,” https://www.npmjs.com/package/
     com / guide / security / app - code - signing - process - sec3ad8e6e53 / web,              node-window-manager.
     2024.                                                                                 [93] J. Sissel, “xdotool: Fake keyboard/mouse input, window management,
[66] M. Developers, “Macos accessibility api,” https://developer.apple.com/                     and more,” https://github.com/jordansissel/xdotool, 2025.
     accessibility/, 2024.                                                                 [94] Microsoft Developer Network, “SetWindowsHookExA function (wi-
[67] 1Password, “How to use universal autofill on mac,” https://1password.                      nuser.h),” https : / / learn . microsoft . com / en - us / windows / win32 / api /
     com/features/how-to-use-universal-autofill-on-mac/, 2024.                                  winuser/nf-winuser-setwindowshookexa, 2024.
[68] M. Developers, “Autotype,” https://github.com/MacPass/MacPass/wiki/                   [95] Apple Inc., “What is keychain access on mac?” 2024. [Online].
     Autotype, 2024.                                                                            Available: https://support.apple.com/guide/keychain- access/what- is-
[69] K. Developers, “Auto-type — keepassxc user guide,” https://keepassxc.                      keychain-access-kyca1083/mac
     org/docs/KeePassXC UserGuide# auto type, 2024.                                        [96] 1Password, “Passkeys: The future of secure sign-in,” 2024. [Online].
[70] M. Naseri, N. P. Borges Jr, A. Zeller, and R. Rouvoy, “Accessileaks: In-                   Available: https://1password.com/product/passkeys
     vestigating privacy leaks exposed by the android accessibility service,”              [97] LastPass, “Passwordless authentication with passkeys,” 2024.
     in PETS 2019-The 19th Privacy Enhancing Technologies Symposium.                            [Online]. Available: https://www.lastpass.com/features/passwordless-
[71] Y. Jang, C. Song, S. P. Chung, T. Wang, and W. Lee, “A11y attacks:                         authentication
     Exploiting accessibility in operating systems,” in Proceedings of the                 [98] M. W. Docs, “Web authentication api,” https://developer.mozilla.org/
     2014 ACM CCS.                                                                              en-US/docs/Web/API/Web Authentication API, 2024.
[72] W. Diao, Y. Zhang, L. Zhang, Z. Li, F. Xu, X. Pan, X. Liu, J. Weng,                   [99] D. Silver, S. Jana, D. Boneh, and E. Chen, “Password Managers:
     K. Zhang, and X. Wang, “Kindness is a risky business: On the usage of                      Attacks and Defenses,” in USENIX Security 14.
     the accessibility {APIs} in android,” in 22nd International Symposium                [100] Y. Fu and D. Wang, “Leaky autofill: An empirical study on the privacy
     on Research in Attacks, Intrusions and Defenses (RAID 2019).                               threat of password managers’ autofill functionality,” in Proceedings
[73] Y. Fratantonio, C. Qian, S. P. Chung, and W. Lee, “Cloak and dagger:                       of the Annual Computer Security Applications Conference (ACSAC).
     from two permissions to complete control of the ui feedback loop,” in                      ACM, 2024.
     2017 IEEE Symposium on Security and Privacy (SP).                                    [101] Y. Fratantonio, C. Qian, S. P. Chung, and W. Lee, “Cloak and Dagger:
[74] 1Password Support, “How 1password fills information in apps on your                        From Two Permissions to Complete Control of the UI Feedback Loop,”
     mac,” https://support.1password.com/mac-universal-autofill-settings/,                      in 2017 IEEE Symposium on Security and Privacy (SP).
     November 2022, accessed: 2024-10-11.                                                 [102] A. Gangwal, S. Singh, and A. Srivastava, “AutoSpill: Credential
[75] A. D. Documentation, “Nswindow.level,” https://developer.apple.com/                        Leakage from Mobile Password Managers,” in Proceedings of ACM
     documentation/appkit/nswindow/level-swift.struct, 2024.                                    CODASPY, 2023.
[76] J. Fisher, “What is the order of nswindow levels?” https://jameshfisher.             [103] J. S. Shapiro, J. Vanderburgh, E. Northup, and D. Chizmadia,
     com/2020/08/03/what-is-the-order-of-nswindow-levels/, 2020.                                “Design of the eros Trusted Window System,” 2004. [Online].
[77] X. Lin, P. Ilia, and J. Polakis, “Fill in the blanks: Empirical analysis                   Available: https://www.usenix.org/conference/13th- usenix- security-
     of the privacy threats of browser form autofill,” in Proceedings of the                    symposium/design-eros-trusted-window-system
     2020 ACM CCS.                                                                        [104] J. Epstein, J. McHugh, R. Pascale, C. Martin, D. Rothnie, H. Orman,
[78] 1Password Support, “Save and fill credit cards and addresses,” https:                      A. Marmor-Squires, M. Branstad, and B. Danner, “Evolution of a
     //support.1password.com/credit- card- address- filling, accessed: 2025-                    trusted B3 window system prototype,” in 1992 IEEE Computer Society
     04-12.                                                                                     Symposium on Research in Security and Privacy.
[79] D. M’Raihi, J. Rydell, M. Pei, and S. Machani, “TOTP: Time-Based                     [105] F. Roesner and T. Kohno, “Securing Embedded User Interfaces: An-
     One-Time Password Algorithm,” Internet Engineering Task Force,                             droid and Beyond,” in USENIX Security Symposium ’13, 2013.




                                                                                     16
[106] A. Bianchi, J. Corbetta, L. Invernizzi, Y. Fratantonio, C. Kruegel, and                                     Hider.app
      G. Vigna, “What the App is That? Deception and Countermeasures in                                             Contents
      the Android User Interface,” in 2015 IEEE S&P.
[107] Y. Lee, X. Wang, K. Lee, X. Liao, X. Wang, T. Li, and X. Mi, “Un-                                               Malicious.app

      derstanding iOS-based Crowdturfing Through Hidden UI Analysis,” in                                                 Contents
      USENIX Security Symposium ’19.
                                                                                                                                    apps.json            Info.plist
[108] Q. A. Chen, Z. Qian, and Z. M. Mao, “Peeking into Your App without                                                                         s


      Actually Seeing It: UI State Inference and Novel Android Attacks,” in                                                             Malicious.app Resources
      23rd USENIX Security Symposium (USENIX Security ’14).
[109] M. Jubur, P. Shrestha, N. Saxena, and J. Prakash, “Bypassing Push-
      based Second Factor and Passwordless Authentication with Human-                                                                  Hider.app Resources
      Indistinguishable Notifications,” in ACM AsiaCCS ’21.
[110] S. Aonzo, A. Merlo, G. Tavella, and Y. Fratantonio, “Phishing Attacks
      on Modern Android,” in Proceedings of the 2018 ACM CCS.
[111] A. T. Mahdad, M. Jubur, and N. Saxena, “Breaching Security Keys                    Fig. 3: Alert window.      Fig. 4: Phishing app structure.
      without Root: FIDO2 Deception Attacks via Overlays exploiting Lim-
      ited Display Authenticators,” in ACM CCS ’24.
[112] K. Cheng, A. Bhattacharya, M. Lin, J. Lee, A. Kumar, J. F. Tian,                 in red: apps.json and Info.plist. The apps.json
      T. Kohno, and F. Roesner, “When the user is inside the user interface:           file contains a predefined list of target applications and their
      An empirical study of ui security properties in augmented reality,” in
      33rd USENIX Security Symposium (USENIX Security ’24).                            corresponding configurations, such as window titles or Bundle
[113] F. Xiao, Z. Yang, J. Allen, G. Yang, G. Williams, and W. Lee,                    Display Names. The phishing application uses this file to
      “Understanding and Mitigating Remote Code Execution Vulnerabilities              identify which credentials to harvest from Keeper’s vault.
      in Cross-platform Ecosystem,” in Proceedings of the 2022 ACM CCS.
[114] M. M. Ali, M. Ghasemisharif, C. Kanich, and J. Polakis, “Rise of                 The Info.plist file stores essential metadata about the
      Inspectron: Automated Black-box Auditing of Cross-platform Electron              application, including its Bundle Display Name. By modifying
      Apps,” in USENIX Security Symposium ’24.                                         this file, the attacker can impersonate trusted applications,
[115] C. Paloscia, K. Solomos, M. M. Ali, and J. Polakis, “Lost in translation:
      Exploring the risks of web-to-cross-platform application migration,”
                                                                                       effectively bypassing Keeper’s verification checks.
      Proceedings on Privacy Enhancing Technologies, 2025.
[116] Z. Jin, S. Chen, Y. Chen, H. Duan, J. Chen, and J. Wu, “A Security               C. Vault Integrity
      Study about Electron Applications and a Programming Methodology
      to Tame DOM Functionalities,” in Proceedings 2023 Network and                       We detected an additional design flaw in 1Password’s cre-
      Distributed System Security Symposium, 2023.                                     dential association process on macOS. The application links
[117] M. M. Ahmadpanah, D. Hedin, M. Balliu, L. E. Olsson, and
      A. Sabelfeld, “SandTrap: Securing JavaScript-driven Trigger-Action
                                                                                       credential records to Bundle IDs based solely on the presence
      Platforms,” in USENIX Security Symposium ’21.                                    of a code signature, even when that signature is invalid or
[118] C. Wang, Y. Zhang, and Z. Lin, “RootFree Attacks: Exploiting Mobile              untrusted. Specifically, 1Password establishes an association
      Platform’s Super Apps From Desktop,” in ACM AsiaCCS ’24.
[119] J. Bonneau, C. Herley, P. C. v. Oorschot, and F. Stajano, “The Quest to
                                                                                       between a credential record and a Bundle ID upon verifying
      Replace Passwords: A Framework for Comparative Evaluation of Web                 the presence of a Code Signature. Notably, this association
      Authentication Schemes,” in 2012 IEEE S&P.                                       is created even if subsequent verification checks fail, such as
[120] Z. Li, W. He, D. Akhawe, and D. Song, “The Emperor’s New Password
      Manager: Security Analysis of Web-based Password Managers,” in
                                                                                       assessing the validity of the signature. To evaluate the security
      USENIX Security Symposium ’14.                                                   implications of this behavior, we tested a scenario involving
[121] S. Oesch and S. Ruoti, “That Was Then, This Is Now: A Security                   credentials for a legitimate service that had not yet been used
      Evaluation of Password Generation, Storage, and Autofill in Browser-
      Based Password Managers,” in USENIX Security ’20.
                                                                                       for autofill in the corresponding legitimate application. We
[122] A. Fabrega, A. Namavari, R. Agarwal, B. Nassi, and T. Ristenpart,                verified that an attacker could exploit this mechanism by trick-
      “Exploiting Leakage in Password Managers via Injection Attacks,” in              ing a user into installing a malicious application. When the
      USENIX Security ’24.
                                                                                       user attempts to autofill credentials for the legitimate service,
                                A PPENDIX                                              1Password verifies that the malicious application includes a
                                                                                       valid Code Signature and subsequently associates the service’s
A. Password Manager Notifications Examples                                             credentials with the malicious app’s Bundle ID. However, in its
   Figure 3 shows the alert displayed when a credentials set is                        subsequent validation steps, 1Password detects that the Code
selected from the Quick Access window.                                                 Signature is either untrusted or unverified and blocks autofill
                                                                                       into the malicious application. Although this validation pre-
B. Keeper: Phishing Application Structure                                              vents immediate credential exfiltration, it introduces a flaw, as
   Figure 4 illustrates the internal structure of the phish-                           once the association between the credentials and the malicious
ing application used to exploit Keeper’s vault. The outer                              Bundle ID is established, 1Password subsequently blocks any
wrapper, named Hider.app, serves as a benign-looking                                   attempt to update the association when the user attempts to
macOS application designed to conceal the embedded mali-                               autofill the same credentials into the legitimate application.
cious component. Within Hider.app, a nested application                                This results in a persistent Denial of Service (DoS) condition,
(Malicious.app) contains the core functionality responsi-                              effectively preventing users from accessing their credentials
ble for credential harvesting. Both applications follow the stan-                      within the intended, legitimate application. While this issue
dard macOS app bundle structure, with the Contents folder                              is not part of our credential stealing attack, nonetheless it
that holds essential files and directories required for execution.                     presents an additional design flaw in 1Password’s verification
The Malicious.app includes two critical files, highlighted                             workflow.



                                                                                  17
TABLE IV: Default and user-defined autofill shortcuts in                 TABLE V: Average time to infer KeePassXC’s autofill shortcut
macOS password managers.                                                 per phase (avg across five iterations).
             (a) Default password manager shortcuts.
                                                                               Shortcut Set Tested                  Avg. Time (s)
  Shortcut                       Password Manager                              Default manager shortcuts            10.54
   Cmd + \                       1Password, Dashlane, Enpass                   Common user-defined shortcuts        21.12
                                                                               Special key-based combinations       99.75
   Cmd + Shift + L               Bitwarden
   Cmd + Shift + Space           LastPass
                                                                          Algorithm 2: Shortcut inference for KeePassXC.
   Cmd + Shift + U               Keeper
   Cmd + Shift + X               NordPass
                                                                           Input: commonDefaultShortcuts,
                                                                                   commonUserDefinedShortcuts
   Cmd + Shift + P               RoboForm
                                                                           Output: Detected autofill shortcut
   Cmd + Shift + M               MacPass
                                                                         1 foreach (primaryKey, modifierKeys) in
                     (b) User-defined shortcuts.                            commonDefaultShortcuts →
                                                                            commonUserDefinedShortcuts do
      Shortcut                                                           2     Trigger modifierKeys + primaryKey
       Cmd + /             Cmd + .            Cmd + ,                    3 primaryKeys ↑ extract all unique keys from prior sets
                                                                            modCombos ↑ {CTRL, CTRL+SHIFT,
       Cmd + ‘              Cmd + ’           Cmd + D
                                                                            CTRL+OPTION, CTRL+SHIFT+OPTION}
       Cmd + Return                                                      4 foreach key in primaryKeys do
                                                                         5     foreach mods in modCombos do
                                                                         6         Trigger mods + key
D. Linux Password Managers
   For Linux systems, we applied the techniques outlined
in §IV and §V to evaluate the availability and behavior of
autofill functionality in desktop password managers. Among               E. KeePassXC: Inferring the Autofill Shortcut
the evaluated password managers, 1Password and KeePassXC                    Unlike other password managers, KeePassXC does not
offer native Linux desktop applications, while Keeper pro-               define a default autofill shortcut. Consequently, successful
vides limited functionality, and LastPass does not support the           credential harvesting requires an attacker to infer the user’s
platform. The 1Password client does not implement autofill               configured keyboard shortcut. Exhaustive brute-force across
on Linux but provides a Quick Access interface, allowing                 all potential combinations is not practical due to the high
users to copy credentials to the clipboard via keyboard short-           number of permutations. To address this, we develop a shortcut
cuts. As previously assessed in §IV-A, this interface can be             inference strategy that prioritizes realistic configurations based
manipulated by a malicious application to extract credentials            on common user behavior and commonly deployed shortcuts.
through automated interaction. We replicated this attack on                 Our method proceeds in three phases. First, it tests the
Linux and confirmed its effectiveness. Similarly, KeePassXC              default autofill shortcuts used by other popular password
supports autofill functionality, and we confirmed that creden-           managers, as shown in Table IVa, under the assumption that
tial injection can be programmatically triggered. However,               users may reuse familiar key bindings. Second, it creates a set
in both cases, OS-level constraints on Linux significantly               of user-defined shortcuts commonly recommended in online
limit the stealthiness of such attacks. Specifically, Linux lacks        discussions and documentation and user guides (Table IVb).
a privileged UI layer—such as the screen-saver level                     Finally, it expands the search space by pairing frequently used
available on macOS—that could be used to obscure the attack              primary keys with combinations of modifier keys such as
interface.                                                               Control, Option, and Shift. Algorithm 2 outlines our
   Additionally, the Linux window manager prevents appli-                inference methodology.
cations from positioning windows outside the visible screen                 We evaluate the effectiveness of each phase independently
boundaries. We also tested workspace-based hiding strategies,            by measuring the average completion time over five iterations,
but triggering either the Quick Access or autofill interface             as shown in Table V. Testing default manager shortcuts
causes it to appear in the user’s current workspace. Although            completes in 10.5 seconds on average, and represents the most
automated credential extraction is technically feasible, stealthy        efficient phase due to its low overhead. The user-defined subset
exploitation under default Linux configurations is impractical.          completes in ↓20 seconds. The final phase, which explores
Finally, the Keeper desktop application does not support                 a broader space of modifier-key combinations, completes in
autofill on Linux and is therefore not susceptible to the class          under 100 seconds. These results confirm the practicality of
of attacks explored in this work. LastPass does not provide              the default-only phase for credential harvesting, while also
a Linux desktop application and is thus excluded from our                highlighting that exhaustive exploration of complicated input
evaluation.                                                              combinations remains possible within a short time window.



                                                                    18
