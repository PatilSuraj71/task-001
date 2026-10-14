
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Sample values supplied directly
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculate bill
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Electronics after GST = {calculateElectronicsGST(a, b):.2f}")
print(f"Fashion after GST = {calculateFashionGST(c, d):.2f}")
print(f"Food after GST = {calculateFoodGST(e):.2f}")
print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")
