from itertools import cycle


class Gun:
    def __init__(self) -> None:
        self.res = cycle(["pif", "paf"])
        self.cnt = 0

    def shoot(self):
        print(next(self.res))
        self.cnt += 1

    def shots_count(self):
        return self.cnt

    def shots_reset(self):
        self.res = cycle(["pif", "paf"])
        self.cnt = 0


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
