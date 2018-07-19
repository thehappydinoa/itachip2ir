import pytest

from itachip2ir import VirtualDevice, iTach
from itachip2ir.exception import iTachException


class TestITach(object):
    def test_itach(self):
        itach = iTach(ipaddress="192.168.1.111", port=4998)
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

    def test_exception(self):
        with pytest.raises(iTachException):
            raise iTachException("ERR_01")

    def test_command(self):
        name = "device"
        commands = {"test_command": "test_ir"}
        itach = iTach(ipaddress="localhost", port=4998)
        device = itach.add(VirtualDevice(
            name=name, commands=commands))
        assert isinstance(device.test_command(), iTachException)
