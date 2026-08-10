---
type: Article
title: CAPTCHA Hax With TesserCap
resource: "https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html"
tags: [article, webseclist-reference, en, gursevkalra-blogspot-com]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T01:14:17+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html"
    title: CAPTCHA Hax With TesserCap
  - id: capture
    resource: "https://web.archive.org/web/20121101144941/https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html"
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2011.md:12"
commit: ""
content_sha256: 237d94d038b76911e1003349804089c89952a28331b2a2dd17c9f38550fad9a6
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html"
published: ""
publisher: gursevkalra.blogspot.com
publisher_english: ""
raw_sha256: 7d633dc86617006a85a40c436375c884cb774b184028e55cdb965b19e61582f7
retrieved_from: "https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html"
retrieved_kind: live
retrieved_utc: "2026-08-09T01:14:17+00:00"
slug: gursevkalra-blogspot-com-random-security-captcha-hax-tessercap
snapshot: 20121101144941
title_english: ""
translation_file: ""
translation_of: ""
---

# CAPTCHA Hax With TesserCap

**CAPTCHA Hax With TesserCap** - Author not stated, gursevkalra.blogspot.com.

- Published: date not stated
- Original: <https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html>
- Preserved from: https://gursevkalra.blogspot.com/2011/11/captcha-hax-with-tessercap.html (live) on 2026-08-09
- Capture timestamp: 20121101144941
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

This blog post was voted as 8th best in [Top 10 Web Hacking Techniques of 2011](https://blog.whitehatsec.com/vote-now-top-ten-web-hacking-techniques-of-2011/) poll*.*

 With the goal of creating a tool that can help security professionals and developers to test their CAPTCHA schemes, I conducted a research on over 200 high traffic websites and several CAPTCHA service providers listed on [Quantcast’s Top 1 Million Ranking Websites](http://www.quantcast.com/top-sites-1).

 During the same time frame, students at the Stanford University also conducted a similar [research (PDF)](http://cdn.ly.tl/publications/text-based-captcha-strengths-and-weaknesses.pdf). Both research works concluded the obvious:

 **An alarming number of CAPTCHAs schemes are vulnerable to automated attacks.**

 I looked around, tested and zeroed in on Tesseract-OCR as my OCR engine. To remove color complexities, spatial irregularities, and other types of random noise from CAPTCHAs, I decided to write my own image preprocessing engine. After a few months of research, coding and testing in my spare time, TesserCap was born and is ready for release now.

 TesserCap is a GUI based, point and shoot CAPTCHA analysis tool with the following features:

- A generic image preprocessing engine that can be configured as per the CAPTCHA type being analyzed.
- Tesseract-OCR as its OCR engine to retrieve text from preprocessed CAPTCHAs.
- Web proxy support
- Support for custom HTTP headers to retrieve CAPTCHAs from websites that require cookies or special HTTP headers in requests
- CAPTCHA statistical analysis support
- Character set selection for the OCR Engine

 An example TesserCap image preprocessing and run on Wikipedia (Wikimedia’s Fancy CAPTCHA) is shown below:

 [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpj6vnjbvGiBSxoYeHWxndVfrmcRRDxY0cG3AHciMszEn_gE1Y8BmfzYWDyx2kZ_oiGmMl2XJegx3mwsQxY7KDnTpG20E9e0yI7pUrPd4WtzeSjp6qSwYVUw8w3Y_aKsMcrcvfXQPZlSA/s320/p1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpj6vnjbvGiBSxoYeHWxndVfrmcRRDxY0cG3AHciMszEn_gE1Y8BmfzYWDyx2kZ_oiGmMl2XJegx3mwsQxY7KDnTpG20E9e0yI7pUrPd4WtzeSjp6qSwYVUw8w3Y_aKsMcrcvfXQPZlSA/s1600/p1.png)

#  Downloads

 TesserCap and it's user manual can be downloaded from one of the following locations:

- [http://www.opensecurityresearch.com/files/tessercap.zip](http://www.opensecurityresearch.com/files/tessercap.zip) -- No password protection on this zip file
- [http://www.mcafee.com/us/downloads/free-tools/tessercap.aspx](http://www.mcafee.com/us/downloads/free-tools/tessercap.aspx) -- Use password as "foundstone" without quotes to extract this zip file.

#  Results

 The two tables below summarize the CAPTCHA analysis performed using TesserCap for few popular websites and some CAPTCHA service providers. All these tests were performed using TesserCap’s image preprocessing module and Tesseract-OCR’s default training data.

|  **Website** |  **Accuracy*** |  **Quantcast Rank** |   |
|  wikipedia |  20-30% |  7 |   |
|  ebay |  20-30% |  11 |   |
|  reddit.com |  20-30% |  68 |   |
|  CNBC |  50+% |  121 |   |
|  foodnetwork.com |  80-90% |  160 |   |
|  dailymail.co.uk |  30+% |  245 |   |
|  megaupload.com  |  80+% |  1000 |   |
|  pastebin.com |  70-80% |  32,534 |   |
|  cavenue.com |  80+% |  149,645 |   |

|  **CAPTCHA Provider** |  **Accuracy*** |   |
|  captchas.net |  40-50% |   |
|  opencaptcha.com |  20-30% |   |
|  snaphost.com |  60+% |   |
|  captchacreator.com |  10-20% |   |
|  www.phpcaptcha.org |  10-20% |   |
|  webspamprotect.com |  40+% |   |
|  ReCaptcha |  0% |   |

 *This accuracy maybe further increased by training the Tesseract-OCR engine for the CAPTCHAs under test.

##  Wikipedia

 [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgazLc-ZHQx6cIieFTw1ZPqAeXY68tlBx-olwcdUBzxSiYKEIUUEjcgfGyZrDaFD5ZHZ6PUOy1Trh2LQCHjv1n-lRFMTDR1VMClo10EVC2kpgNbYR7FE_ubS5R410ZuViKD64-t35vQwC8/s320/p2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgazLc-ZHQx6cIieFTw1ZPqAeXY68tlBx-olwcdUBzxSiYKEIUUEjcgfGyZrDaFD5ZHZ6PUOy1Trh2LQCHjv1n-lRFMTDR1VMClo10EVC2kpgNbYR7FE_ubS5R410ZuViKD64-t35vQwC8/s1600/p2.png)

##  OpenCaptcha Preprocessing

 [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQpFzMXPnZ-S0xmQ_qODT5-H1uHILGUglLs_cSkx-2MZZ-Khq77hM-ozhpC3ZI5rdpvSzjLi_Zvi2-xFRWbrqqCJZlt0XzIZbEeHMMDIOI95FyC8FI1Z61uisZLoplQ-cwECDBuq06RK8/s320/p3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQpFzMXPnZ-S0xmQ_qODT5-H1uHILGUglLs_cSkx-2MZZ-Khq77hM-ozhpC3ZI5rdpvSzjLi_Zvi2-xFRWbrqqCJZlt0XzIZbEeHMMDIOI95FyC8FI1Z61uisZLoplQ-cwECDBuq06RK8/s1600/p3.png)

##  OpenCaptcha Sample Run

 [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinXf1EekU6o-UlgGzCRAexQBLjRZSnU61elvfIpuIdzwwxApI6KJ0Ndty2jjKwsuYbS17bcd9HzLgXzoXaChHr2DXM6CuXoLm-vc1fK_SHMhktUd0P6sH7UEd2KpW-IXpEi9eIc-eAvrk/s320/p4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinXf1EekU6o-UlgGzCRAexQBLjRZSnU61elvfIpuIdzwwxApI6KJ0Ndty2jjKwsuYbS17bcd9HzLgXzoXaChHr2DXM6CuXoLm-vc1fK_SHMhktUd0P6sH7UEd2KpW-IXpEi9eIc-eAvrk/s1600/p4.png)

##  Reddit

 [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnyru4oi0Xk67ieHrKuyQFndqAQ2tjQjKTh2a8QkWydlKbEOL4gsGJPq7w4GEuSGoqj6yA031WNouap7-7ipiNJoOhynkackJy1HHip7YZ8Fl8c2C5pMF_NKy7IcOWbJ-ZST3a0iNwAEU/s320/p5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnyru4oi0Xk67ieHrKuyQFndqAQ2tjQjKTh2a8QkWydlKbEOL4gsGJPq7w4GEuSGoqj6yA031WNouap7-7ipiNJoOhynkackJy1HHip7YZ8Fl8c2C5pMF_NKy7IcOWbJ-ZST3a0iNwAEU/s1600/p5.png)

##  eBay

 [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPBfJCFQybuQzVHMQLvi8l5jQSPOy-IcQ3ArXj62nN9x1wfS3flziJKu5dkwJNpkyd5SNipbIukh8285EK7hcDDRat6EEpZkUpSmvME9YSEuF_HhpD-qzCguI_mPAysyJ4M80nVljgGl8/s320/p6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPBfJCFQybuQzVHMQLvi8l5jQSPOy-IcQ3ArXj62nN9x1wfS3flziJKu5dkwJNpkyd5SNipbIukh8285EK7hcDDRat6EEpZkUpSmvME9YSEuF_HhpD-qzCguI_mPAysyJ4M80nVljgGl8/s1600/p6.png)
