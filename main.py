batman = Actor('batman')
batman.pos = 100, 56

WIDTH = 500
HEIGHT = batman.height + 20

def draw():
    screen.clear()
    batman.draw()

batman.topright = 0, 10

def update():
    batman.left += 2
    if batman.left > WIDTH:
        batman.right = 0

def on_mouse_down(pos):
    if batman.collidepoint(pos):
        batman.image = 'batman3'

def set_batman_3():
    batman.image = 'batman3'
    clock.schedule_unique(set_batman_normal, 1.0)


def set_batman_normal():
    batman.image = 'batman'