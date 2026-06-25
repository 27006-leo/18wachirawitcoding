print("คํานวณbmi")

point1 = int(input("นํ้าหนัก"))
point2 = int(input("ส่วนสูง"))

point1 / ( point2 * point1 )
print("ค่านํ้าหนัก",point1,point2)
average = point1 / (point2 * point1)
print("ค่าเฉลี่ยbmi")
if average>=25:
    print("อ้วน")

elif average>=24.9:
    print("นํ้าหนักเกิน")

elif average>=22.9:
    print("ปกติ")

else:
    print("นํ้าหนักน้อย")