---
type: Whitepaper
title: Are Text-Only Data Formats Safe? (Slides)
description: Presents the LEET 2010 study of malicious TeX documents and online previewers. Examples show why blocking shell commands or filtering literal control sequences does not contain a language with file access and programmable syntax. The deck contrasts vulnerable services with interpreter and process isolation.
resource: "https://www.usenix.org/legacy/event/leet10/tech/slides/checkoway.pdf"
tags: [whitepaper, webseclist-reference, usenix, file-read, filter-bypass, sandbox-escape, case-study, owasp-a05-2021]
generated:
  by: webseclist-refs/1
  at: "2026-09-29T20:45:42+00:00"
status: stable
stale_after: 2027-09-29
sources:
  - id: original
    resource: "https://www.usenix.org/legacy/event/leet10/tech/slides/checkoway.pdf"
    title: Are Text-Only Data Formats Safe? (Slides)
    author: Stephen Checkoway, Hovav Shacham, Eric Rescorla
    last_modified: 2010-04-27
also_at: []
authors:
  - Stephen Checkoway
  - Hovav Shacham
  - Eric Rescorla
canonical_url: ""
cited_by:
  - "2010.md:105"
commit: ""
content_sha256: 5c5ada127883241cb87d4b77417062cb92c6374d47da24a6ca6580d5619c67b2
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://www.usenix.org/legacy/event/leet10/tech/slides/checkoway.pdf"
published: 2010-04-27
publisher: USENIX
publisher_english: ""
raw_sha256: 9942ef74fe1138f6020c8c848934f4be24de9e1bbd6da4e90e26352974c7bc19
retrieved_from: "https://www.usenix.org/legacy/event/leet10/tech/slides/checkoway.pdf"
retrieved_kind: stored
retrieved_utc: "2026-09-29T20:45:42+00:00"
slug: usenix-text-only-data-formats-safe-slides
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Are Text-Only Data Formats Safe? (Slides)

**Are Text-Only Data Formats Safe? (Slides)** - Stephen Checkoway, Hovav Shacham, Eric Rescorla, USENIX.

- Published: 2010-04-27
- Original: <https://www.usenix.org/legacy/event/leet10/tech/slides/checkoway.pdf>
- Preserved from: https://www.usenix.org/legacy/event/leet10/tech/slides/checkoway.pdf (stored) on 2026-09-29
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so
it remains readable if the page goes offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Are Text-Only
             Data Formats Safe?
             Stephen Checkoway, Hovav Shacham, Eric Rescorla




Tuesday, April 27, 2010                                        1
     Intuitive data-safety scale
   Unsafe                                            Safe




Executables                 Media               ASCII Text

              Web Applications      Documents



Tuesday, April 27, 2010                                     2
                                     TEX

                ‣ Document preparation language
                ‣ 7-bit ASCII text
                ‣ Understands boxes and glue
                ‣ Makes pretty equations             boxes and glue
                                     !               H(x, y)
                          D(H!R) =       H(x, y) log
                                                     R(x, y)
                                 x,y∈X


Tuesday, April 27, 2010                                               3
                          How we use TEX




                              TEX

Tuesday, April 27, 2010                    4
     Intuitive data-safety scale
   Unsafe                                            Safe




Executables                 Media               ASCII Text

              Web Applications      Documents      TEX



Tuesday, April 27, 2010                                     5
                          More TEX

                ‣ Turing-complete, macro language: \def
                ‣ Read/write files: \read, \write
                ‣ Extremely malleable syntax: \catcode




Tuesday, April 27, 2010                                   6
        Taking control with TEX
                          Operating
     Distribution                        How
                           System
                                        Write to
                                        Startup
                                      Write to web
     TEX Live                          directory


Tuesday, April 27, 2010                              7
                   LATEX virus lifecycle

                ‣ Compile sploit.tex
                ‣ C:\DOCUME~1\ADMINI~1\STARTM~1
                     \PROGRAMS\STARTUP\sploit.js
                ‣ Restart computer
                ‣ sploit.js finds .tex files; inserts the virus



Tuesday, April 27, 2010                                           8
                          Data exfiltration

                ‣ Read sensitive files
                     ‣ \input, \include
                     ‣ \read, \readline
                ‣ Typeset data in output PDF




Tuesday, April 27, 2010                        9
                          Input filtering


                ‣ Filter out dangerous control sequences
                ‣ Math mode




Tuesday, April 27, 2010                                    10
  TEXniques to bypass filters
                ‣ Macros like \input
                     ‣ \@input, \@iinput, \@input@, \@@input
                     ‣ \lstinputlisting, \verbatiminput
                ‣ Bypass filters
                     ‣ \csname, \begin, ^^xy, \catcode
                ‣ Escape math mode
                     ‣ \end{eqnarray}, \end{align}
Tuesday, April 27, 2010                                        11
Tuesday, April 27, 2010   12
                          TEX’s malleability


                ‣ Category codes control functionality
                ‣ Can be changed by \catcode
                     \catcode`Z=0 ZTeX




Tuesday, April 27, 2010                                  13
               An example: xii.tex
                          By David Carlisle
    \let~\catcode~`76~`A13~`F1~`j00~`P2jdefA71F~`7113jdefPALLF
    PA''FwPA;;FPAZZFLaLPA//71F71iPAHHFLPAzzFenPASSFthP;A$$FevP
    A@@FfPARR717273F737271P;ADDFRgniPAWW71FPATTFvePA**FstRsamP
    AGGFRruoPAqq71.72.F717271PAYY7172F727171PA??Fi*LmPA&&71jfi
    Fjfi71PAVVFjbigskipRPWGAUU71727374 75,76Fjpar71727375Djifx
    :76jelse&U76jfiPLAKK7172F71l7271PAXX71FVLnOSeL71SLRyadR@oL
    RrhC?yLRurtKFeLPFovPgaTLtReRomL;PABB71 72,73:Fjif.73.jelse
    B73:jfiXF71PU71 72,73:PWs;AMM71F71diPAJJFRdriPAQQFRsreLPAI
    I71Fo71dPA!!FRgiePBt'el@ lTLqdrYmu.Q.,Ke;vz vzLqpip.Q.,tz;
    ;Lql.IrsZ.eap,qn.i. i.eLlMaesLdRcna,;!;h htLqm.MRasZ.ilk,%
    s$;z zLqs'.ansZ.Ymi,/sx ;LYegseZRyal,@i;@ TLRlogdLrDsW,@;G
    LcYlaDLbJsW,SWXJW ree @rzchLhzsW,;WERcesInW qt.'oL.Rtrul;e
    doTsW,Wk;Rri@stW aHAHHFndZPpqar.tridgeLinZpe.LtYer.W,:jbye
Tuesday, April 27, 2010                                          14
                          Conclusions


                ‣ Binary/text distinction not a good classifier
                ‣ Arbitrary code execution
                ‣ Exfiltrate sensitive data



Tuesday, April 27, 2010                                           15
                          Questions?




                           Owning people through a typesetting language;
                          it seems unsporting, somehow. – Keaton Mowery


Tuesday, April 27, 2010                                                    16
