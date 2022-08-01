#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from __future__ import print_function

from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks
import xtorcon

try:
    from stem.descriptor.server_descriptor import RelayDescriptor
except ImportError:
    print("You must install 'stem' to use this example:")
    print("  pip install stem")
    raise SystemExit(1)


@react
@inlineCallbacks
def main(reactor):
    tor = yield xtorcon.connect(reactor)

    or_nickname = "moria1"
    print("Trying to get decriptor information about '{}'".format(or_nickname))
    # If the fingerprint is used in place of nickname then, desc/id/<OR identity>
    # should be used.
    try:
        descriptor_info = yield tor.protocol.get_info('desc/name/' + or_nickname)
    except xtorcon.TorProtocolError:
        print("No information found. Enable descriptor downloading by setting:")
        print("  UseMicrodescritors 0")
        print("In your torrc")
        raise SystemExit(1)

    descriptor_info = descriptor_info.values()[0]
    relay_info = RelayDescriptor(descriptor_info)
    print("The relay's fingerprint is: {}".format(relay_info.fingerprint))
    print("Time in UTC when the descriptor was made: {}".format(relay_info.published))
