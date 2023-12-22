#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def perimeter_decorator(func):
    def wrapper():
        sides = []
        n = int(input("Введите количество сторон многоугольника: "))
        for i in range(n):
            side = float(input(f"Введите длину стороны {i + 1}: "))
            sides.append(side)
        result = func(sides)
        print("Периметр фигуры равен =", result)

    return wrapper


@perimeter_decorator
def calculate_perimeter(sides):
    perimeter = sum(sides)
    return perimeter


if __name__ == '__main__':
    calculate_perimeter()