dataset=[]
dataset.append({"id":1,"name":"thuoc tri ghe", "price":80})
dataset.append({"id":2,"name":"thuoc tri hoi nach", "price":100})
dataset.append({"id":3,"name":"thuoc tang tu tin", "price":70})

def print_data():
    for product in dataset:
        id=product["id"]
        name=product["name"]
        price=product["price"]
        infor=f"{id}\t{name}\t{price}"
        print(infor)
#xuat toan bo san pham
print_data()

def sort_data():
    for i in range(0,len(dataset)):
        for j in range(i+1, len(dataset)):
            pi=dataset[i]
            pj=dataset[j]
            if pi["price"]>pj["price"]:
                dataset[i]=pj
                dataset[j]=pi
sort_data()
print("Danh sach san pham sau khi sap xep gia tang dan:")
print_data()

#Viet ham them san pham moi
def add_product():
    id=int(input("Nhap ma: "))
    name=input("Nhap ten: ")
    price=float(input("Nhap gia: "))
    product={"id":id,"name":name, "price":price}
    dataset.append(product)
print("Moi ban nhap san pham moi:")
add_product()
print("Danh sach san pham sau khi nhap moi:")
print_data()
dataset[0]={"id":113, "name":"Thuoc cam cum", "price":20}
print("Danh sach san pham sau khi cap nhat:")
print_data()

dataset.pop(1)
print("Danh sach san pham sau khi xoa:")
print_data()

