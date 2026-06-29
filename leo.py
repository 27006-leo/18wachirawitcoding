print("ความเร็วรถ")

speed = int(input("ความเร็วรถ"))

if speed <= 80:
    print("ปลอดภัย")
elif speed <= 100:
    print("เตือน")
elif speed <= 120:
    print("เสี่ยงถูกปรับ")
else:
    print("ผิดกฏหมาย")