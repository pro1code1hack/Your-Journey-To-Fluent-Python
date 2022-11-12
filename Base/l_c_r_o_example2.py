a = float(input("input first coefficient - "))
b = float(input("input second coefficient - "))
c = float(input("input third coefficient - "))
discriminant = b ** 2 - 4 * a * c  # finding discriminant of quadratic equation
if discriminant > 0:
    x1 = (-b - discriminant ** 0.5) / (2 * a)  # **0.5 is the same as square root
    x2 = (-b + discriminant ** 0.5) / (2 * a)
    print("first root:", x1)
    print("second root:", x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("root:", x)
else:
    print("no roots")
