#!/usr/bin/env python3

import math

def area_triangle(base, height):
    return 0.5 * base * height

def area_rectangle(width, height):
    return width * height

def area_circle(radius):
    return math.pi * radius ** 2

def main():
    while True:
       
        shape = input("Choose a shape (triangle, rectangle, circle): ").strip().lower()
        
        if shape == "":
            break
        
        # Kontroller typen af figur
        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = area_triangle(base, height)
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = area_rectangle(width, height)
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = area_circle(radius)
        else:
            print("Unknown shape!")
            continue  # Skip the rest and start the loop again

        # Print outputtet
        print(f"The area is {area:.6f}")

if __name__ == "__main__":
    main()
