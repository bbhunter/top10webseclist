---
type: Slides
title: "Tick Tock: Building Browser Red Pills from Timing Side Channels (Slides)"
description: "The original conference slide deck presents the accompanying paper's mechanisms and experiments. Uses JavaScript timing ratios for DOM, storage, worker and graphics operations to distinguish tested virtual machines from physical hosts. A malicious site could withhold payloads from virtualized browser inspection without plugins or privileged instructions. The experiments cover two physical machines and a limited environment matrix, not a universal classifier."
resource: "https://www.usenix.org/sites/default/files/conference/protected-files/woot14_slides_ho.pdf"
tags: [slides, webseclist-reference, usenix, timing-attack, browser-fingerprinting, evasion]
generated:
  by: webseclist-refs/1
  at: "2026-09-29T21:07:32+00:00"
status: stable
stale_after: 2027-09-29
sources:
  - id: original
    resource: "https://www.usenix.org/sites/default/files/conference/protected-files/woot14_slides_ho.pdf"
    title: "Tick Tock: Building Browser Red Pills from Timing Side Channels (Slides)"
    author: Grant Ho, Dan Boneh, Lucas Ballard, Niels Provos
    last_modified: 2014
also_at: []
authors:
  - Grant Ho
  - Dan Boneh
  - Lucas Ballard
  - Niels Provos
canonical_url: ""
cited_by:
  - "2014.md:85"
commit: ""
content_sha256: fe056878fe53fef955f3f6b1a968358bc0a643f35de95fc76ee3d1b282d1f604
depth: full
depth_reason: default
kind: slides
language: ""
licence: unknown
original_url: "https://www.usenix.org/sites/default/files/conference/protected-files/woot14_slides_ho.pdf"
published: 2014
publisher: USENIX
publisher_english: ""
raw_sha256: 5584f326b1a9e9e0455d43142ef8297ffd4e7df7f8f7c713e80bdb501c77c68e
retrieved_from: "https://www.usenix.org/sites/default/files/conference/protected-files/woot14_slides_ho.pdf"
retrieved_kind: manual-import
retrieved_utc: "2026-09-29T21:07:32+00:00"
slug: 2014-usenix-tick-tock-building-browser-red-pills-timing-side-channels-slides
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Tick Tock: Building Browser Red Pills from Timing Side Channels (Slides)

**Tick Tock: Building Browser Red Pills from Timing Side Channels (Slides)** - Grant Ho, Dan Boneh, Lucas Ballard, Niels Provos, USENIX.

- Published: 2014
- Original: <https://www.usenix.org/sites/default/files/conference/protected-files/woot14_slides_ho.pdf>
- Preserved from: https://www.usenix.org/sites/default/files/conference/protected-files/woot14_slides_ho.pdf (manual-import) on 2026-09-29
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so
it remains readable if the page goes offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Tick Tock: Building Browser Red
Pills from Timing Side Channels

   Grant Ho, Dan Boneh   and   Lucas Ballard, Niels Provos
         Stanford                      Google
                    Terminology: Red Pills

• Red Pill: code that distinguishes between a real execution
  environment vs. emulated/virtualized environment

• Native Red Pills: Red pills that execute at application layer (directly on
  OS).

• Browser Red Pills: Red pills executed in the browser sandbox
  (embedded in webpages)
             Prior Work on Red Pills:
     Differentiating VMs from Real Machines
• Black Hat 2005: Original Native Red Pill by J. Rutkowska
• Since then, many other papers on native red pills (Chen 2008, Franklin
  2008, Kapravelos 2011, Paleari 2009, Shi 2014, etc.)

• Key Problem: Native red pills rely on low-level operations (examining
  registers, looking for debugging processes, etc.)
    • Inaccessible to websites (Javascript in the browser)

• This Talk: Designing browser red pills
                             Motivation
• Perspective: Malicious website (e.g. drive-by download)

• Challenge: Anti-malware honeypots (i.e. instrumented VMs)




• Goal: deliver malicious web content to normal users, but act benignly in
  anti-malware honeypots (VMs).
                            Attack Model



            ?
                                           Malicious
                                           Website




            or
Real user        Honeypot
                   (VM)
Attack Model


    ?
                Attack Model

                        Real user detected


   Real user




                                             Malicious
                                             Website


                          VM detected



Honeypot (VM)
Design and Implementation of
      Browser Red Pills
              Distinguishing VM vs. non-VM
                    from the Browser
• Can’t access low-level configuration anomalies, but what about
  performance anomalies?

• Side effects of a virtualization = altered behavior/performance of
  certain operations?

• Main Idea: Measure execution time of certain Javascript operations
  (differential operations) to detect virtualization performance
  anomalies
     Constructing Timing-Based Red Pills

• Problem: How do you account for performance differences that
  results from different hardware or background activity?
    • Raw execution times unreliable



• Solution: Use relative timing measurements for red pills
        Constructing Timing-Based Red Pills
• Idea: Run a simple Javascript operation (baseline operation) to gauge
  background load/base performance
    • Also, baseline operation should not have performance difference
      between VM and non-VM

• Adjust red pill’s timing measurement for background load by: dividing
  the differential operation’s execution time by this baseline time

• Timing done in Javascript (granularity: 1 millisecond)
            Browser Red Pills Schematic

                                  Browser Red Pill
                               Step 1: Execute baseline op and
• Three steps to browser          measure execution time
  red pill, which returns a
  number (timing ratio).
                              Step 2: Execute differential op and
                                   measure execution time

                                            Return:
                                    differential_op_time /
                                      baseline_op_time
    Differential Operations             Baseline Operations

1. Writing to Console             1. Repeatedly writing lots of text
2. Local Storage                     to a DOM node

3. Spawning Web Workers
   (Javascript Threads)
4. Communicating between Web      2. Allocating large chunks of
   Workers                           memory

5. Communicating between CPU
   and GPU via WebGL
6. Heavy Graphics Rendering via
   WebGL
Evaluation and Results
                     Testing Environment
• Windows 7 and Windows 8.1 on real machines, VMWare in binary
  translation mode, and VMWare in hardware-assisted virtualization mode (6
  system environments)

• Chrome 34, Firefox 29, IE 11 (3 browser environments)

• 18 Total environments: {Chrome, Firefox, IE} x {Real, VM-BT, VM-HV} x {Win
  7, 8}

• Loaded each red pill webpage 100 times w/ 500 ms in-between reloads
                Evaluation Methodology
• Now we have distributions (100 measurements) of red pill timing
  ratios

• For each red pill on a given {browser, OS} combination:
   • Compare distribution of timing ratios for: Real Machine vs. VM-BT
   • Compare distribution of timing ratios for: Real Machine vs. VM-HV


• Key question: Is there a significant and practical difference
  between a red pill’s timing ratios on a VM vs. non-VM?
                      Evaluation Metrics
• Two criteria (both should be satisfied):

1. Does a t-test of VM timing ratios vs. non-VM timing ratios produce
   a p-value less than 0.05? (statistically significant difference)
2. Is there a “small” overlap between distribution of timing ratios for
   VM vs. non-VM? (practical difference)
    Criteria 1: Independent, Two-Sample
                    T-Test
• “Welch’s t-test”: two independent samples with unknown
  population variances




    Is there a statistically significant difference between distribution A
    (e.g. real machine timing ratios) and distribution B (e.g. VM timing
    ratios)?
           Criteria 1: Two-Sample T-Test (Cont.)

• p-value from t-test: probability that there is no statistical difference
  between the two distributions



• Criteria 1: t-test of average timing ratios of VM vs. non-VM has
  p-value < 0.05 (all our successful red pills have p-value < 0.000001)
Criteria 2: Minimally Overlapping Distributions

        + VM St. Dev.


    VM Avg. Time Ratio
                                                   • Magic-number cut-off: high
                                                     probability of evading of VMs
          - VM St. Dev.
                                                     and targeting of real machines
  No overlap
                          + Non-VM St. Dev.


                          Non-VM Avg. Time Ratio

                          - Non-VM St. Dev.
    Results: Number of Successful Red Pills
               per Environment
                      Chrome                  IE               Firefox
Windows 8 BT             6                    3                   4
Windows 8 HV             6                    3                   4
Windows 7 BT             3                    5                   4
Windows 7 HV             3                    5                   4

• BT = Binary Translation VM, HV = Hardware-assisted virtualization VM
• Numbers represent sum of successful red pills from both DOM baseline +
  Memory baseline
Defenses for Honeypots
         Distorting Time in the Honeypot

• Replace Javascript timing functions with fake timing
  • Return random or faster timing measurements


• Replace Javascript/HTML5 operations with fake functions
  • Cheat on differential operation execution by completing
    early/faking execution

• These are weaker defenses… likely induce other anomalies.
   Detecting Javascript Evasion (Red Pills)
• Detect differential operations
  • Efficacy unclear for many operations (e.g. Console writing and
    Graphics)


• Detect baseline operations
  • More practical and effective against current baseline operations

• Compare rendered content in non-VM and VM to find evasive JS
  (Kapravelos 2013, Kirat 2014)
Conclusion
                                Summary
• Browser red pills are possible via timing side-channels
   • Timing/performance analysis overcome restricted computing environment
   • Baseline operations resolve background load/noise

• Highly effective:
   • Three major browsers on two latest versions of Windows
   • Hardware-assisted virtualization and binary translation

• Detecting baseline operation most promising defense

• Future work: (1) Measure prevalence of existing JS red pills
               (2) Understand JS implementation diffs in good red pills
Questions?
