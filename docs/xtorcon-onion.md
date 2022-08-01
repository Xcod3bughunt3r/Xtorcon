.. _onion_api:

Onion APIs
==========

See the :ref:`programming_guide` for "prose" documentation of these
(and other) APIs.

For non-authenticated services:

IOnionService
-------------
.. autointerface:: xtorcon.IOnionService

IFilesystemOnionService
-----------------------
.. autointerface:: xtorcon.IFilesystemOnionService



Both kinds of authenticated service (ephemeral or disk) implement
these interfaces:

IAuthenticatedOnionClients
--------------------------
.. autointerface:: xtorcon.IAuthenticatedOnionClients

IOnionClient
------------
.. autointerface:: xtorcon.IOnionClient


Concrete classes implementing specific variations of Onion
services. First, ephemeral services (private keys do not live on
disk). See :ref:`server_use` for an overview of the variations.

EphemeralOnionService
---------------------
.. autoclass:: xtorcon.EphemeralOnionService

EphemeralAuthenticatedOnionService
----------------------------------
.. autoclass:: xtorcon.EphemeralAuthenticatedOnionService

EphemeralAuthenticatedOnionServiceClient
----------------------------------------
.. autoclass:: xtorcon.EphemeralAuthenticatedOnionServiceClient


Onion services which store their secret keys on disk:

FilesystemOnionService
----------------------
.. autoclass:: xtorcon.FilesystemOnionService

FilesystemAuthenticatedOnionService
-----------------------------------
.. autoclass:: xtorcon.FilesystemAuthenticatedOnionService

FilesystemAuthenticatedOnionServiceClient
-----------------------------------------
.. autoclass:: xtorcon.FilesystemAuthenticatedOnionServiceClient


Some utility-style classes:

AuthBasic
---------
.. autoclass:: xtorcon.AuthBasic

AuthStealth
-----------
.. autoclass:: xtorcon.AuthStealth

