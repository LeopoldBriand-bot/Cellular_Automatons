from kivy.uix.widget import Widget

class Cell(Widget):
    def __init__(self, typeOfCell, color, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.color = color
        self.typeOfCell = typeOfCell
    