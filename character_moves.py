from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(30, 760, 5):
        draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    for y in range(500, 50, -5):
        draw_boy(760, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(760, 30, -5):
        draw_boy(x, 50)
    pass


def move_left():
    print('Moving left')
    pass


def move_rectangle():
    print("Move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
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


while True:
    # move_circle()
    move_rectangle()
    break
    pass

close_canvas()
