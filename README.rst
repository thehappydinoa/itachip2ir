==========
itachip2ir
==========
.. image:: https://travis-ci.org/thehappydinoa/itachip2ir.svg?branch=master
    :target: https://travis-ci.org/thehappydinoa/itachip2ir

A small module for interacting with the Global Caché iTach WF2IR or IP2IR

==========
How To Use
==========
.. code-block:: python

  from itachip2ir import VirtualDevice, iTach

  commands = {
    "toggle_power": "sendir,1:3,1,40192,1,1,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,529,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,528,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,553,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,4000"
  }

  itach = iTach(ipaddress="192.168.1.111", port=4998)
  blueray = itach.add(VirtualDevice(
    name="blueray", commands=commands))


  if __name__ == "__main__":
    print(blueray.toggle_power())


Check the ``examples/`` folder for more

`The source for this project is available here
<https://github.com/thehappydinoa/itachip2ir>`_.
