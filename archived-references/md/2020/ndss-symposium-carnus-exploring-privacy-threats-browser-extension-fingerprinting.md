---
type: Article
title: "Carnus: Exploring the Privacy Threats of Browser Extension Fingerprinting"
description: Carnus automatically builds behavioural fingerprints of browser extensions from DOM changes, outgoing HTTP requests and intra-browser message traffic, not just web accessible resources. Fingerprinting 29,428 extensions and mining 1.44 million reviews, it shows a site can identify visitors and infer sensitive traits such as religion or medical conditions.
resource: "https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/"
tags: [article, webseclist-reference, en, ndss-symposium, browser-extension, info-leak, side-channel, dom, measurement-study, large-scale-scan, static-analysis, dynamic-analysis, novel-technique]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:43:05+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/"
    title: "Carnus: Exploring the Privacy Threats of Browser Extension Fingerprinting"
    author: Soroush Karami, Panagiotis Ilia, Konstantinos Solomos, Jason Polakis
also_at:
  - "https://www.ndss-symposium.org/wp-content/uploads/2020/02/24383-paper.pdf"
authors:
  - Soroush Karami
  - Panagiotis Ilia
  - Konstantinos Solomos
  - Jason Polakis
canonical_url: ""
cited_by:
  - "2020.md:75"
commit: ""
content_sha256: bfb25730cf05b3f866535c822435ba2485a331c37374aba0cb165d9979e85543
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/"
published: ""
publisher: NDSS Symposium
publisher_english: ""
raw_sha256: fd9d2f867b42b5e6eda2054f33aeb31e8f557453716539c15783fbd34b175cfe
retrieved_from: "https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:43:05+00:00"
slug: ndss-symposium-carnus-exploring-privacy-threats-browser-extension-fingerprinting
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Carnus: Exploring the Privacy Threats of Browser Extension Fingerprinting

**Carnus: Exploring the Privacy Threats of Browser Extension Fingerprinting** - Soroush Karami, Panagiotis Ilia, Konstantinos Solomos, Jason Polakis, NDSS Symposium.

- Published: date not stated
- Original: <https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/>
- Also published at: <https://www.ndss-symposium.org/wp-content/uploads/2020/02/24383-paper.pdf>
- Preserved from: https://www.ndss-symposium.org/ndss-paper/carnus-exploring-the-privacy-threats-of-browser-extension-fingerprinting/ (stored) on 2026-08-11
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Soroush Karami (University of Illinois at Chicago), Panagiotis Ilia (University of Illinois at Chicago), Konstantinos Solomos (University of Illinois at Chicago), Jason Polakis (University of Illinois at Chicago)

With users becoming increasingly privacy-aware and browser vendors incorporating anti-tracking mechanisms, browser fingerprinting has garnered significant attention. Accordingly, prior work has proposed techniques for identifying browser extensions and using them as part of a device's fingerprint. While previous studies have demonstrated how extensions can be detected through their web accessible resources, there exists a significant gap regarding techniques that indirectly detect extensions through behavioral artifacts. In fact, no prior study has demonstrated that this can be done in an automated fashion. In this paper, we bridge this gap by presenting the first fully automated creation and detection of behavior-based extension fingerprints. We also introduce two novel fingerprinting techniques that monitor extensions' communication patterns, namely outgoing HTTP requests and intra-browser message exchanges. These techniques comprise the core of Carnus, a modular system for the static and dynamic analysis of extensions, which we use to create the largest set of extension fingerprints to date. We leverage our dataset of 29,428 detectable extensions to conduct a comprehensive investigation of extension fingerprinting in realistic settings and demonstrate the practicality of our attack. Our experimental evaluation against a state-of-the-art countermeasure confirms the robustness of our techniques as 87.92% of our behavior-based fingerprints remain effective.

Subsequently, we aim to explore the true extent of the privacy threat that extension fingerprinting poses to users, and present a novel study on the feasibility of inference attacks that reveal private and sensitive user information based on the functionality and nature of their extensions. We first collect over 1.44 million public user reviews of our detectable extensions, which provide a unique macroscopic view of the browser extension ecosystem and enable a more precise evaluation of the discriminatory power of extensions as well as a new deanonymization vector. We also automatically categorize extensions based on the developers' descriptions and identify those that can lead to the inference of personal data (religion, medical issues, etc.). Overall, our research sheds light on previously unexplored dimensions of the privacy threats of extension fingerprinting and highlights the need for more effective countermeasures that can prevent our attacks.

 [Paper](https://www.ndss-symposium.org/wp-content/uploads/2020/02/24383-paper.pdf)

 [Video](https://www.youtube.com/watch?v=mfmAWRzpbCU&list=PLfUWWM-POgQv0nEidt3oGK-H1XIyHA4uK&index=6&t=0s)
