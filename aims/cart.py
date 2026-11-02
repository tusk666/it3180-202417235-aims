MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
<<<<<<< HEAD
        print("Calculating total cost with discount...")
        return sum(item.cost for item in self.items)
=======
        return sum(item.cost for item in self.items)*0.8
>>>>>>> a09dcfc118b928d289fb6bf35442134842a0f9d8
    def print_cart(self):
        print("***********************CART***********************")
        print("Ordered Items:")
        for item in self.items:
            print(f"- {item.title} - {item.cost} $")
        print(f"Total cost: {self.total_cost()} $")
        print("***************************************************")