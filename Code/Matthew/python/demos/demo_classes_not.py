

def distance(p1, p2):
    dx = p1['x'] - p2['x']
    dy = p1['y'] - p2['y']
    return (dx*dx + dy*dy) ** 0.5
    # return math.sqrt(dx**2 + dy**2)

point1 = {'x': 5, 'y': 2}
point2 = {'x': 8, 'y': 10}

d = distance(point1, point2)
print(d)
