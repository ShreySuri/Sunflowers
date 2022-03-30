import turtle
import random
import time

t = turtle.Pen()
u = turtle.Pen()
v = turtle.Pen()

t.hideturtle()
u.hideturtle()
v.hideturtle()

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

ta = turtle.Pen()
tb = turtle.Pen()
tc = turtle.Pen()
td = turtle.Pen()
te = turtle.Pen()
tf = turtle.Pen()

ta.hideturtle()
tb.hideturtle()
tc.hideturtle()
td.hideturtle()
te.hideturtle()
tf.hideturtle()

ua = turtle.Pen()
ub = turtle.Pen()
uc = turtle.Pen()
ud = turtle.Pen()
ue = turtle.Pen()
uf = turtle.Pen()

ua.hideturtle()
ub.hideturtle()
uc.hideturtle()
ud.hideturtle()
ue.hideturtle()
uf.hideturtle()

va = turtle.Pen()
vb = turtle.Pen()
vc = turtle.Pen()
vd = turtle.Pen()
ve = turtle.Pen()
vf = turtle.Pen()

va.hideturtle()
vb.hideturtle()
vc.hideturtle()
vd.hideturtle()
ve.hideturtle()
vf.hideturtle()

print("Please be patient. Seeds take time to grow.")


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

ta.up()
tb.up()
tc.up()
td.up()
te.up()
tf.up()

ua.up()
ub.up()
uc.up()
ud.up()
ue.up()
uf.up()

va.up()
vb.up()
vc.up()
vd.up()
ve.up()
vf.up()

ta.right(180)
tb.right(180)
tc.right(180)
td.right(180)
te.right(180)
tf.right(180)

ta.forward(200)
tb.forward(200)
tc.forward(200)
td.forward(200)
te.forward(200)
tf.forward(200)

ta.left(90)
tb.left(90)
tc.left(90)
td.left(90)
te.left(90)
tf.left(90)

ua.right(90)
ub.right(90)
uc.right(90)
ud.right(90)
ue.right(90)
uf.right(90)

va.forward(200)
vb.forward(200)
vc.forward(200)
vd.forward(200)
ve.forward(200)
vf.forward(200)

va.right(90)
vb.right(90)
vc.right(90)
vd.right(90)
ve.right(90)
vf.right(90)

print("Please be patient. Seeds take time to grow.")

ta.forward(210)
tb.forward(170)
tc.forward(130)
td.forward(90)
te.forward(50)
tf.forward(10)

ua.forward(210)
ub.forward(170)
uc.forward(130)
ud.forward(90)
ue.forward(50)
uf.forward(10)

va.forward(210)
vb.forward(170)
vc.forward(130)
vd.forward(90)
ve.forward(50)
vf.forward(10)

ta.right(90)
tb.left(90)
tc.right(90)
td.left(90)
te.right(90)
tf.left(90)

ua.right(90)
ub.left(90)
uc.right(90)
ud.left(90)
ue.right(90)
uf.left(90)

va.right(90)
vb.left(90)
vc.right(90)
vd.left(90)
ve.right(90)
vf.left(90)

print("What color do you think the saplings will be? ")

for i in range(1,281):
    t.forward(1)
    u.forward(1)
    v.forward(1)
    if i % 40 == 10:
        j = int((i - 10)/40)
        if j == 1:
            k = random.randint(1,99)
            l = k % 3
            if l == 0:
                ta.forward(20)
            elif l == 1:
                ta.forward(25)
            else:
                ta.forward(30)
            


