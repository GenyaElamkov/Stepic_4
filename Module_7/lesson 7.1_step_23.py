class Vehicle: ...


class LandVehicle(Vehicle): ...


class WaterVehicle(Vehicle): ...


class AirVehicle(Vehicle): ...


class Car(LandVehicle): ...


class Motorcycle(LandVehicle): ...


class Bicycle(LandVehicle): ...


class Propeller(AirVehicle): ...


class Jet(AirVehicle): ...


# INPUT DATA:

# TEST_1:
print(issubclass(LandVehicle, Vehicle))
print(issubclass(WaterVehicle, Vehicle))
print(issubclass(AirVehicle, Vehicle))

# TEST_2:
print(issubclass(Car, LandVehicle))
print(issubclass(Motorcycle, LandVehicle))
print(issubclass(Bicycle, LandVehicle))

# TEST_3:
print(issubclass(Propeller, AirVehicle))
print(issubclass(Jet, AirVehicle))

# TEST_4:
print(issubclass(Car, Vehicle))
print(issubclass(Motorcycle, Vehicle))
print(issubclass(Bicycle, Vehicle))
print(issubclass(Propeller, AirVehicle))
print(issubclass(Jet, AirVehicle))

# TEST_5:
print(issubclass(Car, WaterVehicle))
print(issubclass(Motorcycle, WaterVehicle))
print(issubclass(Bicycle, WaterVehicle))

print(issubclass(Car, AirVehicle))
print(issubclass(Motorcycle, AirVehicle))
print(issubclass(Bicycle, AirVehicle))

# TEST_6:
print(issubclass(Propeller, LandVehicle))
print(issubclass(Jet, LandVehicle))

print(issubclass(Propeller, WaterVehicle))
print(issubclass(Jet, WaterVehicle))