import socket
from Lib.MyLib.messaging import send_message, get_answer


class Client(object):
    """Класс Клиента"""

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.host = host
        self.port = int(port)

        self.socket.connect((self.host, self.port))
        self.player = self.recv()
        self.player = self.player['data']

        board = self.recv()
        while 'error' in board:
            board = self.recv()
        self.board = board['data']

    def recv(self):
        response = get_answer(self.socket)
        return response

    def view_board(self, player):
        if player == "Белый":
            start, stop, step = 9, -1, -1
        else:
            start, stop, step = 0, 10, 1
        for vertical in range(start, stop, step):
            if vertical == 0 or vertical == 9:
                print(end='  ')
                for horizontal in range(ord('a'), ord('h') + 1):
                    print('{0:8}'.format('   ' + chr(horizontal)), end='')
            else:
                print(vertical, end='  ')
                for horizontal in range(ord('a'), ord('h')+1):
                    role_figures = self.board[chr(horizontal) + str(vertical)]
                    if role_figures != 0:
                        role_figures = role_figures.info()['role'] + role_figures.info()['color'][0]
                    else:
                        role_figures = '   ' + str(role_figures)
                    print('{0:8}'.format(role_figures), end='')
                print(' ' + str(vertical), end='')
            print()

    def send(self, massage):
        send_message(self.socket, massage)

    def update_boarder(self, line_item, new_line_item):
        self.board[new_line_item] = self.board[line_item]
        self.board[line_item] = 0

    def __del__(self):
        self.socket.close()
