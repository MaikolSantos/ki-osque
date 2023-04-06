from collections import Counter
from menu import products


def get_product_by_id(id: int):
    if (type(id) != int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type_product: str):
    if (type(type_product) != str):
        raise TypeError("product type must be a str")

    new_products = [
        product
        for product in products
        if product["type"] == type_product
    ]

    return new_products


def add_product(menu: list, **kwargs):
    id = 1

    ids = [
        product["_id"]
        for product in menu
    ]

    if (ids):
        id = max(ids) + 1

    new_product = {"_id": id, **kwargs}

    menu.append(new_product)

    return new_product


def menu_report():

    count = len(products)

    values = [
        product["price"]
        for product in products
    ]

    sum_values = sum(values)

    avg = round(sum_values / count, 2)

    types_products = [
        product["type"]
        for product in products
    ]

    counter_products = Counter(types_products)

    type_most_common = counter_products.most_common()[0][0]

    return f"Products Count: {count} - Average Price: ${avg} - Most Common Type: {type_most_common}"
