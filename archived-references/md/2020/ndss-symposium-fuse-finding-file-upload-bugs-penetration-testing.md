---
type: Article
title: "FUSE: Finding File Upload Bugs via Penetration Testing"
description: "FUSE mutates file upload requests so they pass a web application's content-filtering checks while preserving the uploaded file's execution semantics, exposing unrestricted file upload and unrestricted executable file upload bugs. Across 33 real PHP applications it found 30 previously unreported remote code execution flaws, 15 of which received CVEs."
resource: "https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/"
tags: [article, webseclist-reference, en, ndss-symposium, file-upload, rce, filter-bypass, php, fuzzing, dynamic-analysis, tooling, cve]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:43:41+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/"
    title: "FUSE: Finding File Upload Bugs via Penetration Testing"
    author: Taekjin Lee, Seongil Wi, Suyoung Lee, Sooel Son
also_at:
  - "https://www.ndss-symposium.org/wp-content/uploads/2020/02/23126-paper.pdf"
authors:
  - Taekjin Lee
  - Seongil Wi
  - Suyoung Lee
  - Sooel Son
canonical_url: ""
cited_by:
  - "2020.md:77"
commit: ""
content_sha256: e2669561c46f43b83db56e6764d5ee261ec71f86bd1dfbac2c65ff470a5cbb54
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/"
published: ""
publisher: NDSS Symposium
publisher_english: ""
raw_sha256: e598aa48f20b92f87bbb497da4c17cc8d1e8f1f4fb582be4c774534064b092e5
retrieved_from: "https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:43:41+00:00"
slug: ndss-symposium-fuse-finding-file-upload-bugs-penetration-testing
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# FUSE: Finding File Upload Bugs via Penetration Testing

**FUSE: Finding File Upload Bugs via Penetration Testing** - Taekjin Lee, Seongil Wi, Suyoung Lee, Sooel Son, NDSS Symposium.

- Published: date not stated
- Original: <https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/>
- Also published at: <https://www.ndss-symposium.org/wp-content/uploads/2020/02/23126-paper.pdf>
- Preserved from: https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/ (stored) on 2026-08-11
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Taekjin Lee (KAIST, ETRI), Seongil Wi (KAIST), Suyoung Lee (KAIST), Sooel Son (KAIST)

An Unrestricted File Upload (UFU) vulnerability is a critical security threat that enables an adversary to upload her choice of a forged file to a target web server. This bug evolves into an Unrestricted Executable File Upload (UEFU) vulnerability when the adversary is able to conduct remote code execution of the uploaded file via triggering its URL. We design and implement FUSE, the first penetration testing tool designed to discover UFU and UEFU vulnerabilities in server-side PHP web applications. The goal of FUSE is to generate upload requests; each request becomes an exploit payload that triggers a UFU or UEFU vulnerability. However, this approach entails two technical challenges: (1) it should generate an upload request that bypasses all content-filtering checks present in a target web application; and (2) it should preserve the execution semantic of the resulting uploaded file. We address these technical challenges by mutating standard upload requests with carefully designed mutation operations that enable the bypassing of content- filtering checks and do not tamper with the execution of uploaded files. FUSE discovered 30 previously unreported UEFU vulnerabilities, including 15 CVEs from 33 real-world web applications, thereby demonstrating its efficacy in finding code execution bugs via file uploads.

 [Paper](https://www.ndss-symposium.org/wp-content/uploads/2020/02/23126-paper.pdf)

 [Video](https://www.youtube.com/watch?v=Ot0unJErC-g&list=PLfUWWM-POgQv0nEidt3oGK-H1XIyHA4uK&index=2&t=0s)
