import random
number = random(1,100)
n =0
print ("ทาย")
while n!= number:
    n = int(input("ทาย:"))
if n < number:
    print("น้อยเกินไป")
elif n<number:
    print("มากเกินไป")
else:
    print("ถูกต้อง")