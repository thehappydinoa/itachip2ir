itachip2ir v1.2.0
=================
A small Python module for interacting with the Global Caché iTach WF2IR or IP2IR

How To Use
=================
.. code-block:: python

	from itachip2ir import iTach, device

	blueray_commands = {
        "toggle_power": ""
    }
  itach = iTach(ip="localhost", port=4998)
  blueray = itach.add(VirtualDevice(
      name="blueray", commands=blueray_commands))
  print(stereo.send_command("on"))

Check the examples folder for more

`The source for this project is available here
<https://github.com/thehappydinoa/itachip2ir>`_.
