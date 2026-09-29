---
type: Slides
title: Illuminating the Security Issues with Lights-Out Server Management (Slides)
description: "The original conference slide deck presents the accompanying paper's mechanisms and experiments. Demonstrates an unauthenticated stack overflow in a management-controller login CGI that yields root on the BMC. Firmware reuse, weak randomization and missing hardening broaden the concern beyond the tested device. Exposure measurements estimate affected systems; the authors did not exploit the Internet hosts they counted."
resource: "https://www.usenix.org/sites/default/files/conference/protected-files/bonkoski_woot13_slides.pdf"
tags: [slides, webseclist-reference, usenix, rce, memory-corruption, case-study]
generated:
  by: webseclist-refs/1
  at: "2026-09-29T21:07:41+00:00"
status: stable
stale_after: 2027-09-29
sources:
  - id: original
    resource: "https://www.usenix.org/sites/default/files/conference/protected-files/bonkoski_woot13_slides.pdf"
    title: Illuminating the Security Issues with Lights-Out Server Management (Slides)
    author: Anthony J. Bonkoski, J. Alex Halderman
    last_modified: 2013
also_at: []
authors:
  - Anthony J. Bonkoski
  - J. Alex Halderman
canonical_url: ""
cited_by:
  - "2013.md:67"
commit: ""
content_sha256: e792c314aca2455f528b3092cfe8d73abf3ea6fdb04d391f95b2a9ebb2b9e0ca
depth: full
depth_reason: default
kind: slides
language: ""
licence: unknown
original_url: "https://www.usenix.org/sites/default/files/conference/protected-files/bonkoski_woot13_slides.pdf"
published: 2013
publisher: USENIX
publisher_english: ""
raw_sha256: 5c49017cf4abab344a9587795ae495b53b26e0777e96fa3085f307071d459bc0
retrieved_from: "https://www.usenix.org/sites/default/files/conference/protected-files/bonkoski_woot13_slides.pdf"
retrieved_kind: manual-import
retrieved_utc: "2026-09-29T21:07:41+00:00"
slug: 2013-usenix-illuminating-security-issues-lights-out-server-management-slides
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Illuminating the Security Issues with Lights-Out Server Management (Slides)

**Illuminating the Security Issues with Lights-Out Server Management (Slides)** - Anthony J. Bonkoski, J. Alex Halderman, USENIX.

- Published: 2013
- Original: <https://www.usenix.org/sites/default/files/conference/protected-files/bonkoski_woot13_slides.pdf>
- Preserved from: https://www.usenix.org/sites/default/files/conference/protected-files/bonkoski_woot13_slides.pdf (manual-import) on 2026-09-29
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so
it remains readable if the page goes offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Illuminating the Security Issues with
      Lights-Out Server Management

Anthony J. Bonkoski                        J. Alex Halderman
                  University of Michigan
       What is IPMI?

       Need to manage a massive cluster of servers?              OEM Names:
        OS installs, monitoring, power-cycle, etc.
                                                                 HP iLo
        How?
                                                                 Dell iDrac
                                                                 Oracle iLOM
        Intel introduces Intelligent Platform
                                                                 Lenovo/IBM IMM
        Management Interface (IPMI) Specification:
                                                                 SuperMicro IPMI
          Adds a second computer
          Always on                                              ATEN IPMI
          Integrated directly into the system buses (e.g. I2C)   MegaRAC
                                                                 Avocent IPMI




Image Copyright: Ulfbastel, License: GFDL 1.2+/CC BY-SA 3.0
       What is IPMI?

       Baseboard Management Controller (BMC)
         The embedded micro-controller: the second CPU




Image Copyright: U. Vezzani, License: CC BY-SA 3.0
Typical IPMI Implementation

System
Embedded on Motherboard or Expansion card
CPU: ARM/MIPS or other low power embedded CPU
OS: Linux is common


Extra OEM Features
Remote Virtual Console
Remote Media
High network connectivity incl. HTTP and SSH.
Why do we care?

In short: IPMI is the perfect spying backdoor
 Always on and often pre-enabled.
 NIC failover*
 Powerful Remote Tools
 Widespread deployment: 100,000+ on public IPs

It’s an embedded system...
 ...often, security is an after-thought!




*As seen on our SuperMicro ATEN-based IPMI
  Known Problems

  Authentication Risks:
  Many vendors ship default passwords
       root/calvin†
  Anonymous undocumented accounts*
  Passwords stored in plain-text*




* SuperMicro ATEN-based IPMI
† Dell iDRAC
Recent Developments

Dan Farmer
 January 2013: Starts publicly denouncing IPMI
 Criticisms are largely just conjectures

 Finds some negligent flaws:
  Hidden backdoor debugging web page on Dell iDRAC
  Could gain root over ssh
Our Work




 Is IPMI security actually a problem?
 Supermicro IPMI

Supermicro SYS-5017C-LF

                                             IPMI Firmware by
                                             ATEN Technology


                                             HTML /               CGI
                                            JavaScript     (written in C)



                                                   Linux 2.6.17

                                            Firmware version 1.86
                                            (build date: 11-14-2012)


                          Nuvoton WPCM450
                          ARM-based BMC
Supermicro Web Interface
   Supermicro SSH Interface

 Backend: Highly modified fork of Dropbear
 Frontend: Systems Management Architecture for Server Hardware Command-
 Line Protocol (SMASH)*
 Notice: a system admin has no access to underlying Unix shell




*Distributed Management Task Force (DMTF) specification: dmtf.org/standards/smash
Reverse Engineering Approach

Fetch firmware from OEM website.
Scan and unpack: binwalk




Mount filesystems
Objdump and IDA Pro
What to Look For?


Begin with Classics:
1. Insecure Input Validation
2. Shell Injection
3. Buffer Overflows
Input Validation

All input validation is done in client-side javascript ...
… and so is permission checking:
  function PrivilegeCallBack(Privilege){
      // full access
      if(Privilege == '04'){
          isSuperUser = 1;
      }
      // only view
      else if(Privilege == '03') {
          var_save_btn.disabled = true;
      }                                    Server-side?
      // no access
                                           No permission checking.
      else {
          alert(lang.LANG_NOPRIVI);        No escaping of input passed to shell.
      }                                    No string length checking in CGI.
  }
Shell Injection

15 of 67 CGI programs made calls to system().
Confirmed shell injection in config_date_time.cgi:
Shell Injection

15 of 67 CGI programs made calls to system().
Confirmed shell injection in config_date_time.cgi:



Getting command output
   Redirect to /nv/system_log.
   Issue GET request to system_log.cgi.


Create a psuedo-terminal
 Wraps GET ands POST request in a python script.
root@localhost #
Buffer Overflows

Server backend:
 … CGI programs.
 … written in C.
 … running as root.
Buffer Overflows

Server backend:       // login.cgi
 … CGI programs.      int main(void)
                      {
 … written in C.        char name[128], pwd[24];
 … running as root.     char *temp ;
                        // ... initialize ...
                        temp = cgiGetVariable("name");
                        strcpy(name, temp);
                        temp = cgiGetVariable("pwd");
                        strcpy(pwd, temp);
                        // ... authenticate user ...
                      }
Buffer Overflows

Server backend:       // login.cgi
 … CGI programs.      int main(void)
                      {
 … written in C.        char name[128], pwd[24];
 … running as root.     char *temp ;
                        // ... initialize ...
                        temp = cgiGetVariable("name");
                        strcpy(name, temp);
                        temp = cgiGetVariable("pwd");
                        strcpy(pwd, temp);
                        // ... authenticate user ...
                      }
Buffer Overflows

No length validation?
Buffer Overflows

No length validation?
Buffer Overflows

No length validation?
Buffer Overflow Exploitability

Buffer-overflow defenses?
No DEP (Stack and Heap are executable).
No Stack Canaries.
Limited ASLR.
   (Stack/Heap base addresses are randomized, but
    dynamic libraries are not. Return-to-libc works.)
Exploitation Challenges

Stack is randomized (ASLR).
   ...but, only 12 bits are random. Just 4096 possibilities.

We gain control on the return from main().
   Stack is small: shellcode must be compact.


BMC crashes and reboots if pounded too hard with requests.
Buffer Overflow Exploit

Solutions
Store the shell command in the name buffer.
Brute force through the stack randomization.
Limit the time between brute-force iterations.
    Avg. search time: ~7 min.


Payload
Fetch (wget) and install modified SSH daemon.
Forks root shell on incorrect password.
    Only 2 instructions changed!
root@localhost #
Vulnerable Models?

Cursory check of all Supermicro IPMI firmware
downloads as of May 23, 2013.
   30 of 64 images appear vulnerable.
   135 device models.

Supermicro says they’re working on a fix.

Possibly affects other ATEN-based products.
The Impact




So, rooting this device is easy!
But, what are the implications?

Yet another broken embedded system?
The Impact



Only as secure as our weakest component.
Entire system is now vulnerable!
Adding an entire computer only weakens.
IPMI for Evil

BMC-based spyware and botnets
Rooted BMC → Rooted host system
  Mount a custom OS and reboot.

Rooted host system → Rooted BMC
   Re-flash the BMC with malicious code.

BMC rootkits
   A backdoor that survives potentially forever.

A scary thought
   IPMI meets Matrix → Is your IPMI just emulated? How do you know?
    Network Measurements

    Scanned all public IPs on May 7, 2013 using ZMap*.
    Downloaded all X.509 certs from HTTPS servers.
    Used identifying characteristics of default certificates.†

                                                                       Could root
                                                                       all these in
                                                                       parallel in
                                                                        minutes!




* ZMap: Fast Internet-wide Scanning and its Security Applications.
  Paper and tool coming this FRIDAY at Usenix Security.
† Details on “identifying characteristics” may be found in our paper
Defenses

For System Operators
Never attach your IPMI device directly to the Internet.
 Use an isolated management network or VLAN.

Change default passwords and certificates.
Disable IPMI if you don’t need it.
Unfortunately: we’re at the will of the Vendor
Defenses

For IPMI Vendors
These are textbook vulns. You have to do better.
Apply security engineering practices.
Sign and verify firmware when flashing.
Make devices hard to deploy on public IPs.
Lessons

                A Culture Clash?


     Embedded                              Internet




                IPMI: hopefully a climax
Future Work

Analysis of other vendors’ implementations
Dell, HP, Lenovo, Oracle, etc.


Firmware update exploitation
Can an attacker inject a backdoor that persists?
Across BMC reboot? Across BMC flashes? Forever?


IPMI honeypot
Unclear whether attackers are exploiting these devices in the wild.
Some anecdotal evidence of their use as spambots.
Are they being used for other malicious purposes?
Conclusions

IPMI serves a vital role for system management.
Carries elevated risks, potential for powerful attacks.
At least some vendors are getting it badly wrong.
Farmer is correct: IPMI is a serious concern.
Our work: A call to arms .
   Illuminating the Security Issues with
      Lights-Out Server Management

Anthony J. Bonkoski                      J. Alex Halderman
abonkosk@umich.edu                        jhalderm@umich.edu
                     University of Michigan
Zmap Scan Details


 Vendor         Identifying Characteristics

 SuperMicro     Subjects containing “linda.wu@supermicro.com” or “doris@aten.com.tw”

 Dell           Subject containing iDRAC

 HP             Subjects containing “CN=ILO” and issuers containing “iLO3 Default Issuer”
                or “Hewlett Packard”

 *Landing pages spot-checked for false positives
