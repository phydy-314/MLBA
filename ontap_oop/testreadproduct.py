from ontap_oop.filefactory import FileFactory
from ontap_oop.product import Product

ff=FileFactory()
dataset=ff.readData("mydataset.json", Product)
print("Danh sach san pham:")
for product in dataset:
    print(product)


def filter_products(dataset, a, b):
    filter_result = []
    for product in dataset:
        if a <= product.price <= b:
            filter_result.append(product)
    return filter_result

a = int(input("Nhap gia toi thieu: "))
b = int(input("Nhap gia toi da: "))

filter_result = filter_products(dataset, a, b)

print(f"Cac san pham co gia tu {a} den {b}:")
for sp in filter_result:
    print(sp)
#Xoa cac san pham co gia be hon x
def remove_products(dataset, x):
    return [product for product in dataset if product.price >= x]

x = int(input("Nhap gia tri x: "))

dataset = remove_products(dataset, x)

print(f"Danh sach san pham sau khi xoa < {x}:")
for product in dataset:
    print(product)