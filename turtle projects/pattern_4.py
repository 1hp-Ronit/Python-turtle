import turtle

color = ['red', 'black', 'purple']
wn = turtle.Screen()
p = turtle.Turtle()
wn.bgcolor('white')
p.speed(0)

for i in range(200):
    p.pencolor(color[i % 3])
    p.forward(i)
    p.left(190)
    p.forward(i)
    p.left(270)
    p.forward(i)
    p.left(180)
    p.forward(i + 2)
    p.left(360)

turtle.listen()
turtle.mainloop()