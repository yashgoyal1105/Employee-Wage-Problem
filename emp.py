import random

PER_HOUR_WAGE = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

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
            case _:
                daily_wage = 0
                attendance_status = "Unknown"

        return daily_wage, attendance_status

print("Welcome to Employee Wage Computation Program")

daily_wage, attendance_status = EmployeeWage.calculate_daily_wage()

# Output results
print(f"Employee is {attendance_status}")
print(f"Daily Wage: ₹{daily_wage}")