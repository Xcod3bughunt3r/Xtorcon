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
    print(default_control_port())
    ep = tor.create_filesystem_onion_endpoint(80, "./test_prop224_service", version=3)

    def on_progress(percent, tag, msg):
        print('%03d: %s' % (percent, msg))
    xtorcon.IProgressProvider(ep).add_progress_listener(on_progress)
    print("Note: descriptor upload can take several minutes")

    port = yield ep.listen(server.Site(Simple()))
    print("Site listening: {}".format(port.getHost()))
    print("Private key:\n{}".format(port.getHost().onion_key))
    yield defer.Deferred()  # wait forever


task.react(main)
