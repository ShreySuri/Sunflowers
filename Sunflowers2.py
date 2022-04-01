import turtle
import random

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

print("Take the time to go into fullscreen mode now.")

ta.forward(150)
tb.forward(70)
tc.forward(-10)
td.forward(-90)
te.forward(-170)
tf.forward(-250)

ua.forward(150)
ub.forward(70)
uc.forward(-10)
ud.forward(-90)
ue.forward(-170)
uf.forward(-250)

va.forward(150)
vb.forward(70)
vc.forward(-10)
vd.forward(-90)
ve.forward(-170)
vf.forward(-250)

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

ta.down()
tb.down()
tc.down()
td.down()
te.down()
tf.down()

ua.down()
ub.down()
uc.down()
ud.down()
ue.down()
uf.down()

va.down()
vb.down()
vc.down()
vd.down()
ve.down()
vf.down()

t.pencolor("green")
t.width(3)
u.pencolor("green")
u.width(3)
v.pencolor("green")
v.width(3)

ta.pencolor("green")
tb.pencolor("green")
tc.pencolor("green")
td.pencolor("green")
te.pencolor("green")
tf.pencolor("green")

ua.pencolor("green")
ub.pencolor("green")
uc.pencolor("green")
ud.pencolor("green")
ue.pencolor("green")
uf.pencolor("green")

va.pencolor("green")
vb.pencolor("green")
vc.pencolor("green")
vd.pencolor("green")
ve.pencolor("green")
vf.pencolor("green")


for i in range (1,101):
    t.forward(1)
    u.forward(1)
    v.forward(1)

k = random.randint(1,99)
l = k % 3
a = l + 1
k = random.randint(1,99)
l = k % 3
b = l + 1
k = random.randint(1,99)
l = k % 3
c = l + 1
for i in range (1, 26):
    ta.forward(a)
    ua.forward(b)
    va.forward(c)
    t.forward(3.2)
    u.forward(3.2)
    v.forward(3.2)
m = 5
for i in range(1,50):
    ta.forward(m)
    ta.left(15)
    ua.forward(m)
    ua.left(15)
    va.forward(m)
    va.left(15)
    m = m - 0.1
    
k = random.randint(1,99)
l = k % 3
a = l + 1
k = random.randint(1,99)
l = k % 3
b = l + 1
k = random.randint(1,99)
l = k % 3
c = l + 1
for i in range (1,26):
    tb.forward(a)
    ub.forward(b)
    vb.forward(c)
    t.forward(3.2)
    u.forward(3.2)
    v.forward(3.2)       
m = 5
for i in range(1,50):
    tb.forward(m)
    tb.right(15)
    ub.forward(m)
    ub.right(15)
    vb.forward(m)
    vb.right(15)
    m = m - 0.1
            
k = random.randint(1,99)
l = k % 3
a = l + 1
k = random.randint(1,99)
l = k % 3
b = l + 1
k = random.randint(1,99)
l = k % 3
c = l + 1
for i in range (1,26):
    tc.forward(a)
    uc.forward(b)
    vc.forward(c)
    t.forward(3.2)
    u.forward(3.2)
    v.forward(3.2)
m = 5
for i in range(1,50):
    tc.forward(m)
    tc.left(15)
    uc.forward(m)
    uc.left(15)
    vc.forward(m)
    vc.left(15)
    m = m - 0.1

k = random.randint(1,99)
l = k % 3
a = l + 1
k = random.randint(1,99)
l = k % 3
b = l + 1
k = random.randint(1,99)
l = k % 3
c = l + 1
for i in range (1,26):
    td.forward(a)
    ud.forward(b)
    vd.forward(c)
    t.forward(3.2)
    u.forward(3.2)
    v.forward(3.2)
m = 5
for i in range(1,50):
    td.forward(m)
    td.right(15)
    ud.forward(m)
    ud.right(15)
    vd.forward(m)
    vd.right(15)
    m = m - 0.1

k = random.randint(1,99)
l = k % 3
a = l + 1
k = random.randint(1,99)
l = k % 3
b = l + 1
k = random.randint(1,99)
l = k % 3
c = l + 1
for i in range (1,26):
    te.forward(a)
    ue.forward(b)
    ve.forward(c)
    t.forward(3.2)
    u.forward(3.2)
    v.forward(3.2)
m = 5
for i in range(1,50):
    te.forward(m)
    te.left(15)
    ue.forward(m)
    ue.left(15)
    ve.forward(m)
    ve.left(15)
    m = m - 0.1

k = random.randint(1,99)
l = k % 3
a = l + 1
k = random.randint(1,99)
l = k % 3
b = l + 1
k = random.randint(1,99)
l = k % 3
c = l + 1
for i in range (1,26):
    tf.forward(a)
    uf.forward(b)
    vf.forward(c)
    t.forward(3.2)
    u.forward(3.2)
    v.forward(3.2)
m = 5
for i in range(1,50):
    tf.forward(m)
    tf.right(15)
    uf.forward(m)
    uf.right(15)
    vf.forward(m)
    vf.right(15)
    m = m - 0.1
    
            


