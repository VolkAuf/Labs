from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

class Lab1:

    def __init__(self):
        self.window = Tk()
        self.window.title("Lab1")

        width = 300
        height = 200
        x = 400
        y = 150

        self.triangle_list = []

        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.resizable(False, False)

        Label(self.window, text="Введите число a").pack()
        self.str_a = Entry(self.window)
        self.str_a.pack()

        Label(self.window, text="Введите число b").pack()
        self.str_b = Entry(self.window)
        self.str_b.pack()

        Label(self.window, text="Введите число c").pack()
        self.str_c = Entry(self.window)
        self.str_c.pack()

        btnAdd = Button(text="Добавить треугольник", command=self.add_triangle)
        btnAdd.pack()

        btnPaint = Button(text="Показать график", command=self.paint_triangle)
        btnPaint.pack()


    def membership_meth(self, triangle, _x):
        x = _x
        a = float(triangle[0])
        b = float(triangle[1])
        c = float(triangle[2])

        membership = 0
        if a <= x <= b:
            return (x - a) / (b - a)

        if b < x <= c:
            return (c - x) / (c - b)

        if x < a or x > c:
            return 0

        return membership



    def paint_triangle(self):
        y = [0, 1, 0]
        scatter_x = []
        scatter_y = []

        if len(self.triangle_list) > 0:
            max = (self.triangle_list[0])[2]
            min = (self.triangle_list[0])[0]
        for i in range(len(self.triangle_list)):
            if max < (self.triangle_list[i])[2]:
                max = (self.triangle_list[i])[2]
            if min > (self.triangle_list[i])[0]:
                min = (self.triangle_list[i])[0]

        x = min
        min_membership = 2

        for j in range(int((max-min) * 10)):
            for i in range(len(self.triangle_list)):
                if min_membership > self.membership_meth(self.triangle_list[i], x):
                    min_membership = self.membership_meth(self.triangle_list[i], x)

            plt.plot([x, x], [min_membership, 0])
            x += 0.1
            min_membership = 2

        for i in range(len(self.triangle_list)):
            #plt.scatter(scatter_x, scatter_y)
            plt.plot(self.triangle_list[i], y, alpha=0.7, label="first", lw=3, mew=2, ms=10)

        plt.show()

    def add_triangle(self):
        triangle = []
        triangle.append(float(self.str_a.get()))
        triangle.append(float(self.str_b.get()))
        triangle.append(float(self.str_c.get()))

        self.triangle_list.append(triangle)
        for i in range(len(self.triangle_list)):
            for j in range(len(self.triangle_list[i])):
                print(self.triangle_list[i][j])


    def run(self):
        self.window.mainloop()