Xtorcon
========
- [*Git Clone*](https://github.com/Xcod3bughunt3r/Xtorcon.git)
- *Python2, PyPy5+, Python3+;*
- *Depends On Twisted, [Automat](https://github.com/glyph/automat), And the [ipaddress](https://pypi.python.org/pypi/ipaddress) Backport for non Python3)*

##### Some Possibly Motivational Example Code :
* ````python2 examples/readme.py````
* ````python2 style examples/readme2.py````

##### Code Python
````
    import treq
    import xtorcon
    import UNIXClientEndpoint
    
    from twisted.internet.task import react
    from twisted.internet.defer import inlineCallbacks, ensureDeferred
    from twisted.internet.endpoints 

    async def main(reactor):
        tor = await xtorcon.connect(
            reactor,
            UNIXClientEndpoint(reactor, "/var/run/tor/control")
        )

        print("Connected to Tor version {}".format(tor.version))

        url = u'https://www.torproject.org:443'
        print(u"Downloading {}".format(repr(url)))
        resp = await treq.get(url, agent=tor.web_agent())

        print(u"   {} bytes".format(resp.length))
        data = await resp.text()
        print(u"Got {} bytes:\n{}\n[...]{}".format(
            len(data),
            data[:120],
            data[-120:],
        ))

        print(u"Creating a circuit")
        state = await tor.create_state()
        circ = await state.build_circuit()
        await circ.when_built()
        print(u"  path: {}".format(" -> ".join([r.ip for r in circ.path])))

        print(u"Downloading meejah's public key via above circuit...")
        config = await tor.get_config()
        resp = await treq.get(
            u'https://meejah.ca/meejah.asc',
            agent=circ.web_agent(reactor, config.socks_endpoint(reactor)),
        )
        data = await resp.text()
        print(data)

    @react
    def _main(reactor):
        return ensureDeferred(main(reactor))
````

##### Try It Now On Debian/Ubuntu
* For example, serve some files via an onion service (*aka* hidden
service):
* Code-Block:: Shell-Session
````
    $ sudo apt-get install --install-suggests python3-xtorcon
    $ sudo twistd -n web --port "onion:80" --path ~/public_html
````

##### To just install this as quickly as possible, using a Debian/Ubuntu system, run the following as root:
* ``sudo apt install python-setuptools python-twisted python-ipaddress graphviz``
* ``python setup.py install``

##### It's recommended to use a virtualenv (see below), but on OSX (and assuming homebrew is installed):
* ``brew install geoip``
* ``pip install -r requirements.txt``
* ``pip install -r dev-requirements.txt``

##### Or, instead of installing locally, simply:
``export PYTHONPATH=.``

##### If you want to take slightly more time, but only install temporarily, use virtualenv:
* ``sudo apt install python-setuptools python-pip``
* ``python setup.py build``
* ``mkdir tmp``
* ``virtualenv --never-download --extra-search-dir=/usr/lib/python2.7/dist-packages/ tmp/xtorcon_env``
* ``cd tmp/xtorcon_env``
* ``source bin/activate``
* ``pip install twisted ipaddress pygeoip``

##### This will download from internets:
``export PYTHONPATH=../../build/lib.linux-x86_64-2.7/``

##### (Or you can type "make virtualenv" which creates tmp/xtorcon_env, up to the "activate" step above) Now, this should work (where "work" means "prints nothing"):
* ``python -c "import xtorcon"``

##### Features Overview
* Currently, txtorcon is capable of: making arbitrary client connections to other services over Tor; configuring [twisted.web.client.Agent](https://twistedmatrix.com/documents/current/web/howto/client.html) instances to do Web requests over Tor; doing both of the above over specific circuits; listening as an Onion service; maintaining up-to-date (live) state information about Tor: Circuits, Streams and Routers (relays); maintaining current (live) configuration information; maintaining representation of Tor's address mappings (with expiry); interrogating initial state of all three of the above; listening for and altering stream -> circuit mappings; building custom circuits; Circuit and Stream state listeners; listening for any Tor EVENT; launching and/or controlling a Tor instance (including Tor Browser Bundle); complete Twisted endpoint support (both "onion"/server side and client-side). 
* This means you may be able to use existing Twisted software via Tor with no code changes. It also is the preferred way to connect (or listen) in Twisted. 
* Comments (positive or negative) appreciated. Even better if they come with patches 😉

##### All [Documentation](https://github.com/Xcod3bughunt3r/blob/main/Xtorcon/docs/index.md).

<br>

## 🌐My Social Link's:
<left><h5><i>
<li><a href="https://hackerone.com/xcod3bughunt3r">HackerOne</a></li>
<li><a href="https://tryhackme.com/p/Xcod3bughunt3r">TryHackMe</a></li>
<li><a href="https://www.linkedin.com/in/xcod3bughunt3r">LinkedIn</a></li>
<li><a href="https://id.quora.com/profile/ALIF-FUSOBAR?ch=10&oid=1837835981&share=f20a095b&srid=hk8GQ9&target_type=user">Quora</a></li>
<li><a href="https://t.me/xcod3bughunt3r">Telegram</a></li>
<li><a href="https://mobile.twitter.com/Xcod3bughunt3r">Twitter</a></li>
<li><a href="https://www.instagram.com/xcod3bughunt3r">Instagram</a></li>
<li><a href="https://www.facebook.com/profile.php?id=100082527189835">Facebook</a></li>
<li><a href="https://tiktok.com/xcod3bughunt3r">TikTok</a></li>
<li><a href="https://www.youtube.com/channel/UCDRFcjutewkhAioAuqTB5wg">YouTube</a></li>
<li><a href="https://t.me/itpeopleindonesia">TeleGroups</a></li>
<li><a href="master@itsecurity.id">Emails</a></li>
<li><a href="https://itsecurity.id">Master Of ITSecurity</a></li>
</i></h5></left>

