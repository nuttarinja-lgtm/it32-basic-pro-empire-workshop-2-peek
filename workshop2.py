name = str(input("ใส่ชื่อของคุณ :"))
age = int(input("ใส่อายุ :"))
power = int(input("ระดับพละกําลัง :"))
money = int(input("inputเงินติดกระเป๋า :"))

if power >= 7:
    print ("ผ่าน ได้รับตําแหน่งผู้รักษา")
elif money >= 100000:
    print ("ผ่าน ได้รับตําแหน่งกระเป๋าตังค์")
elif age <= 24:
    print ("ผ่าน คุณได้รับตําแหน่งดาวรุ่ง")
else:
    print ("ไปไหนก็ไป")
     
