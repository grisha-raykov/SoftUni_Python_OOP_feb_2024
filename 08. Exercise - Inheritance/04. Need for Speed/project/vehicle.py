class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: float):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int) -> None:
        needed_fuel = self.fuel_consumption * kilometers
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel
