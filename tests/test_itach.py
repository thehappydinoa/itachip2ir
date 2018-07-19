import pytest

import itachip2ir
from itachip2ir import VirtualDevice, iTach


class TestiTach(object):
    def test_itach(self):
        itach = iTach(ipaddress="192.168.1.111")
        assert itach.ipaddress == "192.168.1.111"
        assert itach.port == 4998
        assert itach.devices == {}

    def test_device(self):
        name = "device"
        commands = {"test_command": "test_ir"}
        itach = iTach(ipaddress="192.168.1.111", port=4998)
        device = itach.add(VirtualDevice(
            name=name, commands=commands))
        assert itach.devices[device.name] == device
        assert device.name == name
        assert device.commands == commands

    def test_devices(self):
        name1 = "device1"
        name2 = "device2"
        commands = {"test_command": "test_ir"}
        itach = iTach(ipaddress="192.168.1.111", port=4998)
        device1 = VirtualDevice(
            name=name1, commands=commands)
        device2 = VirtualDevice(
            name=name2, commands=commands)
        devices = itach.add(device1, device2)
        assert itach.devices[device1.name] == device1
        assert itach.devices[device2.name] == device2
        assert device1.name == name1
        assert device2.name == name2
        assert device1.commands == commands
        assert device2.commands == commands

    def test_exception(self):
        with pytest.raises(itachip2ir.iTachException):
            raise itachip2ir.iTachException("ERR_01")

    def test_command(self):
        name = "device"
        commands = {"test_command": "test_ir"}
        itach = iTach(ipaddress="localhost", port=4998)
        device = itach.add(VirtualDevice(
            name=name, commands=commands))
        with pytest.raises(itachip2ir.iTachException):
            response = device.test_command()
