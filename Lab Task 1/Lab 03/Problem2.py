import math
def calculateDistance():
    x1=float(input('Enter x1= '))
    x2=float(input('Enter x2= '))
    y1=float(input('Enter y1= '))
    y2=float(input('Enter y2= '))

    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {d:.2f}")
calculateDistance()


