import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def drawing(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    user = int(input('Enter the recursion depth for Koch: '))
    drawing(user)

if __name__ == '__main__':
    main()