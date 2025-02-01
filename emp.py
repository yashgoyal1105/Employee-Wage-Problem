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
        daily_wage = PER_HOUR_WAGE * work_hours

        # Determine attendance status
        if work_hours == 0:
            attendance_status = "Absent"
        elif work_hours == PART_TIME_HOURS:
            attendance_status = "Part-time"
        else:
            attendance_status = "Full-time"

        return daily_wage, attendance_status

# Main program
print("Welcome to Employee Wage Computation Program")

# Calculate daily wage and attendance status
daily_wage, attendance_status = EmployeeWage.calculate_daily_wage()

# Output results
print(f"Employee is {attendance_status}")
print(f"Daily Wage: ₹{daily_wage}")