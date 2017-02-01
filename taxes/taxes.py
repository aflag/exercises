import re

PRODUCT_TYPE_TAXES = {
    "book": 0,
    "food": 0,
    "medicine": 0
}

PRODUCT_TYPES = {
    "book": [
        "book",
    ],
    "food": [
        "chocolate bar",
        "box of chocolates",
        "chocolates",
    ],
    "medical": [
        "headache pills",
    ]
}

class Product:
    def __init__(self, quantity, name, imported, cost):
        self.quantity = quantity
        self.name = name
        self.imported = imported
        self.cost = cost

    @property
    def taxes(self):
        import_taxes = 0 if not self.imported else 0.05
        return PRODUCT_TYPE_TAXES.get(self.type, 0.1) + import_taxes

    @property
    def price(self):
        return self.cost * (1 + self.taxes)

    @property
    def type(self):
        for type_, values in PRODUCT_TYPES.items():
            if self.name in values:
                return type_
        return "other"


def parse(line):
    quantity, name, cost = re.search(r'^([0-9]+)\s+(.+)\s+at\s+(.+)$', line).groups()
    quantity = int(quantity)

    imported = name.startswith("imported")

    if name.startswith("imported"):
        name = name.replace("imported", "", 1).strip()

    cost = float(cost)

    return Product(quantity, name, imported, cost)


def read_products(text):
    products = []
    for line in text.split('\n'):
        products.append(parse(line))
    return products


def to_str(products):
    result = ""
    taxes = 0.0
    total = 0.0
    for product in products:
        if product.imported:
            template = "{} imported {}: {:.2f}\n"
        else:
            template = "{} {}: {:.2f}\n"
        result += template.format(product.quantity, product.name, product.price)
        taxes += product.price - product.cost
        total += product.price
    result += "Sales Taxes: {:.2f}\n".format(taxes)
    result += "Total: {:.2f}\n".format(total)
    return result


def main():
    products = read_producs(sys.stdin.read())
    print(to_str(products))

if __name__ == "__main__":
    main()
