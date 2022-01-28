## CodeOnTheFly
CodeOnTheFly is the newest member of Pedram's random software collection. It allows you to run the code you love on the web. Just call the API, give it a file and, COTF will take care of the rest.
COTF is powered by [TTYD](https://github.com/tsl0922/ttyd) and [Flask](https://github.com/pallets/flask). Without them, COTF would never  be created.

**Disclaimer:** 

> COTF is still in its early stages. We’re currently on version 0.3.0. There is still a long way to go to reach a full release that is properly usable. While it does work, using this in a production environment is not recommended and **Will** certainly, lead to disaster.
> ↳ Pedram

## Index
| Topic | Go |
|--|--|
| How does it work? | ⬇️ |
| What are the uses? | ⬇️ |
| Prerequisites/Dependencies | ⬇️ |
| Installation | ⬇️ |
| How to use | ⬇️ |
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
## Installation
## Usage Examples
## Configuration