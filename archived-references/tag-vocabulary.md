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

184 tags, across 1193 documents that carry a digest.

| Tag | Documents |
|---|---|
| `Crypto` | 1 |
| `HTTP` | 1 |
| `Identity` | 1 |
| `Injection` | 3 |
| `Server` | 3 |
| `XSS` | 1 |
| `abuse-of-functionality` | 2 |
| `activex` | 3 |
| `ai-agent` | 4 |
| `algorithmic-complexity` | 21 |
| `android` | 31 |
| `angular` | 3 |
| `aspnet` | 37 |
| `attack-chain` | 132 |
| `auth-bypass` | 240 |
| `aws` | 25 |
| `azure` | 6 |
| `browser-extension` | 50 |
| `browser-fingerprinting` | 2 |
| `bug-bounty` | 149 |
| `cache` | 55 |
| `cache-deception` | 9 |
| `cache-poisoning` | 58 |
| `case-study` | 215 |
| `cdn` | 36 |
| `charset` | 24 |
| `ci-cd` | 14 |
| `class-pollution` | 3 |
| `clickjacking` | 51 |
| `cloudflare` | 8 |
| `command-injection` | 36 |
| `content-type` | 23 |
| `cookie` | 115 |
| `cors` | 25 |
| `csp` | 50 |
| `csrf` | 94 |
| `css` | 52 |
| `css-injection` | 20 |
| `csti` | 4 |
| `cve` | 190 |
| `database` | 42 |
| `deanonymization` | 2 |
| `defence` | 48 |
| `dependency-confusion` | 1 |
| `deserialization` | 60 |
| `desync` | 27 |
| `detection` | 74 |
| `django` | 7 |
| `dns` | 61 |
| `dns-rebinding` | 18 |
| `docker` | 3 |
| `dom` | 111 |
| `dom-clobbering` | 11 |
| `dos` | 80 |
| `dotnet` | 52 |
| `drupal` | 4 |
| `dynamic-analysis` | 60 |
| `elasticsearch` | 2 |
| `electron` | 8 |
| `email` | 34 |
| `encoding` | 51 |
| `express` | 6 |
| `file-upload` | 61 |
| `filter-bypass` | 214 |
| `flash` | 32 |
| `flask` | 3 |
| `formal-analysis` | 28 |
| `ftp` | 6 |
| `fuzzing` | 40 |
| `gadget-chain` | 76 |
| `gcp` | 8 |
| `github` | 19 |
| `github-actions` | 7 |
| `gitlab` | 4 |
| `go` | 10 |
| `graphql` | 2 |
| `header-injection` | 48 |
| `http` | 165 |
| `http2` | 23 |
| `http3` | 5 |
| `https` | 91 |
| `idor` | 23 |
| `iframe` | 96 |
| `info-leak` | 450 |
| `injection` | 96 |
| `ios` | 16 |
| `java` | 98 |
| `javascript` | 281 |
| `javascript-runtime` | 12 |
| `jenkins` | 1 |
| `joomla` | 4 |
| `jwt` | 13 |
| `kubernetes` | 3 |
| `laravel` | 1 |
| `large-scale-scan` | 105 |
| `lfi` | 26 |
| `llm` | 3 |
| `load-balancer` | 15 |
| `mass-assignment` | 10 |
| `measurement-study` | 190 |
| `mime` | 22 |
| `mitigation` | 125 |
| `mongodb` | 4 |
| `mssql` | 7 |
| `mutation-xss` | 9 |
| `mysql` | 18 |
| `nextjs` | 10 |
| `nodejs` | 57 |
| `nosqli` | 3 |
| `novel-technique` | 562 |
| `oauth` | 51 |
| `open-redirect` | 48 |
| `openid` | 20 |
| `parser-differential` | 130 |
| `passkeys` | 2 |
| `path-traversal` | 49 |
| `pdf` | 19 |
| `perl` | 3 |
| `phishing` | 6 |
| `php` | 81 |
| `postgres` | 6 |
| `postmessage` | 26 |
| `prior-art-extension` | 43 |
| `privilege-escalation` | 78 |
| `prompt-injection` | 3 |
| `prototype-pollution` | 16 |
| `proxy` | 61 |
| `python` | 26 |
| `race-condition` | 22 |
| `rag` | 1 |
| `rails` | 16 |
| `rce` | 193 |
| `react` | 4 |
| `redis` | 3 |
| `request-smuggling` | 35 |
| `response-splitting` | 6 |
| `rest-api` | 40 |
| `reverse-proxy` | 48 |
| `ruby` | 28 |
| `rust` | 3 |
| `same-origin-policy` | 123 |
| `saml` | 15 |
| `sandbox-escape` | 48 |
| `sanitizer-bypass` | 62 |
| `service-worker` | 10 |
| `session-fixation` | 28 |
| `side-channel` | 157 |
| `smtp` | 15 |
| `smuggling` | 13 |
| `soap` | 11 |
| `sop-bypass` | 124 |
| `spring` | 13 |
| `sqli` | 47 |
| `sso` | 54 |
| `ssrf` | 74 |
| `ssti` | 13 |
| `static-analysis` | 56 |
| `struts` | 4 |
| `supply-chain` | 33 |
| `survey` | 17 |
| `symfony` | 1 |
| `timing-attack` | 66 |
| `tls` | 96 |
| `toctou` | 10 |
| `tooling` | 221 |
| `typosquatting` | 9 |
| `ui-redress` | 58 |
| `unicode` | 21 |
| `url-parsing` | 91 |
| `url-spoofing` | 3 |
| `user-enumeration` | 1 |
| `vendor-advisory` | 42 |
| `vue` | 1 |
| `waf` | 15 |
| `waf-bypass` | 58 |
| `wasm` | 1 |
| `webassembly` | 3 |
| `webauthn` | 3 |
| `webrtc` | 9 |
| `websocket` | 7 |
| `wordpress` | 13 |
| `xsleak` | 57 |
| `xss` | 262 |
| `xxe` | 29 |

### Used exactly once

Review these before reusing them: `Crypto`, `HTTP`, `Identity`, `XSS`, `dependency-confusion`, `jenkins`, `laravel`, `rag`, `symfony`, `user-enumeration`, `vue`, `wasm`
