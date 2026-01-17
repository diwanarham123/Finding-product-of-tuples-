tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)

def calculate_product(numbers_tuple):
    product = 1
    for num in numbers_tuple:
        product *= num
    return product

product1 = calculate_product(tuple1)
product2 = calculate_product(tuple2)

print(f"Product of numbers in tuple1: {product1}")
print(f"Product of numbers in tuple2: {product2}")