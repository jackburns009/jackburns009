TL;DR: How to run BASIC, no hints here. Same README.txt included in Level[1-4].


1. Atari BASIC

One option is to use a real Atari XL/XE machine, if you don't have one - there
are plenty Atari emulators out there (note that you want a 8-bit or
XL/XE family [0x01], not VCS/2600 [0x02]). An emulator may require the original
Atari BASIC ROM (Read-only Memory) image.

One recommended emulator that includes the ROM is Xformer[0x03];
for Windows[0x04], note that you may need to install Microsoft Visual C++
Redistributable packages (x86 [0x05] or x64[0x06]).
For Linux you may use the Xformer for DOS[0x07] and run it with dosbox[0x08] or
the mentioned above version for Windows with wine[0x09].


2. Microsoft GW BASIC

Microsoft has released the original code for GW-BASIC interpreter[0x0A].

There are several projects that attempt to build the interpreter from the
original code, for example [0x0B]. You may follow the project documentation
and build executables or download them [0x0C] which can be run in the dosbox or
dosemu (dosemu2).

Finally you may connect to GW-BASIC via network, see HOW-TOs below.

HOW-TOs for GW-BASIC

* Connect

  Linux:
    $ socat file:$(tty),rawer tcp:<host>:1337

  Windows: in Windows Terminal (https://github.com/microsoft/terminal)
    > telnet <host> 1337
  
  replace <host> with the address listed in the challenge description.


* Load the challenge code into memory

  type LOAD "CHALLENG"

  EXAMPLE:
╔════════════════════════════════════════════════════════════════════════════════╗
║Ok                                                                              ║
║LIST                                                                            ║
║Ok                                                                              ║
║FILES                                                                           ║
║CHALLENG.BAS                                                                    ║
║Ok                                                                              ║
║LOAD "CHALLENG"                                                                 ║
║Ok                                                                              ║
║LIST 10-20                                                                      ║
║10 PRINT "*** THE FLAG VERIFICATOR: LEVEL 4 ***"                                ║
║20 PRINT "VERSION FOR MICROSOFT GW-BASIC 1983"                                  ║
║Ok                                                                              ║
║                                                                                ║
║                                                                                ║
║1LIST   2RUN←   3LOAD"  4SAVE"  5CONT←  6,"LPT1 7TRON←  8TROFF← 9KEY    0SCREEN ║
╚════════════════════════════════════════════════════════════════════════════════╝

* Run the program
  type RUN<Enter> 
 

* Send the Break signal.
  In case you want to break a program execution, you may send the BREAK signal:

  Linux: "Ctrl+6" (Ctrl+^) then type "c" then hit "Shift+b"
  Windows: using Windows Terminal, open Setting, click "Open JSON file",
           find the "actions" parameter and append the following entry:

  // Added to play Google Beginner Quest 2023 --- begin
  {
    "command":
     {
        "action": "sendInput",
        "input": "\u001e\u0063\u0042"
     },
     "keys": "f4"
  }
  // Added to play Google Beginner Quest 2023 --- end

  save the JSON file. (https://learn.microsoft.com/en-us/windows/terminal/customize-settings/actions)
  This would allow to send the BREAK signal by pressing F4.

  EXAMPLE:
╔════════════════════════════════════════════════════════════════════════════════╗
║Ok                                                                              ║
║LOAD "CHALLENG"                                                                 ║
║Ok                                                                              ║
║RUN                                                                             ║
║*** THE FLAG VERIFICATOR: LEVEL 4 ***                                           ║
║VERSION FOR MICROSOFT GW-BASIC 1983                                             ║
║FLAG FORMAT: FLAG{[A-Z0-9_!]*}                                                  ║
║FLAG?                                                                           ║
║Break in 120                                                                    ║
║Ok                                                                              ║
║                                                                                ║
║                                                                                ║
║1LIST   2RUN←   3LOAD"  4SAVE"  5CONT←  6,"LPT1 7TRON←  8TROFF← 9KEY    0SCREEN ║
╚════════════════════════════════════════════════════════════════════════════════╝


* Exit

  type SYSTEM <Enter>

* Fn keys
  F1 -> "Ctrl+6" then "1"


3. Ref

[0x01] https://en.wikipedia.org/wiki/Atari_8-bit_family
[0x02] https://en.wikipedia.org/wiki/Atari_2600
[0x03] http://www.emulators.com/xformer.htm
[0x04] http://www.emulators.com/freefile/xformer10.zip
[0x05] https://aka.ms/vs/17/release/vc_redist.x86.exe
[0x06] https://aka.ms/vs/17/release/vc_redist.x64.exe
[0x07] http://www.emulators.com/freefile/pcxf380.zip
[0x08] https://www.dosbox.com/
[0x09] https://www.winehq.org/
[0x0A] https://github.com/microsoft/GW-BASIC
[0x0B] https://codeberg.org/tkchia/GW-BASIC
[0x0C] https://codeberg.org/tkchia/GW-BASIC/releases
[0x0D] http://www.antonis.de/qbebooks/gwbasman

