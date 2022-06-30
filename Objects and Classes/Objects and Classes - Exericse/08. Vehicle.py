class Vehicle:

    def __init__(self, vtype, vmodel, vprice, vowner=None):
        self.type = vtype
        self.model = vmodel
        self.price = vprice
        self.owner = vowner

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return "Car already sold"
        elif money >= self.price:
            self.owner = owner
            diff = money - self.price
            return f"Successfully bought a {self.type}. Change: {diff:.2f}"
        else:
            return f"Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
print(vehicle.sell())
print(vehicle.sell())
print(vehicle)

