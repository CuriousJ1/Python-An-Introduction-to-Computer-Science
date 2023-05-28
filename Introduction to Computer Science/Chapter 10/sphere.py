from math import pi

class Radius:
    
    def __init__(self, radius):
        
        """
        Creates a sphere given the radius
        """
        
        self.radius = radius
        
    def getRadius(self):
        
        """
        Returns the radius of this sphere
        """
        
        return self.radius
    
    def surfaceArea(self):
    
        """
        Returns the surface area of the sphere
        """
        
        self.area = 4 * pi * self.radius ** 2
        return self.area
    
    def sphereVolume(self):
    
        """
        Returns the volume of the sphere
        """

        self.vol = 4 / 3 * pi * (self.radius ** 3)
        return self.vol