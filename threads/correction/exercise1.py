# -----------------------------------------------------------
# Correction of Threads - Exercise 2 Question 2
#
# Tips:
# - Create a class Wall which have an attribute damage that
#   can be decremented
# - Create a class Rock that is a Thread and can inflict
#   damage to the Wall until it is completely destroyed
# - Don't forget to use a lock when modifying the attribute
#   damage
# - Instanciate many Rock classes and start the Wall
#   desctruction
# -----------------------------------------------------------

from threading import Thread, Lock
import random
import time


lock = Lock()


class Wall:
    """
        Object that have a strength attribute that be decremented.
    """
    def __init__(self, strength):
        self.strength = strength

    def get_damage(self, damage):
        self.strength -= damage


class Rock(Thread):
    """
        Thread that inflict damage to an object Wall until it is totally
        destroyed. It can inflict between 1 and 10 damage per second.
    """
    def __init__(self, id, wall):
        Thread.__init__(self)
        self.id = id
        self.wall = wall

    def destroy_wall(self):
        time.sleep(1)
        damage = random.randint(1, 10)
        real_damage = 0
        with lock:
            # Verifying if the wall still have strength (could have
            # changed during the time.sleep of this rock)
            if self.wall.strength > 0:
                real_damage = min(damage, self.wall.strength)
                self.wall.get_damage(real_damage)
        if real_damage > 0:
            print(f"Robot {self.id} did {real_damage} damage to the wall. "
                  f"Remaining strength: {self.wall.strength}")

    # Method called automatically when starting the thread
    def run(self):
        while self.wall.strength > 0:
            self.destroy_wall()


if __name__ == '__main__':
    wall = Wall(100)  # Wall strength is initialized at 100
    rocks = [Rock(i, wall) for i in range(1, 6)]  # We instanciate 6 rocks

    for rock in rocks:
        rock.start()  # Rocks start to attack the Wall

    for rock in rocks:
        rock.join()  # Program ends when every thread has finished running
