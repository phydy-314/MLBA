from ontap_oop.testproduct import product

def filter(a,b):
    filter_result=[]
    for i in product:
        if a <= i['price'] <= b:
            filter_result.append(product)
    return filter_result

a=int(input("Nhap so toi thieu:"))
b=int(input("Nhap so toi da:"))

filter_result = filter(a, b)
print("Các sản phẩm có giá từ", a, "đến", b, ":")
for sp in filter_result:
    print(f"- {sp['name']}: {sp['price']}")
