.. _socks:

:mod:`xtorcon.socks` Module
============================

SOCKS5 Errors
-------------

SocksError
~~~~~~~~~~
.. autoclass:: xtorcon.socks.SocksError


GeneralServerFailureError
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.GeneralServerFailureError


ConnectionNotAllowedError
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.ConnectionNotAllowedError


NetworkUnreachableError
~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.NetworkUnreachableError


HostUnreachableError
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.HostUnreachableError


ConnectionRefusedError
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.ConnectionRefusedError


TtlExpiredError
~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.TtlExpiredError


CommandNotSupportedError
~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.CommandNotSupportedError


AddressTypeNotSupportedError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: xtorcon.socks.AddressTypeNotSupportedError


.. note::
    The following sections present low-level APIs. If you are able
    to work with :class:`xtorcon.Tor`'s corresponding high-level
    APIs, you should do so.


resolve
-------
.. autofunction:: xtorcon.socks.resolve


resolve_ptr
-----------
.. autofunction:: xtorcon.socks.resolve_ptr


TorSocksEndpoint
----------------
.. autoclass:: xtorcon.socks.TorSocksEndpoint
