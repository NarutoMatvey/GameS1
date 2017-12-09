class Figures(object):
    """Шахматные фигуры"""

    def __init__(self, role_figures, line_item, color):
        """Конструктор"""
        self.line_item = line_item
        self.color = color
        self.role_figures = role_figures

    def info(self):
        return {'cell': self.line_item,
                'color': self.color,
                'role': self.role_figures}

    def update_line_item(self, line_item):
        self.line_item = line_item
