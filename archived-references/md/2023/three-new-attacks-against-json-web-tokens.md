---
type: Whitepaper
title: Three New Attacks Against JSON Web Tokens
resource: "https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens-whitepaper.pdf"
tags: [whitepaper, webseclist-reference]
generated:
  by: webseclist-refs/1
  at: "2026-08-11T17:40:24+00:00"
status: stable
stale_after: 2027-08-11
sources:
  - id: original
    resource: "https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens-whitepaper.pdf"
    title: Three New Attacks Against JSON Web Tokens
    author: Tom Tervoort
also_at: []
authors:
  - Tom Tervoort
canonical_url: ""
cited_by:
  - "2023.md:34"
commit: ""
content_sha256: 4b8effc281a91265e49b7cefbe457cb120a21ddc9606022f5597c1f5c5307233
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens-whitepaper.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: 6edba9d7333c149a44f2a553533b8b6aef6c327a043cc3daecdc8ee718567201
retrieved_from: "https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens-whitepaper.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-11T17:40:24+00:00"
slug: three-new-attacks-against-json-web-tokens
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Three New Attacks Against JSON Web Tokens

**Three New Attacks Against JSON Web Tokens** - Tom Tervoort, Publisher not stated.

- Published: date not stated
- Original: <https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens-whitepaper.pdf>
- Preserved from: https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens-whitepaper.pdf (stored) on 2026-08-11
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# Three New Attacks Against JSON Web Tokens

--- page 1 ---

Three New Attacks Against JSON Web Tokens
By: Tom Tervoort, Secura BVJSON Web Tokens (JWTs) have become omnipresent tools for web authentication, session managementand identity federation. However, some have criticized JWT and associated Javascript Object Signingand Encryption (JOSE) standards for cryptographic design aws and dangerous levels of unnecessarycomplexity. These have arguably led to severe vulnerabilities such as the well-known alg:noneattack.When examining JOSE standards myself I also noticed a few potential foot guns that might resultin JWT library implementers introducing vulnerabilities if they were to interpret the RFC in certainways. This prompted me to investigate various JWT libraries for vulnerabilities. As a result, I managedto identify three new classes of JWT attacks aecting at least six dierent implementations. Twoof these attacks (sign/encrypt confusion and polyglot token) can allow complete token forgery,allowing authentication bypasses or privilege escalation in applications using an aected library andconguration. The third (billion hashes) attack can be leveraged for a denial-of-service attack againsttoken-processing servers.In this whitepaper, I will outline these new vulnerability classes (and one other nding) and show howto exploit them. While each could be considered to be purely implementation bugs, I argue that theyare also the result of understandable RFC interpretations and that these problems are indicative ofbroader issues with the JOSE standards.
What's wrong with JWTs?Nowadays, JSON Web Tokens (JWTs) are by far the most popular mechanism for cryptographicallyprotected tokens that transfer identity and privilege information (claims) about an applicationuser or client. They are generally stored by the parties whose identity the tokens describe. To preventusers from altering their own tokens in order to impersonate others or elevate privileges, cryptographicintegrity protection is used. Only those who possess the right secret key should be able to issuetokens.JWT claims are encoded as a JSON object that is subsequently wrapped in a JSON Web Signature(JWS) or JSON Web Encryption (JWE) object, or a combination of the two. JWS and JWE are two of theJavascript Object Signing and Encryption (JOSE) standards. These dene a variety of cryptographicobjects with syntax based on familiar encoding mechanisms like JSON or base64.But is the cryptography any good? I would say that JWS and JWE schemes oer a large improvementof legacy standards such as XML Encryption (which is pretty much fundamentally broken), or shoddy
1

--- page 2 ---

proprietary solutions from Oracle or IBM. Nonetheless, cryptographers still love to complain aboutJWT cryptography. Personally, I particularly agree with the following criticisms:
1.The"alg"parameter, which indicates which cryptographic algorithm to use, is part of thetoken itself. Because the token could have been spoofed by an attacker, this basically meansit's the attacker who tells the verier what kind of cryptography to use (opening op a huge arrayof possibilities for cross-protocol attacks, like the the alg:none and HMAC/RSA confusionattacks). While it is possible to also restrict algorithms in the conguration or store the algorithmalong the key, this is not enforced.
2.Instead of having one strong set of cryptographic primitives selected by experts, it is le up todevelopers (who are probably not cryptographic experts) to make a choice from many dier-ent options (including one algorithm that was eectively broken 17 years before the RFC waspublished!).
3.What makes points 1 and 2 worse is that dierent algorithms can have widely dierent securityproperties. Based on the"alg"value, your token could for example be protected with a MessageAuthentication Code (MAC), signed, encrypted with a shared secret or encrypted with a publickey. An then there is thenonevalue, which indicates no cryptographic protection should beperformed at all!
4.Besides many options for cryptographic algorithms, a large amount of optional features aredened ranging from compression to X.509 certicate processing. Instead of trying to solve oneproblem well the JOSE specications attempts to support many (obscure) use cases, therebyintroducing more complexity and attack surface.Due to issues like this, it is easy for developers using JWTs or those building JWT libraries to makesubtle mistakes which in turn could have high impact. JWT validation is generally a security-criticalprocess and any exploits in that area could lead to privilege escalation as well as full authenticationbypasses. Because of this, I decided to take a closer look at the JWT RFCs as well as the source code ofa variety of open source JWT libraries, which resulted in the discovery of three novel attack techniques,which I will describe here.
New attack 1: Sign/encrypt confusion
TheoryRFC 7519 allows JWTs to either be signed (the JWS form) or encrypted (the JWE form). When usingJWS the claims within the JWT are not hidden from the owner but the token is still protected againsttampering; when using JWE the token contents are hidden from them. It is also possible to combineboth forms by embedding a JWS inside a JWE, but claims that are directly embedded in a JWE are alsoallowed.
2

--- page 3 ---

Both JWS and JWE allow for both symmetric and asymmetric algorithms. These have dierent proper-ties, however: for example, when using a symmetric JWS algorithm (likeHS256) the JWT can both becreated and validated with the same shared secret; meanwhile, when using an asymmetric algorithms(likeRS256) the JWT can only be created by the private key owner but validated by everyone. Whenusing a symmetric JWE you need access to a secret key in order to either encrypt or decrypt it. Becauseauthenticated encryption is used, this is ne: when someone doesn't know the key they will not beable to tamper with claim contents.But what about JWE objects with asymmetrically encryption? In that case a public key is used toencrypt and a private key is used to decrypt. In the context of JWTs that would mean the private keyowner could inspect or validate tokens, but no secrets are needed to issue tokens! See also the tablebelow. Clearly allowing anyone to forge a token goes against the main goal of JWTs.
none
JWS
symmetric
JWS
asymmetric
JWS
symmetric
JWE
asymmetric
JWENeeds secret to read no no no yes yesNeeds secret to changeno
yes yes yes
noWhile RFC 7519 allows encrypted tokens to be wrapped in a single JWE object it does not forbid the useof asymmetric algorithms. In fact, it doesn't mention them at all. This results in many implementationsadding support for these types of asymmetrically encrypted JWTs. Perhaps there is some obscure usecase where this may be useful, but in most situations where you use JWTs you probably do not wanteveryone to be a token issuer.For this reason, a developer well-versed in cryptography will probably not choose to use asymmetricJWE. However not every developer may be aware of this distinction: during pentests I have seenmultiple cases of signing and public-key encryption being confused, resulting in security propertiesopposite to what was expected. This is quite a dangerous feature to support.Even more interestingly, it turns out that even when a developer does not choose to use encryption atall, they may still be vulnerable to a new type of cross-protocol attack under the following conditions:1.They are using a library that accepts both JWS or JWE wrapped JWTs. This is explicitly allowedby the RFC, which describes an automatic method of distinguishing between both types of JWT.2. The library accepts JWE JWTs encrypted with a public key.
3. The developer is issuing asymmetrically signed tokens, using a private/public key pair.
4.The same private/public key pair is supplied to the validation routine (while technically only thepublic key is needed for validation this is common in practice when the same server both issuesand validates tokens).
3

--- page 4 ---

5.The developer does not enforce a specic validation algorithm, and the library does not requirethis by default.In this situation the application will be issuing signed tokens that an attacker can not tamper withdirectly. However, what an attacker can do is encrypt a token with the same public key that is used forsigning. A vulnerable library will then decrypt this JWE object with the private key and consider it asauthentic, even though the developer did not intend to use encrypted tokens in the rst place.This attack would require the attacker to rst gure out the public key that is in use. Since this key doesnot need to be kept secret (hence the name) it is oen published somewhere, such as in a standardOpenID Connect Endpoint. Even when the public key is not published, some algorithms (including thehighly commonRS256,RS384andRS512options) allow it to be computed from just two signatures.In that case the attacker just has to obtain two dierent samples of legitimate signed tokens, aerwhich they can start forging encrypted ones.
ExploitationI identied three libraries against which this attack was possible. A simple example of a vulnerabletoken validator using one of these libraries (Authlib) is as follows:
from authlib.jose import jwt, JsonWebKey
import sys, json
with open(
'
rsa-key.jwk
'
,
'
r
'
) as keyfile:
key = JsonWebKey.import_key(json.load(keyfile))
def validate(token):
claims = jwt.decode(token, key)
claims.validate()This code seems innocuous and is similar to the library's sample code. However, when the key lebeing loaded here happens to contain a private key along with its public key, it becomes vulnerable tothe attack.To exploit this, an attacker rst needs to gure out the public key. I published a script that can computeit relatively eiciently in case theRS256,RS384orRS512algorithm (RSA with PKCS#1 padding) isused.Once the public key is computed or otherwise obtained, the attack becomes trivial: just take an existingtoken's claims and adjust them as you like (or just write claims from scratch). Then you can use any4

--- page 5 ---

JWE encryption tool to make a forged JWT. Personally, I like to use the Burp Suite plugin JWT Editor forthis purpose.
Aected libraries
ˆ
Authlib before version 1.1.0 (CVE-2022-39174)
ˆ
JWCrypto before version 1.4 (CVE-2022-3102)
ˆ
JWX before version 0.12.0
New attack 2: Polyglot token
TheoryThere are several ambiguities in JSON standards and implementations, that can cause dierent parsersto implement the same string dierently. When the same JSON object is passed processed by dierentsystems, these parser inconsistencies can lead to vulnerabilities.Because JWTs are based on JSON, I decided to look around for situations where a token was passedaround between multiple parser implementations and where a parser inconsistency might cause avulnerability. Consider a case where parser A is used to validate a JWT, but where parser B actuallyinterprets its contents aer A does not yield an error. If there is an inconsistency between these parsers,an attacker might construct an input that seems identical to a legitimate JWT to parser A, but willbe interpreted to contain dierent attacker-chosen claims by parser B. This would result in a tokentampering vulnerability.While I did not manage to nd an exploitable JSON parser inconsistency, I did nd a token spoongattack caused by another parser ambiguity: namely on which JWS representation to use. A JWS canactually be represented using three dierent kinds of syntax:compact serialization,general JSONserializationandattened JSON serialization. The JWT RFC species that only the compact serializationshould be used. However, many JWT libraries make the understandable decision to pass on their tokento a general JWS library, and that JWS library may actually support more formats.Such an inconsistency was present between thepython-jwtJWT validator and thejwcryptoJWSvalidator: an attacker could forge an input that appeared towardsjwcryptoas a JSON serializedJWS with a valid signature. However, when interpreted as compact serialization bypython-jwt, adierent payload would be parsed than the one over which the signature was validated. This resultedin a general forgery attack against
python-jwt
.
5

--- page 6 ---

Exploitation
The vulnerable
python-jwt
code was as follows:
def verify_jwt(jwt,
pub_key=None,
allowed_algs=None,
iat_skew=timedelta(),
checks_optional=False,
ignore_not_implemented=False):
[...]
header, claims, _ = jwt.split(
'
.
'
)
parsed_header = json_decode(base64url_decode(header))
[...]
if pub_key:
token = JWS()
token.allowed_algs = allowed_algs
token.deserialize(jwt, pub_key)
elif
'
none
'
not in allowed_algs:
raise _JWTError(
'
no key but none alg not allowed
'
)
parsed_claims = json_decode(base64url_decode(claims))
[...]
return parsed_header, parsed_claimsThis code assumes the JWT is encoded using the compact serialization method, and therefore splits iton periods. Then the header and claims components are decoded, the entire JWT is validated usingjwcrypto(thedeserializemethod will throw an exception when the signature is invalid) andnally the header and claims as originally parsed are returned.To attack this, an attacker rst has to obtain some legitimate (unprivileged) token with a valid signature.This uses compact serialization, which looks like this:
6

--- page 7 ---

AAAA.BBBB.CCCCHere theA's represent the JWS header,B's are the claims andC's are the signature. The attenedJSON equivalent of this JWS object is as follows:
{
"protected": "AAAA",
"payload": "BBBB",
"signature": "CCCC"
}This JWS would also be accepted byjwcrypto'sdeserializemethod and treated identically tothe former one. However, when supplied to thepython-jwtverier an exception would be raisedby the line
jwt.split(
'
.
'
)
, because there is no period in this string.
However, an attacker can modify this representation as follows:
{
"AAAA":".XXXX.",
"protected": "AAAA",
"payload": "BBBB",
"signature": "CCCC"
}From the perspective ofjwcrypto, this is a valid JSON serialized JWS with all the necessary eld. TheadditionalAAAAeld has no meaning in JWS objects and is simply ignored.jwcrypto's validatorwill therefore not raise an exception.
python-jwtwould however split this JSON object on dots and arrive at the following values forclaims and header:
header: {"AAAA:"
claims: XXXXTheheadercontains a number of characters that are not part of the url-safe base64 alphabet. Luckilyfor the attacker, however, the parser used by thebase64url_decodefunction used here will simplydiscard these invalid characters and decode the header in the same way as
AAAA
.Finally,XXXXwill be returned as the validated claims from the JWT. These were however not coveredby any signature and completely falsied by the attacker. The attacker can therefore spoof their identityand any other claim asserted to by the JWT.
7

--- page 8 ---

Aected libraries
ˆ
python-jwt before version 3.3.4 (CVE-2022-39227)
New attack 3: Billion hashes attack
TheoryBesides key-based symmetric and asymmetric cryptography, the JWE standard also supports password-based encryption through thePBES2algorithms. Instead of a key, these algorithms take a passwordas a secret parameter and apply the password-based key derivation PBKDF2 to it in order to derive anencryption key.Because passwords are oen picked by humans, using predictable patterns, password-based encryp-tion is vulnerable to olinedictionaryandbrute-forceattacks where an attacker tries out many potentialpasswords in succession until they nd the one with which they can decrypt a ciphertext. In order tosomewhat mitigate this risk, the PBKDF2 function is parametrized with aniteration countparameterthat denes how many successive cryptographic hash operations need to be carried out in order toturn a password into a key. The higher the iteration count, the slower the function becomes.The idea behind intentionally slowing down this cryptographic operation is to make password guessingattacks more diicult, but you can't set this parameter too high or else it will become to slow for regularuse. The implementer therefore has to try to nd an iteration count value that has an appropriatesecurity/performance trade-o.In JWE, this iteration count is dened in the token headerp2c. This is ne for some password-basedencryption use cases, but creates a problem when an attacker can supply JWE objects that are beingprocessed automatically: in that case an attacker could setp2cto an extremely high value in order tocause denial of service at the server doing the processing. Changing this value will invalidate the JWEauthentication tag. However this tag can only be validated aer the key is derived, and the expensivePBKDF2 computation has therefore already been carried out at that point.
PBES2algorithms are typically not used for JWTs, however various libraries do support these algo-rithms and I found two instances wherePBES2is allowed by default, even if the user did not specify apassword. Instead, these libraries would treat the congured encryption key as a password wheneveraPBES2algorithm was indicated, and perform the PBKDF2 function every time a newPBES2token isprovided. This allowed an unauthenticated resource exhaustion attack against these libraries.
Exploitation
To exploit this, simply create a JWE with the following header:
8

--- page 9 ---

{
"alg": "PBES2-HS512+A256KW",
"p2s": "8Q1SzinasR3xchYz6ZZcHA",
"p2c": 2147483647,
"enc": "A128CBC-HS256"
}Here,p2cis set to the maximal value of a signed 32-bit integer (the highest value accepted by bothvulnerable implementations), and
p2s
is some arbitrary random string.The JWE payload can be set to any arbitrary value. The encrypted key, IV and authentication tag eldscan also be arbitrary random byte sequences, as long as they have appropriate lengths. An example ofa full token using this header us as follows:
eyJhbGciOiJQQkVTMi1IUzUxMitBMjU2S1ciLCJwMnMiOiI4UTFTemluYXNSM3h
jaFl6NlpaY0hBIiwicDJjIjoyMTQ3NDgzNjQ3LCJlbmMiOiJBMTI4Q0JDLUhTMj
U2In0.YKbKLsEoyw_JoNvhtuHo9aaeRNSEhhAW2OVHcuF_HLqS0n6hA_fgCA.VB
iCzVHNoLiR3F4V82uoTQ.23i-Tb1AV4n0WKVSSgcQrdg6GRqsUKxjruHXYsTHAJ
LZ2nsnGIX86vMXqIi6IRsfywCRFzLxEcZBRnTvG3nhzPk0GDD7FMyXhUHpDjEYC
NA_XOmzg8yZR9oyjo6lTF6si4q9FZ2EhzgFQCLO_6h5EVg3vR75_hkBsnuoqoM3
dwejXBtIodN84PeqMb6asmas_dpSsz7H10fC5ni9xIz424givB1YLldF6exVmL9
3R3fOoOJbmk2GBQZL_SEGllv2cQsBgeprARsaQ7Bq99tT80coH8ItBjgV08AtzX
FFsx9qKvC982KLKdPQMTlVJKkqtV4Ru5LEVpBZXBnZrtViSOgyg6AiuwaS-rCrc
D_ePOGSuxvgtrokAKYPqmXUeRdjFJwafkYEkiuDCV9vWGAi1DH2xTafhJwcmywI
yzi4BqRpmdn_N-zl5tuJYyuvKhjKv6ihbsV_k1hJGPGAxJ6wUpmwC4PTQ2izEm0
TuSE8oMKdTw8V3kobXZ77ulMwDs4p.ALTKwxvAefeL-32NY7eTAQThis token can then simply be sent to a vulnerable implementation as is. Conditions for exploitabilityare as follows:
1. The JWT library supports JWE-wrapped JWTs and
PBES
algorithms by default.
2.The JWT library does not use a separate API for password-based encryption, but instead treatsencryption keys and passwords in the same manner.
3. The library user did not congure a specic permissible algorithm for JWT validation.
Aected libraries
ˆ
jose before versions 1.28.1, 2.0.5, 3.20.3 or 4.9.1 (CVE-2022-36083)
ˆ
jose-jwt before version 4.1
9

--- page 10 ---

Not-so-new attack: Key injection
Theory
RFC 7515 denes a rather odd header parameter:
4.1.3. "jwk" (JSON Web Key) Header Parameter
The "jwk" (JSON Web Key) Header Parameter is the public key that
corresponds to the key used to digitally sign the JWS. This key is
represented as a JSON Web Key [JWK]. Use of this Header Parameter is
OPTIONAL.So a JWS can contain a parameter calledjwkthat contains the public key with which the JWS wassigned. This seems rather pointless, as a JWS validator should already be aware of the public key inorder to validate the token. The RFC does not specify what an implementation is supposed do withthis header. I guess the validator could support multiple keys and look up the key from a list, but thatis more easy to implement with the
kid
(Key ID) parameter.However, it is not hard to foresee a way this header could be used wrong: namely if the public key inthejwkparameter were to be used to also validate the token. In this case the attacker couldinjecttheir own key in this header and sign a completely spoofed token themselves. This is actually not anew type of attack: around ve years ago a vulnerability was found in a Cisco JOSE library that workedexactly like this. By adding a
jwk
header with a custom key, an attacker could spoof tokens.During my research I found this same type of vulnerability in the Python libraryauthlib, although itwas only exploitable if the library user would call the JWS API directly. The JWT and OAuth/OIDC APIswere not vulnerable.This authlib bug shows that this attack vector has not yet been completely eliminated. I'd argue thatthis is another good argument as to why the denition of this header value is a design aw. Like thenone
algorithm, implementations should not use it.
ExploitationThis is not a new attack, and tools already exist to nd or exploit this issue. For example: the The JSONWeb Token Toolkit includes a check for this vulnerability class and the Burp Suite plugin JWT Editorhas an Embedded JWK option that automates this attack.
10

--- page 11 ---

Aected libraries
ˆ
Authlib before version 1.1.0 (CVE-2022-39175)
Conclusions and recommendationsWhile JWT and JOSE standards provide a huge improvement over older cryptographic token formats,there are still a number of design aws present that in my opinion increase the chance of implementa-tion bugs. Since I could not review every single JWT library (and only focused on open source ones)it is not unlikely that the attack classes described here might also work against other libraries thatare not listed. Furthermore, due to the complexity and attack surface of JOSE standards it would notsurprise me if more new attack classes would be discovered in the future.
To defend against these types of issues, I would make the following recommendations:
ˆ
For JWT/JOSE library developers:
Less is more: I found it easier to nd vulnerabilities in highly feature-complete libraries thanthose implementing a narrow subset of necessary functionality. Avoid supporting featuresthat don't have a clear use case and turn them o by default when the use case is rare.
Don't use thealgparameter to decide what algorithm to use for validation. Instead,determine it beforehand based on the user conguration or metadata of the key.
Never accept JWTs that are encrypted with a password or public key, or which use a non-compact serialization format.
When delegating token validation to another library, do not attempt to also parse the tokenyourself. Instead, operate on the validated payload returned by that library.
ˆ
For JWT implementers:
Reconsider whether your application really requires cryptographic tokens, and isn't bettero with plain random tokens. Besides sidestepping cryptographic issues, stateful randomtokens are also easier to revoke and don't require key management.
Consider if you can also use a JWT alternative with a stronger cryptographic design, suchas PASETO tokens, Macaroons or Biscuits.
If JWTs are required, explicitly congure the validation algorithm you intend to use. Practi-cally all JWT libraries allow you to do this.
ˆ
For the JOSE working group:
Specify security recommendations that help implementers avoid the types of vulnerabilitiesdiscussed here.
11

--- page 12 ---

Restrict the subset of JWE/JWS algorithms and features that are appropriate for use inJWTs. For example: specify that public-key encryption (without signing) or password-basedencryption should not be used to protect JWT claims.
Discourage the use of untrustedalgheader values for deciding a cryptographic validationalgorithm.
12

--- page 13 ---

DÑ­²Ïc0 ƒ“½€·eì†:hP—@‹ÐDS´YôBÏcÂ`7t£Áº‘^- Þm9…{ëÕ»HÕª’ïè[_ìðBò}¸C/´ŠùyÑÓÂÛ›â¦Ÿèï�XÆAÃG¨´Lÿ†ÜÞ"[—î¥Êô§¢4ö³ÊbUýh¯Å+Z†n¡.“ë[Tµý&ï}Bf@XŸoèl�¢ Æ

--- page 14 ---

^£ñ÷è�yË"I1ÕW²bŽÑ¡§s…Îbˆìõ×¯·ÕîþX|‡ã-åR	ï¼ì�`y.RÕ¿®È¸m;ß�ï£�þÖI± íïÌ	™×Yã[¥ŸâØ%"&j41éGXFhX–ëïš@œK[W±¥æéM¢35œã‚_‹OwR—ê<Fß°Ft/tOÐ$C-ÌÃÿæÌ€LîÉþÿX<’7£÷´^¼§Df8ˆY;ï;í8ùÝ<Ëú_PÚ7‹DDÁŸ†û ‘2Ž+4,{=0°�ÿI‡î×ªÕ„<{ž!ØÊ9ýE<iä¾í½…Ý^D7&#¾ÙÈ‡g~{Øå„ÃgÈ›­º–ö¯ËŽ„,S*ò9xªˆB"	j³b³ª„`q•öhv+9ä³©;ÙÎ¯TtjÖûB‰ìW~{û´š7nd­|éÊÃò w¿²Ëh¨
ü²˜ô@9÷7*�Ÿcâÿý•«+”ÅUËt?¶ç{‡â ®öà’…õ$KÙ0Yö*ë·jî8ò¡Ó*ê›¨“ñz¹¨µ‚¬“Z`cŠ{ßùÓ6™f8±’‰nöÛ›hÎç:%*WÉ¯Ï�Å�Þ4úw€I:qçÁµ�Â*jÚ†J"B·ÞOG½—¼Ü©] šiÏÍD¼7IpšHÒ7Ÿ/‰XUnˆW*~N�

--- page 15 ---

·Àç]c*Ò?ú#ÚŒ@ØÓïÊ32Ï×B»¬ïÓW¥vÏ5ä€úªøÂ?äÅ	r9Gcf5†·­6Nq±^šÞPtb ¸Ù{1DùÌC’ººq#¥!V•p”I³é8S¤N7—Úþ¤c@‚ü#ÿ~P:�cC$¾c.ÝÚE¨ÿ¯sˆo1�TüÔš,„ŸÍ*|—�?Xé7>}û®ß…Üm°‡,A×+Ó¹dÌç`ÑÏ£îëwëÃïF[ßƒhìÏÓ¾™ˆçÏ�ý9ÃL:Ú ‡çVÛQ�¬îcpà“Üaà[û¥VÂtŽèk
