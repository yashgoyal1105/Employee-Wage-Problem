import random

def check_attendance():
    print("Welcome to Employee Wages computation program in Master Branch")
    status = random.choice([1,0])
    if status == 0:
        return "Absent"
    else:
        return "Present"
    
attendance_status = check_attendance()
print(f"Employee is {attendance_status}")
print(f"Welcome to Employee wage computation")
