import socket
from Lib.MyLib.messaging import send_message, get_answer


class Client(object):
    """Класс Клиента"""

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.host = host
        self.port = int(port)

        self.socket.connect((self.host, self.port))

    def recv(self):
        response = get_answer(self.socket)
        return response

    def send(self, massage):
        send_message(self.socket, massage)

    def __del__(self):
        self.socket.close()