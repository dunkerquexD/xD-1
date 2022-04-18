import turtle

tu.screen.bgcolor("black")
tu.color("green")

tu.left(90)
tu.backward(100)
tu.speed(200)
tu.shape("turtle")


def tree():
    if i<10:
        return

    else:
        tu.forward(i)
        tu.color("orange")