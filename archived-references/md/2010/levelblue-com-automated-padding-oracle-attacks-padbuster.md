---
type: Article
title: Automated Padding Oracle Attacks with PadBuster
resource: "http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/"
tags: [article, webseclist-reference, en, gdssecurity-com]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:35:22+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/"
    title: Automated Padding Oracle Attacks with PadBuster
    author: Brian Holyfield
  - id: capture
    resource: "https://web.archive.org/web/20110723192819/http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/"
also_at: []
authors:
  - Brian Holyfield
canonical_url: ""
cited_by:
  - "2010.md:5"
commit: ""
content_sha256: 29e131683b14ba939b509752e3983199fbe497df42a271193a48e98d169fcf07
depth: full
depth_reason: default
kind: article
language: en
licence: unknown
original_url: "http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/"
published: ""
publisher: gdssecurity.com
publisher_english: ""
raw_sha256: 6f3a92df1e702b848dbf24fabcc221aedb7067f484838a468f8f763a40978af1
retrieved_from: "http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:35:22+00:00"
slug: levelblue-com-automated-padding-oracle-attacks-padbuster
snapshot: 20110723192819
title_english: ""
translation_file: ""
translation_of: ""
---

# Automated Padding Oracle Attacks with PadBuster

**Automated Padding Oracle Attacks with PadBuster** - Brian Holyfield, gdssecurity.com.

- Published: date not stated
- Original: <http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/>
- Preserved from: http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/ (stored) on 2026-08-11
- Capture timestamp: 20110723192819
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

Automated Padding Oracle Attacks with PadBuster - Gotham Digital Science

[About](http://www.gdssecurity.com/g/a.php)|[Careers](http://www.gdssecurity.com/g/ca.php)|[Press](http://www.gdssecurity.com/g/pr.php)|[News](http://www.gdssecurity.com/g/ne.php)|[Case Studies](http://www.gdssecurity.com/g/cs.php)|[Tools](http://www.gdssecurity.com/l/t.php)|[Blog](http://www.gdssecurity.com/l/b/)

[![](http://www.gdssecurity.com/images/gds_logo_2.png)](http://www.gdssecurity.com/)

  Sep   14   2010

## [Automated Padding Oracle Attacks with PadBuster](http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/)

Published by Brian Holyfield at 9:20 am under [Application Security](http://www.gdssecurity.com/l/b/category/application-security/),[Tools](http://www.gdssecurity.com/l/b/category/tools/)

There’s been a lot of buzz recently about Padding Oracle Attacks, an attack vector demonstrated by [Juliano Rizzo and Thai Duong](http://netifera.com/research/) during their presentation at BlackHat Europe earlier this summer. While padding oracles are relatively easy to exploit, the act of exploiting them can be time consuming if you don’t have a good way of automating the attack. The lack of good tools for identifying and exploiting padding oracles led us to develop our own internal padding oracle exploit script, PadBuster, which we’ve decided to share with the community. [The tool can be downloaded here](https://www.gdssecurity.com/l/t/d.php?k=PadBuster), but I’ll spend a little bit of time discussing how the tool works and the various use cases it supports.

Update 9/28/10: [PadBuster v0.2](http://www.gdssecurity.com/l/b/2010/09/28/new-version-of-padbuster-available-for-download/) has been released.

**Some Background**

Before we discuss using PadBuster, let’s briefly discuss the fundamentals of a classic padding oracle attack. As the term implies, a critical concept behind a padding oracle attack is the notion of cryptographic padding. Plaintext messages come in a variety of lengths; however, block ciphers require that all messages be an exact number of blocks. To satisfy this requirement, padding is used to ensure that a given plaintext message can always be divided into an exact number of blocks.

While several padding schemes exist, one of the most common padding schemes is described in the PKCS#5 standard. With PCKS#5 padding, the final block of plaintext is padded with N bytes (depending on the length of the last plaintext block) of value N. This is best illustrated through the examples below, which show words of varying length (FIG, BANANA, AVOCADO, PLANTAIN, PASSIONFRUIT) and how they would be padded using PKCS#5 padding (the examples below use 8-byte blocks).

[![](http://www.gdssecurity.com/l/po_fig1_sm.png)](http://www.gdssecurity.com/l/po_fig1.png)
 *Click to Enlarge*

Note that at least one padding byte is ALWAYS appended to the end of a string, so a 7-byte value (like AVOCADO) would be padded with 0×01 to fill the block, while an 8-byte value (like PLANTAIN) would have a full block of padding added to it. The value of the padding byte also indicates the number of bytes, so logically final value(s) at the end of the last block of ciphertext must either:

- A single 0×01 byte (0×01)
- Two 0×02 bytes (0×02, 0×02)
- Three 0×03 bytes (0×03, 0×03, 0×03)
- Four 0×04 bytes (0×04, 0×04, 0×04, 0×04)
- …and so on

If the final decrypted block does not end in one of these valid byte sequences, most cryptographic providers will throw an invalid padding exception. The fact that this exception gets thrown is critical for the attacker (us) as it is the basis of the padding oracle attack.

**A Basic Padding Oracle Attack Scenario**

To provide a concrete example, consider the following scenario:

*An application uses a query string parameter to pass the encrypted username, company id, and role id of a user. The parameter is encrypted using CBC mode, and each value uses a unique initialization vector (IV) which is pre-pended to the ciphertext. *

*When the application is passed an encrypted value, it responds in one of three ways:*

- *When a valid ciphertext is received (one that is properly padded and contains valid data) the application responds normally (200 OK)*
- *When an invalid ciphertext is received (one that, when decrypted, does not end with valid padding) the application throws a cryptographic exception (500 Internal Server Error)*
- *When a valid ciphertext is received (one that is properly padded) but decrypts to an invalid value, the application displays a custom error message (200 OK)*

The scenario described above is a classic Padding Oracle, because we can use the behavior of the application to easily determine whether the supplied encrypted value is properly padded or not. The term oracle refers to a mechanism that can be used to determine whether a test has passed or failed.

 Now that the scenario has been laid out, let’s take a look at one of the encrypted parameters used by the application. This parameter is used by the application to store a semi-colon delimited series of values that, in our example, include the user’s name (BRIAN), company id (12), and role id (2). The value, in plaintext, can be represented as **BRIAN;12;2;**. A sample of the encrypted query string parameter is shown below for reference. Note that the encrypted UID parameter value is encoded using ASCII Hex representation.

```
http://sampleapp/home.jsp?UID=7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6
```

At this point, an attacker would not have any idea what the underlying plaintext is, but for the sake of this example, we already know the plaintext value, the padded plaintext value, and the encrypted value (see diagram below). As we mentioned previously, the initialization vector is pre-pended to the ciphertext, so the first block of 8 bytes is just that.

![](http://www.gdssecurity.com/l/po_fig2_sm.png)

As for the block size, an attacker would see that the length of the encrypted ciphertext is 24 bytes. Since this number is evenly divisible by 8 and not divisible by 16, one can conclude that you are dealing with a block size of 8 bytes. Now, for reference take a look at what happens internally when this value is encrypted and decrypted. We see the process byte-for-byte in the diagram as this information will be helpful later on when discussing the exploit. Also note that the circled plus sign represents the XOR function.

**Encryption Diagram (Click to Enlarge):**
 [![](http://www.gdssecurity.com/l/po_fig3_sm.png)](http://www.gdssecurity.com/l/po_fig3.png)

**Decryption Diagram (Click to Enlarge):**
 [![](http://www.gdssecurity.com/l/po_fig4_sm.png)](http://www.gdssecurity.com/l/po_fig4.png)

It is also worthwhile to point out that the last block (Block 2 of 2), when decrypted, ends in a proper padding sequence as expected. If this were not the case, the cryptographic provider would throw an invalid padding exception.

**The Padding Oracle Decryption Exploit**

Let’s now look at how we can decrypt the value by using the padding oracle attack. We operate on a single encrypted block at a time, so we can start by isolating just the first block of ciphertext (the one following the IV) and sending it to the application pre-pended with an IV of all NULL values. The URL and associated response are shown below:

```
Request:  http://sampleapp/home.jsp?UID=0000000000000000F851D6CC68FC9537
```

```
Response:  500 - Internal Server Error
```

A 500 error response makes sense given that this value is not likely to result in anything valid when decrypted. The diagram below shows a closer look at what happens underneath the covers when the application attempts to decrypt this value. You should note that since we are only dealing with a single block of ciphertext (Block 1 of 1), the block MUST end with valid padding in order to avoid an invalid padding exception.

![](http://www.gdssecurity.com/l/po_fig5_sm.png)

As shown above, the exception is thrown because the block does not end with a valid padding sequence once decrypted. Now, let’s take a look at what happens when we send the exact same value but with the last byte of the initialization vector incremented by one.

```
Request: http://sampleapp/home.jsp?UID=0000000000000001F851D6CC68FC9537
```

```
Response: 500 - Internal Server Error
```

Like before, we also get a 500 exception. This is due to the fact that, like before, the value does not end in a valid padding sequence when decrypted. The difference however, is that if we take a closer look at what happens underneath the covers we will see that the final byte value is different than before (0x3C rather than 0x3D).

![](http://www.gdssecurity.com/l/po_fig6_sm.png)

If we repeatedly issue the same request and increment just the last byte in the IV each time (up to FF) we will inevitably hit a value that produces a valid padding sequence for a single byte of padding (0×01). Only one value (out of the possible 256 different bytes) will produce the correct padding byte of 0×01. When you hit this value, you should end up with a different response than the other 255 requests.

```
Request: http://sampleapp/home.jsp?UID=000000000000003CF851D6CC68FC9537
```

```
Response: 200 OK
```

Let’s take a look at the same diagram to see what happens this time.

![](http://www.gdssecurity.com/l/po_fig7_sm.png)

Given this is the case, we can now deduce the intermediary value byte at this position since we know that when XORed with 0x3C, it produces 0×01.

***If [Intermediary Byte] ^ 0x3C == 0×01,
 then [Intermediary Byte] == 0x3C ^ 0×01,
 so [Intermediary Byte] == 0x3D***

Taking this one step further, now that we know the intermediary byte value we can deduce what the actual decrypted value is. You’ll recall that during the decryption process, each intermediary value byte is XORed with the corresponding byte of the previous block of ciphertext (or the IV in the case of the first block). Since the example above is using the first block from the original sample, then we need to XOR this value with the corresponding byte from the original IV (0x0F) to recover the actual plaintext value. As expected, this gives us 0×32, which is the number "2" (the last plaintext byte in the first block).

Now that we’ve decrypted the 8th byte of the sample block, it’s time to move onto the 7th byte. In order to crack the 8th byte of the sample, we brute forced an IV byte that would produce a last decrypted byte value of 0×01 (valid padding). In order to crack the 7th byte, we need to do the same thing, but this time both the 7th and 8th byte must equal 0×02 (again, valid padding). Since we already know that the last intermediary value byte is 0x3D, we can update the 8th IV byte to 0x3F (which will produce 0×02) and then focus on brute forcing the 7th byte (starting with 0×00 and working our way up through 0xFF).

![](http://www.gdssecurity.com/l/po_fig8_sm.png)

Once again, we continue to generate padding exceptions until we hit the only value which produces a 7th decrypted byte value of 0×02 (valid padding), which in this case is 0×24.

![](http://www.gdssecurity.com/l/po_fig9_sm.png)

Using this technique, we can work our way backwards through the entire block until every byte of the intermediary value is cracked, essentially giving us access to the decrypted value (albeit one byte at a time). The final byte is cracked using an IV that produces an entire block of just padding (0×08) as shown below.

![](http://www.gdssecurity.com/l/po_fig10_sm.png)

**The Decryption Exploit with PadBuster**

Now let’s discuss how to use PadBuster to perform this exploit, which is fairly straightforward. PadBuster takes three mandatory arguments:

- URL – This is the URL that you want to exploit, including query string if present. There are optional switches to supply POST data (-post) and Cookies if needed (-cookies)
- Encrypted Sample – This is the encrypted sample of ciphertext included in the request. This value must also be present in either the URL, post or cookie values and will be replaced automatically on every test request
- Block Size – Size of the block that the cipher is using. This will normally be either 8 or 16, so if you are not sure you can try both

For this example, we will also use the command switch to specify how the encrypted sample is encoded. By default PadBuster assumes that the sample is Base64 encoded, however in this example the encrypted text is encoded as an uppercase ASCII HEX string. The option for specifying encoding (-encoding) takes one of the following three possible values:

- 0: Base64 (default)
- 1: Lowercase HEX ASCII
- 2: Uppercase HEX ASCII

The actual command we run will look like the following:

```
padBuster.pl http://sampleapp/home.jsp?UID=7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6
7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6 8 -encoding 2
```

Notice that we never told PadBuster how to recognize a padding error. While there is a command line option (-error) to specify the padding error message, by default PadBuster will analyze the entire first cycle (0-256) of test responses and prompt the user to choose which response pattern matches the padding exception. Typically the padding exception occurs on all but one of the initial test requests, so in most cases there will only be two response patterns to choose from as shown below (and PadBuster will suggest which one to use).

![](http://www.gdssecurity.com/l/po_pb1_sm.png)

The initial output from PadBuster is shown in the screenshot above. You’ll see that PadBuster re-issues the original request and shows the generated response information before starting its testing. This is useful for authenticated applications to ensure that the authentication cookies provided to PadBuster are working correctly.

Once a response pattern is selected, PadBuster will automatically cycle through each block and brute force each corresponding plaintext byte which will take, at most, 256 requests per byte. After each block, PadBuster will also display the obtained intermediary byte values along with the calculated plaintext. The intermediary values can be useful when performing arbitrary encryption exploits as we will show in the next section.

![](http://www.gdssecurity.com/l/po_pb2_sm.png)

**Encrypting Arbitrary Values**

We’ve just seen how a padding oracle and PadBuster can be used to decrypt the contents of any encrypted sample one block at a time. Now, let’s take a look at how you can encrypt arbitrary payloads using the same vulnerability.

You have probably noticed that once we are able to deduce the intermediary value for a given ciphertext block, we can manipulate the IV value in order to have complete control over the value that the ciphertext is decrypted to. So in the previous example of the first ciphertext block that we brute forced, if you want the block to decrypt to a value of "TEST" you can calculate the required IV needed to produce this value by XORing the desired plaintext against the intermediary value. So the string "TEST" (padded with four 0×04 bytes, of course) would be XORed against the intermediary value to produce the needed IV of 0x6D, 0×36, 0×70, 0×76, 0×03, 0x6E, 0×22, 0×39.

![](http://www.gdssecurity.com/l/po_fig11_sm.png)

This works great for a single block, but what if we want to generate an arbitrary value that is more than one block long? Let’s look at a real example to make it easier to follow. This time we will generate the encrypted string "ENCRYPT TEST" instead of just "TEST". The first step is to break the sample into blocks and add the necessary padding as shown below:

![](http://www.gdssecurity.com/l/po_fig12_sm.png)

When constructing more than a single block, we actually start with the last block and move backwards to generate a valid ciphertext. In this example, the last block is the same before, so we already know that the following IV and ciphertext will produce the string "TEST".

```
Request:  http://sampleapp/home.jsp?UID=6D367076036E2239F851D6CC68FC9537
```

Next, we need to figure out what intermediary value 6D367076036E2239 would decrypt to if it were passed as ciphertext instead of just an IV. We can do this by using the same technique used in the decryption exploit by sending it as the ciphertext block and starting our brute force attack with all nulls.

```
Request:  http://sampleapp/home.jsp?UID=00000000000000006D367076036E2239
```

Once we brute force the intermediary value, the IV can be manipulated to produce whatever text we want. The new IV can then be pre-pended to the previous sample, which produces the valid two-block ciphertext of our choice. This process can be repeated an unlimited number of times to encrypt data of any length.

**Encrypting Arbitrary Values with PadBuster**

PadBuster has the option to automate the process of creating arbitrary encrypted values in addition to decrypting them. There are three command line switches related to creating ciphertexts:

- *-plaintext [String]: plaintext to Encrypt*This is the plaintext you want to encrypt. This option is mandatory when using PadBuster to encrypt data, and its presence is what tells PadBuster to perform encryption instead of decryption
- *-ciphertext [Bytes]: CipherText for Intermediary Bytes (Hex-Encoded)*Optional – can be used to provide the starting ciphertext block for encryption. This option must be used in conjunction with the -intermediary option (see below)
- *-intermediary [Bytes]: Intermediary Bytes for CipherText (Hex-Encoded)*Optional – can be used to provide the corresponding intermediary byte values for the cipher text specified with the -ciphertext option.

The purpose of the -ciphertext and -intermediary options is to speed up the exploit process as it reduces the number of ciphertext blocks that must be cracked when generating a forged ciphertext sample. If these options are not provided, PadBuster will start from scratch and brute force all of the necessary blocks for encryption. Let’s take a look at the actual command syntax used to encrypt data with PadBuster:

```
padBuster.pl http://sampleapp/home.jsp?UID=7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6
7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6 8 -encoding 2 -plaintext "ENCRYPT TEST"
```

The output from PadBuster is shown in the screenshot below:

![](http://www.gdssecurity.com/l/po_pb3_sm.png)

You’ll notice that just like before, PadBuster will first ask you to choose the correct padding error response signature. This step can be skipped if you manually specify the padding error message using the -error option. Also notice that PadBuster performed a brute force of both full ciphertext blocks, because we didn’t specify a starting ciphertext block and associated intermediary value to use. If we had provided these values to PadBuster, the first block would have been calculated instantly and only the second block would require brute force as shown below.

```
padBuster.pl http://sampleapp/home.jsp?UID=7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6
7B216A634951170FF851D6CC68FC9537858795A28ED4AAC6 8 -encoding 2 -plaintext "ENCRYPT TEST"
-ciphertext F851D6CC68FC9537 -intermediary 39732322076A263D
```

![](http://www.gdssecurity.com/l/po_pb4_sm.png)

As you can see, the first block (Block 2) was calculated before prompting for the response signature since this block was calculated using just the data provided with the -ciphertext and -intermediary options. If you are wondering where these two values came from, remember that PadBuster prints these two values to the screen at the conclusion of each round of block processing.

So to wrap things up, we are releasing [PadBuster](https://www.gdssecurity.com/l/t/d.php?k=PadBuster) because we think that other pen testers can benefit from a flexible exploit script for detecting and exploit padding oracles. We would be interested in hearing if there are other features that would make the tool more useful or practical from a tester’s perspective, so let us know if you have any feedback.

 [Comments RSS](http://www.gdssecurity.com/l/b/2010/09/14/automated-padding-oracle-attacks-with-padbuster/feed/)

### Leave a Reply

 Name (required)

 Mail (hidden) (required)

 Website
