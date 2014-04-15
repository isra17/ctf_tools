Shellcode Compiler
==================

Helper to compile and extract shellcode

Install `pyelftools`:

    pip install pyelftools

Build shellcode:

    ./shellcode_compiler hello.S
    \xeb\x191\xc01\xdb1\xd21\xc9\xb0\x04\xb3\x01Y\xb2\x05\xcd\x801\xc0\xb0\x011\xdb\xcd\x80\xe8\xe2\xff\xff\xffhello
