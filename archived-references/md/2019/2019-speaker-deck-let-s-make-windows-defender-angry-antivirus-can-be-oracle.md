---
type: Slides
title: "Let's Make Windows Defender Angry: Antivirus can be an oracle!"
resource: "https://speakerdeck.com/icchy/lets-make-windows-defender-angry-antivirus-can-be-an-oracle"
tags: [slides, webseclist-reference, en, speaker-deck]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T01:44:12+00:00"
status: stable
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://speakerdeck.com/icchy/lets-make-windows-defender-angry-antivirus-can-be-an-oracle"
    title: "Let's Make Windows Defender Angry: Antivirus can be an oracle!"
    author: @speakerdeck, icchy
    last_modified: 2019-10-29
also_at: []
authors:
  - @speakerdeck
  - icchy
canonical_url: ""
cited_by:
  - "2019.md:22"
commit: ""
content_sha256: 42f2fcf114a05f6aa311b83436de537d6e0224e89dc97bf6bd7fc8bc3af3c3bc
depth: full
depth_reason: default
kind: slides
language: en
licence: unknown
original_url: "https://speakerdeck.com/icchy/lets-make-windows-defender-angry-antivirus-can-be-an-oracle"
published: 2019-10-29
publisher: Speaker Deck
publisher_english: ""
raw_sha256: 578efa22c2c70a80f775ebd6b60bc4e1cf84574197d192ba6bba1a55e081e973
retrieved_from: "https://speakerdeck.com/icchy/lets-make-windows-defender-angry-antivirus-can-be-an-oracle"
retrieved_kind: live
retrieved_utc: "2026-08-09T01:44:12+00:00"
slug: 2019-speaker-deck-let-s-make-windows-defender-angry-antivirus-can-be-oracle
snapshot: ""
title_english: ""
translation_file: 2019-speaker-deck-let-s-make-windows-defender-angry-antivirus-can-be-oracle_translate.md
translation_of: ""
---

# Let's Make Windows Defender Angry: Antivirus can be an oracle!

**Let's Make Windows Defender Angry: Antivirus can be an oracle!** - @speakerdeck, icchy, Speaker Deck.

- Published: 2019-10-29
- Original: <https://speakerdeck.com/icchy/lets-make-windows-defender-angry-antivirus-can-be-an-oracle>
- Preserved from: https://speakerdeck.com/icchy/lets-make-windows-defender-angry-antivirus-can-be-an-oracle (live) on 2026-08-09
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content (original)

_The source's own words. An English translation of this document is archived beside it as [`2019-speaker-deck-let-s-make-windows-defender-angry-antivirus-can-be-oracle_translate.md`](2019-speaker-deck-let-s-make-windows-defender-angry-antivirus-can-be-oracle_translate.md)._

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Let's Make Windows Defender Angry: Antivirus can be an oracle! - Speaker Deck

# Let's Make Windows Defender Angry: Antivirus can be an oracle!

A presentation about AVOracle (AntiVirus Oracle) at CODE BLUE 2019 U25 track ([https://codeblue.jp/2019/en/talks/?content=talks_23](https://codeblue.jp/2019/en/talks/?content=talks_23))
Japanese version: [https://speakerdeck.com/icchy/antiuirusuwoorakurutosita-windows-defendernidui-suru-xin-siigong-ji-shou-fa](https://speakerdeck.com/icchy/antiuirusuwoorakurutosita-windows-defendernidui-suru-xin-siigong-ji-shou-fa)

 ![Avatar for icchy](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4MTUsInB1ciI6ImJsb2JfaWQifX0=--1bed4ac42ef8d9bbc01fa3fa9de48ce15635648e/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzEyOCwxMjhdfSwicHVyIjoidmFyaWF0aW9uIn19--f1606beb38d4bb71cc3db4761bac98fe23f6abfb/tonkatsu.jpg)

##  [icchy](https://speakerdeck.com/icchy)

 October 29, 2019

## More Decks by icchy

 [ See All by icchy ](https://speakerdeck.com/icchy)

 [

 React Hooksに潜む罠

 ](https://speakerdeck.com/icchy/react-hooks-pitfalls)

 [ ![Avatar for icchy](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4MTUsInB1ciI6ImJsb2JfaWQifX0=--1bed4ac42ef8d9bbc01fa3fa9de48ce15635648e/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/tonkatsu.jpg) icchy ](https://speakerdeck.com/icchy)

 2

  3.6k

 [

 アンチウイルスをオラクルとした Windows Defenderに対する 新しい攻撃手法

 ](https://speakerdeck.com/icchy/antiuirusuwoorakurutosita-windows-defendernidui-suru-xin-siigong-ji-shou-fa)

 [ ![Avatar for icchy](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4MTUsInB1ciI6ImJsb2JfaWQifX0=--1bed4ac42ef8d9bbc01fa3fa9de48ce15635648e/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/tonkatsu.jpg) icchy ](https://speakerdeck.com/icchy)

 0

  640

 [

 WCTF2019: Gyotaku The Flag

 ](https://speakerdeck.com/icchy/wctf2019-gyotaku-the-flag)

 [ ![Avatar for icchy](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4MTUsInB1ciI6ImJsb2JfaWQifX0=--1bed4ac42ef8d9bbc01fa3fa9de48ce15635648e/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/tonkatsu.jpg) icchy ](https://speakerdeck.com/icchy)

 0

  380

## Other Decks in Research

 [ See All in Research ](https://speakerdeck.com/c/research)

 [

 Fukui Shibiten 39 - AI Art

 ](https://speakerdeck.com/butchi/fukui-shibiten-39-ai-art)

 [ ![Avatar for IWABUCHI Yu(u)ki butchi](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTcwMjYsInB1ciI6ImJsb2JfaWQifX0=--095b7a754ff32159e37778110a816d339cbcce26/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/us-ig-i.png) butchi ](https://speakerdeck.com/butchi)

 0

  170

 [

 敵対生成プロンプト同時探索による内省型プロンプト最適化

 ](https://speakerdeck.com/kinoue_smarthr/di-dui-sheng-cheng-puronputotong-shi-tan-suo-niyorunei-sheng-xing-puronputozui-shi-hua)

 [ ![Avatar for Kotaro Inoue](https://secure.gravatar.com/avatar/35965fa5fb070df50bdbeb10aa78a08a?s=24) kinoue_smarthr ](https://speakerdeck.com/kinoue_smarthr)

 0

  350

 [

 Visual SLAM未来予測 / Future Prediction in Visual SLAM

 ](https://speakerdeck.com/koide3/future-prediction-in-visual-slam)

 [ ![Avatar for koide3](https://secure.gravatar.com/avatar/e19725a18fcb76076c0b3149222e66ff?s=24) koide3 ](https://speakerdeck.com/koide3)

 1

  830

 [

 Google Cloud Next 2026 DM Recap Agentic Data Cloudを添えて / Google Cloud Next 2026 DM Recap

 ](https://speakerdeck.com/nnaka2992/google-cloud-next-2026-dm-recap)

 [ ![Avatar for nnaka2992](https://secure.gravatar.com/avatar/5a979f182ec9a03fdc8099ae064e71eb?s=24) nnaka2992 ](https://speakerdeck.com/nnaka2992)

 0

  100

 [

 重要だけど測れていないもの：高齢者ケアの見えない課題

 ](https://speakerdeck.com/theoriatec2024/zhong-yao-dakedoce-reteinaimono-gao-ling-zhe-keanojian-enaike-ti)

 [ ![Avatar for テオリア・テクノロジーズ](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NTg0MDQyLCJwdXIiOiJibG9iX2lkIn19--a11cf3c988ed80f1908eb2616f1acf54295d2e73/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/Theoria_T_blue.png) theoriatec2024 ](https://speakerdeck.com/theoriatec2024)

 0

  450

 [

 2025年度秋葉原ウォーカブルプロジェクト調査報告 「アキバらしいウォーカブル」とは何か

 ](https://speakerdeck.com/izumiyama_lab/2025nian-du-diao-cha-bao-gao-akibarasiiuokaburu-tohahe-ka)

 [ ![Avatar for 日本大学 都市計画研究室（泉山ゼミ）](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Njk0MzYwLCJwdXIiOiJibG9iX2lkIn19--1be62bf94d04e81397e5c1baa71e453b19f54102/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/%E3%83%AD%E3%82%B4%E5%AE%8C%E6%88%90%E7%89%88%EF%BC%BF%E8%83%8C%E6%99%AF%E9%80%8F%E6%98%8E.png) izumiyama_lab ](https://speakerdeck.com/izumiyama_lab)

 1

  150

 [

 [BlackHatAsia2026] Hidden Telemetry: Uncovering TraceLogging ETW Providers You're Not Using (Yet)

 ](https://speakerdeck.com/asuna_jp/blackhatasia2026-hidden-telemetry-uncovering-tracelogging-etw-providers-youre-not-using-yet)

 [ ![Avatar for Asuka Nakajima](https://secure.gravatar.com/avatar/0cf832af679c778f7c3dd81a2b4aa340?s=24) asuna_jp ](https://speakerdeck.com/asuna_jp)

 1

  630

 [

 第64回CV・PRML勉強会 論文紹介：Linguistic Priors for Visual Decoupling: Towards Symmetric Vision-Brain Alignment

 ](https://speakerdeck.com/sokikatayama/di-64hui-cvprmlmian-qiang-hui-lun-wen-shao-jie-linguistic-priors-for-visual-decoupling-towards-symmetric-vision-brain-alignment)

 [ ![Avatar for Soki Katayama](https://secure.gravatar.com/avatar/f07c5912a741767d06c412ed6d52b531?s=24) sokikatayama ](https://speakerdeck.com/sokikatayama)

 0

  150

 [

 kintone リサーチ副部/UXリサーチャー 業務紹介

 ](https://speakerdeck.com/cybozuinsideout/kintone-researcher)

 [ ![Avatar for Cybozu](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTE1MzQsInB1ciI6ImJsb2JfaWQifX0=--27e7f85415c65b868b4c1afa18dbb922c9361d8b/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/ILMxngMD_400x400.png) cybozuinsideout ](https://speakerdeck.com/cybozuinsideout)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 0

  130

 [

 LA-Bench 2025：実験指示から実行可能手順を生成するためのデータセット/LA-Bench 2025: A Dataset for Generating Executable Experimental Procedures from Experimental Instructions

 ](https://speakerdeck.com/stktu/la-bench-2025-a-dataset-for-generating-executable-experimental-procedures-from-experimental-instructions)

 [ ![Avatar for Shota Kato](https://secure.gravatar.com/avatar/d60dc42bf3b7ad6628b0e67527f441b6?s=24) stktu ](https://speakerdeck.com/stktu)

 0

  110

 [

 第12回人と環境にやさしい交通をめざす全国大会／熊本都市圏「車1割削減、渋滞半減、公共交通2倍」をめざして

 ](https://speakerdeck.com/trafficbrain/20260315-hito-to-kankyo-ni-yasashii)

 [ ![Avatar for Traffic Brain](https://secure.gravatar.com/avatar/e8f618bf29b36a046d01e235071b2ac3?s=24) trafficbrain ](https://speakerdeck.com/trafficbrain)

 0

  140

 [

 Scalable dynamic origin-destination demand estimation enhanced by high-resolution satellite imagery data

 ](https://speakerdeck.com/satai/scalable-dynamic-origin-destination-demand-estimation-enhanced-by-high-resolution-satellite-imagery-data)

 [ ![Avatar for SatAI.challenge](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ2MDUwLCJwdXIiOiJibG9iX2lkIn19--b6d6ea071912ace3f41814c723917566e73c75f5/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/image%20(2).png) satai ](https://speakerdeck.com/satai)

 3

  380

## Featured

 [ See All Featured ](https://speakerdeck.com/p/featured)

 [

 Lessons Learnt from Crawling 1000+ Websites

 ](https://speakerdeck.com/charlesmeaden/lessons-learnt-from-crawling-1000-plus-websites)

 [ ![Avatar for Charles Meaden](https://secure.gravatar.com/avatar/ce0e73fa718d3c8e32bf992761c1968e?s=24) charlesmeaden ](https://speakerdeck.com/charlesmeaden)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 1

  1.5k

 [

 The SEO Collaboration Effect

 ](https://speakerdeck.com/kristinabergwall1/the-seo-collaboration-effect)

 [ ![Avatar for Kristina Bergwall](https://secure.gravatar.com/avatar/ebbb8b31502fbaac10ecc9c5bca51501?s=24) kristinabergwall1 ](https://speakerdeck.com/kristinabergwall1)

 1

  510

 [

 A better future with KSS

 ](https://speakerdeck.com/kneath/a-better-future-with-kss)

 [ ![Avatar for Kyle Neath](https://secure.gravatar.com/avatar/5f2da528927a2ec9ba4fec2069cbc958?s=24) kneath ](https://speakerdeck.com/kneath)

 240

  18k

 [

 HDC tutorial

 ](https://speakerdeck.com/michielstock/hdc-tutorial)

 [ ![Avatar for Michiel Stock](https://secure.gravatar.com/avatar/4888c8378accd22acc2998ddf1414e7f?s=24) michielstock ](https://speakerdeck.com/michielstock)

 2

  780

 [

 The B2B funnel & how to create a winning content strategy

 ](https://speakerdeck.com/katarinadahlin/the-b2b-funnel-and-how-to-create-a-winning-content-strategy)

 [ ![Avatar for Katarina Dahlin](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjAwNTg5LCJwdXIiOiJibG9iX2lkIn19--24cb98b2197cd4cdeb5e3ae1f94b4c1a162cd1bf/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/Avainsana-analyysi%20thumbnails.png) katarinadahlin ](https://speakerdeck.com/katarinadahlin)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 1

  460

 [

 Mind Mapping

 ](https://speakerdeck.com/helmedeiros/mind-mapping)

 [ ![Avatar for Hélio Medeiros](https://secure.gravatar.com/avatar/b870070e35cb43df68fceaee71755106?s=24) helmedeiros ](https://speakerdeck.com/helmedeiros)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 1

  300

 [

 Building AI with AI

 ](https://speakerdeck.com/inesmontani/building-ai-with-ai)

 [ ![Avatar for Ines Montani](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkwMDgsInB1ciI6ImJsb2JfaWQifX0=--32562a32b00d456c251338e2bbab3b3a7c1775bf/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/profile_ines.jpg) inesmontani ](https://speakerdeck.com/inesmontani)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 1

  1.1k

 [

 職位にかかわらず全員がリーダーシップを発揮するチーム作り / Building a team where everyone can demonstrate leadership regardless of position

 ](https://speakerdeck.com/madoxten/building-a-team-where-everyone-can-demonstrate-leadership-regardless-of-position)

 [ ![Avatar for MADOX](https://secure.gravatar.com/avatar/c17f3305cb0231227adae066aa770c51?s=24) madoxten ](https://speakerdeck.com/madoxten)

 64

  56k

 [

 Kristin Tynski - Automating Marketing Tasks With AI

 ](https://speakerdeck.com/techseoconnect/kristin-tynski-automating-marketing-tasks-with-ai)

 [ ![Avatar for Tech SEO Connect](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTQ2NjU4LCJwdXIiOiJibG9iX2lkIn19--14f297c27d2190051dc109b5d472cf0297dd6c3e/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--924ecf2834d46e1be7416cc0ef8ce19d4bbdebbf/40575_logo_social%20media%20profile%204.png) techseoconnect ](https://speakerdeck.com/techseoconnect)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 0

  440

 [

 Practical Orchestrator

 ](https://speakerdeck.com/shlominoach/practical-orchestrator)

 [ ![Avatar for Shlomi Noach](https://secure.gravatar.com/avatar/168ccec72eee0530b818d44f3fedaacf?s=24) shlominoach ](https://speakerdeck.com/shlominoach)

 191

  12k

 [

 Building a A Zero-Code AI SEO Workflow

 ](https://speakerdeck.com/portentint/building-a-a-zero-code-ai-seo-workflow)

 [ ![Avatar for Ian Lurie](https://secure.gravatar.com/avatar/96251c01a6e587b796d043b064fe5224?s=24) portentint ](https://speakerdeck.com/portentint)

 [PRO](https://speakerdeck.com/pro?utm_campaign=PRO&utm_medium=web&utm_source=user_pro_badge)

 0

  650

 [

 Discover your Explorer Soul

 ](https://speakerdeck.com/emna__ayadi/discover-your-explorer-soul)

 [ ![Avatar for Emna](https://speakerdeck.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NzI5LCJwdXIiOiJibG9iX2lkIn19--c59e14bd8fc81f3e291b47c9b3de17d20d6d955b/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fZmlsbCI6WzI0LDI0XX0sInB1ciI6InZhcmlhdGlvbiJ9fQ==--dcc78b2290da0fc746e1bfe817edcd08056147b6/emna__ayadi.jpg) emna__ayadi ](https://speakerdeck.com/emna__ayadi)

 2

  1.2k

## Transcript

-

###  [Let's Make Windows Defender Angry: Antivirus can be an oracle!](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_0.jpg)

 Ryo Ichikawa (icchy) CODE BLUE 2019, 10/29

-

###  [Who am I • icchy (a.k.a. t0nk42) • CTF enthusiast](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_1.jpg)

 ◦ TokyoWesterns captain ◦ Web, Forensics • CTF Oraganizer ◦ TokyoWesterns CTF ▪ Challenge authoring, Infrastructure maintainance ◦ CODE BLUE CTF ▪ Bull's Eye system developer

-

###  [Question • Can you point out the vulnerability? ◦ You'll](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_2.jpg)

 know what the vulnerability is after this talk

-

###  [https://www.rambus.com/blogs/an-introduction-to-side-channel-attacks/ Side-channel attack](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_3.jpg)

-

###  [Side-channel attacks basics • Ordinary exploits ◦ Remote Code Execution](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_4.jpg)

 ◦ Path traversal • Side-channel attacks ◦ Leak sensitive data from side-eﬀects everywhere ◦ Spectre: time diﬀerence between cache hit ◦ XS-Search: unprocted attributes of JavaScript (ex. iframe.length) ◦ Padding oracle: padding error tell us plain text • They are recovering info from side-eﬀects (i.e. oracles)

-

###  [What is the target of side-channel attack? • CPU ◦](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_5.jpg)

 Spectre • Content auditor ◦ XSS auditor • Crypto ◦ Padding oracle (ex. POODLE) • Hardware ◦ Power analysis

-

###  [Content auditors • Content auditors protect users ◦ XSS Auditor](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_6.jpg)

 ◦ WAF (Web Application Firewall) ◦ Antivirus software • Content auditors know the content to be audited • Content auditors sometimes have evaluation

-

###  [Side-channel attacks against content auditor • XS-Search ◦ Triggering false](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_7.jpg)

 positive for XSS Auditor in Chrome • Reﬂected XSS would be detected and blocked ◦ http://target/?<script>var secret = '1234';</script> ◦ query malformed url to leak secret ▪ <script>var secret = '1232';</script> ▪ <script>var secret = '1233';</script> ▪ <script>var secret = '1234';</script> blocked! • Let's call this kind of attack Auditor Based Oracle • How about antivirus software?

-

 [None](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_8.jpg)

-

###  [Antivirus Technologies • one of the most common software we](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_9.jpg)

 use today ◦ Avast ◦ ESET ◦ Kaspersky Security ◦ McAfee ◦ Norton Security ◦ Symantec Endpoint Protection ◦ Trendmicro Virus Buster Cloud ◦ Windows Defender ◦ … • Protect users from malicious attempts by auditing ◦ File content ◦ Network traﬃcs ◦ etc.

-

###  [audit([secret] + [user input])](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_10.jpg)

-

###  [Abusing Antivirus Technologies • What if attacker can control data](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_11.jpg)

 partially? ◦ as saving input with sensitive data ◦ attacker can trigger false positive • [secret] + [user input] => auditor ﬁred? ◦ attacker may leak [secret] by changing [user input] • Antivirus can be an oracle as well! ◦ Various analyzers for contents

-

###  [Abusing Antivirus Technologies • Antivirus Software is blackbox ◦ When](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_12.jpg)

 they work? ◦ What they will do? ◦ How they detect malware? ◦ How is their architecture? ◦ Which ﬁles are required to run them? ◦ etc. • Let's dig into Windows Defender ◦ Most popular ◦ Running on Windows by default

-

###  [Windows Defender • What content will be detected as malicious?](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_13.jpg)

 ◦ They have their own malware list ▪ https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes ◦ Probably other vendors have similar ones. ◦ No details published • We need to analyze Windows Defender!

-

###  [Black-box Windows Defender analysis • Run audit process on… ◦](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_14.jpg)

 ﬁle access ◦ command execution ◦ if (malicious) ▪ block access from user and notify to user • Analyzers for various content ◦ Encoding ▪ Base64 ◦ Archive, Compression ▪ ZIP, GZip, ... ◦ Executables ▪ PE, WSH (VBS, JScript), … • Black-box analyzing is super tiresome work

-

###  [How to analyze Windows Defender efficiently?](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_15.jpg)

-

###  [Windows Defender analysis is tiresome work • "MpCmdRun.exe" can trigger](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_16.jpg)

 the engine directly ◦ still some issues are there

-

###  [Windows Defender analysis is tiresome work • Unexpected behavior of](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_17.jpg)

 Windows Defender ◦ timing issue ◦ neutralization (deletion) • We have to regenerate payloads ◦ ...bunch of times • No debug information ◦ Hard to know why one is detected or not detected • Any useful tools? ◦ several works are there

-

###  [Windows Defender is ported to Linux! • github.com/taviso/loadlibrary ◦ emulating](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_18.jpg)

 mpengine.dll execution ◦ enables us to do try and error ◦ show us some debug output ~$ ./mpclient ../files/eicar main(): Scanning ../files/eicar... EngineScanCallback(): Scanning input EngineScanCallback(): Threat Virus:DOS/EICAR_Test_File identified. ~$ ./mpclient ../files/eicar.b64 main(): Scanning ../files/eicar.b64... EngineScanCallback(): Scanning input EngineScanCallback(): Scanning input->(Base64) EngineScanCallback(): Threat Virus:DOS/EICAR_Test_File identified.

-

###  [Some tips about taviso/loadlibrary • You can get PDB symbol](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_19.jpg)

 ﬁle in older version ◦ refer github.com/0xAlexei/WindowsDefenderTools ◦ MD5=e95d3f9e90ba3ccd1a4b8d63cbd88d1b => 1.271.81.0 ◦ Download older version of mpam-fe.exe then use cabextract ▪ mpengine.dll is core engine • Debug features ◦ enable DEBUG ﬂag to trace API calls inside

-

###  [Windows Defender internals • Windows Defender signature format: *.vdm ◦](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_20.jpg)

 mpasbase.vdm ◦ somehow encrypted • WDExtract would be helpful ◦ github.com/hﬁref0x/WDExtract • Let's see the contents decrypted

-

###  [Windows Defender internals • Windows Defender uses Lua](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_21.jpg)

-

###  [Windows Defender internals signature name signature deﬁnition (string)](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_22.jpg)

-

###  [Windows Defender internals • handlers for various ﬁle format](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_23.jpg)

-

###  [After white-box (?) Windows Defender analysis • Windows Defender has](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_24.jpg)

 JScript analyzer ◦ with DOM API supported • Not just parsing, but also emulating • If JScript calls eval(str) , str would also be audited ◦ eval("EICAR") => detected • What happens if combined

-

###  [Attack to demo application • Simple application for PoC ◦](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_25.jpg)

 GET /?c1=controllable1&c2=controllable2 ▪ save data with simple format ▪ user cannot see the content of Secret ◦ GET /:name ▪ check existence and integrity • How to leak the Secret ?

-

###  [Building exploit • We have Windows Defender emulator! ◦ with](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_26.jpg)

 debug information • JScript eval function also evaluates argument ◦ threat detected if argument contains malicious • eval("EICA" + input) => ? ◦ threat detected → input is "R" ◦ nothing detected → input is not "R"

-

###  [Some issues in JScript engine • if statement will never](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_27.jpg)

 be evaluated ◦ if (true) {eval("EICA" + "R")} → not detected ◦ object accessing will help you: {0: "a", 1: "b", ...}[input] • parser stops on null byte ◦ eval("EICA" + "R[NULL]") → syntax error ◦ how to deal with null bytes?

-

###  [Another feature in mpengine.dll • They can analyze HTML document](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_28.jpg)

 ◦ some html tags would be a trigger (ex. <script>) ◦ parser will not stop on null byte • JScript can access the elements :) ◦ if they have <body> tag ◦ <script>document.body.innerHTML[0]</script><body>[secret]</body> • Now you have an oracle!

-

###  [Building exploit • JavaScript ◦ $idx and $c would be](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_29.jpg)

 iterated • Windows Defender get angry if $c is appropriate • It requires 256 times try for each $idx :( var body = document.body.innerHTML; var eicar = "EICA"; var n = body[$idx].charCodeAt(0); eicar = eicar + String.fromCharCode(n^$c); eval(eicar);

-

###  [Building exploit • much more faster! ◦ Math.min is also](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_30.jpg)

 available, do binary search • $c < [input]: detected • $c > [input]: not detected ◦ then do binary search! var body = document.body.innerHTML; var eicar = "EICA"; var n = body[$idx].charCodeAt(0); eicar = eicar + {$c: 'k'}[Math.min($c, n)]; eval(eicar);

-

###  [Building exploit • Now everything is ready :) ◦ Controllable1:](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_31.jpg)

 <script>...</script><body> ◦ Secret: [secret] ◦ Controllable2: </body> • to get oracle: accessing /:name after querying / ◦ detected → Internal Server Error ◦ not detected → you can see the response ...<script>[script]</script><body>...[secret]...</body>...

-

###  [Demo • AVOracle attack against simple demo application](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_32.jpg)

-

###  [Pros and Cons • Pros ◦ Attacker can use this](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_33.jpg)

 method blindly ◦ No need to know target structure well, just put part of payloads everywhere • Cons ◦ Attacker need to put two pieces of payloads ◦ Only data between payloads would be leaked • Any other variants? ◦ It would be great if there is way to leak previous / following data ◦ No PoC so far

-

###  [Any other victims?](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_34.jpg)

-

###  [Potential victims • So many applications are saving user input](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_35.jpg)

 with sensitive data • Session ﬁle ◦ TokyoWesterns CTF 2019 phpnote ◦ leak HMAC secret stored in PHP session (not visible from user) • Log ﬁle ◦ Apache, Nginx, IIS • Database ◦ ﬁle-based DBMS (ex. SQLite3) • Cache ﬁle ◦ browser, byte code cache

-

###  [Antivirus as ﬁle modiﬁer • Antivirus deletes / modiﬁes ﬁle](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_36.jpg)

 if detected ◦ Windows Defender replaces matched part by spaces (in case of HTML script tag) • Attacker can delete content partially • Even attacker cannot leak data, there might be something to do data<script>eval('EICAR');</script>data data<script> </script>data

-

###  [Wiping out evidence • Attacker can delete part of log](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_37.jpg)

 1. put <script>/* before beginning attack 2. do malicious attempts 3. put */;eval('EICAR');</script> after attack x.x.x.x - - [29/Oct/2019:00:00:00 +0000] "GET /<script>/*" x.x.x.x - - [29/Oct/2019:00:00:10 +0900] "GET /attack.php" ... [some malicious attempts] ... x.x.x.x - - [29/Oct/2019:00:00:00 +0000] "GET /*/;eval('EICAR')</script>"

-

###  [Wiping out evidence • Attacker can delete part of log](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_38.jpg)

 1. put <script>/* before beginning attack 2. do malicious attempts 3. put */;eval('EICAR');</script> after attack x.x.x.x - - [29/Oct/2019:00:00:00 +0000] "GET /<script> </script>"

-

###  [Antivirus as DoS • Deleting matched malicious over structural boundary](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_39.jpg)

 • Structure metadata would be destroyed ◦ replaced by spaces • If two part will not over the boundary ◦ attacker can overwrite other data

-

###  [How about other antivirus?](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_40.jpg)

-

###  [Targeting other antivirus • VirusTotal is the best friend :)](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_41.jpg)

 • Which antivirus suppoorts JScript emulator? ◦ eval('EICA'+'R'); // should be detected ◦ eval('EICA'+'#'); // should not be detected • 4 antivirus passed ◦ Cyren ◦ DrWeb ◦ Microsoft ◦ NANO-Antivirus • TrendMicro ◦ false positive

-

###  [Targeting other antivirus • Further testing • Which antivirus supports](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_42.jpg)

 DOM API? ◦ eval('EICA'+innerHTML[0]);<body>R</body> // should be detected ◦ eval('EICA'+innerHTML[0]);<body>#</body> // should not be detected • Only Microsoft passed ◦ That's why they are vulnerable to AVOracle • SUPERAntiSpyware ◦ false positive

-

###  [Windows Defender is too smart](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_43.jpg)

-

###  [How to prevent this attack? • IMO: no generic way](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_44.jpg)

 to patch ◦ standard behavior, not vulnerability • Disable auditor engine is one way ◦ Chromium XSS auditor is removed ◦ but Microsoft would not remove the engine • Application developers should ... ◦ know about this attack ◦ not save secret with controllable data • … but it is not developer's fault! ◦ Antivirus vendor should take care about that

-

###  [Conclusions • Auditor Based Oracle is everywhere ◦ Antivirus is](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_45.jpg)

 one big example ◦ it would be oracle if it has intelligent engine • Windows Defender is too smarter than other antivirus ◦ resulted in an eﬀective oracle ◦ more smarter engine will get more oracles • Antivirus behavior would be sometimes harmful ◦ not only data leakage, also DoS • DO NOT store any secret surrounded by user input ◦ or your application would be vulnerable to AVOracle

-

###  [Any Questions? @t0nk42 icchy](https://files.speakerdeck.com/presentations/ad7d23687b414ff4874295f328d490b5/slide_46.jpg)
