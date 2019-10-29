
def quad_form():

    print("\nQuadratic Equation Calculator")
    a = float(input("\tA = "))
    b = float(input("\tB = "))
    c = float(input("\tC = "))

    x1 = ((b * b) - (4 * a * c))

    if x1 < 0:
        print("No Solution")

    else:
        x2 = x1 ** .5
        x3 = (-1 * b) + x2
        x4 = x3 / (2 * a)

        print("The first root is: %s" % x4)

    y1 = ((b * b) - (4 * a * c))

    if y1 < 0:
        print("No Solution")

    else:
        y2 = y1 ** .5
        y3 = (-1 * b) - y2
        y4 = y3 / (2 * a)

        print("The first root is: %s" % y4)


print(quad_form())


