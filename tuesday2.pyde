xCoordinate = 50
speed = 5
ellipseSize = 50

def setup():
    size(400,400)
    
def draw():
    background(0)
    global xCoordinate, speed, ellipseSize
    xCoordinate += speed
    leftBoundary = ellipseSize / 2
    rightBoundary = 400 - ellipseSize / 2
    if xCoordinate >rightBoundary or xCoordinate <=leftBoundary:
        speed = -speed
    fill(255,5,250)
    ellipse(50,xCoordinate,50,50)    
    ellipse(xCoordinate,50,50,50)    
