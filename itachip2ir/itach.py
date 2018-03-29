#!/usr/bin/env python2.7
import socket
from contextlib import closing

important = '\033[35m[*]\033[1;m '
hardreturn = '\n'
info = '\033[1;33m[!]\033[1;m '
que = '\033[1;34m[?]\033[1;m '
bad = '\033[1;31m[-]\033[1;m '
good = '\033[1;32m[+]\033[1;m '
run = '\033[1;97m[~]\033[1;m '


class iTach(object):
    def __init__(self, name, ip, port=4998):
        self.name = str(name)
        self.ip = str(ip)
        self.port = int(port)
        if not self._check_ip():
            # print(bad + "Port %s is not open on %s" % (self.port, self.ip))
            raise Exception("Port %s is not open on %s" % (self.port, self.ip))
        print(good + "Created '%s' on %s:%s" %
              (self.name, self.ip, str(self.port)))

    def _check_ip(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(3)
            return (sock.connect_ex((self.ip, self.port)) == 0)

    def _get_ip(self):
        return self.ip

    def _get_port(self):
        return self.port

    def _get_name(self):
        return self.name


class device(object):
    def __init__(self, name, iTach):
        self.name = str(name)
        self.iTach = iTach
        self.commands = {}
        print(good + "Created '%s' on '%s'" %
              (self.name, self.iTach._get_name()))

    def set_command(self, command_name, ir_code):
        self.commands[command_name] = ir_code

    def send_command(self, command_name, byte_size=4096, timeout=3):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.iTach._get_ip(), self.iTach._get_port()))
            s.settimeout(timeout)
            s.sendall(self.commands[command_name] + "\r")
            msg = s.recv(byte_size)
            s.close()
            del s
            return msg
        except socket.error as e:
            #print(bad + "Error connecting to '%s' @ %s:%s" % (self.iTach._get_name(), self.iTach._get_ip(), self.iTach._get_port()))
            raise Exception("Error connecting to '%s' @ %s:%s" % (
                self.iTach._get_name(), self.iTach._get_ip(), self.iTach._get_port()))

    def send_commands(self, command_name, repeats, byte_size=4096, timeout=3):
        for x in range(repeats):
            self.send_command(command_name, byte_size, timeout)


if __name__ == "__main__":
    itach = iTach("Tester iTach ip2ir", "192.168.43.200")
    blueray = device("Blueray Player", itach)
    blueray.set_command("toggle_power", "sendir,1:3,1,40192,1,1,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,529,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,528,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,553,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,4000")
    blueray.send_commands("toggle_power", 3)
