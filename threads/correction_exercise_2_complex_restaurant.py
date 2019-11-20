from threading import Thread, Lock, Event
from queue import Queue, Empty
import time
import random

DISTORT_TIME = 100

queues = {
    "new_customer": Queue(),
    "new_order": Queue(),
    "order_ready": Queue(),
    "bring_meal": Queue(),
    "finish_meal": Queue()
}
end_shift_event = Event()
menu = ["pasta", "lasagna", "pizza", "burrito", "sandwich",
        "salad", "antipasti", "burger"]


class Cook(Thread):
    def __init__(self):
        Thread.__init__(self)

    def cook(self, command, customer_id):
        print(f"Cook starts cooking {command} for customer {customer_id}")
        time.sleep(5/DISTORT_TIME)
        queues["order_ready"].put((command, customer_id))

    def run(self):
        while not end_shift_event.isSet():
            # wait for command from waiter
            try:
                command, customer_id = queues["new_order"].get(True, 0.1)
                queues["new_order"].task_done()

                # cook
                self.cook(command, customer_id)
            except Empty:
                continue


class Waiter(Thread):
    def __init__(self, counter):
        Thread.__init__(self)
        self.cash = 0
        self.counter = counter

    def bring_command_to_cook(self, command, customer_id):
        print(f"Waiter takes command {command} from customer "
              f"{customer_id} and brings it to Cook")
        time.sleep(1/DISTORT_TIME)
        # tell cook there is a new order
        queues["new_order"].put((command, customer_id))

    def bring_command_to_customer(self, command, customer_id):
        print(f"Waiter brings command {command} to customer {customer_id}")
        time.sleep(1/DISTORT_TIME)
        queues["bring_meal"].put(command)

    def cashing(self, customer_id):
        print(f"Customer {customer_id} pays for his meal")
        self.cash += 10

    def run(self):
        while self.counter.value > 0:
            # wait for customer to arrive and take command
            command, customer_id = queues["new_customer"].get()
            queues["new_customer"].task_done()
            self.bring_command_to_cook(command, customer_id)

            # wait for command to be ready
            command, customer_id = queues["order_ready"].get()
            queues["order_ready"].task_done()
            self.bring_command_to_customer(command, customer_id)

            # wait for customer to finish his meal
            command, customer_id = queues["finish_meal"].get()
            queues["finish_meal"].task_done()
            self.cashing(customer_id)

        # Waiter informs the cook that service is done
        end_shift_event.set()
        print(f"Restaurant made {self.cash} euros.")


class Customer(Thread):
    def __init__(self, id, command, counter):
        Thread.__init__(self)
        self.id = id
        self.command = command
        self.counter = counter

    def eat(self, command):
        print(f"Customer {self.id} starts eating {command}")
        time.sleep(5/DISTORT_TIME)
        queues["finish_meal"].put((command, self.id))

    def run(self):
        # Customer notifies waiter of its presence and makes command
        queues["new_customer"].put((self.command, self.id))

        # Customer waits for food
        command = queues["bring_meal"].get()
        queues["bring_meal"].task_done()
        self.eat(command)

        # Customer leaves the restaurant
        self.counter.decr()


class Counter:
    def __init__(self, value):
        self.value = value
        self.lock = Lock()

    def decr(self):
        with self.lock:
            self.value -= 1


if __name__ == '__main__':
    nb_customers = 5
    counter = Counter(nb_customers)
    customers = [Customer(i + 1, random.choice(menu), counter)
                 for i in range(nb_customers)]
    threads = [Cook(), Waiter(counter), *customers]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for queue in queues.values():
        queue.join()
