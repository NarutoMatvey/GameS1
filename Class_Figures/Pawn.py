from Class_Figures.Figures import Figures


class Pawn(Figures):
    """Класс Пешка"""

    def __init__(self, line_item, color):
        super().__init__("Пешка", line_item, color)

    def how_walks_figure(self, new_line_item, kill=False):
        hor = ord(self.line_item[0]) - ord(new_line_item[0])
        ver = int(self.line_item[1]) - int(new_line_item[1])
        if self.color == "Белый":
            if ver > 0:
                return False
        else:
            if ver < 0:
                return False
        if ver < 0:
            ver *= -1
        if hor < 0:
            hor *= -1
        print(kill, ver, hor)
        if kill and ver == 1 and hor == 1:
            self.update_line_item(new_line_item)
            return True
        elif ver == 1 and kill == 0 and hor == 0:
            self.update_line_item(new_line_item)
            return True
        elif (self.line_item[1] == '2' or self.line_item[1] == '7') and ver == 2 and kill == False and hor == 0:
            self.update_line_item(new_line_item)
            return True

        return False
