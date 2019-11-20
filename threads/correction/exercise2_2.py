# -----------------------------------------------------------
# Correction of Threads - Exercise 2 Question 2
# 
# Tips:
# - Create a class Counter that can be shared between the Waiter
#   and Customers, so that the Waiter knows when the service is
#   done. 
# - Create an Event to notify the Cook when service is done.
# - Create an OrQueue class that allows the waiter to wait
#   either for a customer to arrive, for a command to be 
#   ready or for a customer to pay. 
#
# Why using threads is relevant for this type of exercise?
# - Lots of "supposedly" I/O operations with time.sleep()
# - Queues and counters can be shared among restaurant
#   actors, allowing them to communicate information on
#   customer commands
# - No CPU consuming operations (or multiprocessing would
#   have been more interesting)
#
#
# (C) 2019 Marion Vasseur, Paris, France
#
# -----------------------------------------------------------

from threading import Thread, Lock, Event
from queue import Queue, Empty
import time
import random


NB_CUSTOMERS = 3  # Number of customers in the restaurant
DISTORT_TIME = 1  # Can accelerate the time
MENU = ["pasta", "lasagna", "pizza", "burrito", "sandwich",
        "salad", "antipasti", "burger"]  # Restaurant menu


queues = {
    "new_customer": Queue(),  # Queue filled when a Customer arrives
    "new_order": Queue(),  # Queue filled when the Cook receives an order
    "order_ready": Queue(),  # Queue filled when the Cook finishes cooking
    "bring_meal": Queue(),  # Queue filled when a Customer receives its meal
    "finish_meal": Queue()  # Queue filled when a Customer finishes eating
}


end_shift_event = Event()  # Event triggered when every customer has left


class Cook(Thread):
    """
        Restaurant cook that waits for commands from waiter and cool them.
    """
    def __init__(self):
        Thread.__init__(self)

    def cook(self, command, customer_id):
        print(f"Cook starts cooking {command} for customer {customer_id}")
        time.sleep(5/DISTORT_TIME)
        queues["order_ready"].put((command, customer_id))

    def run(self):
        while not end_shift_event.isSet():
            try:
                # Cook waits for command from waiter
                command, customer_id = queues["new_order"].get(True, 0.1)
                queues["new_order"].task_done()

                # Cook the ordered meal
                self.cook(command, customer_id)
            except Empty:
                continue


class Waiter(Thread):
    """
        Restaurant waiter that takes command from customers,
        brings them to the cook, brings ready meals to customers
        and makes them pay for their meal.
    """
    def __init__(self, counter):
        Thread.__init__(self)
        self.cash = 0
        self.counter = counter
        self.or_queue = OrQueue(["new_customer",
                                 "order_ready",
                                 "finish_meal"])

    def bring_command_to_cook(self, command, customer_id):
        print(f"Waiter takes command {command} from customer "
              f"{customer_id} and brings it to Cook")
        time.sleep(1/DISTORT_TIME)

        # Waiter tells Cook that there is a new order
        queues["new_order"].put((command, customer_id))

    def bring_command_to_customer(self, command, customer_id):
        print(f"Waiter brings command {command} to customer {customer_id}")
        time.sleep(1/DISTORT_TIME)
        queues["bring_meal"].put(command)

    def cashing(self, command, customer_id):
        print(f"Customer {customer_id} pays 10 euros for his {command}")
        self.cash += 10

    def run(self):
        while self.counter.value > 0:
            # Waiter waits for customer to arrive and take command
            # or waits for command to be ready
            # or waits for customer to finish his meal
            queue_name, args = self.or_queue.get()

            if queue_name == "new_customer":
                self.bring_command_to_cook(*args)
            elif queue_name == "order_ready":
                self.bring_command_to_customer(*args)
            elif queue_name == "finish_meal":
                self.cashing(*args)

        # Waiter informs the cook that service is done
        end_shift_event.set()

        self.or_queue.join()
        print(f"Restaurant made {self.cash} euros.")


class Customer(Thread):
    """
        Restaurant customer that commands something to eat,
        waits for it, eats it and then leaves.
    """
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
        time.sleep(random.randint(1, 8))

        # Customer notifies waiter of its presence and makes command
        queues["new_customer"].put((self.command, self.id))

        # Customer waits for food
        command = queues["bring_meal"].get()
        queues["bring_meal"].task_done()
        self.eat(command)

        # Customer leaves the restaurant
        self.counter.decr()


class Counter:
    """
        Counter value meant to be shared among threads,
        that can be decremented.
    """
    def __init__(self, value):
        self.value = value
        self.lock = Lock()

    def decr(self):
        with self.lock:
            self.value -= 1


class OrQueue:
    """
        Provide a queue that gets the result of the first queue receiving
        an item among a list of queues.
    """
    def __init__(self, queue_names):
        self.or_queue = Queue()
        self.threads = [
            Thread(target=self.get_queue, args=(queue_name, queue))
            for queue_name, queue in queues.items()
            if queue_name in queue_names]
        for thread in self.threads:
            thread.start()

    def get_queue(self, queue_name, queue):
        while not end_shift_event.isSet():
            try:
                args = queue.get(True, 0.1)
                queue.task_done()
                self.or_queue.put((queue_name, args))
            except Empty:
                continue

    def get(self):
        args = self.or_queue.get()
        self.or_queue.task_done()
        return args

    def join(self):
        for thread in self.threads:
            thread.join()
        self.or_queue.join()


if __name__ == '__main__':
    counter = Counter(NB_CUSTOMERS)
    customers = [Customer(i + 1, random.choice(MENU), counter)
                 for i in range(NB_CUSTOMERS)]
    threads = [Cook(), Waiter(counter), *customers]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for queue in queues.values():
        queue.join()
