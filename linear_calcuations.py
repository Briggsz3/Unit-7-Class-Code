"""
Name: Zachary Briggs
Date: 12/16/24
Description: Linear Calculations
"""
import math

def slope(point1:tuple,point2:tuple)->float:
    x1= point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2= point2[1]
    slope = (y2-y1)/(x2-x1)
    return slope

def distance(point1:tuple, point2:tuple)->float:
    x1= point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2= point2[1]
    drt = math.sqrt(((x2-x1)**2+(y2-y1)**2))
    return drt

def main():
    point1 = (4,5)
    point2= (1,-4)
    print(slope(point1,point2))
    print(distance(point1, point2))


if __name__ == "__main__":
    main()