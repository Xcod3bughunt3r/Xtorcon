#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from __future__ import print_function

from twisted.internet.defer import inlineCallbacks
from twisted.internet.task import react
from twisted.internet.endpoints import TCP4ClientEndpoint

import xtorcon
from xtorcon.util import default_control_port

try:
    import treq
except ImportError:
    print("To use this example, please install 'treq':")
    print("pip install treq")
    raise SystemExit(1)


@react
@inlineCallbacks
def main(reactor):
    ep = TCP4ClientEndpoint(reactor, '127.0.0.1', default_control_port())
    # ep = UNIXClientEndpoint(reactor, '/var/run/tor/control')
    tor = yield xtorcon.connect(reactor, ep)
    print("Connected:", tor)

    resp = yield treq.get(
        'https://www.torproject.org:443',
        agent=tor.web_agent(),
    )

    print("Retrieving {} bytes".format(resp.length))
    data = yield resp.text()
    print("Got {} bytes:\n{}\n[...]{}".format(
        len(data),
        data[:120],
        data[-120:],
    ))
