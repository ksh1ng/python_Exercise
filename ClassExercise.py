                "Interactive Python 17.6 Exercise"

import math
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX = 0, initY = 0):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def __str__(self):
        return 'x = ' + str(self.x) + ', y = ' + str(self.y)
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        newx = self.getX()
        newy = self.getY()
        newx += dx
        newy += dy

        return Point(newx, newy)


class Rectangle:
    '''
    represent a rectangle by knowing three things: the location of its lower left
    corner, its width, and its height.
    '''
    def __init__(self, initP, initW, initH):
        self.location = initP
        self.width = initW
        self.height = initH
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __str__(self):
        return 'Location of its lower left corner: ' + str(self.location) + '\nWidth: ' + str(self.getWidth()) + ' Height: ' + str(self.getHeight())

    def area(self):
        return self.getWidth() * self.getHeight()

    def perimeter(self):
        return (self.getWidth() + self.getHeight()) * 2

    def transpose(self):
        (self.width, self.height) = (self.getHeight(), self.getWidth())

    def contains(self, aPoint):
        x_bound = self.location.getX() + self.getWidth()
        y_bound = self.location.getY() + self.getHeight()

        if aPoint.getX() >= x_bound or aPoint.getX() < self.location.getX():
            return False
        elif aPoint.getY() >= y_bound or aPoint.getY() < self.location.getY():
            return False

        return True

    def diagonal(self):
        return math.sqrt(self.getWidth() ** 2 + self.getHeight() ** 2)

    def collision(self, rectangle):
        '''
        In games, we often put a rectangular “bounding box” around our sprites
        in the game. We can then do collision detection between, say, bombs and
        spaceships, by comparing whether their rectangles overlap anywhere.

        Write a function to determine whether two rectangles collide.
        Hint: this might be quite a tough exercise! Think carefully about all the cases before you code.
        '''
        if self.area() > rectangle.area():
            maxr = self
            minr = rectangle
        else:
            maxr = rectangle
            minr = self


        minr_corner = [minr.location, minr.location.move(minr.getWidth(), 0),
                       minr.location.move(0, minr.getHeight()),
                       minr.location.move(minr.getWidth(),
                       minr.getHeight())]

        for corner in minr_corner:
            if maxr.contains(corner):
                return True

        return False


r = Rectangle(Point(3,4), 6, 8)
r1 = Rectangle(Point(9,12), 6, 8)

print(r.collision(r1))
