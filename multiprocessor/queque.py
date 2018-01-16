#! /usr/bin/env python
# -*- coding:utf-8 -*-

numconsumers = 1
numproducers = 4
nummessages = 4


import threading, queue, time
dataQueque = queue.Queue()
safeprint = threading._allocate_lock()


def producer(idnum, dataqueque):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqueque.put('[producer id=%d, count=%d]' % (idnum, msgnum))


def consumer(idnum, dataqueque):
    while True:
        time.sleep(0.1)
        try:
            data = dataqueque.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer', idnum, 'got ==>', data)


if __name__ == '__main__':
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i, dataQueque))
        thread.daemon = True
        thread.start()
    # waitfor = []
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i , dataQueque))
        # waitfor.append(thread)
        thread.start()

    # for thread in waitfor: thread.join()
    print('Main thread exit.')