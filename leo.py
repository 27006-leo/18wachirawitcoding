point1 = int (input("คะเเนนวิชา1: "))
point2 = int (input("คะเเนนวิชา2: "))
point3 = int (input("คะเเนนวิชา3: "))


total_point = point1 + point2 + point3
average = total_point/3
if average < 60:
    print("คะเเนนรวมของคุณ = ", total_point)
    print("คะเเนนเฉลี่ย 3 วิชา = ", average)
    print("ควรปรับปรุง")
elif average < 80:
    print("ผ่าน")



else:



    print("ดีเยี่ยม")

