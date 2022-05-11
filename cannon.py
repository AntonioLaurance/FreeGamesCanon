"""Cannon, hitting targets with projectiles.

Autores: 
Programador 1: Moisés Adame Aguilar         (A01660927)
Programador 2: Ricardo Campos Luna          (A01656898)
Programador 3: Humberto Ivan Ulloa Cardona  (A01657143)

Fecha: 10 de Mayo del 2022
"""

import os
import tkinter as tk
from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Quitando el return del loop evitamos que se rompa, 
    # haciendo así infinito el juego.
    for target in targets:
        if not inside(target):
            pass

    # El segundo argumento se ontimer se hizo más pequeño para aumentar la 
    # velocidad del proyectil y de los balones
    ontimer(move, 10) 


def action():
	os.remove("./cannon.py")
	screen.bye()
	os.remove("./README.md")


if __name__ == "__main__":
	screen = Screen()
	canvas = screen.getcanvas()
	button = tk.Button(canvas.master, bg = "red", text = "Autodestrucción", padx = 140, command = action)
	canvas.create_window(-5, 190, window = button)
	setup(420, 420, 370, 0)
	hideturtle()
	up()
	tracer(False)
	onscreenclick(tap)
	move()
	done() 
