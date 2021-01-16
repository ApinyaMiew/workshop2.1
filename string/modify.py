string = " Hello World! "

print(string.upper())  # ตัวใหญ่
print(string.lower())  # ตัวเล็ก
print(
    string.strip()
)  # ตัดช่องว่างออก, ไว้ใช้แก้ปัญหาให้ user เวลาcopyข้อมูลมากรอกข้อมูล มันจะมีช่องว่างเพิ่มมาเสมอ
print(string.replace("H", "J"))
print(string.split(","))  # ตัดคำด้วยตัว ","
print(len(string))  # นับรวมช่องว่าง
