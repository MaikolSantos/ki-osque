from menu import products


def calculate_tab(table: list):
    total = 0

    for item in table:
        for product in products:
            if (item["_id"] == product["_id"]):
                total = total + (product["price"] * item["amount"])

    return {"subtotal": f"${round(total,2)}"}
