def KT_SNT(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

number = int(input("Nhap 1 so vao de kiem tra: "))
if KT_SNT(number):
    print(number, "la so nguyen to")
else:
    print(number, "ko phai la so nguyen to")