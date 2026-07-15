quantity = int(input("จํานวนกี่กระบอก :"))
cost = int(input("ต้นทุนของปืน :"))
sell_price = int(input("ราคาขาย :"))
team_members = int(input("จํานวนคนในทีม :"))

print("ต้นทุน", quantity * cost)
print("รายได้ทั้งหมด", sell_price * quantity)
print("กําไร", (sell_price - cost) * quantity)
print("บอสเอาไปกิน", ((sell_price - cost) * quantity) * 20/100)
print("ลูกน้องแบ่งกัน", (((sell_price - cost) * quantity) - ((sell_price - cost) * quantity) * 20/100)/team_members) 


