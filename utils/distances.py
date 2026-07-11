def manhattan(a: tuple,b: tuple):
    """ calculates distance between 2 points """
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])
    distance = d_x + d_y
    return distance
