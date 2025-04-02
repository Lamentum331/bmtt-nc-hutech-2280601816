print("Nhap cac vong van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nCac dong da nhap sau khi chuye thanh in Hoa: ")
for line in lines:
    print(line.upper())
