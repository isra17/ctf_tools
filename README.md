Net Exec
==================

Helper to start a local server and start a process on connection with I/O binded to the socket.

    $ ./net_exec.py -p 12312 ./hello a b c

From another terminal:

    $ nc localhost 12312
    Your name: foo
    Hello  foo  from  ['./hello', 'a', 'b', 'c']


Shellcode Compiler
==================

Helper to compile and extract shellcode

Install `pyelftools`:

    $ pip install pyelftools

Build shellcode:

    $ ./shellcode_compiler.py hello.S
    \xeb\x191\xc01\xdb1\xd21\xc9\xb0\x04\xb3\x01Y\xb2\x05\xcd\x801\xc0\xb0\x011\xdb\xcd\x80\xe8\xe2\xff\xff\xffhello
