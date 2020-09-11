import turtle as t
scale = 100
def move_to(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()

def draw_sieut():
	x, y = t.pos()
	t.setheading(250)
	t.forward(scale)
	move_to(x, y)
	t.setheading(290)
	t.forward(scale)
	move_to(x , y)

def draw_i():
	x, y = t.pos()
	x2 = x + scale 
	move_to(x2, y)
	t.setheading(270)
	t.forward(100)
	move_to(x , y) 

def draw_nieun():
	x, y = t.pos()	
	move_to(x, y)
	t.setheading(270)
	t.forward(scale * 0.5)
	t.left(90)
	t.forward(scale * 0.7)
	move_to(x , y)

def draw_final(func = None):
	x, y = t.pos()
	if func != None:
		move_to(x, y - scale * 2 )
		func()
	move_to( x + scale * 3 , y )

def draw_jieut():
	x, y = t.pos()
	t.setheading(0)
	t.forward(scale * 0.8)
	move_to(x, y - scale)
	t.left(70)
	t.forward(scale)
	t.right(140)
	t.forward(scale)
	move_to(x , y)

def draw_eh():
	x, y = t.pos()
	x2 = x + scale
	move_to(x2, y)
	t.setheading(270)
	t.forward(scale)
	move_to(x2, y - scale * 0.5)
	t.left(90)
	t.forward(scale * 0.5)
	move_to(x2 + scale * 0.5 , y)
	t.right(90)
	t.forward(scale)
	move_to(x, y)

def draw_hieut():
	x, y = t.pos()
	t.setheading(270)
	t.forward(scale * 0.2)
	t.right(90)
	t.forward(scale * 0.5)
	t.left(180)
	t.forward(scale)
	y2 = y - scale * 1.5
	move_to(x, y2)
	t.circle(scale * 0.5)
	move_to(x, y)

def draw_yor():
	x, y = t.pos()
	x2 = x + scale
	move_to(x2, y)
	t.setheading(270)
	t.forward(scale * 2)
	move_to(x2, y - scale * 1.3)
	t.setheading(180)
	t.forward(scale * 0.5)
	move_to(x2, y - scale * 0.7)
	t.setheading(180)
	t.forward(scale * 0.5)
	move_to(x, y)

def draw_ieng():
	x, y = t.pos()
	t.circle(scale * 0.5)
	move_to(x, y)





move_to(-300, 150)

draw_sieut()
draw_i()
draw_final(draw_nieun)

draw_jieut()
draw_eh()
draw_final()

draw_hieut()
draw_yor()
draw_final(draw_ieng)

t.exitonclick()
