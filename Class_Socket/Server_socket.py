import socket
from Lib.MyLib.messaging import send_message, get_answer


class Server(object):
    """Класс Сервер"""

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.host = host
        self.port = int(port)
        self.socket.bind((self.host, self.port))
        self.socket.listen(2)
        self.conn = []

    def accepts(self):
        index = len(self.conn)
        conn, addr = self.socket.accept()
        self.conn += [conn]
        if index % 2 == 0:
            self.conn += [[conn, 0]]
        else:
            self.conn += [[conn, 1]]
        return index

    def recv(self, index):
        response = get_answer(self.conn[index])
        return response['data']

    def send(self, massage, index, error=False):
        send_message(self.conn[index], massage, error)

    def __del__(self):
        for i in range(len(self.conn)):
            self.conn[0].close()
        self.conn.clear()
        self.socket.close()
