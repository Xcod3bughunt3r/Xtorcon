#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from __future__ import print_function

import sys
from twisted.internet import reactor, defer
from xtorcon import TorInfo, build_local_tor_connection


def error(x):
    print("ERROR", x)
    return x


@defer.inlineCallbacks
def recursive_dump(indent, obj, depth=0):
    if callable(obj):
        try:
            print("%s: " % obj, end=' ')
            sys.stdout.flush()
            if obj.takes_arg:
                v = yield obj('arrrrrg')
            v = yield obj()
            v = v.replace('\n', '\\')
            if len(v) > 60:
                v = v[:50] + '...' + v[-7:]
        except Exception as e:
            v = 'ERROR: ' + str(e)
        print(v)

    else:
        indent = indent + '  '
        for x in obj:
            yield recursive_dump(indent, x, depth + 1)


@defer.inlineCallbacks
def setup_complete(info):
    print("Top-Level Things:", dir(info))

    if True:
        # some examples of getting specific GETINFO callbacks
        v = yield info.version()
        ip = yield info.ip_to_country('1.2.3.4')
        boot_phase = yield info.status.bootstrap_phase()
        ns = yield info.ns.name('moria1')
        guards = yield info.entry_guards()

        print('version:', v)
        print('1.2.3.4 is in', ip)
        print('bootstrap-phase:', boot_phase)
        print('moria1:', ns)
        print('entry guards:', guards)

    # now we dump everything, one at a time
    d = recursive_dump('', info)
    d.addCallback(lambda x: reactor.stop())
    d.addErrback(error)


def setup_failed(arg):
    print("SETUP FAILED", arg)
    reactor.stop()


def bootstrap(c):
    info = TorInfo(c)
    info.post_bootstrap.addCallback(setup_complete).addErrback(setup_failed)


d = build_local_tor_connection(reactor, build_state=False)
# do not use addCallbacks() here, in case bootstrap has an error
d.addCallback(bootstrap).addErrback(setup_failed)

reactor.run()
