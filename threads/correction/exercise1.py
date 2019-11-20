from threading import Thread, RLock
import random
import time


lock = RLock()


class Wall:
    def __init__(self, strength):
        self.strength = strength

    def get_damage(self, damage):
        self.strength -= damage


class Rock(Thread):
    def __init__(self, id, wall):
        Thread.__init__(self)
        self.id = id
        self.wall = wall

    def destroy_wall(self):
        time.sleep(1)
        damage = random.randint(1, 10)
        real_damage = 0
        with lock:
            if self.wall.strength > 0:
                real_damage = min(damage, self.wall.strength)
                self.wall.get_damage(real_damage)
        if real_damage > 0:
            print(f"Robot {self.id} did {real_damage} damage to the wall. "
                  f"Remaining strength: {self.wall.strength}")

    def run(self):
        while self.wall.strength > 0:
            self.destroy_wall()


if __name__ == '__main__':
    wall = Wall(100)
    rocks = [Rock(i, wall) for i in range(1, 6)]

    for rock in rocks:
        rock.start()

    for rock in rocks:
        rock.join()
