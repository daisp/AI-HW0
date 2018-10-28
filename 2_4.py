class Point:
    def __init__(self, location=(0,0)):
        self.x = location[0]
        self.y = location[1]
    def show(self):
        print("my location is ({},{})".format(self.x,self.y))


myPoint = Point()
myPoint.show()
