from CircularQueue import CircularQueue
from Stack import Stack
from util import *

def main():
    max_customers = 10
    max_bread_stack_size = 15

    customer_queue = CircularQueue(max_customers)
    bread_barberry_stack = Stack(max_bread_stack_size)
    bread_lavash_stack = Stack(max_bread_stack_size)

    while True:
        print("1. Add bread")
        print("2. Add customer")
        print("3. Display customer queue")
        print("4. Display bread stacks")
        print("5. Save state")
        print("6. Load state")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bread_type = input("Enter bread type (barberry/lavash): ")
            if bread_type == "barberry":
                add_bread_to_stack(bread_barberry_stack, bread_type)
            elif bread_type == "lavash":
                add_bread_to_stack(bread_lavash_stack, bread_type)
            else:
                print("Invalid bread type.")

        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            barberry_count = int(input("Enter barberry count: "))
            lavash_count = int(input("Enter lavash count: "))
            customer = Customer(customer_id, barberry_count, lavash_count)
            add_customer_to_queue(customer_queue, customer)

        elif choice == "3":
            display_customer_queue(customer_queue)

        elif choice == "4":
            print("Barberry bread stack:")
            display_bread_stack(bread_barberry_stack)

            print("Lavash bread stack:")
            display_bread_stack(bread_lavash_stack)

        elif choice == "5":
            save_state(customer_queue, bread_barberry_stack, bread_lavash_stack)

        elif choice == "6":
            load_state(customer_queue, bread_barberry_stack, bread_lavash_stack)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
