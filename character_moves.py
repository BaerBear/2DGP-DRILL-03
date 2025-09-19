from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_at_top():
    print('Moving top')
    for x in range(30, 760, 5):
        draw_boy(x, 550)
    pass


def move_at_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw_boy(760, y)
    pass


def move_at_bottom():
    print('Moving bottom')
    for x in range(760, 30, -5):
        draw_boy(x, 50)
    pass


def move_at_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw_boy(30, y)
    pass


def move_rectangle():
    print("Move rectangle")
    move_at_top()
    move_at_right()
    move_at_bottom()
    move_at_left()
    pass


def move_circle():
    print("Move circle")
    r = 200
    for deg in range(-90, 270):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


def move_to_top():
    for x in range (650, 400, -5):
        draw_boy(x, 50 - (x - 650) * 2)

    pass


def move_to_bottom():
    for x in range(400, 150, -5):
        draw_boy(x, 50 + (x - 150) * 2)
    pass


def move_line():
    for x in range(150, 650, 5):
        draw_boy(x, 50)
    pass


def move_triangle():
    print("Move triangle")
    move_line()
    move_to_top()
    move_to_bottom()
    pass


while True:
    # move_rectangle()
    move_triangle()
    # move_circle()
    break
    pass

close_canvas()
