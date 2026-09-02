def calculate_fuel(cargo_weight):
    ship_weight = 50000
    total_weight = cargo_weight + ship_weight
    fuel_required = total_weight * 3
    return fuel_required

class Starship:
    def __init__(self, base_weight, cargo_weight, final_fuel):
        self.base_weight = base_weight
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel

cargo_load_1 = 1000
cargo_load_2 = 1000
cargo_load_3 = 1000
total_cargo = cargo_load_1 + cargo_load_2 + cargo_load_3

fuel = calculate_fuel(total_cargo)
ship = Starship(50000, total_cargo, fuel)
print("Final fuel: " + str(ship.final_fuel))