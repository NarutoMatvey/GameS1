from Class_Figures.Figures import Figures


class Queen(Figures):
    """Класс Ферзь"""

    def __init__(self, line_item, color):
        super().__init__("Ферзь", line_item, color)

    def how_walks_figure(self, new_line_item):
        ver = ord(self.line_item[0]) - ord(new_line_item[0])
        hor = int(self.line_item[1]) - int(new_line_item[1])
        if ver < 0:
            ver *= -1
        if hor < 0:
            hor *= -1

        if ver != 0 and hor == 0 or ver == 0 and hor != 0:
            self.update_line_item(new_line_item)
            return True
        elif ver == hor:
            self.update_line_item(new_line_item)
            return True
        return False