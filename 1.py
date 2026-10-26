import turtle

def perform_switch_case(state, t, row):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    last_row = 2 * 2
    if state == "INIT":
        t.penup()
        t.goto(10 * 10, 10 * 10)
        t.pendown()
        t.setheading(180)
        return "HORIZ", row

    if state == "HORIZ":
        t.forward(10)

        reached = x <= -10 if row % 2 == 0 else x >= 10
        if reached:
            if row == last_row:
                return "STOP", row
            t.setheading(270)
            return "DOWN", row
        return state, row

    if state == "DOWN":
        t.forward(10)
       
        if y <= 10 - (row + 1) * 3:
            row += 1
            t.setheading(180 if row % 2 == 0 else 0)
            return "HORIZ", row
        return state, row

    return state, row


def draw():
    curr_state = "INIT"
    t = turtle.Turtle()
    t.speed(0)
    row = 0

    while curr_state != "STOP":
        curr_state, row = perform_switch_case(curr_state, t, row)
    turtle.done()


if __name__ == "__main__":
    draw()
