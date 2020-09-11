import turtle as t



count = 0 
while (count <= 5):
	t.penup()
	t.goto(count * 100 - 100, 500 - 100)
	t.pendown()
	t.goto(count * 100 - 100, 0 - 100)
	count = count +1

count = 0
while (count <= 5):
	t.penup()
	t.goto(0 - 100, count * 100 - 100)
	t.pendown()
	t.goto(500 - 100,count * 100 - 100)
	count = count + 1

t.exitonclick()
