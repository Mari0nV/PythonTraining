from threading import Thread, Condition
import time


condition_customer = Condition()
condition_new_order = Condition()
condition_order_ready = Condition()
condition_eaten = Condition()
condition_receive_command = Condition()


class Cook(Thread):
    def __init__(self):
        Thread.__init__(self)

    def cook(self):
        print("Cook starts cooking")
        time.sleep(5)
        with condition_order_ready:
            condition_order_ready.notify()

    def run(self):
        # wait for command from waiter
        with condition_new_order:
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
        with condition_new_order:
            condition_new_order.notify()

    def bring_command_to_customer(self):
        print("Waiter brings command to Customer")
        time.sleep(1)
        with condition_receive_command:
            condition_receive_command.notify()

    def cashing(self):
        print("Customer pays for his meal")
        self.cash += 5

    def run(self):
        # wait for customer to arrive and take command
        with condition_customer:
            condition_customer.wait()
        self.bring_command_to_cook()

        # wait for command to be ready
        with condition_order_ready:
            condition_order_ready.wait()
        self.bring_command_to_customer()

        # wait for customer to finish his meal
        with condition_eaten:
            condition_eaten.wait()
        self.cashing()


class Customer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def eat(self):
        print("Customer starts eating")
        time.sleep(5)
        with condition_eaten:
            condition_eaten.notify()

    def run(self):
        # notify waiter of its presence and make command
        with condition_customer:
            condition_customer.notify()

        # wait for food
        with condition_receive_command:
            condition_receive_command.wait()

        self.eat()


if __name__ == '__main__':
    threads = [Cook(), Waiter(), Customer()]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
