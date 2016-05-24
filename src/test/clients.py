#!/usr/bin/env python

import optparse
from multiprocessing import Process
import socket
import time
import random
import loremipsum

def run_client(num_messages):

    sock = socket.socket()
    sock.connect(('localhost',8080))

    for i in range(num_messages):
        wait_time = random.randint(0,10)
        time.sleep(wait_time)
        sock.send('{}\n'.format(loremipsum.get_sentence()))

    sock.close()

if __name__ == "__main__":

    parser = optparse.OptionParser()
    parser.add_option('-n', '--num-clients', help='number of clients',
                      dest='num_clients', action='store', type='int', default=10)
    parser.add_option('-m','--num-messages', help='number of messages to send',
                      dest='num_messages', action='store', type='int', default=25)

    (opts, args) = parser.parse_args()

    procs = []

    try:
        for i in range(opts.num_clients):
            p = Process(target=run_client, args=(opts.num_messages,))
            p.start()
            procs.append(p)

        for p in procs:
            p.join()
    except KeyboardInterrupt:
        for p in procs:
            p.terminate()
