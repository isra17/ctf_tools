#!/bin/env python
from elftools.elf.elffile import ELFFile
import sys, os

def compile(src):
    return os.system('nasm -f elf %s' % src)

def extract_shellcode(filename):
    f = open(filename, 'rb')
    elffile = ELFFile(f)

    return elffile.get_section_by_name(b'.text').data()

def get_shellcode(src):
    filename, _ = os.path.splitext(src)
    compile(src)
    return extract_shellcode(filename + '.o')

if __name__ == '__main__':
    path = sys.argv[1]
    print(repr(get_shellcode(path))[2:-1])
