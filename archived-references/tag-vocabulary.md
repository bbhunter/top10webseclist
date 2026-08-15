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

188 tags, across 1379 documents that carry a digest.

| Tag | Documents |
|---|---|
| `Crypto` | 1 |
| `HTTP` | 1 |
| `Identity` | 1 |
| `Injection` | 3 |
| `Server` | 3 |
| `XSS` | 1 |
| `abuse-of-functionality` | 34 |
| `activex` | 11 |
| `ai-agent` | 4 |
| `algorithmic-complexity` | 23 |
| `android` | 31 |
| `angular` | 3 |
| `aspnet` | 41 |
| `attack-chain` | 151 |
| `auth-bypass` | 259 |
| `aws` | 25 |
| `azure` | 6 |
| `browser-extension` | 57 |
| `browser-fingerprinting` | 11 |
| `bug-bounty` | 149 |
| `cache` | 56 |
| `cache-deception` | 9 |
| `cache-poisoning` | 61 |
| `captcha-bypass` | 1 |
| `case-study` | 245 |
| `cdn` | 36 |
| `charset` | 27 |
| `ci-cd` | 14 |
| `class-pollution` | 3 |
| `clickjacking` | 53 |
| `cloudflare` | 8 |
| `command-injection` | 40 |
| `content-type` | 31 |
| `cookie` | 131 |
| `cors` | 25 |
| `csp` | 50 |
| `csrf` | 122 |
| `css` | 58 |
| `css-injection` | 22 |
| `csti` | 4 |
| `cve` | 204 |
| `database` | 53 |
| `deanonymization` | 9 |
| `defence` | 58 |
| `dependency-confusion` | 1 |
| `deserialization` | 60 |
| `desync` | 27 |
| `detection` | 95 |
| `django` | 7 |
| `dns` | 73 |
| `dns-rebinding` | 27 |
| `docker` | 3 |
| `dom` | 125 |
| `dom-clobbering` | 12 |
| `dos` | 90 |
| `dotnet` | 54 |
| `drupal` | 4 |
| `dynamic-analysis` | 66 |
| `elasticsearch` | 2 |
| `electron` | 8 |
| `email` | 39 |
| `embedded-device` | 3 |
| `encoding` | 59 |
| `express` | 6 |
| `file-upload` | 77 |
| `filter-bypass` | 250 |
| `flash` | 49 |
| `flask` | 3 |
| `formal-analysis` | 30 |
| `ftp` | 8 |
| `fuzzing` | 40 |
| `gadget-chain` | 76 |
| `gcp` | 8 |
| `github` | 19 |
| `github-actions` | 7 |
| `gitlab` | 4 |
| `go` | 10 |
| `graphql` | 2 |
| `hash-collision` | 1 |
| `header-injection` | 55 |
| `http` | 180 |
| `http2` | 23 |
| `http3` | 5 |
| `https` | 100 |
| `idor` | 26 |
| `iframe` | 118 |
| `info-leak` | 512 |
| `injection` | 105 |
| `ios` | 16 |
| `java` | 111 |
| `javascript` | 336 |
| `javascript-runtime` | 15 |
| `jenkins` | 1 |
| `joomla` | 4 |
| `jwt` | 13 |
| `kubernetes` | 3 |
| `laravel` | 1 |
| `large-scale-scan` | 111 |
| `lfi` | 27 |
| `llm` | 3 |
| `load-balancer` | 15 |
| `mass-assignment` | 10 |
| `measurement-study` | 199 |
| `mime` | 34 |
| `mitigation` | 158 |
| `mongodb` | 4 |
| `mssql` | 10 |
| `mutation-xss` | 9 |
| `mysql` | 23 |
| `nextjs` | 10 |
| `nodejs` | 57 |
| `nosqli` | 3 |
| `novel-technique` | 687 |
| `oauth` | 51 |
| `open-redirect` | 56 |
| `openid` | 23 |
| `parser-differential` | 136 |
| `passkeys` | 2 |
| `path-traversal` | 51 |
| `pdf` | 21 |
| `perl` | 4 |
| `phishing` | 25 |
| `php` | 97 |
| `postgres` | 6 |
| `postmessage` | 28 |
| `prior-art-extension` | 48 |
| `privilege-escalation` | 87 |
| `prompt-injection` | 3 |
| `prototype-pollution` | 16 |
| `proxy` | 73 |
| `python` | 27 |
| `race-condition` | 25 |
| `rag` | 1 |
| `rails` | 16 |
| `rce` | 215 |
| `react` | 4 |
| `redis` | 3 |
| `request-smuggling` | 36 |
| `response-splitting` | 11 |
| `rest-api` | 40 |
| `reverse-proxy` | 48 |
| `ruby` | 28 |
| `rust` | 3 |
| `same-origin-policy` | 155 |
| `saml` | 15 |
| `sandbox-escape` | 59 |
| `sanitizer-bypass` | 71 |
| `service-worker` | 10 |
| `session-fixation` | 31 |
| `side-channel` | 183 |
| `smtp` | 16 |
| `smuggling` | 14 |
| `snmp` | 2 |
| `soap` | 12 |
| `sop-bypass` | 165 |
| `spring` | 13 |
| `sqli` | 57 |
| `sso` | 55 |
| `ssrf` | 84 |
| `ssti` | 13 |
| `static-analysis` | 57 |
| `struts` | 4 |
| `supply-chain` | 37 |
| `survey` | 17 |
| `symfony` | 1 |
| `timing-attack` | 78 |
| `tls` | 104 |
| `toctou` | 12 |
| `tooling` | 243 |
| `typosquatting` | 9 |
| `ui-redress` | 63 |
| `unicode` | 25 |
| `url-parsing` | 102 |
| `url-spoofing` | 9 |
| `user-enumeration` | 4 |
| `vendor-advisory` | 52 |
| `vue` | 1 |
| `waf` | 15 |
| `waf-bypass` | 61 |
| `wasm` | 1 |
| `webassembly` | 3 |
| `webauthn` | 3 |
| `webrtc` | 9 |
| `websocket` | 7 |
| `wordpress` | 15 |
| `xsleak` | 66 |
| `xss` | 312 |
| `xxe` | 30 |

### Used exactly once

Review these before reusing them: `Crypto`, `HTTP`, `Identity`, `XSS`, `captcha-bypass`, `dependency-confusion`, `hash-collision`, `jenkins`, `laravel`, `rag`, `symfony`, `vue`, `wasm`
