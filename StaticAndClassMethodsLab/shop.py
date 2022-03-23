class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        total_value = 0
        for _,value in self.items.items():
            total_value += value
        if total_value < self.capacity:
            if item_name in self.items:
                self.items[item_name] += 1
                return f"{item_name} added to the shop"
            else:
                self.items[item_name] = 1
                return f"{item_name} added to the shop"
        else:
            return f"Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            self.items[item_name] -= amount
            if self.items[item_name] < 0:
                self.items[item_name] += amount
                return f"Cannot remove {amount} {item_name}"
            else:
                return f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))

