from threading import Thread, Event
import time


condition_customer = Event()
condition_new_order = Event()
condition_order_ready = Event()
condition_eaten = Event()
condition_receive_command = Event()


class Cook(Thread):
    def __init__(self):
        Thread.__init__(self)

    def cook(self):
        print("Cook starts cooking")
        time.sleep(5)
        condition_order_ready.set()

    def run(self):
        # wait for command from waiter
        condition_new_order.wait()
        # cook
        self.cook()


class Waiter(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.cash = 0

    def bring_command_to_cook(self):
        print("Waiter takes command and brings it to Cook")
        time.sleep(1)
        # tell cook there is a new order
        condition_new_order.set()

    def bring_command_to_customer(self):
        print("Waiter brings command to Customer")
        time.sleep(1)
        condition_receive_command.set()

    def cashing(self):
        print("Customer pays for his meal")
        self.cash += 5

    def run(self):
        # wait for customer to arrive and take command
        condition_customer.wait()
        self.bring_command_to_cook()

        # wait for command to be ready
        condition_order_ready.wait()
        self.bring_command_to_customer()

        # wait for customer to finish his meal
        condition_eaten.wait()
        self.cashing()


class Customer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def eat(self):
        print("Customer starts eating")
        time.sleep(5)
        condition_eaten.set()

    def run(self):
        # notify waiter of its presence and make command
        condition_customer.set()

        # wait for food
        condition_receive_command.wait()

        self.eat()


if __name__ == '__main__':
    threads = [Cook(), Waiter(), Customer()]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
