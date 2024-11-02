class Warehouse:
    def __init__(self, products):
        self.products = products

    def __str__(self):
        return "justyna to znaczy co XD"

    def __setitem__(self, key, value):
        self.products[key] = value

    def __getitem__(self, key):
        return self.products[key]

    def __contains__(self, item):
        if item in self.products:
            return True
        return False

    def __eq__(self, other):
        if self.products == other.products:
            return True
        return False

    def __len__(self):
        return len(self.products)


    def __iter__(self):
        return iter(self.products)

products = Warehouse({"apple": 10, "orange": 12, "water": 100})
fruits = Warehouse({"apple": 10, "orange": 12, "water": 100})


print(fruits)

