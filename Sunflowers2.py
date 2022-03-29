import turtle

t = turtle.Pen()
u = turtle.Pen()
v = turtle.Pen()


t.hideturtle()
u.hideturtle()
v.hideturtle()

t.up()
t.right(90)
t.forward(250)
t.right(90)
t.forward(200)
t.right(90)
t.down()

u.up()
u.right(90)
u.forward(250)
u.right(180)
u.down()

v.up()
v.right(90)
v.forward(250)
v.right(90)
v.forward(300)
v.right(180)
v.down()
v.forward(600)
v.right(180)
v.forward(100)
v.right(90)


t.pencolor(100,100,100)
t.showturtle()
t.forward(100)
u.showturtle()
u.forward(100)
v.showturtle()
v.forward(100)


