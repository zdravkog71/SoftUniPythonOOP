class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                self.products.remove(pr)


    def __repr__(self):
        message = ""

        for pr in self.products:
             message = [f"{pr.name}: {pr.quantity}" for pr in self.products]

        return "\n".join(message)