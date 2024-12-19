class Patch_txt_angle:
    def RawTurtleDOTwrite(self, arg, move=False, align="left", font=("Arial", 11, "normal"), txt_angle=0):
        if self.undobuffer:
            self.undobuffer.push(["seq"])
            self.undobuffer.cumulate = True
        end = self._write(str(arg), align.lower(), font, txt_angle)
        if move: x, y = self.pos() ; self.setpos(end, y)
        if self.undobuffer: self.undobuffer.cumulate = False
    def RawTurtleDOT_write(self, txt, align, font, txt_angle):
        item, end = self.screen._write(self._position, txt, align, font, self._pencolor, txt_angle)
        self.items.append(item)
        if self.undobuffer: self.undobuffer.push(("wri", item))
        return end
    def TurtleScreenBaseDOT_write(self, pos, txt, align, font, pencolor, txt_angle):
        x, y = pos ; x = x * self.xscale ; y = y * self.yscale
        anchor = {"left":"sw", "center":"s", "right":"se" }
        item = self.cv.create_text(x-1, -y, text = txt, anchor = anchor[align],
            fill = pencolor, font = font, angle = txt_angle)
        x0, y0, x1, y1 = self.cv.bbox(item)
        self.cv.update()
        return item, x1-1
import turtle
turtle.RawTurtle.write         = Patch_txt_angle.RawTurtleDOTwrite
turtle.RawTurtle._write        = Patch_txt_angle.RawTurtleDOT_write
turtle.TurtleScreenBase._write = Patch_txt_angle.TurtleScreenBaseDOT_write


screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('peru')

t = turtle.Turtle()
t.speed(0)

#ground##################################################################

t.pencolor('saddlebrown')
t.fillcolor('saddlebrown')

t.penup()
t.goto(-1000,-100)
t.pendown()

t.begin_fill()
t.goto(1000,-100)
t.goto(1000,-100)
t.goto(1000, -1000)
t.goto(-1000,-1000)
t.goto(-1000,-100)
t.end_fill()

#fireplace##################################################################

t.pencolor('bisque3')
t.fillcolor('bisque3')

t.penup()
t.goto(70,-100)
t.pendown()

t.begin_fill()
t.goto(370,-100)
t.goto(370,-230)
t.goto(70, -230)
t.goto(70,-100)
t.end_fill()

t.pencolor('burlywood3')
t.fillcolor('burlywood3')

t.penup()
t.goto(75,100)
t.pendown()

t.begin_fill()
t.goto(365,100)
t.goto(365,-215)
t.goto(75, -215)
t.goto(75,100)
t.end_fill()

t.pencolor('bisque3')
t.fillcolor('bisque3')

t.penup()
t.goto(70,130)
t.pendown()

t.begin_fill()
t.goto(370,130)
t.goto(370,50)
t.goto(70, 50)
t.goto(70,130)
t.end_fill()

t.pencolor('black')
t.fillcolor('black')

t.penup()
t.goto(119.99999999999997,-215)
t.pendown()

t.setheading(90)
t.begin_fill()
t.goto(320,-215)
t.circle(100, 180)
t.end_fill()
t.penup()
print(t.xcor())
print(t.ycor())

t.pencolor('sienna4')
t.fillcolor('chocolate4')

t.goto(205,-215)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.forward(30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.forward(30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.backward(90)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.setheading(90)
t.forward(27)
t.setheading(0)
t.forward(15)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.forward(30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

t.forward(30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()

#stocking 1##################################################################
t.pencolor('red')
t.fillcolor('red')

t.penup()
t.goto(320,50)
t.pendown()

t.begin_fill()
t.setheading(345)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(100)
print(t.xcor())
print(t.ycor())
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.end_fill()

t.pencolor('snow1')
t.fillcolor('snow1')

t.begin_fill()
t.setheading(345)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.end_fill()

t.pencolor('red')
t.fillcolor('red')

t.penup()
t.goto(342.41438680420134,-59.53353488403298)
t.pendown()

t.begin_fill()
t.setheading(345)
t.circle(17, 180)
t.end_fill()

t.pencolor('snow1')
t.fillcolor('snow1')

t.penup()
t.forward(25)
t.setheading(345)
t.write("M",txt_angle=-15,font=('lora',20,'italic'),align="center")


#stocking 2##################################################################
t.pencolor('red')
t.fillcolor('red')

t.penup()
t.goto(119.99999999999997,50)
t.pendown()

t.begin_fill()
t.setheading(345)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(100)
print(t.xcor())
print(t.ycor())
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.end_fill()

t.pencolor('snow1')
t.fillcolor('snow1')

t.begin_fill()
t.setheading(345)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.end_fill()

t.pencolor('red')
t.fillcolor('red')

t.penup()
t.goto(142.41438680420134,-59.53353488403299)
t.pendown()

t.begin_fill()
t.setheading(345)
t.circle(17, 180)
t.end_fill()

t.pencolor('snow1')
t.fillcolor('snow1')

t.penup()
t.forward(25)
t.setheading(345)
t.write("A",txt_angle=-15,font=('lora',20,'italic'),align="center")


#stocking 3##################################################################
t.pencolor('red')
t.fillcolor('red')

t.penup()
t.goto(218,50)
t.pendown()

t.begin_fill()
t.setheading(345)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(100)
print(t.xcor())
print(t.ycor())
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.end_fill()

t.pencolor('snow1')
t.fillcolor('snow1')

t.begin_fill()
t.setheading(345)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.end_fill()

t.pencolor('red')
t.fillcolor('red')

t.penup()
t.goto(240.41438680420143,-59.53353488403299)
t.pendown()

t.begin_fill()
t.setheading(345)
t.circle(17, 180)
t.end_fill()

t.pencolor('snow1')
t.fillcolor('snow1')

t.penup()
t.forward(25)
t.setheading(345)
t.write("K",txt_angle=-15,font=('lora',20,'italic'),align="center")
# t.write("K", txt_angle=45)

#clock##################################################################

t.pencolor('black')
t.fillcolor('white')

t.setheading(90)
t.forward(250)
t.setheading(0)

t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()

t.setheading(90)
t.forward(40)
t.pendown()
t.forward(25)
t.penup()
t.backward(25)
t.setheading(0)
t.pendown()
t.forward(15)
t.penup()

#tree##################################################################

t.pencolor('brown')
t.fillcolor('brown')

t.goto(-300,-70)

t.pensize(20)
t.pendown()
t.goto(-300,-120)
t.penup()
t.pensize(2)

t.pencolor('darkgreen')
t.fillcolor('darkgreen')

t.goto(-300,250) #1

t.begin_fill()
t.goto(-210,-70)#2
t.goto(-390,-70)#3
t.goto(-300,250)#1
t.end_fill()

#star

t.pencolor('gold')
t.fillcolor('gold')

t.goto(-300,250)
t.pensize(3)
t.pendown()
t.setheading(90)
t.forward(20)
t.backward(40)
t.forward(20)
t.setheading(0)
t.forward(20)
t.backward(40)
t.forward(20)

t.setheading(45)
t.forward(10)
t.backward(20)
t.forward(10)
t.setheading(135)
t.forward(10)
t.backward(20)
t.forward(10)
t.penup()
t.pensize(2)

#ornaments

t.pencolor('red')
t.fillcolor('red')

t.setheading(0)
t.goto(-310,100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-290,150)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-275,70)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-315,0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-270,-45)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-335,50)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-350,-56)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.goto(-260,15)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

#window##################################################################

t.pencolor('white')
t.fillcolor('lightsteelblue')

t.penup()
t.goto(-170,230)
t.pendown()
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()
t.penup()

t.setheading(0)
t.forward(50)
t.setheading(270)
t.pendown()
t.forward(100)
t.penup()

t.setheading(180)
t.forward(50)
t.setheading(90)
t.forward(50)
t.pendown()
t.setheading(0)
t.forward(100)
t.penup()

#presents##################################################################

#green present

t.pencolor('red')
t.fillcolor('green')

t.goto(-200,-50)

t.pendown()
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(70)
t.right(90)
t.forward(50)
t.right(90)
t.forward(70)
t.end_fill()
t.penup()

t.pendown()
t.right(90)
t.forward(29)
t.pensize(2)
t.circle(5)
t.backward(8)
t.circle(5)
t.penup()
t.forward(4)
t.setheading(270)
t.pendown()
t.forward(70)
t.penup()
t.pensize(2)

print(t.xcor())
print(t.ycor())

#gold present

t.pencolor('red')
t.fillcolor('gold')

t.setheading(0)
t.goto(-240,-105)

t.pendown()
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(40)
t.right(90)
t.forward(50)
t.right(90)
t.forward(40)
t.end_fill()
t.penup()

t.setheading(0)
t.forward(29)
t.pendown()
t.pensize(2)
t.circle(5)
t.backward(8)
t.circle(5)
t.penup()
t.forward(4)
t.setheading(270)
t.pendown()
t.forward(40)
t.penup()
t.pensize(2)

#white present

t.pencolor('red')
t.fillcolor('white')

t.setheading(0)
t.goto(-390,-95)

t.pendown()
t.begin_fill()
t.forward(70)
t.right(90)
t.forward(40)
t.right(90)
t.forward(70)
t.right(90)
t.forward(40)
t.end_fill()
t.penup()

t.setheading(0)
t.forward(39)
t.pendown()
t.pensize(2)
t.circle(5)
t.backward(8)
t.circle(5)
t.penup()
t.forward(4)
t.setheading(270)
t.pendown()
t.forward(40)
t.penup()
t.pensize(2)

#nutcracker##################################################################

#head

t.pencolor('tan')
t.fillcolor('tan')

t.setheading(0)
t.goto(-40,0)

t.pendown()
t.begin_fill()
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.end_fill()
t.penup()

#hat

t.pencolor('yellow')
t.fillcolor('blue')

t.setheading(0)
t.backward(5)
t.pendown()
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(50)
t.end_fill()
t.penup()

t.setheading(0)
t.forward(20)
t.setheading(90)
t.pensize(3)
t.pendown()
t.forward(50)
t.penup()
t.pensize(2)

#body

t.pencolor('yellow')
t.fillcolor('red')

t.setheading(270)
t.forward(80)
t.setheading(0)
t.backward(15)

t.setheading(0)
t.backward(5)
t.pendown()
t.begin_fill()
t.forward(40)
t.right(90)
t.forward(60)
t.right(90)
t.forward(40)
t.right(90)
t.forward(60)
t.end_fill()
t.penup()

print(t.xcor())
print(t.ycor())

t.goto(-30,-30)
t.setheading(270)
t.pendown()
t.forward(60)
t.penup()
t.setheading(0)
t.forward(10)
t.setheading(90)
t.pendown()
t.forward(60)
t.penup()

#arms

t.setheading(270)
t.goto(-45,-30)
t.forward(5)
t.pendown()
t.begin_fill()
t.setheading(180)
t.forward(10)
t.setheading(270)
t.forward(40)
t.setheading(0)
t.forward(10)
t.setheading(90)
t.forward(40)
t.end_fill()
t.penup()

t.setheading(0)
t.forward(50)
t.pendown()
t.begin_fill()
t.setheading(180)
t.forward(10)
t.setheading(270)
t.forward(40)
t.setheading(0)
t.forward(10)
t.setheading(90)
t.forward(40)
t.end_fill()
t.penup()

#hands

t.pencolor('tan')
t.fillcolor('tan')

t.goto(-50,-70)
t.setheading(180)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

t.goto(1,-70)
t.setheading(180)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

#legs

t.pencolor('yellow')
t.fillcolor('black')

t.goto(-40,-91)
t.setheading(270)
t.pendown()
t.begin_fill()
t.forward(50)
t.goto(-25,-141)
t.setheading(90)
t.forward(50)
t.end_fill()
t.begin_fill()
t.setheading(270)
t.forward(50)
t.setheading(0)
t.goto(-10,-141)
t.setheading(90)
t.forward(50)
t.end_fill()
t.penup()

#teeth
t.pencolor('black')
t.fillcolor('white')

t.setheading(0)
t.goto(-35,-30)
t.pendown()
t.forward(20)

t.begin_fill()
t.setheading(90)
t.forward(5)
t.setheading(180)
t.forward(20)
t.setheading(270)
t.forward(5)
t.end_fill()

t.begin_fill()
t.setheading(270)
t.forward(5)
t.setheading(0)
t.forward(20)
t.setheading(90)
t.forward(5)
t.end_fill()

t.setheading(180)
t.forward(20)
t.penup()

t.goto(-35,-35)
t.setheading(0)
t.forward(5)
t.setheading(90)
t.pendown()
t.forward(10)

t.setheading(0)
t.forward(5)
t.setheading(270)
t.pendown()
t.forward(10)
t.setheading(0)
t.forward(5)
t.setheading(90)
t.pendown()
t.forward(10)
t.penup()

#eyes

t.pencolor('white')
t.fillcolor('black')

t.goto(-20,-15)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()
t.penup()

t.backward(10)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()
t.penup()

t.hideturtle()

turtle.done()
