#Author Kai Geller
#GitHub Username: KaiGeller
#4/27/2022
# Assignment number 5b this is to keep track of the x and y coordinate of the taxi and the odometer
class Taxicab:
    def __init__(self, x_coord, y_coord):
        """This defines the x and y coordinates of the cab and sets the odometer to 0"""
        self.x_cord = x_coord
        self.y_cord = y_coord
        self.odometer = 0
    def move_x(self, move_x):
        """This moves the cab along the x axis"""
        self.odometer += abs(move_x)
        self.x_coord += move_x
    def move_y(self, move_y):
       """This moves the cab along the y axis"""
       self.odometer += abs(move_y)
       self.y_coord += move_y
    def get_x_cord(self):
        """This gives current x coordinate of cab"""
        return self.x_coord
    def get_y_cord(self):
        """This gives current x coordinate of cab"""
        return self.y_coord
    def get_odometer(self):
        """This gives odometer value"""
        return self.odometer
