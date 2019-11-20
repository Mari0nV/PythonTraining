from threading import Thread
from queue import Queue
import time


queues = {
    "new_customer": Queue(),  # Queue filled when a Customer arrives
    "new_order": Queue(),  # Queue filled when the Cook receives an order
    "order_ready": Queue(),  # Queue filled when the Cook finishes cooking
    "bring_meal": Queue(),  # Queue filled when a Customer receives its meal
    "finish_meal": Queue()  # Queue filled when a Customer finishes eating
}


class Cook(Thread):
    """
        Restaurant cook that waits for commands from waiter and cool them.
    """
    def __init__(self):
        Thread.__init__(self)

    def cook(self, command, customer_id):
        print(f"Cook starts cooking {command} for customer {customer_id}")
        time.sleep(5)
        queues["order_ready"].put((command, customer_id))

    def run(self):
        # wait for command from waiter
        command, customer_id = queues["new_order"].get()
        queues["new_order"].task_done()

        # cook
        self.cook(command, customer_id)


class Waiter(Thread):
    """
        Restaurant waiter that takes command from customers,
        brings them to the cook, brings ready meals to customers
        and makes them pay for their meal.
    """
    def __init__(self):
        Thread.__init__(self)
        self.cash = 0

    def bring_command_to_cook(self, command, customer_id):
        print(f"Waiter takes command {command} from customer "
              f"{customer_id} and brings it to Cook")
        time.sleep(1)
        # Waiter tells Cook that there is a new order
        queues["new_order"].put((command, customer_id))

    def bring_command_to_customer(self, command, customer_id):
        print(f"Waiter brings command {command} to customer {customer_id}")
        time.sleep(1)
        queues["bring_meal"].put(command)

    def cashing(self, customer_id):
        print(f"Customer {customer_id} pays for his meal")
        self.cash += 5

    def run(self):
        # Waiter waits for customer to arrive and take command
        command, customer_id = queues["new_customer"].get()
        queues["new_customer"].task_done()
        self.bring_command_to_cook(command, customer_id)

        # Waiter waits for command to be ready
        command, customer_id = queues["order_ready"].get()
        queues["order_ready"].task_done()
        self.bring_command_to_customer(command, customer_id)

        # Waiter for customer to finish his meal
        command, customer_id = queues["finish_meal"].get()
        queues["finish_meal"].task_done()
        self.cashing(customer_id)
        print(f"Restaurant made {self.cash} euros.")


class Customer(Thread):
    """
        Restaurant customer that commands something to eat,
        waits for it, eats it and then leaves.
    """
    def __init__(self, id, command):
        Thread.__init__(self)
        self.id = id
        self.command = command

    def eat(self, command):
        print(f"Customer {self.id} starts eating {command}")
        time.sleep(5)
        queues["finish_meal"].put((command, self.id))

    def run(self):
        # Customer notifies waiter of its presence and make command
        queues["new_customer"].put((self.command, self.id))

        # Customer waits for food
        command = queues["bring_meal"].get()
        queues["bring_meal"].task_done()
        self.eat(command)


if __name__ == '__main__':
    threads = [Cook(), Waiter(), Customer("Toto", "pasta")]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for queue in queues.values():
        queue.join()
