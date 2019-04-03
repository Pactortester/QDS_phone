# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 11:04
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: ww.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop


import tkinter as tk
from PIL import Image, ImageTk
from time import time, sleep
from random import choice, uniform, randint
from math import sin, cos, radians

root = tk.Tk()
w = tk.Label(root, text="Hello Tkinter!")
w.pack()
root.mainloop()

class part:

    def __init__(self, cv, idx, total, explosion_speed, x=0., y=0., vx = 0., vy = 0., size=2., color = 'red', lifespan = 2, **kwargs):
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = self.color = color
        self.cv = cv
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color)
        self.lifespan = lifespan

    def update(self, dt):
        # 粒子膨胀if self.alive() and self.expand():
        move_x = cos(radians(self.id * 360 / self.total)) * self.initial_speed
        move_y = sin(radians(self.id * 360 / self.total)) * self.initial_speed
        self.vx = move_x / (float(dt) * 1000)
        self.vy = move_y / (float(dt) * 1000)
        self.cv.move(self.cid, move_x, move_y)

        # 以自由落体坠落

