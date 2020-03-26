from math import sqrt

class Point(object):

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def move_to(self,x,y):    
        self.x = x
        self.y = y
    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(0,0)
    p2 = Point(5,6)
    p2.move_to(1,1)
    print(p2)    
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()