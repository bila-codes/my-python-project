class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_items(self, product, qty):
        self.items.append((product, qty))

    def total_bill(self):
        total = 0
        for product, qty in self.items:
            total = total + (product.price * qty)
        return total

    def show_bill(self):
        print("\nYOUR BILL")
        for p, q in self.items:
            print(f"{p.name} x {q} = {p.price * q}")
        print("TOTAL:", self.total_bill())
        print()


class OrderSystem:
    def __init__(self):
        self.products = {}
        self.cart = Order()

    def add_sample_products(self):
        self.products["1"] = Product("1", "Burger", 250)
        self.products["2"] = Product("2", "Pizza", 1200)
        self.products["3"] = Product("3", "Fries", 150)
        self.products["4"] = Product("4", "Cold Drink", 100)

    def show_products(self):
        print("\n--- PRODUCTS ---")
        for p in self.products.values():
            print(f"{p.pid}. {p.name} - {p.price}")
        print("----------------\n")

    def add_to_cart(self):
        self.show_products()

        while True:
            pid = input("Enter product id (done to finish): ")
            if pid == "done":
                break

            if pid in self.products:
                qty = int(input("Quantity: "))
                self.cart.add_items(self.products[pid], qty)
                print("Added to cart!\n")
            else:
                print("Invalid product id!")

    def checkout(self):
        if not self.cart.items:
            print("Cart is empty!\n")
            return

        self.cart.show_bill()
        print("Order Placed Successfully! 🎉\n")
        self.cart = Order()


def main():
    system = OrderSystem()
    system.add_sample_products()

    while True:
        print("\nORDER SYSTEM")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Checkout / Place Order")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.show_products()
        elif choice == "2":
            system.add_to_cart()
        elif choice == "3":
            system.checkout()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()