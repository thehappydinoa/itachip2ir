"""device"""
from contextlib import closing
import socket
import ipaddress


class iTach(object):
    """iTach class"""
    devices = {}

    def __init__(self, ip_address="192.168.1.111", port=4998):
        """init method"""
        if ip_address != "localhost":
            self.ip_address = str(ipaddress.ip_address(ip_address))
        self.ip_address = ip_address
        self.port = port

    def __repr__(self):
        return "iTach(devices=%s, ip_address=%s, port=%d)" % (
            self.devices, self.ip_address, self.port)

    def _check_ip(self):
        """checks if ip_address valid"""
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(3)
            return sock.connect_ex((self.ip_address, self.port)) == 0

    def add(self, device):
        """adds device to devices"""
        device.ip_address = self.ip_address
        device.port = self.port
        self.devices[device.name] = device
        return device

    def send_command(self, device_name, command_name):
        """sends command to device"""
        device = self.devices[device_name]
        return device.send_command(command_name)


class VirtualDevice(object):
    """VirtualDevice class"""
    ip_address = ""
    port = 4998

    def __init__(self, name="", commands={}):
        """init method"""
        self.name = name
        self.commands = commands

    def __repr__(self):
        """repr method"""
        return "VirtualDevice(name=%s, commands=%s)" % (self.name, self.commands)

    def format_command(self, command):
        """format command for sending"""
        if not command.endswith("\r"):
            return command + "\r"
        return command

    def format_command_name(self, command_name):
        """format command in commands for sending"""
        command = self.commands[command_name]
        return self.format_command(command)

    def send_command(self, command_name, byte_size=4096, timeout=3):
        """send command from commands"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.ip_address, self.port))
            sock.settimeout(timeout)
            sock.sendall(self.format_command_name(command_name))
            msg = sock.recv(byte_size)
            sock.close()
            return msg
        except socket.error as error:
            print(repr(error))
            return error

    def send_commands(self, command_name, repeats, byte_size=4096, timeout=3):
        """send command multiple times from command from commands"""
        for x in range(repeats):
            self.send_command(command_name, byte_size, timeout)


if __name__ == "__main__":
    blueray_commands = {
        "toggle_power": "test"
    }
    itach = iTach(ip_address="localhost", port=4998)
    blueray = itach.add(VirtualDevice(
        name="blueray", commands=blueray_commands))
    print(blueray.send_command("toggle_power"))
