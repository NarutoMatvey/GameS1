from Lib.MyLib.Class_lib import *


class Game_board(object):
    """"Класс Игральная доска"""

    def __init__(self):
        self.white, self.black = 20, 20
        self.board = {}
        color = "Белый"
        for vertical in range(1, 9):
            if vertical == 3:
                color = "Чёрный"
            for horizontal in range(ord('a'), ord('h')+1):
                line_item = chr(horizontal) + str(vertical)
                if vertical == 2 or vertical == 7:
                    self.board[line_item] = Pawn(line_item, color)
                elif vertical == 1 or vertical == 8:
                    if chr(horizontal) == 'a' or chr(horizontal) == 'h':
                        self.board[line_item] = Rook(line_item, color)
                    elif chr(horizontal) == 'b' or chr(horizontal) == 'g':
                        self.board[line_item] = Horse(line_item, color)
                    elif chr(horizontal) == 'c' or chr(horizontal) == 'f':
                        self.board[line_item] = Elephant(line_item, color)
                    elif chr(horizontal) == 'd':
                        self.board[line_item] = Queen(line_item, color)
                    else:
                        self.board[line_item] = King(line_item, color)
                else:
                    self.board[line_item] = 0

    def check_course(self, line_item, new_line_item):
        if line_item[0] > 'h' or line_item[0] < 'a' or line_item[1] < '1' or line_item[1] > '8' or len(line_item) != 2:
            return "Клетка " + line_item + " не существует!"

        if new_line_item[0] > 'h' or new_line_item[0] < 'a' or new_line_item[1] < '1' or new_line_item[1] > '8' or len(
                new_line_item) != 2:
            return "Клетка " + new_line_item + " не существует!"

        if self.board[line_item] == 0:
            return "Клетка, которую вы выбрал \'" + line_item + "\' не содержит фигуры!"

        if self.board[new_line_item] != 0 and self.board[new_line_item].color == self.board[line_item].color:
            return "Нельзя ходить в клетку " + new_line_item + ", там уже стоит ваша фигура!"

        if self.board[line_item].role_figures == "Пешка" and self.board[new_line_item] != 0:
            if self.board[line_item].how_walks_figure(new_line_item, True):
                global_prover_otvet = self.global_check()
                if global_prover_otvet != 1:
                    return global_prover_otvet
                rol = self.board[new_line_item].info()['role']
                if "Король" in rol:
                    return "Мат " + self.board[new_line_item].color
                self.update_board(line_item, new_line_item, True)
                return "Пешка успешно походила!"
            else:
                return "Пешка по такой траиктории не может ударить!"

        if self.board[line_item].how_walks_figure(new_line_item):
            if self.board[line_item].role_figures != 'Конь':
                global_prover_otvet = self.global_check(line_item, new_line_item)
                if global_prover_otvet != 1:
                    return global_prover_otvet
            if self.board[new_line_item] != 0:
                rol = self.board[new_line_item].info()['role']
                if "Король" in rol:
                    return "Мат " + self.board[new_line_item].color
                self.update_board(line_item, new_line_item, True)
            else:
                self.update_board(line_item, new_line_item)
            return self.board[new_line_item].role_figures + " успешно походил!"
        else:
            return self.board[line_item].role_figures + " по такой траиктории ходить не может!"

    def global_check(self, line_item, new_line_item):
        gor1, ver1, gor2, ver2 = line_item[0], line_item[1], new_line_item[0], new_line_item[1]
        deltaGOR, deltaVER = 0, 0

        if gor1 < gor2:
            deltaGOR = 1
        elif gor1 > gor2:
            deltaGOR = -1

        if ver1 < ver2:
            deltaVER = 1
        elif ver1 > ver2:
            deltaVER = -1
        i = chr(ord(gor1) + deltaGOR)
        j = chr(ord(ver1) + deltaVER)
        if i <= gor2 and j <= ver2:
            while i < gor2 or j < ver2:
                if self.board[i + j] != 0:
                    return "На пути стоит фигура которую нельзя обойти!"
                i = chr(ord(i) + deltaGOR)
                j = chr(ord(j) + deltaVER)
        elif i >= gor2 and j >= ver2:
            while i > gor2 or j > ver2:
                if self.board[i + j] != 0:
                    return "На пути стоит фигура которую нельзя обойти!"
                i = chr(ord(i) + deltaGOR)
                j = chr(ord(j) + deltaVER)
        elif i <= gor2 and j >= ver2:
            while i < gor2 or j > ver2:
                if self.board[i + j] != 0:
                    return "На пути стоит фигура которую нельзя обойти!"
                i = chr(ord(i) + deltaGOR)
                j = chr(ord(j) + deltaVER)
        elif i >= gor2 and j <= ver2:
            while i > gor2 or j < ver2:
                if self.board[i + j] != 0:
                    return "На пути стоит фигура которую нельзя обойти!"
                i = chr(ord(i) + deltaGOR)
                j = chr(ord(j) + deltaVER)
        return 1

    def update_board(self, line_item, new_line_item, kill=False):
        if kill:
            if self.board[new_line_item].color == "Чёрный":
                self.black -= 1
            else:
                self.white -= 1
        self.board[new_line_item] = self.board[line_item]
        self.board[line_item] = 0
