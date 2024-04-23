from dataclasses import dataclass


@dataclass()
class City:
    name: str
    population: int
    founded: int

    # def __repr__(self):
    #     return f"City(name='{self.name}', population={self.population}, founded={self.founded})"

    # def __eq__(self, other):
    #     if isinstance(other, City):
    #         return (self.name, self.population, self.founded) == (other.name, other.population, other.founded)
    #     return NotImplemented


city = City("Tokyo", 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)
