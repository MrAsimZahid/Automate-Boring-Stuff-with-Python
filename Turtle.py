import turtle
def drawCircle():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brad = turtle.Turtle()
    brad.ht()
    brad.st()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(0)
    brad.resizemode("auto")
    brad.tilt(45)
    num=1
    while(num<40):
        brad.circle(120)
        brad.left(70)
        num+=1

def drawRectangle():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.ht()
    brad.st()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(0)
    #brad.resizemode("auto")
    brad.tilt(45)
    
    num=1
    while(num<20):
        a=1
        while(a<3):
            brad.forward(300)
            brad.right(90)
            brad.forward(150)
            brad.right(90)
            a+=1
        brad.right(100)
        num+=1

def drawSquare():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.ht()
    brad.st()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    #brad.resizemode("auto")
    brad.tilt(45)
    num=1
    while(num<20):
        a=1
        
        while(a<5):
            
            brad.forward(200)
            brad.right(90)
            a+=1
        brad.right(100)
        num+=1

drawCircle()
drawRectangle()
drawSquare()
