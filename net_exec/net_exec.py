#!/bin/env python

import socket
import os, sys
import subprocess
import argparse
import pwd

parser = argparse.ArgumentParser(description='Start a process on incoming connection.')
parser.add_argument('-p', '--port', default=31337, type=int)
parser.add_argument('-u', '--user', nargs='?')
parser.add_argument('program', help='Program executed on connection')
parser.add_argument('args', nargs='*', help='Arguments passed to the program')
args = parser.parse_args()

HOST = 'localhost'
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()

    print('New incomming connection...')

    if os.fork() == 0:
        if args.user:
            uid = pwd.getpwnam(args.user)[2]
            os.setuid(uid)

        print('Start %s... with params %s' % (args.program, str(args.args)) )
        ret = subprocess.call([args.program] + args.args, stdout=conn.fileno(), stdin=conn.fileno())
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
        print('Program terminated with status %d...' % ret)
        sys.exit(0)
