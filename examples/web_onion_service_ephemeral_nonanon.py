#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from __future__ import print_function
from twisted.internet import defer, task, endpoints
from twisted.web import server, resource

import xtorcon
from xtorcon.util import default_control_port
from xtorcon.onion import AuthBasic


class Simple(resource.Resource):
    """
    A really simple Web site.
    """
    isLeaf = True

    def render_GET(self, request):
        return b"<html>Hello, world! I'm a single-hop onion service!</html>"


@defer.inlineCallbacks
def main(reactor):
    # For the "single_hop=True" below to work, the Tor we're
    # connecting to must have the following options set:
    # SocksPort 0
    # HiddenServiceSingleHopMode 1
    # HiddenServiceNonAnonymousMode 1

    tor = yield xtorcon.connect(
        reactor,
        endpoints.TCP4ClientEndpoint(reactor, "localhost", 9351),
    )
    if False:
        ep = tor.create_onion_endpoint(
            80,
            version=3,
            single_hop=True,
        )
    else:
        ep = endpoints.serverFromString(reactor, "onion:80:version=3:singleHop=true")

    def on_progress(percent, tag, msg):
        print('%03d: %s' % (percent, msg))
    xtorcon.IProgressProvider(ep).add_progress_listener(on_progress)

    port = yield ep.listen(server.Site(Simple()))
    print("Private key:\n{}".format(port.getHost().onion_key))
    hs = port.onion_service
    print("Site on http://{}".format(hs.hostname))
    yield defer.Deferred()  # wait forever


task.react(main)
