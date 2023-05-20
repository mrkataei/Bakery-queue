from Bread import Bread
from Customer import Customer

def add_bread_to_stack(bread_stack, bread_type):
    bread = Bread(bread_type)
    if bread_stack.is_full():
        print("Bread stack is full. Cannot add more bread.")
    else:
        bread_stack.push(bread)
        print(f"Added a {bread_type} bread to the stack.")

def add_customer_to_queue(customer_queue, customer):
    if customer_queue.is_full():
        print("Customer queue is full. Cannot add more customers.")
    else:
        customer_queue.enqueue(customer)
        print(f"Added customer {customer.customer_id} to the queue.")


def display_customer_queue(customer_queue):
    print("Customer queue:")
    if customer_queue.is_empty():
        print("Queue is empty.")
    else:
        for customer in customer_queue:
            if customer:
                print(f"id {customer.customer_id}, barberry: {customer.barberry_count} , lavash: {customer.lavash_count}")

def display_bread_stack(bread_stack):
    print("Bread stack:")
    if bread_stack.is_empty():
        print("Stack is empty.")
    else:
        for bread in bread_stack:
            if bread:
                print(bread)

def save_state(customer_queue, bread_barberry_stack, bread_lavash_stack):
    with open("bakery_state.txt", "w") as file:
        # Save customer queue
        file.write("Customer Queue:\n")
        while not customer_queue.is_empty():
            customer = customer_queue.dequeue()
            file.write(f"{customer.customer_id},{customer.barberry_count},{customer.lavash_count}\n")

        # Save bread stacks
        file.write("Bread Barberry Stack:\n")
        while not bread_barberry_stack.is_empty():
            bread = bread_barberry_stack.pop()
            file.write(f"{bread.bread_type}\n")

        file.write("Bread Lavash Stack:\n")
        while not bread_lavash_stack.is_empty():
            bread = bread_lavash_stack.pop()
            file.write(f"{bread.bread_type}\n")

    print("State saved successfully.")
    
def load_state(customer_queue, bread_barberry_stack, bread_lavash_stack):
    try:
        with open("bakery_state.txt", "r") as file:
            lines = file.readlines()

            # Load customer queue
            queue_section = False
            for line in lines:
                if line.strip() == "Customer Queue:":
                    queue_section = True
                elif queue_section and line.strip():
                    customer_info = line.strip().split(",")
                    customer_id = customer_info[0]
                    barberry_count = int(customer_info[1])
                    lavash_count = int(customer_info[2])
                    customer = Customer(customer_id, barberry_count, lavash_count)
                    customer_queue.enqueue(customer)

            # Load bread stacks
            barberry_section = False
            lavash_section = False
            for line in lines:
                if line.strip() == "Bread Barberry Stack:":
                    barberry_section = True
                    lavash_section = False
                elif line.strip() == "Bread Lavash Stack:":
                    barberry_section = False
                    lavash_section = True
                elif barberry_section and line.strip():
                    bread_type = line.strip()
                    bread = Bread(bread_type)
                    bread_barberry_stack.push(bread)
                elif lavash_section and line.strip():
                    bread_type = line.strip()
                    bread = Bread(bread_type)
                    bread_lavash_stack.push(bread)

        print("State loaded successfully.")

    except FileNotFoundError:
        print("No saved state found.")
