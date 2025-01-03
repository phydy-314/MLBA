from ontap_oop.filefactory import FileFactory
from ontap_oop.product import Product

p1=Product(1,"Coca",100)
print(p1)
dataset=[]
dataset.append(p1)
dataset.append(Product(2, "Pepsi", 20))
dataset.append(Product(3, "Sting", 80))
dataset.append(Product(4, "Aqua", 70))
dataset.append(Product(5, "Redbull", 50))
print("Danh sach san pham:")
for product in dataset:
    print(product)

while True:
    id=int(input("Nhap ma: "))
    name=input("Nhap ten: ")
    price=float(input("Nhap gia: "))
    p=Product(id, name, price)
    dataset.append(p)
    ask=input("Nhap tiep khong? (c/k):")
    if ask=="k":
        break
print("Danh sach san pham sau khi nhap")
for product in dataset:
    print(product)
# goi chuc nang chup anh doi tuong xuong o cung
#chup thanh dinh dang json
ff=FileFactory()
ff.writeData("mydataset.json", dataset)



