# Security policy

Thanks for looking. This is a volunteer-run, open-source archive.
**There is no bug bounty and no payment of any kind.** Reports are welcome on
those terms, and valid ones are credited in the published advisory unless you
ask otherwise.

## Reporting

Report privately through GitHub security advisories:

**<https://github.com/irsdl/webhacklist/security/advisories>**

That form stays private between you and the maintainer until an advisory is
published. Please use it rather than a public issue for anything exploitable.
If you cannot use GitHub at all, open a normal issue saying only that you have
a security report and asking for a contact route — do not put the details in it.

The same policy is published at <https://webhacklist.com/security/> and
<https://webhacklist.com/.well-known/security.txt>.

## What this project actually is

A static archive. No accounts, no login, no database, no server-side code — it
serves files. Findings that assume a backend generally do not apply.

## In scope

- `webhacklist.com` and its published assets.
- The site code in this repository: the app shell, the archive reader, the PDF
  viewer, and the build and reference tooling.
- Anything that lets preserved content escape its context — script execution
  from an archived document, the PDF reader, or the content-security policy.

## Out of scope

- **Vulnerabilities in the preserved research itself.** This archive stores
  copies of published security research. Exploit code and payloads inside a
  preserved document are the evidence, are meant to be there, and are served as
  inert text. A payload in an archived article is not a finding.
- Findings against the original websites the archive links to. Those belong to
  their owners — report to them.
- Denial of service, volumetric testing, and anything degrading the service for
  others.
- Social engineering, physical attacks, and the maintainer's personal accounts.
- Automated scanner output with no working proof of concept, and missing-header
  reports with no exploitable consequence on a static, cookieless origin.

## Testing rules

Test against your own copy where you can — the whole site builds and runs
locally from this repository. Against the live site, keep to what a single
browser can do by hand. No scanners, no floods, and nothing aimed beyond the
public files.

## What to expect

This is maintained in spare time, so a first reply may take a couple of weeks.
Valid issues are fixed and published as a GitHub advisory with credit. Not every
report will be treated as a vulnerability, and the reasoning will be explained
when it is not.

## Not a security issue

A wrong byline, a bad capture, a dead link or a misattributed technique is very
welcome as a normal [issue](https://github.com/irsdl/webhacklist/issues). If you
are an author who wants a preserved copy of your own work corrected or removed,
open an issue and say so — that is honoured.
