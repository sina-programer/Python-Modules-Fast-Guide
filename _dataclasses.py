from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    color: str


p1 = Point(10, 15, 'black')
p2 = Point(10, 15, 'green')

print("p1: ", p1)
print("p2: ", p2)

print("p1 == p2 : ", p1 == p2)
print("p1.x : ", p1.x)
