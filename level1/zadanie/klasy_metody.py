class Point:
    x: float
    y: float

    def __init__(self, x, y):
        # ↑↑ konstruktor, czyli metoda tworząca instancje klasy...
        self.x = x
        self.y = y

    def move_to(self, nx, ny):
        self.x = nx
        self.y = ny


p = Point(10, 20)  # tworzenie instancji
print(p.x, p.y)
p.move_to(99, 99)
print(p.x, p.y)

