class Product:
    def __init__(self, length=50, code='codetree'):
        self.length = length
        self.code = code

a, b = tuple(input().split())
product1 = Product()
product2 = Product(b, a)

print(f'product {product1.length} is {product1.code}')
print(f'product {product2.length} is {product2.code}')