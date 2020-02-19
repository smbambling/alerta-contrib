Federation Plugin
========================

This is an plugin that enable federation among several several instances of Alerta providing a single command and control / pane of glass.

For help, join [![Gitter chat](https://badges.gitter.im/alerta/chat.png)](https://gitter.im/alerta/chat)

Installation
------------

Clone the GitHub repo and run:

    $ python setup.py install

Or, to install remotely from GitHub run:

    $ pip install git+https://github.com/alerta/alerta-contrib.git#subdirectory=plugins/federation

Note: If Alerta is installed in a python virtual environment then plugins
need to be installed into the same environment for Alerta to dynamically
discover them.

Configuration
-------------

Add `federation ` to the list of enabled `PLUGINS` in `alertad.conf` server
configuration file and set plugin-specific variables either in the
server configuration file or as environment variables.

```python
PLUGINS = ['federation']
```

**Example**

```python
PLUGINS = ['enhance', 'federation']
FEDERATION_URL = 'http://www.example.com/api'
FEDERATION_API_KEY = 'client_api_key'
```

Copyright (c) 2020 Steven Bambling. Available under the MIT License.
