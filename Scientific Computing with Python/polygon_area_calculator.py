class Rectangle ():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{type(self).__name__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2)** .5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        return ('*'* self.width + '\n') * self.height


    def get_amount_inside(self, shape):
        if shape.width > self.width or shape.height > self.height:
            return 0
        areaforanothershape = shape.get_area()
        areafororiginalshape = self.get_area()
        timesinshape = 0
        while areaforanothershape <= areafororiginalshape:
            timesinshape += 1
            areafororiginalshape = areafororiginalshape - areaforanothershape
        return timesinshape


class Square (Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side

    def __str__(self):
        return f'{type(self).__name__}(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side