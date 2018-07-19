"""device"""
import socket
from contextlib import closing

from .exception import iTachException


class iTach(object):
    """iTach class"""
    devices = {}

    def __init__(self, ipaddress="192.168.1.111", port=4998):
        """init method"""
        self.ipaddress = ipaddress
        self.port = port

    def __repr__(self):
        return "iTach(devices=%s, ipaddress=%s, port=%d)" % (
            self.devices, self.ipaddress, self.port)

    def _check_ip(self):
        """checks if ipaddress valid"""
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(3)
            return sock.connect_ex((self.ipaddress, self.port)) == 0

    def add(self, *devices):
        """adds device to devices"""
        for device in devices:
            device.ipaddress = self.ipaddress
            device.port = self.port
            self.devices[device.name] = device
        if len(devices) > 1:
            return devices
        return devices[0]

    def send_command(self, device_name, command_name):
        """sends command to device"""
        device = self.devices[device_name]
        return device.send_command(command_name)


class VirtualDevice(object):
    """VirtualDevice class"""
    ipaddress = ""
    port = 4998

    def __init__(self, name="", commands={}):
        """init method"""
        self.name = name
        self.commands = commands
        self.generate_methods()

    def __repr__(self):
        """repr method"""
        return "VirtualDevice(name=%s, commands=%s)" % (self.name, self.commands)

    def generate_methods(self):
        for command_name in self.commands.keys():
            def fn():
                return self.send_command(command_name)
            setattr(self, command_name, fn)
            fn.__name__ = command_name

    def format_message(self, msg):
        if isinstance(msg, bytes):
            return msg.decode()
        return msg

    def format_command(self, command):
        """format command for sending"""
        if not command.endswith("\r"):
            return command + "\r"
        return command

    def format_command_name(self, command_name):
        """format command in commands for sending"""
        command = self.commands[command_name]
        return self.format_command(command).encode()

    def send_command(self, command_name, byte_size=4096, timeout=3):
        """send command from commands"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((self.ipaddress, self.port))
            sock.sendall(self.format_command_name(command_name))
            return self.format_message(sock.recv(byte_size))
        except socket.error as error:
            return iTachException(error)
        finally:
            sock.close()

    def send_commands(self, command_name, repeats, byte_size=4096, timeout=3):
        """send command multiple times from command from commands"""
        for x in range(repeats):
            response = self.send_command(command_name, byte_size, timeout)
        return response


if __name__ == "__main__":
    itach = iTach(ipaddress="192.168.1.111", port=4998)
    blueray = itach.add(VirtualDevice(
        name="blueray", commands={"get_net": "get_NET,0:1"}))
    print(blueray.get_net())
