#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from __future__ import print_function
from twisted.internet import defer, task, endpoints
from twisted.web import server, resource

import xtorcon
from xtorcon.util import default_control_port


class Simple(resource.Resource):
    """
    A really simple Web site.
    """
    isLeaf = True

    def render_GET(self, request):
        return b"<html>Hello, world! I'm a prop224 Onion Service!</html>"


@defer.inlineCallbacks
def main(reactor):
    tor = yield xtorcon.connect(
        reactor,
        endpoints.TCP4ClientEndpoint(reactor, "localhost", 9251),
    )
    print("{}".format(tor))
    hs = yield tor.create_filesystem_onion_service(
        [(80, 8787)],
        "./prop224_hs",
        version=3,
    )
    print("{}".format(hs))
    print(dir(hs))

    ep = endpoints.TCP4ServerEndpoint(reactor, 8787, interface="localhost")
    port = yield ep.listen(server.Site(Simple()))
    print("Site listening: {}".format(hs.hostname))
    print("Private key:\n{}".format(hs.private_key))
    yield defer.Deferred()  # wait forever


task.react(main)
