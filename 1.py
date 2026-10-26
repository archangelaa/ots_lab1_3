import turtle

WIDTH = 10      # половина ширины фигуры в клетках (клетка = 10 пикселей)
DROP = 3        # расстояние между параллельными линиями в клетках
NUM_TURNS = 2   # количество витков


def perform_switch_case(state, t, row):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    last_row = 2 * NUM_TURNS  # номер последней горизонтали

    if state == "INIT":
        t.penup()
        t.goto(WIDTH * 10, WIDTH * 10)  # Правый верхний угол = уровень первой линии
        t.pendown()
        t.setheading(180)  # Смотрим влево
        return "HORIZ", row

    if state == "HORIZ":
        t.forward(10)
        # чётные линии идут влево, нечётные вправо
        reached = x <= -WIDTH if row % 2 == 0 else x >= WIDTH
        if reached:
            if row == last_row:
                return "STOP", row
            t.setheading(270)  # Разворот вниз
            return "DOWN", row
        return state, row

    if state == "DOWN":
        t.forward(10)
        # уровень следующей линии считается от начальной точки,
        # поэтому все промежутки строго равны DROP
        if y <= WIDTH - (row + 1) * DROP:
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
