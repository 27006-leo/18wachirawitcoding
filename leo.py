print("โปรเเกรมคํานวณคะเเนนรวม")

point1 = int(input("คะเเนนวิชาคณิตศาสตร์"))
point2 = int(input("คะเเนนวิชาอังกฤษ"))
point3 = int(input("คะเเนนวิชาชีวะ"))

total_point = point1 + point2 + point3
print("คะแนนรวม, total_point")
average = total_point / 3
print("คะแนนเฉลี่ยทั้ง3วิชา",average)

if average >=80:
   print("ดีเยี่ยม")
elif average >=60:
   print("ผ่าน")
else:
   print("ควรปรับปรุง")