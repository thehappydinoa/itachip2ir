"""test_listener"""
import socket
from thread import start_new_thread


class iTachTester(object):
    """iTachTester object"""

    def __init__(self, host="", port=4998, reply="OK"):
        """init method"""
        if host != "":
            self.host = host
        else:
            self.host = socket.gethostname()
        self.port = port
        self.reply = reply

    def client_thread(self, conn):
        """client listener"""
        while True:
            data = conn.recv(4096)
            if not data:
                break
            print("Recieved: %s" % data)
            print("Replied: %s" % self.reply)
            conn.sendall(self.reply)
        conn.close()

    def accept_connections(self):
        """accept connections method"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(10)
        print("Listening on port %d" % self.port)
        while True:
            try:
                conn, addr = sock.accept()
                print("Connected with %s:%d" % addr)
                start_new_thread(self.client_thread, (conn,))
            except (KeyboardInterrupt, socket.error):
                print("Exiting...")
                sock.close()
                exit(0)


if __name__ == "__main__":
    listener = iTachTester()
    listener.accept_connections()
