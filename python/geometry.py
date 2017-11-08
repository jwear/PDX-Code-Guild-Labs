
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y ==other.y

    def __sub__(self, other):
        return Point(other.x - self.x, other.y - self.y)

    def move(self, x, y):
        self.x += x
        self.y += y


class Rectangle:

    def __init__(self, top_left_point, width, height):
        self.top_left_point = top_left_point
        self.width = width
        self.height = height

    def __repr__(self):
        return '(top_left=%s, width=%s, height=%s)' % (self.top_left_point, self.width, self.height)

    def __eq__(self, other):
        return self.top_left_point == other.top_left_point and self.width == other.width and self.height == other.width

    def inside(self, point):
        return (self.top_left_point.x <= point.x <= self.top_left_point.x + self.width and self.top_left_point.y <= point.y <= self.top_left_point.y + self.height)

    def center_point(self, width, height):
        new_x = width / 2
        new_y = height / 2
        return Point(new_x, new_y)
