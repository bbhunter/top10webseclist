---
type: Slides
title: Abusing Intended Feature And Bypassing Facial Recognition
description: "An app's signup requires a live face-detection step, with only two criteria: the face must be human and looking straight ahead. Testing shows a physical photograph held to the camera blurs and is rejected, but a deepfake image supplied through the app's own intended gallery-import feature satisfies both criteria and passes, so anyone can verify as the account holder without ever being in front of the camera."
resource: "https://docs.google.com/presentation/d/16mvSEvpnNYrYcJe4XA_Nwd9OwEuf4UTE/edit?usp=sharing&ouid=101230982661442785272&rtpof=true&sd=true"
tags: [slides, webseclist-reference, abuse-of-functionality, auth-bypass, bug-bounty, case-study, owasp-a01-2021, owasp-a04-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T15:11:54+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "https://docs.google.com/presentation/d/16mvSEvpnNYrYcJe4XA_Nwd9OwEuf4UTE/edit?usp=sharing&ouid=101230982661442785272&rtpof=true&sd=true"
    title: Abusing Intended Feature And Bypassing Facial Recognition
    author: Ishwar Kumar
also_at: []
authors:
  - Ishwar Kumar
canonical_url: ""
cited_by:
  - "2024.md:39"
commit: ""
content_sha256: 6d58f5f9757489fbb861c44db22012f09c8c482c3308268168c89d63058746c6
depth: full
depth_reason: default
kind: slides
language: ""
licence: unknown
original_url: "https://docs.google.com/presentation/d/16mvSEvpnNYrYcJe4XA_Nwd9OwEuf4UTE/edit?usp=sharing&ouid=101230982661442785272&rtpof=true&sd=true"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 03adb6c9095b3064e11e43fc65afe52886c2d4cf4f800c8b290034fa922351b5
retrieved_from: "https://docs.google.com/presentation/d/16mvSEvpnNYrYcJe4XA_Nwd9OwEuf4UTE/edit?usp=sharing&ouid=101230982661442785272&rtpof=true&sd=true"
retrieved_kind: manual-import
retrieved_utc: "2026-08-14T15:11:54+00:00"
slug: abusing-intended-feature-bypassing-facial-recognition
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Abusing Intended Feature And Bypassing Facial Recognition

**Abusing Intended Feature And Bypassing Facial Recognition** - Ishwar Kumar, Publisher not stated.

- Published: date not stated
- Original: <https://docs.google.com/presentation/d/16mvSEvpnNYrYcJe4XA_Nwd9OwEuf4UTE/edit?usp=sharing&ouid=101230982661442785272&rtpof=true&sd=true>
- Preserved from: https://docs.google.com/presentation/d/16mvSEvpnNYrYcJe4XA_Nwd9OwEuf4UTE/edit?usp=sharing&ouid=101230982661442785272&rtpof=true&sd=true (manual-import) on 2026-08-14
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Abusing Intended Feature And Bypassing Facial Recognition.pptx

Abusing Intended Feature And
 Bypassing Facial Recognition



          Author – Ishwar Kumar
             TenguCon 2024
                 $ WHOAMI $

• Aspiring Security Researcher
• Bug Bounty Hunter
• CTF Player
• Uni Student @Comp.Sci.Eng.
• Ranked Top15 researcher @NCIIPC
APPLICATION USES A.I. ? COOL ☺
• The application uses Artificial Intelligence to map out the face of any particular user from the
  group photos

• Automatically find and categorize user images based on their face.

• Saves time by eliminating the need for manual photo searching.
              USER SIGNUP WITH MOBILE/EMAIL




             VERFIY WITH OTP (ONE TIME PASSWORD)




         VERIFY & PASS LIVE FACE DETECTION FEATURE




AFTER BEING VERIFED SUCESSSFULLY YOU WILL BE REDIRECTED TO HOMEPAGE
 Cannot be skipped and is necessary
to complete in order to move forward
Face Detection Criteria Being Used:
1. The face should be of a human.

 2. The human face should be looking
 straight.
Something seems odd in here ?
Yes, it is flawed but what it is ? ☺
1. A.I. fails to detect the difference between a real
      live detected human face and another
                       deepfake.

2. Fulfilling the above two conditions anyone can
  simply import the picture and verify his/her
identity and bypass this crucial step of security.
Testing Various Bypass Methods
• Conducted a test with a physical photograph, it got blur
       and ended up being detected & rejected.


   • Used a deepfake Image from the Intended feature
     (Imported from gallery) and it bypassed the check
The deepfake Image I used to bypass the
  security check and got successfully
          verified as the user
WRITE UP FOR THE VULNERABILITY DISCUSSED
     ANY QUESTIONS ?
REACH ME OUT AT TWITTER - @RAVENZBB
