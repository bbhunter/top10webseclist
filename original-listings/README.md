# original-listings/

PDF snapshots of the **original announcement pages** behind every year of the Top
10 Web Hacking Techniques — captured so the record survives its hosts. For each
year that means two things:

1. **`*-nominees.pdf`** — the full list of everything nominated that year, not just
   the winners.
2. **`*-top10.pdf`** — the post announcing the ten techniques finally selected.

Generated with [`tools/capture_pdf.py`](../tools/capture_pdf.py) (headless Chrome
over CDP). Re-run `python tools/capture_pdf.py verify` to re-check every file, or
`run --only <year>` to add a year. Provenance for every file — source URL, HTTP
status, page count — is in [`tools/sources.json`](../tools/sources.json) and
[`tools/capture-report.json`](../tools/capture-report.json).

## The three eras

| Years | Curator | Host | State |
| --- | --- | --- | --- |
| 2006-2010 | Jeremiah Grossman | `jeremiahgrossman.blogspot.com` | **Live**, now serving as `blog.jeremiahgrossman.com` |
| 2011-2015 | Jeremiah Grossman / Johnathan Kuskos | `whitehatsec.com/blog` | **Dead** — captured from the Wayback Machine |
| 2016/17-2025 | James Kettle | `portswigger.net/research` | **Live** |

## Files

| Year | Nominees | Top 10 | Notes |
| --- | --- | --- | --- |
| 2025 | [2025-nominees.pdf](2025-nominees.pdf) | [2025-top10.pdf](2025-top10.pdf) | #1 Successful Errors |
| 2024 | [2024-nominees.pdf](2024-nominees.pdf) | [2024-top10.pdf](2024-top10.pdf) | Biggest nominee list ever (~100+); #1 Confusion Attacks |
| 2023 | [2023-nominees.pdf](2023-nominees.pdf) | [2023-top10.pdf](2023-top10.pdf) | #1 Smashing the state machine |
| 2022 | [2022-nominees.pdf](2022-nominees.pdf) | [2022-top10.pdf](2022-top10.pdf) | #1 Account hijacking using dirty dancing in sign-in OAuth-flows |
| 2021 | [2021-nominees.pdf](2021-nominees.pdf) | [2021-top10.pdf](2021-top10.pdf) | #1 Dependency Confusion |
| 2020 | [2020-nominees.pdf](2020-nominees.pdf) | [2020-top10.pdf](2020-top10.pdf) | #1 H2C Smuggling |
| 2019 | [2019-nominees.pdf](2019-nominees.pdf) | [2019-top10.pdf](2019-top10.pdf) | #1 Cached and Confused |
| 2018 | [2018-nominees.pdf](2018-nominees.pdf) | [2018-top10.pdf](2018-top10.pdf) | 59 nominations; #1 Breaking Parser Logic |
| 2016/17 | [2016-17-nominees.pdf](2016-17-nominees.pdf) | [2016-17-top10.pdf](2016-17-top10.pdf) | Plus [2016-17-voting.pdf](2016-17-voting.pdf), the 36-technique ballot. #1 A New Era of SSRF |
| 2015 | [2015-nominees-and-top10.pdf](2015-nominees-and-top10.pdf) | *(same file)* | #1 FREAK |
| 2014 | [2014-nominees-and-top10.pdf](2014-nominees-and-top10.pdf) | *(same file)* | #1 Heartbleed |
| 2013 | [2013-nominees-and-top10.pdf](2013-nominees-and-top10.pdf) | *(same file)* | #1 Mutation XSS |
| 2012 | [2012-nominees-and-top10.pdf](2012-nominees-and-top10.pdf) | *(same file)* | #1 CRIME |
| 2011 | [2011-nominees.pdf](2011-nominees.pdf) | [2011-top10.pdf](2011-top10.pdf) | 'The Big List' of 51 nominees; #1 BEAST |
| 2010 | [2010-nominees.pdf](2010-nominees.pdf) | [2010-top10.pdf](2010-top10.pdf) | Plus [2010-finalists.pdf](2010-finalists.pdf), the Final 15 — unique to this year |
| 2009 | [2009-nominees.pdf](2009-nominees.pdf) | [2009-top10.pdf](2009-top10.pdf) | 82 candidates |
| 2008 | [2008-nominees.pdf](2008-nominees.pdf) | [2008-top10.pdf](2008-top10.pdf) | ~70 candidates |
| 2007 | [2007-nominees.pdf](2007-nominees.pdf) | [2007-top10.pdf](2007-top10.pdf) | 80+ candidates |
| 2006 | [2006-nominees-and-top10.pdf](2006-nominees-and-top10.pdf) | *(same file)* | The first year |

## Where the originals live

The pages each PDF was rendered from. Nine years still resolve on their original host;
the WhiteHat era (2011–2015) only survives through the Wayback Machine, which is what
prompted this archive. The same URLs, with HTTP status and page count per capture, are
in [`tools/sources.json`](../tools/sources.json) and
[`tools/capture-report.json`](../tools/capture-report.json).

| Year | Original announcement pages | Host |
| --- | --- | --- |
| 2025 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2025-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2025) | live |
| 2024 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2024-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2024) | live |
| 2023 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2023-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2023) | live |
| 2022 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2022-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2022) | live |
| 2021 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2021-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2021) | live |
| 2020 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2020-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2020) | live |
| 2019 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2019-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2019) | live |
| 2018 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2018-nominations-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2018) | live |
| 2016/17 | [nominees](https://portswigger.net/research/top-10-web-hacking-techniques-of-2017-nominations-open) · [voting](https://portswigger.net/research/top-10-web-hacking-techniques-of-2017-voting-open) · [top 10](https://portswigger.net/research/top-10-web-hacking-techniques-of-2017) | live |
| 2015 | [nominees + top 10](https://web.archive.org/web/20171225140648/https://www.whitehatsec.com/blog/top-10-web-hacking-techniques-of-2015/) | Wayback — original host gone |
| 2014 | [nominees + top 10](https://web.archive.org/web/20160319055228/https://www.whitehatsec.com/blog/top-10-web-hacking-techniques-of-2014/) | Wayback — original host gone |
| 2013 | [nominees + top 10](https://web.archive.org/web/20160312115418/https://www.whitehatsec.com/blog/top-10-web-hacking-techniques-2013/) | Wayback — original host gone |
| 2012 | [nominees + top 10](https://web.archive.org/web/20170903113359/https://www.whitehatsec.com/blog/top-ten-web-hacking-techniques-of-2012/) | Wayback — original host gone |
| 2011 | [nominees](https://web.archive.org/web/20170831160914/https://www.whitehatsec.com/blog/vote-now-top-ten-web-hacking-techniques-of-2011/) · [top 10](https://web.archive.org/web/20150109120123/https://www.whitehatsec.com/resource/grossmanarchives/12grossmanarchives/022112topten2011.html) | Wayback — original host gone |
| 2010 | [nominees](https://blog.jeremiahgrossman.com/2010/11/calling-all-security-researchers-submit.html) · [final 15](https://blog.jeremiahgrossman.com/2011/01/final-fifteen-web-hacking-techniques.html) · [top 10](https://blog.jeremiahgrossman.com/2011/01/top-ten-web-hacking-techniques-of-2010.html) | live |
| 2009 | [nominees](https://blog.jeremiahgrossman.com/2009/12/attention-security-researchers-submit.html) · [top 10](https://blog.jeremiahgrossman.com/2010/01/top-ten-web-hacking-techniques-of-2009.html) | live |
| 2008 | [nominees](https://blog.jeremiahgrossman.com/2009/01/calling-all-researchers-send-in-top-web.html) · [top 10](https://blog.jeremiahgrossman.com/2009/02/top-ten-web-hacking-techniques-of-2008.html) | live |
| 2007 | [nominees](https://blog.jeremiahgrossman.com/2008/01/polls-are-open-top-10-web-hacks-of-2007.html) · [top 10](https://blog.jeremiahgrossman.com/2008/01/top-ten-web-hacks-of-2007-official.html) | live |
| 2006 | [nominees + top 10](https://blog.jeremiahgrossman.com/2006/12/top-10-web-hacks-of-2006.html) | live |

> [!NOTE]
> The WhiteHat-era posts carry a reader comment thread in which people suggest further
> research. Those suggestions are not part of the published nominee list, and the year
> files deliberately don't include them — only what the organisers actually listed.

## Why some years are a single file

Two years' worth of caveats are baked into the filenames, because the process
itself wasn't uniform:

- **2012-2015 (`-nominees-and-top10`)** — WhiteHat ran each year as *one living
  blog post*, edited in place as the cycle progressed. By the end, a single page
  held the complete nominee list, the Final 15, and the Top 10. There is no
  separate results URL to capture, so the distinction is *which snapshot you
  pick*, and the late snapshots used here contain every stage. Two snapshots are
  deliberately avoided: `20160409042357` for 2015 and `20121209035519` for 2012
  are nominations-stage only and have no Top 10.
- **2006 (`-nominees-and-top10`)** — the series' first year had no nominations
  post at all. The single December 2006 post carries the ranked ten, honourable
  mentions, and the full candidate list together.
- **2016 has no list of its own.** The series lapsed after WhiteHat's 2015 edition
  and PortSwigger revived it for 2017, explicitly inviting standout 2016 research;
  the results post is titled "top 10 web hacking techniques of 2017 (and 2016)"
  and #10 is a 2016 technique. So 2016 and 2017 share one set of files, matching
  [2016-17.md](../2016-17.md).
- **2011** is the one WhiteHat-era year with a genuinely distinct results page,
  so it gets a clean two-file split.
- **Voting pages generally can't be archived.** 2017 is the only year with a
  public `voting-open` page; from 2018 PortSwigger moved voting to polls that now
  render just "This poll is now closed", with no candidates.
