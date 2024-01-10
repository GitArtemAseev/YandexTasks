import math
xA, yA, xB, yB = map(int, input().split())
def first(x1, y1, x2, y2):
    way = math.sqrt(x1**2 + y1**2) + math.sqrt(x2**2 + y2**2)
    return way
def second(x1, y1, x2, y2):
    way = abs(math.hypot(x1, y1) - math.hypot(x2, y2))
    radians = abs(math.atan2(y1, x1) - math.atan2(y2, x2))
    way += (min(math.hypot(x2, y2),math.hypot(x1, y1)))*radians
    return way
print(min(first(xA, yA, xB, yB), second(xA, yA, xB, yB)))