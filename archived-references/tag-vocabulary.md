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

189 tags, across 1457 documents that carry a digest.

| Tag | Documents |
|---|---|
| `Crypto` | 1 |
| `HTTP` | 1 |
| `Identity` | 1 |
| `Injection` | 3 |
| `Server` | 3 |
| `XSS` | 1 |
| `abuse-of-functionality` | 48 |
| `activex` | 12 |
| `ai-agent` | 4 |
| `algorithmic-complexity` | 23 |
| `android` | 31 |
| `angular` | 3 |
| `aspnet` | 41 |
| `attack-chain` | 158 |
| `auth-bypass` | 266 |
| `aws` | 25 |
| `azure` | 6 |
| `browser-extension` | 59 |
| `browser-fingerprinting` | 22 |
| `bug-bounty` | 149 |
| `cache` | 57 |
| `cache-deception` | 9 |
| `cache-poisoning` | 62 |
| `captcha-bypass` | 2 |
| `case-study` | 267 |
| `cdn` | 36 |
| `charset` | 33 |
| `ci-cd` | 14 |
| `class-pollution` | 3 |
| `clickjacking` | 53 |
| `cloudflare` | 8 |
| `command-injection` | 40 |
| `content-type` | 33 |
| `cookie` | 136 |
| `cors` | 25 |
| `csp` | 50 |
| `csrf` | 134 |
| `css` | 66 |
| `css-injection` | 22 |
| `csti` | 4 |
| `cve` | 205 |
| `data-breach` | 3 |
| `database` | 56 |
| `deanonymization` | 15 |
| `defence` | 58 |
| `dependency-confusion` | 1 |
| `deserialization` | 60 |
| `desync` | 27 |
| `detection` | 112 |
| `django` | 7 |
| `dns` | 78 |
| `dns-rebinding` | 30 |
| `docker` | 3 |
| `dom` | 134 |
| `dom-clobbering` | 12 |
| `dos` | 90 |
| `dotnet` | 54 |
| `drupal` | 4 |
| `dynamic-analysis` | 66 |
| `elasticsearch` | 2 |
| `electron` | 8 |
| `email` | 40 |
| `embedded-device` | 3 |
| `encoding` | 69 |
| `express` | 6 |
| `file-upload` | 82 |
| `filter-bypass` | 268 |
| `flash` | 56 |
| `flask` | 3 |
| `formal-analysis` | 30 |
| `ftp` | 9 |
| `fuzzing` | 40 |
| `gadget-chain` | 76 |
| `gcp` | 8 |
| `github` | 19 |
| `github-actions` | 7 |
| `gitlab` | 4 |
| `go` | 10 |
| `graphql` | 2 |
| `hash-collision` | 1 |
| `header-injection` | 60 |
| `http` | 187 |
| `http2` | 23 |
| `http3` | 5 |
| `https` | 101 |
| `idor` | 27 |
| `iframe` | 124 |
| `info-leak` | 545 |
| `injection` | 111 |
| `ios` | 16 |
| `java` | 112 |
| `javascript` | 365 |
| `javascript-runtime` | 15 |
| `jenkins` | 1 |
| `joomla` | 4 |
| `jwt` | 13 |
| `kubernetes` | 3 |
| `laravel` | 1 |
| `large-scale-scan` | 117 |
| `lfi` | 28 |
| `llm` | 3 |
| `load-balancer` | 15 |
| `mass-assignment` | 10 |
| `measurement-study` | 200 |
| `mime` | 39 |
| `mitigation` | 164 |
| `mongodb` | 4 |
| `mssql` | 11 |
| `mutation-xss` | 9 |
| `mysql` | 23 |
| `nextjs` | 10 |
| `nodejs` | 57 |
| `nosqli` | 3 |
| `novel-technique` | 722 |
| `oauth` | 51 |
| `open-redirect` | 59 |
| `openid` | 23 |
| `parser-differential` | 143 |
| `passkeys` | 2 |
| `path-traversal` | 51 |
| `pdf` | 22 |
| `perl` | 4 |
| `phishing` | 32 |
| `php` | 101 |
| `postgres` | 6 |
| `postmessage` | 28 |
| `prior-art-extension` | 54 |
| `privilege-escalation` | 88 |
| `prompt-injection` | 3 |
| `prototype-pollution` | 17 |
| `proxy` | 79 |
| `python` | 27 |
| `race-condition` | 25 |
| `rag` | 1 |
| `rails` | 16 |
| `rce` | 217 |
| `react` | 4 |
| `redis` | 3 |
| `request-smuggling` | 38 |
| `response-splitting` | 13 |
| `rest-api` | 41 |
| `reverse-proxy` | 48 |
| `ruby` | 28 |
| `rust` | 3 |
| `same-origin-policy` | 164 |
| `saml` | 15 |
| `sandbox-escape` | 61 |
| `sanitizer-bypass` | 77 |
| `service-worker` | 10 |
| `session-fixation` | 33 |
| `side-channel` | 197 |
| `smtp` | 17 |
| `smuggling` | 14 |
| `snmp` | 2 |
| `soap` | 12 |
| `sop-bypass` | 180 |
| `spring` | 13 |
| `sqli` | 60 |
| `sso` | 55 |
| `ssrf` | 88 |
| `ssti` | 13 |
| `static-analysis` | 58 |
| `struts` | 4 |
| `supply-chain` | 39 |
| `survey` | 18 |
| `symfony` | 1 |
| `timing-attack` | 82 |
| `tls` | 104 |
| `toctou` | 12 |
| `tooling` | 245 |
| `typosquatting` | 9 |
| `ui-redress` | 63 |
| `unicode` | 30 |
| `url-parsing` | 109 |
| `url-spoofing` | 11 |
| `user-enumeration` | 5 |
| `vendor-advisory` | 53 |
| `vue` | 1 |
| `waf` | 15 |
| `waf-bypass` | 62 |
| `wasm` | 1 |
| `webassembly` | 3 |
| `webauthn` | 3 |
| `webrtc` | 9 |
| `websocket` | 7 |
| `wordpress` | 15 |
| `xsleak` | 67 |
| `xss` | 351 |
| `xxe` | 31 |

### Used exactly once

Review these before reusing them: `Crypto`, `HTTP`, `Identity`, `XSS`, `dependency-confusion`, `hash-collision`, `jenkins`, `laravel`, `rag`, `symfony`, `vue`, `wasm`
