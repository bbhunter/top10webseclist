# Tag vocabulary
The controlled vocabulary for `digest.tags` in `archived-references/manifest.json`.
**This file is generated** by counting the tags actually in use. Do not hand-edit it;
a tag enters the vocabulary by being applied to a document and surviving review.

## How to use it
- Choose 4-10 tags per document, from the list below.
- A tag you need that is NOT listed here is a **proposal**: write it with a `?`
  prefix (`?padding-oracle`). Proposals are recorded in the review's report and
  stripped before publication, so a held proposal never reaches a published file.
- Prefer an existing tag over a near-synonym. `sop-bypass` and `same-origin-policy`
  already coexist for the attack and the mechanism; do not add a third spelling.
- A tag is a retrieval key, not a summary. If it would apply to almost every
  document in the archive, it is not earning its place.

## Governance
A `?` proposal is promoted by a maintainer once it has been asked for by more than
one document, or once it names something the vocabulary genuinely cannot express.
Tags used exactly once are listed below and are the first candidates for merging
away.

## The vocabulary

193 tags, across 1648 documents that carry a digest.

| Tag | Documents |
|---|---|
| `Crypto` | 2 |
| `HTTP` | 1 |
| `Identity` | 1 |
| `Injection` | 3 |
| `Server` | 3 |
| `XSS` | 1 |
| `abuse-of-functionality` | 66 |
| `activex` | 12 |
| `ai-agent` | 31 |
| `algorithmic-complexity` | 29 |
| `android` | 33 |
| `angular` | 3 |
| `aspnet` | 46 |
| `attack-chain` | 181 |
| `auth-bypass` | 302 |
| `aws` | 30 |
| `azure` | 11 |
| `blockchain` | 2 |
| `browser-extension` | 71 |
| `browser-fingerprinting` | 23 |
| `bug-bounty` | 165 |
| `cache` | 66 |
| `cache-deception` | 10 |
| `cache-poisoning` | 79 |
| `captcha-bypass` | 2 |
| `case-study` | 272 |
| `cdn` | 45 |
| `charset` | 38 |
| `ci-cd` | 27 |
| `class-pollution` | 5 |
| `clickjacking` | 56 |
| `cloudflare` | 11 |
| `command-injection` | 51 |
| `content-type` | 39 |
| `cookie` | 146 |
| `cors` | 29 |
| `csp` | 55 |
| `csrf` | 141 |
| `css` | 72 |
| `css-injection` | 28 |
| `csti` | 4 |
| `cve` | 249 |
| `data-breach` | 3 |
| `database` | 61 |
| `deanonymization` | 17 |
| `defence` | 59 |
| `dependency-confusion` | 1 |
| `deserialization` | 77 |
| `desync` | 35 |
| `detection` | 119 |
| `django` | 11 |
| `dns` | 86 |
| `dns-rebinding` | 30 |
| `docker` | 4 |
| `dom` | 136 |
| `dom-clobbering` | 14 |
| `domain-takeover` | 2 |
| `dos` | 106 |
| `dotnet` | 66 |
| `drupal` | 4 |
| `dynamic-analysis` | 75 |
| `elasticsearch` | 3 |
| `electron` | 10 |
| `email` | 50 |
| `embedded-device` | 6 |
| `encoding` | 79 |
| `express` | 8 |
| `file-upload` | 88 |
| `filter-bypass` | 297 |
| `flash` | 56 |
| `flask` | 4 |
| `formal-analysis` | 32 |
| `ftp` | 10 |
| `fuzzing` | 49 |
| `gadget-chain` | 93 |
| `gcp` | 11 |
| `github` | 23 |
| `github-actions` | 18 |
| `gitlab` | 7 |
| `go` | 14 |
| `graphql` | 4 |
| `hash-collision` | 6 |
| `header-injection` | 66 |
| `http` | 207 |
| `http2` | 26 |
| `http3` | 5 |
| `https` | 103 |
| `idor` | 27 |
| `iframe` | 133 |
| `info-leak` | 591 |
| `injection` | 118 |
| `ios` | 16 |
| `java` | 120 |
| `javascript` | 381 |
| `javascript-runtime` | 21 |
| `jenkins` | 2 |
| `joomla` | 6 |
| `jwt` | 20 |
| `kubernetes` | 4 |
| `laravel` | 1 |
| `large-scale-scan` | 133 |
| `lfi` | 31 |
| `llm` | 33 |
| `load-balancer` | 16 |
| `mass-assignment` | 11 |
| `measurement-study` | 225 |
| `memory-corruption` | 2 |
| `mime` | 42 |
| `mitigation` | 170 |
| `mongodb` | 6 |
| `mssql` | 11 |
| `mutation-xss` | 11 |
| `mysql` | 24 |
| `nextjs` | 11 |
| `nodejs` | 69 |
| `nosqli` | 3 |
| `novel-technique` | 743 |
| `oauth` | 62 |
| `open-redirect` | 62 |
| `openid` | 29 |
| `parser-differential` | 167 |
| `passkeys` | 10 |
| `path-traversal` | 66 |
| `pdf` | 23 |
| `perl` | 4 |
| `phishing` | 39 |
| `php` | 116 |
| `postgres` | 8 |
| `postmessage` | 34 |
| `predictable-token` | 2 |
| `prior-art-extension` | 57 |
| `privilege-escalation` | 105 |
| `prompt-injection` | 25 |
| `prototype-pollution` | 21 |
| `proxy` | 82 |
| `python` | 34 |
| `race-condition` | 30 |
| `rag` | 2 |
| `rails` | 17 |
| `rce` | 268 |
| `react` | 6 |
| `redis` | 3 |
| `request-smuggling` | 49 |
| `response-splitting` | 17 |
| `rest-api` | 50 |
| `reverse-proxy` | 55 |
| `ruby` | 35 |
| `rust` | 3 |
| `same-origin-policy` | 172 |
| `saml` | 18 |
| `sandbox-escape` | 71 |
| `sanitizer-bypass` | 88 |
| `service-worker` | 10 |
| `session-fixation` | 36 |
| `side-channel` | 206 |
| `smtp` | 18 |
| `smuggling` | 14 |
| `snmp` | 2 |
| `soap` | 13 |
| `sop-bypass` | 189 |
| `spring` | 14 |
| `sqli` | 65 |
| `sso` | 63 |
| `ssrf` | 96 |
| `ssti` | 18 |
| `static-analysis` | 69 |
| `struts` | 4 |
| `supply-chain` | 56 |
| `survey` | 18 |
| `symfony` | 1 |
| `timing-attack` | 89 |
| `tls` | 107 |
| `toctou` | 16 |
| `tooling` | 290 |
| `typosquatting` | 9 |
| `ui-redress` | 71 |
| `unicode` | 37 |
| `url-parsing` | 119 |
| `url-spoofing` | 12 |
| `user-enumeration` | 7 |
| `vendor-advisory` | 54 |
| `vue` | 1 |
| `waf` | 16 |
| `waf-bypass` | 71 |
| `wasm` | 1 |
| `webassembly` | 3 |
| `webauthn` | 11 |
| `webrtc` | 9 |
| `websocket` | 8 |
| `wordpress` | 21 |
| `xsleak` | 72 |
| `xss` | 378 |
| `xxe` | 31 |

### Used exactly once

Review these before reusing them: `HTTP`, `Identity`, `XSS`, `dependency-confusion`, `laravel`, `symfony`, `vue`, `wasm`
