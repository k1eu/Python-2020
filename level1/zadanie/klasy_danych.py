from dataclasses import dataclass


@dataclass  # klasa zawierająca _tylko_ dane (pola)
class User:
    name: str
    age: int


u1 = User('Kadabra', 10)  # to są instancje
u2 = User('Xiaoli', 79)

print(u1)
print(u2)
print(u1.name)