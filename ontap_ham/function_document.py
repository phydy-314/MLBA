def firstDegree(a,b):
    """
    Day la phuong trinh bac 1: ax+b=0
    :param a: he so a
    :param b: he so b
    :return: tra ve ba truong hop ket qua
    """
    if a==0 and b==0:
        print("Phuong trinh co vo so nghiem")
    elif a==0 and b !=0:
        print("Phuong trinh vo nghiem")
    else:
        x=-b/a
        print("Nghiem cua phuong trinh = ",x)
print("Phuong trinh bac 1")
a=float(input("Nhap he so a: "))
b=float(input("Nhap he so b: "))
firstDegree(a,b)
