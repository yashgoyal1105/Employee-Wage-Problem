import random

PER_HOUR_WAGE = 20
FULL_DAY_HOURS = 8

class EmployeeWage:

    @staticmethod
    def check_attendance():
        attendance = random.randint(0, 1)
        if attendance == 1:
            return "Present"
        else:
            return "Absent"
        
    def calculate_daily_wage():
        attendance_status = EmployeeWage.check_attendance()
        if attendance_status == "Present":
            daily_wage = PER_HOUR_WAGE * FULL_DAY_HOURS
        else:
            daily_wage = 0
        return daily_wage, attendance_status

print("Welcome to Employee Wage Computation Program")

daily_wage, attendance_status = EmployeeWage.calculate_daily_wage()

print(f"Employee is {attendance_status}")
print(f"Daily Wage: ₹{daily_wage}")