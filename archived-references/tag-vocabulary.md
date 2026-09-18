# Tag vocabulary
The controlled vocabulary for `digest.tags` in `archived-references/manifest.json`.

**The record is [tag-vocabulary.json](tag-vocabulary.json); this file is a reading
of it.** Both are generated — edit the JSON, never this. Counts are recomputed from
the manifest on every rebuild; `aliases` and the OWASP mapping are stated by hand in
the JSON and survive untouched.

## How to use it
- Up to 10 tags per document. There is no minimum: a document honestly served by
  one tag keeps one.
- **Use a tag from the list before inventing one.** That is the whole point of a
  vocabulary — a reader searching `prototype-pollution` should find every document
  about it, not the two-thirds that happened to pick that spelling.
- A tag the list does not have is still allowed. Write it, and it is adopted and
  reported. Refusing it threw away the one moment someone had actually read the
  document. A `?` prefix still marks it as a proposal you want looked at, and it is
  kept rather than stripped.
- Tags must name the **techniques the research actually uses**. That is what a
  reader searches for, and no count can check it.
- A tag is a retrieval key, not a summary. If it would apply to almost every
  document in the archive, it is not earning its place.

## How drift is prevented
Not by refusal — by folding, before anything is written:

- **Case and punctuation never make a second tag.** `XSS`, `xss` and `  XSS ` are
  one tag. The archive did carry both spellings; the capitalised one had a single
  document.
- **A synonym is folded by an alias.** Add it to `aliases` in the JSON and the old
  spelling can never be published again — `wasm` publishes as `webassembly`.
- `sop-bypass` and `same-origin-policy` deliberately coexist, for the attack and the
  mechanism. Do not add a third spelling of either.
- **Two names for one thing are kept when a reader might arrive by either.** Tags
  are a way IN — for people and for models searching the archive — so `passkeys`
  and `webauthn` both stay, on all ten documents, even though they co-occur
  perfectly. An alias is for a spelling nobody should land on (`wasm`), not for a
  word somebody would reasonably search.

A tag that has fallen to zero documents is **kept**, at `documents: 0`. It was
agreed once, and deleting it would let the same word be re-argued later and would
throw away its OWASP mapping.

**An alias to the empty string retires a word for good.** It resolves to nothing
and is dropped before publication, so a tag that was decided against cannot come
back by being typed again. Three are retired:

| Retired | Why |
|---|---|
| `novel-technique` | was on 743 documents, 45% of the archive. This is a list OF novel techniques, so the tag restated the premise and narrowed no search |
| `server` | three unrelated documents — a botnet scan, a Rails YAML bug, an XML retrieval talk — left over from folding the capitalised `Server` |
| `malicious-server` | one document, and "the attacker controls a server" describes a large share of the archive |

`smuggling` is deliberately NOT folded into `request-smuggling`: it carries cookie,
header and data smuggling, and merging it would mislabel most of its documents.

## OWASP Top 10
Categories are **derived, never typed**. A reviewer tags the techniques; the mapping
in the JSON turns those into categories, which reach the published file as
`owasp-a03-2021` and so on. Nobody tags a document twice, and nobody has to remember
which category a technique belongs to. The mapping is a judgement — edit it in the
JSON.

## The vocabulary

207 tags, across 1925 documents that carry a digest.

| Tag | Documents | OWASP |
|---|---|---|
| `abuse-of-functionality` | 74 | A04:2021 |
| `active-directory` | 1 | — |
| `activex` | 13 | — |
| `ai-agent` | 65 | — |
| `algorithmic-complexity` | 36 | A04:2021 |
| `android` | 35 | — |
| `angular` | 3 | — |
| `argument-injection` | 3 | A03:2021 |
| `aspnet` | 54 | — |
| `attack-chain` | 224 | — |
| `auth-bypass` | 346 | A01:2021 |
| `autofill` | 4 | — |
| `aws` | 36 | — |
| `azure` | 14 | — |
| `blind-xss` | 1 | A03:2021 |
| `blockchain` | 8 | — |
| `browser-extension` | 80 | — |
| `browser-fingerprinting` | 25 | — |
| `browser-history` | 2 | — |
| `bug-bounty` | 168 | — |
| `cache` | 76 | — |
| `cache-deception` | 11 | — |
| `cache-poisoning` | 102 | — |
| `captcha-bypass` | 3 | A04:2021 |
| `case-study` | 300 | — |
| `cdn` | 50 | — |
| `charset` | 40 | A02:2021 |
| `ci-cd` | 30 | A08:2021 |
| `class-pollution` | 5 | A08:2021 |
| `clickjacking` | 59 | A04:2021 |
| `clipboard` | 1 | — |
| `cloudflare` | 12 | — |
| `code-injection` | 3 | — |
| `command-injection` | 58 | A03:2021 |
| `content-type` | 43 | A05:2021 |
| `cookie` | 156 | A07:2021 |
| `cors` | 29 | A01:2021 |
| `crypto` | 15 | A02:2021 |
| `csp` | 71 | A05:2021 |
| `csrf` | 152 | A01:2021 |
| `css` | 77 | — |
| `css-injection` | 34 | A03:2021 |
| `csti` | 5 | A03:2021 |
| `cve` | 252 | — |
| `data-breach` | 5 | — |
| `database` | 72 | — |
| `deanonymization` | 20 | — |
| `defence` | 62 | — |
| `dependency-confusion` | 1 | A06:2021 |
| `deserialization` | 89 | A08:2021 |
| `desync` | 38 | — |
| `detection` | 139 | A09:2021 |
| `django` | 11 | — |
| `dns` | 95 | — |
| `dns-rebinding` | 36 | A10:2021 |
| `docker` | 6 | A05:2021 |
| `dom` | 148 | — |
| `dom-clobbering` | 15 | A08:2021 |
| `domain-takeover` | 2 | — |
| `dos` | 119 | — |
| `dotnet` | 78 | — |
| `drupal` | 6 | — |
| `dynamic-analysis` | 92 | — |
| `elasticsearch` | 3 | — |
| `electron` | 11 | — |
| `email` | 58 | — |
| `embedded-device` | 9 | — |
| `encoding` | 87 | — |
| `express` | 9 | — |
| `file-upload` | 95 | — |
| `file-write` | 4 | — |
| `filter-bypass` | 315 | A05:2021 |
| `flash` | 57 | — |
| `flask` | 6 | — |
| `formal-analysis` | 36 | — |
| `ftp` | 10 | — |
| `fuzzing` | 67 | — |
| `gadget-chain` | 107 | A08:2021 |
| `gcp` | 11 | — |
| `github` | 24 | — |
| `github-actions` | 20 | A08:2021 |
| `gitlab` | 7 | — |
| `go` | 16 | — |
| `graphql` | 9 | — |
| `hash-collision` | 5 | A02:2021 |
| `header-injection` | 78 | A03:2021 |
| `html-injection` | 2 | — |
| `html5` | 1 | — |
| `http` | 226 | — |
| `http2` | 32 | — |
| `http3` | 10 | — |
| `https` | 105 | A02:2021 |
| `identity` | 27 | A07:2021 |
| `idor` | 27 | A01:2021 |
| `iframe` | 140 | — |
| `info-leak` | 655 | — |
| `injection` | 140 | A03:2021 |
| `ios` | 16 | — |
| `jailbreak` | 4 | — |
| `java` | 128 | — |
| `javascript` | 401 | — |
| `javascript-runtime` | 22 | — |
| `jenkins` | 2 | — |
| `joomla` | 6 | — |
| `jwt` | 22 | A07:2021 |
| `kubernetes` | 6 | A05:2021 |
| `laravel` | 2 | — |
| `large-scale-scan` | 133 | — |
| `lfi` | 33 | A01:2021, A03:2021 |
| `llm` | 58 | — |
| `load-balancer` | 18 | — |
| `mass-assignment` | 12 | A01:2021 |
| `mcp` | 4 | — |
| `measurement-study` | 248 | — |
| `memory-corruption` | 5 | — |
| `mime` | 43 | A05:2021 |
| `mitigation` | 184 | — |
| `mongodb` | 6 | — |
| `mssql` | 11 | — |
| `mutation-xss` | 12 | A03:2021 |
| `mysql` | 23 | — |
| `nextjs` | 12 | — |
| `nginx` | 1 | — |
| `nodejs` | 75 | — |
| `nosqli` | 10 | A03:2021 |
| `ntlm` | 2 | — |
| `oauth` | 80 | A07:2021 |
| `open-redirect` | 66 | A04:2021 |
| `openid` | 34 | A07:2021 |
| `parser-differential` | 203 | — |
| `passkeys` | 12 | A07:2021 |
| `password-manager` | 5 | — |
| `path-traversal` | 75 | A01:2021 |
| `pdf` | 29 | — |
| `perl` | 4 | — |
| `phishing` | 41 | A04:2021 |
| `php` | 126 | — |
| `postgres` | 10 | — |
| `postmessage` | 38 | — |
| `predictable-token` | 7 | A02:2021 |
| `prior-art-extension` | 58 | — |
| `privilege-escalation` | 115 | A01:2021 |
| `prompt-injection` | 47 | A03:2021 |
| `prototype-pollution` | 29 | A08:2021 |
| `proxy` | 85 | — |
| `python` | 40 | — |
| `race-condition` | 33 | A04:2021 |
| `rag` | 5 | — |
| `rails` | 17 | — |
| `rce` | 306 | — |
| `react` | 6 | — |
| `redis` | 5 | — |
| `redos` | 3 | — |
| `request-smuggling` | 53 | — |
| `response-splitting` | 19 | A03:2021 |
| `rest-api` | 53 | — |
| `reverse-proxy` | 62 | — |
| `ruby` | 36 | — |
| `rust` | 3 | — |
| `same-origin-policy` | 188 | A01:2021 |
| `saml` | 18 | A07:2021 |
| `sandbox-escape` | 79 | — |
| `sanitizer-bypass` | 89 | A05:2021 |
| `service-worker` | 14 | — |
| `session-fixation` | 42 | A07:2021 |
| `side-channel` | 220 | — |
| `smb` | 1 | — |
| `smtp` | 19 | — |
| `smuggling` | 15 | — |
| `snmp` | 2 | — |
| `soap` | 14 | — |
| `sop-bypass` | 201 | A01:2021 |
| `spring` | 18 | — |
| `sqli` | 72 | A03:2021 |
| `sso` | 69 | A07:2021 |
| `ssrf` | 103 | A10:2021 |
| `ssti` | 24 | A03:2021 |
| `static-analysis` | 85 | — |
| `struts` | 4 | — |
| `subdomain-takeover` | 1 | — |
| `supply-chain` | 62 | A06:2021 |
| `survey` | 19 | — |
| `symfony` | 1 | — |
| `timing-attack` | 96 | — |
| `tls` | 115 | A02:2021 |
| `toctou` | 17 | A04:2021 |
| `tooling` | 342 | — |
| `type-confusion` | 1 | — |
| `typosquatting` | 9 | A06:2021 |
| `ui-redress` | 77 | A04:2021 |
| `unicode` | 41 | — |
| `uri-scheme` | 2 | — |
| `url-parsing` | 126 | — |
| `url-spoofing` | 12 | — |
| `user-enumeration` | 9 | A04:2021 |
| `vendor-advisory` | 57 | — |
| `vue` | 1 | — |
| `waf` | 17 | A05:2021 |
| `waf-bypass` | 77 | A05:2021 |
| `webassembly` | 4 | — |
| `webauthn` | 13 | A07:2021 |
| `webrtc` | 11 | — |
| `websocket` | 12 | — |
| `wordpress` | 22 | — |
| `xsleak` | 76 | — |
| `xss` | 416 | A03:2021 |
| `xxe` | 34 | A03:2021 |

### Never published

These spellings fold into another tag before anything is written:

| Written | Published as |
|---|---|
| `malicious-server` | `` |
| `novel-technique` | `` |
| `server` | `` |
| `wasm` | `webassembly` |

### OWASP Top 10:2021

A document earns these from the techniques it is already tagged with; nobody tags them by hand.

| Category | Tags |
|---|---|
| `A01:2021` Broken Access Control | `auth-bypass`, `cors`, `csrf`, `directory-listing`, `idor`, `lfi`, `mass-assignment`, `path-traversal`, `privilege-escalation`, `same-origin-policy`, `sop-bypass` |
| `A02:2021` Cryptographic Failures | `charset`, `crypto`, `hash-collision`, `https`, `predictable-token`, `tls` |
| `A03:2021` Injection | `argument-injection`, `blind-xss`, `command-injection`, `css-injection`, `csti`, `header-injection`, `injection`, `lfi`, `mutation-xss`, `nosqli`, `prompt-injection`, `response-splitting`, `sqli`, `ssti`, `xss`, `xxe` |
| `A04:2021` Insecure Design | `abuse-of-functionality`, `algorithmic-complexity`, `captcha-bypass`, `clickjacking`, `open-redirect`, `phishing`, `race-condition`, `toctou`, `ui-redress`, `user-enumeration` |
| `A05:2021` Security Misconfiguration | `content-type`, `csp`, `docker`, `filter-bypass`, `kubernetes`, `mime`, `sanitizer-bypass`, `waf`, `waf-bypass` |
| `A06:2021` Vulnerable and Outdated Components | `dependency-confusion`, `supply-chain`, `typosquatting` |
| `A07:2021` Identification and Authentication Failures | `cookie`, `identity`, `jwt`, `oauth`, `openid`, `passkeys`, `saml`, `session-fixation`, `sso`, `webauthn` |
| `A08:2021` Software and Data Integrity Failures | `ci-cd`, `class-pollution`, `deserialization`, `dom-clobbering`, `gadget-chain`, `github-actions`, `prototype-pollution` |
| `A09:2021` Security Logging and Monitoring Failures | `detection` |
| `A10:2021` Server-Side Request Forgery | `dns-rebinding`, `ssrf` |

### Used exactly once

Review these before reusing them: `active-directory`, `blind-xss`, `clipboard`, `dependency-confusion`, `html5`, `nginx`, `smb`, `subdomain-takeover`, `symfony`, `type-confusion`, `vue`
