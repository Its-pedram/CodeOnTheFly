## CodeOnTheFly
CodeOnTheFly is the newest member of Pedram's random software collection. It allows you to run the code you love on the web. Just call the API, give it a file and, COTF will take care of the rest.
COTF is powered by [TTYD](https://github.com/tsl0922/ttyd) and [Flask](https://github.com/pallets/flask). Without them, COTF would not exist.

**Disclaimer:** 

> COTF is still in its early stages. We’re currently on version 0.3.0. There is still a long way to go to reach a full release that is properly usable. While it does work, using this in a production environment is not recommended and **Will** certainly, lead to disaster.

> ↳ Pedram

## Index
| Topic | Go |
|--|--|
| How does it work? | [⬇️](#How-does-it-work) |
| What are the uses? | [⬇️](#What-are-the-uses) |
| Prerequisites/Dependencies | [⬇️](#PrerequisitesDependencies) |
| Installation | [⬇️](#Installation) |
| Usage & Examples | [⬇️](#UsageExamples) |
| Configuration | [⬇️](#Configuration) |
| Roadmap | [⬇️](#Roadmap) |
| Credits | [⬇️](#Credits) |
## How does it work?
Glad you asked! Basically, you call the API with one of the examples from the Usage Examples section. After COTF receives your code through the file you provided, it will generate a single-use session with a terminal where you can interact with your code.
![Example of the TTYD session](https://img.itspedram.com/cotf_terminal_example.png)
## What are the uses?
While COTF could have many uses, it's probably best used by integration into another application. For example, you could use COTF to run the code written in your online IDE. You may also personally use COTF to run code on the remote environment due to a specific compiler/interpreter not being available on the local machine.
## Prerequisites/Dependencies
| Below is a list of dependencies needed for CodeOnTheFly to work. Keep in mind that the list may be incomplete and will vary based on your use case. | |
|--|--|
| [Operating System](https://distrowatch.com/dwres.php?resource=popularity): Most modern Linux Distros will work, including Containers and VMs. While COTF doesn't (and isn't meant to) support macOS or Windows, you might still be able to run the script (with some tweaking) on a machine with those operating systems since TTYD can run on such machines. |
| [Python 3.8.10](https://www.python.org/downloads/): It's a python script after all... An older version might also work. |
| [VirtualEnv](https://pypi.org/project/virtualenv/): Needed to run stuff like Flask and Waitress |
| [TTYD](https://github.com/tsl0922/ttyd): For running terminal sessions in the web.  | 
|  [Flask](https://github.com/pallets/flask): To run the API server. |
| [Waitress](https://pypi.org/project/waitress/):  Production WSGI server. (Optional)|
|[Compilers/Interpreters](https://en.wikipedia.org/wiki/List_of_compilers): You need to manually install a compiler or an interpreter for every language that you plan to use.|
## Installation
First, install all the required dependencies from the section above. COTF is a collection of Python scripts and modules. All you have to do is download the files and run the script. You can either download everything by using the green button labelled "Code" at the top or, if you have git installed, you can clone the repository by executing the following command:

    git clone https://github.com/Its-pedram/CodeOnTheFly.git

Finally, you can either run the script directly from Python by running (from the directory that the files are located at):

    python3 ./CodeOnTheFly.py
Or you may choose to run the small `start.sh` script. To do that, you must first make the script executable by running:

    chmod +x start.sh
  and then you can simply run:
  

    ./start.sh
to start CodeOnTheFly!
## Usage & Examples
To use the API, you must first create a key named "Code" in the form-data section of the body. Then, assign a file to this key and sent the request using GET or POST.

Below are a few examples to help you interact with the API:

cURL:
```bash
curl --location --request POST 'http://localhost:5000' \
--form 'code=@"/path/to/file/testscript.py"'
```

NodeJs (Request):
```js
var request = require('request');
var fs = require('fs');
var options = {
  'method': 'POST',
  'url': 'http://localhost:5000',
  'headers': {
  },
  formData: {
    'code': {
      'value': fs.createReadStream('/path/to/file/testscript.py'),
      'options': {
        'filename': 'testscript.py',
        'contentType': null
      }
    }
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```
Javascript (Fetch):
```js
var formdata = new FormData();
formdata.append("code", fileInput.files[0], "testscript.py");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://localhost:5000", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
Dart (http):
```dart
var request = http.MultipartRequest('POST', Uri.parse('http://localhost:5000'));
request.files.add(await http.MultipartFile.fromPath('code', '/path/to/file/testscript.py'));

http.StreamedResponse response = await request.send();

if (response.statusCode == 200) {
  print(await response.stream.bytesToString());
}
else {
  print(response.reasonPhrase);
}
```
C# (RestSharp):
```csharp
var client = new RestClient("http://localhost:5000");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AddFile("code", "/path/to/file/testscript.py");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```
PHP (HTTP_Request2):
```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('http://localhost:5000');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->addUpload('code', '/path/to/file/testscript.py', 'testscript.py', '<Content-Type Header>');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```
Swift (URLSession):
```swift
import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

var semaphore = DispatchSemaphore (value: 0)

let parameters = [
  [
    "key": "code",
    "src": "/path/to/file/testscript.py",
    "type": "file"
  ]] as [[String : Any]]

let boundary = "Boundary-\(UUID().uuidString)"
var body = ""
var error: Error? = nil
for param in parameters {
  if param["disabled"] == nil {
    let paramName = param["key"]!
    body += "--\(boundary)\r\n"
    body += "Content-Disposition:form-data; name=\"\(paramName)\""
    if param["contentType"] != nil {
      body += "\r\nContent-Type: \(param["contentType"] as! String)"
    }
    let paramType = param["type"] as! String
    if paramType == "text" {
      let paramValue = param["value"] as! String
      body += "\r\n\r\n\(paramValue)\r\n"
    } else {
      let paramSrc = param["src"] as! String
      let fileData = try NSData(contentsOfFile:paramSrc, options:[]) as Data
      let fileContent = String(data: fileData, encoding: .utf8)!
      body += "; filename=\"\(paramSrc)\"\r\n"
        + "Content-Type: \"content-type header\"\r\n\r\n\(fileContent)\r\n"
    }
  }
}
body += "--\(boundary)--\r\n";
let postData = body.data(using: .utf8)

var request = URLRequest(url: URL(string: "http://localhost:5000")!,timeoutInterval: Double.infinity)
request.addValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")

request.httpMethod = "POST"
request.httpBody = postData

let task = URLSession.shared.dataTask(with: request) { data, response, error in 
  guard let data = data else {
    print(String(describing: error))
    semaphore.signal()
    return
  }
  print(String(data: data, encoding: .utf8)!)
  semaphore.signal()
}

task.resume()
semaphore.wait()
```
Go (Native):
```go
package main

import (
  "fmt"
  "bytes"
  "mime/multipart"
  "os"
  "path/filepath"
  "io"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "http://localhost:5000"
  method := "POST"

  payload := &bytes.Buffer{}
  writer := multipart.NewWriter(payload)
  file, errFile1 := os.Open("/path/to/file/testscript.py")
  defer file.Close()
  part1,
         errFile1 := writer.CreateFormFile("code",filepath.Base("/path/to/file/testscript.py"))
  _, errFile1 = io.Copy(part1, file)
  if errFile1 != nil {
    fmt.Println(errFile1)
    return
  }
  err := writer.Close()
  if err != nil {
    fmt.Println(err)
    return
  }


  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Set("Content-Type", writer.FormDataContentType())
  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```
## Configuration
The options for configuration are endless since COTF is open-source and written in Python. You can edit any script and tailor it to your needs. With that said, [*config.py*](https://github.com/Its-pedram/CodeOnTheFly/blob/main/utils/config.py) and [*language_support.py*](https://github.com/Its-pedram/CodeOnTheFly/blob/main/utils/language_support.py) are two of the files main that are meant to be modified to customize COTF's functionality.

`config.py:`

Here you can find general settings related to various aspects of COTF.
```python
# Modify any Flask-related stuff from here.
flask_configuration = {
    # If set to true, this option will switch
    # flask's debug WSGI server with waitress.
    'production' : False,
    # The ip address that you plan for Flask to 
    # listen on.
    'host': '0.0.0.0',
    # The port that you plan for Flask to 
    # listen on.
    'port': '5000',
    # Toggles Flask's debugging features.
    'debug': True,
}
```
```python
# Use this section to choose which IP will your API output when a session is requested.
api_output_configuration = {
    # internal: Will return the internal/local 
    # IP address
    # external: Will return the external/public 
    # IP address
    # localhost: Will return localhost instead of 
    # an IP address
    # Custom: Define the IP address manually
    'IP-Address': 'localhost',
}
```

```python
ttyd_configuration = {
    # Use -1 to disable
    'UID': '1001',
    'GID': '1001',
    'Single-Use': True,
    # Use 0 for random
    # Don't change unless you plan to rapidly test 
    # the changes made to the code.
    'Port': '0',
}
```
> Note: You can further customize ttyd by modifying the generate_command function in [utils.py](https://github.com/Its-pedram/CodeOnTheFly/blob/main/utils/utils.py).

`language_support.py`

This is where support for various languages and compilers/interpreters are added.
```python
# Add acceptable file extensions here. Users can only upload files with one of the extensions below.
ALLOWED_EXTENSIONS = {'py', 'cpp', 'java', 'js', 'ts', 'dart', 'go', 'c'}
```

```python
# This dictionary decides which file extension corresponds to which compiler/interpreter. 
compilers = {
    '.py': 'python3',
    '.cpp': 'g++',
    '.java': 'javac',
    '.js': 'node',
    '.ts': 'tsc',
    '.dart': 'dart',
    '.go': 'go',
    '.c': 'gcc',
}
```

```python
# This is where you define the command syntax for each compiler/interpreter.
def generate_compiler_command(filename, compiler):
    if compiler == 'python3':
        return filename
    elif compiler == 'g++':
        return f" -o {filename.rsplit('.', 1)[0]}.out {filename}"
    elif compiler == 'javac':
        return f" -d {filename.rsplit('.', 1)[0]}.class {filename}"
    elif compiler == 'node':
        return f" {filename}"
    elif compiler == 'tsc':
        return f" {filename}"
    elif compiler == 'dart':
        return f" {filename}"
    elif compiler == 'go':
        return f" {filename}"
    elif compiler == 'gcc':
        return f" -o {filename.rsplit('.', 1)[0]}.out {filename}"
```
> Note: Don't forget to install the nessesary compilers and interpreters before enabling a new language in [language_suppport.py](https://github.com/Its-pedram/CodeOnTheFly/blob/main/utils/language_support.py).
## Roadmap
 - [ ] Authentication
 - [ ] Proper Error Catching and Crash Prevention
 - [ ] Even More Documentation
 - [ ] Implemention of Better Security
 - [ ] Default Support for More Languages

## Credits
Yet again, thanks to [TTYD](https://github.com/tsl0922/ttyd) and [Flask](https://github.com/pallets/flask) for such amazing open-source projects. 

Thanks to Python for being easy to use.

Thanks to the teachers who let me write code while in their classes.