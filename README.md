Net Exec
==================

Helper to start a local server and start a process on connection with I/O binded to the socket.

    $ ./net_exec.py -p 12312 ./hello a b c

From another terminal:

    $ nc localhost 12312
    Your name: foo
    Hello  foo  from  ['./hello', 'a', 'b', 'c']

To debug with gdb, run `gdb -x gdbinit`. It set the config required to follow the child fork and break when the new process start.
When a process is catched, the listening python script is paused. Wait for the process to terminate and then use the `resume` macro to resume the script.

    $ gdb -x gdbinit
    (gdb) run ./net_exec.py ./hello a b c
    ... Open a connection with nc localhost 31337 ...

    Catchpoint 1 (exec'd /usr/bin/python3.3), 0x00007ffff7ddd270 in _start ()
       from /lib64/ld-linux-x86-64.so.2
    ... You are now in the debugged process, set breakpoint as needed ...
    (gdb) continue

    [Inferior 3 (process 3280) exited normally]
    (gdb) resume
    ... You can now open a new connection with nc localhost 31337 ...




Shellcode Compiler
==================

Helper to compile and extract shellcode

Install `pyelftools`:

    $ pip install pyelftools

Build shellcode:

    $ ./shellcode_compiler.py hello.S
    \xeb\x191\xc01\xdb1\xd21\xc9\xb0\x04\xb3\x01Y\xb2\x05\xcd\x801\xc0\xb0\x011\xdb\xcd\x80\xe8\xe2\xff\xff\xffhello
