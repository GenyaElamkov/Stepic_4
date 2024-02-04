from itertools import cycle


class Gun:
    def __init__(self) -> None:
        self.res = cycle(["pif", "paf"])

    def shoot(self):
        print(next(self.res))


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
