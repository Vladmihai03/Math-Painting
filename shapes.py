class Square:
    def __init__(self, x, y, width, color=None):
        self.x = x
        self.y = y
        self.width =width
        self.color = color

    def draw(self, canvas):
        if self.color is not None:
            canvas.data[self.x: self.x+self.width, self.y: self.y+self.width] = self.color


class Rectangle:

    def __init__(self,x,y,height,width,color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self,canvas):
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width]=self.color
