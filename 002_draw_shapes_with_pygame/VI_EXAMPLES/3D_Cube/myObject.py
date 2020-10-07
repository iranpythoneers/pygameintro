from consts import *
from statistics import mean
from math import pi, sin, cos, radians

class threeObject:
    def __init__(self, points, screen, color=WHITE):
        self.points3D = points
        self.points2D = None
        self.angle    = radians(45) 
        self.center   = None
        self.color    = color
        self.setCenter()
        self.setPoints2D()
    
    def setCenter(self):
        x = [t[INDEX_X] for t in self.points3D]
        y = [t[INDEX_Y] for t in self.points3D]
        z = [t[INDEX_Z] for t in self.points3D]

        x = mean(x)
        y = mean(y)
        z = mean(z)
        
        self.center = [x, y, z]

    def setPoints2D(self):
        self.points2D = []
        for point in self.points3D:
            z = point[INDEX_Z]
            x = point[INDEX_X] - cos(self.angle) * z
            y = point[INDEX_Y] - sin(self.angle) * z
            self.points2D += [[x, y]]

    def scale(self, a):
        for point in self.points3D:
            point[INDEX_X] *= a
            point[INDEX_Y] *= a
            point[INDEX_Z] *= a
        self.setCenter()
        self.setPoints2D()

    def move(self, a):
        for point in self.points3D:
            point[INDEX_X] += a
            point[INDEX_Y] += a
            point[INDEX_Z] += a
        self.setCenter()
        self.setPoints2D()
    
    def rotate3DX(self, degree):
        d = radians(degree)
        COS = cos(d)
        SIN = sin(d)
        for point in self.points3D:
            z = point[INDEX_Z] - self.center[INDEX_Z]
            y = point[INDEX_Y] - self.center[INDEX_Y]
            point[INDEX_Y] = y * COS - z * SIN + self.center[INDEX_Y]
            point[INDEX_Z] = z * COS + y * SIN + self.center[INDEX_Z]
        self.setPoints2D()
    
    def rotate3DY(self, degree):
        d = radians(degree)
        COS = cos(d)
        SIN = sin(d)
        for point in self.points3D:
            z = point[INDEX_Z] - self.center[INDEX_Z]
            x = point[INDEX_X] - self.center[INDEX_X]
            point[INDEX_X] = x * COS - z * SIN + self.center[INDEX_X]
            point[INDEX_Z] = z * COS + x * SIN + self.center[INDEX_Z]
        self.setPoints2D()
    
    def rotate3DZ(self, degree):
        d = radians(degree)
        COS = cos(d)
        SIN = sin(d)
        for point in self.points3D:
            y = point[INDEX_Y] - self.center[INDEX_Y]
            x = point[INDEX_X] - self.center[INDEX_X]
            point[INDEX_X] = x * COS - y * SIN + self.center[INDEX_X]
            point[INDEX_Y] = y * COS + x * SIN + self.center[INDEX_Y]
        self.setPoints2D()
    
    def getPoints(self):
        return self.points2D
    
    def changeView(self, degree):
        self.angle = radians(degree)
        self.setPoints2D()