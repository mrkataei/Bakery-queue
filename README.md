# Bakery-queue
The provided code represents a simple bakery system implemented using classes and data structures in Python. It allows users to add bread and customers, display the customer queue and bread stacks, save and load the state of the system.


Here's a breakdown of the code:

The Customer class represents a customer with attributes such as customer ID, barberry count, and lavash count.

The Bread class represents a type of bread with the bread_type attribute.

The CircularQueue class implements a circular queue data structure with methods to enqueue and dequeue items.

The Stack class implements a stack data structure with methods to push and pop items.

The add_bread_to_stack function adds a bread item to the specified bread stack.

The add_customer_to_queue function adds a customer to the customer queue.

The display_customer_queue function displays the contents of the customer queue.

The display_bread_stack function displays the contents of a bread stack.

The save_state function saves the current state of the customer queue and bread stacks to a file.

The load_state function loads the previous state of the customer queue and bread stacks from a file.

The main function is the entry point of the program. It creates instances of the customer queue and bread stacks and provides a menu-based interface for interacting with the bakery system.

To use this code, you can run the main function, which will display a menu with options to perform different actions in the bakery system. Simply enter the corresponding number to select an option.
