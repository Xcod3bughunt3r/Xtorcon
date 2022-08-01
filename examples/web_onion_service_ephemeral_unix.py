#!/usr/bin/env python
# -*- coding: utf-8-sig -*-

from __future__ import print_function
from os.path import abspath

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
        return b"<html>Hello, world! I'm an Onion service (ephemeral, over unix sockets)!</html>"


@defer.inlineCallbacks
def main(reactor):
    tor = yield xtorcon.connect(
        reactor,
        endpoints.TCP4ClientEndpoint(reactor, "localhost", 9051),
    )
    unix_p = abspath('./web_socket')

    ep = endpoints.UNIXServerEndpoint(reactor, unix_p)
    port = yield ep.listen(server.Site(Simple()))

    def on_progress(percent, tag, msg):
        print('%03d: %s' % (percent, msg))
    print("Note: descriptor upload can take several minutes")
    onion = yield tor.create_onion_service(
        ports=[(80, 'unix:{}'.format(unix_p))],
        version=3,  # or try version=2 if you have an older Tor
        progress=on_progress,
    )

    print("Private key:\n{}".format(onion.private_key))
    print("{}".format(onion.hostname))
    yield defer.Deferred()  # wait forever


task.react(main)
