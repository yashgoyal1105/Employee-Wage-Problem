import random

PER_HOUR_WAGE = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
WORKING_DAYS_PER_MONTH = 20
MAX_WORK_HOURS = 100

class EmployeeWage:
    @staticmethod
    def get_work_hours():
        return random.choice([0, PART_TIME_HOURS, FULL_DAY_HOURS])

    @staticmethod
    def calculate_daily_wage():
        work_hours = EmployeeWage.get_work_hours()
        
        match work_hours:
            case 0:
                daily_wage = 0
                attendance_status = "Absent"
            case 4:
                daily_wage = PER_HOUR_WAGE * PART_TIME_HOURS
                attendance_status = "Part-time"
            case 8:
                daily_wage = PER_HOUR_WAGE * FULL_DAY_HOURS
                attendance_status = "Full-time"
        
        return daily_wage, attendance_status, work_hours
    
    @staticmethod
    def calculate_monthly_wage():
        total_wage = 0
        for _ in range(WORKING_DAYS_PER_MONTH):
            daily_wage, _ , _ = EmployeeWage.calculate_daily_wage()
            total_wage += daily_wage
        return total_wage
    
    @staticmethod
    def calculate_wage_with_condition():
        total_wage = 0
        total_work_hours = 0
        total_working_days = 0
        
        while total_work_hours < MAX_WORK_HOURS and total_working_days < WORKING_DAYS_PER_MONTH:
            daily_wage, _, work_hours = EmployeeWage.calculate_daily_wage()
            total_wage += daily_wage
            total_work_hours += work_hours
            total_working_days += 1
        
        return total_wage, total_work_hours, total_working_days

print("Welcome to Employee Wage Computation Program")

daily_wage, attendance_status, _ = EmployeeWage.calculate_daily_wage()
monthly_wage = EmployeeWage.calculate_monthly_wage()
total_wage, total_hours, total_days = EmployeeWage.calculate_wage_with_condition()

print(f"Employee is {attendance_status}")
print(f"Daily Wage: ₹{daily_wage}")
print(f"Total Monthly Wage: ₹{monthly_wage}")
print(f"Total Wage till condition met: ₹{total_wage}")
print(f"Total Work Hours: {total_hours}")
print(f"Total Working Days: {total_days}")
