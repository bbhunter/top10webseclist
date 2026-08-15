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

188 tags, across 1279 documents that carry a digest.

| Tag | Documents |
|---|---|
| `Crypto` | 1 |
| `HTTP` | 1 |
| `Identity` | 1 |
| `Injection` | 3 |
| `Server` | 3 |
| `XSS` | 1 |
| `abuse-of-functionality` | 15 |
| `activex` | 9 |
| `ai-agent` | 4 |
| `algorithmic-complexity` | 21 |
| `android` | 31 |
| `angular` | 3 |
| `aspnet` | 40 |
| `attack-chain` | 139 |
| `auth-bypass` | 251 |
| `aws` | 25 |
| `azure` | 6 |
| `browser-extension` | 52 |
| `browser-fingerprinting` | 5 |
| `bug-bounty` | 149 |
| `cache` | 56 |
| `cache-deception` | 9 |
| `cache-poisoning` | 60 |
| `captcha-bypass` | 1 |
| `case-study` | 231 |
| `cdn` | 36 |
| `charset` | 26 |
| `ci-cd` | 14 |
| `class-pollution` | 3 |
| `clickjacking` | 52 |
| `cloudflare` | 8 |
| `command-injection` | 38 |
| `content-type` | 27 |
| `cookie` | 126 |
| `cors` | 25 |
| `csp` | 50 |
| `csrf` | 110 |
| `css` | 55 |
| `css-injection` | 21 |
| `csti` | 4 |
| `cve` | 197 |
| `database` | 48 |
| `deanonymization` | 3 |
| `defence` | 55 |
| `dependency-confusion` | 1 |
| `deserialization` | 60 |
| `desync` | 27 |
| `detection` | 78 |
| `django` | 7 |
| `dns` | 66 |
| `dns-rebinding` | 20 |
| `docker` | 3 |
| `dom` | 118 |
| `dom-clobbering` | 12 |
| `dos` | 87 |
| `dotnet` | 53 |
| `drupal` | 4 |
| `dynamic-analysis` | 63 |
| `elasticsearch` | 2 |
| `electron` | 8 |
| `email` | 36 |
| `embedded-device` | 2 |
| `encoding` | 55 |
| `express` | 6 |
| `file-upload` | 67 |
| `filter-bypass` | 227 |
| `flash` | 43 |
| `flask` | 3 |
| `formal-analysis` | 30 |
| `ftp` | 6 |
| `fuzzing` | 40 |
| `gadget-chain` | 76 |
| `gcp` | 8 |
| `github` | 19 |
| `github-actions` | 7 |
| `gitlab` | 4 |
| `go` | 10 |
| `graphql` | 2 |
| `hash-collision` | 1 |
| `header-injection` | 52 |
| `http` | 173 |
| `http2` | 23 |
| `http3` | 5 |
| `https` | 99 |
| `idor` | 23 |
| `iframe` | 107 |
| `info-leak` | 473 |
| `injection` | 101 |
| `ios` | 16 |
| `java` | 105 |
| `javascript` | 298 |
| `javascript-runtime` | 12 |
| `jenkins` | 1 |
| `joomla` | 4 |
| `jwt` | 13 |
| `kubernetes` | 3 |
| `laravel` | 1 |
| `large-scale-scan` | 107 |
| `lfi` | 27 |
| `llm` | 3 |
| `load-balancer` | 15 |
| `mass-assignment` | 10 |
| `measurement-study` | 193 |
| `mime` | 25 |
| `mitigation` | 138 |
| `mongodb` | 4 |
| `mssql` | 9 |
| `mutation-xss` | 9 |
| `mysql` | 21 |
| `nextjs` | 10 |
| `nodejs` | 57 |
| `nosqli` | 3 |
| `novel-technique` | 620 |
| `oauth` | 51 |
| `open-redirect` | 51 |
| `openid` | 21 |
| `parser-differential` | 133 |
| `passkeys` | 2 |
| `path-traversal` | 51 |
| `pdf` | 19 |
| `perl` | 3 |
| `phishing` | 16 |
| `php` | 93 |
| `postgres` | 6 |
| `postmessage` | 27 |
| `prior-art-extension` | 43 |
| `privilege-escalation` | 83 |
| `prompt-injection` | 3 |
| `prototype-pollution` | 16 |
| `proxy` | 68 |
| `python` | 27 |
| `race-condition` | 25 |
| `rag` | 1 |
| `rails` | 16 |
| `rce` | 204 |
| `react` | 4 |
| `redis` | 3 |
| `request-smuggling` | 35 |
| `response-splitting` | 8 |
| `rest-api` | 40 |
| `reverse-proxy` | 48 |
| `ruby` | 28 |
| `rust` | 3 |
| `same-origin-policy` | 135 |
| `saml` | 15 |
| `sandbox-escape` | 54 |
| `sanitizer-bypass` | 65 |
| `service-worker` | 10 |
| `session-fixation` | 31 |
| `side-channel` | 164 |
| `smtp` | 16 |
| `smuggling` | 14 |
| `snmp` | 2 |
| `soap` | 12 |
| `sop-bypass` | 140 |
| `spring` | 13 |
| `sqli` | 53 |
| `sso` | 54 |
| `ssrf` | 79 |
| `ssti` | 13 |
| `static-analysis` | 57 |
| `struts` | 4 |
| `supply-chain` | 34 |
| `survey` | 17 |
| `symfony` | 1 |
| `timing-attack` | 67 |
| `tls` | 103 |
| `toctou` | 12 |
| `tooling` | 233 |
| `typosquatting` | 9 |
| `ui-redress` | 60 |
| `unicode` | 23 |
| `url-parsing` | 94 |
| `url-spoofing` | 6 |
| `user-enumeration` | 1 |
| `vendor-advisory` | 48 |
| `vue` | 1 |
| `waf` | 15 |
| `waf-bypass` | 61 |
| `wasm` | 1 |
| `webassembly` | 3 |
| `webauthn` | 3 |
| `webrtc` | 9 |
| `websocket` | 7 |
| `wordpress` | 14 |
| `xsleak` | 60 |
| `xss` | 286 |
| `xxe` | 29 |

### Used exactly once

Review these before reusing them: `Crypto`, `HTTP`, `Identity`, `XSS`, `captcha-bypass`, `dependency-confusion`, `hash-collision`, `jenkins`, `laravel`, `rag`, `symfony`, `user-enumeration`, `vue`, `wasm`
