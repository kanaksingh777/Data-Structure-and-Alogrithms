class Shape:
    def calculate_area(self, *args, **kwargs):
        if 'shape' in kwargs:
            shape = kwargs['shape']
            if shape == 'circle' and len(args) == 1:
                radius = args[0]
                area = 3.14 * radius ** 2
                print(f"Area of the circle: {area}")
            elif shape == 'triangle' and len(args) == 2:
                base, height = args
                area = 0.5 * base * height
                print(f"Area of the triangle: {area}")
            elif shape == 'rectangle' and len(args) == 2:
                length, width = args
                area = length * width
                print(f"Area of the rectangle: {area}")
            else:
                print("Invalid arguments for the specified shape.")
        else:
            print("Please specify the shape using the 'shape' keyword argument.")

# Test
obj = Shape()
obj.calculate_area(3, shape='circle')       # Circle with radius 3
obj.calculate_area(4, 5, shape='triangle')  # Triangle with base 4 and height 5
obj.calculate_area(6, 7, shape='rectangle') # Rectangle with length 6 and width 7

